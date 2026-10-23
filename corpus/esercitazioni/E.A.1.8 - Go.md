# E.A.1.8 - Go

> Fonte: `Esercitazione E.A.1.8 - Go - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione A.1.8 (E.A.1.8)
                     Analisi dei requisiti
                     Analisi dei requisiti mediante UML
                                              Go
                                       – Solo Testo –
                                                                             Esercitazione E.A.1.8

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Go
                           Obiettivi
              Si vuole progettare un sistema informativo per la gestione di partite singole di tornei del
              gioco da tavolo Go.
              Durante la fase di raccolta dei requisiti è stata prodotta la seguente specifica dei
              requisiti.
                 Si chiede di iniziare la fase di Analisi Concettuale ed in particolare di:
                1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze
                e produrre un elenco numerato di requisiti il meno ambiguo possibile
                2. produrre un diagramma UML delle classi concettuale che modelli i dati di in-
                teresse, utilizzando solo i costrutti di classe, associazione, attributo, vincolo di
                identificazione di classe, generalizzazione
                3. produrre la relativa specifica dei tipi di dato in caso si siano definiti nuovi tipi di
                dato concettuali.
                                                                             Esercitazione E.A.1.8

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Go
    1. Specifica dei Requisiti
                 Specifica dei Requisiti
              I dati di interesse per il sistema sono i giocatori, i tornei e le partite.
              Di un giocatore interessa conoscere il nick-name (univoco), il nome, il cognome,
              l’indirizzo e il rank dichiarato (un intero positivo).
              Due giocatori si possono sfidare in una partita. Di una partita interessa sapere la
              data e il luogo in cui è giocata, le regole di conteggio usate (giapponesi o cinesi), quale
              giocatore gioca con le pietre bianche e quale con le pietre nere, il fattore di deficit
              chiamato komi (numero reale non negativo, tra 0 e 10) e l’esito. L’esito può essere
              rappresentato da una rinuncia di uno dei due giocatori, oppure da una coppia di punteggi
              di bianco e di nero (interi non negativi).
              Le partite si possono anche riferire a un torneo.
              Di un torneo interessa sapere il nome, una descrizione testuale, e l’edizione in termini
              dell’anno in cui si svolge.
                                                                             Esercitazione E.A.1.8
