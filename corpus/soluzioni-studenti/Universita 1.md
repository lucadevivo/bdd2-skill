# Universita 1

> Fonte: `Universita 1.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Universit`a 1 (gruppo 42)
         Requisiti
         I dati di interesse per il sistema sono Studenti, Facolt`a, Professori e Corsi.
           1. Studente
               1.1 nome e cognome
               1.2 codice fiscale
               1.3 matricola
               1.4 data di nascita
               1.5 citt`a di nascita
               1.6 corso di laurea - Il/I corso/corsi alla quale lo studente `e iscritto.
               1.7 insegnamenti superati - Gli Insegnamenti che lo studente ha superato, uno stesso
               Insegnamento non pu`o essere superato pi`u di una volta.
           2. Professore
               2.1 nome e cognome
               2.2 data di nascita
               2.3 codice fiscale
               2.4 citt`a di nascita
               2.5 insegnamenti erogati - L’Insegnamento (o pi`u di uno) erogato da un Professore.
           3. Corso di Laurea
               3.1 nome
               3.2 facolt`a
           4. Facolt`a
               4.1 nome
           5. Insegnamento
               5.1 nome
               5.2 ore di lezione
               5.3 corsi alla quale appartiene - Il Corso di Laurea nel quale un Insegnamento viene
               erogato.
               5.4 codice - Serie di caratteri alfanumerici che identificano univocamente un Insegnamento.

         Considerazioni
         Sarebbe possibile considerare una generalizzazione delle classi Professore e Studente, denotata
         Persona, in quanto queste due condividono pi`u aspetti, come l’associazione ad una citt`a, o i
         vari attributi identificativi, differiscono esclusivamente nella loro relazione con Insegnamento.
         Sarebbe quindi corretto considerare Professore e Studente come sottoclassi di Persona.
         UML
