# 05 - Out!

> Fonte: `(05) Progetto Out! - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20080918 (P.20080918)
                                           Out!
                                                                             Progetto P.20080918

    Out!
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20080918

    Out!
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare Out!, un sistema Web che consenta agli utenti di con-
              sultare il programma di diversi cinema e teatri cittadini, e di prenotare gli spettacoli a
              cui desiderano assistere.
                                                                             Progetto P.20080918

    Out!
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
           Out! deve consentire di mantenere informazioni su teatri e cinema e ogni altra sede di
           spettacoli associata al circuito. In particolare, di ogni sede interessa conoscere il nome
           e l’indirizzo. Le sedi possono essere provviste di più sale distinte, ognuna delle quali
           può ospitare uno spettacolo (ad es., cinema multisala, auditorium, etc.). Il sistema deve
           anche mantenere informazioni circa i posti a sedere nelle singole sale delle diverse sedi.
           Di ogni posto interessa conoscere i numeri di fila e colonna.
           Out!
           deve inoltre rappresentare gli spettacoli in programmazione presso i diversi
           enti aderenti al circuito. Di ogni spettacolo interessa conoscere il titolo, la tipologia
           (concerto, rappresentazione teatrale, oppure film), il relativo genere e gli artisti che
           effettuano la performance, oltre che le date, gli orari e le sedi (con relativa sala) in
           cui viene rappresentato. Si osservi infatti che uno stesso spettacolo viene tipicamente
           rappresentato più volte; anche se tipicamente uno spettacolo viene rappresentato sempre
           nella stessa sede, il sistema deve permettere anche di rappresentare spettacoli itineranti.
           Per generalità dunque, si faccia il modo che il sistema possa mantenere informazioni
           circa la sede e la sala per ogni data in cui un certo spettacolo viene rappresentato.
              Scopo principale del sistema è di consentire agli utenti di consultare il calendario degli
              spettacoli in programma, e di prenotare via web posti per gli spettacoli a cui desiderano
              assistere. In particolare, un utente deve poter usare il sistema per:
           1. Iscriversi al servizio, fornendo i propri dati di interesse (nome, cognome, codice
           fiscale) che il sistema deve memorizzare;
                2. Prenotare uno o più posti a prezzo pieno o ridotto di un dato settore per una
                data di uno spettacolo. I posti non sono liberi, pertanto il sistema deve assegnare,
                all’atto della prenotazione, un numero di posti sufficienti non ancora prenotati.1
              1Si assuma per semplicità che i posti vengano assegnati in modo completamente arbitrario, e non
              dal “migliore” al “peggiore”.
                                                                             Progetto P.20080918

    Out!
    2. Specifica dei Requisiti
                3. Consultare la lista degli spettacoli di una certa tipologia e genere (ad es., spettacoli
                teatrali/commedie) previsti in un certo giorno.
                4. Ricevere dal sistema suggerimenti di nuovi spettacoli da vedere. In particolare, si
                richiede che il sistema segnali ad un utente l’insieme degli spettacoli programmati
                nei successivi 7 giorni, che sono dello stesso genere (anche se di tipologia diversa)
                dell’ultimo spettacolo da egli prenotato.
                                                                             Progetto P.20080918
