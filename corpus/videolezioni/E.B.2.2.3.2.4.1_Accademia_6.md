# Trascrizione: E.B.2.2.3.2.4.1_Accademia_6

[00:00:00] Benvenuti in questo webinar nel quale affronteremo l'esercitazione academia 6 che riguarda il linguaggio SQL e in particolare le interlocazioni con tre gruppamenti.
[00:00:12] Ne ricordiamo velocemente lo schema relazionale.
[00:00:16] Abbiamo diversi domini enumerativi, in particolare il dominio strutturato,
[00:00:23] che rappresenta le diverse posizioni che un docente può avere all'interno dell'università.
[00:00:30] Le tipologie dei lavori svolti nell'ambito di progetti universitari,
[00:00:37] nel dominio inoperativo, il lavoro progetto,
[00:00:40] analogamente i lavori, l'attività non progettuali, quindi didattica, ricerca, missione, eccetera.
[00:00:50] Le cause di un'assenza, il dominio posinteger come al solito, una stringa M media come
[00:01:01] parcia al 100, un numero di ore che è un intero compreso tra la 0 e 8 e il dominio
[00:01:07] che è semplicemente in questo caso un numero reale e maggioro quale a zero.
[00:01:11] Ricordo anche velocemente lo schema rilazionale, quindi abbiamo le persone,
[00:01:19] cioè gli strutturati dell'università, i quali hanno quindi una posizione che
[00:01:27] ha un valore di tipo strutturato e uno stipendio. I progetti hanno oltre un
[00:01:35] idea o nome, una data di inizio, una rifine e un budget in denaro. I work package vp sono le
[00:01:46] singole unità in cui è suddiviso un progetto, quindi si riferiscono a un progetto, hanno nome,
[00:01:53] in unizio è una fine. Dopodiché abbiamo le attività di progetto che sono attività svolte
[00:02:03] da singole persone nell'ambito di un work package, di un progetto, per cui abbiamo la persona
[00:02:08] il progetto, il work package, un giorno, una tipologia, il tipo lavoro progetto e la durata
[00:02:15] in ore. Analogamente abbiamo le attività non progettuali che sono attività svolte da
[00:02:21] persone, non nell'ambito di un progetto, per cui hanno semplicemente il tipo che è un lavoro
[00:02:27] non progettuale, una data e una durata in ore. Abbiamo quindi anche le assenze che sono,
[00:02:35] senza delle persone, quindi abbiamo che ferimento a persona, il tipo e il giorno. Andiamo a vedere
[00:02:46] quindi le quelle sequelle che ci viene richiesto di spolgere. La prima ci chiede di calcolare
[00:02:55] quanti sono gli strutturati in ogni fascia, quindi per ognuna delle possibili posizioni
[00:03:05] che sono ricercatore, professore associato e professore ordinario, ci viene chiesto di contare
[00:03:11] quante sono le persone con tale posizione. Ora andiamo a scriverla. Sicuramente qui dovremmo usare
[00:03:24] l'aggregato count che ci permette di contare il numero di record all'interno del risultato di una
[00:03:34] ovviamente se semplicemente noi scrivissimo qualcosa del tipo select
[00:03:40] star count star from persona avremo il numero totale per esempio as numero
[00:03:53] avremo il numero totale di persone, noi in realtà però vogliamo il numero
[00:03:59] totale, il numero di persone per ogni fascia e questo lo otteniamo semplicemente utilizzando
[00:04:06] il costo group by chiedendo però questo è necessario nella target list quindi nella
[00:04:15] cosa la select anche la posizione questo punto noi raggruppiamo il risultato per
[00:04:24] posizione che vi ricordo essere un campo della tabella persona questo punto noi
[00:04:35] noi avremmo nel risultato un insieme di coppie posizione numero dove posizioni sono tutti
[00:04:48] i valori del campo posizione per le n presenti in persona e per ogni uno di questi avremmo
[00:04:57] il numero di persone con quella posizione.
[00:05:02] senza l'aggregato avremo un numero solo, per cui qui è assolutamente necessario, questa
[00:05:09] query è molto semplice, possiamo già andare avanti con la seconda. La seconda in realtà,
[00:05:18] come possiamo vedere, ci chiede di calcolare quanti sono gli strutturati con uno stipendio
[00:05:24] maggiore uguale di 40.000. Beh anche qui lo stipendio andiamo a vedere è un campo di
[00:05:35] persona per cui banalmente non ci viene anche chiesto di selezionare gli
[00:05:42] strutturati con una certa posizione per cui possiamo semplicemente contare con
[00:05:51] count a numero, contiamo gli strutturati quindi tutte le persone in questo caso
[00:06:01] front persona e sotto la condizione che lo stipendio sia maggiore o uguale di
[00:06:14] 40.000. Non abbiamo raggruppamenti da fare poiché non ci viene chiesto di
[00:06:27] di suddividere l'ustipendio per ogni posizione ad esempio.
[00:06:31] Andiamo avanti con la terza query, quanti sono i progetti già finiti che superano il budget
[00:06:39] di 50.000? Anche questa è una query molto semplice, cerchiamo di andare ragionevolmente
[00:06:46] esperiti su queste. Beh quanti sono, già quanti ci fa capire che anche qui dobbiamo
[00:06:55] usare un aggregato, in particolare l'aggregato count, per cui andiamo a contare tutte le
[00:07:09] annuble, la query, sicuramente dovremo avere nella clausa la prompt progetto, il progetto
[00:07:21] ha sia la data di fine che il budget, per cui ci basterà solo progetto, e quindi
[00:07:34] si viene chiesto e selezionati i progetti già finiti quindi fine deve essere
[00:07:44] minore uguale, minore di current time stamp e il budget deve essere maggiore di 50 mila
[00:08:03] Anche questo è una query con aggregato senza raggruppamento, semplice.
[00:08:18] Andiamo quindi nella quarta query a usare altri aggregati.
[00:08:24] Ricordiamo che oltre all'aggregato count che, con il numero di ennuple selezionate,
[00:08:36] Possiamo usare anche gli aggregati Average, AVG, Min e Max che ci distribuiscono quindi il valore medio, il minimo e il massimo, però di valori numerici selezionati.
[00:08:53] Per esempio nella quarta query, qual è la media il massimo e il minimo delle ore dell'attività relativa al progetto Pegasus?
[00:09:01] qui possiamo facilmente usare gli aggregati average min e max, però non avrebbe senso
[00:09:15] scrivere qualcosa del tipo average star, from per esempio persona, perché la media
[00:09:25] può essere ovviamente definita e definita solamente su valori numerici, per cui qui
[00:09:32] dobbiamo passare, dobbiamo selezionare dei campi, anzi un solo campo numerico, così che l'aggregato
[00:09:41] possa calcolare la media su una colonna o su un'espressione che distituisce tape un numero per
[00:09:50] ogni ennubla. A questo punto dobbiamo distribuire la media il massimo e minimo delle ore di attività
[00:10:00] per cui qui non è persona, ci serve sicuramente il progetto perché dobbiamo
[00:10:07] selezionare il progetto di nome Pegasus con il progetto PLEJ e ci servono anche le
[00:10:16] attività progettuali che hanno, ricordiamo, le ore di durata, quindi
[00:10:24] attività, il progetto A. A questo punto partiamo dalla, dalla cloud
[00:10:35] togliere le parti semplici, il progetto deve avere un, un nome che pegasus e il progetto
[00:10:59] nell'attività deve essere l'indidio del progetto, deve essere proprio appunto progetto ok quindi
[00:11:20] ci servono tutte le attività questo punto dobbiamo calcare la media in massimo il minimo quindi
[00:11:32] a punto ore durata, lo chiamiamo as media, qui nella target list possiamo usare quanti
[00:11:54] aggregati vogliamo, è importante che ognuno chiaramente sia espressione la forma corretta,
[00:12:02] per cui anche il massimo max di a.ore durata as massimo e analogamente min a.ore durata as
[00:12:23] minimo. Questa quale quindi distribuirà tre numeri ci aspettiamo che il primo numero
[00:12:38] sia un numero reale perché è una media mentre il secondo valore e il terzo saranno due numeri
[00:12:48] interi compresi tra 1 e 8 anche questa query non necessita di raggruppamenti perché ci viene
[00:12:59] chiesto solamente la media il massimo il minimo delle ore di tutti i docenti su un singolo progetto
[00:13:09] Vediamo adesso la quale è successiva, quali sono le medie, i massimi minimi delle ore giudnagliele
[00:13:16] dedicate al progetto Pegasus da ogni singolo lucente, questa quale fondamentalmente ci
[00:13:23] chiede di calcolare i stessi valori della quarta però per ogni singolo lucente, quindi
[00:13:36] la riscriviamo da 0 per non commettere le tue ture, nel risultato noi ci aspettiamo di
[00:13:41] avere delle ennoble in Q e per ognuna avere il nome guidati in generale di un docente
[00:13:52] e il numero medio, il numero massimo e il numero minimo di ore totali di attività svolte
[00:14:03] da quel docente nell'ambito del progetto Pegasus, per cui sicuramente ci servirà anche persona
[00:14:14] qui, perché dovremmo prendere i dati dei singoli docenti. Quindi selezioniamo per s punto
[00:14:29] id, as, id persona, per completanza selezioniamo anche il nome, il cognome del docente, as
[00:14:44] nome e poi analogamente prima ci servirà il numero medio di ore, il numero massimo
[00:15:03] di ore e il numero minimo di ore quindi qui ci servirà come sempre logetto prg e attività
[00:15:26] il progetto a questo punto nella clause la guerra dobbiamo sempre importe che il nome
[00:15:35] del progetto sia sia pregasus qui mi l'ho dimenticato un end e che l'attività del il progetto
[00:15:55] dell'attività sia pg.id qui però ci serve anche poiché stiamo andando a contare per
[00:16:07] per ogni persona, il totale dell'eore, anzi la media il massimo minimo dell'eore, dobbiamo
[00:16:18] far sì che la persona, quindi il di della persona sia proprio la persona a cui è stata
[00:16:31] segnata l'attività di progetto. In attività del progetto abbiamo il campo persona.
[00:16:38] A questo punto la query finora è praticamente analoga alla precedente, dobbiamo semplicemente
[00:16:53] raggruppare il risultato per ogni ricercatore. Qui usiamo la clause la group by e la gruppiamo
[00:17:03] per tutti e tre i valori, quindi per il spunto id, per il spunto nome e per il spunto cognome.
[00:17:17] In questo modo per ogni persona avremo ne risultato una n'upla che ci dice l'id, il
[00:17:26] nome, il cognome e il numero medio, massimo e minimo, di ore del minimo, il massimo
[00:17:35] la media della durata delle attività nel progetto pay the source, per quella persona.
[00:17:42] In realtà in questa query avremmo potuto semplicemente non selezionare anche il nome il cognome
[00:17:56] e non usare il nome cognome nella group by, lo facciamo semplicemente per chiarezza.
[00:18:03] E' chiaro che è necessario avere un lì d prima totale che siamo sicuri di avere una sola riga per ogni ricercatore,
[00:18:17] una è una sola riga per ogni ricercatore, ogni ricercatore che ha contribuito al progetto Pegasus.
[00:18:26] Guardiamo adesso la query numero 6, in cui ci viene chiesto di contare,
[00:18:32] anzi di calcolare il numero totale di ore dedicate alla didattica da ogni docente.
[00:18:38] Ricordiamo che in attività non progettuale,
[00:18:44] in attività non progettuale,
[00:18:46] queste attività hanno un tipo che
[00:18:48] lavoro non progettuale
[00:18:51] che includerà i possibili valori didattica.
[00:19:01] Qui ci viene chiesto il numero totale
[00:19:04] di ore
[00:19:06] da ogni docente.
[00:19:08] Qui quindi ci aspettiamo di avere un risultato in forma a tabellare in cui per ogni docente
[00:19:18] abbiamo un numero, in questo caso un intero, che rappresenta il numero totale di ore che
[00:19:27] altro non è che la somma delle durate di tutte le attività di tipo, lavoro progettuale
[00:19:34] e di tipo didattica. Ci si esibirà quindi sicuramente la persona e le attività non progettuali
[00:20:11] hanno una durata che è sempre un campo che si chiama ore durata. Quindi nel risultato
[00:20:20] potremmo avere per ogni persona e le scriviamo come al solito i dati in modo leggibile per cui
[00:20:33] persona.nome, pers.cognome e poi ci serve il torale delle ore. Per farlo utilizziamo l'aggregato
[00:20:51] SAM su a.oredurata. Ora nella clavosa da guerra dobbiamo imporre che la persona che svolge
[00:21:04] l'attività sia proprio per il punto di di and dobbiamo import che l'attività sia di tipo
[00:21:20] di lattica questo punto fin qui noi abbiamo in questo caso abbiamo una cosa strana perché vedete
[00:21:41] abbiamo muni di un nome un cognome e poi qui abbiamo un solo numero per cui questa questa
[00:21:48] target list è disomogenea. Abbiamo qui un solo numero, che è la somma di tutte le
[00:21:55] durate di tutte le attività e qui invece abbiamo delle colonne. Abbiamo tutti i di, tutti i
[00:22:02] nomi, tutti i coniomi delle persone. Quindi dobbiamo raggruppare anche qui per
[00:22:09] perz.id, perz.nome, perz.cognome, in modo tale d'avere
[00:22:18] del risultato una sola riga per ogni persona.
[00:22:24] Comperiamo la query, reali, dando un nome alla colonna di aggregato e anche questa
[00:22:42] query è completata. Andiamo alla query numero 7 che ci chiede di
[00:22:53] calcolare la media il massimo e il minimo degli stipendi e dei ricercatori.
[00:22:58] Il ricercatore qui fa riferimento a tutte le persone che hanno una
[00:23:06] posizione che è proprio ricercatore. Ora nella tabella persona abbiamo sia la
[00:23:16] posizione che gli stipendi per cui questa queri sembra molto semplice in
[00:23:22] in quanto possiamo selezionare direttamente da persona, che cosa?
[00:23:36] La media, in cui siamo ad apriato average, di stipendio, mass media, max stipendio, mass
[00:23:56] massimo e min stipendio, mass minimo, fra un persona e dobbiamo semplicemente vorre
[00:24:12] posizione sia proprio invece il cattore, questa queri è molto semplice, avremo quindi
[00:24:25] un risultato che è una tripla di tre numeri compresi tra 1 e 8, eh scusate no una merda
[00:24:34] di tre numeri che sono lo stipendio. Ora perché questa queri molto semplice, beh
[00:24:42] perché nella ottava query, invece, vediamo come se invece vogliamo calcolare lo stipendio
[00:24:51] dei docenti, ma avete risultato suddiviso per ogni una delle fasce, quindi leggiamo
[00:24:59] qui chiede le medie, i massimi minimi degli stipendi dei ricercatori, dei professori associati
[00:25:06] e dei professori ordinari. Qui il modo più semplice è praticamente
[00:25:11] una query simile alla sette in cui però raggruppiamo i risultati per posizione questo punto siamo
[00:25:23] semplicemente copiare perché abbiamo sempre media massima e minimo ci serve però anche
[00:25:34] la posizione e raggruppiamo per posizione questo modo per ogni posizione avremmo quindi
[00:25:58] La media è massima in minimo di istipendi, per completezza, anche questa query è completata.
[00:26:11] Passiamo quindi alla query numero 9, qui ci viene chiesto quante ore la docente Ginevra
[00:26:26] arriva ha dedicato a ogni progetto nel quale ha lavorato. Sicuramente qui dobbiamo calcolare
[00:26:36] quindi il numero totale di ore, come abbiamo fatto nella quale il precedente, l'6, qui abbiamo
[00:26:43] sommato delle ore, dovremo scegliere solo le attività di progetto svolte dal docente
[00:26:53] con nome e ginevra, la docente del nome e ginevra è con i numeriva e dobbiamo calcare un risultato
[00:27:01] valore per ogni progetto, per ogni progetto al quale la docente ha partecipato.
[00:27:11] Ci servirà quindi sicuramente persona perché dobbiamo filtrare le attività svolte da
[00:27:21] generativa. Ci serve il progetto e l'attività progetto. Nel risultato cosa ci aspettiamo
[00:27:39] di avere? Beh, sappiamo che sono progetti a cui parteciva la generativa, per cui per
[00:27:47] ogni progetto dobbiamo avere un numero totali di ore, per cui progetto.d as il di progetto
[00:27:58] e progetto.nome as, semplicemente progetto e poi dovremmo avere il numero totale di
[00:28:11] ore per ogni progetto, per cui la durata in ore è in attività progetto, as totale
[00:28:24] Andiamo quindi a scrivere la clavusa da where, partiamo dal progetto, quindi l'iddil progetto
[00:28:40] deve essere a progetto, e appunto persona deve essere proprio per il subito id e il nome
[00:29:02] la persona deve essere genera, il cognome deve essere diva e quindi andiamo a raggruppare
[00:29:24] il risultato, raggruppare per che cosa per i progetti. Nella target list abbiamo l'id e il
[00:29:33] Nel nome, anche nella groupby, e raggruppiamo per .d, vedete qui abbiamo dd e il nome e poi
[00:29:47] il risultato, quindi nella target list andiamo a raggruppare per progetto d e progetto .nome.
[00:29:58] Passiamo quindi alla decima query, decima query è interessante perché ci viene
[00:30:11] chiesto qual'è il nome dei progetti su cui lavorano più di due strutturati. Ora, notate
[00:30:21] questo più di due strutturati. Abbiamo quindi un maggiore stretto. Ci viene chiesto qual'è
[00:30:29] il nome dei progetti? Beh, iniziamo, quindi la target list abbiamo progetto.id as di progetto,
[00:30:42] progetto.nome as progetto, ci servono sicuramente i progetti, ci servono anche le attività,
[00:31:15] quindi andiamo nella casa web, progetto.id è appunto progetto. Bene, ora qui noi vorremmo
[00:31:38] selezionare solamente i progetti nei quali lavorano più di due persone, quindi ci serve
[00:31:44] anche persona persa che è la persona che lavora attività oggetto e qui, qui potremmo fare
[00:32:06] qualcosa del tipo and count perso punto id maggiore di 2 maggiore stretto. Questa cosa però è
[00:32:21] è illegale perché non è possibile utilizzare direttamente gli aggregati nella clouselover.
[00:32:28] Al massimo quello che potremmo fare è una query anidata per cui qui dentro scrivere
[00:32:37] Select, select count e confrontare il risultato di una query che deve essere un numero con il 2 per esempio.
[00:32:53] Un altro modo legale per risolvere questa query potrebbe essere, beh,
[00:33:06] selezionare tutti i progetti nei quali hanno partecipato almeno tre persone, questo si
[00:33:16] può fare, vedremo come si può fare con almeno due persone in l'undicesima query, però
[00:33:26] già scriverono una query che chiede che debbano esistere tre persone diverse e inizia a essere
[00:33:32] più complicato. Ci viene in aiuto quindi il group by, in particolare la clousa-having
[00:33:41] che soppelisce al limite di SQL che non ci permette di usare il termo limite voluto,
[00:33:50] non ci permette di usare il aggregate nella clousa-wale e quindi scriviamo, raggruppiamo
[00:33:57] per progetto.id, progetto.nome e qui possiamo usare con having possiamo definire una condizione
[00:34:15] che può essere un qualsiasi buleano di condizioni che pengono però valutate sui singoli gruppi
[00:34:23] in questo caso ci basta dire having distinct perché vogliamo sezionare le persone diverse
[00:34:35] quindi having count che dobbiamo contare che cosa distinct per il spunto id maggiore di 2 quindi
[00:34:53] stiamo selezionando i progetti con i dire nome tali che il numero di persone distinte che hanno
[00:35:07] partecipato a attività di progetto all'interno di quel progetto sono più di due. Notate che se qui
[00:35:17] fosse stato maggioro quale due sarebbe stato forse più semplice, abbiamo potuto non usare la
[00:35:24] la class of having. Vediamo infatti nella quale di 11 come questo si può fare nel caso in cui la
[00:35:40] condizione sia più semplice, in particolare nella quale di 11 ci viene chiesto quali sono i
[00:35:43] professori associati che hanno lavorato su più di un progetto, equivalentemente quali
[00:35:51] sono i professori associati che hanno lavorato su almeno due progetti. Allora andiamo innanzitutto
[00:36:06] a selezionare per il spunto ID di persona e per il spunto NOME, per il spunto Cognome
[00:36:28] from persona per se. Ora dobbiamo selezionare solo le persone che hanno lavorato dal
[00:36:48] almeno due progetti e a vedere lo schema relazionale che ci dice che il progetto, per cui persone
[00:36:58] che hanno almeno un'attività di progetto, in almeno due progetti diversi. Il progetto
[00:37:06] è un campo di attività progetto per cui ci basterà guardare la tabella attività
[00:37:12] un modo semplice per vedere per controllare questa condizione è fate il join su attività
[00:37:24] progetto a 1 e attivita progetto a 2 perché in questo modo possiamo import che queste due
[00:37:40] attività di progetto si riferiscono a progetti diversi, ma siano entrambe riferite alla stessa
[00:37:47] persona, in questo modo abbiamo praticamente l'esistenziale, il quantificatore esistenziale. Qui
[00:37:57] possiamo dire che quella persona ha lavorato almeno due progetti diversi. Non ci serve sapere
[00:38:04] in quanti progetti diversi ha lavorato, lo potremmo fare con un'altra query, a questo punto imporniamo
[00:38:13] nella cosa da query che a 1.persona sia proprio perso.id, stessa cosa per la seconda attività,
[00:38:26] e poi dobbiamo impuotre che chiaramente queste due attività di progetto non si riferiscano allo stesso progetto,
[00:38:42] quindi il progetto l'A1 è se diverso da il progetto l'A2. Ora, questa queris ci
[00:38:55] distribuisce i dinomi cognome, ma che succede se la stessa persona ha per esempio lavorato
[00:39:06] a 3-4 attività di progetto ognuna su progetti diversi, beh, ogni volta che per ogni coppia
[00:39:20] di progetti, di attività che si definiscono progetti diversi, avremo una tripla di nome
[00:39:28] con nome. In realtà noi qui vogliamo un'istinta, in modo tale che nel risultato avremo per
[00:39:40] ogni persona solamente una volta il suo nome e il cognome, indipendentemente dal numero
[00:39:46] di attività di progetto e quindi dal numero di progetti diversi ai quali ha partecipato.
[00:39:55] Vedete che questa query semplicemente è a caso del fatto che abbiamo fondamentalmente
[00:40:02] un maggiore uguale a due, tutti i professori che hanno lavorato ad almeno due progetti
[00:40:10] è un pochino più semplice, si può esprimere in questo modo, facendo il join di attività
[00:40:18] per oggetto con se stessa, mentre l'acqua di più precedente in cui c'è un maggior
[00:40:22] estretto, più di due, potrebbe essere espressa in questo modo, ma viene espressa molto
[00:40:30] più agivolmente usando leving. Questa esercitazione termina qui, grazie.
