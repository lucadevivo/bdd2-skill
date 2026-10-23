# Cosa i correttori considerano errore

Distillato da cinque fonti: la pagina ufficiale del corso, un compito valutato 25 con l'elenco
degli errori, le correzioni di un tutor su una soluzione di progetto, i quiz ufficiali con le
risposte corrette, e le sette prove di studenti trascritte dal manoscritto — queste ultime non
corrette da nessuno, e valgono per gli errori che *ricorrono*, non come verità. I percorsi sono in
`corpus.md`.

## Gli errori che chiudono l'esame

La pagina del corso li elenca esplicitamente, e avverte che la lista **non è esaustiva**:

- un diagramma UML delle classi concettuale **inadeguato o con gravi errori**
- errori sostanziali **nell'uso della logica**
- errori sostanziali **nello schema relazionale** o nell'implementazione dei vincoli associati
- errori sostanziali **nella specifica realizzativa** degli use-case (per esempio nel codice SQL)

L'orale parte dalla discussione dello scritto e **non può sanarli**: può concludersi
immediatamente con un'insufficienza.

Questo cambia il modo di lavorare su questi quattro passi. Meglio una risposta più breve e
sicuramente corretta che una ricca e traballante. Se un requisito è ambiguo, modella
l'interpretazione più difendibile e annota l'assunzione, invece di aggiungere struttura fragile.

## Modellazione

**La generalizzazione completa e disjoint va giustificata dai requisiti.** Il test è: un'istanza
di A potrebbe mai essere anche di B?

> Non userei una generalizzazione completa tra *Paziente* e *Medico*, poiché un medico potrebbe
> sempre trovarsi ad essere paziente.
>
> Le IS-A e le generalizzazioni vanno sempre usate in modo oculato, cercando di capire quali
> conseguenze sul sistema ha il loro utilizzo rispetto ciò che dicono i requisiti. In questo caso
> né i requisiti, né il senso comune dicono che un paziente non possa essere medico e viceversa,
> per cui non utilizziamo una generalizzazione.

**Meglio un attributo in più che un vincolo in più**, quando il vincolo nasce solo per compensare
un dato che la traccia non ha chiesto:

> In questi casi è sempre meglio introdurre dati ulteriori, purché ragionevoli, invece che
> introdurre vincoli che potrebbero cozzare con le business rules del sistema. Nel caso in
> questione, con ogni probabilità chi ha raccolto i requisiti ha semplicemente dimenticato di
> richiedere anche l'orario della prestazione.

**I requisiti si leggono in modo critico.** Dati ovviamente necessari vanno modellati anche se
non scritti; e ogni vincolo ha conseguenze pratiche da valutare:

> I requisiti vanno anche letti in modo critico, usando il buon senso per capire quali dati sono
> di interesse, anche nel caso in cui non sono resi espliciti. Inoltre, pensi sempre anche alle
> conseguenze economiche delle scelte di modellazione.

**Vincoli attesi anche quando la traccia non li nomina:**

- non sovrapposizione temporale (due ricoveri dello stesso paziente, due prenotazioni della
  stessa risorsa)
- coerenza delle date rispetto alla data di nascita, o rispetto alle date del contenitore
- identificatori per le entità che vengono contate o assegnate — se i letti si assegnano, i letti
  hanno un numero

## Logica

**Legare ogni variabile alla sua classe.** È l'errore che i correttori segnalano per primo:

> Quando definisce l'insieme `L_occ` dei *Letti* occupati, non fa mai riferimento ai *Letti*
> nella formula, per cui quell'insieme è l'insieme universo se esistono `d, dr` tali che la
> formula è vera, o l'insieme vuoto altrimenti.

**Precondizioni sui parametri effettivi, non su esistenziali generici:**

> La precondizione dell'operazione *registraRicovero* non torna: non deve controllare se esiste
> un *Letto* libero, ma se il *Letto* dato in input lo è.

**Attenzione ai confini degli intervalli.** Un errore reale, su una disgiunzione temporale:

> Considera come occupati tutti i *Letti* relativi a *RicoveriTerminati* che sono iniziati in una
> data successiva alla data `d` data in input. In questo modo, però, sta includendo anche i
> *Ricoveri iniziati e terminati dopo la data d*.

**Rispondere a tutto quello che l'operazione promette.** Da un compito valutato 25:

