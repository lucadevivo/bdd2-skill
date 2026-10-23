# E.B.2.2.3.2.4.1 - SQL DML, Accademia 6, Interrogazioni con raggruppamenti ed aggregati

> Fonte: `Esercitazione E.B.2.2.3.2.4.1 - SQL DML, Accademia 6, Interrogazioni con raggruppamenti ed aggregati - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.4.1 (E.B.2.2.3.2.4.1)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                              Interrogazioni
                              Raggruppamenti
                                 Accademia 6
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.4.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Accademia 6
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Accademia, anche utilizzando funzioni aggregate e/o rag-
              gruppamenti.
                                                                       Esercitazione E.B.2.2.3.2.4.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Accademia 6
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
                                                                      Esercitazione E.B.2.2.3.2.4.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Accademia 6
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
                                                                      Esercitazione E.B.2.2.3.2.4.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Accademia 6
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Quanti sono gli strutturati di ogni fascia?
                2. Quanti sono gli strutturati con stipendio ≥40000?
                3. Quanti sono i progetti già finiti che superano il budget di 50000?
                4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
                ‘Pegasus’?
                5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
                ‘Pegasus’ da ogni singolo docente?
                6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
                7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
                8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
                associati e dei professori ordinari?
                9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
               10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
               11. Quali sono i professori associati che hanno lavorato su più di un progetto?
                                                                      Esercitazione E.B.2.2.3.2.4.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Accademia 6
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Accademia disponibile sul sito web
              del corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Quanti
              sono
              g l i
              s t r u t t u r a t i
              d i
              ogni
              f a s c i a ?
              p o s i z i o n e
              |
              numero
              −−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−
              P r o f e s s o r e
              O r d i n a r i o
              |
              P r o f e s s o r e
              Associato
              |
              R i c e r c a t o r e
              |
              (3
              rows )
              2)
              Quanti
              sono
              g l i
              s t r u t t u r a t i
              con
              s t i p e n d i o >= 40000?
              numero
              −−−−−−−−
              (1 row )
              3)
              Quanti
              sono
              i
              p r o g e t t i
              gia ’
              f i n i t i
              che
              superano
              i l
              budget
              d i
              50000?
              numero
              −−−−−−−−
              (1 row )
              4)
              Qual e ’
              l a
              media ,
              i l
              massimo e
              i l
              minimo
              d e l l e
              ore
              d e l l e
              a t t i v i t a ’
              r e l a t i v e
              a l
              progetto
              " Pegasus "?
              media
              |
              minimo
              |
              massimo
              −−−−−−−−−−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−
              7.8571428571428571
              |
              |
              (1 row )
              5)
              Quali
              sono
              l e
              medie ,
              i
              massimi
              e
              i
              minimi
              d e l l e
              ore
              g i o r n a l i e r e
              d e d i c a t e
              a l
              progetto
              ’ Pegasus ’
              da
              ogni
              s i n g o l o
              docente ?
              id_persona
              |
              nome
              |
              cognome
              |
              media
              |
              minimo
              |
              massimo
              −−−−−−−−−−−−+−−−−−−−−−+−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−
              |
              Asia
              |
              Giordano
              |
              8.0000000000000000
              |
              |
              |
              Anna
              |
              Bianchi
              |
              8.0000000000000000
              |
              |
              |
              Ginevra
              |
              Riva
              |
              8.0000000000000000
              |
              |
              |
              Barbara
              |
              Burso
              |
              7.0000000000000000
              |
              |
              (4
              rows )
              6)
              Qual e ’
              i l
              numero
              t o t a l e
              d i
              ore
              d e d i c a t e
              a l l a
              d i d a t t i c a
              da
              ogni
              docente ?
              id_persona
              |
              nome
              |
              cognome
              |
              o r e _ d i d a t t i c a
              −−−−−−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−+−−−−−−−−−−−−−−−
                       |
                       Consolata
                       |
                       F e r r a r i
                       |
                       |
                       Anna
                       |
                       Bianchi
                       |
                       |
                       Barbara
                       |
                       Burso
                       |
                       |
                       Asia
                       |
                       Giordano
                       |
                       |
                       Mario
                       |
                       Rossi
                       |
                                                                            Esercitazione E.B.2.2.3.2.4.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Accademia 6
    1. Base Dati e Interrogazioni
              (5
              rows )
              7)
              Qual e ’
              l a
              media ,
              i l
              massimo e
              i l
              minimo
              d e g l i
              s t i p e n d i
              d e i
              r i c e r c a t o r i ?
              media
              |
              minimo
              |
              massimo
              −−−−−−−−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−
              40304.2712053571
              |
              |
              45500.3
              (1 row )
              8)
              Quali
              sono
              l e
              medie ,
              i
              massimi
              e
              i
              minimi
              d e g l i
              s t i p e n d i
              d e i
              r i c e r c a t o r i ,
              d e i
              p r o f e s s o r i
              a s s o c i a t i
              e
              d e i
              p r o f e s s o r i
              o r d i n a r i ?
              p o s i z i o n e
              |
              media
              |
              minimo
              |
              massimo
              −−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−+−−−−−−−−−+−−−−−−−−−
              P r o f e s s o r e
              O r d i n a r i o
              |
              39848.6673177083
              |
              36922.1
              |
              45200.1
              P r o f e s s o r e
              Associato
              |
              38211.1437988281
              |
              29200.1
              |
              43500.5
              R i c e r c a t o r e
              |
              40304.2712053571
              |
              |
              45500.3
              (3
              rows )
              9)
              Quante
              ore " Ginevra
              Riva " ha
              dedicato
              ad
              ogni
              progetto
              n e l
              quale
              ha
              l a v o r a t o ?
              id_progetto
              |
              progetto
              |
              totale_ore
              −−−−−−−−−−−−−+−−−−−−−−−−+−−−−−−−−−−−−
              |
              Pegasus
              |
              (1 row )
              10)
              Qual e ’
              i l
              nome
              d e i
              p r o g e t t i
              su
              c u i
              lavorano
              piu ’
              d i
              due
              s t r u t t u r a t i ?
              id_progetto
              |
              progetto
              −−−−−−−−−−−−−+−−−−−−−−−−
              |
              Pegasus
              |
              Simap
              (2
              rows )
              11)
              Quali
              sono
              i
              p r o f e s s o r i
              a s s o c i a t i
              che hanno
              l a v o r a t o
              su
              piu ’
              d i
              un
              progetto ?
              id_persona
              |
              nome
              |
              cognome
              −−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−
              |
              Aurora
              |
              Bianchi
              (1 row )
                                                                      Esercitazione E.B.2.2.3.2.4.1
