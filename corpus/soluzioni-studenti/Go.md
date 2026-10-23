# Go

> Fonte: `Go.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Go (gruppo 42)
         Requisiti
         I dati di interesse per il sistema sono Giocatori, Tornei e Partite.
           1. Giocatore
               1.1 nome
               1.2 cognome
               1.3 nickname - il nickname univoco
               1.4 rank dichiarato - intero positivo
               1.5 indirizzo
           2. Partita
               2.1 data - la data in cui si `e disputata
               2.2 luogo
               2.3 regole - cinesi o giapponesi
               2.4 giocatore pietre bianche
               2.5 giocatore pietre nere
               2.6 komi - fattore di decifit, x ∈[0, 10]
               2.7 esito - se ha vinto il bianco o il nero, rappresentato come rinuncia o coppia di punteggi
               2.8 eventuale torneo di riferimento
           3. Torneo
               3.1 partite associate
               3.2 nome
               3.3 descrizione
               3.4 edizione - anno in cui si svolge

         Considerazioni
         Documenti di Specifica
         3.1
         Tipi di Dato
         Punteggio = {b : Int≥0, n : Int≥0}
         Komi = {Real ∈[0,10]}
         Regole = {cinese,giapponese}
         Rank = Int≥0
         Anno = (”19” or ”20”) concat [”00”,”99”]{1}
         Giocatore = {bianco,nero}
         UML
