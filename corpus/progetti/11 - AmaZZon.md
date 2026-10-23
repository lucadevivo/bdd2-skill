# 11 - AmaZZon

> Fonte: `(11) AmaZZon - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20220222 (P.20220222)
                                     Amazzon
                                                                             Progetto P.20220222

    Amazzon
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20220222

    Amazzon
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare AmaZZon, un piattaforma online di e-commerce che
              vuole offrirsi come marketplace comune di offerte di venditori indipendenti.
              In particolare, si desidera che il sistema consenta ai negozi registrati nella piattafor-
              ma di pubblicare offerte di vendita per prodotti di varie tipologie, che possono essere
              acquistati dagli utenti privati registrati.
                                                                             Progetto P.20220222

    Amazzon
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              La piattaforma AmaZZon è utilizzata sia da negozi (che pubblicano offerte di loro
              prodotti) che dai clienti (che acquistano tali prodotti).
           Di ogni negozio registrato, il sistema deve mantenere informazioni circa il nome,
           l’indirizzo della sede legale, almeno un indirizzo email e opzionalmente un numero di
           telefono per la richiesta di informazioni e assistenza post-vendita.
              I negozi registrati usano la piattaforma per pubblicare offerte di (ovvero per mettere
              in vendita) prodotti di vario genere.
           Gli articoli disponibili su AmaZZon possono essere offerti da più negozi. Le diver-
           se offerte per uno stesso articolo possono differenziarsi nelle condizioni applicate. In
           particolare, all’atto dell’inserimento di un articolo in vendita, il negozio deve dichiarare
           nome e descrizione dell’articolo, marca, numero del modello, categoria, un insieme di tag
           (stringhe), prezzo e istante di inizio e, eventualmente, di fine dell’offerta di vendita. Si
           noti AmaZZon non è a conoscenza delle informazioni di quanti pezzi di un certo articolo
           possono essere vendute da un certo negozio. In caso un negozio dovesse terminare la
           disponibilità di magazzino di un articolo che ha posto in vendita, sarà sua cura eliminare
           la relativa offerta su AmaZZon.
           Il seguente esempio potrebbe aiutare a chiarire alcuni dei requisiti precedenti.
           Il
           negozio ‘New Tech s.r.l.’ con sede legale in ‘via A. Turing 1, Milano’ mette in vendita
           il nuovo modello di televisore al plasma ‘Pony PN123 plus’ al prezzo di 1199.00 Eur.
           L’offerta è valida dal 23 ottobre al 15 novembre 2022 (salvo disponibilità). AmaZZon
           infatti non ha informazioni sulle disponibilità di magazzino del negozio: sarà cura di
           quest’ultimo eliminare l’offerta dal marketplace in caso di tutto esaurito.
           AmaZZon permette ai negozi di definire le spese di spedizione di un articolo in base
           al paese di destinazione e al numero di pezzi acquistati. In particolare, il negozio deve
           associare ad ogni articolo le spese di spedizione per l’acquisto di un singolo pezzo in base
           al paese di destinazione.
                 Il negozio può inoltre definire definire spese di spedizione ridotte in caso di acquisto di
                                                                             Progetto P.20220222

    Amazzon
    2. Specifica dei Requisiti
              più articoli identici. Ad esempio, il negozio di cui sopra definisce le seguenti spese di spe-
              dizione (per un certo paese) per il ‘Pony PN123 plus’: acquisto di 2-4/5-9/10-99/100+
              articoli: Eur 4.99/3.99/2.99/gratis. Le spese di spedizione per 7 pezzi equivarranno
              quindi a 7 × Eur 3.99.
              Dato che più negozi possono mettere in vendita lo stesso articolo (a condizioni diffe-
              renti), AmaZZon mantiene una sua vetrina di tutti gli oggetti disponibili, permettendo
              quindi all’utente di: (i) navigare nella vetrina di tutti gli oggetti in vendita; (ii) consul-
              tare, per ognuno di essi, la scheda tecnica con codice identificativo univoco dell’articolo
              (una stringa secondo un certo standard globale), nome, marca, numero di modello, cate-
              goria, tag; (iii) accedere a tutte le offerte riguardanti l’articolo da parte dei diversi negozi
              (accedendo quindi al prezzo ed ai costi di spedizione).
              Come detto, tutti gli articoli in vendita su AmaZZon sono presenti in una vetrina
              unica. Dunque, all’atto della pubblicazione, da parte di un negozio, di un’offerta per un
              certo articolo, il sistema deve permettere di creare una scheda tecnica per quest’ultimo
              solo se non esiste già. Altrimenti, la nuova offerta dell’articolo consiste (oltre che al
              riferimento all’articolo nella vetrina comune) solo nel prezzo e nei costi di spedizione.
              Per evitare l’inserimento di un articolo nella vetrina comune con dati errati (ad es.,
              errata categoria), un negozio che, all’atto dell’inserimento di una offerta per un articolo
              già esistente in vetrina, dovesse notare un errore nei dati della scheda tecnica dell’oggetto,
              può segnalare l’errore ed eventuali correzioni allo staff di AmaZZon.
              AmaZZon permette agli utenti di acquistare dei buoni regalo, i quali possono essere
              spesi sulla piattaforma per l’acquisto di altri prodotti. Di ogni buono regalo interessa
              conoscere l’utente che l’ha acquistato, l’importo e il periodo di validità. Al momento
              del pagamento, l’utente può scegliere se utilizzare o meno ognuno dei suoi buoni regalo
              attivi. In caso i buoni scelti non dovessero essere sufficienti, il cliente potrà effettuare
              il pagamento residuo con una delle carte di credito registrate (di cui il sistema deve
              memorizzare: nome del titolare, numero –una stringa di 16 cifre–, e data di scadenza),
              se non scaduta.
              Gli utenti privati possono registrarsi al sistema. Gli utenti registrati (dei quali interessa
              il nome utente e l’istante di registrazione) possono visualizzare gli oggetti in vendita e
              le relative offerte (cosa per la quale non è necessaria la registrazione).
              Gli utenti privati registrati possono effettuare acquisti sulla piattaforma, includendo
              un qualsiasi numero di articoli e di pezzi per articolo. Il sistema deve permettere all’utente
              di ottenere l’importo totale dell’acquisto, considerando il costo di ogni articolo e le
              spese di spedizione verso il suo paese (scegliendo ovviamente la tariffa di spedizione più
              conveniente tra quelle offerte dal venditore applicabili al numero di articoli acquistati).
              Inoltre, gli utenti privati registrati possono salvare delle liste dei desideri (wish list),
              contenenti oggetti che desiderano acquistare. Di ogni wish list il sistema mantiene (oltre
              che l’utente registrato proprietario), il nome e l’insieme di oggetti che contiene.
              Periodicamente AmaZZon effettua una verifica del prezzo più basso disponibile per
              ogni oggetto presente nelle wish list di ogni utente e, se rileva un abbassamento di prezzo,
              notifica la cosa all’utente.
                                                                             Progetto P.20220222

    Amazzon
    2. Specifica dei Requisiti
              Le wish list possono essere pubbliche o private. Mentre le wish list private sono visibili
              solo all’utente che le ha create, le wish list pubbliche sono consultabili anche agli utenti
              amici del proprietario, che quindi possono avere ispirazione circa regali particolarmente
              graditi.
           L’amicizia tra utenti di AmaZZon viene instaurata con una richiesta dell’uno e l’ac-
           cettazione dell’altro. L’amicizia è un concetto simmetrico, quindi in ogni coppia di utenti
           amici, ogni utente può consultare le wish list pubbliche dell’altro.
                 Infine, il sistema deve permettere:
           • al management di calcolare, dato un periodo di tempo, il paese dal quale sono
           provenuti più acquisti nel periodo dato
                 • visualizzare tutti gli oggetti in vendita di una data categoria e contenente un dato
                 insieme di tag (mostrando, per ognuno, il prezzo più basso, comprensivo del costo
                 di spedizione)
           • visualizzare gli articoli attualmente più moda, che sono gli articoli il cui volume
           di vendite è salito percentualmente di più nell’ultimo mese, rispetto alla media
           mensile dei due mesi precedenti.
                                                                             Progetto P.20220222
