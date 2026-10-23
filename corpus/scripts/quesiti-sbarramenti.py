#!/usr/bin/env python3
"""I gambi delle domande degli sbarramenti, senza le opzioni e senza le risposte segnate.

    python3 quesiti-sbarramenti.py <destinazione.md> [n1 n2 ...]

Gli sbarramenti sono l'unico materiale del corpus con una **verita' oggettiva**: 40 domande a
risposta multipla con la risposta corretta segnata dal docente. Non si possono pero' dare a
qualcuno da risolvere cosi' come sono, perche' domanda, opzioni, risposta giusta e analisi degli
errori stanno tutte nella stessa pagina.

Questo script estrae il solo **gambo** di ogni domanda — quello che precede la prima riga
`Risposta (x)` — e ne fa un test **a risposta aperta**: invece di scegliere fra quattro opzioni si
produce la risposta, che e' piu' severo del quiz originale. La correzione resta oggettiva: la
risposta segnata dal docente si ritrova nel file di partenza, cercando la riga `Risposta (x)"` —
la spunta sopravvive all'estrazione come una virgoletta.

Senza numeri estrae tutti i quesiti; con dei numeri (1-40, nell'ordine delle quattro prove)
estrae solo quelli. I 13 con la risposta corretta leggibile come testo — logica, molteplicita',
schema relazionale, SQL — sono: 2 4 7 12 14 15 16 18 19 20 23 34 35.
"""
import re, sys
from pathlib import Path

SBARRAMENTI = Path(__file__).parent.parent / "docente-ufficiale" / "sbarramenti"


def quesiti():
    fuori = []
    for f in sorted(SBARRAMENTI.glob("*.md")):
        righe = f.read_text(encoding="utf-8").splitlines()
        inizi = [i for i, r in enumerate(righe) if re.match(r"^\s*Domanda \d+\s*$", r)]
        for n, i in enumerate(inizi):
            fine = inizi[n + 1] if n + 1 < len(inizi) else len(righe)
            blocco = righe[i + 1:fine]
            stop = next((k for k, r in enumerate(blocco)
                         if re.search(r"Risposta \([a-d]\)", r)), len(blocco))
            gambo = "\n".join(r for r in blocco[:stop] if r.strip())
            gambo = re.sub(r"^\s*\[Risposta corretta.*?\]\s*", "", gambo, flags=re.S).strip()
            fuori.append((f.name[16:26], n + 1, gambo))
    return fuori


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__.strip().splitlines()[2].strip())
    tutti = quesiti()
    scelti = [int(a) for a in sys.argv[2:]] or range(1, len(tutti) + 1)
    testo = ["# Quesiti dagli sbarramenti ufficiali\n",
             "> Domande vere di prove di sbarramento del corso, **senza le opzioni di risposta**:",
             "> si risponde in forma aperta. Dove il testo dice «quale delle seguenti opzioni…»,",
             "> **produci tu la risposta corretta** invece di sceglierla. Dove cita un diagramma che",
             "> qui non compare, rispondi su quello che il testo dice e dichiara cosa ti manca.\n"]
    for k, n in enumerate(scelti, 1):
        prova, num, gambo = tutti[n - 1]
        testo.append(f"## Quesito {k}\n\n```\n{gambo}\n```\n")
    Path(sys.argv[1]).write_text("\n".join(testo), encoding="utf-8")
    print(f"{len(list(scelti))} quesiti -> {sys.argv[1]}")
