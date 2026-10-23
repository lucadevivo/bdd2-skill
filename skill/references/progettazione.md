# Progettazione — Domande 6-8

Due delle tre domande sono eliminatorie (7 e 8). Template dalle soluzioni ufficiali
(QuickHospital è l'unica che copre tutta la fase).

## Domanda 6 — Ristrutturazione (20'/30')

Quattro cose, in quest'ordine: scelta del DBMS, progettazione dei tipi di dato in domini SQL,
ristrutturazione del diagramma, ristrutturazione dei vincoli esterni.

La ristrutturazione non è solo normalizzazione: la traccia chiede di *"effettuare opportune
scelte per aumentare le prestazioni complessive del sistema"*. Ogni decisione va motivata, e la
motivazione può essere l'efficienza di un'operazione, non solo la correttezza. Un esempio dalle
correzioni di un tutor: tenere separate `Ricovero` e `RicoveroTerminato` invece di fonderle,
perché lasciando in `Ricovero` solo i dati "freschi" le operazioni che scorrono i ricoveri attivi
non devono filtrare quelli chiusi.

### Progettazione dei tipi di dato

Ogni tipo concettuale diventa un dominio SQL, un tipo strutturato, o una relazione aggiuntiva.

```sql
CREATE DOMAIN Stringa AS VARCHAR;
CREATE DOMAIN DataOra AS timestamp;

CREATE DOMAIN CodiceFiscale AS Stringa
	CHECK (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

CREATE DOMAIN IntegerGZ as Integer
	CHECK (value > 0);

CREATE TYPE __CapienzaSala__ AS (
	n_letti_tipico IntegerGZ,
	n_letti_max IntegerGZ
);

CREATE DOMAIN CapienzaSala as __CapienzaSala__
	CHECK ( value.n_letti_tipico IS NOT NULL
	    and value.n_letti_max IS NOT NULL
	    and value.n_letti_tipico <= value.n_letti_max );
```

La coppia `CREATE TYPE __X__` più `CREATE DOMAIN X as __X__ CHECK (...)` è la convenzione del
corso per dare un vincolo a un tipo strutturato: in PostgreSQL un `CREATE TYPE` non accetta
check, quindi il vincolo si mette sul dominio che lo avvolge.

**Attenzione ai nomi che collidono con i tipi predefiniti.** `path`, `point`, `line`, `box`,
`money`, `text`, `interval` esistono già in `pg_catalog`: un `CREATE DOMAIN path` riesce, ma poi
viene **silenziosamente ombreggiato** dal tipo di sistema, e l'errore arriva molto più tardi in
forma incomprensibile (*"data type path has no default operator class"*). Se un tipo concettuale
si chiama così, dagli un nome diverso nel DDL — `PathFile` — e annotalo.

**La collisione più frequente però la crei tu.** In PostgreSQL domini, tipi e tabelle stanno
nello stesso spazio di nomi, e gli identificatori non quotati vengono ripiegati in minuscolo:
`CREATE TABLE telefono` dopo `CREATE DOMAIN Telefono` fallisce con *"type telefono already
exists"*. Il caso non è raro, è **strutturale**: un attributo multivalore diventa una relazione
che porta il nome del dato, e quel dato ha già un dominio con lo stesso nome. Succede a
`Telefono`/`telefono`, a `Email`/`email`, a `Isbn`/`isbn`. Rinomina la relazione — `rel_telefono`,
oppure `tel_lettore` col nome del ruolo — e dillo. Lo si scopre solo eseguendo il DDL.

**Le parentesi attorno a `value` sono obbligatorie.** Per accedere a un campo di un tipo
strutturato PostgreSQL vuole `(value).campo`: scritto `value.campo` interpreta `value` come nome
di tabella e fallisce con *"missing FROM-clause entry for table value"*. Le soluzioni ufficiali
lo scrivono senza parentesi, e così com'è quel DDL non compila — è uno dei motivi per cui va
eseguito.

**I check si scrivono per esteso.** Nelle soluzioni ufficiali si trova `CHECK (value ~ '...')`,
con i puntini al posto del pattern, e `CREATE TYPE Indirizzo ( ... // per esercizio )`: sono
scorciatoie del docente. Ogni dominio che nell'analisi aveva un formato deve arrivare qui con il
suo `CHECK` completo, e ogni tipo strutturato con tutti i suoi campi. Il DDL prodotto deve poter
essere eseguito così com'è — ed è il modo di verificarlo.

### Dati derivati: qui alcuni diventano memorizzati

Nell'analisi un dato derivabile è un'operazione. In ristrutturazione la domanda cambia: **il DBMS
è in grado di calcolarlo?**

- se il calcolo è sui dati della base — un conteggio, una somma, un massimo — resta derivato, e
  diventa una vista o una funzione
- se dipende da qualcosa che nella base di dati non c'è — la durata di un file video, una
  misura presa da un dispositivo — **deve** diventare un attributo memorizzato, perché nessuna
  query può ricavarlo. Va detto chi lo popola e quando

È l'unico caso in cui la regola della Domanda 2 si rovescia, e va motivato.

### Vincoli dinamici

Alcuni requisiti parlano di **transizioni**, non di stati: "un video censurato non può tornare
visibile", "una prenotazione confermata non si può riportare in attesa". Non hanno una
formulazione FOL su un singolo stato, perché mettono in relazione lo stato prima e quello dopo.

Dichiarali come vincoli dinamici e realizzali sul cambiamento: un trigger `BEFORE UPDATE` che
confronta `old` e `new`, oppure una politica di accesso che impedisce quell'aggiornamento. In
alternativa si possono rendere statici aggiungendo un dato — un istante di censura non nullo che
una volta valorizzato non si azzera — ma è una scelta di modellazione da dichiarare.

### Altri costrutti del DDL

Oltre a domini e tabelle, il DDL del corso comprende:

- **Valori progressivi** — per le chiavi surrogate introdotte in ristrutturazione:
  ```sql
  create sequence Prenotazione_id_seq;
  create table Prenotazione (
    id integer default nextval('Prenotazione_id_seq') primary key,
    ...
  );
  ```
- **Viste** — utili quando la ristrutturazione ha spezzato una classe in più relazioni e le
  operazioni continuano a ragionare sull'originale: `create view` ricompone la vista logica
  senza rinunciare alla struttura fisica scelta.
- **Indici** — si giustificano con le operazioni: un indice sugli attributi su cui la Domanda 8
  filtra o ordina è una delle "opportune scelte per aumentare le prestiti" che la traccia
  chiede.
- **Controllo dell'accesso** — `grant` e `revoke`, che sono la forma SQL delle politiche di
  accesso ai dati usate per realizzare i vincoli esterni.

**Il diagramma ristrutturato si riscrive per intero**, nello stesso formato markdown della
Domanda 2 (`## Classi`, `## Associazioni`, `## Generalizzazioni`): non è un elenco di modifiche
rispetto al concettuale. Viene disegnato anche questo, quindi vale il formato descritto in
`analisi.md`. Se dopo la ristrutturazione non resta nessuna generalizzazione, la sezione si
omette — come le altre sezioni vuote.

Quando discuti a parole le gerarchie da sciogliere, **non usare la forma a elenco**
`- \`X\` generalizza \`Y\``: è la sintassi che il renderer cerca, e trovarla fuori dalla sezione
manda in errore il disegno. Scrivilo in prosa, o dentro un blocco di codice.

### Cosa si elimina

- **attributi multivalore** → nel **diagramma** ristrutturato diventano una **classe a sé** legata
  da un'associazione, non un attributo che sparisce: il ristrutturato ufficiale di QuickHospital ha
  `ValoreTelefono` con l'associazione verso `Paziente`, ed è quella classe che alla Domanda 7 dà la
  relazione aggiuntiva. Serve in più un vincolo di inclusione se la molteplicità minima era 1
- **attributi composti** → tipo strutturato, oppure attributi separati
- **identificatori esterni** → propagazione della chiave, oppure una **chiave surrogata**

**Scegliere un identificatore primario per ogni classe** è un passo a sé, e la traccia lo elenca
esplicitamente. Le opzioni sono tre: un identificatore già presente nel concettuale; la
propagazione della chiave del contenitore, per l'identificazione esterna; una **chiave surrogata**
con valori progressivi, quando gli identificatori naturali sono composti da troppi attributi o
coinvolgono associazioni con molteplicità che non li rendono affidabili. Ogni surrogato va
motivato, e va accompagnato da un `altra chiave` che conserva l'identificazione originaria.

**La decisione sull'identificatore è di questa domanda, non della Domanda 7.** Se una catena di
identificazioni esterne è profonda — `Sede` → `Scaffale` → `Ripiano` → `Copia` — la propagazione
arriva alla Domanda 7 come una chiave primaria di quattro colonne, e con essa ogni foreign key
che punta a quella relazione. Un surrogato lo si introduce **qui**, motivandolo; accorgersene in
Domanda 7 significa tornare indietro e correggere la ristrutturazione, non rattoppare lo schema.
La fedeltà al diagramma resta la scelta di default: la propagazione duplica dati ma tiene in una
sola relazione tutto ciò che serve alle operazioni che percorrono la catena, ed è una scelta
legittima purché il pro e il contro siano scritti.

**Quello che invece non si fa qui è l'accorpamento.** Il diagramma ristrutturato conserva le
associazioni: le molteplicità `0..1`/`1..1` diventano attributi foreign key solo nella traduzione
in relazioni, alla Domanda 7. Nelle soluzioni ufficiali il ristrutturato ha ancora tutte le sue
associazioni, con i marcatori `{id}` che dicono quali reggono l'identificazione, e le
generalizzazioni sciolte compaiono come associazioni `X_isa_Y`.

**Mai far migrare le righe fra due relazioni.** La tentazione, quando una sottoclasse rappresenta
uno stato finale — un noleggio concluso, una riparazione terminata — è tenere nella relazione della
superclasse solo le istanze "aperte" e spostare la riga nell'altra alla chiusura. È sbagliato: la
superclasse deve contenere **tutte** le istanze, e la sottoclasse porta solo i suoi attributi
propri, legata da `X_isa_Y`. È quello che fa il ristrutturato ufficiale di QuickHospital, dove
`Prestazione` contiene tutte le prestazioni e le sottoclassi si attaccano con
`pe_isa_p | Prestazione 1..1 {id1} | PrestazioneEsterna 0..1`.

Il sintomo che riconosce l'errore: **ti ritrovi a dover dire quale relazione usare a seconda della
domanda** — questa per lo storico, quella per le aperte. Con l'`isa` la relazione è una sola, e
`EXISTS` / `NOT EXISTS` sulla sottoclasse risponde a entrambe.

**Non confondere questo con il consiglio del tutor** di *«mantenere la separazione tra Ricovero e
RicoveroTerminato»*, che compare in `errori.md`: quello dice di **non fondere** le due relazioni,
cioè di tenere la sottoclasse invece di schiacciarla nella superclasse con attributi nullable. Le
righe non migrano comunque: `Ricovero` contiene tutti i ricoveri, `RicoveroTerminato` porta solo i
suoi attributi propri e la riga si **aggiunge** alla chiusura. Separazione sì, migrazione no.

**La ristrutturazione non cambia il modello.** Cambia la rappresentazione: scioglie gerarchie,
elimina attributi multivalore, sceglie identificatori. Non toglie valori da un dominio fissato
nell'analisi, non cancella un vincolo esterno perché "così non serve più", non sostituisce un
attributo che i requisiti chiedono con una vista che lo calcola. Se durante la Domanda 6 ti accorgi
che l'analisi ha un difetto, si segnala: correggerlo qui rompe la corrispondenza fra le due fasi,
che è una delle cose che il correttore verifica.

**Generalizzazioni e IS-A fra classi.** Il corso dà tre approcci, da scegliere livello per
livello:

1. **fusione** delle sottoclassi nella superclasse — una sola relazione, con gli attributi delle
   sottoclassi resi opzionali (`[0..1]`). Quello che la fusione crea non è tanto la riscrittura
   di disgiunzione e completezza — con una gerarchia binaria un attributo discriminatore non
   nullo le rende dichiarative — quanto i **vincoli di partecipazione**: le associazioni che
   pendevano da una sottoclasse ora pendono dalla superclasse, e va scritto che valgono solo per
   le ennuple che appartengono a quella sottoclasse
2. **divisione** della superclasse nelle sottoclassi disgiunte
3. **sostituzione** della relazione IS-A con un'associazione, mantenendo entrambe le relazioni

La scelta si motiva con le operazioni: quante ne toccano solo le sottoclassi, quante la
superclasse intera. Ogni approccio genera vincoli esterni diversi — la fusione è quella che ne
genera di più, perché deve riesprimere disgiunzione e completezza in FOL.

**In ristrutturazione il corso è generoso di surrogati.** Misurato sul ristrutturato ufficiale di
Officine 1 (`diagrammi/Officine 3.md`): l'`identificatore` surrogato compare anche dove una chiave
naturale c'era — su `Officina`, che ha un nome, e su `Staff`, che potrebbe propagare il `cf`. La
regola pratica: nel concettuale il surrogato **non** si mette mai; nel ristrutturato, se la chiave
naturale è composta, lunga o si propaga a catena, il surrogato è la scelta attesa — e va motivato
in una riga.

**Marca ogni vincolo ristrutturato con la sua strategia, accanto al nome.** Due studenti su tre
delle prove trascritte lo fanno, e uno scrive pure la legenda: **X** = realizzato in modo
dichiarativo (chiave, dominio, ennupla, inclusione), **T** = serve un trigger. Costa un carattere
per vincolo e fa due cose: obbliga a decidere la strategia *mentre* si riscrive il vincolo, invece
che nella Domanda 7 quando lo spazio finisce; e dà al correttore la mappa per verificare che
nessun vincolo dell'analisi sia sparito — le X si ritrovano fra i vincoli delle relazioni, le T
fra gli ulteriori vincoli esterni.

**Se la gerarchia è `{complete}` ma non `{disjoint}`, la fusione con un discriminatore non
funziona.** Un oggetto può stare in due sottoclassi insieme — il dottorando che è insieme docente
e studente — e un solo attributo `tipo` non lo rappresenta. Le vie sono due: un **booleano per
sottoclasse** (`is_docente`, `is_studente`) con il vincolo che almeno uno sia vero, oppure si
rinuncia alla fusione e si tengono le sottoclassi come relazioni separate legate da inclusione.
Il discriminatore unico si usa **solo** quando la gerarchia è disgiunta.

**Una molteplicità minima maggiore di 1 non è dichiarativa, e il suo trigger va differito.**
`2..*` («ogni autostrada ha almeno due caselli», «ogni domanda ha almeno due risposte») non si
esprime con chiavi, foreign key o inclusioni: serve un trigger. Ma un trigger immediato **fa
fallire il primo inserimento**, perché al momento dell'insert la seconda riga non c'è ancora: si
scrive come `CONSTRAINT TRIGGER ... DEFERRABLE INITIALLY DEFERRED`, che controlla a fine
transazione. Il vincolo di inclusione, da solo, dice «almeno uno» e non basta.

**IS-A fra associazioni.** Si ristruttura **dopo** e **in funzione** di come sono state
ristrutturate le classi agli estremi: la sotto-associazione si fonde nella super-associazione
quando la fusione delle classi l'ha resa ridondante, altrimenti resta e si aggiunge un vincolo
esterno di inclusione.

Quel vincolo è la forma che si trova nelle soluzioni ufficiali:

```
[V.let_gen_pref_isa_let_gen]
	ALL m, s   let_gen_pref(m, s) --> let_gen(m, s).
```

e nello schema relazionale si realizza con una **foreign key verso la relazione più generale**,
annotata col nome del vincolo:

```
Bibliotecario(__persona__, spec_prim)
	fk: (persona, spec_prim) references let_gen(bibliotecario, spec) -- [V.let_gen_pref_isa_let_gen]
```

Funziona come foreign key solo se la super-associazione è diventata una relazione con quella
chiave. Se è stata accorpata, il vincolo diventa un'inclusione e va realizzato con un trigger.

### Vincoli esterni ristrutturati

Si riscrivono nel vocabolario ristrutturato, mantenendo il nome `[V....]`:

```
Specifica ristrutturata vincoli esterni:

[V.Persona.gen_complete]
	ALL p  Persona(p) --> [
		( EXISTS paz  let_isa_pers(paz, p) )
		or
		( EXISTS m    bib_isa_pers(m, p) )
	].
```

Vanno riscritti anche i vincoli che la ristrutturazione **crea**: sciogliere una
generalizzazione, per esempio, trasforma un vincolo implicito del diagramma in un vincolo
esterno esplicito da realizzare.

**Qui i vincoli restano in FOL.** Strategia di realizzazione e codice sono la Domanda 7: in
questa risposta si riscrive la formula nel vocabolario nuovo, non la si implementa.

**Contarli è il passo che si salta senza accorgersene.** Una superclasse può avere più insiemi di
generalizzazione indipendenti, e ognuno genera il suo vincolo: il controllo è scorrere le
associazioni `*_isa_*` che insistono sulla stessa classe, raggrupparle per insieme di
generalizzazione, e verificare che ogni gruppo abbia il suo `[V....]`. Le soluzioni ufficiali ne
sviluppano una e annotano *"tutti gli altri, v. diagramma"*: quella frase nasconde un numero, e
il numero va ricavato dal diagramma.

## Domanda 7 — Schema relazionale con vincoli (30'/60', eliminatoria)

**Che cosa si consegna, per non sbagliare la forma.** La risposta è: la **notazione testuale**
dello schema (quella qui sotto), e per ogni vincolo esterno il **progetto del trigger in
pseudo-codice**, come il modulo chiede alla lettera. Il DDL SQL e i trigger in `plpgsql` sono lo
strumento con cui **verifichi** che quella risposta regga: si scrivono, si eseguono, e si allegano
in appendice — non prendono il posto della notazione né del progetto. È la sola lettura che rende
coerenti *«eseguire è una verifica, non la forma della risposta»* (`SKILL.md`) e *«lo schema si
consegna in due forme»*: due forme sì, ma la seconda è un'appendice verificata, non la risposta.

Notazione delle soluzioni ufficiali: chiave primaria sottolineata (`__attr__` nel testo),
attributi nullable con `*`, vincoli elencati sotto la relazione con rientro.

```
Nazione(__nome__)

Citta(__id__, nome, nazione)
	fk: nazione references Nazione(nome)

Persona(__cf__, nome, cognome, nascita)

Paziente(__persona__, email, indirizzo)
	fk: persona references Persona(cf)
	incl.: persona compare in telefono(paziente)

Bibliotecario(__persona__, spec_prim)
	fk:    persona references Persona(cf)
	incl:  persona compare in let_gen(bibliotecario)
	fk:    spec_prim references Genere(nome)
	fk:    (persona, spec_prim) references let_gen(bibliotecario, spec) -- [V.let_gen_pref_isa_let_gen]

telefono(
	__paziente__:CodiceFiscale,
	__valtel__:Telefono
)
```

### Il vocabolario dei vincoli

La traccia d'esame elenca sei categorie — chiave, chiave primaria, foreign key, ennupla, dominio,
inclusione — e ognuna ha la sua forma nello schema. Sono quelle delle soluzioni ufficiali:

| Vincolo | Come si scrive |
|---|---|
| chiave primaria | attributi sottolineati, `__attr__` nel testo |
| altra chiave | `altra chiave: (nome)` |
| foreign key | `fk: attr references Relazione(attr)` |
| ennupla e dominio | `check: inizio < fine` |
| inclusione | `incl.: attr compare in Relazione(attr)` |

Non inventare prefissi nuovi: `key:`, `enn.:`, `dom.:` non appartengono al corso.

**`check:` è un vincolo di ennupla, sempre.** La slide B.3.1 lo dice esplicitamente — *"il
costrutto check permette la definizione di soli vincoli di ennupla"* — e da lì segue la regola per
il caso che sembra non avere posto nel vocabolario: un controllo che deve **leggere un'altra
relazione** non è un `check:`. Se il valore deve esistere altrove è `fk:`; se deve comparire
altrove è `incl.:`; in entrambi i casi, quando il DBMS non lo garantisce da solo, si dichiara la
realizzazione con trigger nella sezione dei vincoli. Un `check:` che nomina due relazioni è un
vincolo esterno travestito.

**Realizza con gli strumenti del corso, anche quando PostgreSQL ne ha di migliori.** Un vincolo
di non sovrapposizione fra periodi si scriverebbe in PostgreSQL con un `EXCLUDE USING gist` su un
`tsrange`: e' piu' corto, piu' veloce e piu' robusto di un trigger. **Ma `EXCLUDE` non compare da
nessuna parte nel materiale del corso**, che per un vincolo che confronta piu' ennuple prescrive
il trigger progettato secondo la slide B.3.1. La risposta si valuta sul metodo del corso, non
sull'eleganza dell'implementazione: scrivi il trigger. Se vuoi, aggiungi l'`EXCLUDE` come nota a
margine — mai al posto del trigger.

Vale in generale: se stai per usare un costrutto SQL che non trovi nel materiale, fermati e
chiediti come lo farebbe il corso.

**Non tutti i vincoli hanno un nome.** I `[V....]` sono quelli dell'analisi: quelli che la
traduzione genera da sola — l'inclusione che nasce da una molteplicità minima `1` su
un'associazione ordinaria — restano annotazioni `incl.:` senza nome, come nelle soluzioni
ufficiali (`incl.: persona compare in telefono(paziente)`). Battezzarli non è un errore, ma
allunga inutilmente l'elenco dei vincoli da realizzare.

**`fk:` e `incl.:` sono cose diverse.** Una foreign key dice che un valore, *se c'è*, deve
esistere altrove; un'inclusione dice che un valore **deve comparire** da qualche parte, e il DBMS
non la garantisce da solo.

Il **commento `-- [V.nome]`** lega il vincolo a quello dell'analisi: serve a dimostrare che ogni
vincolo esterno è stato realizzato, e a far trovare quelli che non lo sono.

**L'origine di ogni relazione: sul modulo sono due campi distinti, e vanno tenuti distinti.**
Il riquadro di ogni relazione chiede `Derivante da: classe | associazione` — da cerchiare, quindi
una parola sola — e **più sotto, su una riga a sé**, *«la relazione accorpa le relazioni che
implementano le seguenti associazioni: …»*. Fonderli in `Derivante da: classe Officina + assoc.
citta_off, dirige` è comodo ma non è il modulo, e la seconda riga è quella che dimostra dove sono
finite le associazioni senza relazione propria:

```
Officina(__id__, nome, citta, direttore)
	Derivante da: classe
	Accorpa le associazioni: citta_off, dirige
```

Se una relazione non accorpa nulla, la riga si omette.

### Tradurre le associazioni

I vincoli di molteplicità diventano vincoli di chiave, foreign key, o inclusione.

- **`0..*` — `0..*`**: relazione propria con chiave composta dalle due foreign key
- **un ruolo `1..1` o `0..1`**: si può **accorpare** l'associazione nella relazione dell'altro
  estremo, come attributo foreign key. Con `1..1` l'attributo è `NOT NULL`, con `0..1` nullable
- **molteplicità minima 1 sull'estremo opposto**: serve in più un **vincolo di inclusione**, che
  la foreign key da sola non garantisce
- **associazioni con attributi** (association class): relazione propria, sempre
- **associazioni non binarie** (ternarie o più): relazione propria, con chiave composta da tutte
  le foreign key verso le classi coinvolte. Non si accorpano mai: l'accorpamento presuppone due
  soli estremi. Se una molteplicità è `1..1` su uno degli estremi, quella foreign key esce dalla
  chiave e resta un attributo

**Le foreign key possono avere un'azione compensativa.** Per default il DBMS rifiuta la modifica
che violerebbe il vincolo; il progettista può scegliere altro, e il corso usa `ON UPDATE CASCADE`
e `ON DELETE SET NULL`, componibili sulla stessa foreign key. Il caso tipico sono le **chiavi
propagate** da un'identificazione esterna: se cambia il numero di uno scaffale, le copie che lo
citano nella propria chiave devono seguirlo, altrimenti la modifica è impossibile.

```
Ripiano(__n__, __scaffale__, __sede__)
	fk: (scaffale, sede) references Scaffale(n, sede)
		ON UPDATE CASCADE
```

La chiave surrogata si annota nello schema col tipo, come fanno le soluzioni ufficiali —
`Prestito(__id__:serial, inizio, lettore)` — mentre il `create sequence` con `default nextval`
compare nel DDL.

L'accorpamento è la scelta di default quando è possibile, perché evita un join; ma se
l'associazione ha attributi propri, o se le due classi vengono interrogate separatamente, tenere
la relazione separata può essere più efficiente. Motivalo.

**Quando entrambi gli estremi sono `0..1` o `1..1` si può accorpare in due direzioni, e non sono
equivalenti: scegli quella che rende dichiarativi più vincoli.** Con `0..1` — `1..1`, accorpando
dal lato `1..1` l'attributo diventa `not null` più `unique`, e il DBMS garantisce entrambe le
molteplicità; dall'altro lato una delle due resta un vincolo di inclusione da realizzare a mano.

**Se la ristrutturazione ha introdotto una chiave surrogata** al posto di un identificatore —
esterno o interno che fosse — aggiungi un `altra chiave` sugli attributi che identificavano prima.
Quando invece il surrogato arriva a una classe che nel concettuale **non aveva alcun
identificatore**, e capita spesso, non c'è nessun `altra chiave` da scrivere: non inventarne una
per simmetria. Il controllo è guardare la classe nel concettuale e chiedersi se aveva un `{id}`. Quel vincolo non è
più visibile nel diagramma ristrutturato — bisogna risalire al concettuale — e perderlo significa
perdere silenziosamente un'identificazione: è il tipo di errore che costa un passo eliminatorio.

### Realizzazione dei vincoli in SQL

I vincoli esterni **non restano in forma logica**. Per ognuno: strategia scelta, e codice.

```
Progettazione dei vincoli esterni ristrutturati

[V.Prestito.gen_disj_complete]
	ALL prest  Prestito(prest) --> [ ... ]

Strategia:
	- Politiche di accesso ai dati + trigger

Politiche di accesso ai dati:
	impedisci:
		UPDATE su Prestito(id)
		UPDATE su PrestitoScaduto(id)
		UPDATE su PrestitoCorrente(id)
```

### Il progetto del trigger viene prima del codice

La slide B.3.1 non passa dal vincolo al `plpgsql`: in mezzo c'è un **progetto del trigger** in
pseudo-codice, ed è quello che va scritto nella risposta — il codice SQL viene dopo, e da solo non
dimostra il ragionamento.

Il modulo risposte chiede esattamente questo, e in tre punti: *"progettare un trigger che lo
implementi, definendo: (a) gli eventi da intercettare (inserimento, modifica, eliminazione di
ennuple); (b) quando intercettare tali eventi (appena prima o subito dopo l'evento intercettato);
(c) la relativa funzione in pseudo-codice con SQL immerso"*. Il `plpgsql` compilante non è la
risposta: è il modo di verificarla.

```
Progetto del trigger V.Lettore.gen_disj

	Operazioni da intercettare:  INSERT o UPDATE in LettoreInterno o LettoreEsterno
	Quando invocare la funzione: dopo l'operazione intercettata

	Funzione(old, new):
		- Sia isError = EXISTS(
			SELECT *
			FROM LettoreInterno i, LettoreEsterno e
			WHERE i.lettore = new.lettore AND e.lettore = new.lettore
		  )
		- Se isError = TRUE  solleva eccezione "INSERT/UPDATE viola il vincolo"
		- Altrimenti, permetti l'operazione
```

Le tre righe del progetto rispondono a tre domande, in quest'ordine:

- **quali eventi possono portare un DB legale a diventare illegale?** — sono le operazioni da
  intercettare, e sono spesso più d'una su più relazioni. Un evento che non può violare il
  vincolo non si intercetta, e vale la pena scrivere perché
- **prima o dopo l'operazione?** — cioè se la funzione deve vedere il DB prima o dopo la modifica
- **cosa riceve la funzione?** — `old` esiste solo per `UPDATE` e `DELETE` (l'ennupla prima della
  modifica o quella cancellata), `new` solo per `INSERT` e `UPDATE` (l'ennupla dopo). Con eventi
  di tipo diverso sulla stessa funzione, il primo passo è capire quale dei due è valorizzato

**Una funzione condivisa fra tabelle diverse va ramificata con un `IF`, non con un `CASE`.**
plpgsql risolve i riferimenti ai campi di `new`/`old` quando prepara l'**espressione**, non quando
ne valuta il ramo: `u := case TG_TABLE_NAME when 'utente' then new.email else new.utente end`
fallisce con *"record new has no field utente"* anche sulla tabella in cui il ramo giusto sarebbe il
primo. Servono istruzioni separate — `if TG_TABLE_NAME = 'utente' then u := new.email; else ...` —
e su un evento `DELETE` va guardato `TG_OP`, perché `new` non esiste. Misurato due volte su due
prove diverse: è la trappola più costosa del `plpgsql` condiviso.

Trigger diversi possono condividere la stessa funzione: è la forma che il corso preferisce, perché
riduce il codice da scrivere.

**Attenzione a `BEFORE` quando il controllo è una somma o un conteggio.** In un trigger `BEFORE
INSERT` la riga nuova **non è ancora nella tabella**: una `SELECT SUM(...)` la esclude, e il
controllo passa proprio nel caso che doveva bloccare. O si somma il valore di `new` a parte, o il
trigger va messo `AFTER` — che è la scelta della slide, e il motivo per cui il suo progetto dice
*"dopo l'operazione intercettata"*. È l'errore che si vede solo eseguendo, con una prova costruita
per fallire.

**Le politiche di accesso hanno una forma SQL precisa**, ed è la revoca puntuale sulla colonna:

```sql
REVOKE UPDATE (id) ON Lettore FROM PUBLIC;
```

Spesso è la politica a rendere superflui metà dei trigger: se nessuno può cambiare gli
identificatori artificiali, gli `UPDATE` diventano innocui e restano da intercettare solo
`INSERT` e `DELETE`. Dichiaralo, è parte della motivazione della strategia.

**Le foreign key si dichiarano `deferrable`.** Il DDL ufficiale del corso lo fa su **tutte**, e
non è pedanteria: quando due relazioni si riferiscono a vicenda con vincoli obbligatori — una
officina ha un direttore, il direttore lavora in quell'officina — nessuno dei due inserimenti può
venire per primo. Con `deferrable initially deferred`, o con un `set constraints all deferred`
nella transazione, il controllo si sposta alla fine.

```sql
foreign key (direttore) references Staff(id) deferrable initially deferred
```

Il `create table` passa comunque anche senza: il difetto si vede solo provando a **inserire** dei
dati. È una ragione in più per eseguire il DDL con qualche ennupla di prova, non solo per
crearlo.

Le strategie disponibili, in ordine di preferenza:

1. **vincolo dichiarativo** — `check`, `unique`, `not null`, foreign key. Sempre preferibile:
   il DBMS lo garantisce senza codice
2. **trigger** — per i vincoli che coinvolgono più ennuple o più relazioni
3. **politiche di accesso ai dati** — impedire certe operazioni (tipicamente `UPDATE` su una
   chiave, o `DELETE`) quando un trigger non basta o costerebbe troppo

Spesso servono in combinazione: un trigger che controlla l'inserimento più una politica che
impedisce l'update che aggirerebbe il controllo.

**Un vincolo può essere realizzato dall'algoritmo.** Non tutto si esprime in modo dichiarativo o
con un trigger: alcuni vincoli sono garantiti dal codice dell'operazione che li potrebbe violare
— "l'autore non può valutare il proprio video" si controlla dentro `valuta_video`. È una
strategia legittima a **tre condizioni**:

1. **nessun'altra** operazione può violare quel vincolo;
2. il collegamento è scritto in entrambi i punti — qui la strategia, e nella Domanda 8 il commento
   `-- [V.nome]` accanto al controllo. Senza, il vincolo cade nel vuoto fra le due risposte e
   nessuno se ne accorge;
3. all'esame, l'operazione che lo realizza è **fra quelle che la barra laterale chiede di
   sviluppare**.

La terza è quella che si dimentica: se il vincolo riguarda una funzionalità **non** barrata,
affidarlo all'algoritmo lo affida a un'operazione che nella Domanda 8 non comparirà, e il vincolo
resta senza realizzazione. Per quelli scegli un trigger o un vincolo dichiarativo, che vivono
nella Domanda 7 e non dipendono da cosa svilupperai dopo.

**Tutti i vincoli, non solo il primo.** La soluzione ufficiale di QuickHospital ne sviluppa uno
e annota *"tutti gli altri vincoli per disjoint/complete, v. diagramma"*: lì il docente lascia il
resto come esercizio. In una risposta ogni `[V....]` dell'analisi ristrutturata deve comparire
con la sua strategia e il suo codice. Il controllo veloce: scorri i nomi dei vincoli
dell'analisi e verifica che ognuno sia citato qui.

**Realizzare un'inclusione** è il caso in cui serve più attenzione, perché non basta un trigger.
`incl.: cliente compare in Veicolo(cliente)` — ogni cliente possiede almeno un veicolo — richiede
tre cose:

- un controllo all'inserimento del cliente, che però al momento dell'`insert` non può passare:
  il veicolo non esiste ancora. Serve un **`constraint trigger ... deferrable initially
  deferred`**, che verifica a fine transazione
- un controllo su `delete` e `update` del lato che contiene i valori, altrimenti si può togliere
  l'ultimo veicolo di un cliente e violare il vincolo dall'altra parte
- oppure, se il controllo costasse troppo, una **politica di accesso** che impedisce quelle
  operazioni

**Lo stesso schema vale per i vincoli che confrontano due insiemi**, non un valore con un
insieme: "i prodotti prelevati dal magazzino sono uguali, per tipo e numero, a quelli inseriti nel
distributore" non e' un'appartenenza ma un'**uguaglianza fra due insiemi di coppie**, costruiti da
piu' ennuple ciascuno. Nessun controllo per riga puo' funzionare, perche' durante la transazione
l'insieme e' incompleto per definizione: serve un `constraint trigger ... deferrable initially
deferred` su **entrambe** le relazioni di dettaglio, e la condizione si scrive come differenza
**nei due versi** (`A except B` e `B except A` entrambe vuote), altrimenti passa il caso in cui un
lato contiene tutto l'altro piu' qualcosa.

Le inclusioni che nascono da una generalizzazione `{complete}` sciolta hanno la forma
dell'**unione**: `incl.: staff compare in Dipendente(staff) unione Direttore(staff)`, cioè ogni
membro dello staff è un dipendente o un direttore. La realizzazione è la stessa, con la
condizione che cerca in entrambe le relazioni.

Esempio di trigger nella forma usata dal corso (PostgreSQL, `plpgsql`):

```sql
CREATE FUNCTION V_WP_Date_Progetto_Date() RETURNS trigger AS $$
declare
  progettoInizio date;
begin
  select inizio into progettoInizio from Progetto where id = new.progetto;
  if new.inizio < progettoInizio then
    raise exception 'Il progetto comincia il %', progettoInizio;
  end if;
  return new;
end;
$$ language plpgsql;

CREATE TRIGGER WP_dates_within_project_date
BEFORE INSERT OR UPDATE ON WP
FOR EACH ROW EXECUTE PROCEDURE V_WP_Date_Progetto_Date();
```

## Domanda 8 — Specifiche realizzative (30'/45', eliminatoria)

Pseudo-codice **con SQL immerso**, non SQL puro. Per ogni operazione: segnatura con i domini SQL,
l'algoritmo, e la dichiarazione di dove va implementata (DBMS o back-end).

```
Specifica realizzativa dello Use-case GestionePrestiti

bibliotecari_idonei(g:Stringa): Set[Bibliotecario.*]
	pre: nessuna

	post:
		BEGIN TRANSACTION

		Q = SELECT m.*
			FROM Genere spec LEFT OUTER JOIN Bibliotecario m
				ON spec.nome = m.spec_prim
			WHERE spec.nome = s;

		Se Q è vuoto:
			error, s non è il nome di una specializzazione

		Se Q = (NULL, ..., NULL):
			// nessun bibliotecario ha s come spec. primaria
			Q = SELECT m.*
				FROM Bibliotecario m, let_gen ms
				WHERE ms.bibliotecario = m.persona AND ms.spec = s;
		COMMIT;
			// Usiamo una transazione per evitare risultati inaspettati in caso di
			// modifiche concorrenti al DB tra le due query.

		Restituisci Q;
```

Convenzioni:

- il corpo si etichetta `algoritmo:` — è la forma della slide B.3.2 — oppure `post:` quando la
  specifica di Domanda 5 aveva una postcondizione da garantire. Le soluzioni ufficiali usano
  entrambe: scegline una e tienila per tutte le operazioni della risposta
- **l'attore che invoca non è un parametro.** Un'operazione riservata a un ruolo riceve la propria
  identità dal contesto, e la si lega in una riga prima dell'algoritmo: *«Sia `b:CodiceFiscale` il
  valore del campo chiave della ennupla di `Bibliotecario` associata all'attore che ha invocato
  l'operazione»*. Per un'operazione di classe la stessa riga lega `this` alla sua ennupla
- le query si assegnano a una variabile (`Q = SELECT ...`), e poi si ragiona sul risultato
- il controllo di flusso è in italiano: `Se Q è vuoto:`, `Restituisci Q;`, `errore, ...`
- i tipi di ritorno usano i domini SQL: `Set[Bibliotecario.*]`, `integer`, `timestamp`,
  `Codicefiscale` — non i tipi concettuali. Un risultato **ordinato** è una `List[...]` e ne
  esplicita i campi: `List[ (ripiano:IntegerGZ, scaffale:IntegerGZ, sede:Stringa) ]`
- un `sorted(S; criterio)` della Domanda 5 si realizza con `ROW_NUMBER() OVER (ORDER BY ...)`,
  mai con `RANK()` o `DENSE_RANK()`: il Documento A.4.1 definisce l'ordinamento come una biiezione
  fra gli elementi e gli interi `1..|S|`, e a parità di criterio `RANK()` assegnerebbe la stessa
  posizione a due elementi. Quando l'ordine basta a chi chiama, l'`ORDER BY` da solo è più
  semplice: la colonna della posizione serve solo se il risultato la deve contenere
- **un parametro arriva con i domini dello schema relazionale, non con quelli concettuali.** Se
  la classe che il parametro rappresenta ha una chiave composta — tipicamente per identificazione
  esterna — il parametro concettuale `r:Ripiano` diventa i suoi attributi:
  `ripiano_disponibile(n:IntegerGZ, scaffale:IntegerGZ, sede:Stringa)`. È la chiave primaria della
  relazione a dire quanti parametri servono
- **la corrispondenza fra la segnatura concettuale e questa è diretta**: `Medico [0..*]` della
  Domanda 4 diventa `Set[Medico.*]`; un risultato ordinato `(r:Ricovero, pos:Intero > 0) [0..*]`
  diventa `List[ (letto:IntegerGZ, stanza:IntegerGZ, sett:IntegerGZ, piano:integer,
  padiglione:Stringa) ]`, cioè l'elemento strutturato si espande nelle colonne della sua chiave.
  Sono le due operazioni di QuickHospital, nelle due fasi
- un **insieme in ingresso** si scrive `Set[Tipo]` come in uscita, e si annota come viene
  realizzato: un array SQL è la scelta naturale in PostgreSQL, una tabella temporanea se
  l'insieme è grande. Attenzione però: **nessuna operazione ufficiale prende una collezione in
  ingresso** — prendono identificatori e lasciano che sia il database a produrre gli insiemi. Se
  ti serve un parametro-collezione, prima chiediti se l'operazione è modellata bene
- i parametri entrano nell'SQL immerso **per nome, senza marcatori**: `WHERE spec.nome = s`. È
  pseudo-codice, non codice ospite: non servono `:s` né `?`
- le operazioni che leggono e poi scrivono stanno in una transazione, con un commento che dice
  **perché**: tra le due query il database può cambiare
- `SET CONSTRAINTS ALL DEFERRED;` quando l'operazione crea uno stato temporaneamente incoerente

### Un'operazione che scrive

Il template qui sopra è di sola lettura. Le operazioni che modificano lo stato hanno una forma
propria, e sono metà della Domanda 8:

```
valuta_video(u:CodiceUtente, vid:CodiceVideo, voto:Intero in 1..5)
	post:
		BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

		Q = SELECT v.autore FROM Video v WHERE v.codice = vid;
		Se Q è vuoto:
			errore, vid non identifica un video
		Se Q.autore = u:
			errore, un utente non puo' valutare un proprio video   -- [V.no_autovalutazione]

		Q2 = SELECT 1 FROM Valutazione WHERE utente = u AND video = vid;
		Se Q2 non è vuoto:
			errore, l'utente ha gia' valutato questo video

		INSERT INTO Valutazione(utente, video, voto, istante)
		VALUES (u, vid, voto, current_timestamp);

		COMMIT;
```

Tre cose che valgono in generale:

- **un'operazione che non restituisce nulla non ha tipo di ritorno** nella segnatura, e non ha
  `Restituisci`. Se restituisce l'oggetto creato, il tipo è quello e si termina con
  `Restituisci` il valore appena inserito
- ogni caso d'errore ha il **suo** messaggio: distinguere "non esiste" da "esiste ma non si può"
  fa parte della specifica, non è cortesia
- se il vincolo che stai controllando viene dall'analisi, **annota il suo `[V....]`** accanto al
  controllo: è così che si dimostra che è stato realizzato (vedi sotto). La maggior parte dei
  controlli non lo ha, ed è giusto così: *"il prestito non è già stato restituito"* è una
  precondizione dell'operazione, non un invariante del database. Il tag va solo sui controlli che
  corrispondono a un `[V....]` dell'analisi ristrutturata — non inventarne di nuovi qui

### Il livello di isolamento non è un dettaglio

`BEGIN TRANSACTION` da solo, con il `READ COMMITTED` che PostgreSQL usa di default, **non
garantisce le precondizioni di non-esistenza** — proprio quelle più frequenti: "non ha già
votato", "il posto è libero". Due transazioni concorrenti non vedono le righe l'una dell'altra,
entrambe superano il controllo, entrambe inseriscono.

Le strade sono tre, in ordine di preferenza:

1. un **vincolo dichiarativo** che rende impossibile il duplicato (`unique(utente, video)`): il
   DBMS lo garantisce senza costi di isolamento
2. `ISOLATION LEVEL SERIALIZABLE`, che fa fallire una delle due transazioni
3. `SELECT ... FOR UPDATE` sulle righe coinvolte, quando esistono già

Dichiara quale hai scelto. Scrivere `BEGIN TRANSACTION` e fermarsi lì è la forma che *sembra*
corretta e non lo è.

**Vale anche per le operazioni di sola lettura.** Il template qui sopra apre con `BEGIN
TRANSACTION` nudo e un commento che dice di voler evitare risultati incoerenti fra due query:
è esattamente ciò che `READ COMMITTED` **non** garantisce, perché ogni istruzione vede
un'istantanea nuova. Due letture in cui la seconda dipende dall'esito della prima vogliono
`ISOLATION LEVEL REPEATABLE READ`, che fissa un'unica istantanea per l'intera transazione. Le
soluzioni ufficiali scrivono `BEGIN TRANSACTION` e basta: è la forma attestata, ma il livello
dichiarato è la risposta migliore, e costa una riga.

**Quando serve una transazione**: ogni volta che l'operazione fa **più di una query** e il
risultato della seconda dipende da quello della prima — anche se sono due letture, come
nell'esempio di sola lettura qui sopra, perché fra le due il database può cambiare e le due
risposte risulterebbero incoerenti fra loro.

### Verificare le precondizioni

L'algoritmo deve **controllare le precondizioni** scritte alla Domanda 5 e **garantire le
postcondizioni**. Il legame è esplicito: se la precondizione dice "il letto dato in input è
libero", l'algoritmo interroga quel letto, non l'esistenza di un letto libero qualsiasi.

Distinguere i casi di errore è parte della specifica: `prest_id` che non identifica nulla e
`prest_id` che identifica una prestazione già eseguita sono due errori diversi, con due messaggi
diversi.

### DBMS o back-end

Da dichiarare per ogni operazione. Il criterio è quello della slide B.3.2, e distingue per **tipo
di operazione**, non per complessità:

- le **operazioni di use-case** vanno «in generale, nel livello più esterno del back-end, di modo
  che siano accessibili agli utenti del sistema», cioè agli attori del diagramma concettuale —
  in un'applicazione web RESTful sono le procedure dietro gli endpoint REST
- le **operazioni di classe** dipendono dalla tecnologia del back-end: con un back-end a oggetti
  diventano metodi delle classi corrispondenti a quelle del diagramma ristrutturato; in
  alternativa si implementano **nel DBMS con `CREATE FUNCTION`**, e così sono disponibili a tutti
  i back-end che accedono alla base dati, invocabili con `SELECT miaFunzione(argomenti);` o
  dentro query più complesse

## Verificare prima di consegnare

L'SQL scritto qui è il punto in cui un errore costa l'esame. Esegui sempre il DDL e le query su
PostgreSQL prima di dare la risposta per buona — vedi la sezione corrispondente in `SKILL.md`.
