# Analisi concettuale — Domande 1-5

Template presi dalle soluzioni ufficiali del corso (QuickHospital, Travel to the Moon). La forma
conta: i documenti di specifica sono testo strutturato con rientri, non prosa.

**Ambito.** Produci **gli artefatti che il compito chiede, e quelli che la tua modellazione rende
necessari** — per intero, tutti. Le esercitazioni `E.A.1.x` elencano negli Obiettivi uno o due
passi (*"si riveda il diagramma"*, *"produrre la relativa specifica dei tipi di dato"*): non
aggiungerne di estranei, ma se il diagramma che hai prodotto introduce un tipo concettuale,
un'operazione o un vincolo non esprimibile graficamente, la loro specifica fa parte del passo
richiesto e va data. Vedi la checklist in `SKILL.md`.

In particolare **i vincoli esterni non sono mai un artefatto estraneo**: sono la parte del
diagramma che il diagramma non riesce a disegnare. Se gli Obiettivi chiedono "un diagramma UML
concettuale" e nel tuo diagramma resta un requisito non rappresentabile, quel vincolo fa parte
della risposta — altrimenti il requisito è perso.

**Esercitazioni che ne richiamano un'altra.** Diverse non contengono la specifica dei requisiti
ma rimandano a quella precedente (E.A.1.6 rimanda a E.A.1.3): il PDF da solo sembra vuoto. Vai a
recuperare il testo dell'esercitazione citata prima di iniziare.

**Quando l'attributo sta sull'associazione e quando sulla classe.** La regola del corso su una
classe associativa è una sola, ed è quella della slide A.1: *«la natura dell'associazione non
cambia: il diagramma permette ad una stessa coppia di oggetti di formare al più un link»*.
Da lì segue la pratica: l'attributo si mette sull'associazione quando dipende **dalla coppia**,
non da uno solo dei due oggetti. Se un estremo ha molteplicità `1..1` o `0..1`, ogni coppia è
determinata dall'oggetto di quel lato, e l'attributo appartiene semplicemente alla sua classe:
un anno di iscrizione, quando ogni studente è iscritto a un solo corso, è un attributo dello
studente. Non è un divieto — è che sull'uno-a-molti la classe associativa non aggiunge niente.

**Insiemi di valori chiusi: tre strade, non due.** Un elenco chiuso di valori — le posizioni
universitarie, le tipologie di impianto, i colori di difficoltà — può diventare un tipo
enumerato, una classe, o una gerarchia di sottoclassi. Il criterio è **cosa porta con sé ogni
valore**.

| Ogni valore… | Allora |
|---|---|
| è solo un'etichetta, nessuno vi associa nulla, **e la traccia li elenca tutti** | **tipo di dato enumerato** |
| viene contato, confrontato fra istanze, o messo in associazione con altro | **classe** |
| ha attributi, associazioni o operazioni **diversi dagli altri valori** | **sottoclassi** in una generalizzazione |
| non è un valore ma una **forma alternativa** del dato, con attributi propri | **sottoclassi**: è lo stesso caso |
| è una **classificazione senza struttura propria**, ma va contata, confrontata o associata | **classe** di classificazione, non sottoclassi |
| è un **fatto primitivo** su un oggetto, non ricavabile da altro | **attributo**, anche booleano |

**Se ti tocca inventare i valori, non era un enumerato.** Un tipo enumerato dichiara un dominio
chiuso: scriverne uno i cui valori la traccia non nomina («contanti, carta, bonifico» dedotti dal
nulla) significa mettere nel modello un'assunzione arbitraria dove il corso metterebbe una
**classe** — che i valori li lascia ai dati invece che allo schema. Le soluzioni ufficiali fanno
così con `Modello`, `Tipologia`, `CasaProduttrice`. L'enumerato è per gli elenchi che la traccia
chiude lei («uno fra disponibile, noleggiato, in manutenzione, rotto»).

Le quattro strategie convivono, e non è teoria: in una soluzione ufficiale del corso compaiono
tutte e quattro nello stesso diagramma. Il caso più istruttivo è una proprietà booleana che è
**attributo su una classe e operazione su un'altra** — memorizzata dove è un fatto primitivo,
derivata dove segue da quel fatto. Nel dominio della biblioteca sarebbe: `Sede.storica` è un
attributo, perché è una qualità della sede che nessun altro dato determina; `Libro.raro()` è
un'operazione, perché discende dall'anno di edizione e dal numero di copie.

La domanda da farsi non è "quante strategie conosco" ma **che cosa è questo dato**: un fatto, una
derivazione, un'etichetta, o una forma con struttura propria.

Il caso che confonde di più è la **classificazione senza contenuto**: categorie nominate dai
requisiti — libri per fascia d'età, sedi di pregio o ordinarie — che però non portano
attributi diversi fra loro. La tentazione è farne sottoclassi, ma qui la sottoclasse non
porta niente di proprio e la partizione non è un requisito (per il caso in cui invece lo è, vedi
più sotto). Le soluzioni ufficiali in questi casi introducono una **classe
di classificazione** associata all'oggetto: la molteplicità dell'associazione decide se un
oggetto può appartenere a una sola categoria (`1..1`) o a più d'una (`1..*`).

Il terzo caso è quello che sfugge più spesso. Se i lettori istituzionali hanno qualcosa che
quelli privati non hanno, "tipo di lettore" non è un attributo né una classe di lookup: è una
generalizzazione `{disjoint, complete}` di `Lettore`. Il test: prova a elencare gli attributi di
ciascun valore — se le liste differiscono, sono sottoclassi.

**Ma il test funziona in una direzione sola.** Attributi diversi *bastano* a giustificare le
sottoclassi; non sono *necessari*. Nel diagramma ufficiale di Accademia 2, **otto classi su
dodici sono sottoclassi completamente vuote** — nessun attributo, nessuna operazione, nessuna
associazione propria. Il prof le crea lo stesso, perché il loro lavoro è **partizionare
l'estensione**: dire che ogni impegno è di uno e un solo tipo, e che i tipi sono quelli, è
un'informazione che nessun attributo esprime. Quindi una sottoclasse si giustifica quando porta
qualcosa di proprio **oppure** quando la partizione è essa stessa un requisito. Il caso in cui
*non* si giustifica resta quello dell'etichetta derivabile da altri dati.

Nel dubbio fra le prime due, chiediti se in fase di progettazione ti servirebbe una relazione a
sé: se sì, classe.

**Un dato derivabile non si memorizza — e il vincolo è il sintomo.** Se per tenere allineato un
dato a un altro dato ti serve un vincolo esterno, quel dato non andava memorizzato: è
un'**operazione**. Il caso tipico è un livello, una fascia o una categoria che dipende da una somma
accumulata: si scrive `livello(): Livello` sulla classe, con la formula che sceglie il valore, e
l'associazione che lo memorizzava sparisce insieme al vincolo che la sorvegliava.

