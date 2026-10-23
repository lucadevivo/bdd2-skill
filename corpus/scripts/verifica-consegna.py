#!/usr/bin/env python3
"""Controlli meccanici sulla soluzione prodotta, prima di consegnarla.

    python3 verifica-consegna.py <soluzione.md>

Non e' un correttore e non da' voti: **stampa un elenco di cose da guardare**. Esiste perche' i
controlli scritti in prosa dentro la skill non scattano da soli — misurato: la regola sulla catena
di contenimento era in `analisi.md` e la skill l'ha ignorata in tre confronti su tre. Gli errori
che questi controlli cercano sono quelli che il benchmark ha visto davvero: omissioni e simboli
inventati, mai errori di sintassi.

I falsi positivi sono voluti: il costo di guardare una riga in piu' e' nullo, quello di consegnare
un vincolo senza realizzazione e' una domanda eliminatoria.
"""
import re
import sys
from pathlib import Path

BASE = {"Stringa", "Intero", "Reale", "Booleano", "Data", "DataOra", "Ora", "Testo",
        "Carattere", "Numerico", "Sequenza", "Insieme"}

# parole della logica del corso: non sono simboli del diagramma
PAROLE = {"ALL", "EXISTS", "and", "or", "not", "if", "then", "SUM", "MAX", "MIN", "AVG",
          "COUNT", "result", "this", "pre", "post", "dove", "sorted", "ALPHA", "sia", "e",
          "effect", "link", "new", "old", "card", "abs"}

TITOLO = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
DOMANDA = re.compile(r"Domanda\s+(\d)", re.I)
ATTRIBUTO = re.compile(r"^\s*[-*]\s+`(\w+)`\s*:\s*(.+?)\s*$")
OPERAZIONE = re.compile(r"^\s*[-*]\s+\*\*(\w+)\s*\(")
VINCOLO = re.compile(r"\[(V\.[\w.]+)\]")
QUANT = re.compile(r"\b(?:ALL|EXISTS)\s+([a-z]\w*(?:\s*,\s*[a-z]\w*)*)")
# un atomo si scrive `Pred(x)` senza spazio; con lo spazio e' prosa italiana
APPLIC = re.compile(r"\b([A-Za-z_]\w*)\(")


def blocchi(righe):
    """(livello, titolo, prima_riga, ultima_riga) per ogni intestazione."""
    teste = [(i, len(m.group(1)), m.group(2)) for i, r in enumerate(righe)
             if (m := TITOLO.match(r))]
    out = []
    for k, (i, liv, tit) in enumerate(teste):
        fine = len(righe)
        for j, lj, _ in teste[k + 1:]:
            if lj <= liv:
                fine = j
                break
        out.append((liv, tit, i, fine))
    return out


def regione_domanda(righe, bl, n):
    """Le righe della Domanda n, dalla sua intestazione a quella della domanda successiva."""
    inizio = fine = None
    for liv, tit, i, _ in bl:
        m = DOMANDA.search(tit)
        if not m:
            continue
        if int(m.group(1)) == n and inizio is None:
            inizio = i
        elif inizio is not None and int(m.group(1)) != n:
            fine = i
            break
    if inizio is None:
        return None
    return righe[inizio:fine if fine else len(righe)]


def sezione(righe, bl, nome, entro=None):
    nome = nome.lower()
    for liv, tit, i, f in bl:
        if re.sub(r"[`*]", "", tit).strip().lower() == nome:
            if entro and not (entro[0] <= i < entro[1]):
                continue
            return righe[i:f]
    return []


