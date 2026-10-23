# Trascrizione: E.B.2.2.3.2.6.1 - Accademia 7 - BD2

[00:00:01] Alve a tutti, benvenuti nella video-esercitazione HM7 che sarà in centrarla sui esercizi con
[00:00:08] quei annitate nella clausola from.
[00:00:11] Dunque iniziamo il primo esercizio che ci richiede di determinare quale sia la media
[00:00:15] e la deviazione standard degli stipendi per ogni categore di strutturati.
[00:00:19] Iniziamo questo esercizio partendo dal nostro template vuoto e specificando nella
[00:00:24] clausola from la tabella persona dalla quale vogliamo per la punto recuperare le informazioni
[00:00:39] sullo stipendio. Adesso eseguiamo una partizione su tale tabella raggruppando le ennuble in
[00:00:49] base alla loro posizione. Per fare ciò dunque utilizzeremo il costrutto group by specificando
[00:00:56] per la colonna posizione. Adesso l'esercizio ci richiede di associare ad
[00:01:04] ognuno dei gruppi intracciati lo stipendo medio e la relativa standard deviation su
[00:01:11] lo stipendio. Per fareciò adunque faremo utilizzo della documentazione per
[00:01:16] ritrovare per appunto le funzioni che ci servono.
[00:01:19] Quindi andiamo nel nostro modo di ricirche e cerchiamo Aggregate Function SQL.
[00:01:29] Guardate, cerchiamo Postgres.
[00:01:31] Una volta arrivati appunto nella pagina della documentazione verifichiamo che la versione
[00:01:40] supportata in tale pagina sia la stessa che abbiamo per l'appunto nel nostro dbms,
[00:01:48] nel nostro caso quindi il nostro dbms supporta e ha la versione di Postgres SQL 16, quindi
[00:01:55] di conseguenza possiamo procedere e possiamo per l'appunto ispezionare
[00:02:00] le pagine e ritrovare una la funzione apg che per l'appunto ci restituisce Mondia
[00:02:07] e scorrendo troveremo anche la funzione st deb che per l'appunto ci dà la standard
[00:02:15] division quindi adesso ritorniamo al nostro esercizio e per l'appunto utilizziamo
[00:02:23] tali funzioni all'interno della nostra target list dunque la target list sappiamo
[00:02:28] che sicuramente dovrà avere la colonna posizione poiché l'abbiamo specificata
[00:02:32] all'interno del costrutto group by poi andremo utilizzare per l'appunto
[00:02:38] l'aggregate function che citerà la media sugli stipendi quindi AVG stipendio e
[00:02:48] infine andremo per l'appunto a utilizzare l'aggregate function per
[00:02:54] la standard deviation, ovvero ST, sempre sullo stipendio e lo andiamo per la
[00:03:05] punta a rinominare come standard deviation in DEV. E seguendo la
[00:03:14] quaria allo stato attuale possiamo per la punta ritrovare il risultato
[00:03:18] desiderato. Il secondo esercizio ci richiede di determinare quali siano i
[00:03:26] ricercatori, per la punta determinano tutti i attributi con uno stipendio
[00:03:32] superiore alla media della loro categoria dunque per risolvere tale esercizio faremo
[00:03:39] ricorso ad una query anidata all'interno della clausola from dunque l'obiettivo è
[00:03:46] andare ad utilizzare nella clausola from una tabella derivata da una query che
[00:03:53] determini la media degli strippendi dei ricercatori quindi iniziamo da
[00:03:58] nostro template vuoto e per l'appunto andiamo a specificare l'interno della
[00:04:09] clausola from tale querianidata che sarà per l'appunto un select, determiniamo per
[00:04:22] l'appunto la media sullo stipendio quindi e vg stipendio, selectiamo poi la
[00:04:33] tabella persona dalla quale recuperare tali informazioni e imponiamo che per
[00:04:46] per l'appunto la posizione di ogni nupola sia per l'appunto la posizione di quel ricercatore,
[00:04:52] quindi where posizione uguale di ricercatore, rinominiamo dunque questa query anitata nella
[00:05:06] nostra clausola from come med. Adesso aggiungiamo alla nostra clausola from la tabella persona
[00:05:16] da cui recupereremo per l'appunto i dati di tutti i ricercatori, quindi scriviamo persona
[00:05:22] Rick. Una volta terminata comunque la nostra clausola from, avremo bisogno di impostare
[00:05:32] all'interno della clausola where due condizioni, innanzitutto che per l'appunto la persona
[00:05:38] un ricercatore e la seconda condizione è che per l'appunto lo stipendio sia per l'appunto
[00:05:58] maggiore rispetto alla media di tutti i ricercatori che andremo ad ottenere proprio grazie alla
[00:06:05] nostra query ammitata, anidata med, quindi avremo med.step poiché per l'appunto tale
[00:06:12] query utilizzerà come funziona aggregata la media sullo stipendio di tutti i ricercatori.
[00:06:17] Dunque andiamo adesso ad eseguire la query allo stato attuale, dovremmo ovviamente scrivere
[00:06:27] all'interno della nostra target list gli attributi che vogliamo per l'appunto ottenere, quindi
[00:06:33] in questo caso perché vogliamo tutti gli attributi dei ricercatori, andremo a specificarlo
[00:06:41] all'interno della nostra target list e così facendo per l'appunto otterremo il risultato
[00:06:46] esiderato. L'esercizio numero 3 ci richiede di determinare per ogni categoria di strutturati
[00:06:56] quanti siano le persone con uno stipendio che differisce monthly che differisceavesce
[00:06:59] di al massimo una deviazione standard dalla media.
[00:07:02] La strategia ad otteremo per risolvere l'esercizio ad definire una coerianità alla qualificazione di
[00:07:10] clausola from in cui associiamo ad ogni posizione la media e la standard deviation
[00:07:20] dello stipendio. Dunque utilizzeremo poi tali tali dati per impostare una
[00:07:28] condizione nella clausola where che per l'appunto utilizza i tale statistiche
[00:07:33] aggregate. Dunque partiamo ad allo scrivere innanzi tutto la prima query
[00:07:37] quindi partiamo, schiumiamo il nostro template classico e specifichiamo all'interno della
[00:07:48] clausola from la tabella persona. Raggruppiamo poi, diciamo, ogni tipologia di strutturato
[00:08:00] per la propria posizione e infine associiamo ad ogni posizione per l'appunto la media dello
[00:08:15] stipendio e ovviamente la standard deviation se lo stipendio quindi. Adesso andiamo a
[00:08:44] rinominare tale query come query stats andando per l'appunto ad utilizzare il
[00:08:51] costrutto wit quindi scriviamo per l'appunto wit eseguiamo scusate eseguiamo
[00:08:59] prima la query per per l'appunto vedere l'output su tale query e per l'appunto
[00:09:03] possiamo vedere che per ogni tipologia di posizione avremo la statistica aggregata
[00:09:09] dalla media sullo stipendio e la statistica aggregata sulla standard deviation
[00:09:13] quindi andiamo adesso ad utilizzare dalle query all'interno del
[00:09:19] costruto wit, specificando per l'appunto il nome stats, has e inseriamo per
[00:09:27] l'appunto la nostra query. Adesso possiamo andare ad utilizzare questa
[00:09:32] query in un'altra query che sarà per l'appunto la query finale quindi partiamo
[00:09:37] nuovamente dal template vuoto e specificiamo all'interno della
[00:09:45] clausola from del nostro template vuoto per l'appunto la tabella stats che abbiamo
[00:09:50] appena introdotto e la tabella persona adesso passiamo per l'appunto alla
[00:10:03] nostra alla nostra clausola where nella quale imposteremo innanzitutto il
[00:10:08] join tra le due tabelle quindi che p punto posizione sia uguale a stats punto posizione.
[00:10:18] Adesso possiamo per la punto andare ad utilizzare le informazioni aggregate che avremo all'interno
[00:10:33] da bella stats per poter per la punto determinare che lo stipendio sia per la punto che lo
[00:10:43] stipendio sia di al massimo una deviazione standard rispetto alla media della categoria,
[00:10:47] quindi per fare per fare ciò andremo per la punto a scrivere che p punto stipendio sia per
[00:10:57] la punto compreso quindi utilizzeremo betwing e avremo poi la differenza tra stats punto media
[00:11:09] meno stat punto la standard deviation ovviamente e quindi compreso tra questo valore e la somma
[00:11:27] tra queste due informazioni quindi avremo che stats punto media più stats punto la standard
[00:11:42] Adesso andiamo a raggruppare ognuno delle ennuble all'interno del nostro output per posizione per
[00:11:54] poter poi eseguire il conteggio di tale ennuble quindi eseguiremo utilizzeremo il costruito
[00:11:59] groupby p.posizione. Infine andiamo a costruire la nostra target list all'interno
[00:12:12] da quale per l'appunto dobbiamo necessariamente utilizzare ovviamente la colonna posizione
[00:12:16] lo che è utilizzata all'interno del nostro costrutto crubai e infine il count di
[00:12:27] tutta l'anuple, quindi count star, che definiamo as numero.
[00:12:32] Adesso andiamo ad eseguire la query e per l'appunto otteniamo il risultato
[00:12:41] desiderato. L'esercizio numero quattro ci richiede di rintracciare gli strutturati che hanno
[00:12:52] lavorato almeno 20 ore complessive in attività progettuali. Quindi iniziamo l'esercizio
[00:13:00] scrivendo il nostro template vuoto e specificando all'interno della clausola from la tabella
[00:13:06] persona e la tabella attività progetto che saranno per l'appunto le tabelle che
[00:13:21] andremo ad utilizzare per determinare per l'appunto gli strutturati che è l'ora di lavoro all'interno
[00:13:30] di attività progettuali. Adesso andiamo a impostare per l'appunto il join tra le
[00:13:39] due tabelle scrivendo che ap.persona sia uguale a la persona.d. Adesso andiamo a raggruppare
[00:13:54] le ennuble che avremo in tale risultato per ogni singola persona. E poiché vogliamo
[00:14:05] ristituire di ogni persona l'ID il nome, il cognome, la posizione e lo stipendio dovremmo
[00:14:11] andare ad inserire all'interno del costrutto group by tutte queste informazioni che poi
[00:14:17] vorremmo inserire all'interno della target list, quindi avremo p.id, p.nome, p.connome,
[00:14:29] p.posizione e lo stipendio. Dunque andiamo a specificare all'interno
[00:14:42] della target list tutte queste informazioni che abbiamo per l'appunto utilizzato per
[00:14:46] da gruppamento e contestualmente vogliamo all'associare ad ogni una delle persone il numero
[00:14:56] di ore cumulative che sono per l'appunto state state eseguite in attività progettuali quindi per
[00:15:03] fare ciò utilizziamo la funzione aggregata Sam che prende come utilizza come parametro il numero
[00:15:11] per l'appunto delle ore eseguite, quindi ap, quindi ore durata, s, ore lavorate. Se eseguiamo
[00:15:27] per l'appunto la query allo stato attuale possiamo vedere che per ogni singola persona
[00:15:32] avremmo il numero accumulativo di ore lavorate. Adesso per risolvere finalmente l'esercizio
[00:15:38] avremo bisogno di imporre una condizione sulla funzione aggregata che non possiamo
[00:15:44] andare a inserire all'interno della nostra glasola wear, infatti si è scrivessimo in
[00:15:47] questo caso che la SAM sia per l'appunto maggiore uguale di 20, otterremo per l'appunto
[00:15:58] un errore in quanto tale condizione non può essere esplicitata all'interno della glasola
[00:16:03] wear, quindi sposteremo all'interno di tale condizione, all'interno di un costrutto
[00:16:10] dedicato a specificare delle condizioni utilizzando delle funzioni aggregate,
[00:16:15] che in questo caso sarà per l'appunto il costrutto eiving. Specificiamo la nostra condizione e
[00:16:21] infine andiamo ad eseguire la query e possiamo vedere per l'appunto che otterremo delle
[00:16:28] ennuple in cui la somma delle ore lavorate sia maggiore o uguale di 20, quindi in questo caso
[00:16:36] prima Anna Bianchi che ha ore lavorate solamente 38. Procediamo con la query numero 5 che ci
[00:16:46] chiede quali sono i progetti la cui durata è superiore alla media delle durate di tutti
[00:16:51] i progetti restituire il nome dei progetti e la loro durata in giorni. Ok scriviamoci
[00:16:58] e andiamo a svolgerla. Prima di tutto vediamo qual è la media della turata di tutti i progetti
[00:17:20] e per farlo andiamo ad inserire la struttura, prendiamo la tabella progetto e andremo a
[00:17:30] fare attraverso la funzione aggregata AVG la media per capire qual è appunto la
[00:17:44] meta di durata dei giorni dei progetti. Sappiamo che all'interno della bella
[00:17:50] progetto abbiamo, andiamo ad eseguire la query, abbiamo la tala di inizio, la tala di fine e quindi per
[00:17:56] per prendere la durata media in giorni possiamo fare avvg fine, quindi andiamo a prendere
[00:18:07] la data di fine e la data di fine sottraiamo la data di inizio così che vediamo quanto
[00:18:12] è durato il progetto e se abbiamo visto quelli e vediamo che questo è il dato della
[00:18:20] la durata media dei progetti. Andiamo a rinominarle questa colonna. Le nominiamo con es, durata media, giorni.
[00:18:35] Ok, questa tabella andremo ad utilizzarla all'interno di un'altra query, perché cosa
[00:18:46] dobbiamo vedere adesso quali sono i progetti che hanno durato a superiore a questa media
[00:18:52] quindi andiamo ad inserire questa tabella all'interno del costruttowheat e il costruttowheat ci
[00:19:04] richiede che venga dato un uomo a questa tabella e la chiamiamo stats, inseriamo la
[00:19:15] tabella all'interno dell'Wheat. Adesso possiamo utilizzare il dado fornito
[00:19:28] scelto a questa tabella all'interno, utilizzando, scusate, all'interno
[00:19:33] dell'Wheat utilizzando il nome STAZZ e quindi Wheat ci permette di creare delle
[00:19:42] tabelle temporanei che poi possiamo utilizzare all'interno delle nostre
[00:19:46] query. Andiamo quindi a scrivere il resto della query. In quest'altra parte
[00:19:55] dobbiamo vedere quali sono i progetti che hanno una durata superiore alla media,
[00:20:03] quindi sicuramente prenderemo in considerazione anche qui la tabella
[00:20:06] progetto. Andiamo a stampare e prendiamo in considerazione anche la
[00:20:13] nella target list mettiamo ciò che ci viene richiesto quindi dobbiamo restituire il nome
[00:20:21] dei progetti e la loro durata in giorni quindi mettiamo un alias con il progetto proj mettiamo proj e
[00:20:34] stampiamo il nome poi stampiamo la durata in giorni del progetto quindi proj e come abbiamo
[00:20:42] abbiamo già fatto solo, facciamo il punto sirio, meno il punto inizio e diamo, rinominiamo
[00:20:54] questa tabella, questa colonna, scusate, è durata, ok, quindi adesso abbiamo il nome
[00:21:05] del progetto in natura da ingiorni del progetto, dobbiamo andare a prendere solamente i progetti
[00:21:14] che hanno la durata in giorni maggiore della durata media di tutti i progetti, quindi inseriamo
[00:21:20] la clause da where e dobbiamo dire all'interno della clause dobbiamo scrivere che la durata
[00:21:27] del progetto, quindi facciamo sempre la subtractione tra i fine e inizio progetto,
[00:21:32] per il punto fine meno però il punto inizio, deve essere maggiore della durata media
[00:21:41] che c'è data dalla tabella stats, e andiamo a prendere durata media più, eseguiamo la
[00:21:53] query e possiamo vedere che one sharing insima hanno una durata in giorni maggiore della
[00:22:05] media. Andiamo avanti con l'esercizio numero 6, copriamo prima di tutto il testo e poi
[00:22:13] andiamo a leggere. L'esercizio numero 6 dice quali sono i progetti terminati in
[00:22:23] data di Erna che hanno avuto attività di tipo di mostrazione, restituire il nome
[00:22:27] di ogni progetto e il numero complessivo delle ore dedicate a tale attività nel
[00:22:32] progetto. Allora, per fare ciò innanzitutto possiamo iniziare andando a
[00:22:38] a vedere quali sono i i progetti finiti andiamo a prendere la tabella progetto e
[00:22:49] vediamo quali sono i progetti terminati quindi prendiamo l'identificativo e
[00:22:57] andiamo a prendere il nome dei progetti terminati quindi all'interno della
[00:23:02] lausola web scriviamo che la data di fine del progetto deve essere minore della
[00:23:11] data corrente usiamo il current date eseguiamo questa query e vediamo che questi sono i progetti
[00:23:20] terminati adesso andiamo a vedere quali dei progetti terminati hanno attività di tipo
[00:23:28] dimostrazione quindi facciamo il join con attività progetto api e all'interno del
[00:23:38] quindi andiamo a mettere le condizioni necessari per il join, quindi andiamo a dire che app.progetto deve
[00:23:47] essere uguale app.progetto.id e poi dobbiamo dire che il tipo dell'attività al progetto, quindi app.tipo,
[00:24:00] di essere esattamente dimostrazione.
[00:24:21] Vediamo che Pegasus ha due attività a progetto.
[00:24:25] Per curiosità andiamo a dizzerire nella target list
[00:24:29] la durata di quest'attività a progetto.
[00:24:33] Sappiamo che l'attività a progetto ha la colonna
[00:24:37] o re-durata.
[00:24:41] facciamo app.ore-durata ed eseguiamo e vediamo che la prima attività
[00:24:51] progetto di Pegasus ha dura 8 ore e la seconda 7 ore quindi in totale Pegasus a
[00:24:58] 15 ore di attività al progetto dedicata alla dimostrazione. Andiamo ad
[00:25:03] effettuare effettivamente questo calcolo utilizzando la funzione
[00:25:06] aggregata SAM, che permette di fare la somma di tutti i valori all'interno di una colonna,
[00:25:16] rinominiamo la colonna della somma con orezione e andiamo a raggruppare il tutto per l'identificativo
[00:25:28] del progetto, usiamo il GRUB-I e all'interno di GRUB-I ci scriviamo. Quindi adesso sappiamo
[00:25:43] che Pegasus ha un totale di ore di dimostrazione uguale a 15.
[00:25:48] Passiamo ora alla quale finale, la quale numero 7 che ci chiede quali sono i professori
[00:25:55] ordinari che hanno fatto più assenze per malattia, del numero di assenze meglio
[00:26:02] per la mattia dei professori associati, restituire l'identificativo, il nome e il cognome del
[00:26:08] professore, si riuscire per il suo ordinario, e il numero di giorni di essenza per la mattia.
[00:26:13] Quindi andiamo a copiarci il titolo, innanzitutto, all'interno della nostra quera e cancelliamo
[00:26:29] la quali precedenti. Per svolgere questo esercito ci andremo a frammentarlo in più
[00:26:36] parti perché prima di tutto dobbiamo andare a calcare il numero di giorni di assenza per
[00:26:40] malattia del professore associato, quindi di tutti i professori associati. Poi dobbiamo
[00:26:45] calcare la media dei giorni di malattia per i professori associati e successivamente
[00:26:50] calcoliamo il numero di giorni di assenza per malattia dei professori ordinari. Infine
[00:26:59] ovviamente mettiamo a confronto i giorni di malattia dei professori ordinati con
[00:27:05] la media dei professori associati quindi per fare ciò cominciamo a calcolare il numero
[00:27:11] regioni di assenza della malattia per i professori associati per farlo andiamo a scrivere
[00:27:18] select e from all'interno del from scriviamo personi e andiamo a fare join con la tabella
[00:27:31] assenza, facciamo che l'identificativo della persona deve essere uguale alla persona nella
[00:27:45] da bella assenza e dobbiamo andare a prendere, quindi calcolare, scusatemi, i giorni di
[00:27:53] assenza per malattia, quindi andiamo a dire che la tipologia di assenza, quindi appunto
[00:28:03] tipo deve essere esattamente malattia e poi andiamo a dire che la persona deve essere
[00:28:12] un professore associato quindi p punto posizione è uguale a professore associato di, andiamo
[00:28:32] a vedere l'eseguizio della query. Ok, quindi c'è Andrea Verona che ha fatto delle ore di
[00:28:41] malattia. Ora, il giorno il 12.7. Quindi andiamo adesso a vedere, anzi, una target list.
[00:28:56] Innanzi tutto non abbiamo bisogno che tutti questi dati per i professori associati. Quindi
[00:29:03] chiediamo una target list che vogliamo solamente l'identificativo e vogliamo mantenere, vogliamo
[00:29:11] sapere quanti giorni di malattia hanno fatto, quindi facciamo il count, usiamo un apretato
[00:29:17] e andiamo a dire conta tutte le assenze e noi nomiamo come non giorni e raggruppa per persona
[00:29:40] conto identificativo. In questo modo andiamo a raggruppare per identificativo poiché c'è
[00:29:48] l'identificativo nella target list e contiamo il numero di giorni di assenza
[00:29:56] eseguiamo la query e vediamo infatti che la persona 7 quindi un identificativo 7 ha
[00:30:04] fatto un giorno di assenza ok questa prima da breve la temporanea con il
[00:30:10] costruito wheat andiamo a rinominarla come giorni ma la tia pia sta per professore
[00:30:19] associato e in questo modo possiamo utilizzarla nelle quelli che che verranno
[00:30:32] andiamo ad intentarla con una maggior gibilità ok abbiamo bisogno di di un
[00:30:40] di un'altra qualità, possiamo farla, ovviamente, inserendo una virgola e andando a definire
[00:30:50] un altro nome per la nuova tabella. Adesso andiamo a calcolare la media dei giorni di
[00:30:56] malattia per i professori associati, quindi possiamo chiamarla come abbiamo fatto per
[00:31:01] la quali precedente staz e andiamo a chiamarla staz PIA quindi le statistiche dei professori
[00:31:08] associati e facciamo sì che questa tabella quindi abbia al su interno il valore medio
[00:31:17] del numero di assenze per malattie dei professori associati quindi scriviamo select from e abbiamo
[00:31:26] già le assenze per malattie dei professori associati qui, quindi andiamo a prendere proprio
[00:31:33] questa tabella, quindi prendiamo la tabella giorni malattie PA e andiamo a dire che vogliamo
[00:31:43] media della colonna numJourney e la rinominiamo come numJourneyMedium. In questo caso abbiamo
[00:31:58] il numero di giorni medio di malattia per i professori associati. Cosa ci rimane ad
[00:32:05] fare adesso? Ci rimane ad calcolare il giorno di malattia per i professori ordinari e
[00:32:10] e poi andare a vedere quali professori ordinari hanno fatto più giorni di malattia rispetto
[00:32:16] alla media dei professori associati. Quindi facciamo un'altra tabela temporanea con i
[00:32:22] giorni di malattia per i professori ordinari. Quindi questa tabela andrà a chiamarla giorni
[00:32:32] tia professori ordinari e all'interno di questa tabella ovviamente andiamo a calcolare
[00:32:45] una cosa molto simile a quella che abbiamo raccolto per i professori associati, quindi
[00:32:52] inseriamo nel from persona p e assenza a e andremo a fare il join tra persona e assenza
[00:33:03] e lo facciamo nella class lower, quindi andiamo a dire come abbiamo fatto per i professori
[00:33:11] andiamo a dire che l'id della persona deve essere esattamente la persona all'interno della tabella
[00:33:24] assenza, quindi assenza.oper. Poi dobbiamo andare a dire che uniamo queste due tabelle con una
[00:33:36] volta unite queste due tabelle andiamo a dire che il tipo definiamo che il tipo di assenza deve
[00:33:45] esattamente malattia anche per i professori ordinari e definiamo appunto
[00:33:51] differentemente da questa quali qui che da questa tabela temporanea
[00:34:00] qui definiamo che la posizione della persona deve essere esattamente
[00:34:10] professore ordinario ok però diversamente da come abbiamo fatto per i professori
[00:34:23] associati che prendavamo solamente l'identificativo poiché la query ci
[00:34:27] richiede di restituire i dati per i professori ordinari qui andiamo infatti
[00:34:34] anche per i professori associati raggruppiamo solamente per i di qui andiamo
[00:34:38] sicuramente a prenderli identificativo ma insieme a identificativo prendiamo
[00:34:42] anche il nome, il cognome, e andiamo a contare il numero di assenze per giorni di malattia
[00:34:55] per questi professori, quindi facciamo il count che abbiamo fatto precedentemente,
[00:35:03] noi nominiamo un nome diverso quindi non so, non...
[00:35:07] giorni...
[00:35:08] no, la... tia...
[00:35:11] e...
[00:35:13] andiamo a reagruppare
[00:35:16] per...
[00:35:18] per i dati inseriti dall'interno della target list, quindi utilizziamo group by
[00:35:26] per...
[00:35:27] identificativo della persona, il nome e il cognom.
[00:35:31] Ok, arrivati a questo punto, quindi abbiamo
[00:35:33] la tabella che ci carcola i giorni di malattia per i professori associati
[00:35:39] che mantiene i dati di giorni di malattia per i professori associati
[00:35:45] la tabella sta a spà che carcola la media
[00:35:52] quindi il numero di giorni medio di assenze per malattia e professori associati
[00:35:59] La tabella giorni malattia pioh che carcola
[00:36:04] il
[00:36:06] i giorni malattia
[00:36:09] Per i professori ordinari andiamo adesso a scrivere la quale principale spazio
[00:36:16] con
[00:36:19] From quindi prendiamo
[00:36:22] La tabella giorni malattia professori ordinari perché dobbiamo vedere
[00:36:26] quali sono i professori ordinari che hanno fatto più giorni di malattia rispetto
[00:36:34] alla miglia dei professori associati. Questa tabela andiamo a rilominarla con
[00:36:37] GMPO, giorni di malattia e professori ordinari e poi andiamo a autorizzare anche
[00:36:44] ad ampera temporanea stazpa e la chiamiamo, possiamo anche nominarla, andiamo ad iniziare la
[00:36:56] clasla where e dove andiamo a verificare che effettivamente i professori ordinari all'interno
[00:37:05] della tabella gmpo prendiamo in considerazione il numero dei giorni di malattie di questi
[00:37:14] professori e andiamo a verificare che il numero di giorni di malattia dei professori ordinari
[00:37:25] sia maggiore della media, quindi di professori associati.
[00:37:35] Infine la quale ci richiede di restituire l'ID, quindi facciamo GMPO.ID, ci chiede
[00:37:52] di restituire il nome, ci chiede di restituire il cognome, il numero di giorni di assenza
[00:38:04] per malattia possiamo utilizzare il campo calcolato qui.
[00:38:09] Andiamo ad eseguire la quale, c'è un problema, è stata bella, ok e possiamo vedere che abbiamo
[00:38:36] Ginevra arriva che ha fatto un totale di tre giorni di assenze per malattia e che questi
[00:38:47] tre giorni gli essense sono superiore alla media dei giorni per malattia, gli essense
[00:38:55] fatte per malattia dei professori associati.
