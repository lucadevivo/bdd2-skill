# Trascrizione: E.B.2.2.3.2.7.1 - Cielo 4 - BD2

[00:00:00] Iniziamo l'esercitazione C4 partendo dalla query numero 1, andando quindi a trovare i voli di durata media maggiore tra tutti voli della stessa compagnia.
[00:00:09] Dema selezionare tutte le entrate della tabella volo 1, in cui abbiamo la condizione durata minuti che sia maggiore della media della durata minuti,
[00:00:20] presa come select average durata minuti dalla tabella volo, una seconda istanza di questa tabella quindi una tabella volo presa come
[00:00:29] volo 2
[00:00:31] in cui abbiamo anche la condizione
[00:00:44] che la compagnia
[00:00:46] della prima tabella sia uguale alla compagnia del secondo
[00:00:51] andiamo a ritornare
[00:01:01] questa query come possiamo vedere però presenta
[00:01:04] una referenza della query inestata a quella esterna e quindi andremo a ricalcolare diverse
[00:01:13] volte l'everage della durata minuti anche per compagnia già viste. Per questo motivo possiamo
[00:01:20] proporre per queste query una seconda versione che sia più leggera e andiamo a scriverla.
[00:01:27] Iniziamo a creare una tabella che chiamiamo STAZZ che contenga la durata media in minuti
[00:01:37] per ciascuna compagnia. Quindi andiamo a selezionare l'evereggi della durata in minuti da una tabella
[00:01:53] volo attraverso un group-by che ci consenta di effettuare la media sulle compagnie. Andiamo
[00:02:11] poi a selezionare i campi che ci interessano a partire da due tabelle, la tabella volo e
[00:02:19] la tabella appena creata stats. In questo caso, come nel precedente, andiamo a controllare
[00:02:45] che la compagnia dei voli che stiamo verificando corrisponda a quella della tabella contenente
[00:02:51] le statistiche e che la durata di minuti del volo in questione sia maggiore della
[00:02:58] durata media e otteniamo questo risultato. Procediamo quindi con la seconda quiri, andiamo a trovare
[00:03:21] le città che abbiano più di un aeroporto dove almeno un volo si ha operato da Pitalia. Quindi
[00:03:29] andiamo a selezionare la città dalla tabella luogo aeroporto e andiamo a controllare che
[00:03:34] l'attributo aeroporto di questa tabella sia presente nell'Unione, in questo caso ad
[00:03:42] adoperata con l'OR essendo in destra della clausola war delle partenze della tabella
[00:03:50] arriva e partenze tali che la compagnia di questi voli sia a pittalia e l'unione appunto
[00:04:08] con la tabella ritornata con la selezione degli arrivi della tabella arrivi e partenze
[00:04:19] Inquenderemo nuovamente a controllare che la compagnia sia a pitalia, notiamo come c'è
[00:04:33] necessità avendo usato il costruttore anidato di utilizzare un doppio anidamento in sostituzione
[00:04:40] alla clausola di unione.
[00:04:45] Quindi al termine di questo doppio anidamento andiamo a fare un group by per le città
[00:05:04] e a controllare che il numero di aeroporti sia maggiore di 1.
[00:05:09] Anche di questa query andiamo a proporre più di una versione, questo è il risultato.
[00:05:33] La seconda versione sfrutta il costrutto weed, così che possiamo utilizzare la clausora union.
[00:05:46] Quindi andiamo a selezionare gli aeroporti di interesse come l'unione tra le partenze,
[00:05:57] dove la compagnia sia per l'appunto a Italia e gli arrivi presi dalla tabella rivi e partenze dove la compagnia sia sempre a Italia.
[00:06:15] Dopo aver selezionato in questo modo airporti possiamo finalmente andare a selezionare le città della tabella luogo aeroporto
[00:07:10] controllando all'interno del nostro web semplicemente che l'aeroporto sia nella
[00:07:18] tabella che abbiamo creato con la clavus o la weed. Quindi con aeroporto
[00:07:25] ancora una volta andiamo a ripetere il group by per raggruppare percetta e
[00:07:54] andiamo ad assicurarci che ci siano almeno più di un aeroporto. Per questa
[00:08:19] Quiri abbiamo anche una terza versione in cui andiamo ad eliminare del tutto l'annidamento
[00:08:24] nella Closura VR, andiamo a selezionare l'attributo città dalla tabella l'overporto e andiamo
[00:08:34] a prendere per la nostra Quiri anche la tabella aeroporto e la tabella rivie partenza
[00:08:40] e la tabella volo. Nella Closura VR andiamo a controllare appunto che la compagnia
[00:08:57] dalla tabella volo sia in Italia che il codice dell'aeroporto sia tra le partenze o gli arrivi
[00:09:15] di arrivi e partenze in questo modo e che corrisponde anche al codice preso dalla tabella volo e
[00:09:44] alla tabella nuove aeroporto. Ripetiamo gli ultimi step quindi nuovamente il group
[00:10:07] by per città e andiamo ad asseguirarci che il numero di aeroporti sia aggervi 1 e
[00:10:35] otteniamo lo stesso risultato. Passiamo quindi alla query numero 3 e andiamo a trovare le
[00:10:44] coppie di aeroporti a eb tali che esistono l'itra eb e il numero di voli dal primo al
[00:10:50] secondo sia uguale a quello del secondo al primo. Andiamo quindi a selezionare partenza
[00:10:58] e arrivo dalla tabella arrivi e partenze, la prima instanza di questa tabella.
[00:11:04] Vi andremo infatti a considerare 3 all'interno del nostro web, dove in un primo momento andiamo a creare una prima qui rinnestata e a selezionare il numero con count di stanze nella tabella rive e partenze una seconda estanza, quindi rive e partenze due, in cui la partenza si è uguale alla partenza della prima tabella e anche l'arrivo.
[00:11:41] Andiamo a verificare che il numero ritornato da questa quirina estata sia uguale al numero
[00:12:02] ritornato alla seguente quirina, quindi andiamo a considerare nuovamente il numero di stanze
[00:12:08] quindi col count, ritornate alla tabella, arrivi ai partenze, ecco, una terza istanza,
[00:12:23] in cui la partenza sia uguale all'arrivo della quirina tabella e l'arrivo sia
[00:12:31] uguale alla partenza della prima.
[00:12:46] In questo caso abbiamo una quiria emidata e le quiri interne sono correlate a quelle esterne, quindi andiamo a recalcolare più volte cose che potremmo risparmiare.
[00:12:57] Infatti, dev'è proprio una seconda versione in cui andiamo ad eliminare l'annitamento e creiamo una prima tabella stazza, in cui andiamo a calcolare il numero di voli partendo dalla tabella rivie partenze
[00:13:23] e andando a raggruppare per coppia di partenza e arrivo, andiamo poi a selezionare le partenze
[00:14:04] i arrivi, dalle tabelle, l'appena creata stats e una seconda versione della stessa, quindi
[00:14:12] S1 e S2 e andiamo a controllare che all'interno della nostra clausola
[00:14:29] UR che le coppie partenze arrivo siano uguali e che il numero di voli sia
[00:14:39] uguale tra le due tabelle. Meglio i partenze arrivo siano invertite in realtà e otteniamo
[00:15:35] lo stesso risultato. Procediamo con la query numero 4 in cui andiamo a
[00:15:45] selezionare le compagnie che hanno voli con durata media maggiore della
[00:15:49] durata media di tutte le compagnie, andiamo a creare una prima versione in cui
[00:15:55] selezioniamo il nome delle compagnie appunto dalla tabella compagnie e andiamo a
[00:16:02] creare una query innestata, il costruttoware, in cui selezioniamo la
[00:16:10] durata media in minuti dei voli in cui la compagnie sia uguale a quella della
[00:16:23] tabella compagnia, selezionata all'esterno, e la durata minuti che abbiamo appena selezionato
[00:16:35] sia maggiore della media, quindi superiore al select average della durata minuti dalla
[00:16:43] tabella volo.
[00:16:52] In questo caso abbiamo la quirinestata che si referenzia la quirie esterna, motivo
[00:17:03] per il quale, come abbiamo detto precedentemente, abbiamo un'inefficienza per cui possiamo andare
[00:17:10] a costruire una seconda versione di questa query in cui utilizziamo il costruito weed
[00:17:20] e andiamo a creare questa tabella durata media voli selezionando la durata media con i
[00:17:34] collegi durata minuti della tabella volo e andiamo a selezionare la durata media
[00:17:51] dei voli di una compagnia, andando a selezionare il nome, la durata in minuti media, dalle tabelle
[00:18:14] compagnia e volo, andando a verificare che la compagnia sia della tabella volo sia quella
[00:18:31] della stessa e della tabella compagnia e andando a raggruppare con un group by per il nome
[00:18:38] della compagnia. Fatto questo andiamo a selezionare le compagnie delle tabelle appena
[00:19:08] create quindi durata media voli compagnia e durata media voli andando ad inserire come
[00:19:36] unica condizione all'interno del wear che la durata media dei voli sia maggiore della
[00:19:44] durata media dei voli delle compagnie. Questa versione non presenta alcun annidamento per cui
[00:20:01] è più efficiente della precedente e otteniamo lo stesso risultato.
[00:20:37] Procediamo con la quinta guerra in cui andiamo a ottenere gli aeroporti da cui partono voli
[00:20:47] per almeno due nazioni diverse. Una prima versione andiamo semplicemente a selezionare
[00:20:52] il codice della tabella aeroporto e nel guerra andiamo a verificare che il risultato della
[00:21:01] querinestata in cui selezioniamo il numero di nazioni differenti dalla tabella arrivi
[00:21:09] e partenze e luogo aeroporto in cui la partenza della tabella arrivi e partenze corrisponde
[00:21:36] al codice della tabella aeroporto esterna e l'arrivo della tabella rive appartenza e corrisponda
[00:21:45] all'aeroporto invece se lezionato alla tabella rive arrivi in un rive porto.
[00:22:03] Ancora una volta questa è solo una prima versione della soluzione, possiamo infatti
[00:22:11] andare a produrne una seconda che non contenga una query in estata e andiamo a
[00:22:23] selezionare le partenze della tabella arrivi e partenze e la tabella l'aeroporto
[00:22:31] che andremo ad utilizzare invece per gli arrivi infatti nel guerra andiamo
[00:22:39] ad assicurarci che l'arrivo della tabella arrivi e partenze sia uguale
[00:22:43] all'aeroporto era da bella l'overporto e andando a raggruppare per aeroporti di
[00:22:57] partenza, ci assicuriamo con un even count che le in azioni di arrivo
[00:23:14] siano superiori a 2, superiori uguali a 2 e otteniamo lo stesso risultato.
[00:23:34] Alleggere il quesito numero 6, che ci chiede quali sono i vuoli che partono dalle città con un unico aeroporto
[00:23:45] Dobbiamo restituire i codici dei voli, le compagnie e gli aeroporti di partenza di arrivo
[00:23:51] Bene, questo si fa con costruendo una tabella con il costruttore Witt
[00:24:00] Che tabella dobbiamo costruire?
[00:24:02] direi di costruirci la tabella del città con un unico aeroporto ok quindi andiamo a prendere la
[00:24:21] tabella al luogo a lavorare sul tabello al luogo aeroporto e andiamo a reagurare per città
[00:24:36] Iniziamo a città e facciamo un group-buy in città.
[00:24:43] Questo ci permette di fare un count sul numero di errori portali all'interno della città.
[00:24:54] Iniziamo che questo sia uno.
[00:25:06] Quindi scopriamo che i Parigi, New York e London l'ondranno un solo rapporto nella città.
[00:25:16] e questa da bella qui ce la chiamiamo città con unico aeroporto e su cosa dobbiamo lavorare
[00:25:48] chiaramente su città con unico aeroporto cca dobbiamo lavorare su luogo aeroporto e arrivo
[00:26:12] così da fare i dovuti join perché tutte le informazioni che ci interessano alla fine
[00:26:23] sono all'interno della Dabbella rivolvertenza quindi la città con un único report andiamo
[00:26:36] a fare il join con città di Vova Report e di conseguenza da la report di Vova Report
[00:26:48] facciamo a join con la partenza di orche o partenza ok quindi abbiamo detto cciva di città deve
[00:27:06] essere uguale a l a città e la assolta la rivolta di rivolto deve essere uguale ad app.partenza
[00:27:27] Cosa ci interessa? Ci sono tutte le informazioni di una tabella ARIVALORATO.
[00:27:37] Quindi questo è il risultato, questa è attenzione perché ci sono anche altre soluzioni a questo tipo di quelli
[00:27:47] dove potete utilizzare diversi livelli di anninamento all'interno delle quelli,
[00:27:53] si può utilizzare il costrutto IN, però utilizzare molti livelli di inendamento è molto poco di gildia.
[00:28:06] Seconda cosa, l'IN tipicamente è poco efficiente, quindi credo che questa sia la soluzione più chiara e deficiente.
[00:28:19] Allora, andiamo a leggere la domanda numero 7 che ci chiede quali sono gli aeroporti raggiungibili
[00:28:27] dall'aeroporto GFK tramite vuoli diretti e indiretti.
[00:28:31] Allora, per fare questo tipo di esercizi bisogna usare quello che si chiama il Whid
[00:28:40] Questo perché vi mostro che i dati su cui andiamo a lavorare sono tra virgolette gerarchici
[00:28:56] o meglio hanno una struttura che è ad albero.
[00:29:00] Adesso vi mostro se andiamo a vedere le partenze in pittenza.
[00:29:18] Vediamo che per i voli diretti è molto semplice, perché è un dato che abbiamo già all'interno della tabella.
[00:29:34] Vedi, in JFK FCO è JFK FCO, quindi ci aspettiamo che nel risultato per quanto riguarda i voli diretti avremo partenza arrivo, JFK FCO, o meglio, gli arrivi solo a FCO, perché vediamo solo gli arrivi.
[00:29:52] Per quelli indiretti, invece, dobbiamo partire da FCO.
[00:29:59] Una volta scoperto che da JFK posso arrivare ad FCO, bene, allora da FCO dove arrivo?
[00:30:06] Quindi devo porre la partenza uguale ad FCO.
[00:30:11] E vedere dove arrivo, cioè al ciantino e a JFK.
[00:30:18] Arrivali a JFK ci fermiamo.
[00:30:22] arrivati a champino invece dobbiamo andare a controllare dove andiamo da
[00:30:26] champino e arriviamo al fco agfk, a questo punto ci fermiamo perché sono
[00:30:32] destinazione che abbiamo già analizzato. Questa è una struttura d'altra, no?
[00:30:40] In questi casi, quando abbiamo strutture di questo tipo, un buon candidato è proprio
[00:30:45] l'utilizzo della ricorzione del weekday recassive.
[00:30:51] Adesso andiamo a vedere sulla documentazione che ho già preparato, controlla sempre che la versione sia corretta, sia quella della documentazione e sia quella della vostra installazione di Postgre
[00:31:09] vedete che la sintasi è molto simile al WIT classico, c'è un consulto in più, è il recassive,
[00:31:27] ma la parte importante è proprio questa, all'interno della quale abbiamo quello che si chiama nella
[00:31:38] documentazione la chiamano il termine non ricorsivo è questo qua quindi sarebbe
[00:31:48] il da dove parte la ricorsione ok in questo caso parte da uno follow union
[00:31:54] follow union all e il secondo termine è il termine ricorsivo invece ok in questo
[00:32:05] In questo caso, lui aggiunge ad N, un P1, front P, notare il front P, e si ferma quando
[00:32:18] N è uguale a 100, cioè un meglio continua, intanto che N è uguale a 100, ok?
[00:32:30] Cosa cambia tra lo union e lo union null?
[00:32:33] cambia che i termini, le righe duplicate, vengono eliminate con lo union, con lo union
[00:32:43] Oll invece queste rimangono ed è molto importante questa cosa per la nostra cosa, bene?
[00:32:53] quindi come lo appliciamo al nostro quesito?
[00:33:03] Allora, innanzitutto cancelliamo questa, andiamo a vedere, chiamiamola la tabella raggiungibili.
[00:33:16] Abbiamo detto caso base su un meglio termine non rikorsivo e dopo avremo il testo.
[00:33:41] Ok, nel termine non rikorsivo dobbiamo chiederci da dove vogliamo partire, in questo caso è molto semplice,
[00:33:48] perché partiamo dall'aeroporto GERKY o meglio, in questo caso ci identifica proprio quali sono i voli diretti che partono da GERKY, quindi partiamo da GERKY.
[00:34:12] Select from sempre quello, la tabela arrivo partenza, la vogliamo su quella, vogliamo la partenza condizionando sul fatto che la partenza debba essere uguale a gfk.
[00:34:34] Ok? Vi mostro il risultato di questa, così in parerina, vegliamo anche, capirgolette passo passo quello che succede, succede questo, ok?
[00:34:50] dobbiamo usare lo yunon a noi, non lo yunonol, perché non ci interessano i duplicati, ma se
[00:35:03] noi mettessimo lo yunonol e dopo ve lo mosso, la ricorsione non finirebbe mai. Adesso capirete
[00:35:10] perché. Comunque nel termine ricorsivo che cosa vogliamo? Partiamo sempre dal solito,
[00:35:19] Allora, ci serve la tabella raggiungibile, che chiamiamo R, e la tabella arriva a partenza.
[00:35:37] Che vogliamo fare? Quando si valuta il termine ricorsivo, cosa succede all'interno di Postgre?
[00:35:53] Che Postgre, scusate, c'è una tabella temporanea dove l'interno è contenuto il risultato della chiamata ricorsiva precedente.
[00:36:06] Nel caso dell'esimpio qui, cosa succede?
[00:36:11] Quando n è uguale a 1 abbiamo una tabella al temporale dove c'è 1 e gli aggiungiamo il più 1.
[00:36:21] Quando n è uguale a 2, a questo punto della ricorzione, lui vede n uguale a 2 e gli aggiunge il più 1.
[00:36:34] Ok, quindi vede sempre quello che succede nello step precedente.
[00:36:40] E la stessa cosa è qui. Sfruttando questa logica, noi avremo in uno step intermedio una o un po' più righe.
[00:36:55] Facciamo un esempio per le proprie, visto che ci abbiamo qui.
[00:37:00] Abbiamo detto, nel primo passo otteniamo il risultato gfkfco.
[00:37:09] Nel secondo passo, quello che vede internamente è proprio questa rica qui, ok?
[00:37:20] Come facciamo a dirgli che deve andare a cercare le righe che partono l'FCO?
[00:37:29] Abbiamo detto nella tabella R che è tra virgolette temporanea, perché la stiamo
[00:37:39] costruendo in corso d'opera, ok, nella tabella R, abbiamo partenza e arrivo, ok, a noi interessa
[00:37:49] l'arrivo, e dobbiamo assicurarci che sia uguale alla partenza di arrivo partenza. Stiamo
[00:38:01] sostituendo, no? Stiamo cambiando la... da partenza JFK, lo stiamo sostituendo con
[00:38:09] f.io. Quindi la condizione da tempore r.arrivo uguale a p.partenza e selezioniamo a p.partenza
[00:38:41] in questo modo che succede. Siamo sempre qui. Questa r è la tabella con solo gf.io. Prendiamo
[00:38:58] l'arrivo, abbiamo anche la tabella arrivo partenza, andiamo a prendere tutte le righe che hanno
[00:39:10] come partenza FCO, quindi questa, questa, questa e questa.
[00:39:26] Cosa succede? Nello step seguente andiamo ad analizzare una riga di FCO a champino e una riga di FCO GFK.
[00:39:44] Saltiamo per un attimo champino. Andiamo a vedere cosa succede qua. Questo è interessante.
[00:39:55] perché qui è dove la ricorzione dovrebbe interrompersi, altrimenti ritorniamo a gfrk,
[00:40:06] ritorniamo a fco, poi di nuovo si instaurà un cibo che non finisce Так più. Però abbiamo
[00:40:15] detto perché utilizziamo lo union invece dello union all, perché lo union all, scusate lo
[00:40:21] union ci vada a eliminare, non li andiamo proprio più ad analizzare, non fanno più parte del
[00:40:29] risultato. Quindi quando ci ritroviamo nella situazione nella quale abbiamo come arrivo
[00:40:40] JFK nella chiamata dopo, che succede? Ci ritroviamo come partenza JFK e arrivo FCO. Ma questa
[00:40:57] se ricordo ce l'abbiamo, l'abbiamo costruita addittura nel primo step, nel termine non
[00:41:05] ricorsivo, essendo un duplicato, non viene chiamato, viene, diciamo, non viene chiamato,
[00:41:15] viene cancellato il risultato e quindi non viene più considerato.
[00:41:28] e quindi continuiamo solo su champino, da champino vediamo che arriviamo all'fco e a gfk, quindi la ricorsione si interrompe per la stessa logica di quando abbiamo incontrato gfk precedentemente
[00:41:47] Ok, costruita la tabella, qual è il risultato, è questo, in realtà a noi interessano soltanto
[00:42:12] gli arrivi, scusate, e gli arrivi come vedete ci sono deduplicati quindi metteremo il distinto
[00:42:29] e questo è il risultato.
[00:42:31] Allora, adesso andiamo a leggere il quesito numero 8, quali sono ricette raggiungibili
[00:42:36] con voli diretti e ingretti, perché la Roma è chiaramente la struttura sia della
[00:42:45] domanda che quindi non si pensa di risultato come quella precedente, cambia
[00:42:53] soltanto che adesso abbiamo, dobbiamo coinvolgere una tabella in più all'interno della
[00:43:01] la tabella, quella riguardante le città, luogo aeroporto, ok perché qua abbiamo andato
[00:43:11] a aeroporto la città, bene, vediamo, procediamo esattamente come prima, quindi, qui più
[00:43:25] La tabella la chiamiamo città es, es come prima, termine non riuscivo. Facciamo un'altra
[00:43:45] parte. Così vediamo da dove partiamo e dobbiamo partire ovviamente da tutte le città, dobbiamo
[00:44:05] costruirci una tabella dove all'interno abbiamo non il codice dell'aeroporto, ma la città e l'arrivo sempre in una città, ok?
[00:44:21] Quindi con partenza a Roma dove arriviamo?
[00:44:28] Sicuramente ci serve la tabella partenza che chiamiamo AP, poi aeroporto L a 1 e l'overeroporto A2.
[00:44:57] L a 1 riguarderà le partenze e L a 2 riguarderà le arrivi.
[00:45:09] quindi prendiamo a t punto partenza, uguale te ne ha uno, destra uguale te le ha due e le ha quattro
[00:45:42] quindi vogliamo la città, il nome della città per la partenza e la seconda
[00:46:00] allora e questo voglio farvelo vedere quale sarà il risultato
[00:46:07] Non dobbiamo partire da Roma. Roma, Roma, no. Da Roma riusciamo sicuramente a raggiungere
[00:46:17] New York, come volo diretto, vale a New York, Roma, risultato. Tornando alla domanda da
[00:46:30] dove partiamo, chiaramente non partiamo da questa tabella, ma dobbiamo partire dalla
[00:46:34] bella dove l'aeroporto di partenza, la città di partenza in Roma, quindi l'A1 città uguale
[00:46:44] come questa, questo è il nostro termine non ricorsivo.
[00:47:04] Utilizziamo anche qui lo union distinct che a un ordre vero avremmo dovuto utilizzare
[00:47:12] e nel termine ricorsivo andiamo a lavorare sulle tappelle, arrivo partenza, città.
[00:47:27] Nella condizione dobbiamo fare esattamente quello che abbiamo fatto prima, quindi la partenza diventa l'arrivo
[00:47:49] e per semplificarci la vita mettiamo nella target list del termine non ricorsioso,
[00:47:56] lo andiamo ad utilizzare adesso l'aeroporto dell'arrivo.
[00:48:05] Questo perché a questo punto nel R possiamo direttamente utilizzare l'aeroporto di arrivo
[00:48:22] per condizionare che la partenza debba essere uguale all'aeroporto di arrivo
[00:48:30] e inoltre che l'arrivo deve essere uguale al l'aeroporto.
[00:48:46] A questo punto nella target list quello che ci interessava
[00:49:00] erano le città raggiungibili, un po' di diretti in diretti per tendere a vedere.
[00:49:06] Quali sono le città raggiungibili? Sono la quale a questo punto ci prendiamo anche l'aeroporto.
[00:49:17] Nel select questo caso la queue ci chiedeva esclusivamente le città
[00:49:38] e c'è l'errore perché aggiungendo una target list qui poi lo union non funziona più
[00:49:57] perché devono essere il numero di colonne uguale quindi direi che la partenza la possiamo togliere
[00:50:08] perché non ci serve e tra l'altro l'arrivo, lo rinominiamo in città,
[00:50:15] pubblico con esattamente uno scalo intermedio partendo dall'aleguato a Gietti.
[00:50:39] Allora in questo caso ci servirà sicuramente un contatore, ok?
[00:50:46] Perché dobbiamo calcolarci, contarci gli scali, ok?
[00:50:52] Dunque, sempre partendo dal Twitter e Carsevo, dove la tabella è stata la che abbiamo scali.
[00:51:09] Il termine non merigorsivo partiamo, allora dobbiamo partire chiaramente dai voli diretti che partono da JFK.
[00:51:31] Ok, sempre considerando le città.
[00:51:37] Select from where,
[00:51:41] nel from andiamo prende partenza p,
[00:51:47] nel where abbiamo detto che partiamo ad oggetti.
[00:51:58] L'arrivo deve essere uguale
[00:52:11] al codice dell'aeroporto.
[00:52:16] Nella target list vogliamo l'aeroporto
[00:52:26] La città e abbiamo detto che ci sarà un contatore degli scali, quindi partiamo dal
[00:52:47] zero e questo è il risultato.
[00:52:56] Infatti da GFK possiamo raggiungere direttamente soltanto il FG.
[00:53:03] Quindi questo è il nostro strato bella dove partiamo.
[00:53:11] A questo punto, partiamo da 9.00 o 9.00, dobbiamo lavorare sicuramente sulla tabella Scali,
[00:53:44] sulla tabella Arrivo Partenza.
[00:53:55] Adesso per limitare la compurazione a livello 1, non vogliamo andare più in profondità
[00:54:12] del livello 1. Come vi dicevo in precedenza, mentre la tabella Scali viene costruita,
[00:54:28] ne possiamo vedere quello che è successo il risultato delle direzioni precedente.
[00:54:33] Lo che ne facciamo, quello che dobbiamo fare è quello di non calcolare i piani di volo
[00:54:52] con 2 più trate, quindi quando scali è uguale a 2, teoricamente sc punto scali mi verrebbe
[00:55:10] a dire che debba essere 1, mai sbagliato, questo perché, come ho detto prima, vediamo
[00:55:21] ciò che c'è precedentemente, quindi se scali è uguale a 1, la chiamata ricorsiva
[00:55:29] faccio, quindi in realtà mi ferma due. Io poi adesso vedremo che nella target list facciamo
[00:55:40] un contatore dove incremento gli scali ad ogni chiamata. Ok, io metto nel where scalio
[00:55:51] uguale a uno, la chiamata la faccio e conto anche quelli con due scali e 3-0. Ok, faccio
[00:56:06] 0, guardo le riche che hanno un numero di scalio uguale a 0, faccio la chiamata ricorsiva,
[00:56:14] incremento il contatore e mi fermo. Dopodiché, capite che dopo non avrò più, avendo scalio
[00:56:27] uguale a uno, non li chiamo più. Poi devo condizionare sul fatto che mi serve il codice
[00:56:47] dell'aeroporto di partenza, l'aeroporto d'arrivo sia uguale all'aeroporto dell'horror.
[00:57:12] La target list, cosa ci serve? Ci serve sicuramente gli scali che abbiamo detto.
[00:57:26] Andiamo le volte in volta ad incrementare.
[00:57:32] Poi mi serve la città e l'aeroporto gli arrivo, quindi p.arrivo,
[00:57:45] Se vogliamo quello che ci ritorna, qual'è il risultato?
[00:57:55] Scari, ah beh, mi ho sbagliato totalmente l'ordine del colonne.
[00:58:06] Quindi Scari va per ultimo, città in mezzo, lo reporto bene.
[00:58:12] Quest'è il risultato?
[00:58:50] se ne mettiamo scali uguale ad uno, bene, ci va a togliere quelli con il zero,
[00:59:02] con l'esattamente che ci chiede, uno scala intercettivo.
[00:59:14] Visto che ci chiede soltanto i nomi, necessitavamo i nomi poi giustavete.
