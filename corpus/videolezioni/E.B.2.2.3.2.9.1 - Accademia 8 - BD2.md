# Trascrizione: E.B.2.2.3.2.9.1 - Accademia 8 - BD2

[00:00:01] Alve a tutti, benvenuti nell'Esercitazione Akademia 8 in centrata su Outer Join quelli anni date.
[00:00:09] Dunque partiamo dal primo esercizio che ci richiede di determinare quali siano le persone, con i di, nome, cognome,
[00:00:20] che hanno avuto assenze solo nei giorni in cui non avevano alcuna attività, sia progettuale che non progettuale.
[00:00:28] Dunque, nella risoluzione di questo esercizio, daremo una prima versione in cui utilizziamo
[00:00:34] una query adnidata nella clasola WHERE e poi una più efficiente basata su OuterJoin.
[00:00:39] In questa prima versione, vogliamo rimuovere o non considerare all'interno della tabella
[00:00:45] persona che andremo per l'appunto a inserire all'interno di una clasola FROM.
[00:00:54] vogliamo non considerare tutte le nubile che hanno effettuato delle assenze in dei giorni in cui avevano delle attività, dunque definiamo all'interno della nostra target list per le colonne che ci interessano, quindi in questo caso avremo l'edì della persona come richiesto,
[00:01:21] apriamo poi il nome e apriamo quel cognome.
[00:01:36] Adesso quello che vogliamo fare è combinare questa prima queri ad un'altra queri che
[00:01:45] venga utilizzata per sottrarre le annuble indesiderate.
[00:01:50] Dunque per fare ciò facciamo ricorso all'operatore except che per l'appunto
[00:02:00] Date 2 query, restituisce, diciamo, determina, seleziona tutte le ennucle della prima query
[00:02:12] che non sono all'interno della seconda query che viene data.
[00:02:17] Dunque adesso dobbiamo definire la nostra seconda query che avrà, come target list,
[00:02:25] la stessa identica target list della prima query, quindi avremo select, distinct, avremo
[00:02:31] poi lidi della persona, il nome della persona e il cognome.
[00:02:45] Adesso le tabelle di differimento per questa seconda query saranno per l'appunto la tabella
[00:02:50] persona e la tabella assenza.
[00:03:03] Adesso definiamo all'interno della clausola web gli attributi che andiamo ad utilizzare per l'appunto per fare il join, ovvero che appunto persona sia uguale per l'appunto di della persona.
[00:03:21] Adesso, quello che vogliamo fare è scrivere all'interno della clausola where la condizione in cui il giorno di riferimento non sia né un giorno di un'attività progettuale per una data persona, né il giorno di un'attività non progettuale.
[00:03:46] quindi per fare ciò faremo per l'appunto ricorso a due queri annitate
[00:03:50] quindi scriviamo la prima, ovvero quello per le le attività, le attività di
[00:03:56] progetto, i giorni di attività di progetto, quindi scriveremo che il giorno
[00:04:02] dell'assenza sia uguale, usiamo, utilizziamo eni per definire una
[00:04:09] qualsiasi di queste ennue e andiamo a scrivere per la, per la, per selezionare
[00:04:16] un qualsiasi giorno di questo tipo quindi avremo select, giorno from, attività, progetto, ap,
[00:04:34] where soprattutto quindi la persona dell'attività e sia per la appunto la persona che ha eseguito
[00:04:45] l'assenza quindi ap.persona uguale a.persona. Il discorso molto molto simile va fatto appunto
[00:04:58] per le attività non progettuali quindi avremo or e definiamo per l'appunto che è il giorno
[00:05:14] quindi il giorno dell'assenza sia in qualsiasi giorno di un'attività non progettuale riguardante
[00:05:25] quella persona, quindi select, giorno, from, attività non progettuale, tanto che la persona
[00:05:54] di differimento di tale attività, np. persona, sia, per l'appunto, la persona relativa
[00:06:02] l'assenza. Infine quello che vogliamo, quello che ci resta a fare è per l'appunto andare ad
[00:06:16] imporre un ordinamento sul nostro output finale. Quindi per fare ciò andremo ad utilizzare per
[00:06:26] l'appunto il costruttore del BIID. Andiamo adesso a eseguire la nostra query e possiamo per
[00:06:43] appunto trovare il risultato atteso. La problematica principale riguardante la
[00:06:54] soluzione che abbiamo appena proposta riguarda per l'appunto l'ottimizzazione
[00:06:59] delle performance in quanto se per l'appunto andiamo a inspezionare la
[00:07:04] query che abbiamo appena fatto possiamo notare che abbiamo ben due subquery
[00:07:09] all'interno una clausola war che sono correlate rispetto appunto alla
[00:07:16] queri più esterna infatti abbiamo appunto delle coelonne che vengono coinvolte
[00:07:21] dalla queri più esterna e la queri più interna e questo fa in modo che la
[00:07:28] sub queri entrambe le sub queri debbano essere
[00:07:32] rigalcolate ogni volta per ogni persona e questo ha degli impacti
[00:07:37] estremamente negativi in termini di performance. Quindi una soluzione del
[00:07:44] tutto equivalente, che però risulta essere sicuramente più performante è
[00:07:48] utilizzando gli outer join, gli outer join che per l'appunto sfruttano l'indice e
[00:07:54] ci consentire di non dover recalcolare ad ogni volta, appunto, i valori sul
[00:08:00] giorno dell'attività progettuale e non progettuale. Quindi andiamo a vedere come
[00:08:05] possiamo scrivere una query equivalente in questo caso, ma che è sicuramente più
[00:08:10] ottimizzata in termini di performance. Quindi partiamo sempre dal nostro
[00:08:15] template vuoto. Quindi andiamo a scrivere all'interno della nostra
[00:08:20] clausola from dove andremo innanzitutto a correlare ad ogni persona le
[00:08:25] potenziale, le potenziale assenze. Dunque andiamo a scrivere tra
[00:08:34] parentesi che persona persona p left order join alla tabella senza che chiamiamo a on punto
[00:09:03] persona e ovviamente l'id della persona p punto id dunque andiamo innanzitutto a eseguire questa
[00:09:16] questa quera intermedia e appunto guardando il risultato possiamo vedere che ad ogni
[00:09:34] persona è associata per l'appunto un'assenza. Ovviamente perché si sta
[00:09:39] parlando di un left outer join, nei casi in cui una persona non abbia appunto
[00:09:45] svolto, non abbia delle assenze da registrare, viene per l'appunto
[00:09:51] presentato delle Nuprenal in corrispondenza della tabella assenza, poiché per la punta
[00:09:57] è un left outer join, quindi in questo caso nella tabella di sinistra vengono utilizzate
[00:10:02] tutte le Nupre nella tabella di destra se non ci sono corrispondenze. Circa il join vengono
[00:10:11] presentate le Nupre con un valore a Null. Quindi adesso andiamo a utilizzare un
[00:10:18] un ulteriore join, quindi un ulteriore left outer join con le attività di
[00:10:24] progetto, quindi vogliamo associare delle attività di progetto che abbiano lo
[00:10:29] stesso giorno delle assenze. Quindi andremo a scrivere, ancora una volta,
[00:10:35] left outer join di questa tabella di output, per l'appunto rispetto all'attività
[00:10:48] progetto. Eseguiamo ancora una volta, ovviamente non abbiamo definito il join, quindi definiamo
[00:11:09] che app.persona è uguale a.persona, ovviamente perché vogliamo utilizzare sempre la persona
[00:11:19] come elemento ricorrente al sempre presente nella nostra tabella e ovviamente app Giorno
[00:11:29] uguale a Giorno. Andiamo ad eseguire adesso e possiamo vedere che abbiamo aggiunto quindi
[00:11:39] la tabella precedente. Abbiamo eseguito l'Eft Outer Join con le tabelle attività progetto
[00:11:45] quindi la dove, otterremo che la dove abbiamo una persona con un'assenza, andiamo ad associare
[00:11:55] anche tutte le ennuble, delle ennuble di attività, attività progetto, la dove il giorno risulta
[00:12:03] essere lo stesso, la persona risulta essere quella della prima tabella e il giorno risulta
[00:12:08] essere un giorno appunto dell'attività di progetto.
[00:12:12] Quindi a questo adesso dobbiamo aggiungere anche quello che è le attività, le attività
[00:12:24] non progettuali, quindi abbiamo solamente utilizzato quelle progettuali, quindi scriviamo
[00:12:30] un'altra parentesi e andiamo ad aggiungere con ulteriore left outer join le attività
[00:12:41] non progettuali, nominiamo ANP e il join in questo caso verrà per l'appunto
[00:13:08] eseguito, verrà eseguito sull'obviamente la persona, quindi onANP.persona
[00:13:15] che deve essere uguale ad apunto persona, and ANP giorno è uguale ad apunto
[00:13:28] i giorni. Andiamo ad eseguire la guerra allo stato attuale. Abbiamo un errore di sintassi
[00:13:39] dove l'attività è un progettuale e dunque ancora una volta avremmo per l'appunto ottenuto
[00:14:01] un un un'interiore tabella nella quale abbiamo aggiunto anche le informazioni circa le
[00:14:07] attività non progettuali che avvengono potenzialmente nello stesso, nello stesso giorno che è stato
[00:14:18] definito da appunto quello dell'assenza. Possiamo procedere andando a definire quella che è una
[00:14:28] partizione, solo ovviamente la persona e poiché ci interessa nel nome e il cognome di ogni
[00:14:35] persona allora utilizzeremo entrambe, dove tutte le tali attributi all'interno del costrutto group by
[00:14:42] quindi avremo group by p, di il nome e il cognome. Adesso quello che dobbiamo fare è a dare imporre
[00:15:02] la condizione in questa tabella che abbiamo per l'appunto ottenuto. Adesso randiamo e
[00:15:09] e inseriamo questi elementi nella target list e ragniamo, quello che vogliamo fare è ovviamente
[00:15:19] andare a contare le occorrenze di ogni persona e determinare se tale conteggio sia uguale
[00:15:30] a 0 oppure se avremo dei valori non alle di assenza. Quindi per fare questo utilizzeremo
[00:15:46] per l'appunto il costrutto having che ci permetterà di definire delle condizioni sulla
[00:15:52] funzione aggregata count e quindi avremo che count id deve essere uguale a zero in questo caso quindi
[00:16:05] è il caso in cui non abbiamo, nel caso in cui appunto non è mai non è mai stata eseguita
[00:16:16] alcuna senza quindi dobbiamo considerare anche questo caso e invece eseguiamo il count anche
[00:16:24] quindi impostiamo che il count sia uguale a da punto id e in questo caso vogliamo determinare se
[00:16:33] il conteggio delle assenze sia esattamente uguale al numero di giorni in cui non ci sono
[00:16:44] svolte per l'appunto delle attività progettuali non progettuali quindi per fare questo dovremmo
[00:16:51] appunto sommare tale, tale valore e quindi avremo che app.pd is null and
[00:17:04] np.pd is null. Adesso dovremmo eseguire il casting di tale valore ad intero e aggiungiamo
[00:17:22] la parentesi. Adesso, se andiamo appunto ad eseguire la queria allo stato attuale, possiamo
[00:17:35] vedere che abbiamo ottenuto lo stesso risultato di prima, quindi il risultato di siderato.
[00:17:41] Infine vogliamo imporre un ordinamento, così come ci richiede l'esercizio. Quindi andremo a
[00:17:50] scrivere che order by id e seguendo possiamo vedere appunto che l'output sarà
[00:18:02] appunto ordinato per id. Abbiamo ottenuto quindi un risultato del
[00:18:06] tutto equivalente alla prima risoluzione dell'esercizio ma in questo
[00:18:09] caso risulta essere estremamente più performante in quanto utilizzante una
[00:18:15] soluzione con con outer join che fa per l'appunto utilizzo di indici.
[00:18:20] Siamo adesso al secondo esercizio. Il secondo esercizio ci chiede di determinare quali
[00:18:27] siano le persone con il dinome e cognome che non hanno mai partecipato dal
[00:18:31] com'un progetto durante la durata del progetto Pegasus.
[00:18:34] Dunque in questo caso mostremo una soluzione in cui invece la queri anidata
[00:18:40] all'interno della clausola wear comporterà effettivamente un
[00:18:45] vantaggio intermille di legibilità della queri e inolte non comporterà
[00:18:49] una spesa eccessiva in termini di performance in quanto non avremo alcuna sub-query correllata
[00:18:56] rispetto a quella più esterna. Quindi iniziamo subito la strategia che adotteremo per risolvere
[00:19:06] dalle esercizio sarà quello quindi di definire una query in cui andremo a trovare tutte
[00:19:12] le persone che abbiano partecipato effettivamente ad un progetto durante la durata del
[00:19:19] progetto Pegasus quindi iniziamo scrivendo il nostro template tuoto e per appunto
[00:19:30] ottenere questa informazione andiamo per l'appunto a utilizzare la tabella
[00:19:38] persona avremo poi la tabella progetto e infine avremo appunto la tabella
[00:19:56] attività-progetto. Adesso andiamo ad definire la condizione in cui vogliamo
[00:20:10] che il progetto sia il progetto Pegasus quindi PRPegasus è uguale a Pegasus.
[00:20:18] Avremo poi che vogliamo che imporre il join tra per l'appunto la persona
[00:20:26] tra le la tabella persona e la tabella attività progetto quindi avremo per
[00:20:31] l'appunto che and ap punto persona sia uguale ad p2.id e infine vogliamo
[00:20:46] imporre che tale persona abbia per l'appunto attività partecipato a tale
[00:20:51] all'attività, durante la durata di Pegasus, quindi avremo che end ap.giorno between pr.pegasus.inizio.end.pegasus.fine.
[00:21:17] Adesso, quindi, se andiamo ad eseguire la queri allo stato attuale,
[00:21:21] si intassi rpgasus.none, non abbiamo definito appunto la colonna,
[00:21:41] se andiamo ad eseguire la queri, possiamo appunto notare una tabella in cui abbiamo associato
[00:21:48] le ennuble di persona, di progetto, di attività di progetto, in cui, per l'appunto,
[00:21:56] anche le informazioni circa il giorno in cui si è svolto un'attività di progetto,
[00:22:01] quindi tutti questi giorni sono tutti giorni di attività di progetto di una
[00:22:06] data persona durante la durata di Pegasus. Quindi poche è possibile che si
[00:22:14] possano creare dei valori, dei valori duplicati all'interno di tale
[00:22:19] di tale guerri, andremo innanzitutto a selezionare gli di delle persone in
[00:22:23] quanto sono è il valore che vogliamo utilizzare poi nella queri nella queri più esterna e
[00:22:30] inoltre dobbiamo verificare che effettivamente tali tali id di persone non si ripetano più
[00:22:35] volte quindi utilizzeremo appunto l'operatore distint il costunto distint ovviamente sul
[00:22:45] all'interno della nostra target list utilizzando poi il l'id della persona quindi in questo
[00:22:51] caso otterremo i unici di persone che hanno effettivamente partecipato durante la durata
[00:23:03] di Pegasus ad un qualsiasi progetto, una qualsiasi attività di progettuale. Quindi
[00:23:11] adesso quello che vogliamo fare è utilizzare questa tabella ed escludere quindi dalla
[00:23:18] tabella persona tutte le persone che abbiano questi d quindi andiamo a comporare adesso la query più
[00:23:23] esterna dove avremo per appunto front persona mettiamo questa tra parentesi e avremo appunto il
[00:23:42] from select e where quindi all'interno della cloud la from andiamo a definire per l'appunto la
[00:23:56] la tabella persona. Andiamo poi a definire la nostra cloud, la
[00:24:04] query che sarà dove utilizzeremo appunto la nostra query, la nostra query anidata.
[00:24:07] Infatti vogliamo che gli D delle persone che stanno considerando non siano gli D che
[00:24:12] abbiamo invece definito precedentemente con la nostra query anidata.
[00:24:16] Adesso andiamo a selezionare, a definire all'interno della nostra target list,
[00:24:29] di il nome e il cognome come ci viene richiesto dall'esercizio. Andiamo ad eseguire e appunto
[00:24:48] abbiamo rimosso per appunto tutte le persone che invece hanno effettivamente partecipato
[00:24:56] ad un progetto durante la durata di Pegasus e quindi otteniamo di conseguenza tutte
[00:25:03] le persone che non hanno mai partecipato ad alcun progetto durante la durata del
[00:25:07] il progetto Pegasus. Adesso l'ultima cosa che ci è restata a fare è quello di ordinare
[00:25:14] il risultato, quindi order by id e quindi nella nostra tabella di output id saranno per appunto
[00:25:22] tutti ordinati da un avventi. Adesso specificiamo che tale query, differentemente dalla
[00:25:29] prima versione della query dell'esercizio 1 risulta essere più performante in quanto
[00:25:35] se andiamo a rispezionare la subquery anidata nella clausola wear possiamo definirla come non correlata
[00:25:41] in quanto non abbiamo l'utilizzo all'interno di tale quelle di colonne o di attributi che sono
[00:25:48] stati invece definiti nella query più esterna questo infatti permette al dbms di ottimizzare
[00:25:54] la query andandola a eseguire un'unica volta e poi ad andarla a utilizzare all'interno della
[00:26:01] condizione aware, quindi in questo caso la condizione aware è che l'ID non sia all'interno di tale
[00:26:05] risultato e questo risulta essere essenzialmente più efficiente rispetto invece alla situazione
[00:26:12] precedente in cui invece le query erano correlate alla query esterna.
[00:26:19] Adesso all'esercizio numero 3 che ci richiede l'ID il nome, il cognome e lo stipendio,
[00:26:27] dei ricercatori con stipendio maggiore rispetto a tutti i professori. Quindi in...
[00:26:33] iniziamo quindi questo esercizio andando a definire all'interno della
[00:26:40] clausola from i strutturati, quindi utilizzeremo la tabella persona e
[00:26:49] stabiliamo all'interno della clausola where che la posizione di ogni persona
[00:26:56] che stiamo considerando sia quella di ricercatore. Adesso andiamo conseguentemente ad imporre
[00:27:09] all'interno della nostra clausola wear che lo stipendio sia maggior rispetto allo stipendio
[00:27:16] di tutti i ricercatori quindi per fare per fare ciò facciamo uso di una query anidata all'interno
[00:27:24] della clausola all'interno della nostra clausola wear in cui andiamo ad associare lo stipendio
[00:27:30] andiamo a considerare lo stipendio di tutti i professori associati ed ordinari, quindi per fare
[00:27:37] ciò andremo a scrivere end e lo stipendio della persona, dello strutturato ricercatore considerato
[00:27:48] nella guaria attuale deve essere maggiore di tutte le annuble che andremo a considerare all'interno
[00:27:55] della nostra querianidata, quindi andiamo a scrivere la nostra querianidata, scriviamo il nostro template
[00:28:02] vuoto e andiamo ancora una volta a considerare la tabella persona, in questo caso però utilizzeremo
[00:28:15] un'altra tabella, quindi la denominiamo persona 2, P2. Andiamo poi ad imporre che la posizione sia
[00:28:29] per l'appunto una posizione o ricercatore o professore associato o professore ordinario
[00:28:37] quindi che p2 punto posizione sia uno dei valori ovvero professore ordinario e professore associato.
[00:29:09] Adesso che abbiamo definito la nostra query non ci resta che andare a definire quale valore
[00:29:22] verrà utilizzata all'interno della nostra target list e questo valore poi verrà confrontato
[00:29:27] con lo stipendio della query più esterna, quindi in questo caso vogliamo ancora una
[00:29:33] volta utilizzare il stipendio quindi è primo che p2.stipendio verrà confrontato
[00:29:39] tutte le nuble di stipendio verranno confrontate per lo stipendio della queri esterna. Andiamo ad
[00:29:47] eseguire la queri allo stato attuale e otterremo un'unica ennubla che corrisponde a tale condizione.
[00:30:01] Andiamo quindi ad inserire all'interno della nostra target list le informazioni della
[00:30:07] assolturato che ci interessano, ovvero l'ID il nome, il cognome e lo stipendio e
[00:30:16] infine andiamo a eseguire un ordinamento come ci richiede per l'appunto
[00:30:23] l'esercizio rispetto per l'appunto all'ID quindi avremo order by id e
[00:30:34] ed eseguendo otterremo il risultato di siderato.
[00:30:39] Facciamo notare ancora una volta che, in questo caso,
[00:30:40] l'utilizzo di una query annidata all'interno della cloud
[00:30:44] la query è accettabile, perché ancora una volta la subquery
[00:30:48] non è correlata rispetto alla query più esterna.
[00:30:51] Quindi questo ci permette di eseguire la query una sola volta.
[00:30:58] Il dbms ottimizzerà la query, la seguirà una sola volta
[00:31:01] e lo confronterà ogni volta a quei valori di tipo stipendio.
[00:31:04] Stibile di poter rintracciare una soluzione che sia leggermente più efficiente rispetto
[00:31:14] alla soluzione che abbiamo appena prodotto e infatti ci accorgiamo che se andiamo a
[00:31:21] guardare la nostra queri annidata noi produciamo una serie di ennuble e poi tutti i valori
[00:31:26] di stipendio di queste ennuble vengono per l'appunto confrontate con lo stipendio
[00:31:31] della queri più esterna. Ragionandome sull'esercizio però ci rendiamo conto che non abbiamo bisogno
[00:31:38] di effettuare il confronto con ogni singola nupla, ma abbiamo per l'appunto bisogno di
[00:31:43] effettuare il confronto solamente con il valore massimo dello stipendio di tale nuple.
[00:31:50] Dunque quello che possiamo fare in questo caso è andare a rimuovere l'operatore
[00:31:55] e andiamo dunque ad utilizzare ad estrarre lo stipendio massimo che sia per l'appunto
[00:32:08] dei professori ordinari e dei ricercatori. Quindi per fare ciò utilizziamo la funzione
[00:32:13] aggregata max su per l'appunto lo stipendio. E possiamo vedere che per l'appunto eseguendo
[00:32:21] la queri otterremo una queri del tutto simile alla prima queri un risultato del tutto simile ma
[00:32:27] in questo caso dalla querianità sta uscendo un unico valore che per l'appunto il massimo
[00:32:33] che poi viene confrontato con lo stipendio di tutti i ricercatori. Procediamo con
[00:32:40] lo svolgimento della quarta queri la quale ci chiede quali sono le persone che hanno
[00:32:45] lavorato sui progetti con un budget superiore alla media dei budget di tutti i progetti
[00:32:51] ci sfidiamo il testo della Wary, un commento come sempre, e andiamo a svolgerla.
[00:33:01] Per iniziare a svolgere questa Wary partiamo dal nostro solito template e per vedere quali
[00:33:22] persone hanno lavorato all'interno dei progetti, le tabelle interessate sono una tabella persona
[00:33:28] sicuramente e la tabella attività progetto che rinomiamo con app e la tabella progetto
[00:33:40] ovviamente e andiamo ad unire queste tabelle, quindi all'interno della slow air andremo
[00:33:49] ad unire tabelle che abbiamo appena scritto all'interno del form, quindi uniremo la
[00:33:56] tabella persona con l'attività progetto, l'attività progetto con il progetto, quindi
[00:34:02] scriviamo che l'identificativo della persona deve essere esattamente quello che sta all'interno
[00:34:09] attività a progetto e poi scriviamo che il progetto di si da progetto è uguale all'identificativo
[00:34:21] del progetto. In questo modo abbiamo fatto una grande tabella con tutti i dati delle attività
[00:34:26] progetto. Andiamo ad eseguirla, andiamo ad eseguirla e vediamo che ci sono tutte le
[00:34:39] attività progetto e in più oltreti da progetto ci sono i dati delle persone e dei
[00:34:46] progetti, che altrimenti non sarebbero presenti all'interno della tabella
[00:34:52] attività progetto e una volta fatto questo possiamo andare a filtrare
[00:34:57] queste annuble con un ulteriore end per vedere quali di questi progetti hanno un
[00:35:09] budget superiore alla media e quindi per fare questo dobbiamo dire che il
[00:35:15] il progetto, il budget del progetto, quindi nella colonna budget che vediamo essere presenti
[00:35:25] nella tabella progetto, quindi progetto punto budget deve essere maggiore della media di
[00:35:38] tutti i budget dei progetti, quindi come possiamo farlo questa cosa? Possiamo inserire una
[00:35:44] che è realizzata all'interno del Word dove andiamo a scrivere dentro delle parentesi
[00:35:53] tonde la clasola Select, quindi selezioniamo e la clasola From, andiamo a cavo per una
[00:36:07] maggiore ghiblità e all'interno della clasola From ovviamente andiamo ad inserire la tabella
[00:36:15] progetto e dobbiamo dire dobbiamo fare ovviamente la media, con la funzione
[00:36:22] aggregata media, dei budget dei progetti. Questa quere annitata ci
[00:36:30] ristruirà la media dei budget di tutti i progetti, mentre la quere esterna ci
[00:36:37] che ci restituisce tutte le persone che hanno lavorato ai progetti in cui budget è maggiore
[00:36:48] della media. Andiamo a definire una target list e innanzitutto stampiamo. Vediamo che
[00:37:00] allora bianchi ha lavorato al progetto wine sharing che è un progetto con un budget
[00:37:09] superiore alla media, andiamo a vedere qual è la media
[00:37:18] di budget per capire, la media budget è 368.000 scusate quindi effettivamente
[00:37:30] il budget di one sharing a suo arrivole. Ora andiamo a inserire nella target list i dati
[00:37:40] delle persone perché c'è una chiesto quali sono le persone e quindi andiamo a inserire
[00:37:46] l'identificativo, andiamo a inserire il nome e andiamo a inserire il cognome della
[00:37:52] Se avessimo voluto, per esempio, supponiamo che avessimo, che volessimo ordinare questi
[00:38:06] risultati per ordine crescente, ci basterà aggiungere la class order by e in ordine
[00:38:16] crescente di cosa, di identificativo, quindi inseriamo identificativo.
[00:38:21] E seguiamo, ovviamente avendo solamente un risultato al termine dell'eseguzione della
[00:38:31] query, non è molto utile ma potrebbe tornare l'ultima, utili in altri casi.
[00:38:35] Passiamo quindi allo svolgumento dell'ultima query, della query numero 5, che ci chiede
[00:38:42] quali sono i progetti con un'ombaggia di inferiore alla media, ma con un numero
[00:38:45] un pressivo di ore dedicate all'attività di ricerca sopra la media.
[00:38:49] Andiamo ad eseguirla, andiamo innanzitutto a scrivere come sempre il tiro del terzo
[00:38:58] dentro in un commento e poi eseguiamola, proviamo ad eseguire l'esercizio e innanzitutto
[00:39:10] Dobbiamo vedere quali sono i progetti con un budget inferior alla media, quindi facciamolo a bella
[00:39:25] progetto. Di questo progetto andiamo a inserire una target list rinitificativo il nome del
[00:39:32] il progetto. E dopo che hanno dei progetti, i quali hanno un budget, minore, come abbiamo
[00:39:44] visto poco fa, nell'esercizio numero 4, minore della media, non farlo sempre con una warriani
[00:39:54] data all'interno del war, prendiamo la media, quindi in un sito prendiamo la bella
[00:40:05] progetto e facciamo una media dei bar. Qui stiamo vendendo i progetti con un
[00:40:15] bargetti in filo della media. Come abbiamo visto prima dovrebbero essere tutti
[00:40:20] tra le wine sharing, ok ci siamo. Adesso andiamo a vedere quali di questi
[00:40:29] progetti hanno dedicato una quantità di tempo in ore superiore della media per
[00:40:46] attività di ricerca e sviluppo. Per farlo andiamo a inserire in-end una
[00:40:55] unizione all'interno del web e diciamo che l'ID che abbiamo appena trovato dei progetti
[00:41:09] con budget minore della media deve essere presente in... andiamo a specificare dove
[00:41:24] deve essere presente il nostro ID. Deve essere presente ovviamente all'interno
[00:41:29] dei progetti che hanno effettuato un numero complessivo di ore dedicata attività di cerca
[00:41:37] sopra la media, quindi andiamo a calcolarlo selep e from e possiamo dire che prendiamo
[00:41:45] sicuramente la tabella attività al progetto e il tipo di questo attività al progetto
[00:41:54] dobbiamo considerare il ricerca sviluppo e andiamo a dire, innanzitutto ok, prendiamo l'identificativo
[00:42:13] del progetto perché dobbiamo vedere se l'identificativo, uno più identificativo che escono poi da
[00:42:22] questa parte, la quali sono presenti in questa parte di questo, quindi se ne soniamo
[00:42:27] l'attività progetto si chiama progetto, e adesso dobbiamo andare a considerare, dobbiamo
[00:42:40] andare a considerare questi progetti i quali hanno una somma delle ore durata di queste
[00:42:51] attività progetto magia e della media. Per fare la somma, ovviamente, avremo bisogno
[00:42:56] di una funzione aggregata, ma la cosa è che bisogna fare il bisogno di un identificativo
[00:43:02] quindi possiamo dovremmo utilizzare un SAM con delle ore della durata, sicuramente. Quindi
[00:43:13] dobbiamo fare una somma delle ore della durata. Questo potrebbe essere messo intorno di un
[00:43:16] having per filtrare sicuramente questi tipi di progetti, ma sappiamo che l'utilizzo
[00:43:24] delle funzioni aggregate richiede un raggruppamento, quindi raggruppiamo per l'identificativo del
[00:43:31] progetto, quindi andiamo a fare un group by progetto. In questa maniera raggruppiamo per
[00:43:43] il progetto e poi andiamo a calcare la somma dell'ora di durata di ogni progetto e andiamo
[00:43:50] dire che questa somma durata, cioè dobbiamo filtrare i progetti, la cui somma
[00:43:56] delle ore durata è maggiore della media delle somme di tutti i progetti,
[00:44:05] di tutte le attività di cerca. Quindi andiamo a scrivere un'altra quali
[00:44:12] anni data all'interno del Leving che ci raccolà la media delle ore
[00:44:18] dedicate all'attività di progetto, di tipo di cerca e sviluppo di tutti i progetti, quindi andiamo a scrivere SELECT e FROM.
[00:44:34] Adesso da un momento che all'interno del FROM abbiamo bisogno di fare prima di tutto una somma delle ore durata,
[00:44:44] dell'attività progetto, raggruppata per progetto, e adesso vediamo il perché,
[00:44:49] e poi dobbiamo fare una meta e tutte queste somme, all'interno del from andremo a definire
[00:44:54] un'altra query anidata sua volta e possiamo scrivere questa query in questo modo nella
[00:45:06] target list, la vediamo dopo, andiamo a scrivere il from e diciamo che è l'attività
[00:45:15] l'attività progetto, prendiamo la tabella attività progetto dove la tipologia è uguale
[00:45:29] a ricerca e sviluppo, quindi l'attività progetto di ricerca e sviluppo, le raggruppiamo per
[00:45:41] ogni progetto come abbiamo fatto prima, proprio per chi le andiamo a raggruppare.
[00:45:47] perché noi vogliamo sapere le somme per ogni progetto di attività di ricerche
[00:45:54] sviluppo, quindi andiamo a usare la funzione reala SAM, pure, durata e la
[00:46:01] rinominiamo con, non so, somma, pure. Quindi adesso abbiamo preso,
[00:46:09] ricapitolando, abbiamo preso i progetti con baggiato minore della media,
[00:46:14] Stiamo cercando tra questi progetti quelli che hanno dedicato un ammontare di
[00:46:24] ore all'attività di progetto di tipo ricerca e sviluppo maggiore della media.
[00:46:29] Per fare questo dobbiamo calcolare la somma di tutte le ore dedicate per
[00:46:37] l'attività di ricerca e sviluppo di tutti i progetti, fare la media di
[00:46:42] queste ore per avere una media generale e andare a confontarla con la somma che abbiamo
[00:46:51] ricavato qui.
[00:46:52] Quindi nel select esterno di questa query possiamo illuminarla questa tabella che abbiamo
[00:47:04] inserito all'interno del from come una query anidata e la chiamiamo as mediaore e all'interno
[00:47:15] di questo select quindi andiamo a prendere la media di sommaore quindi abbiamo raggruppato
[00:47:21] per progetti fatto la somma del ore delle ritorate e adesso andiamo a fare la media di
[00:47:25] tutti i progetti per ritoriare quindi andiamo a utilizzare la funzione aggregata average
[00:47:31] e vediamo che solamente Pegasus ha un baggetto inferiore della media e un numero di ore
[00:47:49] dedicate all'attività di ricerca superiore alla media, nel caso in cui volessimo restituire
[00:47:56] oggetti ordinati per i di crescente, ovviamente basterà inserire alla fine della
[00:48:03] query la clasone order by, come aveva fatto prima, rimane peccato, peccato al
[00:48:16] momento che abbiamo solamente un ennobla all'interno di questa query. Una volta
[00:48:22] svolta la query però possiamo notare una cosa,
[00:48:25] noi sappiamo che la clasula herring non è, non sempre è ottimizzata e
[00:48:32] in realtà molte volte non è proprio ottimizzata perché viene eseguita in fase di output su
[00:48:38] ogni gruppo quindi è veramente molto molto pesante e molto onerosa e però possiamo osservare
[00:48:45] che fortunatamente le quei interni che abbiamo sono tutte quei che sono non sono correlate
[00:48:54] quindi cosa possiamo fare? Possiamo cercare di allergire il calcolo utilizzando delle
[00:49:04] quere annitate delle tabele temporaneo utilizzando la clausola WIT per calcolare le statistiche
[00:49:12] come abbiamo fatto nell'esercitazione precedente in academia 7 quindi per fare ciò possiamo
[00:49:22] proviamo a rifare la query e vediamo che dal momento che molti di queste di queste
[00:49:31] query istituiscono solamente pochi, poche ennue per esempio questa restituzione la
[00:49:38] media questa insomma anche anche questa restituzione la strumento la media
[00:49:43] possiamo andare ad ottimizzarla attraverso la grado sulla will, adesso
[00:49:48] proviamo a rifare l'esercizio 5 in maniera ottimizzata, quindi procediamo con vedere la
[00:49:55] versione ottimizzata per la query 5 e cancelliamo quello che abbiamo fatto e proviamo a rifarlo
[00:50:02] con i width. Allora anzi e tutto possiamo creare una tabella temporale, lo dobbiamo
[00:50:09] solamente inserire come abbiamo detto, da un momento ci siamo accorti che possiamo
[00:50:12] ottimizzarla, andiamo ad inserire da quella sola width e andiamo a calcularci il
[00:50:17] il budget media per i progetti, quindi facciamo una tabella budget media e andiamo a scrivere
[00:50:28] select and from nella tabella progetto facciamo una vg di budget e non so che la rinominiamo
[00:50:42] la colonna con valore e la ridondiamo in questo modo. Successivamente creiamo una tabla temporalea
[00:50:52] per andare a capire il totale di ore di ricerca spese in ogni progetto quindi la chiamiamo
[00:51:00] e andiamo a definirla quelli utilizziamo sicuramente andremo a considerare la tabella progetto e cosa
[00:51:24] possiamo fare in questo caso ma in questo caso possiamo andare a utilizzare un left
[00:51:32] Left Outer Join ci permette di fare un join nel quale il dbms va ad esaminare le righe
[00:51:48] della tabella di sinistra, in questo caso non abbiamo progetto, con quelle della tabella
[00:51:53] di destra noi andremo ad inserire sicuramente la tabella attività a progetto, facciamo
[00:51:59] anzi. Cosa farà? Ma questo letto del giorno manterrà le riche della tabella di sinistra.
[00:52:21] Va a vedere se queste riche hanno una corrispondenza con le riche di destra. Se la corrispondenza
[00:52:26] esiste, crea un n nubla all'interno della tabella. Se c'è più di una corrispondenza,
[00:52:33] crea più n nuble. Dal momento in cui la corrispondenza non esiste, comunque crea
[00:52:39] una nubla, ma inserirà il valore null dove nelle colonne corrispondenti in cui non c'è
[00:52:46] appunto la corrispondenza, quindi nelle colonne di attività a progetto in questo caso, perché
[00:52:50] mantiene sempre le colonne di progetto. E il letto del join poi ci richiede l'utilizzo
[00:52:59] dell'on per andare a capire dove andare a fare il join, quindi noi diremo che il progetto
[00:53:05] di attività al progetto deve essere uguale al progetto.d e andiamo a dire che la tipologia
[00:53:21] dell'attività di progetto da considerare in questo letto del join è il ricerca e sviluppo.
[00:53:36] Ok, in questo caso i progetti che hanno delle attività del progetto e il ricerca e sviluppo
[00:53:41] avranno una corrispondenza in un attività progetto, altrimenti no, e andiamo a prendere
[00:53:51] anzienti nella target list l'identificativo del progetto, poi possiamo inserire quello
[00:53:57] di mio progetto, poi andiamo ad inserire, dobbiamo fare una somma, facciamo la somma
[00:54:05] delle ore della turata per ogni progetto, perché qui dobbiamo vedere le ore di ricerca
[00:54:10] fatti da tutti i progetti quindi facciamo Sam di attività progetto punto
[00:54:19] ore dura ok e noi andiamo questo campo con valore
[00:54:31] ovviamente dal momento che abbiamo utilizzato la funzione aggregata
[00:54:35] dobbiamo raggruppare, quindi group by e raggruppiamo per id del progetto perché è il valore che
[00:54:43] sta all'attacchietlist, quindi pr.id. Cosa succede però? Dal momento che con il
[00:54:54] left-over join potremmo avere, non avere corrispondenti in attività progetto e la funzione
[00:55:03] Sam potrebbe non avere nulla da sommare e come possiamo fare in questo caso? Possiamo utilizzare
[00:55:12] la funzione co-qualesce e questa funzione cosa fa? Permette di valutare i parametri che
[00:55:32] inseriamo al suo interno e di andare a prendere il primo parametro non null all'interno
[00:55:43] della colonna che è passata, nella colonna che abbiamo inserito. Il risultato di questa
[00:55:52] funzione null se è solo se tutti i i valori della colonna sono null e possiamo anche andare
[00:56:07] a mettere un numero di default da restituire dal momento in cui tutti sono null e noi
[00:56:14] inseriamo zero. Quindi adesso abbiamo la, ricapitolando, abbiamo la tabella per il
[00:56:22] budget medio, la tabella a temporare per il budget medio, abbiamo la tabella che ci
[00:56:25] dice quante ore hanno dedicato ogni progetto a attività di ricerca e
[00:56:34] sviluppo, andiamo a farci la tabella che
[00:56:43] che calcola la media delle ore di ricerca di ogni progetto, quindi la tabela riameremo
[00:56:53] media, ore, ricerca, e andiamo a, andiamo su un po' di spazio, e andiamo a anziere
[00:57:08] quelli, quindi dobbiamo andare a prendere la tabella che abbiamo appena creato, qui
[00:57:18] che abbiamo calcolato ogni progetto quanto tempo è investito in attività di cerche di
[00:57:23] sviluppo e andiamo a fare la media per questo tempo calcolato, abbiamo prima calcolato, abbiamo
[00:57:36] fatto la somma di tutte le attività e poi abbiamo fatto la media, quindi valore che abbiamo
[00:57:42] chiamato valore la colonna e ora andiamo a scrivere la vari più esterna che quindi prenderà
[00:57:54] solamente e andrà a sezionare andrà andremo a filtrare solamente i progetti con un budget
[00:58:00] medio inferore a quello indicato dalla tabella budget tabella temporale budget medio e con
[00:58:08] un tutorial di ore investite in attività di ricerca maggiore della media, quindi scriviamo
[00:58:16] l'acqua esterna e andiamo ad inserire la tabella progetto, diciamo sicuramente bisogno
[00:58:27] la tabella pargetmedio che abbiamo calcolato e andiamo a prendere in considerazione la
[00:58:44] tabella totale ore di ricerca perché dobbiamo vedere quali sono i progetti che hanno fatto
[00:58:51] e poi prendiamo anche la media ovviamente di questa ricerca quindi medie, ore, quindi andiamo a prendere questa labbella qui
[00:59:15] e la nominiamo ok andiamo a fare un gioco di queste way
[00:59:25] all'interno del way andremo a definire i giovani quindi facciamo il budget
[00:59:31] e il budget lo vediamo da ogni facciamo totale
[00:59:37] l'ore ricerca deve essere, prendiamo il progetto di questo tutorial del progetto, deve essere
[00:59:47] esattamente progetto.di, poi facciamo, dobbiamo dire che il valore in totale ori ricerca
[01:00:03] Quello che abbiamo raccolato è la somma delle ore dedicata alle ricerche di piluppo.
[01:00:12] Il totale delle ore, quindi totale ore di ricerca, appunto abbiamo chiamato valore, deve essere
[01:00:21] maggiore del valore indicato dalla tabella media ore ricerca, quindi media ore ricerca
[01:00:34] se non lo avevamo chiamato così anche quella ok anche quella quella colonna e poi cosa ci
[01:00:45] manca ah sì tu puoi ovviamente andare a dire che il budget del progetto progetto punto
[01:00:53] budget deve essere minore del di quello indicato dalla tabella budget media quindi budget
[01:01:06] punto valore. Arrivedo a questo punto abbiamo, abbiamo detto che la tabella
[01:01:14] progetto, nella tabella progetto è il budget considerato dell'assee minore del
[01:01:19] budget medio. Abbiamo unito il progetto, la tabella progetto con la tabella
[01:01:27] da le ore di ricerca e abbiamo detto che il budget, la somma delle ore per l'attività
[01:01:40] di ricerca deve essere maggiore della media. Andiamo adesso a ensinere la target list l'identificativo
[01:01:50] di questi progetti e il nome. Perfetto. Abbiamo appunto lo stesso risultato della
[01:02:00] guerra precedente. Abbiamo fatto la stessa cosa, ma utilizzando questi
[01:02:06] weed, quindi graando queste tabelle temporanea, abbiamo ottimizzato di
[01:02:10] molto la guerra, perché i prodotti di tabelle con una sola elnubla è a costo
[01:02:15] zero, quindi abbiamo il prodotto con questa tabella e questa tabella a costo
[01:02:18] 0 ed è sicuramente molto più ottimizzato dell'eving andiamo anche anche qui come
[01:02:26] ho fatto prima andiamo a ordinare per il progetto per l'identificativo del
[01:02:31] progetto anche se appunto non è molto utile per questo caso specifico ma
[01:02:36] potrebbe essere solo per altri quindi andiamo a farlo
[01:02:40] il progetto e quindi anche la 45 è finita e abbiamo visto anche una
[01:02:52] versione ottimizzata, una soluzione ottimizzata, dirà 45.
