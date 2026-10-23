# B.2.2.3.2.7.2 - SQL DML, Cielo 5, Interrogazioni annidate, con costrutto WITH ed ARRAY

> Fonte: `Esercitazione B.2.2.3.2.7.2 - SQL DML, Cielo 5, Interrogazioni annidate, con costrutto WITH ed ARRAY - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.7.2 (E.B.2.2.3.2.7.2)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                      Interrogazioni
                      Interrogazioni Annidate
                                        Cielo 5
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.7.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 5
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Cielo, anche utilizzando funzioni aggregate, o raggruppa-
              menti, query annidate nella clausola from o tabelle temporanee definite con il costrutto
              WITH.
              Prima di svolgere l’esercitazione, studiare in autonomia la possibilità, offerta da
              PostgreSQL, di definire campi di una query di tipo ARRAY.
                                                                       Esercitazione E.B.2.2.3.2.7.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 5
    1. Base Dati e Interrogazioni
                 Base Dati e Interrogazioni
              Il database Cielo è definito sul seguente insieme di domini e sul seguente schema
              relazionale con vincoli.
              Definizione dei domini
                     • PosInteger
                     integer ≥0
                     • StringaM
                     varchar(100)
                     • CodIATA
                     char(3)
              Schema relazionale con vincoli della base dati
                   Volo (codice: PosInteger, comp: StringaM, durataMinuti: PosInteger)
                    [VincoloDB.1]
                    foreign key: comp references Compagnia(nome)
                    [VincoloDB.2]
                    foreign key: (codice, comp) references ArrPart(codice, comp)
                   ArrPart (codice: PosInteger, comp: StringaM, arrivo: CodIATA, partenza: Co-
                   dIATA)
                    [VincoloDB.3]
                    foreign key: (codice, comp) references Volo(codice, comp)
                    [VincoloDB.4]
                    foreign key: arrivo references Aeroporto(codice)
                    [VincoloDB.5]
                    foreign key: partenza references Peroporto(codice)
                   Aeroporto (codice: CodIATA, nome: StringaM)
                    [VincoloDB.6]
                    foreign key: codice references LuogoAeroporto(aeroporto)
                                                                      Esercitazione E.B.2.2.3.2.7.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 5
    1. Base Dati e Interrogazioni
                   LuogoAeroporto (aeroporto: CodIATA, citta: StringaM, nazione: StringaM)
                    [VincoloDB.7]
                    foreign key: aeroporto references Aeroporto(codice)
                   Compagnia (nome: StringaM, annoFondaz*: PosInteger)
                 (*): può essere NULL
                                                                      Esercitazione E.B.2.2.3.2.7.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 5
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Quali sono gli aeroporti raggiungibili da dall’aeroporto ‘JFK’ tramite voli diretti e
                indiretti?
                2. Quali sono le città raggiungibili con voli diretti e indiretti partendo da Roma?
                3. Quali sono i piani di volo, con al più due scali intermedi, da ‘FCO’ a ‘JFK’? Per
                ogni piano di volo restituire la sequenza di voli previsti (con aeroporto di partenza,
                compagnia, codice volo, aeroporto di arrivo) e la durata complessiva. Evitare di
                restituire piani di volo ‘degeneri’, ovvero che facciano tappa intermedia a FCO o
                due volte nello stesso aeroporto. Ordinare il risultato per durata complessiva del
                piano di volo.
                                                                      Esercitazione E.B.2.2.3.2.7.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 5
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Cielo disponibile sul sito web del
              corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Quali
              sono
              g l i
              a e r o p o r t i
              r a g g i u n g i b i l i
              da
              d a l l ’ aeroporto
              ’JFK ’
              t r a m i t e
              v o l i
              d i r e t t i
              e
              i n d i r e t t i ?
              aeroporto
              −−−−−−−−−−−
               FCO
              CIA
              JFK
              (3
              rows )
              2)
              Quali
              sono
              l e
              c i t t a ’
              r a g g i u n g i b i l i
              con
              v o l i
              d i r e t t i
              e
              i n d i r e t t i
              partendo
              da Roma?
              c i t t a
              −−−−−−−−−−
              Roma
              New York
              (2
              rows )
              3)
              Quali
              sono
              i
              p i a n i
              d i
              volo ,
              con
              a l
              piu ’
              due
              s c a l i
              intermedi ,
              da
              ’FCO’
              a
              ’JFK ’ ?
              Per
              ogni
              piano
              d i
              volo
              r e s t i t u i r e
              l a
              sequenza
              d i
              v o l i
              p r e v i s t i
              (
              aeroporto
              d i
              partenza ,
              compagnia ,
              codice
              volo ,
              aeroporto
              d i
              a r r i v o )
              e
              l a
              durata
              complessiva .
              E v i t a r e
              d i
              r e s t i t u i r e
              p i a n i
              d i
              volo
              ’ degeneri ’ ,
              ovvero
              che
              f a c c i a n o
              tappa
              i n t e r m e d i a
              a FCO o due
              v o l t e
              n e l l o
              s t e s s o
              aeroporto .
              Ordinare
              i l
              r i s u l t a t o
              per
              durata
              complessiva
              d e l
              piano
              d i
              volo .
              piano_volo
              |
              durata_totale
              −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−
              {"(FCO, A p i t a l i a ,536 , JFK) "}
              |
              {"(FCO, MagicFly ,134 , JFK) "}
              |
              {"(FCO, Caimanair ,265 , JFK) "}
              |
              {"(FCO, A p i t a l i a ,1265 , CIA ) " ,"( CIA , A p i t a l i a ,534 , JFK) "}
              |
              (4
              rows )
                                                                      Esercitazione E.B.2.2.3.2.7.2
