# Accademia 1

> Fonte: `Accademia 1.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Accademia 1 (gruppo 42)
         Requisiti
         I dati di interesse per il sistema sono Docenti, Progetti ed Attivit`a.
           1. Docente
               1.1 Nome
               1.2 Cognome
               1.3 Data di nascita
               1.4 Matricola
               1.5 Posizione universitaria
               1.6 Progetti alla quale partecipa
           2. Progetto
               2.1 Nome
               2.2 Acronimo
               2.3 Codice progetto
               2.4 Data inizio
               2.5 Data fine
               2.6 Docenti coinvolti
               2.7 Work Package
                 2.7.1 Nome
                 2.7.2 Data inizio
                 2.7.3 Data fine
           3. Attivit`a
               3.1 Data
               3.2 Durata in ore
               3.3 tipologia impegno
               3.4 motivazione
         Considerazioni
         Ci sar`a una classe TipologiaAttivit`a, un Attivit`a pu`o essere di pi`u tipologie.
         Un Attivit`a pu`o coinvolgere pi`u Docenti.

         UML
