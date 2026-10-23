# 08 - Ristobook

> Fonte: `(08) - Ristobook - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20220506 (P.20220506)
                                    RistoBook
                                                                             Progetto P.20220506

    RistoBook
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20220506

    RistoBook
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare RistoBook, un’applicazione web per creare e gestire
              prenotazioni per ristoranti.
                                                                             Progetto P.20220506

    RistoBook
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              Il sistema deve permettere ai clienti di effettuare prenotazioni presso i ristoranti iscritti,
              usufruendo, eventualmente, di promozioni. I ristoratori, invece, possono iscriversi per
              registrare i propri ristoranti e gestire le loro prenotazioni e le loro promozioni.
           Dei clienti interessa conoscere il nome e l’indirizzo e-mail, mentre dei ristoranti in-
           teressa il nome, la partita IVA (una stringa numerica), l’indirizzo, la città e l’insieme
           di tipologie di cucina offerte (scelte da una lista tenuta sotto controllo dallo staff di
           RistoBook).
           I clienti possono prenotare presso un ristorante specificando il giorno, l’ora e il numero
           di commensali. Le prenotazioni dei clienti devono essere confermate (o rifiutate) dal
           personale incaricato dei rispettivi ristoranti, che devono poter accedere ad RistoBook
           tramite una interfaccia dedicata.
           Uno dei punti di forza del modello di business di RistoBook è la possibilità per
           i ristoranti di offrire e pubblicizzare scontistiche (dette promozioni). In particolare, i
           ristoratori devono poter definire una promozione specificando una percentuale di sconto
           sulle prenotazioni consumate in un certo periodo di tempo. Tali promozioni sono valide
           per al massimo un certo numero di coperti al giorno.
           Ad esempio, un ristorante potrebbe definire la seguente promozione: sconto del 20%
           sulle prenotazioni dalle 20 alle 22 da martedì 15 giugno 2022 a venerdì 18 giugno 2022,
           valido per al massimo 10 coperti al giorno. Un altro ristorante potrebbe definire invece
           una promozione del tipo: sconto del 25% sulle prenotazioni dalle 18 alle 19 di tutti i
           martedì e giovedì dal 1 ottobre al 31 dicembre 2022.
              Al momento della prenotazione, il cliente può scegliere una delle promozioni ancora
              disponibili (anche nessuna, se lo desidera).
           Il sistema deve permettere ai ristoratori e ai clienti di gestire lo stato delle prenotazio-
           ni. In particolare, quando una prenotazione viene creata, questa è nello stato “pendente”.
           Il ristoratore può scegliere se accettarla o rifiutarla. Quando il cliente usufruisce effettiva-
           mente della prenotazione, questa viene contrassegnata come “completata”. Se, invece, il
                                                                             Progetto P.20220506

    RistoBook
    2. Specifica dei Requisiti
              cliente non dovesse presentarsi al ristorante, il ristoratore contrassegnerà la prenotazione
              come “non utilizzata”. Inoltre, in ogni momento (prima del giorno ed ora prenotati) i
              clienti possono annullare le proprie prenotazioni, anche se già accettate. Infine, in caso
              di tutto esaurito (o per altre ragioni, ad es. giorni di chiusura), il responsabile di un
              ristorante deve poter chiudere le prenotazioni per un certo lasso di tempo (ad es., una
              certa data e fascia oraria, o un’intera settimana): da quel momento in poi, RistoBook
              non consentirà più ai clienti di richiedere prenotazioni in quel lasso di tempo (a meno
              che il ristoratore non le riapra).
                 Il sistema deve offrire, oltre quelle già descritte, le seguenti funzionalità ai suoi attori:
                 • Il sistema deve permettere ristoratori di RistoBook di calcolare alcune statistiche
                 di utilizzo delle loro promozioni. In particolare, dato un periodo di tempo, Risto-
                 Book deve permettere calcolare, per ogni promozione del ristorante considerato, il
                 numero medio di clienti al giorno (dove la media è calcolata sui giorni di validità
                 della promozione) che ha utilizzato quella promozione in una prenotazione.
                 • Data una città x, un insieme di tipologie di cucina C, un tasso di sconto minimo
                 s ed una data d, i clienti devono poter trovare quali sono i ristoranti nella città x
                 che offrono almeno una delle tipologie di cucina in C e prevedono promozioni con
                 sconti di tasso almeno s nella data d ancora utilizzabili per il numero di coperti
                 che sono interessati a prenotare.
                                                                             Progetto P.20220506
