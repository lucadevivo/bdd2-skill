# BD2_2019-11-07_TravelPlan

> Fonte: `BD2_2019-11-07_TravelPlan.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina.

---

Si vuole progettare e realizzare TravelPlan, un sistema per la creazione e la condivisione di
         Itinerari di viaggio.
         Gli utenti di TravelPlan utilizzano il sistema per organizzare viaggi ed unirsi a viaggi organizzati
         da altri utenti.
         Di ogni utente interessa conoscere il nome, il cognome, l’indirizzo email, la città di provenienza
         e la data di iscrizione.
         Ogni utente può creare viaggi in qualità di organizzatore; dei viaggi interessa il nome, il numero
         minimo e il numero massimo di partecipanti. Gli utenti di TravelPlan possono quindi prendere parte
         ai viaggi organizzati dagli altri utenti.
         Un viaggio è associato ad un certo numero di attività quali visite, pasti, tour, trasporti e per-
         nottamenti. Di ogni attività interessa conoscere il nome, l’istante di inizio, la durata, il prezzo, il
         luogo in cui si tiene, delle informazioni testuali ed eventualmente un insieme di codici identificativi
         di biglietti/prenotazioni relativi all’attività.
         Di ogni luogo interessa conoscere l’indirizzo, la città, la regione e la nazione.
         Per facilitare la pianificazione, il sistema deve permettere di creare attività composte, cioè che
         raggruppano più attività semplici. Ad esempio, l’attività “tour gastronomico del centro storico”
         includerà la visita di due piazze, un percorso a piedi, un pasto al ristorante e la visita di una cantina.
         Il sistema deve poter rappresentare gli spostamenti (con qualsiasi mezzo: treno, aereo, nave,
         bicicletta, a piedi, ecc.) come attività, delle quali è di interesse conoscere sia il luogo di partenza
         che quello di arrivo.
         I pernottamenti sono attività particolari, poiché il sistema non deve poter rappresentare più di
         un pernottamento al giorno per ogni utente che partecipa a un viaggio.
         Poiché può succedere che gli utenti che partecipano a uno stesso viaggio non prendano tutti
         parte alle stesse attività (p.es., due sotto-gruppi possono alloggiare in hotel diversi), il sistema deve
         permettere di specificare, per ogni attività inclusa in un viaggio, gli utenti che vi partecipano. Se
         per una certa attività non è specificato nessun utente, si assume che tutti i partecipanti al viaggio
         ne facciano parte.

         I partecipanti ad un viaggio possono dare un feedback all’organizzazione del viaggio, assegnando
         un voto da 1 a 5.
         TravelPlan prevede un sistema di punteggi per i propri utenti, in base alle valutazioni ricevute
         viaggi da loro organizzati. Il punteggio p di un utente è così calcolato: p è uguale a 0 se la
         media aritmetica dei voti ricevuti è  ≤ 3, altrimenti p è uguale alla parte intera inferiore del 10% del
         numero di feedback ricevuti con voto ≥ 4.
         Il sistema deve offrire le seguenti funzionalità agli utenti registrati:
            1.
            Creare viaggi in qualità di organizzatori e aggiungere a essi attività di vario tipo;
            2.
            Trovare tutti i viaggi che includono una certa destinazione in un certo intervallo di tempo;
            3.
            Trovare la/e città toccata/e dal maggior numero di viaggi in un certo intervallo di tempo;
            4.
            Calcolare, per ogni regione di una data nazione, il numero di viaggi organizzati in un dato
            Periodo di tempo che toccano quella regione.
            5.
            Dato un budget minimo, un budget massimo, un insieme di regioni, un periodo di tempo e un
            punteggio, calcolare l’insieme dei viaggi che hanno un budget nell’intervallo richiesto, toccano
            Almeno una delle regioni date, si svolgono completamente all’interno del periodo dato e sono
            Organizzati da un utente con un punteggio pari o superiore a quello dato.
