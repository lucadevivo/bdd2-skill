# 15 - My Precious

> Fonte: `(15) My Precious - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20220909 (P.20220909)
                                 My Precious
                                                                             Progetto P.20220909

    My Precious
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20220909

    My Precious
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare My Precious, un sistema di gestione di opere d’arte e
              delle relative esposizioni per conto di un museo, finalizzato all’utilizzo interno.
              Tramite il sistema, si vuole che i responsabili del museo possano gestire il patrimonio
              artistico e organizzare delle esposizioni delle opere e che il management possa ottenere
              delle statistiche sulle visite.
                                                                             Progetto P.20220909

    My Precious
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              Gli utenti di My Precious sono i responsabili della gestione delle opere d’arte del museo
              e dell’organizzazione delle esposizioni.
           È di interesse rappresentare le opere a disposizione del museo, con il nome, la catego-
           ria (p.es., dipinto, scultura, mosaico, manoscritto, ecc.), l’autore, l’anno di realizzazione,
           la tecnica (se rilevante) e le correnti artistiche alle quali è associata.
              Di un autore interessano il nome d’arte, il luogo e la data di nascita, la data di morte
              e le opere realizzate che sono di proprietà del museo.
           Un’opera di proprietà del museo può essere presa in prestito da o data in prestito
           a un altro museo. Di un’opera in prestito interessa il museo di origine o destinazione,
           la data di inizio del prestito e quella di fine. Alcune opere, per via di un’importanza
           particolare o poiché troppo delicate, non possono essere date in prestito.
           Alcune opere di proprietà del museo possono essere oggetto di restauri, nel qual
           caso interessa il periodo di restauro; un’opera in restauro non può essere esposta nel
           museo. Il sistema deve mantenere le informazioni riguardo a tutti i restauri ai quali è
           stata sottoposta ogni opera di proprietà del museo, da quando è di sua proprietà.
              I responsabili della gestione del patrimonio del museo organizzano le esposizioni delle
              opere, le quali possono essere permanenti oppure temporanee.
           Le esposizioni permanenti espongono le opere di proprietà del museo e le raggrup-
           pano, ad esempio, per periodo storico.
           Le esposizioni temporanee, invece, sono esposizioni speciali che si tengono per periodi
           di tempo più o meno brevi (in genere qualche mese) e hanno un tema particolare, come
           un artista, un gruppo di artisti, una corrente artistica o un periodo storico.
           Di un’esposizione è di interesse conoscere la sezione del museo nella quale ha luogo
           e le opere coinvolte.
           Di un’esposizione temporanea interessa il nome e il periodo di tempo nel quale si
           tiene.
                                                                             Progetto P.20220909

    My Precious
    2. Specifica dei Requisiti
              Il museo vende diversi tipi di biglietto. Ogni biglietto può essere utilizzato solamente
              nella data scelta al momento del suo acquisto.
                 Le tipologie di biglietto in vendita sono le seguenti:
                1. il biglietto full access, che dà accesso a tutte le esposizioni, permanenti e tempo-
                ranee;
                2. un biglietto valido per tutte e sole le esposizioni permanenti;
                3. un biglietto valido per tutte le esposizioni permanenti ed una sola esposizione
                temporanea, quest’ultima a scelta del visitatore.
              Il sistema deve offrire le seguenti funzionalità ai responsabili del patrimonio artistico
              e al management:
                1. inserimento e rimozione di opere d’arte;
                2. registrazione del restauro di un’opera d’arte;
                3. creazione di un’esposizione, con le opere relative;
                4. calcolare il numero dei biglietti venduti in un dato giorno per ognuna delle diverse
                tipologie;
                5. dato un periodo di tempo, il numero medio di biglietti (di qualsivoglia tipologia)
                venduti (media giornaliera) nel periodo dato;
                6. dato un periodo di tempo, calcolare un resoconto che contenga, per ognuna delle
                correnti artistiche note, il numero di artisti che ha realizzato almeno un’opera di
                proprietà del museo appartenente a quella corrente, nel periodo dato;
                7. dato un periodo di tempo, calcolare l’esposizione temporanea per la quale sono
                stati venduti più biglietti nel periodo (considerando tutti i tipi di biglietto rilevanti);
                8. dato un artista e un periodo di tempo, calcolare le opere realizzate dall’artista ed
                in possesso del museo che non sono state oggetto di restauri nel periodo dato;
                9. trovare le opere attualmente in restauro che non sono esposte da più tempo,
                insieme alla data di loro ultima esposizione.
                                                                             Progetto P.20220909
