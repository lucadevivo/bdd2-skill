# Trascrizione: E.B.2.2.3.2.4.2 - Cielo 2 -BD2

[00:00:00] Alve a tutti, in questa video esercitazione andremo ad affrontare gli esercizi di cielo 2 inerenti ai raggruppamenti.
[00:00:10] Iniziamo dunque dal primo esercizio che ci richiede di determinare per ogni riporto quante siano le compagnie che abbiano mai avuto tale aeroporto sia come il luogo di partenza che come il luogo di arrivo.
[00:00:25] Iniziamo dunque scrivendo il nostro classico template vuoto e andando a
[00:00:31] specificare all'interno della clausola from le tabelle che ci interessano
[00:00:37] dunque la tabella aeroporto e la tabella compagnia. Inoltre ci accorgiamo però
[00:00:53] che per poter associare l'aeroporto a compagnia abbiamo bisogno delle
[00:00:57] tabelle volo e la tabella arrivo partenza. Adesso andiamo a specificare all'interno
[00:01:11] della nostra clausola AWARE gli attributi che ci consentiranno per la
[00:01:15] punto di fare il join quindi avremo appunto vcomp uguale a c nome avremo
[00:01:27] poi arrivo partenza codice uguale v punto codice quindi il codice del volo e infine
[00:01:40] arrivo avremo per l'appunto la compagnia quindi app.compagnia uguale a c.nome
[00:01:49] adesso il testo ci richiede di considerare per ogni aeroporto sia i voli di
[00:01:58] arrivo che voli di partenza dunque dobbiamo imporre tal in condizione all'interno
[00:02:02] della glasola word, scrivendo che ap.partenza uguale a.codice or, quindi simultaneamente
[00:02:16] andiamo a considerare che ap.arrivo, ap.arrivo sia uguale a.codice.
[00:02:26] Adesso, eseguendo la query allo stato attuale, possiamo notare che per ogni volo
[00:02:37] Nostro output avremo due nuplé, una con l'aeroporto di arrivo ed una con l'aeroporto di partenza
[00:02:44] come possiamo vedere appunto da questa tabella di output avremo che
[00:02:50] nuplé numero 1 e nuplé numero 2 saranno entrambi inerenti al volo 132
[00:02:55] ma nel primo caso avremo appunto l'aeroporto di riferimento sarà JFK Airport e il secondo invece l'aeroporto di Roma
[00:03:02] Fiumicino. Quindi il testo adesso ci richiede di
[00:03:05] di raggruppare le ennubre determinando una partizione per ogni singola aeroporto.
[00:03:13] Dunque aggiungiamo il costrutto per appunto group by che ci consente di eseguire delle
[00:03:25] partizioni all'interno del nostro output. Nel nostro caso noi vogliamo raggruppare
[00:03:34] le ennubre per l'aeroporto, dunque specificheremo all'interno di tale costrutto a punto codice,
[00:03:40] ovvero il codice dell'aeroporto e il nome. Adesso andiamo per l'appunto a definire la nostra
[00:03:53] target list, poiché abbiamo utilizzato un recroupamento, sappiamo che nella nostra target list
[00:03:59] potremmo utilizzare un subset di attributi che compongono la clausola group by, quindi in
[00:04:05] In questo caso andremo a utilizzare entrambi attributi del codice e del nome dell'aeroporto.
[00:04:10] Se eseguiamo la query così come poiché abbiamo ottenuto le partizioni all'interno della
[00:04:26] nostra tabela di output ma non avendo, per l'appunto, utilizzato alcuna funzione di
[00:04:31] aggregazione, non avremo alcun valore associato a tali partizioni, a tali raggruppamenti.
[00:04:37] Dunque per completare l'esercizio non ci resta che contare il numero di compagnie distinte che
[00:04:44] siano associate ad ognuno di queste partizioni di reagruppamenti.
[00:04:48] Per fare ciò dunque andremo ad inserire all'interno della nostra target list l'instruzione count
[00:04:58] associata per l'appunto all'instruzione distinte che andremo a rinominare per l'appunto
[00:05:13] come non compagnia. Ricordiamo che appunto l'istruzione Listing ci permetterà di non
[00:05:28] avere all'interno del nostro output dei conteggi della stessa compagnia associata alla stessa
[00:05:33] partizione. Dunque andiamo ad eseguire la query e per l'appunto possiamo ritrovare
[00:05:42] il risultato aspettato, il risultato atteso. Passiamo adesso al secondo esercizio.
[00:05:51] Il secondo esercizio ci richiede di determinare quanti siano i voli che
[00:05:55] partono dal rapporto con codici htr e hanno naturata di almeno 100 minuti.
[00:06:01] Dunque iniziamo l'esercizio partendo dal nostro template vuoto e andiamo a
[00:06:06] specificare all'interno della clausola from le tabelle di cui abbiamo
[00:06:10] bisogno quindi leggendo il testo dell'esercizio, ci accorgiamo che ci viene
[00:06:15] richiesta la durata del volo che possiamo trovare per l'appunto nella tabella
[00:06:18] volo e appunto una condizione sull'arrioporto di partenza e quindi
[00:06:27] utilizzeremo la tabella hard part. Andiamo adesso a specificare all'interno
[00:06:36] della nostra clasola where la condizione che ci permetterà di costruire il
[00:06:41] tra le due tabelle, ovvero che il codice del volo sia uguale appunto a ap.codice.
[00:06:48] Se eseguiamo la query allo stato attuale, appunto possiamo usare che per ogni volo avremmo
[00:06:57] le informazioni relative all'arrivo e alla partenza.
[00:07:01] Adesso andiamo ad imporre all'interno della nostra clausola where le condizioni circa
[00:07:07] per l'aeroporto di partenza che deve essere htr e la durata.
[00:07:12] quindi andremo a scrivere che ap.partenza sarà uguale ad htr o per il codice dell'aeroporto
[00:07:21] and v.durata-minuti deve essere maggiore o uguale di 100.
[00:07:32] Eseguendo la quiera allo stato attuale possiamo notare che all'interno del nostro output
[00:07:49] avremo un'unica n nupla adesso il testo dell'esercizio ci richiede però di
[00:07:58] ritornare di contare quanti siano i voli che rispettano tale condizioni di
[00:08:04] conseguenza per fare ciò andremo ad utilizzare per l'appunto la funzione
[00:08:11] l'aggregazione count che andrà a contare le nuple all'interno del
[00:08:16] del nostro output, che in questo caso è formato per l'appunto da un'unica ennubula, quindi
[00:08:20] scriveremo count, has, voli e otteniamo per l'appunto il risultato desiderato. Specifichiamo
[00:08:32] che poiché in questo caso ogni volo occorre un'unica volta all'interno della tabella
[00:08:39] arrivò partenza. In questo caso possiamo permetterci di non andare ad utilizzare l'operatore
[00:08:52] distinct, l'instruzione distinct all'interno della funzione di aggregazione count, ma in
[00:08:59] casi in cui appunto non saremo potuti partire da tale assunzione avremmo dovuto necessariamente
[00:09:05] scrivere count distinct e v punto codice e avremo ottenuto per l'appunto un risultato
[00:09:20] del tutto del tutto uguale in questo caso. In specificiamo inoltre che poiché in questo
[00:09:27] caso sappiamo che all'interno di arrivo partenza ogni vola è presente un'unica volta possiamo
[00:09:32] permetterci di non utilizzare distinct in quanto risulta essere un'operazione più
[00:09:38] dispendiosa e più costosa. Inoltre la queri che abbiamo, questa queri che abbiamo
[00:09:45] prodotta è del tutto equivalente alla queri che avremmo avuto specificando come
[00:09:50] parametro all'interno della funzione aggregazione count il codice. Come
[00:09:59] possiamo vedere il risultato è lo stesso ma in questo caso abbiamo
[00:10:02] utilizzato per l'appunto il count star in quanto risulta essere un'operazione
[00:10:08] meno dispendiosa e meno costosa. L'esercizio numero 3 ci requiere di trovare quanti
[00:10:21] siano gli aeroporti sui quali opera la campagna apitalia per ogni nazione nella
[00:10:26] quale essa opera. Dunque iniziamo l'esercizio specificando all'interno
[00:10:33] la glasola from, le tabelle che abbiamo bisogno per recuperare tali informazioni,
[00:10:37] quindi leggendo il testo sappiamo di per certo che dovremmo utilizzare per
[00:10:40] appunto la tabella luogo e apporto e la tabella volo nella quale possiamo
[00:10:52] trovare informazioni sulla compagnia. Notiamo inoltre che per poter eseguire
[00:10:58] il join di associare tali tabelle abbiamo bisogno anche delle
[00:11:02] tabelle a aeroporto e la tabella a rivo partenza, adesso andiamo per l'appunto a
[00:11:17] specificare all'interno della nostra clausola where le condizioni che ci
[00:11:22] permetteranno di seguire il join, ovvero che l punto aeroporto sia uguale a
[00:11:28] punto codice, abbiamo bisogno perché il codice del volo sia uguale sia per la
[00:11:39] tabella app.volo che la tabella arrivo partenza quindi app.codice e infine come
[00:11:49] per l'esercizio precedente abbiamo bisogno di considerare sia i voli in
[00:11:53] partenza che i voli in arrivo quindi questo lo andremo a specificare con un or e
[00:12:00] avremo una condizione che è app.partenza uguale a.codice oppure che
[00:12:11] api.arrivo sia uguale per l'appunto ad apunto codice, che è il codice dell'aeroporto.
[00:12:23] Infine andiamo a specificare la condizione che impone appunto la compagnia
[00:12:34] pitalia ovvero che la compagnia di questi voli che stiamo andando che
[00:12:39] stiamo andando per l'appunto considerate un essere associati alla
[00:12:42] compagnia apitalia dunque scriviamo e v punto comp per la compagnia è uguale ad apitalia
[00:12:51] adesso se andiamo per l'appunto a diseguire la query allo stato attuale possiamo per
[00:13:05] l'appunto trovare tutti i voli delle informazioni dei voli associati appunto all'aeroporto di
[00:13:12] arrivo l'aeroporto di partenza che siano inerenti alla compagnia apitalia adesso quello
[00:13:19] che noi vogliamo fare su questo output è quello di raggruppare tutte queste nubile per
[00:13:26] nazione e poi associare a tale, a ognuno di queste partizioni, o quindi a ognuno delle
[00:13:33] nazioni, il conteggio distinto degli aeroporti. Per fare ciò quindi utilizzeremo il costrutto
[00:13:40] group by nella quale andremo per la punta a specificare quale colonna dobbiamo utilizzare
[00:13:49] dei periodi di occupamento ovvero l punto nazione. Adesso andiamo a comporre la nostra
[00:13:59] target list poiché abbiamo utilizzato il costrutto group by sappiamo che gli attributi
[00:14:08] specificati all'interno della target list dovranno essere un subset di attributi specificati
[00:14:15] all'interno della clausola group by quindi in questo caso abbiamo un unico attributo
[00:14:19] che andremo a utilizzare, ovvero la nazione. Adesso, poiché vogliamo ad aggregare, vogliamo
[00:14:31] associare ad ognuna delle partizioni, il conteggio degli aeroporti distinti, andremo ad adoperare
[00:14:40] l'utilizzo della funzione di aggregazione count associata appunto all'istruzione
[00:14:46] distint su ovviamente il codice degli aeroporti. Sottolineiamo che se non avessimo utilizzato
[00:14:59] in questo caso l'istruzione disting, avremmo potuto ottenere situazioni in cui ad una nazione
[00:15:07] è associata nel conteggio più volte lo stesso aeroporto.
[00:15:12] Quindi denominiamo infine, che vuolona come infine andiamo a eseguire la nostra query
[00:15:27] e possiamo per l'appunto ritrovare il risultato aspettato.
[00:15:31] Sottolineiamo ancora una volta che debba esserci necessariamente la concordanza tra la clausola
[00:15:38] group by e le colonne che vado a specificare all'interno della target list.
[00:15:43] Se in questo caso avessi utilizzato una colonna che non è presente all'interno della clausola
[00:15:50] group by e quindi che non è stato utilizzato per creare la partizione, quindi come ad
[00:15:54] esempio la compagnia, possiamo notare che otteniamo per l'appunto un errore che
[00:16:02] ci dice che la colonna all'interno della target list compagnia deve essere inserita all'interno
[00:16:09] della clausola group by oppure deve essere utilizzata all'interno di una funzione di
[00:16:14] aggregazione come fatto come per l'appunto con il codice dell'aeroporto. L'esercizio
[00:16:22] numero 4 ci richiede di determinare quale sia la media il massimo e il minimo della
[00:16:27] durata dei voli effettuati dalla compagnia magic fly. Per la risoluzione di tale esercizio
[00:16:34] bisogno unicamente da tabella a volo, all'interno della quale potremmo trovare la durata di ogni
[00:16:40] volo. Quindi iniziamo a non specificare la tabella a volo all'interno della nostra clasola from
[00:16:45] e specificando come condizioni all'interno della clasola where che la compagnia associata appunto
[00:16:53] ai voli che vogliamo considerare sia per la punto magic fly quindi v.comp sarà per la
[00:17:01] appunto quale è a magic fly eseguiamo la query allo stato attuale e otterremo per
[00:17:11] l'appunto tutti i voli di magic fly all'interno della nostra base di dati
[00:17:16] adesso noi vogliamo andare ad ottenere delle statistiche sulla colonna durata
[00:17:22] minuti quindi la prima statistica richiesta è la media per andare per
[00:17:26] l'appunto a calcolare la media andremo ad utilizzare l'istruzione
[00:17:30] average a vg su ovviamente la colonna che ci interessa ovvero v punto durata
[00:17:37] minuti e rinominiamo questa colonna come durata media
[00:17:47] adesso andiamo a rintracciare il massimo dunque per ritrovare il massimo
[00:18:02] all'interno della colonna durata minuti utilizzeremo l'istruzione max
[00:18:08] specificando ancora una volta la stessa colonna, quindi v.durata-minuti e la
[00:18:19] rinominiamo come max-durata. Infine dobbiamo rintracciare il minimo e la
[00:18:29] funzione e l'istruzione che ci permetterà di determinare il minimo sulla
[00:18:34] colonna-durata-minuti sarà per l'istruzione min. Andremo ad utilizzare
[00:18:39] ancora una volta la colonna-durata-minuti. Andiamo ad eseguire la
[00:18:51] nostra query e appunto ritroviamo il risultato atteso.
[00:18:57] Andiamo adesso ad eseguire la query numero 5, la quale ci chiede quale è l'anno di
[00:19:05] fondazione della compagnia più vecchia che opera in ognuno degli aeroporti, scriviamo
[00:19:12] il testo della query all'interno di un commento e andiamo ad inserire le solite
[00:19:18] clausole per lo svolgimento dell'aquelli, a l'interno della clausola from andiamo
[00:19:27] ad inserire le tappelle di cui ci interessano per lo svolgimento dell'aquelli quindi la
[00:19:34] tappella sull'aeroporto, la tappella a compagnia, poi dobbiamo sapere gli
[00:19:42] aeroporti, i voli che sono offerte dalle varie compagnie, quindi la
[00:19:49] della bella volo e dove arrivano e dove partono questi voli, quindi la dappella Rpart.
[00:19:55] All'interno della classe la UER andiamo a dire poi che la volo.compagnia è uguale
[00:20:05] a compagnia.nome, deve essere uguale a compagnia.nome, andiamo a dire che Rpart.codice deve
[00:20:16] uguale a volo punto codice e poi andiamo a dire che un aeroporto può essere un
[00:20:26] aeroporto di partenza o un aeroporto di arrivo come facciamo a fare questa cosa
[00:20:30] anzi tutto andiamo a dire che può essere un aeroporto di partenza quindi a punto
[00:20:35] codice è uguale al porto a part app.partenza oppure app.codice può essere un aeroporto
[00:20:49] che arriva e andiamo a inserire tutto insieme a 40 secondi e vediamo la
[00:21:02] qual'è il definitore, cosa ci si torna, ci torna appunto tutte le annule e tutti i dati
[00:21:08] relativi ai voli, quindi di questi dati dobbiamo capire quale è l'anno in questa fondata
[00:21:18] la compagnia più vecchia per ogni aeroporto, quindi che opramo le varie aeroporti, per
[00:21:22] fare questo andiamo in su, sicuramente a prendere aeroporto.podice e aeroporto.node
[00:21:32] e ovviamente vediamo che se quando questa query abbiamo preso la tabella codice
[00:21:42] e la colonna codice e la colonna nome di ogni volo quindi andiamo a
[00:21:50] recruppare per questi due campi utilizzando il group by in modo tale da
[00:22:04] da non avere tutti tutti i duplicati e in modo tale da poter andare a utilizzare l'aggregato
[00:22:17] min che ci dice che possiamo prendere il valore minimo della colonna fondazione quindi
[00:22:25] compagnia.annoFondazione. In questo modo possiamo vedere che nell'aeroporto di Roma
[00:22:35] la compagnia più antica che opera è stata fondata nel 1900 quindi andando a
[00:22:45] raggruppare sia per codice che per nome e poi andando ad utilizzare il min sull'anno
[00:22:52] di fondazione della compagnia vediamo che riusciamo a destrapolare in questo
[00:23:00] caso la compagnia più vecchia per ogni aeroporto, andiamo a rinominare la colonna min con anno
[00:23:07] eseguiamo ed ecco qui la quale numero c'è in questa volta, passiamo a svolgere la quale
[00:23:17] numero sei, la quale ci chiede quante sono le nazioni diverse raggiungibile da ogni
[00:23:24] in azione tramite uno o più voli, quindi inseriamo sempre il commento con il tasto
[00:23:39] della query ed andiamo a scrivere le solite clausole, di cosa avremo bisogno?
[00:23:48] avremo bisogno sicuramente dei luoghi degli aeroporti e abbiamo bisogno di due
[00:23:57] tabelle di questi luoghi perché abbiamo bisogno sia per l'aeroporto di
[00:24:00] arrivo che per l'aeroporto di partenza quindi l'aeroporto di l'aeroporto A1 e il
[00:24:05] luogo aeroporto L2. Poi avevamo bisogno di sapere i voli, quindi
[00:24:16] i dati radivi ai voli, quindi il volo V. Abbiamo bisogno di sapere i dati radivi agli
[00:24:21] aeroporti, quindi a aeroporto A1 che mostrovamente prenderemo in
[00:24:27] considerazione come aeroporto di partenza e aeroporto A2 che prenderemo
[00:24:32] in considerazione come aeroporto di arrivo e poi la tabella R part che ci dà indicazione
[00:24:39] sull'arrivo e la partenza dei vari poli e all'interno della clasola UL andiamo ad
[00:24:50] inserire alcune condizioni come il luogo dell'aeroporto della tabella luogo aeroporto
[00:25:06] deve essere uguale a 1 punto codice, quindi all'aeroporto di partenza, quello che considereremo
[00:25:15] all'aeroporto di partenza, e la stessa cosa per l'aeroporto 2, quindi l2 punto aeroporto,
[00:25:24] dev'essere uguale a 2.14. Poi successivamente ci interessa sapere che la nazione dell'aeroporto
[00:25:38] a 1 è diversa la nazione dell'aeroporto a 2 quindi possiamo farlo con l1 appunto
[00:25:43] un'azione diverso dalle 2.nazione e ci interessa inoltre sapere che il volo della
[00:25:58] tabella ARPART, quindi ARPART.codice è uguale a volo.codice e poi andiamo a
[00:26:07] dire che l'aeroporto di partenza è a 1.codice e facciamo lo stesso per l'aeroporto di arrivo
[00:26:20] quindi facciamo part.arrivo è uguale a 2.codice. Perfetto. Cosa vogliamo sapere quindi? Vogliamo
[00:26:35] sapere quante nazioni sono raggiungibili da ogni nazione, per fareciò innanzitutto proviamo
[00:26:45] a stampare questa quale, ok, anche il secto, la taglia è stata ok, vediamo, possiamo prendere
[00:26:57] le nazioni di partenza, quindi l1.nazione ed estampiamo e da ognuna di queste vogliamo
[00:27:13] sapere quante nazioni sono raggiungibili, quindi per fare ciò in azzi tutto andiamo
[00:27:21] utilizzare il group by per raggruppare le ennouple per la nazionalità, e le
[00:27:36] reagruppiamo per l1.nazione. In una volta che le abbiamo
[00:27:42] raggruppate possiamo andare a conteggiare, quindi usiamo il count,
[00:27:49] usiamo il count, quante nazioni sono raggiungibili dalla nazione L1, quindi andiamo a contare
[00:28:02] L2.Nazione. Ok, l'ultima cosa da perfezionare, che contando in questo modo, vengono contati
[00:28:19] anche i duplicati di L2, mentre noi vogliamo quante sono le nazioni diverse. Andiamo
[00:28:26] di inserire all'interno del count un Distint, vediamo infatti che per esempio dalla francia
[00:28:34] può raggiungere sulla mentorna razione, per l'Italia la mentorna razione e così via,
[00:28:39] rinominiamo questa colonna con la che abbiamo raggiungibili ed eseguiamo l'acquari, perfetto,
[00:28:49] questa è l'esecuzione dell'acquari numero 6, passiamo ora all'acquari numero 7 da
[00:28:55] quale ci chiede, quale è la durata media dei voli che partono da ognuno degli
[00:29:03] ok per fare ciò andiamo sempre ad inserire i nostri i nostri clausole
[00:29:12] adesso trovate la query, nel from andiamo ad inserire le tabelle di cui avremo bisogno
[00:29:24] quindi andiamo ad inserire la tabella aeroporto sicuramente, la tabella polo per vedere i dati
[00:29:35] che vediamo da dove partono i vari voli. Andiamo a inserire la clauselaware.
[00:29:52] All'interno della clauselaware dobbiamo dire che il codice del volo è uguale a darpart.codice.
[00:30:01] Poi dobbiamo dire che la partenza, quindi i voli che partono al part.partenza deve essere uguale
[00:30:15] a parto da questo aeroporto, aeroporto.podice, e andiamo a cominciare a deseguire questa questa query.
[00:30:30] Ok, abbiamo tutti i dati delle varie e non l'appunto. Cosa vogliamo inserire nella target list?
[00:30:42] Vogliamo inserire sicuramente il codice e il nome dell'aeroporto perché siamo interessati
[00:30:50] alla media, la durata media dei voli che è partuta ognuno degli aeroporti quindi sicuramente
[00:30:56] siamo interessati ad inserire a punto codice e a punto nome quindi andiamo a
[00:31:03] tutti gli aeroporti interessati nei voli e di questi aeroporti poi dobbiamo andare
[00:31:14] a calcolare la durata media dei voli che partono insomma da questi aeroporti
[00:31:19] come facciamo per fare ciò andiamo a raggruppare per questi aeroporti come
[00:31:25] abbiamo già fatto nella colore numero 5, non racculpiamo solamente per un valore
[00:31:30] ma racculpiamo per due valori, andiamo a racculpare per app.codice e per app.nome
[00:31:37] e poi andiamo a calcolare la media della durata dei voli che passano da questi
[00:31:47] da questi riporti quindi per calcolare questa media possiamo utilizzare AVG e lo
[00:31:54] lo utilizziamo sulla durata in minuti del volo
[00:31:57] durata in minuti
[00:32:01] andiamo subire il nome della tabella, la colonna
[00:32:05] e il nome della media
[00:32:07] ok, quindi adesso possiamo vedere che la media della durata
[00:32:17] per l'aeroporto FCO, quindi l'aeroporto Roma Fiumicino
[00:32:21] la meta della durata dei voli è di 545 minuti
[00:32:25] mentre per l'aeroporto di Londra è di 105 minuti e così via
[00:32:29] Passiamo alla quale numero 8, andiamo a scrivere il testo della quale numero 8 dentro
[00:32:43] nel commento e andiamo a leggere cosa ci chiede.
[00:32:45] Quale è la durata complessiva dei boli operati da una delle compagnie fondate a partire
[00:32:51] dal 1950.
[00:32:53] Prima di tutto possiamo selezionare tutte le compagnie con anno di fondazione maggiore
[00:33:11] il 1950, quindi nella clasula from, a me al fare mia c e nella clasula where possiamo
[00:33:29] fare c.annofondats maggiore o uguale a 1950. Vediamo quali sono le compagnie. Questi sono
[00:33:42] compagnia fondate fondate dopo il 1950 quindi a parte del 1950 cosa abbiamo
[00:33:52] vedere adesso qual è la durata complessiva dei voli di queste compagnie
[00:33:55] quindi all'interno della clausola from andremo a inserire anche la tabella volo
[00:34:01] all'interno della clasera where andiamo ad inserire che volo.comp deve essere uguale
[00:34:16] a c.nome e di queste accompagniamo a sapere la durata complessiva dei voli quindi andiamo
[00:34:27] sicuramente iniziamo nella target list, la compagnia con tuo nome e dobbiamo raggruppare
[00:34:37] queste compagnie quindi utilizzare il group by per il nome appunto della compagnia quindi
[00:34:43] per c.no come facciamo a sommare la durata complessiva
[00:34:53] di volo operare da queste compagnie quindi raggruppando le compagnie per nome possiamo
[00:34:58] dire di vuole fare la somma della durata in minuti dei voli queste compagnie quindi volo punto
[00:35:10] durata in minuti perfetto e andiamo a denominare direttamente questa colonna con durata totale
[00:35:27] per la durata compressiva dei minuti dei voli operati da queste compagnie.
[00:35:35] Pagliato.
[00:35:41] Mancalende.
[00:35:42] Siamo la query.
[00:35:46] Quindi vediamo che la compagnia Matchfly, che abbiamo visto,
[00:35:50] è stata fondata dopo il 1950,
[00:35:54] ha una durata compressiva dei voli di 1260 minuti e così via.
[00:36:03] Continuiamo l'esercitazione CELO 2 della quiri numero 9.
[00:36:12] Andiamo a scrivere il template vuoto e a selezionare le tabelle di interesse.
[00:36:18] La prima tabella e la tabella d'aeroporto, qui abbiamo la tabella compagnia, arrivi e partenze e volo.
[00:36:25] Andiamo a selezionare i campi da ritornare, quindi in questo caso il codice e il nome degli aeroporti presi dalla tabella aeroporto.
[00:36:48] Per quanto riguarda le condizioni da controllare, in primis andiamo a verificare che la compagnia presa alla tabella volo corrisponda a quella della tabella compagnia.
[00:36:59] E facciamo lo stesso con il codice preso da arrivi e partenze e il codice di volo invece dalla tabella volo.
[00:37:07] Infine andiamo a controllare che il codice preso dalla tabella aeroporto
[00:37:18] corrisponda o al codice di partenza nella tabella rivie partenze o al codice di
[00:37:24] arrivo. Infine andiamo a raggruppare per codice dell'aeroporto quindi con il
[00:37:39] group-by sull'attributo codice della tabella aeroporto e andiamo a
[00:37:43] verificare che ci siano almeno due compagnie legate agli aeroporti che
[00:37:52] appunto vengono ritornati in questo modo e questo è il risultato della Quiri.
[00:38:14] Passiamo alla Quiri numero 10 e andiamo a scrivere le tabelle di interesse,
[00:38:22] quindi la tabella logreporto scritta per due volte.
[00:38:28] questo mondo ne avremo due copie che ci serviranno a verificare che appunto
[00:38:39] l'esistenza di almeno due aeroporti differenti e andiamo a ritornare l'attributo
[00:38:44] città che possiamo prendere da una delle due tabelle è indifferente infatti
[00:38:49] la prima condizione che andremo a controllare è proprio che la città
[00:38:52] del primo aeroporto sia identica alla seconda e poi andremo a verificare che
[00:38:58] l'aeroporto della prima tabella sia differente dalla seconda
[00:39:04] In questo modo ci assicuriremo che ci sono almeno due riporti differenti legati alla stessa città.
[00:39:09] Se lasciamo il codice in questo modo, però una città può essere ripetuta più di una volta,
[00:39:16] quindi andiamo a inserire il distinct, come comando,
[00:39:21] ed ecco qui il risultato.
[00:39:23] Passiamo quindi all'undicesima query.
[00:39:29] Anche in questo caso devo scrivere il template puoto e poi a inserire le tabelle di interesse,
[00:39:36] questo caso la tabella compagnia e la tabella volo. Come richiesto dalla traccia
[00:39:45] andiamo a ritornare il nome della compagnia e andiamo a verificare in
[00:39:52] primis che la compagnia della tabella volo corrisponda a quello della tabella
[00:39:56] compagnia e poi andiamo a raggruppare per compagnia, quindi per l'attributo nome
[00:40:06] della tabella compagnia e a verificare che la media della durata, in questo
[00:40:12] caso ce l'abbiamo in minuti nella tabella volo si ha maggiore di 6 ore quindi 6 per 60 essendo
[00:40:22] in minuti e questo è il risultato. Diamo poi a eseguire l'ultima query quindi nuovamente il
[00:40:47] template vuoto e in questo caso come tabelle di interesse abbiamo la tabella compagnia e la
[00:40:51] tabella volo e come campi di interesse da ritornare abbiamo nuovamente il nome della
[00:40:58] la compagnia. Verifichiamo come nella qui di precedente che la compagnia della tabella
[00:41:06] volo corrisponda a quella della tabella compagnia, raggruppiamo come prima per
[00:41:15] compagnia e verifichiamo invece che il minimo della durata dei voli sia di
[00:41:23] 100 minuti. Quindi andiamo a selezionare il volo di durata minimo e
[00:41:27] ci assicuriamo che sia maggiore a 100. E questo è quanto è ritornato.
[00:41:36] finiamo in questo modo l'esercitazione CELO 2