**L'unica eccezione: la definizione ricorsiva sul tempo.** Se il valore dipende da grandezze che a
loro volta dipendono dal valore in istanti precedenti — l'importo di una vendita dipende dallo
sconto, lo sconto dal livello, il livello dagli importi delle vendite precedenti — allora
ricalcolarlo richiede un'**induzione sulle date**, che la logica del primo ordine non esprime. Lì
si memorizza, e si **dichiara come assunzione** con questo motivo scritto. È l'unico caso in cui si
memorizza un derivabile.

Attenzione a non confondere due cose diverse: il valore **corrente** (derivato, un'operazione) e il
valore **applicato a una transazione** (un fatto storico, memorizzato sulla transazione). Il primo
cambia da solo quando cambiano i dati; il secondo deve restare quello di allora.

**Una classe non resta scollegata.** Nei 25 diagrammi ufficiali non ce n'è una. Se una classe non
ha nessuna associazione, o è di troppo, o ti sei perso il legame: spesso è il legame *storico* —
non "quale livello ha il cliente", ma "quale livello è stato applicato a questa vendita".

**Se la traccia dice di memorizzare un dato, lo si memorizza**, anche se un suo valore sarebbe
derivabile. Un attributo enumerato dichiarato dai requisiti — *"lo stato attuale, uno fra
disponibile, noleggiato, in manutenzione, rotto"* — è un dato, non una vista: gli altri tre valori
non sono ricavabili da nulla, e il dominio è quello che la traccia elenca.

**Una generalizzazione non è un'appartenenza.** `B` è sottoclasse di `A` solo se ogni `B` **è lo
stesso oggetto** di un `A`, visto più in dettaglio. Se `B` è "un pezzo di" o "una variante di" `A`,
sono due oggetti e ci vuole un'associazione. Tre segnali che stai per sbagliare:

- ti servirebbe **comunque** l'associazione verso la stessa classe, per dire *di quale* `A` si
  tratta — se il legame non entra nell'identità, non è identità;
- la sottoclasse avrebbe un **identificatore proprio**: nei 25 diagrammi ufficiali nessuna
  sottoclasse ne porta uno, ereditano quello della superclasse;
- i **conteggi si rompono**: "quanti `A` ci sono" comincia a contare anche i `B`.

**Su quale classe si mette la generalizzazione: sull'oggetto, non sullo stato.** Quando un oggetto
può trovarsi in forme alternative con **struttura diversa** — esiti, stati, modalità di conclusione
— si specializza **l'oggetto che si trova in quello stato**, non si reifica lo stato in una classe
a parte con le proprie sottoclassi. La tentazione della classe `Esito`/`Stato` collegata `1..1`
all'oggetto è forte proprio quando le alternative sono asimmetriche, ed è sbagliata: introduce una
classe che non ha identità propria, e costringe a un'identificazione esterna inventata.

Nei diagrammi ufficiali non esiste **nessuna** classe reificata di questo tipo — nessuna `Esito`,
`Stato`, `Status`. Le forme alternative sono sempre sottoclassi dell'oggetto: `Riparazione`
generalizza `RiparazioneTerminata` (Officine 1), `Prestazione` generalizza `PrestazioneFinalizzata`
e poi `PrestazioneEseguita` (QuickHospital), `Partita` generalizza `PartitaConPunteggi` e
`PartitaConRinuncia` (Go). Ogni sottoclasse porta la struttura che le è propria: gli attributi in
più, o l'associazione che solo quella forma richiede.

Nel dominio della biblioteca: un prestito può chiudersi con una restituzione (che ha una data) o
con uno smarrimento (che ha un importo di rimborso e un legame col lettore che risponde). Sono
`Prestito` generalizza `PrestitoRestituito` / `PrestitoSmarrito`, non un `Esito` appeso al
prestito.

**Prima di scegliere, conta gli stati: è la decisione che dimensiona la Domanda 7.** Una catena di
stati resa a sottoclassi produce una relazione per stato, e ognuna arriva fino allo schema
relazionale. Misurato su Deli (14-02-2024), che ha otto stati: sei sottoclassi hanno portato lo
schema a **21 relazioni contro le ~15 di una prova tipica**, e la Domanda 7 a 179 righe contro un
limite di 160 — con il taglio ormai impossibile, perché quello che sforava erano relazioni e
vincoli, che non si tagliano.

Il conto da fare **prima** di disegnare, non dopo:

| Stati che portano un dato proprio | Scelta |
|---|---|
| uno o due | sottoclassi, annidate se la progressione è lineare |
| tre o più | sottoclassi solo per quelli con dati, e un **attributo enumerato** per gli stadi che non ne portano — dichiarando la scelta |
| nessuno | attributo enumerato, e basta |

Il criterio non cambia — lo stato che porta un istante vuole la sua sottoclasse — ma quando gli
stadi sono molti conviene sapere in anticipo che ognuno costerà una relazione, un `X_isa_Y` e una
riga nel budget della Domanda 7.

**Attenzione a non confondere questo caso con lo stato simmetrico.** Se le alternative *non*
portano struttura diversa — un video è pubblico o privato, e basta — non sono sottoclassi: è un
**attributo di tipo enumerato** (`stato: stato_video`), come nelle soluzioni ufficiali di TuTubi.
La generalizzazione la giustifica l'asimmetria, o la partizione richiesta dai requisiti.

**Quando *un solo* valore porta struttura**, le due regole si scontrano: l'elenco è chiuso dalla
traccia (che vorrebbe l'enumerato) ma una delle alternative ha un dato in più (che vorrebbe le
sottoclassi). La via che regge le due fasi è **sottoclassi in analisi, fusione in
ristrutturazione**: nel concettuale il diagramma esprime da sé disgiunzione e completezza, e
l'attributo in più sta dove deve; in Domanda 6 la fusione con un attributo discriminatore non
nullo li rende dichiarativi e toglie un join alle operazioni. Motiva entrambi i passaggi — è una
scelta, non un automatismo, e il corpus ha un precedente per l'altra strada (eBuy usa l'attributo
enumerato).

**Ma prima di concludere «non portano struttura», chiediti quando quello stato è stato deciso.**
Uno stato che *qualcuno assegna in un momento* — una prenotazione accettata, rifiutata,
annullata — porta con sé almeno l'**istante della decisione**, e spesso chi l'ha presa: quello è
attributo della sottoclasse, e allora le sottoclassi si giustificano. Il segnale è che stai per
scrivere un solo attributo `stato: enumerato` per un fatto che nella realtà ha una data. Se invece
lo stato è una proprietà che l'oggetto ha e basta, senza un istante in cui è cambiata, l'enumerato
è giusto.

**Attributi multivalore.** La molteplicità di un attributo si scrive in coda, fra parentesi
quadre: `telefono: Telefono [1..*]`, `apertura: Apertura [0..*]`. Le soluzioni ufficiali li usano.
Diventa un attributo multivalore ciò che è **un valore ripetuto dello stesso oggetto**; diventa
invece una classe a sé ciò che ha identità propria, o a cui altri oggetti si associano. In
ristrutturazione l'attributo multivalore genera una relazione aggiuntiva, con un vincolo di
inclusione se la molteplicità minima è 1.