> Lo UC in FOL sulla ricerca Eventi non è completo, ho calcolato solo la media senza poi
> ritornare gli eventi come richiesto.

**Richiamare l'operazione che hai già definito, invece di rifare il calcolo dentro il vincolo.**
Dallo stesso compito, ed è il primo rilievo dell'elenco:

> i vincoli in FOL sul numero di persone [...] sono semanticamente corretti ma non risolvono
> completamente il problema, in quanto controllo solo che la prenotazione non ecceda la capacità,
> invece credo andasse richiamato lo UC per i posti disponibili

Il vincolo che riscrive a mano un conto che un'operazione già fa è più debole di quello che la
richiama: ripete una parte della logica e ne perde il resto. Se nel diagramma c'è
`posti_disponibili()`, il vincolo di capienza si appoggia a quella.

**Esprimere in FOL anche ciò che sembra procedurale**: se una specifica restituisce una sequenza,
il criterio di ordinamento va formalizzato, non descritto a parole.

## Ristrutturazione e schema relazionale

**Valutare se tenere separate le entità storiche da quelle correnti**, come scelta di efficienza:

> Nella ristrutturazione, avrei mantenuto la separazione tra *Ricovero* e *RicoveroTerminato*.
> Mantenendo in *Ricovero* solamente dati "freschi" rendiamo più efficienti diverse operazioni.

**Ogni vincolo esterno dell'analisi deve avere una realizzazione.** Il modo di dimostrarlo è
annotare i vincoli dello schema con il nome `[V....]` da cui derivano. Un vincolo che nell'analisi
c'era e nello schema non compare è una lacuna visibile.

**Nei trigger, interrogare la relazione giusta:**

> Il trigger *V.Stanza.maxLetti* è palesemente scorretto, deve essersi confuso (esiste sempre al
> più una sola stanza con un certo id). La query dovrebbe essere fatta sulla relazione *Letto*.

## SQL

Dal compito valutato 25, la distinzione tra errori gravi e non gravi. **Gravi**: un trigger
sbagliato. **Non gravi**, ma comunque segnalati:

> - il group by è superfluo, nel senso che non è un errore ma il risultato sarebbe stato uguale
>   senza scriverlo
> - la Zona nella clausola from non era necessaria, quindi anche l'ultima riga `z.id = a.zona`
>   si poteva omettere
> - il risultato lo ritorno esternamente ad SQL facendo la differenza, mentre si poteva fare
>   direttamente nella select: `SELECT z.pax - count(*)`

La lezione: le query devono essere **minime**. Tabelle nella `FROM` che non servono, `GROUP BY`
inutili, calcoli portati fuori dall'SQL quando l'SQL li farebbe — non fanno fallire, ma vengono
notati.

Il corollario pratico: **esegui l'SQL prima di consegnarlo**. Un errore di sintassi o una join
che moltiplica le righe sono errori gravi ed evitabili in trenta secondi. I due database di
esempio del corso sono già pronti, vedi `SKILL.md`.

## Errori di coerenza tra fasi

Il modulo risposte lega le domande fra loro — e i campi che chiede sono essi stessi un controllo:
la Domanda 7 vuole per ogni relazione `Derivante da: classe | associazione` **e** la riga *«la
relazione accorpa le relazioni che implementano le seguenti associazioni»*, che è il posto dove si
dimostra che nessuna associazione è sparita. Le rotture di questo legame sono errori:

- la Domanda 5 deve usare **lo stesso vocabolario** della Domanda 2. Simboli nuovi introdotti
  qui rompono il legame tra diagramma e specifica
- la Domanda 8 deve essere **conforme alle pre/postcondizioni** della Domanda 5, non una
  reinterpretazione libera
- le Domande 5 e 8 riguardano **solo i requisiti contrassegnati dalla barra laterale**.
  Sviluppare le operazioni sbagliate costa quanto sbagliarle

## Gli errori che ricorrono negli svolgimenti degli studenti

Le sette prove trascritte del corpus (`soluzioni-studenti/*TRASCRIZIONE.md`) non sono corrette da
nessuno, quindi non fanno testo su cosa è giusto. Fanno testo su **cosa sbagliano persone che il
corso l'hanno seguito**: gli stessi errori tornano su prove diverse, ed è materiale di controllo
prima della consegna.

