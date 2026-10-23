# E.A.1.7 - Impiegati e studenti

> Fonte: `Esercitazione E.A.1.7 - Impiegati e studenti - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione A.1.7 (E.A.1.7)
                     Analisi dei requisiti
                     Analisi dei requisiti mediante UML
                      Impiegati e Studenti
                                       – Solo Testo –
                                                                             Esercitazione E.A.1.7

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Impiegati e Studenti
                           Obiettivi
              Si vuole sviluppare un sistema informativo per la gestione dei dati anagrafici di alcune
              tipologie di persone. Durante la fase di raccolta dei requisiti è stata prodotta la seguente
              specifica dei requisiti.
                 Si chiede di iniziare la fase di Analisi Concettuale ed in particolare di:
                1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze
                e produrre un elenco numerato di requisiti il meno ambiguo possibile
                2. produrre un diagramma UML delle classi concettuale che modelli i dati di in-
                teresse, utilizzando solo i costrutti di classe, associazione, attributo, vincolo di
                identificazione di classe, generalizzazione
                3. produrre la relativa specifica dei tipi di dato in caso si siano definiti nuovi tipi di
                dato concettuali.
                                                                             Esercitazione E.A.1.7

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Impiegati e Studenti
    1. Specifica dei Requisiti
                 Specifica dei Requisiti
              I dati di interesse per il sistema sono i dati anagrafici di alcune tipologie di persone.
              Di ogni persona interessa mantenere nome, cognome, codice fiscale e data di nascita.
              Degli uomini interessa mantenere anche la posizione militare, mentre delle donne si vuole
              mantenere anche il numero di maternità.
              Alcune persone sono impiegati. Di questi interessa rappresentare lo stipendio e il
              ruolo, che può essere di segretario, direttore, oppure di progettista. Alcuni progettisti
              sono responsabili di progetto. Di questi interessa mantenere la collezione dei progetti di
              cui sono responsabili. Di tali progetti interessa il nome.
              Alcune persone sono studenti. Di questi interessa rappresentare anche il numero di
              matricola.
              Nel dominio di interesse gli studenti non sono mai impiegati, ma esistono persone
              che non sono né impiegati né studenti.
                                                                             Esercitazione E.A.1.7
