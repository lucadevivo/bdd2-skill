# Correggere una soluzione, non riscriverla

Questo file serve quando il compito è **valutare** una soluzione — tua, dell'utente, o di uno
studente — invece di produrne una. È il mestiere opposto: si legge quello che c'è, si dice cosa
non regge e perché, e **non si consegna una soluzione alternativa**. Chi corregge non riscrive.

Le fonti dei criteri, in ordine di autorevolezza, sono quelle di `corpus.md`:
`STRUTTURA-ESAME.md` per gli errori che chiudono l'esame, `errori.md` per il distillato delle
correzioni vere, il modulo risposte per i campi obbligatori, i diagrammi e le soluzioni ufficiali
per le convenzioni.

## La regola che governa tutto: errore o scelta diversa?

Il corso dice esplicitamente che **non esiste una sola soluzione giusta**. Quindi ogni rilievo va
messo in una di tre caselle, e va detto in quale:

| Casella | Che cos'è | Esempio |
|---|---|---|
| **errore** | contraddice i requisiti, la teoria o una convenzione del corso | identificazione attraverso un estremo `0..*`; un vincolo dell'analisi senza realizzazione |
| **scelta discutibile** | difendibile, ma il corso di solito fa altro, e conviene saperlo | `{disjoint, complete}` su un esito che può non essersi ancora verificato |
| **scelta diversa** | legittima quanto un'altra: non è un rilievo | `Tariffa` come classe invece che come attributo multivalore |

Il tutor chiude una revisione con *«tutto il resto va bene»* dopo sei rilievi su una soluzione
completa: **una soluzione non deve essere perfetta, deve essere priva di errori sostanziali nei
quattro passi eliminatori.** Inventare rilievi per sembrare accurati falsa la correzione tanto
quanto non vederne.

## L'ordine: prima i quattro passi eliminatori

Si comincia da dove si fallisce, non dall'inizio del documento.

| Passo | La domanda da farsi |
|---|---|
| **Domanda 2** | il diagramma è adeguato? ci sono gravi errori di notazione o di modellazione? |
| **Domanda 5** | la logica regge? le variabili sono legate, le precondizioni parlano dei parametri? |
| **Domanda 7** | lo schema e i vincoli sono corretti? ogni vincolo dell'analisi è realizzato? |
| **Domanda 8** | la specifica realizzativa è conforme alle pre/post della Domanda 5? l'SQL funziona? |

Per ognuno si arriva a un verdetto secco — **passa / a rischio / non passa** — con la ragione. Le
altre domande (1, 3, 4, 6) si correggono dopo, e i loro rilievi non sono mai eliminatori.

## I controlli meccanici, che si fanno prima di leggere

Non sono opinioni, quindi si fanno per primi e si riportano come fatti.

1. **Il diagramma, se esiste un ufficiale da confrontare:**
   `python3 scripts/confronta_uml.py <soluzione.md> <diagrammi/ufficiale.md>`. Il verdetto va letto,
   non copiato: nomi diversi per la stessa associazione non sono errori, e lo script lo dice da sé;
   le generalizzazioni con più insiemi le fonde per superclasse, quindi lì va guardato a mano.
2. **L'SQL si esegue.** DDL, trigger e query vanno provati su PostgreSQL (vedi `SKILL.md`), e per i
   trigger serve **almeno una prova costruita per fallire**: un trigger che non scatta mai passa la
   compilazione e non fa niente.
3. **Ogni `[V....]` dell'analisi si ritrova nella Domanda 7** — e la sua realizzazione **tiene**.
   Sono due controlli, non uno. Il primo è binario (il vincolo c'è o non c'è) e si fa scorrendo i
   nomi. Il secondo si fa **leggendo ogni progetto di trigger come codice e costruendoci contro un
   controesempio**: gli errori che si trovano solo così sono `old` scambiato con `new` su un
   `UPDATE`, un evento che nessuno intercetta, un `BEFORE` dove serviva `AFTER`. Una soluzione può
   avere tutti i vincoli realizzati e metà delle realizzazioni bucate — e senza questo controllo la
   Domanda 7 passa a pieni voti.
4. **I diagrammi arrivano nella consegna?** Il ristrutturato è l'input dichiarato della Domanda 7:
   se resta in un file esterno o in un rimando, quella domanda non ha il suo input. Si contano gli
   `<svg>` nel documento finale.
5. **L'ambito delle Domande 5 e 8 corrisponde alla barra laterale.** Operazioni sviluppate che la
   barra non chiede, o requisiti barrati senza operazione, sono due errori diversi e vanno
   distinti.
6. **Ogni variabile di ogni formula è legata, e legata alla sua classe.** Si fa a occhio ma è
   meccanico: per ciascuna formula si scorre l'elenco delle variabili e si controlla che ognuna
   (a) sia quantificata e (b) compaia in un atomo che ne dice la classe — `Letto(l)`, `Ricovero(r)`.
   È il controllo che si dimentica proprio perché sembra ovvio: in un test avversariale, con otto
   errori seminati in una soluzione ufficiale, l'unico non trovato è stato **la sparizione di
   `Letto(l)`** da un vincolo di non sovrapposizione, mentre l'occhio era sulla parte temporale.
   Una variabile non legata rende l'insieme o universale o vuoto, e il vincolo non dice più niente.

   **Attenzione al falso positivo:** una variabile è legata anche quando a tiparla è un **atomo di
   associazione** — in `let_ric(l, r)` la `l` è per forza un letto e la `r` un ricovero. Scrivere
   anche `Letto(l)` è la forma delle soluzioni ufficiali ed è più chiara, ma la sua assenza è una
   *scelta diversa*, non un errore. L'errore vero è la variabile che non compare in **nessun**
   atomo che la vincoli: è il caso dell'insieme `L_occ` citato in `errori.md`, dove la formula non
   nomina mai i letti.

