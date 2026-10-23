# Dove trovare cosa

Radice: `__BDD2_ROOT__/corpus/`. **Tutto il corpus è markdown**: si legge con
Read e si cerca con `grep -ril`. Restano PDF solo le cose che il testo non rende — le tracce
d'esame e gli svolgimenti manoscritti.

Tre file di orientamento nella radice: `INDICE.md` (la mappa completa), `NOTAZIONE.md` (la regola
UML/ER e la classificazione delle fonti), `STRUTTURA-ESAME.md` (le 8 domande, i tempi, i passi
eliminatori).

## Per trovare un esempio di un artefatto

| Cerchi | Vai a |
|---|---|
| pipeline completa e ufficiale, dall'analisi alle operazioni | `soluzioni-ufficiali/QuickHospital.md` |
| specifiche di classe e di use-case con FOL | la stessa, sezioni «Analisi»; oppure `soluzioni-ufficiali/Travel to the moon.md`, che ha side effect con `ALPHA` e sommatorie |
| **se QuickHospital è il compito** e non puoi aprirlo | forma degli artefatti: `teoria/A.2`, `teoria/B.3.1`, `teoria/B.3.2` e i template dentro `references/`; concettuale gemello: `soluzioni-ufficiali/E.A.1.11 - Officine 1.md`; ristrutturato: `diagrammi/Officine 3.md` (forma `X_isa_Y`, surrogati); use-case e operazioni: `soluzioni-ufficiali/Travel to the moon.md` |
| raffinamento dei requisiti | `soluzioni-ufficiali/E.A.1.2 - Voli aerei 1.md`, `E.A.1.3 - Università 1.md`, `Esercitazioni universitarie 1.md` |
| diagramma UML in forma testuale | `diagrammi/*.md` — 31 file, dagli export XML dei progetti del docente |
| l'immagine dello stesso diagramma | `diagrammi/*.png`, esportata dall'autore: fedele al 100% |
| schema relazionale con vincoli | `soluzioni-ufficiali/QuickHospital.md`, sezione della Domanda 7 |
| specifiche realizzative (pseudo-codice + SQL immerso) | la stessa, Domanda 8; e `teoria/B.3.2` |
| ristrutturazione e domini SQL | `soluzioni-ufficiali/E.A.1.11 - Officine 1.md`, `teoria/B.3.1` |
| esercizio FOL puro risolto | `soluzioni-studenti/(FOL) Dipendenti.md` |
| una prova d'esame svolta per intero | `soluzioni-studenti/2023-01-13-EasyToll-svolgimento-TRASCRIZIONE.md` (poi Slimmy, CozyRooms, DKLCloud, TimeBank) |
| riassunto compatto di tutto il corso | `soluzioni-studenti/Appunti di teoria (studente-B).md`, 29 pagine, UML |

**Se stai svolgendo un esercizio, non aprire la sua soluzione.** Vale in particolare per
QuickHospital, che questa tabella indica come esempio di forma: se il compito è proprio quello,
cerca la forma altrove.

Gli esempi dentro i reference della skill seguono una regola precisa, che vale la pena conoscere
per sapere di cosa fidarsi:

- gli esempi che mostrano **come si scrive** un artefatto — la struttura del diagramma, la
  notazione dello schema relazionale, la sintassi FOL — sono su un dominio inventato (una
  biblioteca: `Libro`, `Copia`, `Prestito`, `Lettore`, `Sede`), che non corrisponde a nessun
  esercizio del corso
- gli esempi che mostrano **come si decide** — quando una generalizzazione è giustificata, quando
  un dato va derivato — sono anch'essi su quel dominio, e apposta: un esempio di decisione preso
  da un esercizio reale ne regalerebbe la soluzione
- le **citazioni** in `errori.md` e i fatti sui database in `sql.md` mantengono invece i nomi
  originali, perché sono prove e non esempi: alterarli li renderebbe falsi

Per cercare un concetto si parte dalla teoria, che è tutta in markdown:

```bash
grep -ril "insiemi ordinati" __BDD2_ROOT__/corpus/teoria/
```

## Tracce d'esame e progetti

**40 tracce ufficiali, 2016→2026**, in `tracce-esame/`, nominate `BD2_<data>_<Nome>.pdf`.
`tracce-esame/INDICE.md` le elenca tutte con data, sistema, pagine e note.

**Sono PDF di sole immagini** (3 su 40 hanno un livello di testo): si leggono con Read a pagine
(`pages: "1"`), non con `pdftotext`. E vanno lette come immagini comunque, perché i requisiti da
sviluppare nelle Domande 5 e 8 sono marcati da una **barra verticale nera nel margine sinistro**,
che nel testo non c'è.

Accanto a ogni traccia c'è un `<nome>.ocr.md`: **serve a cercare, non a studiare.** È un OCR
(somiglianza misurata 99,7% / 99,2% / 80,5% sulle tre tracce di cui esiste il testo vero) e in
questo corso una parola sbagliata cambia una molteplicità. Trovata la traccia, si apre il PDF.

I **16 progetti del corso**, in `progetti/`, sono il modello diretto delle tracce d'esame: la
pagina del corso dice che l'esame consiste in *"una specifica dei requisiti testuale del tipo di
quelle disponibili nella sezione Progetti"*. Se l'utente si prepara all'esame, sono la palestra
giusta.

