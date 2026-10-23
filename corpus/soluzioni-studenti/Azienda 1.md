# Azienda 1

> Fonte: `Azienda 1.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Azienda 1 (gruppo 42)
                                                         The answer to the Ultimate Question of Life,
                                                         the Universe, and Everything
                                                             Douglas Adams
                                                             ”The Hitchhiker’s Guide to the Galaxy”
           Requisiti
           I dati di interesse per il sistema sono impiegati, dipartimenti, direttori dei dipartimenti e progetti
           aziendali.
           Impiegato
             1. Nome (include anche il doppio nome), cognome, data di nascita e stipendio attuale.
             2. Dipartimento a cui afferisce, con relativa data di afferenza (esattamente uno).
             3. La data di afferenza al dipartimento non pu`o essere precedente alla creazione dell’azienda.
             4. Ogni dipendente pu`o cambiare dipartimento, e vogliamo memorizzare lo storico dei dipartimenti in cui
             ha lavorato.
             5. L’afferenza con la data pi`u recente sar`a considerata quella corrente.
             6. Un impiegato pu`o dirigere pi`u di un dipartimento.
             7. Un dirigente non afferisce al dipartimento che dirige. Afferisce al dipartimento riservato ai dirigenti.
             8. L’impiegato pu`o partecipare a 0 o pi`u progetti (un nuovo impiegato non partecipa ancora a nessun
             progetto).
           Dipartimento
             1. Nome, telefono.
           Progetto
             1. Ad un progetto possono partecipare 0 o pi`u impiegati (potrebbe succedere che il progetto `e nuovo e
             non `e stato assegnato nessun impiegato).
             2. Il budget di un progetto non pu`o essere negativo.

           UML
