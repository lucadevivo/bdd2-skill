# E.A.1.5 - Voli aerei 2

> Fonte: `Esercitazione E.A.1.5 - Voli aerei 2 - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione A.1.5 (E.A.1.5)
                     Analisi dei requisiti
                     Analisi dei requisiti mediante UML
                                  Voli Aerei 2
                                       – Solo Testo –
                                                                             Esercitazione E.A.1.5

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Voli Aerei 2
                           Obiettivi
              Si vuole sviluppare un sistema informativo per la gestione di dati relativi a voli aerei.
              Durante la fase di raccolta dei requisiti è stata prodotta la seguente specifica dei requisiti.
                 Si chiede di iniziare la fase di Analisi Concettuale ed in particolare di:
                1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze
                e produrre un elenco numerato di requisiti il meno ambiguo possibile
                2. produrre un diagramma UML delle classi concettuale che modelli i dati di interesse,
                utilizzando solo i costrutti di classe, associazione, attributo, generalizzazione tra
                classi
                3. produrre la relativa specifica dei tipi di dato in caso si siano definiti nuovi tipi di
                dato concettuali.
                                               Esercitazione E.A.1.5

    Analisi dei requisiti
    Analisi dei requisiti mediante UML
    Voli Aerei 2
    1. Specifica dei Requisiti
                 Specifica dei Requisiti
              I dati di interesse per il sistema sono voli, compagnie aeree ed aeroporti.
              Dei voli interessa rappresentare codice, durata, compagnia aerea ed aeroporti di
              partenza e arrivo.
              Degli aeroporti interessa rappresentare codice, nome, città (con nome e numero di
              abitanti) e nazione.
              Delle compagnie aeree interessa rappresentare nome, anno di fondazione, e la città
              in cui ha sede la direzione.
              Un tipo particolare di voli sono voli charter. Questi possono prevedere tappe interme-
              die in aeroporti. Delle tappe intermedie di un volo charter interessa mantenere l’ordine
              con cui esse si susseguono (ad esempio, un certo volo che parte da “Milano Linate” e
              arriva a “Palermo Punta Raisi”, prevede tappe intermedie prima nell’aeroporto di Bologna
              e poi in quello di Napoli). Dei voli charter interessa rappresentare anche il modello di
              velivolo usato.
                                               Esercitazione E.A.1.5