**Un vincolo di inclusione dice «almeno uno», non «almeno due».** In EasyToll la traccia chiede
almeno due caselli per autostrada (`2..*`) e lo schema lo rende con `Casello(id) ⊆ aut_cas(casello)`.
Lo studente se ne accorge e lo annota a margine: *«2 volte minimo, non so come dirlo»*. Ha ragione:
ogni molteplicità minima **maggiore di 1** non è esprimibile con chiavi, foreign key o inclusioni,
e va nei vincoli esterni con un trigger. Lo stesso vale per `1..1` su una relazione separata: è
inclusione, quella sì, ma solo quella.

**Il vocabolario deve restare identico dalla Domanda 2 alla Domanda 8.** In TimeBank l'operazione
`MEDIA` compare con **quattro arietà diverse** nelle varie domande, e la funzione SQL dichiarata ne
ha una quinta. Nella stessa prova, la costante `x` (un accredito bonus) è usata in due specifiche e
**non è mai dichiarata** — né attributo, né costante, né relazione di configurazione. Un simbolo che
compare in una formula esiste solo se il diagramma o le specifiche dei tipi lo hanno introdotto.

**I confini degli intervalli sono la fonte di errore numero uno delle specifiche.** Casi visti:
`MEDIA` di TimeBank media i voti degli scambi con `inizioSca <= t` mentre la traccia dice *prima* di
`t`; `CALCTASSO` di Città Verde ha per precondizione `i >= f` invece di `i <= f`; `BIGLMEDIA` di My
Precious divide per `i - f` invece che per `f - i`. Il controllo che li prende tutti e tre: leggere
la precondizione e chiedersi **quale caso vuole escludere**, e rifare a mente un esempio con due
date concrete.

**La sottoquery che deve restringere va legata alla riga esterna.** In My Precious `BIGLDATA`
costruisce tre CTE di biglietti senza mai filtrare sulla data `d` che è l'argomento
dell'operazione; in Città Verde `NOINTERVENTI` toglie con una `EXCEPT` le aree con interventi, ma
la seconda `SELECT` non lega l'intervento all'area, così un intervento qualsiasi nel periodo
svuota il risultato. È lo stesso errore della FOL con la variabile non legata alla sua classe,
tradotto in SQL: **una condizione che non nomina l'entità di cui parla non la restringe**.

**Il trigger deve interrogare la relazione di cui parla il suo nome.** Oltre al rilievo del tutor
su `V.Stanza.maxLetti`, in My Precious `T.OPERA.NOESPTEMPDURANTERESTAURO` interroga `PRESTITO`: è
un copia-e-incolla dal trigger vicino, e nessuno lo rilegge. Prima di consegnare, per ogni trigger:
il nome, l'evento intercettato e le tabelle nella `FROM` devono parlare della stessa cosa.

**Cose fatte bene, che vale la pena copiare come metodo:**

- in Città Verde il trigger `T.INTERVENTO.SQUAPOSSIBILE` **richiama l'operazione della Domanda 8
  come tabella** (`FROM SQUADREPOSSIBILIINTERVENTO(NEW.ID)`) invece di riscriverne il calcolo: è
  esattamente il rilievo del tutor sul vincolo che non richiama lo use-case, risolto;
- sempre in Città Verde, il vincolo `V.CAPO.SEPARTECIPA` nato dalla divisione di una sottoclasse
  diventa in Domanda 7 un **vincolo di inclusione su quattro attributi**, non un trigger: prima si
  cerca il costrutto dichiarativo, il trigger è l'ultima risorsa;
- in My Precious le **pagine di minute sono usate come continuazione** con il rimando esplicito
  scritto sulla pagina di partenza («CONTINUA A MINUTE 2,3»). Il modulo dice che quelle pagine non
  vengono valutate *a meno che non siano puntate da pagine precedenti*: senza il rimando, il
  lavoro c'è ed è come non ci fosse.

## Cosa non è un errore

Per calibrare: il tutor chiude la revisione finale con *"tutto il resto va bene"* dopo aver
elencato sei rilievi su una soluzione completa. Una soluzione non deve essere perfetta, deve
essere **priva di errori sostanziali nei quattro passi eliminatori**. Scelte di modellazione
diverse ma difendibili sono accettate: il corso dice esplicitamente che non esiste una sola
soluzione giusta.
