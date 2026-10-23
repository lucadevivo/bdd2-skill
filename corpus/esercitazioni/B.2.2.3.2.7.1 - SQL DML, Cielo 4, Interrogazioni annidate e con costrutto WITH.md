# B.2.2.3.2.7.1 - SQL DML, Cielo 4, Interrogazioni annidate e con costrutto WITH

> Fonte: `Esercitazione B.2.2.3.2.7.1 - SQL DML, Cielo 4, Interrogazioni annidate e con costrutto WITH - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.7.1 (E.B.2.2.3.2.7.1)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                      Interrogazioni
                      Interrogazioni Annidate
                                        Cielo 4
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Cielo, anche utilizzando funzioni aggregate, o raggruppa-
              menti, query annidate nella clausola from o tabelle temporanee definite con il costrutto
              WITH.
              Prima di svolgere l’esercitazione, studiare in autonomia il costrutto WITH RECUR-
              SIVE supportato da PostgreSQL.
                                                                       Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
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
                                                                      Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
    1. Base Dati e Interrogazioni
                   LuogoAeroporto (aeroporto: CodIATA, citta: StringaM, nazione: StringaM)
                    [VincoloDB.7]
                    foreign key: aeroporto references Aeroporto(codice)
                   Compagnia (nome: StringaM, annoFondaz*: PosInteger)
                 (*): può essere NULL
                                                                      Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Quali sono i voli di durata maggiore della durata media di tutti i voli della stessa
                compagnia? Restituire il codice del volo, la compagnia e la durata.
                2. Quali sono le città che hanno piu” di un aeroporto e dove almeno uno di questi ha
                un volo operato da “Apitalia”?
                3. Quali sono le coppie di aeroporti (A, B) tali che esistono voli tra A e B ed il numero
                di voli da A a B è uguale al numero di voli da B ad A?
                4. Quali sono le compagnie che hanno voli con durata media maggiore della durata
                media di tutte le compagnie?
                5. Quali sono gli aeroporti da cui partono voli per almeno 2 nazioni diverse?
                6. Quali sono i voli che partono dalle città con un unico aeroporto? Restituire codice
                dei voli, compagnie, e gli aeroporti di partenza e di arrivo.
                7. Quali sono gli aeroporti raggiungibili dall’aeroporto “JFK” tramite voli diretti e
                indiretti?
                8. Quali sono le città raggiungibili con voli diretti e indiretti partendo da Roma?
                9. Quali sono le città raggiungibili con esattamente uno scalo intermedo partendo
                dall’aeroporto “JFK”?
                                                                      Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
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
              i
              v o l i
              d i
              durata
              maggiore
              d e l l a
              durata
              media
              d i
              t u t t i
              i
              v o l i
              d e l l a
              s t e s s a
              compagnia ?
              R e s t i t u i r e
              i l
              codice
              d e l
              volo ,
              l a
              compagnia e
              l a
              durata .
              Versione
              codice
              |
              comp
              |
              durataminuti
              −−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−−−−−
              |
              MagicFly
              |
              |
              Caimanair
              |
              |
              A p i t a l i a
              |
              |
              MagicFly
              |
              |
              Caimanair
              |
              |
              A p i t a l i a
              |
              (6
              rows )
              Versione
              codice
              |
              comp
              |
              durataminuti
              |
              duratamedia
              −−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−
              |
              MagicFly
              |
              |
              420.0000000000000000
              |
              Caimanair
              |
              |
              347.6666666666666667
              |
              A p i t a l i a
              |
              |
              432.4000000000000000
              |
              MagicFly
              |
              |
              420.0000000000000000
              |
              Caimanair
              |
              |
              347.6666666666666667
              |
              A p i t a l i a
              |
              |
              432.4000000000000000
              (6
              rows )
              2)
              Quali
              sono
              l e
              c i t t a ’
              che hanno
              piu ’
              d i
              un
              aeroporto
              e dove
              almeno uno
              d i
              q u e s t i
              ha un
              volo
              operato
              da
              ’ A p i t a l i a ’ ?
              Versione
              c i t t a
              −−−−−−−
              Roma
              (1 row )
              Versione
              c i t t a
              −−−−−−−
              Roma
              (1 row )
              Versione
              c i t t a
              −−−−−−−
              Roma
              (1 row )
              3)
              Quali
              sono
              l e
              coppie
              d i
              a e r o p o r t i
              (A, B)
              t a l i
              che
              e s i s t o n o
              v o l i
              t r a A e
              B ed
              i l
              numero
              d i
              v o l i
              da A a B e ’
              uguale
              a l
              numero
              d i
              v o l i
              da B ad A?
              Versione
              partenza
              |
              a r r i v o
              −−−−−−−−−−+−−−−−−−−
               CDG
               | HTR
               CIA
               | FCO
                                                                            Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
    1. Base Dati e Interrogazioni
              FCO
              |
              CIA
              HTR
              | CDG
              (4
              rows )
              Versione
              partenza
              |
              a r r i v o
              −−−−−−−−−−+−−−−−−−−
              CDG
              | HTR
              CIA
              | FCO
              FCO
              |
              CIA
              HTR
              | CDG
              (4
              rows )
              4)
              Quali
              sono
              l e
              compagnie
              che hanno
              v o l i
              con
              durata
              media
              maggiore
              d e l l a
              durata
              media
              d i
              t u t t e
              l e
              compagnie ?
              Versione
              nome
              −−−−−−−−−−
              A p i t a l i a
              MagicFly
              (2
              rows )
              Versione
              compagnia
              −−−−−−−−−−−
              A p i t a l i a
              MagicFly
              (2
              rows )
              5)
              Quali
              sono
              g l i
              a e r o p o r t i
              da
              c u i
              partono
              v o l i
              per
              almeno 2
              n a z i o n i
              d i v e r s e ?
              Versione
              codice
              −−−−−−−−
               FCO
              CIA
              HTR
              (3
              rows )
              Versione
              partenza
              −−−−−−−−−−
              CIA
              FCO
              HTR
              (3
              rows )
              6)
              Quali
              sono
              i
              v o l i
              che
              partono
              d a l l e
              c i t t a ’
              con un
              unico
              aeroporto ?
              R e s t i t u i r e
              codice
              d e i
              v o l i ,
              compagnie ,
              e
              g l i
              a e r o p o r t i
              d i
              partenza
              e
              d i
              a r r i v o .
              Versione
              codice
              |
              comp
              |
              a r r i v o
              |
              partenza
              −−−−−−−−+−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−−
              |
              MagicFly
              | FCO
              | JFK
              |
              A p i t a l i a
              | FCO
              | JFK
              |
              MagicFly
              | CDG
              | HTR
              |
              Caimanair
              | HTR
              | CDG
              |
              A p i t a l i a
              | FCO
              | HTR
              (5
              rows )
              Versione
              codice
              |
              comp
              |
              a r r i v o
              |
              partenza
                                                                            Esercitazione E.B.2.2.3.2.7.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni Annidate
    Cielo 4
    1. Base Dati e Interrogazioni
              −−−−−−−−+−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−−
              |
              MagicFly
              | FCO
              | JFK
              |
              A p i t a l i a
              | FCO
              | JFK
              |
              MagicFly
              | CDG
              | HTR
              |
              Caimanair
              | HTR
              | CDG
              |
              A p i t a l i a
              | FCO
              | HTR
              (5
              rows )
              7)
              Quali
              sono
              g l i
              a e r o p o r t i
              r a g g i u n g i b i l i
              d a l l ’ aeroporto
              ’JFK ’
              t r a m i t e
              v o l i
              d i r e t t i
              e
              i n d i r e t t i ?
              a r r i v o
              −−−−−−−−
              FCO
              JFK
              CIA
              (3
              rows )
              8)
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
              9)
              Quali
              sono
              l e
              c i t t a ’
              r a g g i u n g i b i l i
              con
              esattamente
              uno
              s c a l o
              intermedo
              partendo
              d a l l ’ aeroporto
              ’JFK ’ ?
              c i t t a
              −−−−−−−−−−
              New York
              Roma
              (2
              rows )
                                                                      Esercitazione E.B.2.2.3.2.7.1
