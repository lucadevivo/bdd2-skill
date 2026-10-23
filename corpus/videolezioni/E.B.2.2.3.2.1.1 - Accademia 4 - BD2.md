# Trascrizione: E.B.2.2.3.2.1.1 - Accademia 4 - BD2

[00:00:00] In questa videolezione andremo ad eseguire gli esercizi di Academia 4
[00:00:07] riguardo le interrogazioni sul singola tabella. Iniziamo ricordando lo schema
[00:00:14] relazionale partendo per l'appunto dai domini, possiamo notare numerosi
[00:00:21] domini enumerativi. Iniziamo ad esempio dal dominio strutturato, ovvero
[00:00:28] un dominio denominativo che ammette i valori ricercatore, professor associato e professor
[00:00:34] ordinario. Abbiamo poi il dominio lavoro progetto che corrisponde ad essere ricerca e sviluppo,
[00:00:42] dimostrazione, management e altro. Abbiamo poi il dominio numerativo lavoro non progettuale
[00:00:48] che può essere didattica, ricerca, missione e infine abbiamo causa senza che può essere
[00:00:54] di chiusura universitaria, maternità e malattia. Abbiamo poi poi il solito POS integer che corrisponde
[00:01:02] ad essere il dominio dei numeri positivi, compreso 0, ovviamente. Abbiamo poi il dominio
[00:01:09] string m, ovvero una stringa con il massimo 100 caratteri. Abbiamo il dominio numero ore
[00:01:15] che è un intero compreso tra 0 e 8 e infine abbiamo il dominio denaro che corrisponde
[00:01:22] insieme dei numeri reali, maggiori di zero. Andiamo poi a ricordare quelle che sono le
[00:01:29] tabbelle del nostro schema relazionale. Abbiamo quindi la tabbella persona con il suo id,
[00:01:42] abbiamo un nome, il cognome, la posizione e lo stipendio. La tabbella persona può
[00:01:50] risponde ad essere il personale all'interno della base di dati academia, poi abbiamo il
[00:01:55] progetto che ha come colonne l'ID, il nome, una data di inizio, una data di fine e un
[00:02:03] budget in denaro. Abbiamo poi un work page cage che fa riferimento a uno specifico
[00:02:08] progetto e ha come diave anche un identificativo, un nome, una data di inizio, una data
[00:02:14] di fine. Poi abbiamo le attività di progetto che hanno anche loro un identificativo, una
[00:02:25] specifica persona, un progetto, un wall package, un giorno, una tipologia di lavoro progetto
[00:02:33] e una durata in ore. Abbiamo poi le attività non progettuali che hanno un identificativo,
[00:02:40] una persona di riferimento, il tipo di lavoro non progettuale, la data di un giorno e la
[00:02:50] dura tenore. Infine, abbiamo l'assenza che ha un identificativo associato appunto all'identifico
[00:02:58] di riferimento di una persona, ha come un tipo di causa-assenza e un giorno di riferimento.
[00:03:06] Iniziamo dunque con il primo esercizio che ci richiede di determinare i cognomi
[00:03:23] distrinti di tutti i strutturati all'interno della nostra base di dati.
[00:03:28] Dunque poiché si parla ovviamente di un'interlocazione, inizieremo subito con
[00:03:33] l'istruzione SELECT e specifichiamo nella target list la colonna che
[00:03:40] ci interessa recuperare attraverso la nostra interlocazione, ovvero la
[00:03:43] colonna cognome. Specifichiamo poi all'interno della causa la from, la tabbella all'interno
[00:03:55] del nostro schema che vogliamo interrogare, quindi nel nostro caso la tabbella persona.
[00:04:00] Dunque il testo dell'esercizio ci richiede adesso che il risultato della nostra interrogazione
[00:04:12] non contenga degli elementi duplicati, dunque che ci siano unicamente degli elementi
[00:04:18] distinti. Infatti, ci accorgiamo che se andiamo ad eseguire la seguente query possiamo notare
[00:04:27] che c'è la possibilità di ottenere dei cognomi duplicati dunque avremo ad esempio bianchi che
[00:04:36] è presente due volte all'interno del nostro output. Per ovviare a tale problematica facciamo
[00:04:44] dunque uso dell'istruzione select distinct. Talla istruzione garante che all'interno
[00:04:54] del nostro output non saranno presenti dei valori duplicati, infatti adesso abbiamo bianchi
[00:05:00] due volte, ma se andiamo a eseguire adesso la query bianchi sarà presente una sola
[00:05:06] volta e infatti avremo solamente venti ennuble. Passiamo dunque al secondo esercizio.
[00:05:13] Dunque, il secondo esercizio ci richiede di determinare quali siano gli strutturati di
[00:05:21] tipo ricercatore, andando a specificare il loro nome e il loro cognome.
[00:05:26] Dunque, iniziamo nuovamente con l'istruzione select e andiamo a specificare all'interno
[00:05:36] della target list la colonna nome e la colonna cognome.
[00:05:42] Ancora una volta all'interno della clausola from andremo a specificare la tabella persona.
[00:05:50] Diversamente dalla queri precedente, in questo caso abbiamo bisogno di imporre una condizione
[00:05:59] che venga rispettata da tutte le annuble del nostro output.
[00:06:05] Quindi in questo caso avremo bisogno di una clausola where.
[00:06:09] tale clausola where dovrà andare a verificare specifica una condizione
[00:06:18] che si dovrà verificare sulla colonna posizione della nostra tabella.
[00:06:24] Ricordiamo andando a guardare lo schema relazionale che la colonna
[00:06:32] posizione sarà di tipo strutturato che è un domine numerativo quindi avremo
[00:06:38] a disposizione tre possibili valori, che è ricercatore, professore associato e
[00:06:42] professore ordinario. Quindi nel nostro caso vogliamo che la colonna, le nuble
[00:06:49] del nostro output abbiano nella colonna posizione il valore ricercatore, quindi
[00:06:54] scriveremo posizione ricercatore. Andiamo dunque a eseguire la nostra query e
[00:07:06] otterremo come risultato per l'appunto tutti gli strutturati che sono di tipo
[00:07:12] ricercatore. Specifichiamo che essendo il dominio di posizione dominio numerativo
[00:07:19] ammette solamente quelle specifiche string. Dunque, se andiamo ad utilizzare
[00:07:24] un'altra stringa come ad esempio studente o una qualsiasi attristrica che non
[00:07:30] rientri nel set delle string accettate, otterremo un errore di sintassi.
[00:07:39] Passiamo dunque al terzo esercizio. Il terzo esercizio ci dichiere di determinare
[00:07:50] quali siano i professori associati, il cui il cognome comincia con la lettera V.
[00:07:56] Ancora una volta con la nostra istruzione SELECT,
[00:08:02] specificheremo una target list che contiene il nome e il cognome.
[00:08:11] La clausola from ancora una volta andrà ad indicare la tabella persona e in questo caso
[00:08:23] l'esercizio richiede che due diverse condizioni vengano diciamo verificate si verificano
[00:08:33] all'interno del nostro output. La prima è che appunto alla posizione sia professore
[00:08:42] associato, la seconda condizione è che il cognome cominci con la lettera V. Quindi
[00:08:47] riguardo la posizione, agiamo esattamente come abbiamo fatto con
[00:08:51] l'esercizio scosso, quindi scriviamo la nostra causa la WHERE,
[00:08:57] andremo a legare l'altra condizione con l'operatore AND.
[00:09:20] Adesso poiché in questo caso, diversamente da come abbiamo fatto con
[00:09:25] con l'ugianza della colonna posizione, dobbiamo verificare una similarità e per verificare
[00:09:35] una similarità, ovvero un qualcosa che inizi con la lettera V, una stringa che inizi
[00:09:40] con la lettera V, abbiamo bisogno dell'operatore like. Adesso possiamo specificare un pattern
[00:09:52] che vada a rappresentare una stringa, una qualsiasi stringa che inizi con la
[00:09:57] lettera V. Per fare ciò dunque specificiamo la lettera iniziale e poi
[00:10:02] mettiamo all'interno del nostro pattern la percentuale. Questo fa in modo che
[00:10:10] tutti, diciamo, le string che stiamo ricercando inizi con la
[00:10:17] lettera V. Dunque andiamo ad eseguire la nostra query. Possiamo per l'appunto
[00:10:36] verificare che i cognome ricercati iniziano appunto tutti quanti con la lettera V, quindi
[00:10:43] in questo caso questi sono delle ennuble di professori associati che il cui cognome inizia
[00:10:51] con la lettera V, come richiesto dall'esercizio. Specificano inoltre che è possibile anche
[00:11:00] utilizzare un simbolo che vada a qualificare una qualsiasi carattere che è rappresentato
[00:11:09] dall'underscore, dal simbolo di underscore. Quindi se in questo caso ad esempio andiamo
[00:11:15] ad utilizzare il simbolo di underscore e poi la letter R vuol dire che stiamo cercando
[00:11:21] un cognome che inizia con la lettera V che abbia un qualsiasi caratteri come secondo
[00:11:27] carattere e abbia come terzo carattere R e poi può essere una qualsiasi seguito, una qualsiasi string.
[00:11:34] Infatti, se andiamo ad eseguire la seguente query otterremo solamente Verona,
[00:11:41] poiché è l'unico che rispetta l'unico professor associato, il cui cognome rispetta questa condizione.
[00:11:49] Sottolineiamo un errore tipico che può essere commesso in questi casi,
[00:11:55] ovvero quello di andare a sostituire like con l'operatore di guaianza, ma se andiamo
[00:12:02] ad utilizzare appunto l'operatore di guaianza in questo caso non è terremo nulla, poiché
[00:12:08] stiamo andando a comparare il valore del cognome con questa esatta stringa che non è interpretato
[00:12:16] come un pattern. Passiamo dunque all'esercizio numero 4, l'esercizio numero 4 ci richiede
[00:12:29] di determinare quali siano i professori sia associati che ordinari il cui cognome inizia
[00:12:34] con la lettera a b. Dunque la target list e la clausola from di questa query risultano
[00:12:42] essere esattamente le stesse che avevamo definito nelle precedente guerre, quindi avremo, selezioneremo
[00:12:50] il nome e la colonna cognome, from la solita tabella persona. Adesso la particolaria di
[00:13:07] questo esercizio sta nel considerare più di due condizioni, infatti dovremmo ammettere
[00:13:16] all'interno del nostro output, professori che siano sia associati
[00:13:19] che ordinari e che al tempo stesso, ognuno di questa N-nouple rispetti la
[00:13:24] condizione di avere il cognome che inizi con la lettera V.
[00:13:31] Adesso scriverò una prima versione della clausola WHERE più lunga e poi vedremo
[00:13:36] una versione equivalente più compatta di questa condizione.
[00:13:41] Quindi, iniziamo scrivendo la nostra clausa alla WHERE, andando a definire la condizione
[00:13:50] in cui abbiamo professori associati, il cui cognome inizia con la lettera V, quindi scriviamo
[00:13:59] tra parentesi, la posizione è professore assuciato, e quindi contemporaneamente voglio
[00:14:17] che il cognome incomincie con la vetra V, quindi come fatto con l'esercizio precedente,
[00:14:25] avremo che cognome, like e avremo il nostro pattern ovvero V percentuale, adesso se andiamo
[00:14:40] ad eseguire la seguente, la seguente query otterremo diciamo un output all'interno del
[00:14:49] quale avremo unicamente dei professori associati il cui cognome inizia con la V. A questa
[00:14:55] condizione adesso dobbiamo legare la condizione in cui abbiamo dei professori ordinati
[00:14:59] il cui cognome inizi con la lettera V, quindi aggiungeremo con l'operatore buleano or l'altra
[00:15:09] condizione che vogliamo trivere, ovvero che la posizione sia professore ordinario e in
[00:15:26] modo similare a quanto ho fatto prima, end, quindi contemporaneamente voglio che il cognome
[00:15:36] sia, abbia rispetto il pattern che inizia con la lettera B, quindi B percentuale.
[00:15:42] Adesso se andiamo ad eseguire la seguente query, otterremo come risultato, appunto,
[00:15:50] professori associati ordinari in cui cognome inizia con la lettera B.
[00:15:55] Volendo, è possibile scrivere una versione più compatta di questa condizione, di questa
[00:16:01] clausola where e andiamo a vedere come scriverne che sia del tutto appunto
[00:16:07] equivalente a quella che abbiamo appena scritto quindi in questo caso
[00:16:11] andiamo a scrivere la posizione che può essere sia professore ordinario che
[00:16:18] professore associato quindi avremo posizione uguale or quindi può essere
[00:16:30] professore ordinario or vogliamo che contemporaneamente a questa questa
[00:16:51] condizione che abbiamo appena scritto vogliamo che venga valutato il cognome e
[00:16:55] quindi andremo ad aggiungere and cognome like come scritto prima il
[00:17:06] notropattern quindi avremo b% come potete vedere l'output è
[00:17:17] è esattamente lo stesso di quanto ho tenuto con la versione precedente ma abbiamo scritto
[00:17:22] una clausola wear più compatta rispetto a quella scritta in precedenza.
[00:17:28] Passiamo alla query numero 5 che ci chiede quali sono i progetti già terminati alla
[00:17:39] data di Erna. Per fare ciò prendiamo la tabella progetto di cui selezioneremo.
[00:17:51] Nella clausola select andiamo ad inserire tutti i campi e in inziuto vediamo come è
[00:17:59] composto, quali sono i record all'interno della tabella del progetto e andiamo a prendere
[00:18:07] solamente i progetti la cui data di fine e minore della data attuale, quindi nella
[00:18:12] Tra solo where inseriremo fine, minore e current rate.
[00:18:24] E' facile vedere che tutti i progetti che avevamo all'interno della nostra tabella sono già terminati
[00:18:30] e quindi questa query restituta tutti i progetti che avevamo già visto che prima.
[00:18:36] Passiamo alla pari numero 6, la quale ci chiede quali sono i nomi di tutti i progetti ordinati
[00:18:46] in ordine crescente dall'inizio quindi ci chiede solamente i nomi e non ci chiede tutto tutti i
[00:18:52] progetti quindi utilizziamo sempre la tabella progetto e nella classola select andremo a inserire
[00:19:02] identificativo del progetto e il nome, ma che non ci chiede tutti i vari del progetto ma ci chiede
[00:19:09] i nomi e poi ci chiede che questi nomi devono essere ordinati in ordine crescente per
[00:19:18] l'ordine di inizio, quindi andiamo ad utilizzare l'order by per l'ordine di inizio di campo inizio
[00:19:28] in ordine crescente e vediamo che questo è l'ordine crescente,
[00:19:39] quindi one sharing il progetto in seto prima e così via.
[00:19:44] Passiamo alla quale numero 7 che chiede quale sono i nomi di work package e anche questi
[00:19:53] dovevano essere ordine di ordine crescente per nome, quindi andiamo a prendere.
[00:20:03] Nel classo la form inseriamo la data per la wallpackage. Nella classo la select inseriamo
[00:20:17] call e andiamo a vedere cosa di tutti i recorders contro l'interno della data per la wallpackage.
[00:20:26] Poi, nel momento che ci chiede i nomi di Warpage,
[00:20:30] possiamo fare una prima, quindi,
[00:20:32] una target list della sola selec,
[00:20:37] sulla selecta mettiamo l'identificativo e mettiamo il nome del Warpage.
[00:20:43] E poi gli ordiniamo utilizzando sempre l'order by.
[00:20:49] Questa volta avrò utilizzato il nome e sempre l'ordine crescente.
[00:20:57] Allora iniziamo subito dal primo coesito, il numero 8 che ci chiede quali sono distinte le case di assenza di tutti gli strutturati.
[00:21:19] Allora, sappiamo che all'interno del DBHM4 c'è la tabella ASSENSA dove è specificato l'attributo tipo che ci dice quale è la caso della ASSENSA.
[00:21:35] E quindi andiamo a scrivere la query, select, dove all'interno della target list inseriamo
[00:21:45] tipo, from, assenza.
[00:21:49] Il risultato di questa query è la seguente da Bella che vedete in basso, dove però sono
[00:22:04] presenti dei duplicati. Per eliminare questi duplicati utilizziamo la glasola Distint che
[00:22:14] per l'appunto ci va ad eliminare. Questo perché? Perché SQL lascia a noi la responsabilità
[00:22:23] di scegliere se eliminare un duplicati. Questo per un motivo puramente di velocità
[00:22:33] attenzione che il Distint viene valutato su tutta l'article list quindi se andiamo a
[00:22:44] raggiungere persona vedete che i duplicati come magari qualcuno vorrebbe
[00:22:52] aspettarsi che il Distint dà una valutata solo su tipo perché è l'attributo
[00:22:58] più vicino alla causola, ma questo come vedete non è vero perché in questo modo va ad eliminare
[00:23:06] tutte le righe identiche all'interno della tabella. Quindi qua ricorrete questa.
[00:23:19] Adesso passiamo al quesito numero 9 che in realtà è molto molto simile per struttura al numero 8 e cambia soltanto la tappella dove lavoriamo.
[00:23:38] Il quesito ci chiede quali sono distinte le tipologie di attività di progetto di tutti gli strutturati.
[00:23:46] Allora andiamo a vedere all'interno dello schema attività-progetto ci chiedeva 2G di attività-progetto.
[00:23:58] Quindi attività-progetto, il tipo, eccolo qua l'attributo tipo e quindi penso che l'avviate già capito da soli come si struttura questa query.
[00:24:13] Select Distint Tipo from Actività Progetto e, come vedete, il risultato è esattamente quello che ci aspettiamo, perché se togliamo Distint, ecco qua tutti i dubitani.
[00:24:35] Prassima query, la numero 10 che ci chiede quali sono i giorni distinti nei quali del personale effettuato attività?
[00:24:47] attività non progettuali di tipo didattica. Il quesilo ci impone anche di dare il risultato
[00:24:54] in ordine crescente. Allora, sotto l'attività non progettuale, quindi andiamo a vedere
[00:25:02] la tabella attività non progettuale che ha attributo giorno, ed è, credo, l'unico
[00:25:13] Sì, ah no, serve anche il tipo, ok, il tipo perché l'acquieri ci impone la condizione,
[00:25:27] il quesito ci impone la condizione che le attività non progettuali debbano essere
[00:25:32] di tipo didattica. Quindi, select, distinto, giorno, from, attività, non progettuale.
[00:25:47] Il condizionale si esprime con la clausola where, dove andiamo ad inserire tipo uguale
[00:26:00] l'ordinamento si fa con l'order by, l'order by giorno in modo ascendente, anche se di default
[00:26:20] l'ordinamento è ascendente, però è sempre meglio essere espliciti per chiarezza e questa
[00:26:29] la queri che ci aspettiamo. Occhio vi faccio notare una cosa che se andiamo a togliere
[00:26:38] l'order by è risultato esattamente lo stesso, questo perché con il distinct il DB va a
[00:26:47] fare già un ordinamento di suo perché è molto più semplice, è meglio è molto
[00:26:53] più veloce, andare ad eliminare i pubblicati di un certo attributo quando il l'ordinamento
[00:27:04] è dato esattamente da questo attributo.
[00:27:07] Quanto è che se va a togliere il distinto, questa volta, come vediamo, il risultato non
[00:27:13] è più ordinato.
[00:27:14] Andiamo ad aggiungerci di nuovo order by giorno, anche senza scendente, è sempre
[00:27:24] meglio un interlo, vi faccio vedere che è equivalente il risultato ed è
[00:27:29] equivalente quindi adesso vedete che è ordinando in modo scendente, ma
[00:27:35] vedete anche che andando ad inserire il Distint, va a eliminare i
[00:27:40] pubblicati veramente, ma l'ordinamento è esattamente. E quindi per questo
[00:27:46] webinare è tutto e ci vediamo alla prossima.
