# E.A.1.10 - Accademia 2

> Fonte: `Esercitazione E.A.1.10 - Accademia 2 - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione A.1.10 (E.A.1.10)
                     Analisi dei requisiti
                     Analisi dei requisiti mediante UML
                                 Accademia 2
                                       – Solo Testo –
                                                                            Esercitazione E.A.1.10

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Accademia 2
                           Obiettivi
              Si vuole progettare un sistema informativo per la gestione delle tabelle orarie relative al
              ruolo di docente universitario.
              Durante la fase di raccolta dei requisiti è stata prodotta la seguente specifica dei
              requisiti.
                 Si chiede di iniziare la fase di Analisi Concettuale ed in particolare di:
                1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze
                e produrre un elenco numerato di requisiti il meno ambiguo possibile
                2. produrre un diagramma UML delle classi concettuale che modelli i dati di in-
                teresse, utilizzando solo i costrutti di classe, associazione, attributo, vincoli di
                identificazione di classe, generalizzazione
                3. produrre la relativa specifica dei tipi di dato in caso si siano definiti nuovi tipi di
                dato concettuali.
                                                                            Esercitazione E.A.1.10

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Accademia 2
    1. Specifica dei Requisiti
                 Specifica dei Requisiti
              I dati di interesse per il sistema sono i docenti universitari, i progetti di ricerca e le
              attività dei docenti.
              Di ogni docente interessa conoscere il nome, il cognome, il luogo e la data di nasci-
              ta, la matricola e la posizione universitaria (una tra: ricercatore, professore associato,
              professore ordinario).
              Dei progetti interessa il nome, un acronimo, la data di inizio, la data di fine e i
              docenti che vi partecipano.
              Un progetto è composto da molti Work Package (WP). Oltre al progetto a cui fa
              riferimento, del WP interessa sapere il nome, la data di inizio e la data di fine.
              Il sistema deve permettere ai docenti di registrare impegni di diverso tipo tra: as-
              senza (per chiusura universitaria, malattia, gravidanza, etc.), attività legate a impegni
              istituzionali (didattica, ricerca, missione, consiglio di dipartimento, consiglio di area di-
              dattica, etc.), attività legate a impegni progettuali (Ricerca e Sviluppo, Dimostrazione,
              Management, etc.).
              Degli impegni interessa sapere il giorno in cui avvengono, la durata e la tipologia
              di impegno con relativa motivazione. Si noti che alcuni impegni (ad es., impegno per
              didattica oppure alcuni tipi di assenza) possono occupare solo parte di una giornata
              lavorativa, pertanto la loro durata va misurata in giorni; altri impegni ed altre tipologie
              di assenza (ad es., assenza per malattia) occupano intere giornate, e la loro durata,
              dunque, va misurata in giorni.
                                                                            Esercitazione E.A.1.10
