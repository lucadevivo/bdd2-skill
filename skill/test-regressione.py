#!/usr/bin/env python3
"""Fixture di regressione della skill bdd2.

    python3 test-regressione.py [radice-del-corpus]

Tre controlli, tutti a costo zero e senza rete:

1. **Le regole non spariscono.** Ogni riga di `INVARIANTI` è una correzione pagata con un test in
   cieco o con la lettura della teoria: se una riscrittura della skill la cancella, qui fallisce.
   Il testo cercato è una *frase distintiva*, non l'intero paragrafo: si può riformulare intorno,
   non si può togliere il concetto senza accorgersene.
2. **I percorsi citati esistono.** La skill nomina file del corpus: se il corpus si sposta o un
   file cambia nome, la skill manda l'agente a leggere il vuoto.
3. **Il corpus ha le grandezze attese.** 40 tracce, l'OCR delle scansioni, le figure della teoria
   effettivamente richiamate dai markdown.

Esce con codice 1 al primo insieme di errori, elencandoli tutti.
"""
import re
import sys
from pathlib import Path

QUI = Path(__file__).parent
def _corpus_predefinito():
    """Il corpus accanto alla skill (repository pubblico) o quello locale."""
    accanto = QUI.parent / "corpus"
    return accanto if accanto.exists() else Path.home() / "Scrivania/BDD2-corpus-nuovo"


CORPUS = Path(sys.argv[1]) if len(sys.argv) > 1 else _corpus_predefinito()

# (file della skill, frase distintiva come regex, che cosa protegge)
INVARIANTI = [
    ("references/fol.md", r"`attr/3`", "l'alfabeto FOL del modulo d'esame: attr/3 per gli attributi di associazione"),
    ("references/fol.md", r"classe associativa sono .{0,4}`attr/3`",
     "gli attributi di una classe associativa sono attr/3 sui due estremi, non un oggetto-link"),
    ("references/fol.md", r"op/\(n\+2\)", "il predicato delle operazioni di classe"),
    ("references/fol.md", r"«Solo», «soltanto»", "dove va il fatto positivo con «solo/soltanto»"),
    ("references/fol.md", r"vacuità", "la prova della formula sul caso vuoto"),
    ("references/fol.md", r"tipizzazione \*\*fuori\*\*", "legare la variabile alla classe fuori dall'universale"),
    ("references/fol.md", r"smette di esprimerlo",
     "un vincolo che il diagramma esprime si scrive dove il diagramma smette di esprimerlo"),
    ("references/analisi.md", r"per partecipante", "un dato per partecipante sta sulla classe associativa"),
    ("references/analisi.md", r"punti_bianco", "il segnale dei due attributi col nome del ruolo"),
    ("references/analisi.md", r"capienza", "un limite che viene dai dati è un attributo, non una molteplicità"),
    ("references/analisi.md", r"surrogat", "il surrogato tecnico non identifica nell'analisi"),
    ("references/analisi.md", r"## Use case", "il formato testuale unico degli use-case"),
    ("references/progettazione.md", r"vincoli dinamici", "i vincoli dinamici nascono nell'analisi e si realizzano in D6"),
    ("references/errori.md", r"almeno due", "l'inclusione non esprime una molteplicità minima > 1"),
    ("references/errori.md", r"arietà", "il vocabolario non cambia da una domanda all'altra"),
    ("references/errori.md", r"minute", "le pagine di minute valgono solo se puntate"),
    ("SKILL.md", r"barra", "la barra laterale decide l'ambito di D5 e D8"),
    ("SKILL.md", r"proporzioni di una prova vera", "le grandezze misurate di una prova completa"),
    ("SKILL.md", r"## Generalizzazioni", "le sezioni della consegna restano a livello ##, o componi.py se le mangia"),
    ("references/fol.md", r"simbolo globale, non locale",
     "il nome di un attributo di associazione e' globale: due omonimi collidono"),
    ("references/fol.md", r"chiusura transitiva",
     "i vincoli di chiusura transitiva si dichiarano senza formula e si realizzano con WITH RECURSIVE"),
    ("references/progettazione.md", r"generoso di surrogati",
     "in ristrutturazione il surrogato e' la scelta attesa, misurato su Officine 3"),
    ("references/progettazione.md", r"Marca ogni vincolo ristrutturato",
     "X/T accanto al vincolo: la strategia si decide mentre si riscrive"),
    ("references/progettazione.md", r"DEFERRABLE INITIALLY DEFERRED",
     "la molteplicita' minima > 1 vuole un constraint trigger differito"),
    ("references/progettazione.md", r"`\{complete\}` ma non `\{disjoint\}`",
     "gerarchia completa ma non disgiunta: niente discriminatore unico"),
    ("references/fol.md", r"in modo vacuo, e lo si può dimostrare",
     "il corso legge «solo» in modo vacuo: Accademia 8 da' 20 righe, non 6"),
    ("references/sql.md", r"multiplo esatto",
     "il numero di righe atteso smaschera una proiezione di troppo"),
    ("references/sql.md", r"dominio composito",
     "le trappole di plpgsql viste eseguendo"),
    ("references/analisi.md", r"su otto, `<<include>>` ed `<<extend>>` non compaiono",
     "il docente non usa mai include/extend negli use-case: misurato su 8 diagrammi"),
    ("references/analisi.md", r"Un requisito di primo livello per ogni",
     "il raffinamento segue la struttura del testo, non quella del diagramma"),
    ("references/analisi.md", r"parametro che dipende",
     "un parametro che dipende da una sola classe e' un suo attributo, non una classe associativa"),
    ("SKILL.md", r"esercitazioni che vanno in coppia",
     "nelle esercitazioni appaiate la limitazione dei costrutti e' il compito"),
    ("SKILL.md", r"collezione nominata",
     "la collezione nominata dalla traccia e' una classe: il caso Cronologia di TuTubi"),
    ("SKILL.md", r"controllo dei contenitori",
     "il controllo finale sui contenitori: l'errore misurato tre volte su tre"),
    ("SKILL.md", r"budget, che è un vincolo e non un consiglio",
     "il budget di lunghezza per domanda, con la regola di taglio"),
    ("SKILL.md", r"RUNBOOK-ESAME\.md",
     "il runbook dei controlli meccanici per esercitarsi su una traccia"),
    ("references/correzione.md", r"Attenzione al falso positivo",
     "il falso positivo del controllo sulle variabili: l'atomo di associazione tipa"),
    ("references/correzione.md", r"variabile di ogni formula è legata",
     "il controllo meccanico sul legame delle variabili, l'unico errore sfuggito al test avversariale"),
    ("references/correzione.md", r"errore / scelta discutibile / scelta diversa|tre caselle",
     "il protocollo di correzione distingue errore da scelta diversa"),
    ("SKILL.md", r"Chi decide dov'è la barra",
     "la barra la dichiara l'utente: e' l'unico passo senza misura, e governa D5 e D8"),
    ("references/barra.md", r"luminosità colonna per colonna",
     "come si trova la barra da soli, quando non c'e' un utente che la dichiara"),
    ("SKILL.md", r"controlli\.md",
     "il file di lavoro: un passo che non produce niente viene saltato"),
    ("SKILL.md", r"Un livello per volta",
     "il grep del passo zero si fa un livello di autorita' per volta"),
    ("SKILL.md", r"il posto dove ripararlo è la Domanda 2",
     "il simbolo che manca si aggiunge al diagramma, non si inventa nella formula"),
    ("SKILL.md", r"si contraddicono",
     "requisiti contraddittori: nucleo comune, conflitto dichiarato, lettura dei barrati"),
    ("SKILL.md", r"verifica-consegna\.py",
     "i controlli meccanici sulla soluzione, prima di comporre"),
    ("references/analisi.md", r"conta gli stati",
     "gli stati resi a sottoclassi dimensionano la D7: misurato su Deli, 21 relazioni"),
    ("references/progettazione.md", r"va ramificata con un `IF`, non con un `CASE`",
     "plpgsql risolve i campi di new/old alla preparazione dell'espressione, non del ramo"),
]