**I tipi di base**, che non vanno specificati, sono quelli che la slide A.1 elenca:
`Intero`, `Reale`, `Booleano`, `Data`, `Ora`, `DataOra`. **`Stringa` non è in quell'elenco**, ma
slide e soluzioni ufficiali la usano ovunque senza mai specificarla (`nome: Stringa`): trattala
come base anche tu, e specifica invece ogni stringa **con un formato** — un codice, una targa,
un'email — che è un tipo concettuale a sé. Tutto il resto — codici, formati, tipi strutturati,
enumerazioni — va definito.

## Domanda 1 — Raffinamento dei requisiti (10', non valutata)

Elenco numerato gerarchico, un requisito per voce, con i rimandi espliciti tra requisiti. Serve
a eliminare ambiguità, omissioni e ridondanze del testo originale.

```
1. Requisiti sui libri. Di ogni libro il sistema deve rappresentare:
	1.1. codice ISBN (v. req. 4), che lo identifica
	1.2. titolo (stringa)
	1.3. numero di pagine (intero positivo)
	1.4. le copie possedute dalla biblioteca (v. req. 2)

2. Requisiti sulle copie. Di ogni copia il sistema deve rappresentare:
	2.1. numero di inventario (stringa), che la identifica
	2.2. il libro di cui è copia (v. req. 1)
	2.3. la sede in cui si trova (v. req. 3)
```

La numerazione poi si riusa: quando una scelta di modellazione è discutibile, il modo pulito di
motivarla è citare il requisito (`v. req. 3.2`).

Non è valutata, ma farla bene rende più veloce tutto il resto — ed è qui che si annotano le
assunzioni sui punti ambigui, invece di lasciarle implicite nel diagramma.

**Un requisito di primo livello per ogni *cosa* di cui il testo parla, non per ogni concetto che
finirà nel diagramma.** Nel raffinamento ufficiale di Esercitazioni universitarie 1 i requisiti di
primo livello sono quattro — insegnamenti, docenti, esercitazioni, esercizi — e il dato che
riguarda la **coppia** esercizio-esercitazione sta annidato sotto l'esercitazione (`3.2. esercizi
compresi, per ognuno: …`), con il rimando. Nel diagramma quel dato diventerà una classe
associativa; nel raffinamento resta dov'è. Promuoverlo a requisito di primo livello non è un
errore, ma allontana il raffinamento dalla struttura del testo, che è quello che il docente segue.

**Le dimensioni, misurate sugli ufficiali:** 4-5 requisiti di primo livello e una ventina di righe
in tutto. Se il tuo raffinamento supera le 30 righe non stai disambiguando, stai riscrivendo il
testo.

## Domanda 2 — Diagramma UML e specifiche (45'/75', eliminatoria)

Quattro artefatti: il diagramma, le specifiche dei tipi di dato, le specifiche di classi e
associazioni, i vincoli esterni.

### Il diagramma, in forma testuale

Usa **esattamente** questa struttura markdown — intestazioni `###` per le classi, elenchi puntati
per gli attributi, una tabella per le associazioni. Non racchiuderla in un blocco di codice e non
sostituirla con testo indentato: in questa forma il diagramma prodotto si confronta
automaticamente con i diagrammi ufficiali, che sono scritti nello stesso formato. Un testo indentato dentro un blocco di codice è
altrettanto leggibile per un umano, ma rende il confronto impossibile.

## Classi

### Libro
- `isbn`: CodiceISBN `{id}`
- `titolo`: Stringa
- `pagine`: Intero > 0

### Copia
- `inventario`: Stringa `{id}`

### CopiaPregiata
_(nessun attributo proprio)_

### Sede
- `codice`: Stringa `{id}`
- `nome`: Stringa

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| copia_libro   | Copia `0..*`   | Libro `1..1` |
| copia_sede    | Copia `0..*`   | Sede `1..1`  |
| sede_citta    | Sede `0..*`    | Citta `1..1` |

## Classi associative

- `Recensione` su `let_libro` — attributi: `voto`: Intero in 1..5, `data`: Data

## Specializzazioni di associazione

- `vend_nuovo` specializza `vendi` — estremi: `ArticoloNuovo` `0..*`, `VenditoreProfessionale` `1..1`

**La riga che conta per il confronto sta però sotto `## Generalizzazioni`**, ed è la forma dei
diagrammi ufficiali (`diagrammi/E.A.1.11 - Officine 1.md`):

```
## Generalizzazioni

- `vendi` generalizza `vend_nuovo` _(fra associazioni)_
```

Scrivi **entrambe**: quella sotto `## Generalizzazioni` perché è la notazione del corso ed è
quella che `confronta_uml.py` legge, la sezione dedicata perché dice anche gli estremi. Ometterla
dalle generalizzazioni fa sparire la specializzazione dal confronto e dal disegno.

## Generalizzazioni

- `Prestito` generalizza `Ricovero`, `PrestitoDomicilio`  **{disjoint, complete}**

Le **operazioni** stanno nella stessa lista puntata degli attributi della loro classe, con le
parentesi e il tipo di ritorno: `- \`n_dipendenti()\`: Intero >= 0`.

Sulle generalizzazioni **si accettano due forme**, e `confronta_uml.py` le fonde per superclasse
prima di confrontarle: i figli tutti su una riga, come sopra, oppure una riga per coppia — che è
quella che `converti-xml.py` produce dai diagrammi ufficiali, perché nell'export ogni arco è un
elemento a sé. Con una riga per coppia **il vincolo va scritto una volta sola**, su una
qualunque delle righe del gruppo: ripeterlo su tutte fa disegnare più annotazioni sullo stesso
insieme di generalizzazione.

**Cosa il renderer sa disegnare, e cosa no.** Il diagramma prodotto viene reso graficamente
(vedi *Come si consegna* in `SKILL.md`), e conviene sapere cosa arriva nell'immagine:

- classi, attributi, operazioni, associazioni con molteplicità, generalizzazioni con i loro
  vincoli: disegnati
- **classi associative**: disegnate col tratteggio verso l'associazione, ma **solo se la classe
  compare anche sotto `## Classi`** oltre che sotto `## Classi associative`. Elencala in
  entrambe le sezioni.
- **specializzazioni di associazione**: PlantUML non ha il costrutto, quindi finiscono in una
  nota a lato. Sono comunque nel documento e nel confronto: l'immagine non le perde, ma non le
  disegna come frecce.
- **le tabelle diverse da quella delle associazioni** non vengono lette come associazioni, ma
  restano leggibili nel documento: puoi usarle liberamente.

Dettagli di forma che contano per il confronto automatico:

- la molteplicità va in backtick subito dopo il nome della classe (`Sede \`1..1\``)
- le generalizzazioni usano il verbo "generalizza", i figli in backtick, e il vincolo
  `{disjoint, complete}` in grassetto a fine riga
- `{id}` si scrive in backtick dopo il tipo dell'attributo (`- \`cf\`: CodiceFiscale \`{id}\``),
  oppure **dentro** i backtick della molteplicità quando l'identificazione è esterna
  (`| scaff_sala | Scaffale \`0..*\` | Sala \`1..1 {id}\` |`)
- le operazioni si scrivono `- **nome()**: Tipo`; la forma `- \`nome()\`: Tipo` è accettata dal
  parser ma la prima è quella che i diagrammi ufficiali producono
- una classe senza attributi propri tiene comunque la sua intestazione `###`, con
  `_(nessun attributo proprio)_` sotto: serve a distinguerla da una dimenticanza
- le sezioni `## Classi associative` e `## Specializzazioni di associazione` si **omettono**
  quando non ce ne sono; non si scrive "nessuna"

Sulla generalizzazione, le **uniche annotazioni che esistono** nel materiale del corso sono
`{disjoint}`, `{complete}` e `{disjoint, complete}`. **`{incomplete}` non esiste**: non compare
in nessuna slide né in nessuna soluzione ufficiale. L'assenza di `complete` *è* l'incompletezza,
e non si annota.

Le quattro combinazioni si scelgono così:

- **`{disjoint, complete}`** — ogni istanza della superclasse è esattamente di una sottoclasse.
  È il caso quando i requisiti dicono che le due categorie esauriscono e si escludono: una
  persona che è o studente o professore.
- **`{complete}` da solo** — le sottoclassi **esauriscono** la superclasse ma possono
  **sovrapporsi**: ogni istanza è di almeno una, e può essere di più d'una. È il caso quando i
  requisiti dicono che non esistono istanze "generiche", ma nulla vieta a un oggetto di stare in
  due categorie. La soluzione ufficiale di QuickHospital fa così con `Persona`, generalizzata in
  `Paziente` e `Medico`: non esistono persone che non siano né l'uno né l'altro, ma un medico può
  benissimo essere anche paziente — ed è esattamente il rilievo che il tutor fa a chi ci mette
  `disjoint`.
- **`{disjoint}` da solo** — le sottoclassi si escludono ma **non esauriscono**, e il caso tipico
  è quello in cui **l'appartenenza si determina solo più tardi**: un prestito diventa
  "restituito" o "smarrito" solo quando si chiude, quindi al momento in cui lo si registra non
  si può imporre che sia già di una delle due. Se ti accorgi che imporre `complete` costringerebbe a
  scegliere una sottoclasse in un istante in cui il dato non c'è ancora, `complete` non ci va.

  Vale ogni volta che le sottoclassi sono **esiti**, anche quando la traccia li elenca come se
  fossero i soli possibili: nel diagramma ufficiale di Go, `Partita` generalizza
  `PartitaConPunteggi` e `PartitaConRinuncia` con **`{disjoint}` e basta**, perché una partita
  registrata e non ancora conclusa non è né l'una né l'altra. Dichiarare l'assunzione «non si
  registrano partite non disputate» per poter mettere `complete` è una scelta più stretta di
  quella del corso: se il dominio ammette l'oggetto prima dell'esito, `complete` è un errore.
- **nessuna annotazione** — le sottoclassi possono sovrapporsi e non esauriscono.

#### Più insiemi di generalizzazione sulla stessa superclasse

Una superclasse può essere partizionata **su più assi indipendenti**, ognuno col suo vincolo. È
il caso della soluzione ufficiale di Accademia 2: `Impegno` è partizionato *per categoria*
(assenza / istituzionale / progettuale) e, in parallelo, *per unità di durata* (a ore / a
giornate intere). Sono due insiemi distinti: ogni impegno è di una sola categoria **e** di una
sola unità, e sono scelte fra loro indipendenti.

Fonderli in un unico elenco produce un modello sbagliato — direbbe che un'assenza non può essere
giornaliera. Quando succede, dichiara gli insiemi con un'etichetta fra quadre:

```
## Generalizzazioni

- `Impegno` generalizza `Assenza`, `Istituzionale`, `Progettuale`  **{disjoint, complete}** [insieme: categoria]
- `Impegno` generalizza `AOre`, `AGiornate`  **{disjoint, complete}** [insieme: durata]
```

L'etichetta non è notazione del corso — sul diagramma i due insiemi si distinguono perché sono
due triangoli separati — ma nel testo serve, altrimenti l'informazione va persa. Nota che
`confronta_uml.py` **fonde comunque per superclasse**: su questo caso il suo verdetto va letto a
mano.

Le due domande da farsi sono indipendenti, e conviene porsele separatamente: *"esiste un'istanza
della superclasse che non è di nessuna sottoclasse?"* decide `complete`; *"può un'istanza stare in
due sottoclassi insieme?"* decide `disjoint`.

### Sequenze: ordine derivato o ordine memorizzato

Un requisito che parla di sequenza ordinata ha due modellazioni, e il discriminante è **se
l'ordine è derivabile dai dati che ci sono già**.

**Derivabile** — l'ordine discende da un istante, da una coordinata, da una coppia di chiavi:
non si memorizza nulla, si calcola con `sorted` e un criterio d'ordine (vedi `fol.md`). È il caso
più frequente e va preferito, perché un ordine memorizzato può contraddire i dati da cui
dovrebbe discendere.

**Non derivabile** — la posizione è una scelta indipendente, che qualcuno decide e il sistema
ricorda. Allora serve un attributo `ordine: Intero > 0` sulla classe reificata, e quell'attributo
non si regge da solo: servono due vincoli esterni che le tracce danno per impliciti:

```
[V.Passaggio.ordini_univoci]
	not EXISTS p1, p2, perc, n   Passaggio(p1) and Passaggio(p2) and p1 != p2 and
	                             pass_perc(p1, perc) and pass_perc(p2, perc) and
	                             ordine(p1, n) and ordine(p2, n).

[V.Passaggio.ordini_contigui]
	ALL p, perc, n   Passaggio(p) and pass_perc(p, perc) and ordine(p, n) and n > 1 -->
	                 EXISTS p2  Passaggio(p2) and pass_perc(p2, perc) and ordine(p2, n - 1).
```

Univocità più esistenza del predecessore danno una numerazione `1..n` contigua. Senza il secondo,
niente vieta tappe numerate 1, 5, 9.

### Specializzazione di attributi e di operazioni

Una sottoclasse non aggiunge solo proprietà nuove: può **specializzare** quelle ereditate,
restringendone il tipo.

```
### ArticoloInVendita
- `nome`: Stringa
- `anni_garanzia`: Intero >= 0

### ArticoloNuovo   (sottoclasse di ArticoloInVendita)
- `codice_ean`: Stringa
- `anni_garanzia`: Intero >= 2      // specializza ArticoloInVendita.anni_garanzia
```

