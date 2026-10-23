# 13 - CoLab

> Fonte: `(13) CoLab.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20220610 (P.20220610)
                                         CoLab
                                                                             Progetto P.20220610

    CoLab
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20220610

    CoLab
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare CoLab, un sistema di gestione per un certo spazio di
              coworking, ovvero uno spazio attrezzato come ufficio e utilizzato da più persone abbonate
              per periodi più o meno brevi. Imprenditori, liberi professionisti e imprese condividono
              il luogo di lavoro per abbattere i costi fissi legati al possesso di un ufficio, per creare
              opportunità di networking e condividere idee.
              Per mezzo del sistema, si vogliono gestire i clienti dello spazio di coworking, le
              strutture e i servizi offerti e gli abbonamenti.
                                                                             Progetto P.20220610

    CoLab
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              CoLab è direttamente utilizzato dai gestori dello spazio di coworking, dai suoi clienti e
              dai suoi utenti.
           Gli utenti abbonati dello spazio, oltre ad avere accesso ad una postazione di lavoro
           personale, possono utilizzare, spazi comuni (per esempio sale riunioni) e attrezzature
           (stampanti, telefono, ecc).
              Di ogni utente interessa il nome, il cognome, la data di nascita, l’indirizzo e l’indirizzo
              email.
           Gli abbonamenti sono stipulati dai clienti, che possono essere persone fisiche oppure
           imprese.
           Delle persone fisiche interessa il nome, il cognome, la data di nascita ed
           eventualmente la partita IVA, mentre delle imprese interessa la ragione sociale e la
           partita IVA.
           Un abbonamento ha un istante di inizio e una tipologia. Delle tipologie di abbona-
           mento interessa il prezzo, la durata, l’intervallo di date in cui può essere sottoscritto e il
           numero di utenti che possono usufruire dello stesso abbonamento.
           Di ogni abbonamento interessa conoscere anche gli utenti dello spazio di lavoro che
           ne usufruiscono concretamente; un abbonamento sottoscritto da un cliente aziendale
           deve indicare l’insieme di utenti che ne usufruiscono.
           Di ogni servizio offerto dallo spazio (sala riunioni, attrezzatura, ecc.) interessa co-
           noscere una descrizione e un prezzo unitario per il suo utilizzo; ad esempio, per una sala
           riunioni il prezzo unitario rappresenterà il costo dell’utilizzo della sala per un’ora, mentre
           per una stampante sarà il costo di stampa di ogni pagina.
           Ad ogni tipologia di abbonamento è associato un insieme di servizi cui è possibile
           usufruire con un abbonamento di tale tipologia, ognuno con una percentuale di sconto
           sul prezzo dell’utilizzo unitario e una soglia mensile di utilizzo gratuito (un intero).
           Ogni volta che un utente utilizza un servizio (ad esempio, utilizza la sala riunioni
           o effettua una telefonata), il sistema deve memorizzarne l’istante di inizio, quello di
           fine e la quantità utilizzata, rappresentata da un numero intero (per esempio, minuti di
                                                                             Progetto P.20220610

    CoLab
    2. Specifica dei Requisiti
              conversazione telefonica, pagine stampate, ore di utilizzo della sala riunioni). Il sistema
              di gestione di un servizio deve poter comunicare a CoLab la quantità di servizio utilizzato
              e gli istanti di inizio e fine dell’utilizzo.
              Per questioni di sicurezza, rendicontazione e profilazione, il sistema deve mantenere
              lo storico degli accessi allo spazio di coworking per ogni utente. Di ogni accesso interessa
              conoscere l’istante di entrata e quello di uscita.
              A ogni utente abbonato è associata una postazione di lavoro, la quale è caratterizzata
              da un numero identificativo ed è assegnata in modo esclusivo ad un utente abbonato.
              Il sistema deve offrire delle funzionalità specifiche alle diverse tipologie di utenti. In
              particolare, i potenziali clienti devono poter scegliere e sottoscrivere un abbonamento di
              una tipologia disponibile nel periodo corrente.
              I clienti devono poter monitorare i servizi utilizzati dagli utenti associati ai loro
              abbonamenti.
              Gli utenti devono poter effettuare l’accesso, registrare l’uscita.
              I gestori dello spazio devono poter creare nuove tariffe, aggiungere servizi e verificare
              l’abbonamento di un utente.
                 Inoltre:
                1. Il management dello spazio, per monitorare l’utilizzo delle postazioni, deve poter
                calcolare, dato un insieme di intervalli orari disgiunti (ad esempio, “8:00–12:30”,
                “13:00–17:00”, “19:00–23:00”) la media giornaliera di utenti abbonati che hanno
                usufruito dello spazio per ogni intervallo orario, nel mese corrente.
                2. Il sistema deve poter calcolare, data un’impresa e un lasso di tempo, il costo totale
                dei servizi utilizzati oltre le soglie gratuite dagli utenti a essa associati, nel periodo
                indicato.
                3. Il management vuole poter calcolare, dato un periodo ed un intero positivo k,
                i k servizi maggiormente utilizzati dagli utenti che hanno effettuato accessi nel
                periodo.
                4. Il servizio clienti vuole poter calcolare, dato un periodo, gli utenti associati ad un
                abbonamento valido che non hanno effettuato alcun accesso nel periodo dato.
                                                                             Progetto P.20220610