7. **I campi del modulo ci sono?** Per ogni relazione `Derivante da:` e, dove serve, la riga degli
   accorpamenti; per ogni trigger gli eventi, il quando e la funzione in pseudo-codice.

## Che cosa guardare, domanda per domanda

**Domanda 2.** Le cose che i correttori segnano davvero:

- generalizzazione `{complete}` o `{disjoint}` **non giustificata dai requisiti** — il test è: può
  un'istanza di A essere anche di B? Un medico può essere paziente;
- `{complete}` su un esito che al momento della creazione non è ancora determinato;
- identificazione che coinvolge attributi non `[1..1]` o estremi non `1..1`;
- catene di contenimento schiacciate in attributi (perdono l'identificazione);
- un limite **che varia da istanza a istanza** scritto come molteplicità invece che come attributo
  (una capienza diversa per ogni sala). Se il limite è uniforme e la traccia lo enuncia come
  regola, la molteplicità numerica è legittima: è una scelta discutibile, non un errore;
- un dato **derivabile** memorizzato come attributo, riconoscibile dal vincolo che serve a tenerlo
  allineato;
- una classe senza nessuna associazione;
- vincoli in italiano lasciati come segnaposto, o `~ '...'` non sviluppati;
- vincoli esterni che riscrivono ciò che il diagramma già dice (molteplicità, identificazione,
  disjoint/complete in analisi): sono rumore, e vanno segnalati come tali.

**Domanda 5.** L'errore che i correttori nominano per primo è **la variabile non legata alla sua
classe**: un insieme definito senza nominare `Letto(x)` non è «i letti occupati». Poi:
precondizioni su esistenziali generici invece che sui parametri; operazioni che non restituiscono
tutto quello che la segnatura promette; un calcolo rifatto a mano dentro un vincolo invece di
richiamare l'operazione che già lo fa; confini degli intervalli temporali sbagliati; formule che
sul **caso vuoto** dicono il contrario di quello che si voleva.

**Domanda 7.** Vincoli senza realizzazione; `check:` che nominano due relazioni (sono vincoli
esterni travestiti); inclusioni trattate come foreign key; trigger che interrogano la relazione
sbagliata; `BEFORE` dove serviva `AFTER` su somme e conteggi; chiavi surrogate senza `altra chiave`
quando il concettuale aveva un identificatore.

**Domanda 8.** Conformità alle pre/post della Domanda 5 — è il legame che il modulo impone;
transazioni assenti dove due query dipendono l'una dall'altra; livello di isolamento non dichiarato
dove la precondizione è di non-esistenza; query non minime (tabelle inutili nella `FROM`, `GROUP
BY` superflui, calcoli portati fuori dall'SQL): queste ultime non sono gravi, ma vengono notate.

## La forma del referto

```
## Verdetto sui passi eliminatori

| Passo | Esito | Perché |
|---|---|---|
| Domanda 2 | a rischio | la catena Padiglione→Piano→Settore è schiacciata in attributi di Stanza |
| Domanda 5 | passa | |
| Domanda 7 | non passa | [V.Stanza.capienza] non ha nessuna realizzazione |
| Domanda 8 | passa | |

## Errori

1. **[Domanda 7] Il vincolo `[V.Stanza.capienza]` non è realizzato.** Nell'analisi c'è, nello
   schema non compare. *Criterio:* «ogni vincolo esterno dell'analisi deve avere una
   realizzazione» (`errori.md`). *Come si ripara:* trigger `AFTER INSERT OR UPDATE` su `Letto`.

## Scelte discutibili

1. **[Domanda 2] `{complete}` su `Prenotazione`.** Difendibile se si assume che non si registrino
   prenotazioni prima della decisione, ma il corso in un caso identico (Go) mette `{disjoint}` e
   basta.

## Scelte diverse, non rilievi

- `Tariffa` come classe invece che come attributo multivalore: entrambe hanno un precedente
  ufficiale.

## Che cosa è verificato a macchina

- `confronta_uml.py`: 11 classi contro 17, 4 associazioni mancanti (elencate sopra)
- DDL eseguito su PostgreSQL: passa; 3 prove costruite per fallire, tutte fallite nel punto giusto
```

Ogni rilievo porta **dove sta** (la domanda), **il criterio** con la sua fonte, e **come si
ripara** in una riga. Un rilievo senza criterio è un'opinione; un criterio senza fonte non si
distingue da un'invenzione.

## Correggere una soluzione dell'utente

Vale tutto quello che c'è sopra, più due cose.

**Non riscrivere.** Se una parte è sbagliata si dice cosa e perché, e si indica la direzione — non
si consegna la versione giusta, che toglierebbe l'esercizio. L'eccezione è quando l'utente chiede
esplicitamente la soluzione.

**Dire quanto è grave, in termini d'esame.** Non «manca un vincolo» ma «questo, da solo, fa fallire
la Domanda 7». È l'informazione che serve a decidere su cosa tornare, e senza di essa un elenco di
dieci rilievi non dice se il compito era da 18 o da 30.
