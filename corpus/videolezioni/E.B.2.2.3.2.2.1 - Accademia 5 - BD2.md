# Trascrizione: E.B.2.2.3.2.2.1 - Accademia 5 - BD2

[00:00:01] di questa video lezione andremo ad eseguire gli esercizi di HMA5
[00:00:06] e riguardo le interrogazioni a tabbella multipla.
[00:00:10] Iniziamo dunque dal primo esercizio che richiede di determinare quali siano il nome,
[00:00:15] la data di inizio e la data di fine dei warpackage del progetto di nome Pegasus.
[00:00:20] Quindi iniziamo l'esercizio subito con un consiglio riguardo l'ordine con il quale costruiamo la nostra query.
[00:00:27] Infatti, poiché si sta svolgendo esercizi a tabella multipla, si consiglia di scrivere
[00:00:34] prima il template vuoto SELECT FROM WHERE in questo modo e di andare poi in ordine a
[00:00:40] comporre prima la clause LA FROM con le tabelle di riferimento, poi andare a definire le
[00:00:47] condizioni all'interno di WHERE e infine andare ad esplicitare la target list all'interno
[00:00:54] dell'istruzione select. Dunque l'esercizio richiede di utilizzare due tabelle del
[00:01:01] nostro schema relazionale che sono per la punto wallpackage e progetti che andiamo
[00:01:07] a scrivere all'interno della nostra clausola from in tal maniera quindi avremo
[00:01:12] VPSV e progetto SPRJ. Ricordiamo che attraverso il costrutto ES possiamo associare per una
[00:01:27] maggiore comodità il nome di una tabella ad un simbolo che poi possiamo andare a riutilizzare
[00:01:33] all'interno della nostra query. Dunque andando a specificare le due tabelle all'interno
[00:01:40] della clausola, della clausola from, siamo implicitamente creando un prodotto cartesiano
[00:01:48] in cui andiamo ad associare a tutte le nuble della prima tabella, quindi in questo caso
[00:01:52] WP, tutte le nuble della seconda tabella, quindi in questo caso PRJ e se andiamo a
[00:02:00] eseguire la query così come è, possiamo per l'appunto notare che le colonne che
[00:02:08] vanno da progetto a fine sono per l'appunto le colonne, i valori delle colonne della nostra
[00:02:16] tabella vp mentre da id a budget avremo per l'appunto i valori delle colonne della nostra
[00:02:24] tabella progetto. Adesso ovviamente non abbiamo bisogno di tutte le ennubre del prodotto cartesiano
[00:02:31] per andare a svolgere l'esercizio ma di un join in cui consideriamo solo le ennubre in cui
[00:02:36] abbiamo il World Package e il relativo progetto di riferimento. Dunque questo è specificato
[00:02:43] all'interno della tabella WP attraverso la colonna progetto e dunque andiamo appunto a scrivere
[00:02:55] all'interno della nostra clausola WHERE vp.progetto uguale progetto prj.id. Se andiamo a
[00:03:11] reseguire appunto alla WHERE allo stato attuale, andando a reseguire la WHERE allo
[00:03:19] stato attuale, possiamo notare che le ennubre sono ovviamente ridotte, in questo caso
[00:03:23] per ogni wallpackage abbiamo il relativo progetto di riferimento.
[00:03:27] Adesso l'esercizio ci richiede ovviamente di andare a determinare i wallpackage del
[00:03:34] progetto Pegasus, quindi abbiamo bisogno di un'utteriore condizione in end all'interno
[00:03:38] della clausola where.
[00:03:40] Quindi andremo a scrivere end e prg.nome, ovvero andiamo a definire per l'appunto
[00:03:51] il nome del progetto che è Pegasus, infine andiamo per la punto a specificare quelle
[00:04:06] che sono le colonne che ci interessano all'interno della target list, quindi nel nostro caso avremo
[00:04:12] bisogno del nome, quindi v punto nome, v punto inizio e v punto fine, e seguendo otterremo
[00:04:26] per l'appunto l'output richiesto dal nostro esercizio, passiamo dunque al secondo esercizio,
[00:04:35] il secondo esercizio ci richiede di determinare quali siano il nome, il cognome e la posizione
[00:04:41] degli strutturati che hanno almeno un'attività nel progetto Pegasus ordinati per cognome
[00:04:47] decrescente, quindi come fatto nel esercizio precedente iniziamo a comporre la nostra
[00:04:55] partendo innanzitutto al template vuoto e poi specificando all'interno della
[00:05:01] clausola from le tre tabelle di cui abbiamo bisogno, ovvero la tabella
[00:05:06] attività progetto, la tabella persona e la tabella progetto.
[00:05:21] Adesso sappiamo che le tabelle attività progetto e persona sono legate
[00:05:32] dalla colonna persona all'interno della tabella attività-progetto, quindi andiamo a impurre
[00:05:37] questo vincolo all'interno della nostra clausola where per creare il join, quindi avremo attiti.persona
[00:05:46] uguale per.id. Similmente avremo che le tabelle attività-progetto e progetto sono legate
[00:05:59] dalla colonna progetto nella tabella attività progetto. Quindi andremo in porre anche questo
[00:06:04] vinculo e avremo attt.progetto uguale prj.id. Adesso, eseguendo la query allo stato attuale
[00:06:28] Notiamo che le nuble di output riguardano tutte le persone che abbiano mai partecipato
[00:06:34] ad onotivitare il progetto di un qualsiasi progetto.
[00:06:37] Adesso per rendere più legibile l'output andiamo subito a inserire la target list che
[00:06:42] ci viene richiesta dall'esercizio, quindi andando a esplicitare il nome, il cognome
[00:06:51] e la posizione.
[00:06:54] Adesso a noi non interessano ovviamente tutti i progetti, ma interessa uno specifico progetto
[00:07:09] per il progetto Pegasus, quindi andiamo a imporre all'interno della clousola where
[00:07:14] tale condizione, specificando quindi che il nome del progetto prg.nome sia per l'appunto
[00:07:21] Pegasus e ancora una volta andiamo ad eseguire.
[00:07:26] Come potete vedere, il numero dell'ennube di output è ulteriormente diminuito.
[00:07:33] Quindi possiamo vedere che ci stiamo avvicinando all'output richiesto, ma notiamo che all'interno
[00:07:42] di tale output sono presenti i valori duplicati, come ad esempio Anna Bianchi.
[00:07:47] E questo vuol dire che tale persona ha eseguito più attività all'interno dello stesso
[00:07:55] progetto. Utilizziamo quindi l'istruzione Select Distinct come
[00:08:02] introdotta nella precedente video esercitazione per andare ad eliminare tutti
[00:08:09] divulgati all'interno del nostro Output ed eseguendo possiamo notare che non
[00:08:17] avremo più valori duplicati. Infine abbiamo ovviamente bisogno di ordinare
[00:08:25] il nostro output imponendo un ordinamento decrescente sul cognome della persona. Utilizziamo
[00:08:32] dunque il costrutto order by, seguito poi innanzitutto dalla colonna che vogliamo utilizzare
[00:08:43] per l'ordinamento, quindi in questo caso è per punto cognome e infine andiamo a specificare
[00:08:55] il costrutto Desk che ci permette di avere un ordinamento decrescente per l'appunto sui
[00:09:04] cognomi dell'output e andato a eseguire possiamo per l'appunto trovare il risultato desiderato.
[00:09:12] Adesso all'esercizio numero 3, l'esercizio numero 3 richiede di determinare quale
[00:09:23] sia il nome, il cognome e la posizione degli strutturati che hanno più di un'attività
[00:09:29] nel progetto Pegasus. Adesso poiché l'esercizio è molto simile rispetto a quelli dell'esercizio
[00:09:37] 3, partiamo da quest'ultimo e cambiamo tale queri per raggiungere per l'appunto il risultato
[00:09:43] desiderato. Allora innanzitutto andiamo a rimuovere la condizione relatives all'ordinamento
[00:09:55] decognomi che non è più richiesta appunto dal nostro esercizio.
[00:10:00] Adesso un modo equivalente per leggere il testo dell'esercizio è quello di andare a
[00:10:07] cercare una persona che abbia eseguito almeno due attività distinte all'interno del progetto
[00:10:14] Pegasus, che è un modo del tutto equivalente di esprimere che abbiano fatto più di
[00:10:21] attività nel progetto Pegasus. Per fare ciò abbiamo bisogno di aggiungere un'altra tabella
[00:10:28] alla clausola from della tabella attività progetto che andremo a chiamare AT2. Imporrà le stesse identiche
[00:10:53] condizioni di join nei confronti delle tabelle persona per il progetto PRG, quindi andiamo a
[00:11:01] scrivere esattamente le stesse condizioni che avevamo scritto per HAT, quindi avremo HAT2.persona
[00:11:12] uguale per similmente HAT2.progetto uguale prg.id. Adesso infine avremmo bisogno di specificare
[00:11:37] che gli d delle attività della nuova tabella che abbiamo considerato siano per
[00:11:42] l'appunto diversi rispetto agli d delle attività che sono già presenti all'interno
[00:11:46] del nostro output. Dunque per fare ciò andiamo a esplicitare che at punto
[00:11:54] id sia diverso da at 2 punto id. In tal modo abbiamo imposto che ogni
[00:12:03] persona all'interno del nostro output abbia eseguito almeno due attività distinte, dunque più
[00:12:10] di una, inerentemente al progetto Pegasus. Andiamo quindi a eseguire la nostra query e verifichiamo
[00:12:19] per l'appunto che l'output sia quello desiderato. L'esercizio numero quattro. L'esercizio numero
[00:12:30] quattro ci richiede di determinare quali siano il nome, il cognome e la posizione dei
[00:12:35] professori ordinari che abbiano fatto almeno un'assenza per manattia.
[00:12:40] Dunque, iniziamo la nostra query andando ad esplicitare nella clausola from le due
[00:12:47] tabelle di cui abbiamo bisogno, ovvero la tabella persona e la tabella
[00:12:54] assenza. Adesso abbiamo bisogno similmente ai precedenti esercizi
[00:13:06] partendo dal prodotto cartesiano delle due tabelle, imponiamo un join
[00:13:11] considerando gli attributi persona e id di rispettivamente delle due tabelle persone
[00:13:18] assenza, quindi avremo per punto id uguale a sn punto persona.
[00:13:28] Adesso abbiamo bisogno di impostare la condizione che determini il tipo di
[00:13:36] assenza ovvero malattia quindi andiamo a scrivere a sn.tipo uguale malattia
[00:13:47] inseriamo all'interno per poter eseguire questa query andiamo a inserire
[00:13:55] all'interno della nostra target list le colonne richieste quindi il nome il
[00:14:02] cognome e la posizione e seguendo otteniamo nel nostro output una
[00:14:18] serie di ennublenerenti a generici strutturati che abbiano effettuato almeno un'assenza per
[00:14:25] malattia. Infatti possiamo vedere ricercatore, professore associato e professore ordinario.
[00:14:31] Abbiamo quindi bisogno di impuere l'ultima condizione all'interno della nostra clausola
[00:14:37] relativa per l'appunto alla posizione e quindi avremo che per punto posizione sia
[00:14:51] per l'appunto eseguendo possiamo notare che l'output contiene numerosi
[00:15:05] duplicati per l'appunto della nuplacon generativa che indica che per l'appunto
[00:15:11] questa strutturata ha effettuato più essenze per malattie di conseguenza per
[00:15:16] per andare a rendere unica ogni nuplà all'interno del nostro risultato,
[00:15:23] utilizzeremo l'operatore selectDistinct, l'istruzione selectDistinct e andando ad eseguire possiamo notare che otteniamo il risultato desiderato.
[00:15:36] Procediamo con l'esercizio numero 5, in quale ci chiede quali sono i professori ordinari che hanno fatto più di un'assenza per malattia.
[00:15:50] possiamo anche leggerla come quali sono i professori ordinari che hanno fatto almeno due ascenze della malattia.
[00:15:57] Per fare ciò, cominciamo a scrivere la struttura della query, insegniamo la clasa alla serie from.
[00:16:04] Sicuramente dovremmo prendere la tabella persona e la tabella assenza.
[00:16:11] Le prenderemo due età belle, assenza, perché in questo modo possiamo imporre che questa persona deve aver fatto almeno due assenze e che queste due assenze si riferiscono ad assenze diverse ma fatte dalla stessa persona, quindi andiamo a scrivere assenza 1 e assenza 2.
[00:16:33] in la clasola where andiamo a dire sicuramente che la persona d'essenza 1 deve essere la
[00:16:45] stessa, esattamente, vers punto d. La stessa cosa deve essere vers senza 2 e poi dobbiamo
[00:17:00] dire che assenza 1.d è diverso da assenza 2.d in questo modo appunto andiamo a prendere
[00:17:10] due assenzi diverse della stessa persona. Successivamente dobbiamo andare a definire il
[00:17:15] tipo dell'assenza quindi dobbiamo dire che assenza 1.tivo deve essere esattamente
[00:17:22] malattina e che la tipologia di assenza 2 è uguale alla tipologia di assenza
[00:17:31] Infine dovremmo andare a dire che la posizione delle persone di cui siamo interessati sono
[00:17:41] di professore ordinari, quindi perz punto posizione è uguale a professore ordinario.
[00:17:54] nella target list metteremo perz.ed perz.nomesnome e perz.cognone.ers
[00:18:15] eseguiamo la WERI e vediamo che queste sono le persone che sono i professori
[00:18:24] ordinari che hanno fatto più di un'assenza per malattia
[00:18:28] ovviamente ci sono delle persone che hanno fatto più dito assenze e c'è il generariva
[00:18:36] appunto ha fatto più dito assenze per prendere solamente una, per prendere solamente per
[00:18:44] fare in modo che abbiamo solamente una persona con la tripla di nome e cognome, andiamo
[00:18:51] ad utilizzare il distinct, andiamo a lavorare, quindi solamente il generariva è il professionale
[00:19:05] ordinario che ho fatto più di una senza per malattia. Procediamo con la quale numero 6 che
[00:19:12] ci chiede quali sono il nome, il cognome e la posizione dei ricercatori, non anzitore
[00:19:18] alla posizione, perché ovviamente la posizione c'era fatta già data, c'era fatta già data
[00:19:23] con un professore ordinario e quindi il nome, il cognome e la posizione dei ricercatori
[00:19:29] che hanno almeno un impegno per ditattica. Ok, scriviamo sempre la struttura della
[00:19:35] se andiamo a prendere sempre persona perz e attività non progettuale che andiamo a vedere i task
[00:19:48] e andiamo a vedere insomma l'attività che non sono ditatti quindi sono un'attività non progettuale
[00:19:54] attività non progettuale, andiamo a e andiamo ad inserire la class law where
[00:20:08] nella clasula web dobbiamo dire che la persona è così riferita attività è esattamente
[00:20:17] per spondridi, poi dobbiamo dire che il tipo dell'attività didattica, perché ci chiede
[00:20:33] appunto che hanno almeno un impegno didattica e poi dobbiamo andare a dire che la posizione
[00:20:50] della persona accusamente interessati è un ricercatore, quindi apunto, potezione uguale
[00:20:59] a ricercatore, ok, lo stesso, la stessa cosa che vi mandiamo a prendere perz.d perz.
[00:21:12] inserire la posizione perché appunto c'è già stata data, l'abbiamo aggianti da
[00:21:28] allettano del web, eseguiamo la, possiamo seguirla quelli, il problema, andate a seguirla
[00:21:45] e vediamo insomma che questi sono i ricercatori che hanno almeno un impegno per di tattica,
[00:21:55] ovviamente ci sono dei duplicati perché Barbara ha due impegni per di tattica, noi non
[00:21:59] avevamo bisogno di duplicati, quindi andiamo a inserire anche qui il distinto, ecco
[00:22:05] quella quale che ho piacata. Procediamo con la quale numero 7 che ci chiede quale
[00:22:10] sono il nome con il nome e la posizione dei ricercatori che hanno più di un impegno per
[00:22:15] ditattica. Ok, per questa quali andiamo a utilizzare un approccio simile alla quali numero 5,
[00:22:22] utilizziamo la scruttura, sarebbe per Chrome, usatelizzeremo persona, attivitando un progettuale
[00:22:34] perchè andiamo a prendere l'attività non progettuale perchè sono le impeglie di
[00:22:43] didattica prima e le attuale e lo chiameremo A1 perchè andiamo ad utilizzare sempre due
[00:22:56] tabelle in maniera tale che possiamo imporre che si riferiscono a due attività non progettuale
[00:23:05] diverse, quindi attività non progettuale a 2. Perfetto. Andiamo ad inserire la sua
[00:23:14] where, all'interno della quale scriveremo che a 1.persona deve essere esattamente
[00:23:25] il tipo di A1 deve essere tipo di Tattica, 1 punto tipo è uguale a Tattica e il tipo
[00:23:58] di A2 deve essere uguale al tipo di A1 come abbiamo fatto per la quale numero 5, quindi
[00:24:03] A2 punto attivo è uguale a A1 punto attivo.
[00:24:12] Arrivate a questo punto, dobbiamo dire che l'ID dell'attività non progettuale però
[00:24:19] deve essere diverso dall'identificativo dell'attività non progettuale 2 perché
[00:24:28] In questo modo possiamo riferirci a due attività non progettuali,
[00:24:35] quindi due impegni per la didattica, ma diversi per la stessa persona.
[00:24:42] A 1 punto di D è diverso da 2 punto di D e poi bisogna andare a dire che siamo interessati
[00:24:56] Perz punto posizione uguale di cercare.
[00:25:06] Per questi, con lo stesso aggiornamento delle due quali precedenti, utilizzeremo il distinto.
[00:25:11] Perz punto ID perz problema e ci siamo.
[00:25:41] Quindi Barbara Burso è una ricerca di cerca più di un'impegno epitattica.
[00:25:51] Procediamo con la quale numero 8 che ci chiede quali sono i nome e quali nomi degli strutturati
[00:26:01] che nello stesso giorno hanno sia attività progettuali che attività non progettuali.
[00:26:07] Allora, andiamo sempre con la struttura della quale, sella from, all'interno del from
[00:26:15] mettiamo persona che hanno bisogno di strutturati e poi andiamo a mettere ovviamente attività
[00:26:21] l'attività progetto e l'attività non progettuale perché abbiamo bisogno di questa persona
[00:26:26] in tutte e due tabelle quindi l'attività progetto api che è in tutte e due tabelle e soprattutto
[00:26:35] in questo giorno quindi l'attività progettuale api, ok, andiamo ad inserirla sulla cuore
[00:26:54] all'interno della cuore diciamo che la persona che è in volta in attività progettuale
[00:27:00] l'attività non progettuale è per z punto e d e dobbiamo dire che l'attività non progettuale
[00:27:25] abbia nello stesso giorno, quindi attività progettuale punto giorno è esattamente
[00:27:31] che ottengono un progettuale per l'orno perfetto. Di questi, come le quale precedenti, andremo a prendere
[00:27:39] persona.d, che vediamo adesso. Quindi, persona.d, persona.d, ognuno.d, mettiamo sempre il
[00:27:58] piste intendo lo stesso doveva di prima, perché vogliamo sapere solamente chi è
[00:28:02] non quanta volta compagno di questo effetto. Andiamo ad eseguire i lavori. Quindi
[00:28:12] Anabianchi è una strutturata che ha nello stesso giorno si attività
[00:28:19] progettuali che attivitano progettuali. Allora, andiamo a leggere il quesito
[00:28:26] numero 9 che ci chiede quali sono il nome e cognome dei strutturati che nello
[00:28:30] stesso giorno hanno si attività progettuali che attivitano progettuali e
[00:28:34] questa parte è identica al quesito numero 8. Però la domanda numero 9 ci
[00:28:41] chiede anche di proiettare il giorno il nome del progetto, il tipo di
[00:28:45] attività non progettuali e la durata in ore di entrambe l'attività, quindi possiamo
[00:28:50] partire dalla struttura della query fatta per il cosino numero 8 e andare a utilizzarla
[00:29:01] come base per fare la query per il numero 9.
[00:29:06] I dati aggiuntivi che c'è, ad oltre il giorno e il nome e il cognome, sono il giorno dell'attività progettuale o non progettuale, è la stessa cosa.
[00:29:21] Quindi nella target list si va ad aggiungere ap.giornu, as.giornu, sarebbe stata la stessa
[00:29:32] cosa se vi siamo preso l'attività di giorno dalla tabella attività non progettuale.
[00:29:39] Poi ci chiede il tipo di attività non progettuali, il nome del progetto lo lasciamo per ultimo.
[00:29:48] diciamo il tipo di attività non progettuali lo prendiamo dall'attributo tipo, quindi
[00:30:08] facciamo anp.tipo e la durata in ore di entrambe l'attività, quindi da attività progettuale
[00:30:26] andiamo a prendere l'attributo ore durata,
[00:30:30] qua possiamo chiamarlo appi durata,
[00:30:43] e dall'attività non progettuali prendiamo lo stesso attributo as-ant durata.
[00:30:55] Infine, dobbiamo andare a prenderci il nome del progetto.
[00:30:59] Questa è un'informazione che non è contenuta nelle tabelle
[00:31:04] che abbiamo utilizzato prima per la query numero 8.
[00:31:09] Allora, il nome del progetto vediamo che è solo all'interno della tabella Progetto.
[00:31:17] Ecco qui.
[00:31:19] Per andare a rigavarcelo,
[00:31:21] qua notiamo nella tabella T da Progetto che esiste un attributo progetto che è parte
[00:31:32] della Florenchi, formata dalla coppia progetto WP che si riferisce
[00:31:33] formata dalla coppia progetto WP, che si riferisce alla tabella WP di attributi progetto ed di della tabella WP.
[00:31:46] A sua volta, l'attributo progetto di WP è una florenchi dell'attributo ed di della tabella progetto.
[00:31:56] Quindi quello che possiamo fare è andare a fare un join tra le tabelle
[00:32:03] attività progetto e la tabella progetto. Quindi andiamo ad aggiungere la
[00:32:09] tabella progetto all'interno della clasula from che chiamiamo prg e la
[00:32:20] condizione è quella solida ovvero prg.ed uguale a l'ed del progetto all'interno
[00:32:33] della tabella t da progetto quindi ap.progetto. A questo punto nella quei
[00:32:45] precedente, abbiamo bisogno del Distint, questo perché il quesito ci chiedeva soltanto il
[00:32:55] nome del cognome, adesso, degli strutturati, adesso che abbiamo delle informazioni aggiuntive,
[00:33:03] il Distint non è più necessario e quindi andando a lanciare la query il risultato è il
[00:33:12] il seguito, dove abbiamo il nome, il cognome, lo strutturato, il giorno, il tipo e la durata
[00:33:22] di entrambi l'attività, come richiesto dal quesito.
[00:33:25] Adesso passiamo al quesito numero 10 che ci chiede quali sono il nome, il cognome degli
[00:33:30] strutturati che nello stesso giorno sono assenti all'attività progettuale.
[00:33:34] quindi partendo dallo stesso template solito, dobbiamo andare ad agire sulle tabelle Assense,
[00:33:53] la tabella attività progetto e la tabella persona.
[00:34:03] A questo punto dobbiamo fare un join dove andiamo a prendere le attività progettuali
[00:34:20] e le assenze che sono nello stesso giorno e poi dobbiamo anche ultimamente andare a condizionare
[00:34:29] sull'ID dell'attività-progetto che si riferisce tapella persona, quindi l'attributo persona
[00:34:38] della da bella attività-progetto, dobbiamo condizionare che sia uguale all'ID della persona, all'interno
[00:34:46] della da bella persona e la stessa cosa la dobbiamo fare anche per la da bella assenza.
[00:34:54] quindi abbiamo detto che dobbiamo fare il join condizionando su il giorno dell'essenza
[00:35:06] dell'attiva progetto, quindi as.giornogualeapp. e a questo punto dobbiamo prendere, siccome ci serve il
[00:35:23] il nome e il condomeno della persona, dobbiamo prendere tutte le righe che sono uguali a
[00:35:33] quelle della persona, dell'edì della persona, quindi per perse punto edd ap.persona e perse
[00:35:42] punto edd uguale a senso punto persona. A questo punto nella target list del select
[00:35:51] inseriamo in modo distinto stavolta, quindi eliminando i duplicati persona.nome e persona.nome e risultato è questo, all'ambianche.
[00:36:10] Adesso svolgiamo il quesito numero 11 che ci chiede quali sono i nomi del cognome dei strutturali che nello stesso giorno sono assenti a noti da progettuali.
[00:36:23] si richiede anche di progettare il giorno, il nome del progetto, la causa dell'assenza,
[00:36:29] la durata in ore della titola progettuale. Questa è, in grosso modo, molto simile alla
[00:36:35] queri che abbiamo fatto per il quesito numero 9, e qui la logica è esattamente la stessa.
[00:36:43] Questa volta, però, dobbiamo agire sempre sulla tabella persona, ma su...
[00:36:53] tabella assente e assenza e la tabella attività progettuale, attività progetto, scusate. Quindi
[00:37:05] persona, as, pers, assense, as, as e attività progetto, as, ap. A questo punto dobbiamo
[00:37:30] prendere come prima tutte le attività progetto di quella persona e l'assenza della specifica
[00:37:40] persona, quindi persi.id uguale a as.persona e persi.id uguale ad app. Ma non è finita qui
[00:37:59] perché dobbiamo anche fare il join andando a condizionare sul fatto che ci chiedeva il
[00:38:12] nome del progetto, quindi ho dimenticato nel from il progetto, la tabella progetto. Dicevo
[00:38:26] siccome ci chiede anche il nome del progetto dobbiamo includere nella tabella from, nella
[00:38:33] crasano la tabella progetto e andare a filtrare sul led del progetto, come abbiamo fatto
[00:38:42] nel quesido numero 9, e led del progetto. A questo punto. Le informazioni richieste
[00:38:51] all'interno del risultato sono il nome del cognome dei strutturati, il giorno, il
[00:39:14] Il nome del progetto è RG.9, la cosa è l'assenza che veniva specificata all'interno del tipo
[00:39:30] e infine la durata in ore della attività progettuale, quindi a p ore durata.
[00:39:42] Scusate, ho dimenticato che le assenze della attività progettuale devono essere dello
[00:39:55] stesso giorno, uguale a senso molto giorno. Ultimo cosido, prepariamo la
[00:40:11] query, ci chiede quali sono i WP che hanno lo stesso nome ma parteggono
[00:40:18] progetti diversi. A questo punto dobbiamo agire soltanto sulla tabella WP che
[00:40:31] però dobbiamo prendere due volte quindi dobbiamo andare a fare il prodotto
[00:40:37] cartesiano della tabella vp con se stessa e la chiamiamo vp1 la prima e vp2 la
[00:40:47] seconda a questo punto di questo prodotto cartesiano immaginario in realtà tra
[00:40:56] vp1 e vp2 dobbiamo tenere soltanto le righe con lo stesso nome vp1 punto
[00:41:07] uguale a vp2.nome ma non è finito qui perché il progetto deve essere diverso e quindi dobbiamo
[00:41:21] tenere soltanto quelle che hanno il progetto differente. Il progetto vp1 progetto diverso
[00:41:36] la vp2 progetto e nella target list inseriamo penso il nome quali sono i vp con lo stesso
[00:41:48] che ha un stesso nome ok dobbiamo inserire il nome chiaramente visto che ci chiede
[00:41:53] soltanto il nome dobbiamo utilizzare il costrutto distinct per eliminare i duplicati altrimenti
[00:42:02] otterremo il risultato con diversi nomi, diversi nomi duplicati per l'appunti, c'è un errore.
[00:42:20] Ecco qui, senza il distinto vediamo se c'erano dei duplicati, sì c'erano dei duplicati quindi va assolutamente
[00:42:32] e per questo web inare tutto ci vediamo alla prossima
