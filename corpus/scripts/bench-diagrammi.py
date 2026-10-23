#!/usr/bin/env python3
"""Benchmark dei diagrammi: confronta i diagrammi prodotti con gli ufficiali del docente.

    python3 bench-diagrammi.py <cartella-con-i-diagrammi-prodotti>

Nella cartella ci vuole un file per esercitazione, con uno dei nomi della tabella `UFFICIALI`
(`officine1.md`, `voliaerei1.md`, `universita1.md`, …). Per ognuno esegue `confronta_uml.py`
contro il diagramma ufficiale e riassume in una riga: classi prodotte su ufficiali, associazioni,
e i nomi delle classi mancanti — che sono la cosa che conta, perché è lì che si perdono i punti.

Il confronto è strutturale e grezzo: nomi diversi per lo stesso concetto risultano come
divergenze. La colonna «mancanti» va letta, non sommata.

**Attenzione ai banchi bruciati.** `SKILL.md` e `analisi.md` citano per nome elementi degli
ufficiali di Officine 1, Accademia 2 e Universita' 2: su quelle tre il punteggio e' gonfiato e non
misura piu' niente. Le colonne pulite sono le altre.
"""
import re
import subprocess
import sys
from pathlib import Path

QUI = Path(__file__).parent
DIAGRAMMI = QUI.parent / "diagrammi"

UFFICIALI = {
    "officine1.md": "E.A.1.11 - Officine 1.md",
    "accademia2.md": "E.A.1.10 - Accademia 2.md",
    "accademia1.md": "A.1.4 Accademia 1.md",
    "voliaerei1.md": "Voli Aerei — E.A.1.2 - Voli aerei 1.md",
    "voliaerei2.md": "Voli Aerei — E.A.1.5 - Voli aerei 2.md",
    "universita1.md": "E.A.1.3 - Universita 1.md",
    "universita2.md": "E.A.1.3 - Universita 2.md",
    "esercitazioni1.md": "Esercitazioni universitarie 1.md",
    "officine3.md": "Officine 3.md",
}
BRUCIATE = {"officine1.md", "accademia2.md", "universita2.md"}

CONTA = re.compile(r"classi:\s*(\d+) vs (\d+)\s*\|\s*associazioni:\s*(\d+) vs (\d+)")


def mancanti(uscita):
    dentro, fuori = False, []
    for riga in uscita.splitlines():
        if riga.startswith("## Classi solo in quella ufficiale"):
            dentro = True
            continue
        if dentro:
            if riga.startswith("## "):
                break
            nome = riga.strip()
            if nome and not nome.startswith("("):
                fuori.append(nome)
    return fuori


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    prodotti = Path(sys.argv[1])
    print(f"{'esercitazione':<22} {'classi':>9} {'assoc.':>9}  classi mancanti")
    for nome, ufficiale in UFFICIALI.items():
        f = prodotti / nome
        if not f.exists():
            continue
        r = subprocess.run([sys.executable, str(QUI / "confronta_uml.py"),
                            str(f), str(DIAGRAMMI / ufficiale)],
                           capture_output=True, text=True)
        m = CONTA.search(r.stdout)
        if not m:
            print(f"{nome:<22} confronto fallito: {r.stderr.strip().splitlines()[-1:]}")
            continue
        cp, cu, ap, au = m.groups()
        perse = mancanti(r.stdout)
        marchio = " (banco bruciato)" if nome in BRUCIATE else ""
        print(f"{nome[:-3]:<22} {cp + '/' + cu:>9} {ap + '/' + au:>9}  "
              f"{', '.join(perse) if perse else '—'}{marchio}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
