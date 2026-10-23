# E.A.1.11 - Officine 1

> Fonte: `Esercitazione E.A.1.11 - Officine 1 - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione A.1.11 (E.A.1.11)
                     Analisi dei requisiti
                     Analisi dei requisiti mediante UML
                                     Officine 1
                                       – Solo Testo –
                                                                            Esercitazione E.A.1.11

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Officine 1
                           Obiettivi
              Si vuole sviluppare un sistema informativo per la gestione dei dati di una catena di
              officine.
              Durante la fase di raccolta dei requisiti è stata prodotta la seguente specifica dei
              requisiti.
                 Si chiede di iniziare la fase di Analisi Concettuale ed in particolare di:
                1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze
                e produrre un elenco numerato di requisiti il meno ambiguo possibile
                2. produrre un diagramma UML delle classi concettuale che modelli i dati di in-
                teresse, utilizzando solo i costrutti di classe, associazione, attributo, vincoli di
                identificazione di classe, generalizzazione, operazioni di classe
                3. produrre la relativa specifica dei tipi di dato in caso si siano definiti nuovi tipi di
                dato concettuali e le specifiche informali di eventuali classi con operazioni.
                                                                            Esercitazione E.A.1.11

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Officine 1
    1. Specifica dei Requisiti
                 Specifica dei Requisiti
              I dati di interesse per il sistema sono quelli relativi alle officine della catena, i relativi
              dipendenti e direttori, e quelli relativi alle riparazioni dei veicoli.
              Di ogni officina della catena interessano il nome, l’indirizzo, il numero di dipendenti,
              i dipendenti con il relativo numero di anni di servizio ed il direttore.
              Dei dipendenti e dei direttori interessano il nome, il codice fiscale, l’indirizzo e il
              numero di telefono; inoltre dei direttori interessa anche la data di nascita.
              Per quanto riguarda le riparazioni dei veicoli, sono dati di interesse il codice, il vei-
              colo (modello, tipo, targa, anno di immatricolazione e proprietario), la data ed ora di
              accettazione e quella di riconsegna (per le riparazioni terminate).
                 Infine, dei proprietari dei veicoli interessano nome, codice fiscale, indirizzo e telefono.
                                                                            Esercitazione E.A.1.11
