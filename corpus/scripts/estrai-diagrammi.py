#!/usr/bin/env python3
"""Estrae i diagrammi dai progetti Visual Paradigm (.vpp) delle fonti.

    python3 estrai-diagrammi.py <cartella-fonti/01-corso> <destinazione>

Per ogni .vpp produce `<nome>.md` (il diagramma in forma testuale: classi, attributi con
tipi e {id}, tabella delle associazioni con le molteplicita', generalizzazioni con i loro
vincoli, note) e `<nome>.puml`. Se accanto al .vpp c'e' l'export PNG fatto dall'autore, lo
copia e lo dichiara: e' la resa fedele, meglio di qualunque rendering nostro.

Il nome viene dal percorso, non dal file: nelle fonti quattro `.vpp` si chiamano tutti
"Travel to the moon.vpp" e sono quattro passi diversi della stessa soluzione.
"""
import re, shutil, sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))
import vpp2uml


def nome_dal_percorso(vpp: Path, radice: Path) -> str:
    """Materia + cartella della soluzione + nome del file, senza le parti ridondanti."""
    parti = list(vpp.relative_to(radice).parts[:-1]) + [vpp.stem]
    prefissi = re.compile(r'^(0\d\s*-\s*|Soluzione\s+)', re.I)
    boilerplate = re.compile(r'^(Diagramma UML delle classi concettuale|'
                             r'Class Diagram\w*|Progettazione)$', re.I)
    pezzi = []
    for p in parti:
        p = re.sub(r'-\d{8}$', '', prefissi.sub("", p).strip(" ,"))
        if not p or boilerplate.match(p):
            continue
        if pezzi and pezzi[-1].casefold() in p.casefold():   # "Accademia" + "Accademia 2"
            pezzi[-1] = p                                    # tiene il piu' specifico
        elif not pezzi or p.casefold() not in pezzi[-1].casefold():
            pezzi.append(p)
    nome = " — ".join(pezzi).replace("_", " ")
    return re.sub(r'\s+', ' ', nome).strip(" —")


def esporta(vpp: Path, radice: Path, dest: Path):
    nome = nome_dal_percorso(vpp, radice)
    testo = vpp2uml.markdown(str(vpp))
    puml = vpp2uml.puml(str(vpp), nome)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / f"{nome}.md").write_text(testo, encoding="utf-8")
    (dest / f"{nome}.puml").write_text(puml, encoding="utf-8")

    png = [p for p in vpp.parent.glob("*.png")]
    copiati = []
    for sorgente in png:
        destinazione = dest / f"{nome} — {sorgente.stem}.png"
        shutil.copy2(sorgente, destinazione)
        copiati.append(destinazione.name)
    return nome, len(testo.splitlines()), copiati


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    radice, dest = Path(sys.argv[1]), Path(sys.argv[2])
    for vpp in sorted(radice.rglob("*.vpp")):
        try:
            nome, righe, png = esporta(vpp, radice, dest)
            print(f"{righe:>4} righe  {len(png)} png  {nome}")
        except Exception as e:
            print(f"   ERRORE su {vpp.relative_to(radice)}: {e}")
