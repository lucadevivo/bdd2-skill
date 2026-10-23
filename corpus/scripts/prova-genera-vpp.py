#!/usr/bin/env python3
"""Prova del generatore: rigenera un progetto vero e confronta i modelli, uno per uno.

    python3 prova-genera-vpp.py [progetto-esportato/project.xml]

Legge un `project.xml` esportato da Visual Paradigm, ne ricava la descrizione compatta, la
dà in pasto a `genera-vpp-xml.py` e poi **rilegge il file prodotto con lo stesso lettore**,
confrontando classe per classe, attributo per attributo, associazione per associazione. Se
il generatore perde o storpia qualcosa, il confronto fallisce: è un controllo che può dire
di no.

Non confronta i diagrammi, perché il generatore non li produce: gli elementi arrivano nel
Model Explorer e il diagramma si fa in VP trascinandoceli sopra.
"""
import json, subprocess, sys, tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

QUI = Path(__file__).parent
URI = "http://www.visual-paradigm.com/product/vpuml/modelexporter"
NS = "{" + URI + "}"
PREDEFINITO = Path.home() / "Scrivania/BDD2-vpp-da-esportare/02 - Go/project.xml"


def prop(m, tipo, nome):
    for p in m.findall(f"{NS}ModelProperties/{NS}{tipo}"):
        if p.get("name") == nome:
            return p
    return None


def testo(m, nome):
    p = prop(m, "TextModelProperty", nome)
    if p is None:
        return ""
    v = p.find(f"{NS}StringValue")
    return (v.get("value") or "") if v is not None else ""


def punta_a(m, nome):
    p = prop(m, "ModelRefProperty", nome)
    if p is None:
        return None
    r = p.find(f"{NS}ModelRef")
    return r.get("id") if r is not None else None


def figli(m):
    c = m.find(f"{NS}ChildModels")
    return list(c) if c is not None else []


def leggi(percorso: Path):
    """Riduce un progetto a quello che il generatore sa rappresentare."""
    radice = ET.parse(percorso).getroot()
    nome_di = {e.get("id"): e.get("name") for e in radice.iter(f"{NS}Model") if e.get("id")}
    classi, associazioni, generalizzazioni = {}, [], []
    for m in radice.iter(f"{NS}Model"):
        if m.get("modelType") == "Class":
            classi[m.get("name")] = [(a.get("name"), testo(a, "type"))
                                     for a in figli(m) if a.get("modelType") == "Attribute"]
        elif m.get("modelType") == "Association":
            estremi = [(m.find(f"{NS}{lato}").find(f"{NS}Model")
                        if m.find(f"{NS}{lato}") is not None else None)
                       for lato in ("FromEnd", "ToEnd")]
            if all(e is not None for e in estremi):
                associazioni.append({
                    "nome": m.get("name") or "",
                    "da": nome_di.get(punta_a(estremi[0], "EndModelElement")),
                    "molt_da": estremi[0].get("name") or "",
                    "a": nome_di.get(punta_a(estremi[1], "EndModelElement")),
                    "molt_a": estremi[1].get("name") or "",
                })
        elif m.get("modelType") == "Generalization":
            generalizzazioni.append((nome_di.get(punta_a(m, "from")),
                                     nome_di.get(punta_a(m, "to"))))
    return classi, associazioni, generalizzazioni


def descrizione(classi, associazioni, generalizzazioni):
    per_padre = {}
    for padre, figlia in generalizzazioni:
        per_padre.setdefault(padre, []).append(figlia)
    return {
        "nome": "Prova",
        "classi": classi,
        "associazioni": associazioni,
        "generalizzazioni": [{"padre": p, "figlie": f} for p, f in per_padre.items()],
    }


def confronta(atteso, ottenuto, che_cosa):
    if atteso == ottenuto:
        print(f"  ok   {che_cosa}: {len(atteso)}")
        return True
    print(f"  NO   {che_cosa}: atteso {len(atteso)}, ottenuto {len(ottenuto)}")
    for x in atteso:
        if x not in ottenuto:
            print(f"         manca:  {x}")
    for x in ottenuto:
        if x not in atteso:
            print(f"         in piu: {x}")
    return False


def main(origine: Path):
    classi, associazioni, generalizzazioni = leggi(origine)
    # il generatore non sa fare le classi associative: un'associazione senza nome nel
    # progetto di partenza e' quella, e va esclusa dal confronto
    associazioni = [a for a in associazioni if a["nome"]]
    nomi = set(classi) | {a["nome"] for a in associazioni}
    generalizzazioni = [g for g in generalizzazioni if g[0] in nomi and g[1] in nomi]

    with tempfile.TemporaryDirectory() as tmp:
        spec = Path(tmp) / "spec.json"
        fuori = Path(tmp) / "generato.xml"
        spec.write_text(json.dumps(descrizione(classi, associazioni, generalizzazioni),
                                   ensure_ascii=False), encoding="utf-8")
        subprocess.run([sys.executable, str(QUI / "genera-vpp-xml.py"), str(spec), str(fuori)],
                       check=True)
        c2, a2, g2 = leggi(fuori)

    print(f"\nconfronto con {origine.parent.name}:")
    esiti = [
        confronta(classi, c2, "classi"),
        confronta(sorted(sum(classi.values(), [])), sorted(sum(c2.values(), [])), "attributi"),
        confronta(sorted(map(str, associazioni)), sorted(map(str, a2)), "associazioni"),
        confronta(sorted(generalizzazioni), sorted(g2), "generalizzazioni"),
    ]
    print("\nTUTTO UGUALE" if all(esiti) else "\nCI SONO DIFFERENZE")
    return 0 if all(esiti) else 1


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else PREDEFINITO))
