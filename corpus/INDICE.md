# Indice del corpus BDD2

Mappa della cartella. Ogni riga dice **cosa c'è** e **da dove viene**. Il passaggio di consegne
sulla ricostruzione — trappole comprese — è in `STATO.md`; la regola UML/ER è in `NOTAZIONE.md`;
la struttura della prova scritta è in `STRUTTURA-ESAME.md`.

Tutto il corpus è **markdown**: si legge con Read e si cerca con `grep -ril`. Le uniche cose che
restano PDF sono quelle che il testo non rende — le tracce d'esame e gli svolgimenti manoscritti.

## Le cartelle

| Cartella | Contenuto | Origine |
|---|---|---|
| `teoria/` | le **9 slide** del corso in markdown + 205 PNG delle pagine con figura, in `teoria/figure/<slide>/` | i PDF ufficiali, convertiti con `scripts/converti-pdf.py` |
| `esercitazioni/` | **24** esercitazioni: `E.A.1.x` (analisi), `E.A.3.x` (FOL), `B.2.2.x` (SQL) | i PDF del corso |
| `progetti/` | i **16 progetti**, numerati `01 - Travel to the moon` … `16 - RainAir` | i PDF del corso |
| `soluzioni-ufficiali/` | **12** soluzioni del docente, una per esercizio, con le figure in `soluzioni-ufficiali/figure/` | i 60 `.txt` ufficiali, raggruppati da `scripts/raccogli-soluzioni.py` |
| `diagrammi/` | **31 diagrammi** dei progetti Visual Paradigm in forma testuale + **33 PNG** esportati dall'autore | gli export XML dei 25 progetti, letti da `scripts/converti-xml.py` |
| `tracce-esame/` | le **40 tracce** 2016→2026 in PDF, `INDICE.md` con la scheda di ognuna, **37 `.ocr.md`** e 3 `.md` veri | `scripts/indicizza-tracce.py`, `scripts/ocr-tracce.py` |
| `docente-ufficiale/` | modulo risposte (2 versioni), syllabus, **4 sbarramenti** con le risposte segnate, svolgimenti d'esame, correzioni del tutor | il sito del docente |
| `videolezioni/` | **9 trascrizioni** delle esercitazioni SQL, con i minutaggi | le registrazioni del corso |
| `soluzioni-studenti/` | **18** documenti scritti a macchina di studente-B + **5 trascrizioni** di prove d'esame manoscritte + i diagrammi importabili in Visual Paradigm | sorgenti LaTeX; le trascrizioni sono fatte a mano leggendo i PDF |
| `database/` | `accademia 3` (6 tabelle) e `cielo` (5 tabelle), **verificati caricandoli in PostgreSQL** | il materiale delle esercitazioni |
| `scripts/` | i convertitori e gli strumenti (vedi sotto) | scritti per il corpus |
| `tools/` | `plantuml.jar` per rendere i diagrammi, `pylib/` con la libreria markdown | — |

## Dove cercare cosa

| Cerchi | Vai a |
|---|---|
| la teoria su un costrutto UML | `teoria/A.1 - Analisi dei requisiti mediante UML.md` |
| la forma di un documento di specifica | `teoria/A.2 - Documenti di specifica (specifiche informali).md` |
| sintassi e semantica della FOL | `teoria/A.3` e, per l'uso nell'analisi, `teoria/A.4` |
| la convenzione `sorted` per le operazioni | `teoria/A.4.1 - Definire insiemi ordinati.md` |
| ristrutturazione e traduzione | `teoria/B.3.1 - Progettazione di basi dati relazionali.md` |
| progettazione delle funzionalità (pseudo-codice + SQL immerso) | `teoria/B.3.2 - Progettazione delle funzionalità.md` |
| SQL, DDL e DML | `teoria/B.2.2 - Il linguaggio SQL.md` (180 pagine) |
| **una pipeline completa e ufficiale** | `soluzioni-ufficiali/QuickHospital.md` |
| un diagramma UML ufficiale in forma testuale | `diagrammi/*.md`, con accanto il PNG dell'autore |
| il testo di una traccia d'esame | `tracce-esame/BD2_<data>_<Nome>.pdf` — **il PDF, non l'OCR** |
| come un correttore giudica | `docente-ufficiale/svolgimenti/2020-09-04-SafeOnTheBeach-errori.md` e `docente-ufficiale/progetti/QuickHospital-correzioni-tutor.md` |
| il modulo risposte e i tempi delle 8 domande | `docente-ufficiale/modulo-risposte-UML-2024-06-05.md`, `STRUTTURA-ESAME.md` |
| un esercizio FOL puro risolto | `soluzioni-studenti/(FOL) Dipendenti.md` |
| una prova d'esame svolta per intero | `soluzioni-studenti/2023-01-13-EasyToll-…-TRASCRIZIONE.md` (e Slimmy, CozyRooms, DKLCloud, TimeBank) |
| il ragionamento a voce su una query | `videolezioni/` |

## Gli script

| Script | Fa |
|---|---|
| `converti-pdf.py` | PDF → markdown con PyMuPDF, rendendo a parte le pagine con figura. Rifiuta i PDF di sole immagini |
| `converti-xml.py` | export XML di Visual Paradigm → markdown del diagramma + copia dei PNG dell'autore |
| `genera-vpp-xml.py` | il contrario: descrizione JSON → `project.xml` importabile in VP, **diagramma disegnato compreso** |
| `diagrammi-prove.py` | le descrizioni dei diagrammi delle prove trascritte; le rigenera tutte |
| `prova-genera-vpp.py` | prova di non regressione del generatore: rigenera un progetto vero e riconfronta |
| `indicizza-tracce.py`, `ocr-tracce.py` | l'indice e l'OCR delle 40 tracce |
| `raccogli-soluzioni.py` | i `.txt` di soluzione raggruppati per esercizio |
| `componi.py` | **soluzione in markdown → un unico HTML** con i diagrammi disegnati come SVG |
| `uml2png.py` | solo il diagramma, in PNG o SVG |
| `confronta_uml.py` | confronta due diagrammi in forma testuale e dice cosa manca o diverge |

`componi.py` e `uml2png.py` usano `tools/plantuml.jar`; PyMuPDF sta in `~/.local/venv-bdd2/bin/python`
(Arch blocca `pip --user`).

## Cosa **non** c'è, e perché

- **le soluzioni di studenti in ER**: si leggono, non si imitano (`NOTAZIONE.md`). Le trascrizioni
  fatte sono solo di prove svolte sul modulo UML;
- **le discussioni GitHub**: 47 thread, 14 000 caratteri di contenuto reale in tutto, non
  autorevoli;
- **le copie annotate delle tracce** (`05 - Testo.pdf`): sono gli stessi testi che il corpus ha
  già in versione migliore.