def formule(righe):
    """I blocchi recintati: e' li' che stanno le formule."""
    out, dentro, buf = [], False, []
    for r in righe:
        if r.startswith("```"):
            if dentro:
                out.append("\n".join(buf))
                buf = []
            dentro = not dentro
            continue
        if dentro:
            buf.append(r)
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    testo = Path(sys.argv[1]).read_text(encoding="utf-8")
    righe = testo.splitlines()
    bl = blocchi(righe)
    rilievi = []

    def segna(dove, cosa):
        rilievi.append((dove, cosa))

    # un documento parziale (una sola domanda, un'esercitazione di solo diagramma) non ha
    # l'intestazione "Domanda 2": si guarda tutto il file invece di lamentarsi
    d2 = regione_domanda(righe, bl, 2)
    if d2 is None:
        d2, i2 = righe, 0
    else:
        i2 = next(i for liv, tit, i, f in bl if DOMANDA.search(tit) and
                  int(DOMANDA.search(tit).group(1)) == 2)
    entro2 = (i2, i2 + len(d2))
    bl2 = blocchi(d2)

    classi_sez = sezione(d2, bl2, "classi")
    assoc_sez = sezione(d2, bl2, "associazioni")
    gen_sez = sezione(d2, bl2, "generalizzazioni")
    ca_sez = sezione(d2, bl2, "classi associative")
    tipi_sez = sezione(d2, bl2, "specifica dei tipi di dato")
    spec_sez = sezione(d2, bl2, "specifica delle classi")

    # ---- classi, attributi, operazioni del diagramma
    classi, attributi, operazioni, corrente = {}, {}, {}, None
    for r in classi_sez:
        m = TITOLO.match(r)
        if m and len(m.group(1)) >= 3:
            corrente = re.sub(r"[`*]", "", m.group(2)).strip()
            classi[corrente] = []
            continue
        if not corrente:
            continue
        if (a := ATTRIBUTO.match(r)):
            classi[corrente].append(a.group(1))
            attributi[a.group(1)] = a.group(2)
        elif (o := OPERAZIONE.match(r)):
            operazioni.setdefault(corrente, []).append(o.group(1))

    if not classi:
        print("  documento senza sezione `## Classi`: saltati i controlli che dipendono dal\n"
              "  diagramma (tipi, identificazione, operazioni, alfabeto delle formule).\n")

    # ---- 1. tipi non di base senza specifica
    definiti = {m.group(1) for r in tipi_sez
                if (m := re.match(r"^\s*(\w+)\s*:", r)) and m.group(1) not in ("pre", "post")}
    for attr, tipo in attributi.items():
        primo = re.sub(r"[`*]", "", tipo).strip().split()[0].rstrip(",")
        if primo in BASE or primo in definiti or primo in classi:
            continue
        segna("tipi di dato", f"`{attr}: {primo}` — tipo non di base senza specifica fra i tipi di dato")

    # ---- 2. classi senza identificazione
    id_da_assoc = {c for r in assoc_sez if "{id}" in r
                   for c in re.findall(r"\b([A-Z]\w*)\s+`", r)}
    sottoclassi = set()
    for r in gen_sez:
        nomi = re.findall(r"`(\w+)`", r)
        sottoclassi.update(nomi[1:])
    associative = {m.group(1) for r in ca_sez if (m := re.search(r"`(\w+)`", r))}
    for c, attrs in classi.items():
        if c in sottoclassi or c in associative or c in id_da_assoc:
            continue
        blocco = "\n".join(classi_sez)
        i = blocco.find(f"### {c}")
        corpo = blocco[i:blocco.find("\n### ", i + 1)] if i >= 0 else ""
        if "{id}" in corpo:
            continue
        segna("identificazione", f"classe `{c}` senza identificazione")

    # ---- 3. operazioni disegnate senza specifica
    testo_spec = "\n".join(spec_sez)
    for c, ops in operazioni.items():
        for op in ops:
            if not re.search(rf"\b{re.escape(op)}\s*\(", testo_spec):
                segna("operazioni", f"`{c}::{op}()` e' nel diagramma ma non ha specifica "
                                    f"(pre, post, formula) nella Specifica delle classi")

    # ---- 3bis. un nome usato come attributo e come operazione e' una collisione di simboli
    nomi_op = {op for ops in operazioni.values() for op in ops}
    for nome in sorted(nomi_op & set(attributi)):
        segna("alfabeto", f"`{nome}` e' insieme attributo e operazione: in FOL il nome e' un simbolo "
                          f"globale, i due collidono (v. fol.md). Rinominane uno")

    # ---- 4. ogni [V....] dell'analisi arriva alla progettazione
    vincoli_d2 = []
    for liv, tit, i, f in bl:
        if entro2[0] <= i < entro2[1] and (m := VINCOLO.search(tit)):
            vincoli_d2.append(m.group(1))
    # se la progettazione non c'e' (documento di sola analisi) non c'e' niente da controllare
    i6 = next((i for liv, tit, i, f in bl if DOMANDA.search(tit) and
               int(DOMANDA.search(tit).group(1)) in (6, 7)), None)
    coda = "\n".join(righe[i6:]) if i6 is not None else None
    for v in vincoli_d2 if coda is not None else []:
        if v not in coda:
            segna("vincoli", f"`[{v}]` non ricompare dalla Domanda 6 in poi: "
                             f"nessuna realizzazione in SQL")

    # ---- 5. variabili non tipate e 6. simboli fuori alfabeto
    # l'alfabeto e' quello dichiarato nella Domanda 2 **fuori dalle formule** (un simbolo usato
    # solo dentro una formula non e' dichiarato: e' inventato li'), piu' le segnature della D4
    d4 = regione_domanda(righe, bl, 4) or []
    fuori, dentro = [], False
    for r in d2:
        if r.lstrip().startswith("```"):
            dentro = not dentro
        elif not dentro:
            fuori.append(r)
    dichiarati = set(re.findall(r"\w+", "\n".join(fuori) + "\n" + "\n".join(d4)))
    # la specifica dei tipi di dato e quella delle classi sono blocchi recintati, ed e' li' che
    # tipi, campi e operazioni vengono *dichiarati*: un nome a inizio riga seguito da `(` o da `:`
    # e' una dichiarazione, non un uso
    dichiarati |= {m.group(1) for r in d2
                   if (m := re.match(r"^\s*([A-Za-z_]\w*)\s*[:(]", r))}
    dichiarati |= set(classi) | set(attributi) | definiti
    usati = set()
    for f in formule(d2) + formule(regione_domanda(righe, bl, 5) or []):
        for var in {v.strip() for g in QUANT.findall(f) for v in g.split(",")}:
            atomi = re.findall(rf"\b[A-Za-z_]\w*\s*\([^)]*\b{re.escape(var)}\b[^)]*\)", f)
            if not atomi:
                segna("logica", f"variabile `{var}` quantificata ma non legata da nessun atomo — "
                                f"formula: {f.strip().splitlines()[0][:60]}…")
        usati |= set(APPLIC.findall(f))
    for s in sorted(usati - PAROLE - dichiarati) if classi else []:
        segna("alfabeto", f"`{s}(...)` usato nelle formule ma mai dichiarato nella Domanda 2")

    # ---- 7. intestazioni inghiottite da componi.py
    DISEGNO = ("classi", "associazioni", "generalizzazioni", "classi associative",
               "specializzazioni di associazione", "use case", "use-case", "attributi")
    for liv, tit, i, f in bl:
        if re.sub(r"[`*]", "", tit).strip().lower() not in DISEGNO:
            continue
        for liv2, tit2, i2b, _ in bl:
            if i < i2b < f and liv2 > liv:
                pulito = re.sub(r"[`*]", "", tit2).strip()
                if " " in pulito or pulito.lower().startswith(("specifica", "vincol", "tipi",
                                                               "operazioni", "domanda", "note")):
                    segna("consegna", f"`{tit2}` sta dentro `{tit}`: componi.py la toglie dalla "
                                      f"consegna insieme al diagramma — portala a livello ##")

    # ---- 8. le operazioni della Domanda 5 sono quelle della Domanda 8
    # il vocabolario delle operazioni e' quello della Domanda 4: si controlla che le operazioni
    # specificate alla 5 siano realizzate alla 8, che e' il legame che il modulo impone
    d5, d8 = regione_domanda(righe, bl, 5) or [], regione_domanda(righe, bl, 8) or []
    t5, t8 = "\n".join(d5), "\n".join(d8)
    op_d4 = {m.group(1) for f in formule(d4) for r in f.splitlines()
             if (m := re.match(r"^\s+([a-z]\w*)\s*\(", r))}
    for op in sorted(op_d4):
        if re.search(rf"\b{re.escape(op)}\s*\(", t5) and not re.search(rf"\b{re.escape(op)}\s*\(", t8):
            segna("ambito", f"`{op}` specificata alla Domanda 5 ma non realizzata alla Domanda 8")

    # ---- referto
    if not rilievi:
        print("nessun rilievo meccanico. Restano i controlli che una macchina non fa:")
    else:
        larghezza = max(len(d) for d, _ in rilievi)
        for dove, cosa in rilievi:
            print(f"  {dove:<{larghezza}}  {cosa}")
        if any(d == "identificazione" for d, _ in rilievi):
            print("\n  Sull'identificazione: **non aggiungere un surrogato**. Nel concettuale non si\n"
                  "  inventa un identificatore che i requisiti non nominano (v. analisi.md, e la\n"
                  "  Prestazione di QuickHospital): il surrogato nasce nella Domanda 6. Qui guarda solo\n"
                  "  se ne hai schiacciato uno — una catena di contenimento resa con attributi lascia la\n"
                  "  classe piu' interna senza identificazione, ed e' l'errore misurato tre volte su tre.")
        print(f"\n{len(rilievi)} cose da guardare. Poi i controlli che una macchina non fa:")
    print("""  - i contenitori: ogni luogo o collezione nominato dalla traccia e' classe o attributo?
  - la barra laterale: le operazioni di D5 e D8 sono quelle dei requisiti barrati, tutte e sole?
  - il caso vuoto di ogni «solo / tutti / nessun altro»
  - la lunghezza: python3 misura-lunghezza.py <soluzione.md>""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