# grandezze del corpus: (descrizione, glob, minimo atteso)
GRANDEZZE = [
    ("tracce d'esame in PDF", "tracce-esame/*.pdf", 40),
    ("tracce con OCR", "tracce-esame/*.ocr.md", 37),
    ("dispense di teoria", "teoria/*.md", 9),
    ("esercitazioni", "esercitazioni/*.md", 24),
    ("progetti del corso", "progetti/*.md", 16),
    ("diagrammi ufficiali", "diagrammi/*.md", 31),
    ("trascrizioni di svolgimenti", "soluzioni-studenti/*TRASCRIZIONE.md", 7),
    ("script del corpus", "scripts/*.py", 10),
]

RIGA_PERCORSO = re.compile(r"(?:__BDD2_ROOT__/corpus|" + re.escape(str(CORPUS)) + r")([\w./ '\-]*)")
IMMAGINE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def invarianti():
    for rel, pattern, cosa in INVARIANTI:
        f = QUI / rel
        if not f.exists():
            yield f"manca il file della skill: {rel}"
        elif not re.search(pattern, f.read_text(encoding="utf-8")):
            yield f"regola sparita da {rel}: {cosa}  (cercavo /{pattern}/)"


def percorsi():
    for f in [QUI / "SKILL.md", *sorted((QUI / "references").glob("*.md"))]:
        for coda in RIGA_PERCORSO.findall(f.read_text(encoding="utf-8")):
            # la cattura si ferma al primo carattere non di percorso, ma può trascinare
            # gli argomenti di un comando: si tiene la prima parola dopo l'ultimo `/`
            p = (CORPUS / coda.strip().lstrip("/")).as_posix().rstrip("/.,;:")
            # un percorso del corso può contenere spazi (`accademia 3`), ma la cattura può
            # anche aver trascinato gli argomenti di un comando: se il tutto non esiste, si
            # riprova con la parte prima del primo spazio
            if p and not Path(p).exists() and not Path(p.split(" ")[0]).exists():
                yield f"{f.name} cita un percorso che non esiste: {p}"


def grandezze():
    for cosa, glob, minimo in GRANDEZZE:
        n = len(list(CORPUS.glob(glob)))
        if n < minimo:
            yield f"{cosa}: {n} < {minimo} attesi ({glob})"


def figure():
    for md in (CORPUS / "teoria").glob("*.md"):
        for link in IMMAGINE.findall(md.read_text(encoding="utf-8")):
            if link.startswith("http"):
                continue
            if not (md.parent / link).exists():
                yield f"{md.name}: figura richiamata e assente: {link}"


def main():
    if not CORPUS.exists():
        sys.exit(f"corpus non trovato: {CORPUS}")
    errori = []
    for nome, prova in [("regole", invarianti), ("percorsi", percorsi),
                        ("grandezze", grandezze), ("figure", figure)]:
        miei = list(prova())
        print(f"{nome:12} {'OK' if not miei else str(len(miei)) + ' PROBLEMI'}")
        errori += miei
    if errori:
        print()
        for e in errori:
            print(f"  - {e}")
        sys.exit(1)
    print("\ntutto a posto")


if __name__ == "__main__":
    main()
