# BDD2 — skill per Basi di Dati Modulo 2

<p align="center">
  <a href="https://paypal.me/soldyys">
    <img src="https://img.shields.io/badge/☕%20Offrimi%20un%20caff%C3%A8-PayPal-FFDD00?style=for-the-badge&logo=paypal&logoColor=black" alt="Offrimi un caffè su PayPal" height="56">
  </a>
</p>

Skill per agenti AI che risolve esercizi e tracce d'esame di **Basi di Dati, Modulo 2** con la
metodologia del corso.

Scritta in markdown puro, gira su **Codex**, **Claude Code** e qualunque altro agente o chat.

## A cosa serve

Studiare. La usi per vedere il metodo applicato a un esercizio, confrontare la tua soluzione con
una svolta nelle convenzioni che il correttore si aspetta, e capire dove sbagli.

## Integrità accademica

È uno strumento per **prepararsi prima dell'esame**, come un libro di esercizi svolti o un gruppo
di studio. L'esame di Basi di Dati Modulo 2 si sostiene in aula: non è lì che si usa, e non
sostituisce il capire.

L'uso del presente repository è consentito ai soli fini di studio qui descritti. 
Ogni utilizzo difforme ricade sotto l'esclusiva responsabilità dell'utente, ivi compresi i rischi e le conseguenze che ne derivino.

## Cosa risolve

- Raffinamento dei requisiti
- Diagramma UML concettuale + specifiche
- Diagramma degli use-case
- Segnature delle operazioni
- Specifiche delle operazioni in FOL
- Ristrutturazione e domini SQL
- Schema relazionale con vincoli
- Specifiche realizzative

## Requisiti

Il metodo si legge senza installare niente. Questi servono solo agli strumenti di verifica:

| Serve a | Programma | macOS | Linux (Debian/Ubuntu) | Windows |
|---------|-----------|-------|------------------------|---------|
| confronto e consegna | `python3` | preinstallato | `apt install python3` | python.org o WSL |
| disegnare i diagrammi | `java` | `brew install openjdk` | `apt install default-jre` | Adoptium o WSL |
| eseguire l'SQL | `docker` | Docker Desktop | `apt install docker.io` | Docker Desktop |
| leggere la barra delle tracce | `pdftoppm` | `brew install poppler` | `apt install poppler-utils` | `choco install poppler` o WSL |

Su Windows conviene **WSL2**: gli script sono bash con percorsi POSIX.

## Installazione

```bash
git clone https://github.com/lucadevivo/bdd2-skill.git
cd bdd2-skill
```

**Codex** — legge le skill da `~/.codex/skills/`:

```bash
./install.sh            # = ./install.sh codex
```

Poi la richiami con `$bdd2 Risolvi la Domanda 2 di questa traccia`. Per un singolo progetto, copia
`skill/` in `<progetto>/.agents/skills/bdd2/`.

**Claude Code** — attivazione automatica, nessun prefisso:

```bash
./install.sh claude
```

**Altri agenti** (Cursor, Cline, Windsurf, Copilot, Gemini CLI):

```bash
./install.sh altro ~/dove/vuoi/bdd2
```

Aggiungi al file di istruzioni dell'agente (`AGENTS.md`, `.cursorrules`, `CLAUDE.md`, `GEMINI.md`)
una riga tipo: *«Per Basi di Dati Modulo 2, leggi e segui `bdd2/SKILL.md` e il reference indicato
dalla sua tabella»*. In alternativa incolla `skill/SKILL.md` nel contesto quando serve.

**Chat senza filesystem** (ChatGPT, Gemini, Claude via browser): i 7 file markdown stanno in ~40k
token. Incolla `skill/SKILL.md` come istruzioni di sistema e aggiungi solo il reference del compito:

| Compito | File |
|---------|------|
| traccia o progetto completo | `analisi.md` + `progettazione.md` + `fol.md` |
| analisi concettuale (D1–5) | `analisi.md` + `fol.md` |
| solo logica | `fol.md` |
| progettazione (D6–8) | `progettazione.md` |
| esercitazione SQL | `sql.md` |
| cosa conta come errore | `errori.md` |

## Come si usa su una traccia

Le tracce qui raccolte sono prove d'esame **già svolte**: le usi per esercitarti.

Se la traccia ha le **barre verticali nere** nel margine — marcano i requisiti le cui operazioni
vanno sviluppate — vanno passate all'agente **come immagini**, perché quasi tutte le tracce sono
PDF di sole immagini e un modello che riceve solo testo non le vede:

