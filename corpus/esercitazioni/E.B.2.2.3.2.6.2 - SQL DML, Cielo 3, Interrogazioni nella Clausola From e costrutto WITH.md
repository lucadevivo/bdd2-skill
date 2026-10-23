# E.B.2.2.3.2.6.2 - SQL DML, Cielo 3, Interrogazioni nella Clausola From e costrutto WITH

> Fonte: `Esercitazione E.B.2.2.3.2.6.2 - SQL DML, Cielo 3, Interrogazioni nella Clausola From e costrutto WITH - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.6.2 (E.B.2.2.3.2.6.2)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                 Interrogazioni
                 Interrogazioni nella Clausola
                                        From
                                        Cielo 3
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.6.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Cielo 3
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Cielo, anche utilizzando funzioni aggregate, o raggruppa-
              menti, query annidate nella clausola from o tabelle temporanee definite con il costrutto
              WITH.
                                                                       Esercitazione E.B.2.2.3.2.6.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Cielo 3
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
                                                                      Esercitazione E.B.2.2.3.2.6.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Cielo 3
    1. Base Dati e Interrogazioni
                   LuogoAeroporto (aeroporto: CodIATA, citta: StringaM, nazione: StringaM)
                    [VincoloDB.7]
                    foreign key: aeroporto references Aeroporto(codice)
                   Compagnia (nome: StringaM, annoFondaz*: PosInteger)
                 (*): può essere NULL
                                                                      Esercitazione E.B.2.2.3.2.6.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Cielo 3
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Qual è la durata media, per ogni compagnia, dei voli che partono da un aeroporto
                situato in Italia?
                2. Quali sono le compagnie che operano voli con durata media maggiore della durata
                media di tutti i voli?
                3. Quali sono le città dove il numero totale di voli in arrivo è maggiore del numero
                medio dei voli in arrivo per ogni città?
                4. Quali sono le compagnie aeree che hanno voli in partenza da aeroporti in Italia con
                una durata media inferiore alla durata media di tutti i voli in partenza da aeroporti
                in Italia?
                5. Quali sono le città i cui voli in arrivo hanno una durata media che differisce di più
                di una deviazione standard dalla durata media di tutti i voli? Restituire città e
                durate medie dei voli in arrivo.
                6. Quali sono le nazioni che hanno il maggior numero di città dalle quali partono voli
                diretti in altre nazioni?
                                                                      Esercitazione E.B.2.2.3.2.6.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Cielo 3
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Cielo disponibile sul sito web del
              corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Qual e ’
              l a
              durata
              media
              d e i
              v o l i
              ( media
              c a l c o l a t a
              s u l l e
              d i v e r s e
              compagnie )
              che
              partono
              da un
              aeroporto
              s i t u a t o
              i n
              I t a l i a ?
              compagnia
              |
              durata_media
              −−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−
              A p i t a l i a
              |
              471.0000000000000000
              Caimanair
              |
              491.5000000000000000
              MagicFly
              |
              600.0000000000000000
              (3
              rows )
              2)
              Quali
              sono
              l e
              compagnie
              che
              operano
              v o l i
              con
              durata
              media
              maggiore
              d e l l a
              durata
              media
              d i
              t u t t i
              i
              v o l i ?
              comp
              |
              durata_media
              −−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−
              MagicFly
              |
              420.0000000000000000
              A p i t a l i a
              |
              432.4000000000000000
              (2
              rows )
              3)
              Quali
              sono
              l e
              c i t t a ’
              dove
              i l
              numero
              t o t a l e
              d i
              v o l i
              i n
              a r r i v o
              e ’
              maggiore
              d e l
              numero medio
              d e i
              v o l i
              i n
              a r r i v o
              per
              ogni
              c i t t a ’ ?
              c i t t a
              |
              numero_arrivi
              −−−−−−−−−−+−−−−−−−−−−−−−−−
              Roma
              |
              New York
              |
              (2
              rows )
              4)
              Quali
              sono
              l e
              compagnie
              aeree
              che hanno
              v o l i
              i n
              partenza
              da
              a e r o p o r t i
              i n
              I t a l i a
              con una
              durata
              media
              i n f e r i o r e
              a l l a
              durata
              media
              d i
              t u t t i
              i
              v o l i
              i n
              partenza
              da
              a e r o p o r t i
              i n
              I t a l i a ?
              compagnia
              |
              durata_media
              −−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−
              A p i t a l i a
              |
              499.3333333333333333
              Caimanair
              |
              499.3333333333333333
              (2
              rows )
              5)
              Quali
              sono
              l e
              c i t t a ’
              i
              c u i
              v o l i
              i n
              a r r i v o
              hanno una
              durata
              media
              che
              d i f f e r i s c e
              d i
              piu ’
              d i
              una
              d e v i a z i o n e
              standard
              d a l l a
              durata
              media
              d i
              t u t t i
              i
              v o l i ?
              R e s t i t u i r e
              c i t t a ’
              e
              durate
              medie
              d e i
              v o l i
              i n
              a r r i v o .
              c i t t a
              |
              durata_media
              −−−−−−−−+−−−−−−−−−−−−−−−−−−−−−
              P a r i s
              |
              60.0000000000000000
              London
              |
              60.0000000000000000
              (2
              rows )
              6)
              Quali
              sono
              l e
              n a z i o n i
              che hanno
              i l
              maggior numero
              d i
              c i t t a ’
              d a l l e
              q u a l i
              partono
              v o l i
              d i r e t t i
              i n
              a l t r e
              n a z i o n i ?
                  nazione
                  |
                  num_citta
                                                                            Esercitazione E.B.2.2.3.2.6.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni nella Clausola From
    Cielo 3
    1. Base Dati e Interrogazioni
              −−−−−−−−−−−−−−−−+−−−−−−−−−−−
              France
              |
              I t a l y
              |
              United Kingdom
              |
              USA
              |
              (4
              rows )
                                                                      Esercitazione E.B.2.2.3.2.6.2
