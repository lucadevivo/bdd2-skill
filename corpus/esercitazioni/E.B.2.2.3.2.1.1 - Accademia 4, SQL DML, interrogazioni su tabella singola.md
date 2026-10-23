# E.B.2.2.3.2.1.1 - Accademia 4, SQL DML, interrogazioni su tabella singola

> Fonte: `Esercitazione E.B.2.2.3.2.1.1 - Accademia 4, SQL DML, interrogazioni su tabella singola - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.1.1 (E.B.2.2.3.2.1.1)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
           Interrogazioni
           Interrogazioni su Singola Tabella
                                 Accademia 4
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              singole tabelle del database Accademia.
                                                                       Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
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
                                                                      Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
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
                                                                      Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni:
                1. Quali sono i cognomi distinti di tutti gli strutturati?
                2. Quali sono i Ricercatori (con nome e cognome)?
                3. Quali sono i Professori Associati il cui cognome comincia con la lettera ‘V’?
                4. Quali sono i Professori (sia Associati che Ordinari) il cui cognome comincia con la
                lettera ‘V’?
                5. Quali sono i Progetti già terminati alla data odierna?
                6. Quali sono i nomi di tutti i Progetti ordinati in ordine crescente di data di inizio?
                7. Quali sono i nomi dei WP ordinati in ordine crescente (per nome)?
                8. Quali sono (distinte) le cause di assenza di tutti gli strutturati?
                9. Quali sono (distinte) le tipologie di attività di progetto di tutti gli strutturati?
               10. Quali sono i giorni distinti nei quali del personale ha effettuato attività non pro-
               gettuali di tipo ‘Didattica’? Dare il risultato in ordine crescente.
                                                                      Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
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
              i
              cognomi
              d i s t i n t i
              d i
              t u t t i
              g l i
              s t r u t t u r a t i ?
              cognome
              −−−−−−−−−−−−−
               F e r r a r i
               V a l e n t i n i
               B a s i l e
               Burso
               Bianchi
               Martino
               Zante
               V i t a l i
               Rossi
               Verona
               Giordano
               Greco
              M a r t i n e l l i
              Riva
              Spada
              Costa
              Donati
              S p e n s i e r a t o
              Longo
              Quadro
              (20
              rows )
              2)
              Quali
              sono
              i
              R i c e r c a t o r i
              ( con nome e cognome ) ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−+−−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              Mario
              |
              Rossi
              |
              Barbara
              |
              Burso
              |
              Gino
              |
              Spada
              |
              Dario
              |
              B a s i l e
              |
              G i u l i a
              |
              Costa
              |
              Carla
              |
              M a r t i n e l l i
              (7
              rows )
              3)
              Quali
              sono
              i
              P r o f e s s o r i
              A s s o c i a t i
              i l
              c u i
              cognome
              comincia
              con
              l a
              l e t t e r a
              ’V’ ?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−+−−−−−−−−−−−
              |
              Andrea
              |
              Verona
              |
              Paolo
              |
              V a l e n t i n i
              (2
              rows )
              4)
              Quali
              sono
              i
              P r o f e s s o r i
              ( s i a
              A s s o c i a t i
              che
              O r d i n a r i )
              i l
              c u i
              cognome
              comincia
              con
              l a
              l e t t e r a
              ’V’ ?
               i d
               |
               nome
               |
               cognome
                                                                            Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
    1. Base Dati e Interrogazioni
              −−−−+−−−−−−−−−−+−−−−−−−−−−−
              |
              Andrea
              |
              Verona
              |
              Leonardo
              |
              V i t a l i
              |
              Paolo
              |
              V a l e n t i n i
              (3
              rows )
              5)
              Quali
              sono
              i
              P r o g e t t i
              gia ’
              t e r m i n a t i
              a l l a
              data
              odierna ?
              i d
              |
              nome
              |
              i n i z i o
              |
              f i n e
              |
              budget
              −−−−+−−−−−−−−−−−−−−−+−−−−−−−−−−−−+−−−−−−−−−−−−+−−−−−−−−
              |
              Artemide
              |
              2000−01−01
              |
              2002−12−31
              |
              |
              Pegasus
              |
              2012−01−01
              |
              2014−12−31
              |
              |
              WineSharing
              |
              1999−01−01
              |
              2003−12−31
              |
              |
              Simap
              |
              2010−02−01
              |
              2014−03−17
              |
              |
              DropDiscovery
              |
              2010−09−13
              |
              2013−01−20
              |
              (5
              rows )
              6)
              Quali
              sono
              i
              nomi
              d i
              t u t t i
              i
              P r o g e t t i
              o r d i n a t i
              i n
              o r d i n e
              c r e s c e n t e
              d i
              data
              d i
              i n i z i o ?
              i d
              |
              nome
              −−−−+−−−−−−−−−−−−−−−
              |
              WineSharing
              |
              Artemide
              |
              Simap
              |
              DropDiscovery
              |
              Pegasus
              (5
              rows )
              7)
              Quali
              sono
              i
              nomi
              d e i WP o r d i n a t i
              i n
              o r d i n e
              c r e s c e n t e
              ( per nome) ?
              i d
              |
              nome
              −−−−+−−−−−−−−−−−−−−−−−−
              |
              Dissemination
              |
              Main
              A c t i v i t y
              |
              Main
              Research
              |
              State
              of
              the
              Art
              | WP1
              | WP1
              | WP2
              | WP2
              | WP3
              | WP3
              (10
              rows )
              8)
              Quali
              sono
              ( d i s t i n t e )
              l e
              cause
              d i
              assenza
              d i
              t u t t i
              g l i
              s t r u t t u r a t i ?
              t i p o
              −−−−−−−−−−−−−−−−−−−−−−−−
              Maternita
              Chiusura
              U n i v e r s i t a r i a
              Malattia
              (3
              rows )
              9)
              Quali
              sono
              ( d i s t i n t e )
              l e
              t i p o l o g i e
              d i
              a t t i v i t a ’
              d i
              progetto
              d i
              t u t t i
              g l i
              s t r u t t u r a t i ?
              t i p o
              −−−−−−−−−−−−−−−−−−−−
               Ricerca
               e
               Sviluppo
                                                                            Esercitazione E.B.2.2.3.2.1.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Singola Tabella
    Accademia 4
    1. Base Dati e Interrogazioni
               Management
              Dimostrazione
              A l t r o
              (4
              rows )
              10)
              Quali
              sono
              i
              g i o r n i
              d i s t i n t i
              n e i
              q u a l i
              d e l
              p e r s o n a l e
              ha
              e f f e t t u a t o
              a t t i v i t a ’
              non
              p r o g e t t u a l i
              d i
              t i p o
              ’ Didattica ’ ?
              Dare
              i l
              r i s u l t a t o
              i n
              o r d i n e
              c r e s c e n t e .
              giorno
              −−−−−−−−−−−−
              2011−03−15
              2011−05−07
              2012−04−18
              2014−04−01
              2014−04−03
              (5
              rows )
                                                                      Esercitazione E.B.2.2.3.2.1.1