**Cinque prove d'esame svolte** sono state trascritte a mano dagli originali manoscritti e stanno
in `soluzioni-studenti/`: EasyToll 2023-01-13 e Slimmy 2023-01-30 (tutte e 8 le domande),
CozyRooms 2023-09-11, DKLCloud 2024-01-16 (parziale), TimeBank 2024-04-03 (tutte e 8). Non sono
ufficiali e **nessuno le ha corrette**: si usano per vedere come si compila il modulo e quanto
si riesce a scrivere nei tempi, mai come autorità. Gli errori dei loro autori sono riportati come
sono, e le note di lettura in fondo a ogni trascrizione li segnalano.

## Teoria del corso

In `teoria/`, un markdown per slide, con le pagine che contengono figure rese come PNG in
`teoria/figure/<slide>/`:

- `A.1` UML nell'analisi concettuale — classi, associazioni, molteplicità, association class,
  identificazione, generalizzazione, operazioni, specializzazioni, use-case
- `A.2` Documenti di specifica — la forma di tutti gli artefatti dell'analisi
- `A.3` FOL — sintassi e semantica
- `A.4` FOL nell'analisi concettuale — alfabeto, semantica del diagramma, vincoli esterni,
  specifiche delle operazioni
- `A.4.1` Definire insiemi ordinati — la convenzione `sorted` per le operazioni che restituiscono
  una sequenza
- `B.1` Progettazione: introduzione e modello relazionale
- `B.2.2` Il linguaggio SQL (180 pagine, DDL e DML)
- `B.3.1` Progettazione di basi dati relazionali — ristrutturazione e traduzione
- `B.3.2` Progettazione delle funzionalità

Manca la Parte I (introduzione, ciclo di vita del software): non è materiale d'esame.

Le **24 esercitazioni** stanno in `esercitazioni/` (`E.A.1.x` analisi, `E.A.3.x` FOL, `B.2.2.x`
SQL) e le **12 soluzioni ufficiali** in `soluzioni-ufficiali/`.

## Videolezioni SQL

`videolezioni/`, 9 lezioni trascritte con i minutaggi (35 000 parole): Accademia 4-8 e Cielo 1-4,
dalle interrogazioni su singola tabella agli outer join e agli annidamenti.

Contengono le motivazioni e gli errori tipici commentati a voce dal docente, che nei PDF non ci
sono. Sono trascrizioni automatiche: i nomi propri sono storpiati, il senso è integro.

## Database di esempio

In `database/`, verificati caricandoli davvero in PostgreSQL con `ON_ERROR_STOP=1`:

- `accademia 3/` — personale universitario, progetti, WP, attività, assenze. 6 tabelle, 69 righe.
  È il database delle esercitazioni Accademia 4-8.
- `cielo/` — voli, compagnie, aeroporti. 5 tabelle, 35 righe. Esercitazioni Cielo 1-4.
  `constraints.sql` contiene `-- no constraints.`: è corretto, non è un file rotto.

Ordine di caricamento: `domains-tables.sql`, `constraints.sql`, `data.sql`.

## Criteri di correzione

Quattro fonti, in ordine di autorevolezza:

1. `STRUTTURA-ESAME.md` — la lista ufficiale degli errori che chiudono l'esame
2. `docente-ufficiale/svolgimenti/2020-09-04-SafeOnTheBeach-errori.md` — un compito valutato 25,
   con la distinzione fra errori gravi e non gravi; lo svolgimento a cui si riferisce è
   trascritto accanto, e i rilievi sono richiamati nel punto esatto in cui l'errore si trova
3. `docente-ufficiale/progetti/QuickHospital-correzioni-tutor.md` — correzioni di un tutor su una
   soluzione, con le regole ricavate
4. `docente-ufficiale/sbarramenti/` — 4 prove a risposta multipla con le risposte corrette
   segnate (si riconoscono cercando `Risposta (x)"`). Non rispecchiano il formato d'esame
   attuale, ma sono l'unico materiale con una verità oggettiva: utili per autovalutazione su
   semantica dei diagrammi, FOL e SQL

Il distillato è in `errori.md`.

## Gli strumenti

In `scripts/`, tutti da lanciare con `python3` (PyMuPDF sta in `~/.local/venv-bdd2/bin/python`):

| Script | Fa |
|---|---|
| `componi.py` | **la consegna**: soluzione in markdown → un unico HTML con i diagrammi come SVG |
| `uml2png.py` | solo il diagramma, in PNG o SVG |
| `confronta_uml.py` | confronta due diagrammi in forma testuale e dice cosa manca o diverge |
| `converti-xml.py` | export XML di Visual Paradigm → markdown del diagramma |
| `genera-vpp-xml.py` | descrizione JSON → progetto importabile in Visual Paradigm, **diagramma disegnato compreso** |

`componi.py` e `uml2png.py` rendono i diagrammi con `tools/plantuml.jar`, che sta nel corpus: è
l'unico modo di disegnarli offline.

## I diagrammi ufficiali si rigenerano, non si scrivono a mano

`diagrammi/` è prodotto da `scripts/converti-xml.py` a partire dagli **export XML** che stanno in
`~/Scrivania/BDD2-vpp-da-esportare/` (un `project.xml` per progetto, più i PNG dell'autore). Non
modificare quei markdown a mano: si rigenerano.

L'XML risolve quello che il `.vpp` non permetteva di leggere — in particolare le
**generalizzazioni fra associazioni** (la specializzazione di associazione: i ruoli distinti,
per esempio `bianco`/`nero` in Go). Se un `.md` sembra mancarne una, si guarda il PNG accanto.

Due trappole del formato, per chi ci mette le mani: la molteplicità sta nel **nome** dell'estremo
(la proprietà `multiplicity` resta `Unspecified`), e un tipo scritto `Intero > = 0` viene spezzato
da VP in `type="Intero >"` più `initialValue="0"`.
