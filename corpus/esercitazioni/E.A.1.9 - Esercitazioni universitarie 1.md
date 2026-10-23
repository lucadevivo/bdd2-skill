# E.A.1.9 - Esercitazioni universitarie 1

> Fonte: `Esercitazione E.A.1.9 - Esercitazioni universitarie 1 - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione A.1.9 (E.A.1.9)
             Analisi dei requisiti
             Analisi dei requisiti mediante UML
             Esercitazioni Universitarie 1
                                       – Solo Testo –
                                                                             Esercitazione E.A.1.9

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Esercitazioni Universitarie 1
                           Obiettivi
              Si vuole progettare un sistema informativo per tenere traccia delle esercitazioni svolte
              durante le lezioni di insegnamenti universitari.
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
                                                                             Esercitazione E.A.1.9

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Esercitazioni Universitarie 1
    1. Specifica dei Requisiti
                 Specifica dei Requisiti
              I dati di interesse per il sistema sono insegnamenti universitari e le esercitazioni ivi
              erogate.
              Di ogni insegnamento interessa sapere il nome, il relativo numero di crediti formativi
              universitari, i docenti (possono essere più d’uno) e l’anno accademico di riferimento. Dei
              docenti interessa matricola, nome e cognome.
              Un insegnamento può prevedere diverse esercitazioni, ognuna erogata in una certa
              data e composta da molti esercizi, scelti tra quelli disponibili nel sistema.
              Di ogni esercizio, il sistema deve rappresentare il testo e la o le relative soluzioni
              disponibili (anche nessuna). Per ogni esercizio presentato in una esercitazione, il sistema
              deve mantenere l’informazione circa il fatto che questo sia stato solo presentato (per
              essere svolto in modo autonomo dagli studenti), oppure anche risolto in aula (e, in
              questo caso, quale delle soluzioni disponibili è stata mostrata).
                                                                             Esercitazione E.A.1.9
