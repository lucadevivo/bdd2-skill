# Notazione: si produce UML, si legge anche ER

**Regola di output.** La skill produce **sempre e solo il diagramma UML delle classi**.
L'Entity-Relationship apparteneva all'ordinamento vecchio (fino all'A.A. 2023/2024): non va
mai prodotto, né proposto come alternativa valida.

**Regola di input.** Una fonte che mostra un diagramma ER resta utilizzabile. Si legge per il
contenuto, non si imita nella forma: il diagramma va tradotto in UML, tutto il resto del
documento vale invariato.

## Cosa cambia davvero tra le due notazioni

Il drift riguarda **solo il diagramma concettuale**:

| | ER (vecchio) | UML (attuale) |
|---|---|---|
| Contenitore | entità | classe |
| Legame | relationship | associazione |
| Molteplicità | `(min,max)` sull'estremo **opposto** | `min..max` sull'estremo **proprio** |
| Attributi di legame | attributi di relationship | association class |
| Gerarchie | generalizzazione tra entità | generalizzazione tra classi |

**L'inversione di posizione delle molteplicità è la trappola principale.** Leggendo una
soluzione ER, i vincoli di molteplicità vanno ribaltati prima di riportarli in UML.

Restano **identici** nelle due versioni: specifica dei tipi di dato, vincoli esterni in FOL,
diagramma degli use-case, specifica delle operazioni con pre/post, ristrutturazione, schema
relazionale con vincoli, SQL, trigger e politiche di accesso. In un documento di soluzione
questa è la stragrande maggioranza delle pagine.

## Classificazione delle fonti

### UML nativo — fonti primarie, da imitare anche nella forma

- `docente-ufficiale/esami/BD2.Esame.Risposte.UML.pdf` — **modulo risposte ufficiale, versione
  2024-06-05.UML**: definisce le 8 domande della prova, i tempi e le convenzioni di risposta.
  Vedi `STRUTTURA-ESAME.md`. Ha sostituito il facsimile 2020 in ER.

- **il materiale del corso**, scaricabile dalla pagina ufficiale:
  soluzioni ufficiali in `.txt`, progetti `.vpp`, Travel to the Moon (A.1–A.4),
  QuickHospital (soluzione completa, `Class Diagram concettuale.png`)
- `soluzioni-studenti/Appunti di teoria (studente-B).md` — riassunto del
  corso in 29 pagine, interamente UML ("Ristrutturazione del Diagramma delle Classi", zero
  occorrenze di ER). Stesso autore delle soluzioni ER qui sotto: ha aggiornato gli appunti,
  non le soluzioni.
- `docente-ufficiale/syllabus.md` — versione 2024-02-08
- `videolezioni/` — 9 videolezioni SQL (la notazione non entra in gioco)

### Neutro rispetto alla notazione

- `docente-ufficiale/esami/tracce/` — 41 tracce d'esame: **specifiche dei requisiti** in
  italiano, senza diagrammi
- `soluzioni-studenti/studente-A/**/* - Testo.pdf` — testi dei progetti
- `database/{accademia 3,cielo}/*.sql` — schemi PostgreSQL
- `docente-ufficiale/esami/svolgimenti/20200904-...-errori.txt` — errori di un compito da 25
- `docente-ufficiale/progetti/QuickHospital-correzioni_tutor-TRASCRIZIONE.md` — correzioni
  di un tutor, valide in UML tal quale

### Diagrammi ER, resto valido — leggere per FOL, ristrutturazione, schema relazionale, SQL

Il diagramma va riconvertito; il resto del documento si usa così com'è.

- `soluzioni-studenti/studente-A/` — progetti e prove d'esame svolte (testo + soluzione appaiati)
- `soluzioni-studenti/studente-D/` — esercitazioni singole, incluse Officine 3/4 e
  Voli Aerei 3 sulla ristrutturazione
- `soluzioni-studenti/studente-B/` — soluzioni progetti
- `soluzioni-studenti/studente-C/` — 12 soluzioni progetti. Unica fonte per **ecoParks**; per gli
  altri progetti fa da **seconda soluzione indipendente**, utile per non sovradattarsi allo
  stile di un singolo studente.
- `docente-ufficiale/esami/sbarramenti/` — 4 prove a risposta multipla ufficiali **con le
  risposte corrette segnate** (+3 / −3, soglia 18/30). Su ~10 domande, solo 3-4 partono da un
  diagramma ER; le altre sono SQL, alfabeto e semantica FOL, schema relazionale — neutre.
  Il quiz del 2020-06-08 include anche le **spiegazioni** delle opzioni sbagliate.
  Le domande con ER in input restano utili: chiedono la formula FOL che ne dà la semantica,
  la ristrutturazione corretta e la traduzione in schema relazionale, cioè i passi della
  pipeline. Va solo letto il diagramma con le molteplicità nella convenzione ER.
- `docente-ufficiale/progetti/QuickHospital-svolgimento-studente-E.pdf` (trascritto in `-TRASCRIZIONE.md`) — scansione manoscritta

### Escluso

Il corpus non tiene le copie in notazione ER di roba che ha gia' in UML: il syllabus 2016, i
due facsimile del modulo risposte 2020 e il modulo vuoto ridisegnato da uno studente. Il
modulo che vale e' `docente-ufficiale/modulo-risposte-UML-2024-06-05.pdf`.
