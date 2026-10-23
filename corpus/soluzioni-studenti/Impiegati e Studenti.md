# Impiegati e Studenti

> Fonte: `Impiegati e Studenti.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Impiegati e Studenti (gruppo 42)
         Requisiti
           1. Persona
               1.1 nome
               1.2 cognome
               1.3 codice fiscale
               1.4 data di nascita
               1.5 Sesso
                 1.5.1 Uomo
                 1.5.1.1 posizione militare - il ruolo che l’uomo assume nell’esercito
                 1.5.2 Donna
                 1.5.2.1 maternit`a - il numero di figli
               1.6 Impiego
                 1.6.1 stipendio in euro
                 1.6.2 Ruolo
                 1.6.2.1 segretario
                 1.6.2.2 direttore
                 1.6.2.3 progettista - insieme ai progetti di cui `e responsabile.
               1.7 Studente
                 1.7.1 matricola
           2. Progetto
               2.1 nome

         Documenti di Specifica
         2.1
         Tipi di Dato
         I tipi sono dati sottoforma di espressioni regolari :
         CF = [A-Z]{6} [0-9]{2} [A-Z]{1} [0-9]{2} [A-Z]{1} [0-9]{3} [A-Z]{1}
         UML
