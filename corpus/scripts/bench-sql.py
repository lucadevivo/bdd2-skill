#!/usr/bin/env python3
"""Benchmark SQL: confronta le query prodotte con i risultati attesi stampati nelle esercitazioni.

    python3 bench-sql.py <esercitazione.md> <cartella-risposte> [--container bdd2pg]

`cartella-risposte` contiene un file per interrogazione, numerato: `01.sql`, `02.sql`, …
Ogni file è **una sola query**. Il database si ricava dal nome dell'esercitazione (Accademia o
Cielo) e le query si eseguono nel container Docker del corso.

Il metro è quello stampato nel PDF del docente, l'unica verità oggettiva del corso a portata di
mano. Due controlli per interrogazione:

- **righe**: il numero di righe restituite deve essere quello del `(N rows)` atteso;
- **valori**: le parole del risultato atteso che non compaiono nell'output vengono elencate come
  **avviso**, non come bocciatura: l'estrazione del PDF è sporca e non regge un confronto esatto.
  Il verdetto automatico è quello sulle righe; gli avvisi si guardano a occhio.

L'estrazione del PDF spazieggia le lettere («F e r r a r i»): il confronto le ricompone prima.
Il verdetto è per interrogazione, e alla fine c'è il punteggio.
"""
import re
import subprocess
import sys
from pathlib import Path

CONTAINER = "bdd2pg"
NUMERO = re.compile(r"^[ \t]*(\d{1,2})\)[ \t]*$", re.M)
RIGHE = re.compile(r"\(\s*(\d+)\s*\n?\s*rows?\s*\)")
SEPARATORE = re.compile(r"[-\u2212\u2013\u2014]{3,}")
PAROLA = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_]{2,}")
RUMORE = {"rows", "row", "select", "from", "where", "group", "order", "count", "null",
          "true", "false", "quali", "sono", "delle", "degli", "della", "tutti", "tutte",
          "quanti", "quante", "elencare", "dare", "risultato", "ordine", "crescente",
          "decrescente", "distinti", "distinte", "nome", "nomi", "cognome", "cognomi"}


def ricomponi(testo):
    """«F e r r a r i» -> «Ferrari». L'estrazione del PDF spazieggia le lettere."""
    prima = None
    while prima != testo:
        prima = testo
        testo = re.sub(r"(?<=\b\w) (?=\w\b)", "", testo)
    return testo


def attesi(md):
    """{numero: (righe_attese, parole_attese)} dai risultati stampati nell'esercitazione."""
    testo = md.read_text(encoding="utf-8")
    i = testo.find("Risultati Attesi")
    if i < 0:
        sys.exit(f"{md.name}: non contiene i risultati attesi")
    coda = testo[i:]
    tagli = [(m.group(1), m.start(), m.end()) for m in NUMERO.finditer(coda)]
    fuori = {}
    for k, (numero, _, fine) in enumerate(tagli):
        inizio_prossimo = tagli[k + 1][1] if k + 1 < len(tagli) else len(coda)
        blocco = ricomponi(coda[fine:inizio_prossimo])
        righe = RIGHE.search(blocco)
        # il blocco comincia con il testo della domanda e le intestazioni di colonna: i valori
        # veri cominciano dopo la riga di trattini che psql stampa sotto l'intestazione
        separatore = SEPARATORE.search(blocco)
        valori = blocco[separatore.end():] if separatore else blocco
        parole = {p.lower() for p in PAROLA.findall(valori)} - RUMORE
        fuori[int(numero)] = (int(righe.group(1)) if righe else None, parole)
    # l'intestazione e il pie' di pagina delle slide finiscono dentro i blocchi: si riconoscono
    # perche' tornano in quasi tutti, mentre i valori veri stanno in uno solo
    if len(fuori) > 2:
        conta = {}
        for _, parole in fuori.values():
            for p in parole:
                conta[p] = conta.get(p, 0) + 1
        ricorrenti = {p for p, n in conta.items() if n > len(fuori) * 0.5}
        fuori = {k: (r, parole - ricorrenti) for k, (r, parole) in fuori.items()}
    return fuori


def esegui(db, sql, container):
    r = subprocess.run(
        ["docker", "exec", "-i", container, "psql", "-U", "postgres", "-d", db,
         "-A", "-t", "-F", "|", "-v", "ON_ERROR_STOP=1"],
        input=sql, capture_output=True, text=True)
    if r.returncode != 0:
        return None, r.stderr.strip().splitlines()[0] if r.stderr else "errore"
    righe = [r_ for r_ in r.stdout.splitlines() if r_.strip()]
    return righe, None


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    md = Path(sys.argv[1])
    risposte = Path(sys.argv[2])
    container = sys.argv[sys.argv.index("--container") + 1] if "--container" in sys.argv else CONTAINER
    db = "accademia" if "accademia" in md.name.lower() else "cielo"

    prove = attesi(md)
    passate = mancanti = fallite = 0
    print(f"{md.name}\ndatabase: {db}\n")
    for numero in sorted(prove):
        righe_attese, parole_attese = prove[numero]
        f = risposte / f"{numero:02d}.sql"
        if not f.exists():
            print(f"  {numero:>2}  —        risposta mancante")
            mancanti += 1
            continue
        righe, errore = esegui(db, f.read_text(encoding="utf-8"), container)
        if errore:
            print(f"  {numero:>2}  ERRORE   {errore}")
            fallite += 1
            continue
        uscita = ricomponi("\n".join(righe)).lower()
        perse = sorted(p for p in parole_attese if p not in uscita)
        conta_ok = righe_attese is None or len(righe) == righe_attese
        avviso = (f"   [valori da guardare: {', '.join(perse[:5])}"
                  + (" …]" if len(perse) > 5 else "]")) if perse else ""
        if conta_ok:
            print(f"  {numero:>2}  ok       {len(righe)} righe{avviso}")
            passate += 1
        else:
            print(f"  {numero:>2}  DIVERSO  righe {len(righe)} invece di {righe_attese}{avviso}")
            fallite += 1
    totale = passate + fallite + mancanti
    print(f"\npunteggio: {passate}/{totale}"
          + (f"  ({mancanti} senza risposta)" if mancanti else ""))
    return 0 if fallite == 0 and mancanti == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
