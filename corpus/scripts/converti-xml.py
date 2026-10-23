#!/usr/bin/env python3
"""Diagrammi UML dagli export XML di Visual Paradigm.

    python3 converti-xml.py <cartella-con-i-progetti-esportati> <destinazione>

Sostituisce la lettura diretta dei `.vpp`: l'XML contiene anche le **generalizzazioni fra
associazioni** (la specializzazione di associazione), che nel `.vpp` non erano risolvibili.

Per ogni diagramma non vuoto produce un markdown nello stesso formato di prima, e copia le
immagini esportate dall'autore.
"""
import re, shutil, sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "{http://www.visual-paradigm.com/product/vpuml/modelexporter}"
MOLTEPLICITA = re.compile(r'^[\d*?.]+\s*\.\.?[.:]?\s*[\d*?]+$|^[\d*]+$')


def testo_proprieta(modello, nome):
    for p in modello.findall(f"{NS}ModelProperties/{NS}StringProperty"):
        if p.get("name") == nome:
            return p.get("value") or ""
    return ""


def riferimento(modello, nome):
    for p in modello.findall(f"{NS}ModelProperties/{NS}ModelRefProperty"):
        if p.get("name") == nome:
            mr = p.find(f"{NS}ModelRef")
            return mr.get("id") if mr is not None else None
    return None


def tipo_attributo(attributo):
    """Visual Paradigm spezza un tipo scritto `Intero > = 0` in type=`Intero >` e
    initialValue=`0`: qui si ricompone come l'autore l'aveva scritto."""
    tipo = valore = ""
    for p in attributo.findall(f"{NS}ModelProperties/{NS}TextModelProperty"):
        v = p.find(f"{NS}StringValue")
        testo = v.get("value") if v is not None else ""
        if p.get("name") == "type":
            tipo = testo or ""
        elif p.get("name") == "initialValue":
            valore = testo or ""
    return f"{tipo} = {valore}" if valore else tipo


def molteplicita(estremo):
    """VP mette la molteplicita' nel nome dell'estremo se l'autore l'ha digitata li',
    nella proprieta' altrimenti. Se ci sono entrambe e discordano, si riportano tutte e due."""
    nome = (estremo.get("name") or "").strip()
    prop = testo_proprieta(estremo, "multiplicity")
    prop = "" if prop in ("Unspecified", "") else prop
    if nome and prop and nome != prop:
        return f"{nome} ({prop})"
    return nome or prop or "?"


def leggi(progetto: Path):
    radice = ET.parse(progetto).getroot()
    per_id = {m.get("id"): m for m in radice.iter(f"{NS}Model")}
    nome = lambda i: (per_id[i].get("name") or "(senza nome)") if i in per_id else "?"
    tipo = lambda i: per_id[i].get("modelType") if i in per_id else None

    diagrammi = []
    for d in radice.iter():
        if not d.tag.endswith("}Diagram"):
            continue
        elementi = [e for e in d.iter()
                    if e.tag.endswith("}Shape") or e.tag.endswith("}Connector")]
        sul_diagramma = {e.get("model") for e in elementi if e.get("model")}
        if not sul_diagramma:
            continue
        diagrammi.append({"nome": d.get("name"), "tipo": d.get("diagramType"),
                          "ids": sul_diagramma})
    return per_id, nome, tipo, diagrammi


