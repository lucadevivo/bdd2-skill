# E.B.2.2.3.2.9.1 - SQL DML, Accademia 8, interrogazioni con annidamenti nella clausola where e outer join

> Fonte: `Esercitazione E.B.2.2.3.2.9.1 - SQL DML, Accademia 8, interrogazioni con annidamenti nella clausola where e outer join - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.9.1 (E.B.2.2.3.2.9.1)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                                    Interrogazioni
                                 Outer Join
                                 Accademia 8
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Accademia, anche utilizzando funzioni aggregate, o rag-
              gruppamenti, query annidate nella clausola FROM, tabelle temporanee definite con il
              costrutto WITH, query annidate nella clausola WHERE, outer join.
                                                                       Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
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
                                                                      Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
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
                                                                      Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni:
                1. Quali sono le persone (id, nome e cognome) che hanno avuto assenze solo nei
                giorni in cui non avevano alcuna attivitÃ (progettuali o non progettuali)?
                2. Quali sono le persone (id, nome e cognome) che non hanno mai partecipato ad
                alcun progetto durante la durata del progetto “Pegasus”?
                3. Quali sono id, nome, cognome e stipendio dei ricercatori con stipendio maggiore
                di tutti i professori (associati e ordinari)?
                4. Quali sono le persone che hanno lavorato su progetti con un budget superiore alla
                media dei budget di tutti i progetti?
                5. Quali sono i progetti con un budget inferiore allala media, ma con un numero
                complessivo di ore dedicate alle attività di ricerca sopra la media?
                                                                      Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Accademia disponibile sul sito web
              del corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Quali
              sono
              l e
              persone
              ( id ,
              nome e cognome )
              che hanno
              avuto
              assenze
              s o l o
              n e i
              g i o r n i
              i n
              c u i
              non avevano
              alcuna
              a t t i v i t Ã
              ( p r o g e t t u a l i
              o non
              p r o g e t t u a l i ) ?
              Ordinare
              i l
              r i s u l t a t o
              per
              i d
              c r e s c e n t i .
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−−−+−−−−−−−−−−−−−
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
              Aurora
              |
              Bianchi
              |
              Guido
              |
              S p e n s i e r a t o
              |
              Consolata
              |
              F e r r a r i
              |
              Andrea
              |
              Verona
              |
              Asia
              |
              Giordano
              |
              Carlo
              |
              Zante
              |
              Ginevra
              |
              Riva
              |
              Davide
              |
              Quadro
              |
              Dario
              |
              B a s i l e
              |
              S i l v i a
              |
              Donati
              |
              F i o r e l l a
              |
              Martino
              |
              Leonardo
              |
              V i t a l i
              |
              Paolo
              |
              V a l e n t i n i
              |
              Emilio
              |
              Greco
              |
              G i u l i a
              |
              Costa
              |
              E l i s a
              |
              Longo
              |
              Carla
              |
              M a r t i n e l l i
              (20
              rows )
              1)
              Versione
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−−−+−−−−−−−−−−−−−
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
               Aurora
               |
               Bianchi
               |
               Guido
               |
               S p e n s i e r a t o
               |
               Consolata
               |
               F e r r a r i
               |
               Andrea
               |
               Verona
               |
               Asia
               |
               Giordano
               |
               Carlo
               |
               Zante
               |
               Ginevra
               |
               Riva
               |
               Davide
               |
               Quadro
               |
               Dario
               |
               B a s i l e
               |
               S i l v i a
               |
               Donati
               |
               F i o r e l l a
               |
               Martino
               |
               Leonardo
               |
               V i t a l i
               |
               Paolo
               |
               V a l e n t i n i
               |
               Emilio
               |
               Greco
               |
               G i u l i a
               |
               Costa
               |
               E l i s a
               |
               Longo
               |
               Carla
               |
               M a r t i n e l l i
                                                                            Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
    1. Base Dati e Interrogazioni
              (20
              rows )
              2)
              Quali
              sono
              l e
              persone
              ( id ,
              nome e cognome ,
              o r d i n a t e
              per
              i d
              c r e s c e n t e )
              che non hanno mai
              p a r t e c i p a t o
              ad
              alcun
              progetto
              durante
              l a
              durata
              d e l
              progetto
              " Pegasus "?
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−−−+−−−−−−−−−−−−−
              |
              Mario
              |
              Rossi
              |
              Gino
              |
              Spada
              |
              Guido
              |
              S p e n s i e r a t o
              |
              Consolata
              |
              F e r r a r i
              |
              Andrea
              |
              Verona
              |
              Carlo
              |
              Zante
              |
              Dario
              |
              B a s i l e
              |
              S i l v i a
              |
              Donati
              |
              F i o r e l l a
              |
              Martino
              |
              Leonardo
              |
              V i t a l i
              |
              Paolo
              |
              V a l e n t i n i
              |
              Emilio
              |
              Greco
              |
              G i u l i a
              |
              Costa
              |
              E l i s a
              |
              Longo
              |
              Carla
              |
              M a r t i n e l l i
              (15
              rows )
              2)
              Versione
              i d
              |
              nome
              |
              cognome
              −−−−+−−−−−−−−−−−+−−−−−−−−−−−−−
              |
              Mario
              |
              Rossi
              |
              Gino
              |
              Spada
              |
              Guido
              |
              S p e n s i e r a t o
              |
              Consolata
              |
              F e r r a r i
              |
              Andrea
              |
              Verona
              |
              Carlo
              |
              Zante
              |
              Dario
              |
              B a s i l e
              |
              S i l v i a
              |
              Donati
              |
              F i o r e l l a
              |
              Martino
              |
              Leonardo
              |
              V i t a l i
              |
              Paolo
              |
              V a l e n t i n i
              |
              Emilio
              |
              Greco
              |
              G i u l i a
              |
              Costa
              |
              E l i s a
              |
              Longo
              |
              Carla
              |
              M a r t i n e l l i
              (15
              rows )
              3)
              Quali
              sono
              id ,
              nome ,
              cognome e
              s t i p e n d i o
              d e i
              r i c e r c a t o r i
              ( i n
              o r d i n e
              d i
              i d
              c r e s c e n t e )
              con
              s t i p e n d i o
              maggiore
              d i
              t u t t i
              i
              p r o f e s s o r i
              ( a s s o c i a t i
              e
              o r d i n a r i ) ?
              i d
              |
              nome
              |
              cognome
              |
              s t i p e n d i o
              −−−−+−−−−−−+−−−−−−−−−+−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              45500.3
              (1 row )
              3)
              Versione
              i d
              |
              nome
              |
              cognome
              |
              s t i p e n d i o
              |
              p o s i z i o n e
              −−−−+−−−−−−+−−−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              45500.3
              |
              R i c e r c a t o r e
              (1 row )
              4)
              Quali
              sono
              l e
              persone
              ( o r d i n a t e
              per
              i d
              c r e s c e n t e )
              che hanno
              l a v o r a t o
              su
              p r o g e t t i
              con un budget
              s u p e r i o r e
              a l l a
              media
              d e i
              budget
              d i
              t u t t i
              i
              p r o g e t t i ?
              i d
              |
              nome
              |
              cognome
                                                                            Esercitazione E.B.2.2.3.2.9.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Outer Join
    Accademia 8
    1. Base Dati e Interrogazioni
              −−−−+−−−−−−−−+−−−−−−−−−
              |
              Aurora
              |
              Bianchi
              (1 row )
              5)
              Quali
              sono
              i
              p r o g e t t i
              ( o r d i n a t i
              con
              i d
              c r e s c e n t e )
              con un budget
              i n f e r i o r e
              a l l a l a
              media , ma con un numero
              complessivo
              d i
              ore
              d e d i c a t e
              a l l e
              a t t i v i t a ’
              d i
              r i c e r c a
              sopra
              l a
              media ?
              i d
              |
              nome
              −−−−+−−−−−−−−−
              |
              Pegasus
              (1 row )
              5)
              Versione
              i d
              |
              nome
              −−−−+−−−−−−−−−
              |
              Pegasus
              (1 row )
                                                                      Esercitazione E.B.2.2.3.2.9.1