Il tipo specializzato deve essere **più ristretto** di quello della superclasse: `Intero >= 2` è
un sottoinsieme di `Intero >= 0`. Se non lo è, la specializzazione è scorretta.

La **specializzazione di operazioni di classe** funziona allo stesso modo: una sottoclasse può
ridefinire un'operazione ereditata
(l'articolo in offerta calcola il prezzo scontato), e anche qui la segnatura della sottoclasse
deve restringere quella della superclasse, non cambiarla. La specifica della versione
specializzata va data insieme a quella della classe che la ridefinisce.

In FOL entrambe sono implicate dal diagramma e non si riscrivono fra i vincoli esterni.

### Specializzazione di associazioni

Una classe associativa **è anche una classe**: può essere terminale di altre associazioni ed
essere radice di relazioni IS-A. Da qui la specializzazione di associazioni.

Due condizioni di correttezza, che il corso tratta a parte perché è dove si sbaglia:

- **Compatibilità di tipo.** Gli estremi della sotto-associazione devono essere sottoclassi dei
  corrispondenti estremi della super-associazione.
- **Le molteplicità sono fuorvianti, e vanno ricontrollate.** La sotto-associazione **eredita** i
  vincoli della super-associazione, quindi la molteplicità che scrivi su di essa non è quella che
  vale davvero. Prima di consegnare, verifica quale molteplicità il diagramma implica, non quella
  che hai scritto.

#### Il ruolo distinto è una specializzazione, non un'associazione a sé

È il caso più frequente e quello che si sbaglia più spesso. Quando due classi sono legate da
un'associazione generale e in più da **ruoli distinti**, i ruoli non sono associazioni
indipendenti: sono **specializzazioni** di quella generale.

Il caso tipico: uno scambio interbibliotecario coinvolge esattamente due sedi, e una delle
due ha il ruolo di prestante. Modellare `coinvolge` e poi `prestante` come due associazioni
separate lascia passare uno stato assurdo — la sede prestante potrebbe non essere fra le due
coinvolte. Con la specializzazione il vincolo è nel diagramma:

```
| associazione | estremo A | estremo B |
|---|---|---|
| coinvolge    | Sede `2..2` | Scambio `0..*` |
| prestante    | Sede `1..1` | Scambio `0..*` |
| richiedente  | Sede `1..1` | Scambio `0..*` |

## Generalizzazioni

- `coinvolge` generalizza `prestante`, `richiedente` **{disjoint, complete}** _(fra associazioni)_

## Specializzazioni di associazione

- `prestante` specializza `coinvolge`
- `richiedente` specializza `coinvolge`
```

Due avvertenze su questo blocco, perché sono gli errori che si fanno scrivendolo:

- **le due sezioni vanno in direzioni opposte** — sotto `## Generalizzazioni` il soggetto è la
  super-associazione (`coinvolge` **generalizza** `prestante`), nella sezione dedicata è la
  sotto-associazione (`prestante` **specializza** `coinvolge`). Scriverne una al rovescio inverte
  il verso della freccia;
- **tieni la stessa classe sempre nella stessa colonna** per tutte le righe della tabella: se
  `Sede` sta in colonna A per `coinvolge`, ci sta anche per `prestante` e `richiedente`. Il
  confronto legge le coppie per posizione, e alternarle fa risultare divergenti associazioni
  identiche.

Il `{disjoint, complete}` sulla generalizzazione **fra link** dice che ogni coinvolgimento è o
il lato prestante o quello richiedente, e i due non coincidono. Senza di esso servirebbero due
vincoli esterni in FOL per dire la stessa cosa: il diagramma lo esprime meglio.

Lo stesso vale per i ruoli che compaiono **solo a cose fatte**. Un'associazione che collega le
stesse due classi per registrare un esito — quale sede ha poi smarrito il volume, quale lo ha
restituito in ritardo — specializza anch'essa l'associazione generale: è così che si vincola
che si riferisca a **quello** scambio e a una sede che vi ha davvero preso parte.

> Vale anche quando i due estremi sono la stessa classe due volte e i ruoli si chiamano come i
> due contendenti di una gara: la forma è questa, qualunque sia il dominio.

#### Un dato che vale *per partecipante* sta sull'associazione generale

Quando due oggetti della stessa classe partecipano allo stesso fatto con ruoli distinti — i due
giocatori di una partita, le due sedi di uno scambio — e ognuno porta un proprio valore, quel
valore **non si sdoppia in due attributi con il nome del ruolo**. `punti_bianco` e `punti_nero`
sulla partita sembrano naturali e sono la strada sbagliata: legano il dato al ruolo invece che al
partecipante, e non reggono se i ruoli diventano tre.

La forma del corso è una **classe associativa sull'associazione generale**, con l'estremo che
porta la molteplicità del gruppo: nel diagramma ufficiale di Go il punteggio è una classe
associativa su `PartitaConPunteggi 0..* — Giocatore 2..2`, non due attributi della partita.

Il segnale per riconoscerlo: **stai per scrivere due attributi che differiscono solo per il nome
del ruolo.** Allora il dato è del partecipante, e va sull'associazione che lo lega al fatto.

#### Reificare non toglie i ruoli distinti

Quando un'associazione va reificata in una classe — perché la stessa coppia può ripetersi, o
perché porta attributi — i ruoli distinti **restano associazioni a sé**, con i loro attributi.

Un percorso di ricollocazione tocca molti scaffali, anche due volte lo stesso: serve una classe
`Passaggio`. Ma il primo e l'ultimo scaffale non sono passaggi qualsiasi, e hanno dati propri —
l'ora di inizio, il tempo impiegato — quindi restano due associazioni distinte,
`scaffale_iniziale` e `scaffale_finale`. La classe reificata modella la ripetizione; le
associazioni distinte modellano gli estremi, che ripetizioni non sono.

Il criterio è: **hanno dati propri?** Se il primo e l'ultimo elemento non portano nulla che gli
altri non abbiano, sono solo le posizioni 1 e n della sequenza e non servono associazioni in più.

I nomi delle associazioni sono corti e in minuscolo, spesso composti dalle classi coinvolte
(`prest_copia`, `copia_libro`, `let_prest`). Diventano simboli di predicato nella FOL e nomi di
relazione nello schema, quindi conviene sceglierli una volta bene.

**Come si legge una molteplicità:** il numero scritto accanto a una classe dice quante *sue*
istanze partecipano all'associazione per ogni istanza dell'altra classe. In
`copia_sede | Copia 0..* | Sede 1..1` il `1..1` accanto a `Sede` dice che ogni copia si trova
in esattamente una sede; lo `0..*` accanto a `Copia` dice che una sede può contenere molte
copie, o nessuna.

È l'opposto della convenzione ER, dove il vincolo sta sull'estremo opposto: se stai traducendo
da una soluzione in ER, questa è la cosa da ribaltare.

#### Un limite che viene dai dati è un attributo, non una molteplicità

La domanda è **se il numero è lo stesso per tutte le istanze**.

- **uguale per tutte** — due sedi per uno scambio, due giocatori per una partita: è una regola del
  dominio e va nella molteplicità (`2..2`);
- **diverso da istanza a istanza** — la capienza di una sala, il tetto di iscritti di un corso: è
  un **attributo** del contenitore, con la molteplicità larga (`0..*`), e il legame fra i due
  diventa un vincolo esterno realizzato con un trigger.

Il caso che inganna è quello in cui la traccia enuncia un limite uniforme — *«una stanza può
contenere da un minimo di 1 a un massimo di 8 posti letto»* — e la molteplicità `1..8` sembra la
traduzione esatta. Lo è, e non è un errore; ma il concettuale ufficiale di QuickHospital sceglie
lo stesso l'attributo, `capienza: CapienzaStanza`, perché modella la capienza **della singola
stanza** invece del limite di legge, ed è un dato in più che i requisiti non vietano. Delle due,
la seconda è più vicina al modo di lavorare del corso («meglio un attributo in più che un vincolo
in più»); la prima è difendibile, e va dichiarata.

#### Un parametro che dipende *solo* da una classe è un attributo di quella classe

Il caso: «la velocità massima consentita è un parametro del sistema, che può dipendere anche dalla
classe del veicolo». La tentazione è farne una classe associativa fra il dispositivo che applica il
limite e la classe di veicolo — così ogni dispositivo può avere il suo. Ma la traccia dice che
dipende **dalla classe del veicolo**, non dalla coppia: l'attributo va su `ClasseVeicolo` e basta.

Il criterio è quello dell'`attr/3`: una classe associativa esiste quando il dato ha bisogno di
**entrambi** gli estremi per essere determinato. Se un estremo basta, il dato è un suo attributo, e
la classe associativa aggiunge una libertà che i requisiti non chiedono — cioè un modo di sbagliare
in più, e vincoli in più da scrivere. Il controllo è meccanico: prova a leggere il dato come
funzione di un estremo solo; se la frase della traccia regge, non è una classe associativa.

**E due limiti distinti restano due attributi.** *«il volume di traffico sostenibile in entrata ed
in uscita»* sono due numeri, non uno: `volMaxEntrata` e `volMaxUscita`. Sono le letture affrettate
che costano una classe o un attributo, non i concetti difficili.

#### Il minimo si mette a 0, salvo prova contraria

È l'errore che ricorre più di ogni altro. Sui 356 estremi dei 23 diagrammi ufficiali il prof usa:

| molteplicità | volte |
|---|---|
| `0..*` | 167 |
| `1..1` | 135 |
| `0..1` | 20 |
| `1..*` | **14** |

`0..*` e `1..1` da soli coprono l'85%. Il **minimo 1 sul lato "molti"** compare 14 volte su 356,
e sempre per lo stesso motivo: **l'oggetto non può esistere senza almeno un legame**. Un medico
senza nessuna specializzazione non è un medico; un corso di laurea fuori da ogni facoltà non
esiste. È l'unico caso in cui `1..*` si scrive.

Che sia una scelta forte lo dice il prof stesso: è l'unica cosa che annota a mano sul diagramma
di Università 2 — *"La scelta dei vincoli di molt. 1..\* sottende che un CdL, per esistere, deve
essere sempre incardinato in almeno una facoltà ed includere almeno un insegnamento"*.

Prima di scrivere un minimo 1, fatti questa domanda: **posso creare l'oggetto prima di avere il
legame?** Se un insegnamento può essere istituito prima che gli si assegni un docente, allora è
`0..*`, non `1..*`. Nel dubbio, `0`. Un minimo troppo largo è un modello permissivo; un minimo
troppo stretto rende inserribili solo oggetti completi, ed è un requisito che nessuno ha chiesto.

Un esempio completo e ufficiale è in `BDD2-corpus-nuovo/diagrammi/` (31 diagrammi dagli export
dei progetti Visual Paradigm del corso, con accanto il PNG dell'autore). Per la resa visuale
della **tua** soluzione usa `scripts/uml2png.py` o `scripts/componi.py`, che disegnano con
`tools/plantuml.jar` dentro al corpus; mai generare `.vpp`.

### Specifica dei tipi di dato

Solo i tipi non di base. I tipi strutturati elencano i campi; quelli vincolati danno il pattern.
Un tipo di dato può avere vincoli e operazioni, come una classe.

```
Specifica dei tipi di dato

Periodo:
	- da:DataOra [0..1]
	- a:DataOra [0..1]

	[V.Periodo.legale]
		ALL p, x, y   Periodo(p) and da(p, x) and a(p, y) --> y >= x.

	interseca(p1:Periodo, p2:Periodo):Booleano
		pre: nessuna
		post:
			result = vero se e solo se i due periodi hanno almeno un istante in comune.

			Gli estremi sono opzionali: un 'da' assente vale -infinito, un 'a' assente
			vale +infinito. Le guardie universali rendono la formula corretta anche in
			quei casi, perche' l'antecedente e' falso e la condizione non morde.

			Formalmente:

			result <--> [ ( not EXISTS a1, d2  a(p1, a1) and da(p2, d2) and a1 < d2 )
			              and
			              ( not EXISTS a2, d1  a(p2, a2) and da(p1, d1) and a2 < d1 ) ].

CodiceFiscale: Stringa che soddisfa l'espressione regolare
	'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
	(6 lettere per cognome e nome, 2 cifre di anno, 1 lettera di mese, 2 cifre di
	 giorno, 4 caratteri di comune, 1 carattere di controllo)

Email: Stringa che soddisfa l'espressione regolare
	'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

Telefono: Stringa che soddisfa l'espressione regolare
	'^\+?[0-9]{6,15}$'

Indirizzo:
	- via: Stringa
	- civico: Stringa che soddisfa l'espressione regolare '^[0-9]+[A-Za-z]?$'
	- cap: Stringa che soddisfa l'espressione regolare '^[0-9]{5}$'

TipoPrestito: tipo enumerato, con i soli valori ammessi
	{ breve, ordinario, lungo }
```

Le **enumerazioni** sono il terzo caso, accanto ai tipi strutturati e a quelli con un formato:
si elencano tutti i valori ammessi, senza abbreviare. I valori si scrivono **senza virgolette**:
la slide A.1 è esplicita, *"non è una stringa, ma un simbolo (valore del tipo enumerativo)"*.

Per un intervallo numerico la notazione del corso è `in a..b` — `Reale in 18..30`, `Intero in
1..5` — e si può usare inline nel tipo di un attributo. In fase di progettazione diventeranno un
`create type ... as enum`, oppure una relazione a sé se nel frattempo la classificazione è
cresciuta fino a meritare una classe.

**Le espressioni regolari si scrivono per esteso.** Le soluzioni ufficiali mettono `~ '...'`
perché il docente lascia il formato come esercizio: è una scorciatoia didattica, non la forma
attesa in una risposta. Lo stesso vale per le operazioni dei tipi di dato, che nell'originale
finiscono spesso con `... // per esercizio` e qui invece vanno specificate.

I tipi con struttura interna (`Periodo`, `Indirizzo`, `CapienzaSala`) sono quelli che in
ristrutturazione diventeranno `CREATE TYPE` o relazioni aggiuntive: definirli qui con cura fa
risparmiare lavoro alla Domanda 6.

### Specifica delle classi e dei vincoli esterni

Per classe: le operazioni di classe con pre/post, e i vincoli esterni che la riguardano.

```
Classe Prestito e sottoclassi

Classe Prestito

[V.Prestito.istante_presunto_dopo_istante_rich]
	ALL p, ipren, ipres  Prestito(p) and istante_rich(p, ipren)
	                     and inizio_previsto(p, ipres) --> ipres >= ipren.

Classe PrestitoScaduto
	periodo():Periodo
		pre: nessuna
		post:
			result soddisfa:
			EXISTS i   da(result, i) and inizio(this, i)
			           and (not EXISTS f  a(result, f))
```

I vincoli si nominano `[V.Classe.cosa_dice]`. Il nome viene riusato in ristrutturazione e nella
realizzazione SQL, quindi deve essere descrittivo.

Vanno scritti solo i vincoli che il diagramma **non** esprime già. Molteplicità, tipizzazione,
generalizzazioni e specializzazioni sono implicate dal diagramma: riscriverle è rumore. Vedi
`fol.md`, sezione "Quello che il diagramma già dice".

**Che cosa può entrare in un identificatore, alla lettera.** La slide A.1 lo dice come
avvertenza, e uno degli sbarramenti ufficiali ci costruisce sopra una domanda: *«un vincolo di
identificazione di classe può coinvolgere solo attributi a molteplicità `[1..1]` e/o ruoli della
classe a molteplicità `1..1`»*. Quindi: niente `{id}` su un attributo opzionale o multivalore, e
niente identificazione esterna attraverso un estremo `0..1` o `0..*` — nel quiz del 2020-06-08 il
diagramma sbagliato è proprio quello che identifica attraverso un ruolo `(0,N)`, e la risposta lo
chiama *«sintatticamente illegale»*. Se l'estremo su cui vorresti appoggiarti non è `1..1`, o la
molteplicità è sbagliata o l'identificazione è un'altra.

L'**identificazione non fa eccezione**: è un costrutto del diagramma e non va mai riscritta come
vincolo esterno. Si segna `{id}` sull'attributo che identifica; se l'identificatore è composto si
segna su tutti gli attributi che lo compongono; se è **esterno**, cioè coinvolge un'associazione,
`{id}` va **in tutti e due i posti**: sull'attributo *e* sull'estremo dell'associazione verso
la classe che fa da ambito. Come `Sala \`1..1 {id}\`` nella soluzione ufficiale di QuickHospital,
dove il numero dello scaffale identifica solo dentro la sua sala — e lì l'attributo `n` porta
`{id}` a sua volta.

**Nel concettuale non si inventa un identificatore.** Se la traccia non dice come si identifica
una classe, le strade sono due — l'identificazione esterna attraverso un'associazione, oppure
**nessun identificatore affatto**. La seconda è legittima e non è un ripiego: nel diagramma
concettuale ufficiale di QuickHospital la classe `Prestazione`, che è la classe centrale del
progetto, ha due attributi e **nessun `{id}`**, né sull'attributo né su un estremo. Il surrogato
compare solo nello schema ristrutturato, come `Prestazione(__id__:serial, ...)`.

Vale in tutti i diagrammi ufficiali: gli `id` e gli `identificatore` surrogati stanno **solo**
nei diagrammi ristrutturati (TuTubi, Officine 3), mai nei concettuali. Dove invece un
identificatore nel concettuale c'è, è la traccia a nominarlo — il `codice` delle crociere di
Travel to the Moon è scritto nel testo del progetto.

Quindi: inventare un `codice: Stringa {id}` che la traccia non nomina è un errore, non una
prudenza. Il surrogato si introduce nella **Domanda 6**, motivandolo, dove `progettazione.md`
spiega come.

**Attenzione a non confondere il surrogato inventato con il dato che la realtà ha di sicuro.** Un
identificatore che esiste nel mondo e che nessuno metterebbe in dubbio — il codice fiscale di una
persona, la targa di un veicolo, l'ISBN di un libro — è un **dato ovviamente necessario**, di
quelli che `errori.md` dice di modellare anche se la traccia non li scrive: il concettuale
ufficiale di QuickHospital ha `Persona` con `cf: CodiceFiscale {id}` senza che i requisiti lo
nominino. Quello che non si inventa è un identificatore **tecnico**, che esiste solo perché ti
serviva una chiave. La domanda da farsi: *questo codice esiste anche fuori dal mio database?*

Segnarlo su un posto solo non è un errore fatale: nelle esercitazioni più vecchie (Officine 1)
il prof marca solo l'estremo, e in Università 2 e Voli aerei 2 non lo marca affatto. Il
riferimento è il progetto QuickHospital, che è completo; le esercitazioni sono volutamente
parziali. Ma **la marcatura in più non è mai un errore**: la mancanza sì, se toglie
un'informazione che serve a chi legge.

**Un vincolo che parla di una transizione non ha formula, e si dichiara qui lo stesso.** «Una
prenotazione confermata non torna in attesa», «un video censurato non torna visibile» mettono in
relazione lo stato prima e quello dopo: la logica del primo ordine parla di un singolo stato, e
non li esprime. Non è un'eccezione alla regola che i vincoli si formalizzano — è un vincolo di
tipo diverso. Enuncialo fra i vincoli esterni con il suo nome `[V....]`, scrivi **in una riga
perché non ha formula**, e rimanda alla Domanda 6, dove `progettazione.md` spiega come si realizza
sul cambiamento (trigger su `old`/`new`, o politica di accesso). Lasciarlo fuori dall'analisi
significa perderlo.

I vincoli che il diagramma non cattura sono tipicamente: condizioni tra attributi della stessa
classe, non sovrapposizione temporale, coerenza tra date, inclusione fra associazioni che il
diagramma non dichiara come specializzazioni. **Non** completezza e disgiunzione delle gerarchie:
quelle le dice il diagramma, e diventano vincoli esterni solo in ristrutturazione (vedi `fol.md`).

## Domanda 3 — Diagramma degli use-case (5'/10')

Attori e use-case, con le associazioni attore-use-case e le eventuali dipendenze `<<include>>` /
`<<extend>>` e generalizzazioni. Ad alto livello: raggruppa le funzionalità per attore, non una
casella per operazione.

Il diagramma degli use-case si scrive in forma testuale, **nel formato dei diagrammi ufficiali**:
una sola sezione `## Use case`, gli attori e gli use-case su due righe di elenco, poi una riga per
ogni legame. È l'unico formato che il renderer disegna, e quello che `converti-xml.py` produce
dagli export del docente. Non disegnarlo in ASCII.

```
## Use case

Attori: `Bibliotecario`, `Lettore`, `Tornello`

Use case: `GestionePrestiti`, `Catalogazione`, `VerificaMorosita`

- `Bibliotecario` — `GestionePrestiti`
- `Lettore` — `GestionePrestiti`
- `Bibliotecario` — `Catalogazione`
- `GestionePrestiti` `<<include>>` `VerificaMorosita`
- `SollecitoRitardo` `<<extend>>` `GestionePrestiti`
- `Bibliotecario` generalizza `Direttore`
```

Attori, use-case, associazioni, inclusioni, estensioni e generalizzazioni stanno tutti in
quell'unico elenco: è così che il formato distingue i legami, dal simbolo o dal verbo che portano.

**In otto diagrammi degli use-case ufficiali su otto, `<<include>>` ed `<<extend>>` non compaiono
mai.** Il docente mette attori, use-case e i legami fra loro, e basta. La sintassi qui sotto resta
perché il costrutto esiste ed è nel programma, ma usarlo è **allontanarsi dalla forma del corso**:
prima di scrivere un `<<include>>`, chiediti se quella cosa non sia semplicemente **uno use-case a
sé**, associato al suo attore.

Misurato: nella prova su TuTubi l'unica divergenza dal diagramma ufficiale è stata proprio questa —
la visualizzazione di un video, che l'ufficiale ha come use-case dell'utente, è finita come
`VerificaVisione` inclusa in un altro use-case, e la funzionalità è sparita dalla vista.

**`<<include>>` o `<<extend>>`?** La differenza è fra obbligatorio e condizionale.

- **`include`** — comportamento **obbligatorio e condiviso**, estratto per riuso: il caso base
  *non è completo* senza l'incluso. Lo si scopre dopo aver scritto tutti gli use-case, notando
  una sequenza che si ripete identica (un'autenticazione, un controllo di validità, un calcolo).
  Il caso base sa dei suoi inclusi; l'incluso non sa chi lo include.
- **`extend`** — comportamento **condizionale o opzionale**, cioè un flusso alternativo: si
  innesta nel caso base a un punto di estensione, e solo se la condizione è verificata. Si usa
  quando un'alternativa diventa abbastanza complessa da meritare un use-case a sé.

Il test rapido: se togliendo quel comportamento il caso base resta sensato, è `extend`; se il
caso base diventa incompleto, è `include`.

**Generalizzazione tra attori**: l'attore B può fare le veci di A e ne eredita tutte le
associazioni — i manager accedono a tutti gli use-case della segreteria. Vale anche fra use-case,
quando uno è una variante specializzata di un altro.

**Ma la generalizzazione degli use-case è più povera di quella delle classi**, e la slide A.1 lo
dice esplicitamente: *«nei diagrammi degli use-case non possiamo usare generalizzazioni uniche che
coinvolgono più sotto-usecase, né tantomeno vincoli `{disjoint}` e `{complete}`»*. Quindi una
freccia per figlio, e **nessuna annotazione** sul fascio: `{disjoint}` o `{complete}` su un
diagramma degli use-case sono un errore di notazione, non una precisazione in più.

Un avvertimento che le slide danno esplicitamente: **gli attori non sono classi.** Il diagramma
degli use-case non implica che esistano `Segreteria` o `Manager` nel diagramma delle classi, né
che la gerarchia fra attori corrisponda a una generalizzazione fra classi. Sono due modelli
separati, e mescolarli è un errore di lettura frequente.

## Domanda 4 — Segnature delle operazioni (10')

Solo le segnature, raggruppate per use-case. Nome, parametri tipati, tipo di ritorno.

```
Use-case GestionePrestiti
	copie_disponibili(l:Libro): Intero >= 0
	nuovo_prestito(let:Paziente, c:Copia): Prestito

Use-case Statistiche
	durata_media_prestiti(da:Data, a:Data): Reale >= 0
```

**L'attore che invoca non è un parametro, e vale già da qui.** Se un'operazione è riservata a un
ruolo — il medico che chiede il proprio itinerario — l'identità di chi la invoca arriva dal
contesto, non dalla segnatura: né in Domanda 4 né in Domanda 5. Si lega con una riga in testa alla
specifica, come fa la soluzione ufficiale di QuickHospital (*«Sia m:Medico l'oggetto associato
all'attore che ha invocato l'operazione»*), e la stessa riga si ripete in Domanda 8.

I tipi possono portare vincoli inline (`Intero > 0`, `Reale >= 0`): è la notazione del corso, non
uno strappo. Qui vanno **tutte le operazioni di use-case**, non solo quelle da specificare alla
Domanda 5. Le operazioni **di classe** e quelle dei tipi di dato appartengono invece alla
Domanda 2, dove sono già dichiarate nel diagramma e specificate: non si ripetono qui.

## Domanda 5 — Specifiche delle operazioni in FOL (30'/60', eliminatoria)

**Solo le operazioni che servono ai requisiti contrassegnati dalla barra laterale**, più le
operazioni ausiliarie che quelle richiamano. Dichiara esplicitamente quali sono, prima di
scriverle: sviluppare le operazioni sbagliate costa quanto sbagliarle.

La struttura e le regole della logica sono in **`fol.md`** — leggilo prima di scrivere formule.
In sintesi: segnatura, `pre:` (o `pre: nessuna`), `post:`, spiegazione discorsiva e poi la
formula introdotta da *"Formalmente"*; risultato sempre `result`; vocabolario identico a quello
della Domanda 2; ogni variabile legata alla sua classe; side effect elencati con `ALPHA`.

```
Specifica use-case GestionePrestiti

	copie_disponibili(l:Libro): Intero >= 0
		pre: nessuna

		post:
			- Sia C = { c | c:Copia and (c,l):copia_libro }
			- Sia P = { p | p:Prestito and
			                EXISTS c  c in C and (p,c):prest_copia and p.aperto() }

			result = |C| - |P|
```

Attenzione a non scrivere precondizioni **vacue**: se l'associazione ha molteplicità `1..1`,
"esiste un link che coinvolge l'argomento" è già garantito dal diagramma, e metterlo fra le
precondizioni è lo stesso rumore di riscrivere una molteplicità fra i vincoli esterni. Si scrive
`pre: nessuna`.

Se l'operazione richiamata è un'**operazione di classe** — `p.aperto()`, `t.durata_gg()` — è già
specificata alla Domanda 2 e qui si richiama e basta: riscriverla è la stessa duplicazione che la
Domanda 4 evita non elencandola. La regola qui sotto riguarda le operazioni di **use-case**.

Se un'operazione ne richiama un'altra (`copie_disponibili` dentro la precondizione di
`nuovo_prestito`), va specificata anche quella: è una delle "operazioni ausiliarie" che la
traccia include nella richiesta.
