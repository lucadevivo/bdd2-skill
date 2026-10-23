# E.B.2.2.3.2.4.2 - SQL DML, Cielo 2, interrogazioni con raggruppamenti ed aggregati

> Fonte: `Esercitazione E.B.2.2.3.2.4.2 - SQL DML, Cielo 2, interrogazioni con raggruppamenti ed aggregati - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.4.2 (E.B.2.2.3.2.4.2)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                              Interrogazioni
                              Raggruppamenti
                                        Cielo 2
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.4.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Cielo 2
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Cielo.
                                                                       Esercitazione E.B.2.2.3.2.4.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Cielo 2
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
                                                                      Esercitazione E.B.2.2.3.2.4.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Cielo 2
    1. Base Dati e Interrogazioni
                   LuogoAeroporto (aeroporto: CodIATA, citta: StringaM, nazione: StringaM)
                    [VincoloDB.7]
                    foreign key: aeroporto references Aeroporto(codice)
                   Compagnia (nome: StringaM, annoFondaz*: PosInteger)
                 (*): può essere NULL
                                                                      Esercitazione E.B.2.2.3.2.4.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Cielo 2
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
                aeroporti?
                2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
                100 minuti?
                3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
                nella quale opera?
                4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
                compagnia ‘MagicFly’?
                5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
                aeroporti?
                6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
                voli?
                7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?
                8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
                a partire dal 1950?
                9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?
               10. Quali sono le città con almeno due aeroporti?
               11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
               ore?
               12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
               minuti?
                                                                      Esercitazione E.B.2.2.3.2.4.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Cielo 2
    1. Base Dati e Interrogazioni
              1.1
              Risultati Attesi delle Query
              Per incentivare gli studenti ad eseguire le loro interrogazioni su un DBMS, di seguito
              vengono riportati i risultati delle query sul database Accademia disponibile sul sito web
              del corso.
              È quindi possibile eseguire le proprie query e verificare che l’output sia consistente
              con quello riportato nelle pagine seguenti.
              1)
              Quante sono
              l e
              compagnie
              che
              operano
              ( s i a
              i n
              a r r i v o
              che
              i n
              partenza )
              n e i
              d i v e r s i
              a e r o p o r t i ?
              codice
              |
              nome
              |
              num_compagnie
              −−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−
              CDG
              |
              Charles
              de
              Gaulle ,
              Aeroport
              de
              P a r i s
              |
              CIA
              |
              Aeroporto
              d i Roma Ciampino
              |
              FCO
              |
              Aeroporto
              d i Roma Fiumicino
              |
              HTR
              |
              Heathrow
              Airport ,
              London
              |
              JFK
              | JFK A i r p o r t
              |
              (5
              rows )
              2)
              Quanti
              sono
              i
              v o l i
              che
              partono
              d a l l ’ aeroporto
              ’HTR’
              e hanno una
              durata
              d i
              almeno 100
              minuti ?
              num_voli
              −−−−−−−−−−
              (1 row )
              3)
              Quanti
              sono
              g l i
              a e r o p o r t i
              s u i
              q u a l i
              opera
              l a
              compagnia
              ’ A p i t a l i a ’ ,
              per
              ogni
              nazione
              n e l l a
              quale
              opera ?
              nazione
              |
              num_aerop
              −−−−−−−−−−−−−−−−+−−−−−−−−−−−
              I t a l y
              |
              United Kingdom
              |
              USA
              |
              (3
              rows )
              4)
              Qual e ’
              l a
              media ,
              i l
              massimo e
              i l
              minimo
              d e l l a
              durata
              d e i
              v o l i
              e f f e t t u a t i
              d a l l a
              compagnia
              ’ MagicFly ’ ?
              media
              |
              minimo
              |
              massimo
              −−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−+−−−−−−−−−
              420.0000000000000000
              |
              |
              (1 row )
              5)
              Qual e ’
              l ’ anno
              d i
              fondazione
              d e l l a
              compagnia
              piu ’
              vec chia
              che
              opera
              i n
              ognuno
              d e g l i
              a e r o p o r t i ?
              codice
              |
              nome
              |
              anno
              −−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−
              CIA
              |
              Aeroporto
              d i Roma Ciampino
              |
              HTR
              |
              Heathrow
              Airport ,
              London
              |
              CDG
              |
              Charles
              de
              Gaulle ,
              Aeroport
              de
              P a r i s
              |
              FCO
              |
              Aeroporto
              d i Roma Fiumicino
              |
              JFK
              | JFK A i r p o r t
              |
              (5
              rows )
              6)
              Quante sono
              l e
              n a z i o n i
              ( d i v e r s e )
              r a g g i u n g i b i l i
              da
              ogni
              nazione
              t r a m i t e
              uno o piu ’
              v o l i ?
                                                                            Esercitazione E.B.2.2.3.2.4.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Raggruppamenti
    Cielo 2
    1. Base Dati e Interrogazioni
              nazione
              |
              r a g g i u n g i b i l i
              −−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−
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
              7)
              Qual e ’
              l a
              durata
              media
              d e i
              v o l i
              che
              partono
              da ognuno
              d e g l i
              a e r o p o r t i ?
              codice
              |
              nome
              |
              media_durata
              −−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−
              CIA
              |
              Aeroporto
              d i Roma Ciampino
              |
              407.0000000000000000
              HTR
              |
              Heathrow
              Airport ,
              London
              |
              105.0000000000000000
              CDG
              |
              Charles
              de
              Gaulle ,
              Aeroport
              de
              P a r i s
              |
              60.0000000000000000
              FCO
              |
              Aeroporto
              d i Roma Fiumicino
              |
              545.5000000000000000
              JFK
              | JFK A i r p o r t
              |
              599.5000000000000000
              (5
              rows )
              8)
              Qual e ’
              l a
              durata
              complessiva
              d e i
              v o l i
              o p e r a t i
              da ognuna
              d e l l e
              compagnie
              fondate
              a
              p a r t i r e
              dal
              1950?
              nome
              |
              durata_tot
              −−−−−−−−−−−+−−−−−−−−−−−−
              Caimanair
              |
              MagicFly
              |
              (2
              rows )
              9)
              Quali
              sono
              g l i
              a e r o p o r t i
              n e i
              q u a l i
              operano
              esattamente
              due compagnie ?
              codice
              |
              nome
              −−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
              CDG
              |
              Charles
              de
              Gaulle ,
              Aeroport
              de
              P a r i s
              CIA
              |
              Aeroporto
              d i Roma Ciampino
              (2
              rows )
              10)
              Quali
              sono
              l e
              c i t t a ’
              con almeno due
              a e r o p o r t i ?
              c i t t a
              −−−−−−−
              Roma
              (1 row )
              11)
              Qual e ’
              i l
              nome
              d e l l e
              compagnie
              i
              c u i
              v o l i
              hanno una
              durata
              media
              maggiore
              d i
              6 ore ?
              compagnia
              −−−−−−−−−−−
              A p i t a l i a
              MagicFly
              (2
              rows )
              12)
              Qual e ’
              i l
              nome
              d e l l e
              compagnie
              i
              c u i
              v o l i
              hanno
              t u t t i
              una
              durata
              maggiore
              d i
              minuti ?
              compagnia
              −−−−−−−−−−−
              A p i t a l i a
              (1 row )
                                                                      Esercitazione E.B.2.2.3.2.4.2
