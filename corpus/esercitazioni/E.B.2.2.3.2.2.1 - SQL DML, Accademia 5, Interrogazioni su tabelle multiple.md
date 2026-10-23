# E.B.2.2.3.2.2.1 - SQL DML, Accademia 5, Interrogazioni su tabelle multiple

> Fonte: `Esercitazione E.B.2.2.3.2.2.1 - SQL DML, Accademia 5, Interrogazioni su tabelle multiple - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.2.1 (E.B.2.2.3.2.2.1)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                     Interrogazioni
                     Interrogazioni su Tabelle
                                 Multiple
                                 Accademia 5
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Accademia.
                                                                       Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
    1. Base Dati e Interrogazioni
                 Base Dati e Interrogazioni
              Il database Accademia è definito sul seguente insieme di domini e sul seguente schema
              relazionale con vincoli.
              Definizione dei domini
                     • Strutturato
                     enum (’Ricercatore’, ’Professore Associato’, ’Professore Ordinario’)
                     • LavoroProgetto
                     enum (’Ricerca e Sviluppo’, ’Dimostrazione’, ’Management’, ’Altro’)
                     • LavoroNonProgettuale
                     enum (’Didattica’, ’Ricerca’, ’Missione’, ’Incontro Dipartimentale’, ’Incontro
                     Accademico’, ’Altro’)
                     • CausaAssenza
                     enum (’Chiusura Universitaria’, ’Maternita’, ’Malattia’)
                     • PosInteger
                     integer ≥0
                     • StringaM
                     varchar(100)
                     • NumeroOre
                     integer tra 0 e 8
                     • Denaro
                     real ≥0
                                                                      Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
    1. Base Dati e Interrogazioni
              Schema relazionale con vincoli della base dati
                   Persona (id: PosInteger, nome: StringaM, cognome: StringaM, posizione: Strut-
                   turato, stipendio: Denaro)
                   Progetto (id: PosInteger, nome: StringaM, inizio: date, fine: date, budget:
                   Denaro)
                    [VincoloDB.1]
                    altra chiave: (nome)
                    [VincoloDB.2]
                    ennupla: inizio < fine
                   WP (progetto: PosInteger, id: PosInteger, nome: StringaM, inizio: date, fine:
                   date)
                    [VincoloDB.3]
                    ennupla: inizio < fine
                    [VincoloDB.4]
                    altra chiave: (progetto, nome)
                    [VincoloDB.5]
                    foreign key: progetto references Progetto(id)
                   AttivitaProgetto (id: PosInteger, persona: PosInteger, progetto: PosInteger,
                   wp: PosInteger, giorno: date, tipo: LavoroProgetto, oreDurata: NumeroOre)
                    [VincoloDB.6]
                    foreign key: persona references Persona(id)
                    [VincoloDB.7]
                    foreign key: (progetto, wp) references WP(progetto, id)
                   AttivitaNonProgettuale (id: PosInteger, persona: PosInteger, tipo: Lavoro-
                   NonProgettuale, giorno: date, oreDurata: NumeroOre)
                    [VincoloDB.8]
                    foreign key: persona references Persona(id)
                   Assenza (id: PosInteger, persona: PosInteger, tipo: CausaAssenza, giorno: date)
                    [VincoloDB.9]
                    altra chiave: persona, giorno
                    [VincoloDB.10]
                    foreign key: persona references Persona(id)
                                                                      Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
                ‘Pegasus’?
                2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
                una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
                3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
                una attività nel progetto ‘Pegasus’?
                4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
                fatto almeno una assenza per malattia?
                5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
                fatto più di una assenza per malattia?
                6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
                un impegno per didattica?
                7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
                impegno per didattica?
                8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
                attività progettuali che attività non progettuali?
                9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
                attività progettuali che attività non progettuali? Si richiede anche di proiettare il
                giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
                entrambe le attività.
               10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
               assenti e hanno attività progettuali?
               11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
               assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
               nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
               12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
                                                                      Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Accademia disponibile nel materiale
              didattico del corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Quali
              sono
              i l
              nome ,
              l a
              data
              d i
              i n i z i o
              e
              l a
              data
              d i
              f i n e
              d e i WP d e l
              progetto
              " Pegasus "?
              i d
              |
              nome
              |
              i n i z i o
              |
              f i n e
              −−−−+−−−−−−+−−−−−−−−−−−−+−−−−−−−−−−−−
              | WP1
              |
              2012−01−01
              |
              2012−12−31
              | WP2
              |
              2012−01−01
              |
              2012−12−31
              | WP3
              |
              2013−01−01
              |
              2013−12−31
              (3
              rows )
              2)
              Quali
              sono
              i l
              nome ,
              i l
              cognome e
              l a
              p o s i z i o n e
              d e g l i
              s t r u t t u r a t i
              che hanno almeno una
              a t t i v i t a ’
              n e l
              progetto
              " Pegasus " ,
              o r d i n a t i
              per
              cognome
              d e c r e s c e n t e ?
              i d
              |
              nome
              |
              cognome
              |
              p o s i z i o n e
              −−−−+−−−−−−−−−+−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−
              |
              Ginevra
              |
              Riva
              |
              P r o f e s s o r e
              O r d i n a r i o
              |
              Asia
              |
              Giordano
              |
              P r o f e s s o r e
              O r d i n a r i o
              |
              Barbara
              |
              Burso
              |
              R i c e r c a t o r e
              |
              Anna
              |
              Bianchi
              |
              R i c e r c a t o r e
              (4
              rows )
              3)
              Quali
              sono
              i l
              nome ,
              i l
              cognome e
              l a
              p o s i z i o n e
              d e g l i
              s t r u t t u r a t i
              che hanno
              piu ’
              d i
              una
              a t t i v i t a ’
              n e l
              progetto
              " Pegasus "?
              i d
              |
              nome
              |
              cognome
              |
              p o s i z i o n e
              −−−−+−−−−−−+−−−−−−−−−+−−−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              R i c e r c a t o r e
              (1 row )
              4)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e i
              P r o f e s s o r i
              O r d i n a r i
              che hanno
              f a t t o
              almeno una
              assenza
              per
              m a l a t t i a ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−+−−−−−−−−−−
              |
              Asia
              |
              Giordano
              |
              Ginevra
              |
              Riva
              (2
              rows )
              5)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e i
              P r o f e s s o r i
              O r d i n a r i
              che hanno
              f a t t o
              piu ’
              d i
              una
              assenza
              per
              m a l a t t i a ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−+−−−−−−−−−
              |
              Ginevra
              |
              Riva
              (1 row )
              6)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e i
              R i c e r c a t o r i
              che hanno
              almeno un impegno
              per
              d i d a t t i c a ?
               i d
               |
               nome
               |
               cognome
                                                                            Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
    1. Base Dati e Interrogazioni
              −−−−+−−−−−−−−−+−−−−−−−−−
              |
              Barbara
              |
              Burso
              |
              Mario
              |
              Rossi
              |
              Anna
              |
              Bianchi
              (3
              rows )
              7)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e i
              R i c e r c a t o r i
              che hanno
              piu ’
              d i
              un impegno
              per
              d i d a t t i c a ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−+−−−−−−−−−
              |
              Barbara
              |
              Burso
              (1 row )
              8)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e g l i
              s t r u t t u r a t i
              che
              n e l l o
              s t e s s o
              giorno
              hanno
              s i a
              a t t i v i t a ’
              p r o g e t t u a l i
              che
              a t t i v i t Ã
              non
              p r o g e t t u a l i ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−+−−−−−−−−−
              |
              Anna
              |
              Bianchi
              (1 row )
              9)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e g l i
              s t r u t t u r a t i
              che
              n e l l o
              s t e s s o
              giorno
              hanno
              s i a
              a t t i v i t a ’
              p r o g e t t u a l i
              che
              a t t i v i t a ’
              non
              p r o g e t t u a l i ?
              Si
              r i c h i e d e
              d i
              r e s t i t u i r e
              anche
              i l
              giorno ,
              i l
              nome d e l
              progetto ,
              i l
              t i p o
              d e l l ’ a t t i v i t a ’
              non
              p r o g e t t u a l e
              e
              l a
              durata
              i n
              ore
              d i
              entrambe
              l e
              a t t i v i t a ’ .
              i d
              |
              nome
              |
              cognome
              |
              giorno
              |
              p r j
              |
              h_prj
              |
              att_noprj
              |
              h_noprj
              −−−−+−−−−−−+−−−−−−−−−+−−−−−−−−−−−−+−−−−−−−−−+−−−−−−−+−−−−−−−−−−−+−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              2012−04−18
              |
              Pegasus
              |
              |
              D i d a t t i c a
              |
              (1 row )
              10)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e g l i
              s t r u t t u r a t i
              che
              n e l l o
              s t e s s o
              giorno
              sono
              a s s e n t i
              e hanno
              a t t i v i t a ’
              p r o g e t t u a l i ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−+−−−−−−−−−
              |
              Anna
              |
              Bianchi
              (1 row )
              11)
              Quali
              sono
              i l
              nome e
              i l
              cognome
              d e g l i
              s t r u t t u r a t i
              che
              n e l l o
              s t e s s o
              giorno
              sono
              a s s e n t i
              e hanno
              a t t i v i t a ’
              p r o g e t t u a l i ?
              Si
              r i c h i e d e
              anche
              d i
              p r o i e t t a r e
              i l
              giorno ,
              i l
              nome
              d e l
              progetto ,
              l a
              causa
              d i
              assenza
              e
              l a
              durata
              i n
              ore
              d e l l a
              a t t i v i t a ’
              p r o g e t t u a l e .
              i d
              |
              nome
              |
              cognome
              |
              giorno
              |
              causa_ass
              |
              progetto
              |
              ore_att_prj
              −−−−+−−−−−−+−−−−−−−−−+−−−−−−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−+−−−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              2012−04−18
              |
              Malattia
              |
              Pegasus
              |
              (1 row )
              12)
              Quali
              sono
              i WP che hanno
              l o
              s t e s s o
              nome , ma appartengono
              a
              p r o g e t t i
              d i v e r s i ?
              nome
              −−−−−−
               WP1
               WP2
               WP3
                                                                            Esercitazione E.B.2.2.3.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Accademia 5
    1. Base Dati e Interrogazioni
              (3
              rows )
                                                                      Esercitazione E.B.2.2.3.2.2.1