```bash
./scripts/prepara-traccia.sh corpus/tracce-esame/BD2_2023-09-11_CozyRooms.pdf
```

Allega i JPEG, fatti indicare quali requisiti hanno la barra (con le frasi esatte), poi procedi con
le otto domande in ordine: ogni passo usa l'output del precedente.

**Database di prova**

```bash
./scripts/carica-database.sh    # container bdd2pg con accademia e cielo
docker exec bdd2pg psql -U postgres -d accademia -c "select ..."
```

**Diagrammi e consegna:**

```bash
./scripts/scarica-plantuml.sh                    # una volta sola
python3 scripts/uml2png.py mio-diagramma.md      # PNG/SVG del diagramma
python3 scripts/componi.py soluzione.md -o out/  # HTML con i diagrammi dentro
python3 scripts/confronta_uml.py mio.md ufficiale.md
```

## Struttura

```
skill/     SKILL.md + 7 reference: la skill vera e propria
corpus/    il materiale su cui si appoggia
  teoria/            9 dispense in markdown con le figure delle slide
  esercitazioni/     24 esercitazioni, testo e consegna
  progetti/          16 progetti del corso
  soluzioni-ufficiali/   soluzioni del docente per esercizio
  diagrammi/         31 diagrammi UML ufficiali (export Visual Paradigm)
  tracce-esame/      40 tracce 2016–2026 (PDF) con OCR e indice
  docente-ufficiale/ modulo risposte, syllabus, prove di sbarramento, correzioni tutor
  soluzioni-studenti/ prove trascritte dal manoscritto e relativi diagrammi
  database/          i due schemi PostgreSQL (accademia, cielo)
  scripts/           conversione, OCR, generazione diagrammi e i banchi di prova bench-*.py
scripts/   confronto, resa diagrammi, composizione consegna, sincronizza.sh
install.sh installa la skill per Codex, Claude Code o altro
```

`skill/test-regressione.py` verifica che le regole siano al loro posto, i percorsi esistano e il
corpus sia integro. Lanciala dopo ogni modifica.

## Quanto è verificata

Ogni fase della prova è stata confrontata, alla cieca, con materiale del docente (l'agente non
poteva aprire la soluzione):

| Fase | Metro | Esito |
|------|-------|-------|
| SQL | risultati delle 10 esercitazioni | 84/86; i 2 errori erano di lettura del testo |
| Domanda 2 | 6 diagrammi ufficiali | 2 identici, 2 equivalenti, 1 riparato, 1 completo |
| Domanda 6 | 2 ristrutturazioni ufficiali | 14/14 su una, 9/10 sull'altra |
| Domanda 7 | schema di QuickHospital | 16/16 relazioni, più 7 richieste dalle sue foreign key |
| Domande 4–5 | specifiche di Travel to the Moon | stessi side effect, stessa precondizione |
| Domanda 1 | 2 raffinamenti ufficiali | uno identico, uno equivalente |
| Domanda 3 | use-case ufficiale | attori 2/2, use-case 7/7 con una divergenza |
| correzione | 8 errori seminati in una soluzione | 7 trovati, l'ottavo argomentato |

## Materiale di terzi

> Il corpus include materiale didattico del corso — tracce d'esame, soluzioni del docente,
> correzioni del tutor, prove di studenti — raccolto a fini di studio perché la skill ci si
> appoggia per esempi, confronti e criteri di correzione. **Questo materiale appartiene ai
> rispettivi autori**, non è opera mia e non è coperto dalla licenza di questo repository. Se ne
> detieni i diritti e vuoi che venga rimosso, apri una issue o scrivimi: lo tolgo subito.

Restano fuori dal repo per scelta: gli script di raccolta usati una volta, le discussioni di GitHub,
le scansioni manoscritte (restano le trascrizioni), i PDF di slide ed esercitazioni (scaricabili
dalla pagina del corso; qui c'è il testo convertito e, dove serve, la figura della pagina senza piè
di pagina) e `plantuml.jar` (lo scarica lo script quando serve).

## Licenza

Il codice degli script e i documenti scritti per questo repository sono sotto licenza **MIT**
([`LICENSE`](LICENSE)): liberamente riutilizzabili, basta mantenere la nota di copyright. La licenza
copre solo la mia opera, non il materiale di terzi descritto sopra.

## Autore

**Luca De Vivo** — [@lucadevivo](https://github.com/lucadevivo)

Se la skill ti è servita e vuoi offrire un caffè: [paypal.me/soldyys](https://paypal.me/soldyys).
Facoltativo.
