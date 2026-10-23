# Esercitazioni Universitarie 1

> Fonte: `Esercitazioni Universitarie 1.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazioni Universitarie 1 (gruppo 42)
         Requisiti
         I dati di interesse per il sistema sono Insegnamenti ed Esercitazioni.
           1. Insegnamento
               1.1 nome
               1.2 crediti formativi
               1.3 docenti che lo erogano
               1.4 anno accademico
               1.5 esercitazioni dell’insegnamento
           2. Docente
               2.1 nome
               2.2 cognome
               2.3 matricola
           3. Esercitazione
               3.1 data
               3.2 esercizi coinvolti
           4. Esercizio
               4.1 testo
               4.2 soluzione
               4.3 se presentato oppure risolto in aula (con soluzione)
           5. Soluzione
               5.1 testo della soluzione e risultato

         Considerazioni
         Documenti di Specifica
         3.1
         Tipi di Dato
         Matricola = Stringa [0-9]{7}
         Anno = (”19” or ”20”) concat [”00”,”99”]{1}
         UML