def markdown(progetto: Path, titolo: str, diagramma, per_id, nome, tipo):
    ids = diagramma["ids"]
    dentro = lambda t: [i for i in ids if tipo(i) == t]

    L = [f"# {'Diagramma degli use-case' if diagramma['tipo'] == 'UseCaseDiagram' else 'Diagramma UML delle classi'} — {titolo}", ""]
    L += [f"> Fonte: export XML di Visual Paradigm, diagramma «{diagramma['nome']}».", ""]

    classi = sorted(dentro("Class"), key=nome)
    associative = {riferimento(per_id[i], "from"): riferimento(per_id[i], "to")
                   for i in dentro("AssociationClass")}

    if classi:
        tipi_dato = set()
        blocchi = []
        for i in classi:
            righe = []
            for figlio in per_id[i].findall(f"{NS}ChildModels/{NS}Model"):
                if figlio.get("modelType") != "Attribute":
                    continue
                t = tipo_attributo(figlio)
                modificatore = testo_proprieta(figlio, "typeModifier")
                tipi_dato.add(t)
                righe.append(f"- `{figlio.get('name')}`: {t}{' ' + modificatore if modificatore else ''}")
            etichetta = " _(classe associativa)_" if i in associative else ""
            blocchi.append(f"### {nome(i)}{etichetta}\n" + ("\n".join(righe) if righe else "_(nessun attributo)_"))
        if tipi_dato:
            L += ["## Tipi di dato", "", ", ".join(f"`{t}`" for t in sorted(x for x in tipi_dato if x)), ""]
        L += ["## Classi", ""] + [b + "\n" for b in blocchi]

    associazioni = sorted(dentro("Association"), key=nome)
    if associazioni and classi:
        L += ["## Associazioni", "", "| associazione | estremo A | estremo B |", "|---|---|---|"]
        per_associazione = {v: k for k, v in associative.items()}
        for i in associazioni:
            m = per_id[i]
            estremi = []
            for lato in ("FromEnd", "ToEnd"):
                e = m.find(f"{NS}{lato}/{NS}Model")
                if e is None:
                    estremi.append("?"); continue
                estremi.append(f"{nome(riferimento(e, 'EndModelElement'))} `{molteplicita(e)}`")
            decoro = f" _(classe associativa: {nome(per_associazione[i])})_" if i in per_associazione else ""
            L.append(f"| {nome(i)}{decoro} | {estremi[0]} | {estremi[1]} |")
        L.append("")

    generalizzazioni = dentro("Generalization")
    if generalizzazioni:
        L += ["## Generalizzazioni", ""]
        for i in sorted(generalizzazioni, key=lambda x: nome(riferimento(per_id[x], "from"))):
            m = per_id[i]
            padre, figlio = riferimento(m, "from"), riferimento(m, "to")
            vincolo = f"  **{m.get('name')}**" if m.get("name") else ""
            fra = " _(fra associazioni)_" if tipo(padre) == "Association" else ""
            L.append(f"- `{nome(padre)}` generalizza `{nome(figlio)}`{fra}{vincolo}")
        L.append("")

    attori, casi = sorted(dentro("Actor"), key=nome), sorted(dentro("UseCase"), key=nome)
    if attori or casi:
        L += ["## Use case", ""]
        if attori:
            L.append("Attori: " + ", ".join(f"`{nome(i)}`" for i in attori))
        if casi:
            L.append("")
            L.append("Use case: " + ", ".join(f"`{nome(i)}`" for i in casi))
        L.append("")
        for i in associazioni:
            m = per_id[i]
            capi = []
            for lato in ("FromEnd", "ToEnd"):
                e = m.find(f"{NS}{lato}/{NS}Model")
                capi.append(nome(riferimento(e, "EndModelElement")) if e is not None else "?")
            etichetta = f"  ({m.get('name')})" if m.get("name") else ""
            L.append(f"- `{capi[0]}` — `{capi[1]}`{etichetta}")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def converti(cartella: Path, dest: Path):
    progetto = cartella / "project.xml"
    titolo = re.sub(r'^\d+ - ', '', cartella.name)
    per_id, nome, tipo, diagrammi = leggi(progetto)
    dest.mkdir(parents=True, exist_ok=True)
    prodotti = []
    for d in diagrammi:
        suffisso = "" if len(diagrammi) == 1 else f" — {d['nome']}"
        file = dest / f"{titolo}{suffisso}.md"
        file.write_text(markdown(progetto, titolo, d, per_id, nome, tipo), encoding="utf-8")
        prodotti.append((file.name, len(d["ids"])))
    for png in sorted(cartella.glob("*.png")):
        shutil.copy2(png, dest / f"{titolo} — {png.stem}.png")
    return prodotti, len(list(cartella.glob("*.png")))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sorgente, dest = Path(sys.argv[1]), Path(sys.argv[2])
    for cartella in sorted(p for p in sorgente.iterdir() if (p / "project.xml").exists()):
        prodotti, png = converti(cartella, dest)
        for file, quanti in prodotti:
            print(f"{quanti:>3} elementi  {png} png  {file}")
