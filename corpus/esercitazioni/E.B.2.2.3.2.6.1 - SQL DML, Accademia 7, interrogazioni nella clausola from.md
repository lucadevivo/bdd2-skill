# E.B.2.2.3.2.6.1 - SQL DML, Accademia 7, interrogazioni nella clausola from

> Fonte: `Esercitazione E.B.2.2.3.2.6.1 - SQL DML, Accademia 7, interrogazioni nella clausola from - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.6.1 (E.B.2.2.3.2.6.1)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                 Interrogazioni
                 Interrogazioni nella Clausola
                                 From
                                 Accademia 7
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.6.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Accademia 7
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Accademia, anche utilizzando funzioni aggregate, o rag-
              gruppamenti, query annidate nella clausola from o tabelle temporanee definite con il
              costrutto WITH.
                                                                       Esercitazione E.B.2.2.3.2.6.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Accademia 7
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
                                                                      Esercitazione E.B.2.2.3.2.6.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Accademia 7
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
                                                                      Esercitazione E.B.2.2.3.2.6.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Accademia 7
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?
                2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media
                della loro categoria?
                3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che
                differisce di al massimo una deviazione standard dalla media della loro categoria?
                4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività
                progettuali? Restituire tutti i loro dati e il numero di ore lavorate.
                5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i
                progetti? Restituire nome dei progetti e loro durata in giorni.
                6. Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo
                “Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle
                ore dedicate a tali attività nel progetto.
                7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del nu-
                mero di assenze medio per malattia dei professori associati? Restituire id, nome e
                cognome del professore e il numero di giorni di assenza per malattia.
                                                                      Esercitazione E.B.2.2.3.2.6.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Accademia 7
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Accademia disponibile sul sito web
              del corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Qual e ’
              l a
              media e
              l a
              d e v i a z i o n e
              standard
              d e g l i
              s t i p e n d i
              per
              ogni
              c a t e g o r i a
              d i
              s t r u t t u r a t i ?
              p o s i z i o n e
              |
              media
              |
              dev_standard
              −−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−
              P r o f e s s o r e
              O r d i n a r i o
              |
              39848.667317708336
              |
              2894.855495562445
              R i c e r c a t o r e
              |
              40304.271205357145
              |
              3602.198235119911
              P r o f e s s o r e
              Associato
              |
              38211.143798828125
              |
              4359.258153186441
              (3
              rows )
              2)
              Quali
              sono
              i
              r i c e r c a t o r i
              ( t u t t i
              g l i
              a t t r i b u t i )
              con uno
              s t i p e n d i o
              s u p e r i o r e
              a l l a
              media
              d e l l a
              l o r o
              c a t e g o r i a ?
              i d
              |
              nome
              |
              cognome
              |
              p o s i z i o n e
              |
              s t i p e n d i o
              −−−−+−−−−−−−−−+−−−−−−−−−−−−+−−−−−−−−−−−−−+−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              R i c e r c a t o r e
              |
              45500.3
              |
              Barbara
              |
              Burso
              |
              R i c e r c a t o r e
              |
              40442.5
              |
              Dario
              |
              B a s i l e
              |
              R i c e r c a t o r e
              |
              |
              Carla
              |
              M a r t i n e l l i
              |
              R i c e r c a t o r e
              |
              42030.2
              (4
              rows )
              3)
              Per
              ogni
              c a t e g o r i a
              d i
              s t r u t t u r a t i
              quante
              sono
              l e
              persone
              con uno
              s t i p e n d i o
              che
              d i f f e r i s c e
              d i
              a l
              massimo una
              d e v i a z i o n e
              standard
              d a l l a
              media
              d e l l a
              l o r o
              c a t e g o r i a ?
              p o s i z i o n e
              |
              numero
              −−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−
              P r o f e s s o r e
              O r d i n a r i o
              |
              R i c e r c a t o r e
              |
              P r o f e s s o r e
              Associato
              |
              (3
              rows )
              4)
              Chi
              sono
              g l i
              s t r u t t u r a t i
              che hanno
              l a v o r a t o
              almeno 20
              ore
              complessive
              i n
              a t t i v i t a ’
              p r o g e t t u a l i ?
              R e s t i t u i r e
              t u t t i
              i
              l o r o
              d a t i
              e
              i l
              numero
              d i
              ore
              l a v o r a t e .
              i d
              |
              nome
              |
              cognome
              |
              p o s i z i o n e
              |
              s t i p e n d i o
              |
              ore_lavorate
              −−−−+−−−−−−+−−−−−−−−−+−−−−−−−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−−−−−
              |
              Anna
              |
              Bianchi
              |
              R i c e r c a t o r e
              |
              45500.3
              |
              (1 row )
              5)
              Quali
              sono
              i
              p r o g e t t i
              l a
              c u i
              durata
              e ’
              s u p e r i o r e
              a l l a
              media
              d e l l e
              durate
              d i
              t u t t i
              i
              p r o g e t t i ?
              R e s t i t u i r e
              nome
              d e i
              p r o g e t t i
              e
              l o r o
              durata
              i n
              g i o r n i .
              nome
              |
              durata_giorni
              −−−−−−−−−−−−−+−−−−−−−−−−−−−−−
              WineSharing
              |
              Simap
              |
              (2
              rows )
                                                                            Esercitazione E.B.2.2.3.2.6.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Accademia 7
    1. Base Dati e Interrogazioni
              6)
              Quali
              sono
              i
              p r o g e t t i
              t e r m i n a t i
              i n
              data
              odierna
              che hanno
              avuto
              a t t i v i t a
              ’
              d i
              t i p o
              " Dimostrazione "?
              R e s t i t u i r e
              nome d i
              ogni
              progetto
              e
              i l
              numero
              complessivo
              d e l l e
              ore
              d e d i c a t e
              a
              t a l i
              a t t i v i t a ’
              n e l
              progetto .
              i d
              |
              nome
              |
              ore_dimostrazione
              −−−−+−−−−−−−−−+−−−−−−−−−−−−−−−−−−−
              |
              Pegasus
              |
              (1 row )
              7)
              Quali
              sono
              i
              p r o f e s s o r i
              o r d i n a r i
              che hanno
              f a t t o
              piu ’
              assenze
              per
              m a l a t t i a
              d e l
              numero
              d i
              assenze
              medio
              per
              m a l a t t i a
              d e i
              p r o f e s s o r i
              a s s o c i a t i ?
              R e s t i t u i r e
              id ,
              nome e cognome
              d e l
              p r o f e s s o r e
              e
              i l
              numero
              d i
              g i o r n i
              d i
              assenza
              per
              m a l a t t i a .
              i d
              |
              nome
              |
              cognome
              |
              num_giorni_malattia
              −−−−+−−−−−−−−−+−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−
              |
              Ginevra
              |
              Riva
              |
              (1 row )
                                                                      Esercitazione E.B.2.2.3.2.6.1
