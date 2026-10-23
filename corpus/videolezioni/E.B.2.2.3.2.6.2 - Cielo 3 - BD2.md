# Trascrizione: E.B.2.2.3.2.6.2 - Cielo 3 - BD2

[00:00:00] Alve a tutti benvenuti nella video esercitazione cielo 3 nella quale andremo ad affrontare degli
[00:00:06] esercizi su interrogazioni nella clausola from. Partiamo dunque dal primo esercizio che
[00:00:13] ci richiede di trovare la durata media per ogni compagnia dei voli che partono da un
[00:00:17] aeroporto situato in Italia. La strategia che adotteremo per risolvere
[00:00:22] tale esercizio sarà quello di definire una prima query all'interno grazie
[00:00:27] la quale otterremo per ogni compagnia la durata di ogni volo partente da un
[00:00:35] aeroporto italiano. Dunque una volta definita dalle quei e poi quest'altra
[00:00:40] quei verrà utilizzata nella clausola from di una quei più esterna che verrà
[00:00:45] poi a sua volta utilizzata per aggregare la durata, la durata dei voli
[00:00:53] attraverso la funzione EWG, quindi la funzione di media.
[00:00:58] Dunque partiamo dalla curima query, la query più interna e iniziamo a scrivere al nostro
[00:01:04] template vuoto la clausola from, all'interno della quale rintracciamo le tabelle che ci
[00:01:12] permetteranno di unire la durata dei voli alle compagnie.
[00:01:20] tali tabelle saranno appunto le tabelle a ricopartenza, art part, la tabella volo v e la
[00:01:31] tabella luogo aeroporto. Una volta fatto ciò andiamo a definire le condizioni in la clausola
[00:01:42] where che ci permetteranno di fare il join tra le tra queste tabelle ovvero che il codice del
[00:01:49] del volo si è uguale a punto codice che appunto il codice della
[00:02:02] compagnia, il nome della compagnia si è uguale a v.comp, quindi la compagnia del volo e dato
[00:02:12] che ci interessano informazioni sull'aeroporto di partenza prima che app.partenza sia uguale
[00:02:18] l punto aeroporto. Adesso l'ultima condizione che ci resta da definire è la condizione appunto
[00:02:27] che i voli partano che gli aeroporti la partenza dei voli avvenga da aeroporti italiani per
[00:02:34] fareciò quindi definiremo che l punto nazione sia uguale per l appunto a itali. Iniz
[00:02:44] finiamo con il definire la target list che in questo caso noi vogliamo ottenere per
[00:02:52] ogni compagnia la durata del volo e vorremmo anche ottenere delle nuble che
[00:02:58] hanno per la appunto la stessa compagnia quindi avremo che app.com nella nostra
[00:03:06] target list e associeremo ad ogni compagnia la durata del volo quindi
[00:03:10] v punto durata minuti. Andiamo ad eseguire la quaria allo stato attuale per verificarne
[00:03:22] la correttezza e possiamo vedere che ad ogni anno la corrisponde a un volo di cui sappiamo
[00:03:29] appunto la compagnia e sappiamo la durata in minuti del volo. Quindi andiamo a inserire
[00:03:36] tale quaria all'interno del costrutto weed per poterla poi riutilizzare dopo nella
[00:03:40] quelli più esterni, quindi weed, la chiamiamo partenze italiane, has e
[00:03:52] specificiamo la nostra quelli. Adesso passiamo con il definire la quelli più
[00:03:59] esterna. Iniziamo nuovamente con il nostro template vuoto e in questo caso
[00:04:05] utilizzeremo nella clausola from la quelli appena definita, quindi partenze
[00:04:10] italiane. Adesso ovviamente vogliamo raggruppare tutte queste
[00:04:22] perché come potete vedere l'output qui in basso potremmo avere delle ennubile con la
[00:04:27] stessa compagnia, noi vogliamo raggruppare per compagnia quindi utilizzeremo il costrutto
[00:04:32] group by dove specificchiamo come elemento per come colonna per raggruppare le ennubile
[00:04:40] appunto la compagnia. Ovviamente avendo specificato qui la colonna della compagnia dovrò
[00:04:50] necessariamente utilizzare tale colonna all'interno della nostra target list quindi
[00:04:54] id.comp.es compagnia. Infine vogliamo associare ad ogni
[00:05:03] compagnia quindi la durata media di tutti i voli, dei voli che compaiono nella
[00:05:10] tabella partenza italiana. Dunque per fare questo dobbiamo utilizzare
[00:05:15] necessariamente la funzione aggregata della media ovvero AVG e
[00:05:22] specificiamo come colonna di cui vogliamo calcolare la media appunto la
[00:05:26] durata in minuti quindi id punto durata in minuti
[00:05:34] quindi nominiamo come durata media e andando a eseguire la guerria allo
[00:05:40] stato attuale possiamo ritrovare il risultato desiderato l'esercizio
[00:05:48] Num. 2 ci richiede di trovare le compagnie che operano voli con durata media
[00:05:54] maggiore rispetto alla durata media di tutti i voli. Per risolvere tale
[00:05:59] esercizio faremo ricorso a due queri anidate all'interno della clasa la
[00:06:04] fronma. Una prima queri verrà utilizzata per determinare la media della
[00:06:11] durata di tutti i voli. La seconda queri invece verrà utilizzata per
[00:06:21] determinare per ogni compagnia la media della durata generale di tutti i voli.
[00:06:28] Una volta ottenute queste due queri le andremo per l'appunto ad utilizzare in
[00:06:38] una queri esterna, all'interno della clausola fromline queri esterna, per
[00:06:43] confrontare i valori delle due cabbelle, quindi ottenere il nostro risultato.
[00:06:46] Quindi partiamo innanzitutto con la prima queri nella quale vogliamo
[00:06:52] trovare appunto la media durata di tutti i voli, questa è una queri molto semplice.
[00:06:55] partiamo per l'appunto dalla clausola from e utilizziamo la tabella volo per
[00:07:02] ottenere la durata poi avremo in questo caso nella target list la
[00:07:10] grid function avg che ci darà la media per l'appunto della durata in minuti di
[00:07:19] tutti i voli. Adesso andiamo ad eseguire a query e possiamo trovare appunto una
[00:07:35] tabella con un unico valore che contherà per la media della durata di ogni
[00:07:42] volo. Adesso nella seconda query vogliamo per
[00:07:46] determinare la media della durata dei voli per ogni
[00:07:53] compagnia, quindi la query sarà molto semplice, solamente che avremo bisogno
[00:07:56] ovviamente di raggruppare per per ogni per ogni compagnia quindi andiamo partiamo dall'altra
[00:08:05] dell'altra query e andiamo per l'appunto a diseguire il raggruppamento utilizzando l'operatore
[00:08:10] group by e andando per l'appunto a raggruppare per compagnia adesso ovviamente perché abbiamo
[00:08:20] definito la compagnia in group by siamo necessariamente obbligati ad utilizzare la
[00:08:25] compagnia nella target list quindi avremo comp e avremo per l'appunto composto la nostra
[00:08:32] seconda query di cui avevamo bisogno infatti se andiamo ad eseguire per
[00:08:36] eseguire ovviamente solo la seconda query in questo caso in ordine avremo che per
[00:08:40] per ogni compagnia avremo la relativa durata media adesso quello che vogliamo
[00:08:45] fare utilizzare queste due tabelle e confrontarle per determinare invece le
[00:08:49] compagnie che hanno una che hanno una durata media di volo superior
[00:08:54] la durata media di tutti i voli quindi per fare ciò per utilizzare queste due
[00:09:00] tabelle nella in una clausola from di una query esterna dovremmo utilizzare
[00:09:07] wit e chiamiamo la prima media durata volo has e avremo per appunto inserito la
[00:09:30] prima e adesso inseriamo la seconda query nel nostro costrutto weed che sarà per l'appunto
[00:09:38] media durata compagnia has. Adesso quindi avremmo per l'appunto definito le due query
[00:10:01] all'interno del con il con il nostro costrutto weed possiamo riutilizzarle nella query più
[00:10:06] esterna quindi partiamo nuovamente dal template tuoto quindi select from wheat e avremo per
[00:10:15] l'appunto che la clausola from utilizzerà entrambe le query che abbiamo appena definito quindi
[00:10:22] avremo l'appunto media durata volo has dv e media durata compagnia media durata
[00:10:47] compagnia che andremo a chiamare per l'appunto mdc adesso andiamo per l'appunto a confrontare che
[00:11:02] che per ogni nupla, dobbiamo avere che la media della turata di ogni compagnia sia della
[00:11:16] compagnia presa delle nupla deve essere maggiore rispetto alla turata media generale di tutti
[00:11:21] i voli, quindi andiamo a impostare questa condizione all'interno della nostra clausola
[00:11:28] della nostra clausola where, quindi avremo che
[00:11:32] mdc.media
[00:11:40] durata. Sarà per l'appunto
[00:11:46] maggiore rispetto a
[00:11:49] mdv.media
[00:11:56] durata.
[00:11:59] Adesso, ovviamente, quindi da dalla tabella, da questa tabella, possiamo vedere che se andiamo ad eseguire
[00:12:06] avremo ottenuto per ogni nuplà del nostro output la media durata sia della prima tabella
[00:12:19] quindi di media durata follow e la media durata di media durata compagnia quindi quello che
[00:12:24] vogliamo fare ovviamente ottenere la compagnia e la relativa durata media quindi in questo
[00:12:31] caso magic fly possiamo vedere che ha una durata media di volo di 420 minuti che è
[00:12:40] maggior rispetto alla durata media generale ovvero quella definita dalla
[00:12:43] prima query quindi andiamo a definire la nostra target list dove avremo per
[00:12:48] appunto che m avremo la compagnia quindi mdc.comp e avremo poi appunto la mdc.media
[00:13:07] durata es media durata com andiamo ad eseguire la query e possiamo per l'appunto trovare
[00:13:22] il risultato desiderato. L'esercizio numero 3 chiede di trovare quali
[00:13:30] siano le città dove il numero 3 di voli in arrivo è maggiore del numero medio di
[00:13:34] l'inarrivo per ogni città. Per risolvere questo esercizio faremo nuovamente
[00:13:41] ricorsa due query anni data all'interno della clausola from. Quindi l'obiettivo è
[00:13:47] definire una prima query in cui avremo per ogni città il conteggio di arrivi,
[00:13:53] quindi il conteggio comunativo di arrivi, quindi conteggio per ogni città.
[00:14:05] Nella seconda query invece vogliamo trovare la media degli arrivi di ogni città. Una
[00:14:21] volta definite le due query poi queste ultime possono essere inserite all'interno della
[00:14:26] clausola from e potremmo andare a verificare la condizione che per appunto che il numero
[00:14:31] di arrivi sia maggior rispetto alla media degli arrivi all'interno della clausola
[00:14:37] were di una query più esterna. Quindi partiamo dalla prima query nella quale
[00:14:42] vogliamo determinare il conteggio degli arrivi per ogni città, quindi iniziamo dal template
[00:14:47] vuoto e inseriamo all'interno della nostra clausola from le tabelle di cui abbiamo bisogno,
[00:14:56] ovvero la tabella arrivo partenza che è per l'appunto l'aeroporto arrivo l'aeroporto
[00:15:03] di partenza e ovviamente ovviamente avremo bisogno anche della tabella luogo aeroporto.
[00:15:09] Adesso impostiamo nella clausola where la condizione del join in cui appunto l'aeroporto
[00:15:18] di arrivo debba essere uguale per l'appunto a l punto a aeroporto.
[00:15:23] Adesso vogliamo raggruppare quindi le nubile che abbiamo in questa questa
[00:15:33] query che se possiamo eseguirla troviamo qui.
[00:15:37] Vogliamo andarla a raggruppare ovviamente per ogni ogni città e poi
[00:15:41] eseguire un conteggio su tale raggruppamento, quindi per fare ciò
[00:15:45] utilizziamo il costrutto group by definiamo dunque una partizione per per città
[00:15:53] quindi l punto città eseguiamo ovviamente ci dà un errore poiché in questo
[00:16:03] caso abbiamo definito nella clasa la group by una colonna che dobbiamo
[00:16:08] necessariamente andare ad utilizzare nella nostra target list quindi eseguiamo
[00:16:13] nuovamente possiamo vedere che la partizione è stata eseguita ma non abbiamo alcun valore
[00:16:18] aggregato associato ad ognuna delle partizioni quindi andiamo ad utilizzare la aggregate function
[00:16:24] count dove contiamo tutte le correnze di tutte le nuble e lo chiameremo numero arrivi.
[00:16:30] Eseguiamo la query e possiamo vedere che abbiamo il risultato intermedio che ci serve.
[00:16:38] Adesso passiamo alla seconda query ovvero la media degli arrivi per ogni città in questo
[00:16:45] In questo caso la queri è molto semplice e per eseguire questa queri andremo ad utilizzare
[00:16:55] la queri che abbiamo già definito, quindi il conteggio di più per città, e aggregheremo
[00:17:00] quindi utilizzeremo un valore aggregato su tali valori.
[00:17:06] Quindi andiamo a scrivere il nostro tempo è tuoto e andiamo ad utilizzare all'interno
[00:17:15] della clausolafrom il conteggio degli arrivi e questa la query che è stata appena definita quindi
[00:17:22] per poterla utilizzare l'andiamo a inserire all'interno del costrutto wit e lo andiamo a
[00:17:28] chiamare conteggio arrivi per città haas e lo inseriamo per l'appunto lo definiamo con il
[00:17:42] costrutto width quindi adesso possiamo utilizzarlo nella clausola from avremo
[00:17:46] conteggio arrivi per città
[00:17:53] adesso noi vogliamo utilizzare il valore della vogliamo utilizzare una
[00:18:00] media sui sulla colonna numero arrivi che possiamo trovare qui in basso quindi
[00:18:05] per fare questo non abbiamo ovviamente bisogno di aggregare nulla
[00:18:08] poiché abbiamo già i valori che ci servono nella colonna numero arrivi
[00:18:11] quindi utilizzeremo l'aggregate function numero arrivi as media arrivi quindi in questo caso non
[00:18:25] ci è servito eseguire alcuna partizione perché in questo output le nuble sono già partizionate
[00:18:31] per città quindi eseguiamo la query e possiamo vedere che avremo una media generale di tutti
[00:18:41] e di arrivi per ogni singola città, adesso perché vogliamo utilizzare anche questa query
[00:18:48] nella nostra query finale per eseguire il confronto lo andremo ad inserire nella clautola from quindi
[00:18:58] la chiameremo media arrivi città di ogni città ovviamente e inseriamo la cuori che abbiamo
[00:19:12] appena scritto adesso passiamo quindi alla cuori la cuori finale quindi scriviamo il nostro
[00:19:21] template vuoto dove andremo ad utilizzare ovviamente le due tabelle che abbiamo definito
[00:19:31] nel nostro weed, quindi con teggio arrivi per città e media arrivi città. Quindi avremo
[00:19:40] con teggio arrivi per città che chiameremo CAC e media arrivi per città che si nominiamo Mac.
[00:19:57] Adesso, leggermente esercizio, ci si richiede di determinare quali siano le città in cui il
[00:20:04] il numero dalle di voli sia maggiore rispetto al numero medio di voli, quindi andremo a
[00:20:09] imporre tale condizione alla claudulaver scrivendo che cac punto numero arrivi sia per la punto
[00:20:18] maggiore rispetto a mech punto media arrivi. Eseguiamo la guerria allo stato attuale
[00:20:35] E potremmo vedere che avremo per l'appunto delle sole annuble in cui il numero di arrivi
[00:20:44] è superiore rispetto alla media di arrivi, quindi per Roma avremo 5 arrivi che è superiore
[00:20:48] rispetto alla media generale 2.75 e se questa cosa vale per New York, quindi adesso finiamo
[00:20:55] la nostra target list per ottenere il risultato di serato che sarà per l'appunto la
[00:21:00] città quindi la colama città e per l'appunto il numero arrivi in questo caso la media non
[00:21:07] vogliamo ottenerla quindi eseguiamo la query e troviamo appunto il risultato desiderato
[00:21:20] vediamo adesso lo svolgimento della query numero 4 che ci chiede quali sono le compagnie aeree che
[00:21:29] hanno vola in partenza dell'aeroporto in italia una durata media inferiore alla
[00:21:33] durata media tutti i voli in partenza dell'aeroporto in italia per farlo in tutti
[00:21:39] iniziamo copiandoci il testo della quale andiamo a vedere quali sono le
[00:21:46] compagnie che hanno dei voli in partenza dell'aeroporto italiani e vediamo la
[00:21:51] durata dei loro voli quindi iniziamo scrivendo la struttura della quale
[00:21:57] avremo sicuramente bisogno della tabella ARPART, le nominiamo AP, della tabella BOLO che nominiamo V
[00:22:07] e della tabella L'UOGO AERO VORTO che nominiamo con le tra L.
[00:22:15] Andiamo ad unire queste tabelle e per farlo dobbiamo dire che ARPART.CODICE è esattamente
[00:22:25] volo.police e poi andiamo a dire che
[00:22:33] artpart.partenza è esattamente il luogo
[00:22:41] aeroporto.airoporto in questo modo
[00:22:46] abbiamo un'itera da bella artpart con volo in
[00:22:51] in questo modo è a part con l'uoco l'ocorto con con quest'altra condizione
[00:22:58] successivamente dobbiamo andare a dire che a definire che la nazione da cui partono questi voli
[00:23:11] perché abbiamo collegato il luogo dell'uoco l'ocorto alla partenza
[00:23:15] quindi andiamo a dire che la nazione di L deve essere Italia
[00:23:20] di questi voli andiamo ad inserire la target list app.com, quindi la compagnia e la durata
[00:23:36] in minuti del volo ok vediamo che queste sono le compagnie che hanno dei voli che partono
[00:23:49] l'Italia e questa è la durata in minuti di quei voli. Adesso dobbiamo andare a
[00:23:57] calcolare la media dei voli che partono dall'Italia, quindi questa vuole qui la
[00:24:03] facciamo di entrare in una vuole temporanea attraverso il costrutto
[00:24:06] e rinominiamo questa query durata partense e italiane e andiamo a utilizzare questa query
[00:24:34] che abbiamo appena fatto per andare a calcolare la media de polli che partono d'Italia, quindi
[00:24:42] quindi andiamo ad utilizzare un'altra tabela temporanea che possiamo chiamare media, durata, partenze,
[00:24:56] utilizziamo la struttura classica della query e andiamo a dire che prendendo la tabella
[00:25:12] durata partenze dagli anni, quindi andando a considerare la tabella appena calcolata,
[00:25:18] vediamo quale è la media della durata in minuti
[00:25:23] quindi per vedere la media utilizziamo la funzione che è legata a vg
[00:25:28] e vediamo facciamo la vg della colonna durata in minuti
[00:25:34] quindi durata in minuti
[00:25:39] ok e la denominiamo
[00:25:47] in questo modo abbiamo che questa tabela temporanea
[00:25:50] ci dice quale è la durata media delle de voli con partenza italiana. Quindi fatto
[00:26:03] questo andiamo a calcolarci la media e la durata de voli per ogni compagnia.
[00:26:12] Quindi possiamo sempre farlo sulla tabella durata partenza italiana e
[00:26:19] e vediamo, creiamo un'altra tabella temporanea che chiamiamo compagnia, curata, curata, partenze italiane, quindi sarebbe la curata delle partenze italiane per compagnia
[00:26:36] e andiamo a definire anche questa query, la definiamo anzi tutto, scriviamo le classiche
[00:26:51] calsole che di cui sicuramente aremo bisogno e andiamo a prendere in considerazione quindi
[00:26:57] questa tabbella. Come il from, iniziamo la tabbella temporale
[00:27:00] a durata partenza d'aliane all'interno della quale andiamo a vedere nella target
[00:27:07] lì stenderemo compagnia e la media dei voli di ogni compagnia quindi facciamo una media
[00:27:17] sulla colonna durata a minuti e rinominiamo durata media. La momento che abbiamo utilizzato
[00:27:30] una funzione aggregata andiamo quindi a raggruppare utilizzando il group by per cosa
[00:27:40] raggruppiamo raggrupperemo per la compagnia ok adesso considerando la media che abbiamo
[00:27:52] calcolato per le compagnie quindi quest'ultima questa ultima tabela temporanea e la media
[00:28:02] fatta su tutti i voli quindi quest'altra ultima e quest'altra la penultima tabela
[00:28:08] temporanea e dobbiamo andare a filtrare, a prendere solamente le compagnie che
[00:28:15] hanno una durata media inferiore alla media di tutti i voli che partono in
[00:28:19] Italia per farlo e oggi andiamo a creare la quale di quelle esterna, quindi la
[00:28:28] quale principale, vediamo un po' di spazio, all'interno di questa quale quindi andiamo a
[00:28:35] considerare la tabella dove abbiamo la meta di tutte le compagnie italiane, quindi compagnie italiane e
[00:28:43] media, faremo una situazione del genere, compagnie, media, durata, e andiamo a prendere questa tabella
[00:29:02] qui che ci dice quale è la media di tutti i voli che partono dall'Italia e questa qui la
[00:29:10] nominiamo compagnie dorata partenza italiana cdp e media dorata partenza
[00:29:20] andiamo a cavo così del gemello la nominiamo media dorata partenza
[00:29:27] italiana mdp e di queste compagnie di queste di queste tabelle dobbiamo
[00:29:37] anziché soprattutto una target list, prima di tutto inseriamo il nome della
[00:29:43] compagnia, quindi lo prendiamo da cdp comp e andiamo a nominare la colonna
[00:29:53] compagnia e prendiamo la media perché non so, mandiamo a mostrare le
[00:30:04] le compagnie e la loro media dei voli, durata media, quindi ammipd.durata media e ci mamminiamo
[00:30:15] che questa vola non è una condurata. Poi andiamo a inserire la clausola where, all'interno
[00:30:23] della quale dobbiamo dire che consideriamo solamente le compagnie che hanno una durata
[00:30:32] media inferiore alla media di tutti i voli che partono all'aria, quindi dobbiamo dire che la durata
[00:30:40] media per compagnie, quindi compagnie durata e partenze da piane punto durata media, stiamo andando a
[00:30:52] prendere questa colonna qui, deve essere minore della durata media di tutti i voli che partono
[00:31:05] da Italia, quindi media durata partenza italiana punto durata, andiamo a considerare questa
[00:31:18] colorna qui, eseguiamo i voli e vediamo che questi sono, queste qui sono le
[00:31:28] compagnie che hanno i voli, dei voli impartenzati dall'Italia e questi voli
[00:31:37] hanno una durata media inferiore alla durata media di tutti i voli in
[00:31:42] partenza da aeroporti italiani. Passiamo ora allo svolgimento della
[00:31:48] la quale ci chiede, quale sono le città e quei voli in nativo hanno la durata metrica che
[00:31:55] differisce specia di più di una derivazione standard
[00:31:58] da la durata media di tutti i voli e ci chiede di restituzionare la città e le durate media di voli
[00:32:04] in nativo.
[00:32:05] Iniziamo.
[00:32:06] Come prima cosa calcoliamo la durata media di voli in nativo, la quali ci chiede quali ci chiede
[00:32:29] come prima cosa calcoliamo la durata media di voli e ovviamente la loro
[00:32:34] di versione standard, quindi per farlo possiamo fare e tutto partiamo sempre
[00:32:43] dalla clossa da select e from e consideriamo la tabella volo, prendiamo il
[00:32:50] considerazione della tabella volo e ci basta questa per calcolare la media
[00:32:54] della durata minuti dei voli e la di versione standard della durata
[00:32:59] e per farlo realizziamo la funzione di aggregazione AVG per la durata di minuti e questo ci
[00:33:12] distrutirà la media della durata e poi andiamo ad utilizzare la funzione aggregata per calcolare
[00:33:22] la dilazione standard. PostgreSQL ci ci permette di calcolare la dilazione standard
[00:33:28] utilizzando la funzione aggregata stdd e boom all'interno della quale andiamo a
[00:33:48] inserire con quella colonna per la quale vogliamo calcolare la
[00:33:53] la direzione standard dorata in minuti, denominare la colonna con la direzione standard, eseguiamo.
[00:34:10] Ho già aperto qui la documentazione di PostgreSQL e per andare a vedere insomma come fai la direzione standard
[00:34:20] infatti tra le funzioni aggregate vediamo che è appunto quella della direzione standard.
[00:34:28] torniamo ai nostri esercizi e vediamo che questa è la media della durata di minuti di ecoli
[00:34:36] e questa invece è la direzione standard. Ora inseriamo questa qui all'interno di... facciamo
[00:34:46] una tabella temporanea attraverso la consola weed e che come chiamiamo staz e andiamo a
[00:35:01] inserire questa questa quale all'interno e poi infine dobbiamo andare a calcolare le
[00:35:13] città e dobbiamo prendersi c'è la città che è adurata media perché quello che
[00:35:20] che ci è chiesto di restituire, che differiscono di più di una devazione standard
[00:35:33] di tutti i voli, della media di tutti i voli. Quindi per farlo andiamo a scrivere
[00:35:40] la cuore esterna e all'interno della cuore esterna dobbiamo prendere in considerazione
[00:35:48] e per prendere le città e vogliamo prendere un'inconserazione da bella part a p
[00:36:01] prendiamo un'inconserazione da bella volo o dobbiamo
[00:36:07] dobbiamo prendere in considerazione anche il luogo dell'aeroborto quindi luogo l'aeroborto l
[00:36:16] Prendiamo in conciazione ovviamente la tabela temporanea che abbiamo appena creato, stazza.
[00:36:27] Ok, con questa quale andiamo ad effettuare le unioni tra le varie tabelle, quindi iniziamo la classe LaWare
[00:36:46] e dobbiamo dire dove il codice del volo di arpart è uguale al volo punto codice
[00:36:58] poi dobbiamo dire che l'arrivo, l'aeroporto di arrivo e dobbiamo prendere il luogo dell'aeroporto
[00:37:16] quindi in questo modo stiamo collegando ARPART con l'overporto e vediamo in considerazione
[00:37:26] solamente l'overporto di arrivo perché c'è stato chiesto quali sono le città che vuol
[00:37:31] in arrivo hanno un'aturata media che differentiere di più di una animazione standard quindi
[00:37:37] andiamo ad unire da pelle per codice del volo con tra al parte volo e poi andiamo a vedere
[00:37:49] il luogo dell'aeroporto di arrivo e basta. Una volta fatto questo ovviamente inseriamo nella
[00:38:05] target list le città e poi all'interno del target list dovremmo anche inserire la
[00:38:14] durata in minuti quindi per chi di ogni città vogliamo sapere qual è la media della durata
[00:38:19] in minuti quindi andiamo a inserire la considerazione di grada media di volo punto durata
[00:38:27] e la rimaniamo durata. Possiamo andare a vedere quale sono quelle medie
[00:38:47] della durata di minuti di voli per ogni città di arrivo e possiamo farlo se seguiamo la
[00:38:53] guerra e adesso avremo un errore perché ovviamente città è nella target list dove c'è anche
[00:39:01] una colsina gregata quindi va messa nel group-by, inseriamo città nel group-by in modo giustamente
[00:39:14] da raggruppare per le città, in questo modo vediamo che abbiamo raggruppato per le città
[00:39:22] e per le città abbiamo la durata media dei minuti di voli che sono in arrivo in quella
[00:39:29] città.
[00:39:30] Adesso cosa dobbiamo fare?
[00:39:32] Adesso dobbiamo andare a filtrare quelle città e andiamo a prendere solamente le città
[00:39:41] la cui durata media è maggiori di una derivazione standard.
[00:39:46] lo facciamo andando a filtrare appunto la colonna di durata media con la clasola
[00:39:58] herring e diciamo che non dobbiamo prendere quindi usiamo anche in not, non dobbiamo
[00:40:08] prendere quelle città per cui la media è compresa tra la media generica di tutti i
[00:40:41] quindi sta appunto media la sottrazione e l'addizione della mediazione della
[00:40:56] defezione standard quindi non deve essere compresa tra la media e la defezione standard
[00:41:03] e la stessa cosa andiamo a metterlo con le andale mettiamo sotto questa questa
[00:41:17] in between per una legibita maggiore e dobbiamo fare la stessa cosa ma aggiungendo
[00:41:29] la deviazione standard in questo modo andremo a prendere solamente le città
[00:41:34] la meta di durata in minuti per ogni volo sia maggiore di una
[00:41:43] la deviazione standard dell'area media di tutti gli altri poli. Andiamo ad eseguire la query.
[00:41:51] L'errore è andato dal fatto che giustamente tutte le colonne che non sono infuse in funzione di
[00:42:08] aggregazione ben modellizzata nella target list o nel leving devono essere
[00:42:16] inseriti all'interno della clausola group by quindi dobbiamo andare ad inserire
[00:42:21] nella clausola group by la direzione standard e la media ok in questo modo
[00:42:40] vediamo che le città di Londra e Parigi con una donata media di 60 minuti
[00:42:46] di feriscano più di una direzione standard dalla donata meta di tutti i voli.
[00:42:52] Passiamo adesso alla sesta e ultima quelli che ci chiede quali sono le azioni che hanno
[00:43:01] il maggior numero di città dalle quali partono voli dirette in altre azioni.
[00:43:06] scriviamoci questo testo all'interno del nostro commento e andiamo ad eseguire da quelli.
[00:43:16] Allora, prima di tutto, iniziamo vedendo quante città per ogni nazione hanno voli verso altre nazioni.
[00:43:25] Quindi scriviamo le relazioni in base che scriviamo sempre.
[00:43:31] per fare ciò andremo a considerare la tabella ARPART e due tabelle l'aeroporto che andrà a
[00:43:47] definire il luogo dell'aeroporto di partenza e uno che andrà a definire il luogo dell'aeroporto
[00:43:54] e poi andiamo a dire che le azioni dell'aeroporto di partenza e dell'aeroporto d'Orivo devono
[00:44:11] essere belle, allora l'aeroporto di partenza al fatto.partenza è uguale l'uovo partenza.aeroporto
[00:44:33] e poi andiamo a dire che le nazioni dell'aeroporto di partenza e dell'aeroporto d'orivo devono essere diverse
[00:44:43] quindi nuovo partenza punto nazione
[00:44:49] deve essere diverso da nuovo partenza punto arrivo
[00:44:55] e adesso andiamo ad inserire una target list la vogliamo calcolare in una nazione quante
[00:45:18] città ci sono che hanno boli che vanno in nazioni diverse quindi andiamo a calcolare
[00:45:24] La nazione di partenza, quindi luocopartenza.nazione e contiamo, vogliamo contare, quante città
[00:45:42] ha una nazione, ma le contiamo distintamente, altrimenti venderebbe anche i duplicati.
[00:45:50] Rominiamo questa colonna con...
[00:45:57] Dobbiamo ovviamente inserire l'epinazione all'interno della cosa da Group By
[00:46:03] perché tutte le colonne che non... che non vengono utilizzate all'interno delle funzioni aggregate
[00:46:15] ma sanno una target liste e devono stare all'interno della... all'interno del Group By.
[00:46:21] E andiamo ad eseguire la quale.
[00:46:25] ok vediamo che la Francia ha una città l'Italia ha una città e così via queste sono le città
[00:46:34] che hanno
[00:46:35] dei voli che vanno in altre nazioni
[00:46:40] e sono divisi per nazione inseriamo questa guerra all'interno del
[00:46:46] di un'altra colonna di un'altra scusa di un'altra dobbia del coramea con la con il costrutto witt
[00:46:54] come la chiamiamo
[00:46:57] chiamiamo la stazza sempre, perché ci dà una statistica su quante città ci sono.
[00:47:04] Adesso andiamo a vedere, anche se in questo caso non abbiamo bisogno perché sono tutti
[00:47:20] di uno, però in realtà ne abbiamo bisogno perché non è detto che tutte le azioni abbiano
[00:47:27] solamente una città. Andiamo a prendere il massimo numero di città da questa tabella,
[00:47:36] quindi creiamo un'altra tabela temporaria che chiameremo maxCittà e all'interno di
[00:47:51] questa tabela scriveremo la quella di indica. Vediamo in considerazione la tabela stazze
[00:48:03] quale è il massimo, il massimo di Numo Città, Numo Città all'interno di quella tabella
[00:48:22] e questa quale veramente avrà uno all'interno della, all'interno di questo risultato sarà
[00:48:35] di questa query, è facile vederlo, e adesso andiamo a scrivere la query più esterna e nella
[00:48:45] query più esterna diciamo quali nazioni di quelle selezionati nella tabela stats hanno
[00:48:55] esattamente numero di città massime quindi per farlo andiamo a scrivere sempre la
[00:49:02] la clausola select e la clausola from. All'interno della clausola from abbiamo bisogno quindi
[00:49:10] dit stats e abbiamo bisogno di max, citta, max. E cosa dobbiamo dire? Dobbiamo selezionare
[00:49:39] solamente le nazioni che hanno esattamente il numero di città massime, quindi staz.num.città
[00:49:51] e andiamo a stampare tutti i dati della bella STAZZ, quindi STAZZ.org
[00:50:11] Ok, vediamo che il risultato è lo stesso dell'esercizio della Piena Guéry ma il risultato
[00:50:42] è giusto perché in Francia c'era il massimo delle città per cui ci sono dei voli che
[00:50:50] vanno in altre nazioni uno e quindi abbiamo che queste sono le nazioni che
[00:50:58] hanno il maggior numero di città con voli diretti in altre nazioni.
