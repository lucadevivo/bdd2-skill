# Trascrizione: E.B.2.2.3.2.2.2_Cielo_1 - BD2

[00:00:01] Benvenuti nella video esercitazione CELO1, all'interno del quale andremo ad affrontare
[00:00:08] le interrogazioni su tabbella multipla. Iniziamo la video esercitazione andando a
[00:00:14] ricordare lo schema relazionale, partendo per l'appunto della definizione dei domini
[00:00:19] in cui troviamo il classico post-integer, ovvero il dominio di numeri positivi, abbiamo
[00:00:26] poi stringa M, ovvero una stringa che può essere per l'appunto al massimo di 100 caratteri
[00:00:32] e il dominio codiata che può essere una stringa di esattamente 3 caratteri. Passiamo dunque
[00:00:40] alle tabelle del nostro schema relazionale, troviamo per l'appunto la tabella volo caratterizzata
[00:00:47] da un codice, da una compagnia e da una durata in minuti. Abbiamo poi la tabella
[00:00:53] arrivo partenza, caratterizzata anche esso da un codice, da una compagnia, dal codice
[00:00:58] iata dell'aeroporto di arrivo e dal codice iata dell'aeroporto di partenza.
[00:01:04] Abbiamo poi la tabella aeroporto, caratterizzata dal codice iata dell'aeroporto e dal nome
[00:01:11] dell'aeroporto in stringa. Troviamo poi la tabella luco aeroporto, caratterizzata
[00:01:18] una colonna aeroporto, quindi un codiceiata, avremo una città e una nazione e infine troviamo la
[00:01:26] compagnia caratterizzata per la punta da una colonna nome o per una stringa e dall'anno di
[00:01:31] fondazione. Siamo dunque dal primo esercizio che ci richiede di determinare quali sono i voli
[00:01:43] specificando il codice e il nome della compagnia, la cui durata supera alle tre ore. Quindi
[00:01:49] iniziamo la nostra query scrivendo innanzi tutto il template vuoto e
[00:02:00] specificiamo all'interno della clausola from la tabella dal quale vogliamo
[00:02:05] recuperare delle informazioni ovvero la tabella volo.
[00:02:08] Adesso vogliamo imporre la condizione all'interno della nostra query in cui
[00:02:17] abbiamo che la durata del volo debba essere debba superare le tre ore, quindi
[00:02:23] andiamo ad utilizzare la colonna durata a minuti che deve essere necessariamente maggiore uguale di
[00:02:35] 180 minuti ovvero 3 ore. Infine, specificiamo all'interno della target list le colonne che
[00:02:43] ci interessa avere nel nostro output, nella nostra tabela di output ovvero codice che
[00:02:50] che rinomeremo e comp che sarà denominata compagnia, eseguiamo la nostra query e possiamo
[00:03:09] vedere per l'appunto il risultato atteso. L'esercizio numero 2 è molto simile rispetto
[00:03:20] al primo surcizio a Nintendo il quale ci viene chiesto di determinare quali siano
[00:03:25] le compagnie che hanno voli che superano le tre ore. In questo caso, quindi, notiamo che le
[00:03:30] condizioni che dobbiamo andare a imporre all'interno della nostra Cloud SolarWare sono esattamente
[00:03:35] lo stesse, così come la tabella all'interno della Cloud SolarFrom, che resta la tabella
[00:03:42] volo. Quello che cambia in tale esercizio è il modo in cui andiamo per l'appunto
[00:03:48] a presentare l'output. Infatti ci vengono chieste le compagnie interessate, unicamente
[00:03:54] compagni interessate. Dunque andremo a modificare la nostra target list andando a rimuovere per
[00:04:00] l'appunto i codici dei voli. Se eseguiamo la query allo stato attuale possiamo notare che avremo
[00:04:08] appunto delle compagnie che avranno delle nuble che avranno dei valori duplicati ovvero delle
[00:04:14] compagnie che compagnono più botte perché sono associati a più voli. Quindi per andare a
[00:04:20] adobbiare a tale situazione, utilizzeremo l'instruzione Select Distinct e possiamo vedere che per l'appunto
[00:04:30] i valori duplicati all'interno d'italiano che sono stati rimossi e abbiamo ottenuto
[00:04:36] per l'appunto l'output che stavamo cercando.
[00:04:38] Siamo dunque al terzo esercizio in cui ci viene richiesto di determinare quali siano
[00:04:46] i voli, specificando il codice e il nome della compagnia che partono dall'aeroporto
[00:04:50] con codice CHA.
[00:04:52] Dunque, iniziamo questa query andando a scrivere ancora una volta il nostro template vuoto
[00:04:59] che andremo a comporre partendo dalla nostra clasula from.
[00:05:03] In questo caso, quindi, la tabella che ci interessa utilizzare per la nostra query
[00:05:11] è la tabella arrivo partenza R. La condizione che dobbiamo andare in
[00:05:20] imporre che le ennuble all'interno del solato devono rispettare e che per l'appunto la
[00:05:26] partenza, il codice yata radiva la partenza sia per l'appunto c e a. Quindi andremo a
[00:05:33] scrivere partenza uguale c e a. Infine andiamo a comporre la nostra target list specificando
[00:05:45] le informazioni che ci vengono richieste all'interno dell'esercizio dunque il codice
[00:05:49] il nome della compagnia, quindi scriveremo codice es, codice volo e comp es. Eseguiamo la nostra
[00:06:09] query e troviamo qua il risultato desiderato. Procediamo con la query numero 4, la quale
[00:06:19] che ci chiede quali sono le compagnie che hanno voli che arrivano all'aeroporto con
[00:06:24] un cuo di certo CO. Per farla di assoluto andiamo a scrivere l'astruttore della Coevi.
[00:06:33] All'interno del Chrome prendiamo la considerazione da bella part part e prendiamo i voli che
[00:06:44] hanno come valore di arrivo il FCO. Di questi voli ovviamente vogliamo sapere
[00:06:58] Quali sono le compagnie che forniscono questo servizio?
[00:07:03] Quindi andiamo insieme a una target list della class of the select, il nome della colonna che compa.
[00:07:13] Quindi questi sono i voli.
[00:07:16] Da un momento che ci sono duplicati andiamo ad inserire, e noi vogliamo inserire solamente
[00:07:20] quali sono le compagnie che lo fanno, quindi non ci interessa di duplicare, andiamo a inserire il distinct.
[00:07:26] e per dovidare la colonna facciamo un TMS
[00:07:36] perfetto, quindi queste sono le compagnie che hanno di boli
[00:07:41] che arrivano all'aeroporto con il quale c'è FCO
[00:07:44] procediamo con la quale numero 5
[00:07:47] andiamo a leggerle a quale sono i boli
[00:07:56] codice del bolo e nome della compagnia che partono all'aeroporto FCO
[00:08:00] e arrivano all'aeroporto JFK
[00:08:02] andiamo sempre a prendere considerazione da bella Rpart
[00:08:06] Nel where inseriamo le cose che ci vengono richieste, quindi che deve partire dall'aeroporto fco, quindi la parte tensa uguale di essere uguale a fco e l'arrivo deve essere aggerti, perfetto.
[00:08:36] andiamo adesso insieme alla target list quello che ci ho richiesto quindi il codice del
[00:08:42] bolo e il nome della compagnia perfetto quindi abbiamo che il codice e il bolo con
[00:08:57] codice 144 della compagnia magic fly parte da fco e arriva a jfk che andiamo a
[00:09:06] rinominare le colonne per una comprensione maggiore dell'algibita maggiore, questo è il codice
[00:09:18] l'ultimo codice volo e con il primo che abbiamo compagnia. Procediamo con l'acquari numero 6,
[00:09:32] l'acquari si chiede quali sono le compagnie che hanno volli che fattano l'aeroporto FCO e
[00:09:39] e aterrano all'aeroporto jfk quindi per fare ciò andiamo sempre con una considerazione
[00:09:49] da bella art part e andiamo a selezionare l'ho fatto prima e la prima siamo andati a prendere
[00:10:17] il codice del volo e il numero di compagnia.
[00:10:19] Adesso dobbiamo solamente considerare le compagnie che hanno questo tipo di voli.
[00:10:22] Quindi dove la partenza è uguale FCO, al vivo è uguale JIT.
[00:10:37] Ok, quindi andiamo a prendere le compagnie che fanno questo tipo di volo.
[00:10:45] Ok, perfetto.
[00:10:47] che ne veniamo potrebbero esserci deduplicati perché in questo caso stiamo citando quali
[00:10:54] compagnia lo fanno, potrebbero passare un test e ci usiamo un distinto anche se non ci sono.
[00:11:00] E noi ne veniamo alla colonna. Vediamo la quali numero 7 che ci chiede, quali sono i nomi
[00:11:14] delle compagnie che hanno volito i diretti dalla città di Roma alla città di New York.
[00:11:19] quindi questo è un po' diverso, andiamo qua a scrivere la struttura, dobbiamo sicuramente
[00:11:29] prendere con considerazione la tabella ARR part e l'IALN ARR part, poi prendendo in considerazione
[00:11:46] la tabella, prendendo in considerazione la tabella luogo aeroporto, questa tabella
[00:12:08] Nominiamo luogo P perché sarei il luogo di partenza e abbiamo bisogno di un'altra tabella per il luogo di arrivo, quindi rinvigno luogo A, andiamo a capo così riusciamo a leggerla bene.
[00:12:32] Ok.
[00:12:33] Questa, andiamo a prendere di queste tabelle, innanzitutto dobbiamo dire che in Rpart,
[00:12:45] la partenza deve essere uguale a l'uovo partenza.ai rovata. Dobbiamo fare lo stesso
[00:13:04] con l'arrivo.
[00:13:24] Dobbiamo andare a dire che
[00:13:27] l'aeroporto di partenza deve essere nella città di Roma
[00:13:31] quindi luogo di partenza
[00:13:35] punto città
[00:13:39] è uguale a Roma
[00:13:42] e dobbiamo fare la stessa cosa
[00:13:44] però con il luogo di arrivo che deve essere
[00:13:47] uguale a New York
[00:13:50] L'uovo questa volta di attivo, quindi l'uovo A.Città è uguale a New York. Perfetto.
[00:14:02] Di questi voli andiamo a prendere i nomi delle compagnie che effettuano.
[00:14:12] Quindi per fare ciò dobbiamo prendere part.
[00:14:18] In una target list mettiamo le compagnie che sono all'interno della tabella Rpart, quindi Rpart.com
[00:14:26] Come ho fatto già prima, andiamo a nominare la colonna
[00:14:31] Vediamo che ci sono dedicati a un'interessa sapere
[00:14:41] Quali sono i voli, quindi interessa sapere quali sono le compagnie
[00:14:45] E andiamo a mettere un distinto
[00:14:50] queste sono le compagnie che effettuano e che hanno voli diretti dalla città di Roma
[00:14:55] alla città di New York. Continuiamo le esercitazioni sul database
[00:15:06] cello 1, in particolare le prendiamo dalla query numero 8, andiamo come prima cosa a
[00:15:12] scrivere il nostro template vuoto e andiamo ad analizzare la query, le abbiamo quindi
[00:15:18] strapolare gli aeroporti con relativo codice yata nome e luogo dei quali partono vuole
[00:15:23] della compagnia di nome Magic Fly. La prima cosa che facciamo è andare a
[00:15:28] selezionare le tabelle di interesse, quelle che ci serviranno per estrapolare
[00:15:32] esattamente questi valori. Come prima tabella andiamo a inserire la tabella
[00:15:36] aereoporto, poi la tabella arrivi e partenze e infine la tabella luogo
[00:15:42] aereoporto. Per quanto riguarda i valori invece dei campi da selezionari
[00:15:48] abbiamo il campo codice dalla tabella aereoporto che andrà a
[00:15:52] rappresentare appunto il codice, il campo nome dalla stessa tabella e infine per il
[00:15:58] luogo il campo città dalla tabella luogo aeroporto. Per quanto riguarda le
[00:16:04] condizioni da controllare dobbiamo verificare che la compagnia estrapolata
[00:16:10] alla tabella rive e partenza sia esattamente quella desiderata quindi
[00:16:13] magic fly che l'aeroporto di partenza corrisponde esattamente al codice
[00:16:19] all'interno della tabella aeroporto e infine che l'aeroporto di partenza in arrivi e partenze
[00:16:29] sia corrispondente anche all'aeroporto della tabella luogo aeroporto. Andiamo a verificare
[00:16:44] questo risultato. Passiamo quindi alla seconda query. Nella seconda query andiamo a selezionare
[00:16:51] come tabelle di interesse, arrivi e partenze, il luogo aeroporto per ben due volte, una prima
[00:16:58] volta in modo tale che corrisponde al luogo del primo aeroporto e una seconda che corrisponde
[00:17:03] al luogo del secondo aeroporto. Per quanto riguarda invece i campi di interesse andiamo a selezionare
[00:17:09] il codice da arrivi e partenze, la compagnia dalla stessa tabella e l'aeroporto di partenza
[00:17:18] e l'aeroporto di arrivo sempre dalla mediesima tabella.
[00:17:22] La tabella luogo aeroporto che non è stata utilizzata nei campi del SELECT verrà utilizzata per controllare le condizioni.
[00:17:28] La prima condizione che controlliamo è infatti che l'aeroporto di partenza dalla tabella arrivi aeroporto
[00:17:33] corrisponda esattamente all'aeroporto nella tabella luogo aeroporto 1,
[00:17:39] quindi nella tabella in cui si occupiamo del luogo del primo aeroporto.
[00:17:43] allo stesso modo dalla tabella arrivi e partenze se lezioniamo l'arrivo e
[00:17:46] controlliamo che corrisponda all'aeroporto nella tabella luogo aeroporto 2.
[00:17:52] Infine abbiamo altre due condizioni da controllare che riguardano il luogo la
[00:17:58] città degli due aeroporti quindi andiamo a selezionare luogo aeroporto 1 e
[00:18:02] controlliamo che la città sia Roma e luogo aeroporto 2 e controlliamo che
[00:18:06] la città sia New York. Qui una piccola correzione, un errore di
[00:18:17] scrittura della Stringa New York che richiede lo spazio e altri piccoli errori di battuta.
[00:18:32] Finalmente, eccoci. Passiamo quindi alla decima quiri. In questo caso abbiamo qualche tabella
[00:18:40] in più. Abbiamo per due volte la tabella l'Ugheria Porto, un po' per la logica precedente,
[00:18:50] quindi arrivi a partenze per il primo volo e arrivi a partenze per il secondo volo.
[00:19:05] Nella tabella di selezione dei campi di ritornare abbiamo la compagnia, che deve essere in comune ma in questo caso la prendiamo dal primo volo,
[00:19:18] il codice e la partenza sempre del primo volo.
[00:19:23] Poi abbiamo il luogo dello scalo che corrisponde all'arrivo del primo volo,
[00:19:29] infine il codice del secondo volo e il luogo del arrivo.
[00:19:36] Come condizioni da controllare?
[00:19:49] Andiamo in primis a verificare che l'aeroporto di partenza sia corrispondente
[00:19:56] all'aeroporto della tabella luogo aeroporto 1.
[00:20:00] Poi verifichiamo che la città di partenza e il primo volo si aroma, dopodiché verifichiamo
[00:20:17] che l'arrivo del primo volo corrisponda alla partenza del secondo, quindi siamo uno scalo
[00:20:24] effettivamente, che l'arrivo del secondo volo corrisponda al luogo del luogo aeroporto
[00:20:34] della tabella luogo aeroporto numero 2 e infine le ultime due condizioni quindi che
[00:20:45] il luogo di arrivo sia New York quindi dalla tabella luogo aeroporto numero 2
[00:20:54] controlliamo che la città sia New York e infine controlliamo che le compagnie dei
[00:21:05] due voli corrispondano che un altro criterio richiesto all'interno del
[00:21:12] il testo ed ecco il risultato. Passiamo quindi all'ultima delle query, in questo caso andiamo
[00:21:36] a selezionare semplicemente la tabella arrivi e partenze e la tabella compagnia. Per quanto
[00:21:48] riguarda gli attributi invece andiamo a considerare semplicemente la compagnia presa dalla
[00:21:53] tabella arrivi e partenze e come condizioni andiamo a controllare che la partenza avvenga
[00:22:06] dall'aeroporto FCO, lo stesso modo andiamo a verificare il corretto aeroporto di arrivo,
[00:22:18] andiamo ad assicurarci che la compagnia nella tabella compagnia corrisponda a quella degli
[00:22:25] voli selezionati da arrivi e partenze e infine a verificare la conoscenza e l'anno di fondazione,
[00:22:34] quindi che l'anno di fondazione con attributo opzionale non sia nullo. Questo è il risultato
[00:22:42] e terminiamo in questo modo l'esercitazione.
