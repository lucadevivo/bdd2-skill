# E.B.2.2.3.2.2.2 - SQL DML, Cielo 1, interrogazioni su tabelle multiple

> Fonte: `Esercitazione E.B.2.2.3.2.2.2 - SQL DML, Cielo 1, interrogazioni su tabelle multiple - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.3.2.2.2 (E.B.2.2.3.2.2.2)
                            Basi di dati
                            Sistemi di Gestione di Basi di Dati Relazionali
                          Il Linguaggio SQL
                          Data Manipulation Language
                     Interrogazioni
                     Interrogazioni su Tabelle
                                        Multiple
                                        Cielo 1
                                       – Solo Testo –
                                                                       Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
                           Obiettivi
              Si chiede di definire opportune query SQL per rispondere a diverse interrogazioni su
              tabelle multiple del database Cielo.
                                                                       Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
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
                                                                      Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
    1. Base Dati e Interrogazioni
                   LuogoAeroporto (aeroporto: CodIATA, citta: StringaM, nazione: StringaM)
                    [VincoloDB.7]
                    foreign key: aeroporto references Aeroporto(codice)
                   Compagnia (nome: StringaM, annoFondaz*: PosInteger)
                 (*): può essere NULL
                                                                      Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
    1. Base Dati e Interrogazioni
                 Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
                1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
                2. Quali sono le compagnie che hanno voli che superano le 3 ore?
                3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
                codice ‘CIA’?
                4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
                ‘FCO’?
                5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
                e arrivano all’aeroporto ‘JFK’?
                6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
                rano all’aeroporto ‘JFK’?
                7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
                città di ‘New York’?
                8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
                della compagnia di nome ‘MagicFly’?
                9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
                atterrano ad un qualunque aeroporto della città di ‘New York’? Restituire: codice
                del volo, nome della compagnia, e aeroporti di partenza e arrivo.
               10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
               voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
               qualunque aeroporto della città di ‘New York’? Restituire: nome della compagnia,
               codici dei voli, e aeroporti di partenza, scalo e arrivo.
               11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
               rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?
                                                                      Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
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
              ( codice
              e nome
              d e l l a
              compagnia )
              l a
              c u i
              durata
              supera
              l e
              3 ore ?
              codice_volo
              |
              compagnia
              −−−−−−−−−−−−−+−−−−−−−−−−−
              |
              MagicFly
              |
              Caimanair
              |
              A p i t a l i a
              |
              A p i t a l i a
              |
              A p i t a l i a
              |
              MagicFly
              |
              Caimanair
              |
              A p i t a l i a
              (8
              rows )
              2)
              Quali
              sono
              l e
              compagnie
              che hanno
              v o l i
              che
              superano
              l e
              ore ?
              compagnia
              −−−−−−−−−−−
               MagicFly
               Caimanair
              A p i t a l i a
              (3
              rows )
              3)
              Quali
              sono
              i
              v o l i
              ( codice
              e nome
              d e l l a
              compagnia )
              che
              partono
              d a l l ’
              aeroporto
              con
              codice
              ’ CIA ’ ?
              codice_volo
              |
              compagnia
              −−−−−−−−−−−−−+−−−−−−−−−−−
              |
              Caimanair
              |
              A p i t a l i a
              (2
              rows )
              4)
              Quali
              sono
              l e
              compagnie
              che hanno
              v o l i
              che
              a r r i v a n o
              a l l ’ aeroporto
              con
              codice
              ’FCO’ ?
              compagnia
              −−−−−−−−−−−
              A p i t a l i a
              MagicFly
              Caimanair
              (3
              rows )
              5)
              Quali
              sono
              i
              v o l i
              ( codice
              e nome
              d e l l a
              compagnia )
              che
              partono
              d a l l ’
              aeroporto
              ’FCO’
              e
              a r r i v a n o
              a l l ’ aeroporto
              ’JFK ’ ?
              codice_volo
              |
              compagnia
              −−−−−−−−−−−−−+−−−−−−−−−−−
              |
              MagicFly
              |
              Caimanair
              |
              A p i t a l i a
              (3
              rows )
                                                                            Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
    1. Base Dati e Interrogazioni
              6)
              Quali
              sono
              l e
              compagnie
              che hanno
              v o l i
              che
              partono
              d a l l ’ aeroporto
              ’FCO’
              e
              a t t e r r a n o
              a l l ’ aeroporto
              ’JFK ’ ?
              compagnia
              −−−−−−−−−−−
               MagicFly
               Caimanair
              A p i t a l i a
              (3
              rows )
              7)
              Quali
              sono
              i
              nomi
              d e l l e
              compagnie
              che hanno
              v o l i
              d i r e t t i
              d a l l a
              c i t t a ’
              d i
              ’Roma ’
              a l l a
              c i t t a ’
              d i
              ’New York ’ ?
              compagnia
              −−−−−−−−−−−
              A p i t a l i a
              MagicFly
              Caimanair
              (3
              rows )
              8)
              Quali
              sono
              g l i
              a e r o p o r t i
              ( con
              codice IATA ,
              nome e
              luogo )
              n e i
              q u a l i
              partono
              v o l i
              d e l l a
              compagnia
              d i nome
              ’ MagicFly ’ ?
              c o d i c e i a t a
              |
              nome
              |
              c i t t a
              −−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−
              JFK
              | JFK A i r p o r t
              | New York
              FCO
              |
              Aeroporto
              d i Roma Fiumicino
              | Roma
              HTR
              |
              Heathrow
              Airport ,
              London
              |
              London
              (3
              rows )
              9)
              Quali
              sono
              i
              v o l i
              che
              partono
              da un qualunque
              aeroporto
              d e l l a
              c i t t a ’
              d i
              ’Roma ’
              e
              a t t e r r a n o
              ad un qualunque
              aeroporto
              d e l l a
              c i t t a ’
              d i
              ’New York ’ ?
              R e s t i t u i r e :
              codice
              d e l
              volo ,
              nome
              d e l l a
              compagnia ,
              e
              a e r o p o r t i
              d i
              partenza
              e
              a r r i v o .
              codice_volo
              |
              compagnia
              |
              partenza
              |
              a r r i v o
              −−−−−−−−−−−−−+−−−−−−−−−−−+−−−−−−−−−−+−−−−−−−−
              |
              A p i t a l i a
              |
              CIA
              | JFK
              |
              MagicFly
              | FCO
              | JFK
              |
              Caimanair
              | FCO
              | JFK
              |
              A p i t a l i a
              | FCO
              | JFK
              (4
              rows )
              10)
              Quali
              sono
              i
              p o s s i b i l i
              p i a n i
              d i
              volo
              con
              esattamente
              un cambio
              (
              u t i l i z z a n d o
              s o l o
              v o l i
              d e l l a
              s t e s s a
              compagnia ) da un qualunque
              aeroporto
              d e l l a
              c i t t a ’
              d i
              ’Roma ’
              ad un qualunque
              aeroporto
              d e l l a
              c i t t a ’
              d i
              ’New
              York ’ ?
              R e s t i t u i r e :
              nome
              d e l l a
              compagnia ,
              c o d i c i
              d e i
              v o l i ,
              e
              a e r o p o r t i
              d i
              partenza ,
              s c a l o
              e
              a r r i v o .
              compagnia
              |
              codice_volo_1
              |
              partenza
              |
              s c a l o
              |
              codice_volo_2
              |
              a r r i v o
              −−−−−−−−−−−+−−−−−−−−−−−−−−−+−−−−−−−−−−+−−−−−−−+−−−−−−−−−−−−−−−+−−−−−−−−
              Caimanair
              |
              |
              CIA
              | FCO
              |
              | JFK
              A p i t a l i a
              |
              | FCO
              |
              CIA
              |
              | JFK
              (2
              rows )
              11)
              Quali
              sono
              l e
              compagnie
              che hanno
              v o l i
              che
              partono
              d a l l ’ aeroporto
              ’FCO
              ’ ,
              a t t e r r a n o
              a l l ’ aeroporto
              ’JFK ’ ,
              e
              d i
              c u i
              s i
              conosce
              l ’ anno
              d i
              fondazione ?
              compagnia
              −−−−−−−−−−−
                                                                            Esercitazione E.B.2.2.3.2.2.2

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Manipulation Language
    Interrogazioni
    Interrogazioni su Tabelle Multiple
    Cielo 1
    1. Base Dati e Interrogazioni
               MagicFly
               Caimanair
              A p i t a l i a
              (3
              rows )
                                                                      Esercitazione E.B.2.2.3.2.2.2
