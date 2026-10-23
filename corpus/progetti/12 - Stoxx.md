# 12 - Stoxx

> Fonte: `(12) Stoxx - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20160519 (P.20160519)
                                          Stoxx
                                                                             Progetto P.20160519

    Stoxx
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20160519

    Stoxx
    1. Introduzione
                 Introduzione
              Si vuole progettare Stoxx, un’applicazione per la gestione di una agenzia di promotori
              finanziari. In particolare, il sistema deve consentire di gestire il portafoglio titoli dei
              clienti dei diversi promotori dell’agenzia e di monitorare il loro andamento.
                                                                             Progetto P.20160519

    Stoxx
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              Di ogni promotore dell’agenzia, identificato da una matricola, interessa il nome, il
              cognome e l’insieme dei clienti di cui gestisce il portafoglio.
           Dei clienti interessa il nome, il cognome, il codice fiscale, almeno un recapito telefo-
           nico, un indirizzo email (se disponibile) e gli estremi di un documento di riconoscimento
           (tipo e numero), oltre che il promotore che gestisce attualmente il loro capitale.
           I clienti possono cambiare promotore all’interno dell’agenzia: Stoxx deve quindi es-
           sere in grado, per ogni cliente, di mantenere anche l’informazione su tutti i promotori
           dell’agenzia che hanno gestito il suo patrimonio nel passato (con relativo periodo), e una
           descrizione sulla causa che ha portato il cliente ad abbandonarlo (ad es., insoddisfazione).
           Gli strumenti finanziari accessibili ai clienti dell’agenzia possono essere di diverse
           tipologie: fondi gestiti, titoli azionari, titoli obbligazionari, o titoli di stato. Dei titoli
           azionari e obbligazionari interessa l’azienda emittente, dei fondi la società di gestione,
           dei titoli di stato lo stato che li ha emessi. I fondi gestiti sono paragonabili a titoli, ma in
           realtà consistono in investimenti, da parte della società di gestione del fondo, in un gran
           numero di titoli; tale politica ha come obiettivo quello di offrire al cliente uno strumento
           finanziario altamente diversificato e quindi meno soggetto alle volatilità del mercato,
           mantenendo la semplicità di gestione dei titoli (quote di un fondo gestito possono essere
           acquistate e vendute come se fossero semplici titoli azionari, obbligazionari o di stato).
           Di ogni fondo gestito Stoxx deve mantenere l’informazione circa il numero (non la lista)
           di titoli che contiene e la sua composizione, data dalla percentuale (in valore) di titoli
           azionari, obbligazionari, e di stato che lo compongono (non è necessario che da un fondo
           si possa risalire ai singoli titoli in possesso del fondo).
           I clienti, dietro consiglio del loro promotore, effettuano investimenti, ognuno dei quali
           si concretizza in uno o più atti di compravendita di un certa quantità di un titolo o fondo.
           Di ogni atto di compravendita, Stoxx deve mantenere l’informazione sulla quantità del
           titolo o del fondo acquistati o ceduti, la data dell’atto e l’importo investito o liquidato.
                 Al fine di monitorare l’andamento degli investimenti dei clienti, nel sistema vengono
                                                                             Progetto P.20160519

    Stoxx
    2. Specifica dei Requisiti
              memorizzati periodicamente i valori di tutti i titoli (azionari, obbligazionari, di stato) e
              delle quote di tutti i fondi gestiti trattati. La periodicità di tali monitoraggi non è nota a
              priori, e non è uguale per tutti i titoli o fondi. Pertanto, se per un certo giorno il valore
              di un titolo o della quota di un fondo non è disponibile, questo si assume essere rimasto
              invariato dall’ultima rilevazione.
              Il sistema viene utilizzato direttamente solo dai promotori dell’agenzia (che effettuano
              investimenti o disinvestimenti per conto dei loro clienti). In particolare, Stoxx deve fornire
              ai promotori dell’agenzia le seguenti funzionalità:
                 • Investire, per conto di un dato cliente, una certa quantità di denaro in un dato
                 titolo o fondo. Il numero di quote del titolo o fondo acquisite nel portafoglio del
                 cliente è dato dal valore dell’importo investito diviso il valore più recente della
                 quotazione del titolo o fondo scelto.
                 • Disinvestire, per conto di un dato cliente, tutte o una parte delle quote di un
                 titolo o fondo in suo possesso: la funzione dovrà restituire l’importo da liquidare
                 al cliente a seguito della transazione, calcolato come il prodotto tra il numero di
                 quote del titolo o fondo che il cliente ha deciso di vendere e il valore più recente
                 della relativa quotazione.
                 • Calcolare il valore complessivo corrente del portafoglio di un dato cliente, ottenuto
                 moltiplicando il numero di quote in portafoglio di ogni titolo o fondo per il valore
                 della relativa quotazione più recente.
                 • Calcolare il profilo di rischio di un dato cliente, che dipende dal valore percentuale
                 di azioni da egli possedute, rispetto al valore del suo portafoglio complessivo.
                 A tal fine valgono sia i titoli azionari posseduti direttamente dal cliente, sia le
                 componenti azionarie dei diversi fondi di cui il cliente possiede quote. Il profilo di
                 un cliente è “basso” se la percentuale di azioni da egli possedute è al più il 10% del
                 suo portafoglio, “moderato” se tale percentuale è compresa tra il 10% (estremo
                 escluso) e il 40%, “alto” se è compresa tra il 40% (estremo escluso) e il 60%,
                 “aggressivo” se è superiore al 60%.
                                                                             Progetto P.20160519
