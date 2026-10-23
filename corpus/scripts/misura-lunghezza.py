#!/usr/bin/env python3
"""Misura una soluzione domanda per domanda e la confronta con la lunghezza di una prova vera.

    python3 misura-lunghezza.py <soluzione.md> [altre.md ...]

Il metro non è un'opinione: viene dalle **sette prove d'esame trascritte** del corpus
(`soluzioni-studenti/*TRASCRIZIONE.md`), svolte in quattro ore e mezza da chi ha seguito il corso.
`TIPICO` è la mediana delle prove complete; `LIMITE` è il tetto oltre il quale non si sta più
rispondendo, si sta scrivendo un trattato — ed è il doppio abbondante del tipico, quindi largo.

Serve perché una soluzione va **ricopiata a mano sul modulo**: 2000 righe non entrano in nessuna
prova, per quanto siano giuste.
"""
import re
import sys
from pathlib import Path

# righe di contenuto per domanda, misurate sulle sette trascrizioni
TIPICO = {1: 18, 2: 103, 3: 7, 4: 24, 5: 25, 6: 24, 7: 81, 8: 43}
LIMITE = {1: 30, 2: 160, 3: 15, 4: 40, 5: 90, 6: 60, 7: 160, 8: 120}

DOMANDA = re.compile(r"^(#+)\s*.*Domanda\s+(\d)", re.I)
CHIUSURA = re.compile(r"^#{1,2}\s+.*(note di lettura|come usarlo|appendice|assunzioni)", re.I)
TITOLO = re.compile(r"^(#{2,6})\s+(.+?)\s*$")

# Le sezioni che `componi.py` toglie dalla consegna: il diagramma le mostra gia', si
# disegnano nel riquadro del modulo e non si ricopiano. Contarle falsava la D6, che risultava 12x il tipico
# mentre due terzi delle righe erano il diagramma in notazione testuale.
# ponytail: l'elenco e' copiato da componi.py invece di importarlo, che tirerebbe dentro
# markdown e uml2png per tre righe di dati.
SEZIONI_NEL_DISEGNO = ("classi", "associazioni", "generalizzazioni", "classi associative",
                       "specializzazioni di associazione", "use case", "use-case",
                       "attributi")


def misura(path):
    corrente, conta, disegno, salto = None, {}, {}, None
    for riga in Path(path).read_text(encoding="utf-8").splitlines():
        t = TITOLO.match(riga)
        if t:
            livello = len(t.group(1))
            titolo = re.sub(r"[`*]", "", t.group(2)).strip().lower()
            if titolo in SEZIONI_NEL_DISEGNO and (salto is None or livello <= salto):
                salto = livello
                continue
            if salto is not None and livello <= salto:
                salto = None
        m = DOMANDA.match(riga)
        if m:
            corrente = int(m.group(2))
            continue
        if CHIUSURA.match(riga):
            corrente = None
            continue
        if salto is not None:
            if corrente and riga.strip():
                disegno[corrente] = disegno.get(corrente, 0) + 1
            continue
        if corrente and riga.strip() and not riga.lstrip().startswith(">"):
            conta[corrente] = conta.get(corrente, 0) + 1
    return conta, disegno


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for path in sys.argv[1:]:
        conta, disegno = misura(path)
        print(f"\n{Path(path).name}")
        print(f"  {'':4} {'righe':>7} {'tipico':>7} {'limite':>7}   verdetto")
        sfori = 0
        for d in range(1, 9):
            n = conta.get(d, 0)
            if not n:
                nota = "solo diagramma: si disegna nel riquadro" if disegno.get(d) else "non risposta"
                print(f"  D{d}   {'—':>7} {TIPICO[d]:>7} {LIMITE[d]:>7}   {nota}")
                continue
            if n > LIMITE[d]:
                verdetto = f"TAGLIARE: {n / TIPICO[d]:.1f}× il tipico"
                sfori += 1
            elif n < TIPICO[d] * 0.4:
                verdetto = "molto corta, controlla che non manchi un pezzo"
            else:
                verdetto = "ok"
            print(f"  D{d}   {n:>7} {TIPICO[d]:>7} {LIMITE[d]:>7}   {verdetto}")
        tot, tipico_tot = sum(conta.values()), sum(TIPICO.values())
        print(f"  tot  {tot:>7} {tipico_tot:>7} {sum(LIMITE.values()):>7}   "
              f"{tot / tipico_tot:.1f}× una prova vera")
        if sfori:
            print(f"  → {sfori} domande oltre il limite: la consegna non è ricopiabile a mano")
    return 0


if __name__ == "__main__":
    sys.exit(main())
