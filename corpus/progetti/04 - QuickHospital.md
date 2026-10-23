# 04 - QuickHospital

> Fonte: `(04) Progetto QuickHospital - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20080110 (P.20080110)
                               QuickHospital
                                                                             Progetto P.20080110

    QuickHospital
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20080110

    QuickHospital
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare QuickHospital, un sistema informatico per la gestio-
              ne di ricoveri e di visite mediche in un ospedale estremamente efficiente. Il sistema
              deve permettere la memorizzazione e gestione dei pazienti e dei relativi ricoveri ospe-
              dalieri e prenotazioni di visite ambulatoriali, nonché degli itinerari di visita dei medici
              dell’ospedale.
                                                                             Progetto P.20080110

    QuickHospital
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
           Il sistema QuickHospital deve permettere di memorizzare e gestire informazioni circa i
           pazienti e i medici dell’ospedale nel quale viene installato. In particolare, dei pazienti
           interessano alcune informazioni anagrafiche (nome, cognome e data di nascita) ed i loro
           recapiti, distinti in recapiti telefonici, recapito email e postale (questi ultimi unici).
           Per quanto riguarda i medici dell’ospedale invece, interessa mantenere informazioni
           sul loro nome, cognome e data di nascita, ed i pazienti che hanno in cura.
              Un paziente può essere ricoverato, in una certa data, solo se una precedente verifica
              della disponibilità dei posti letto presenti nell’ospedale ha dato esito positivo.
           Una volta effettuato il ricovero, il paziente ha assegnato un posto letto nell’ambito
           di una stanza; una stanza può contenere da un minimo di 1 ad un massimo di 8 posti
           letto. Le stanze hanno un piano ed un settore (interi positivi).
           Il sistema deve inoltre permettere la memorizzazione dello storico di tutti i pazienti
           che sono stati ricoverati e poi dimessi nel tempo, con le informazioni relative ai posti
           letto occupati durante i diversi ricoveri.1
           Sono funzionalità specifiche del sistema la registrazione del ricovero di un paziente
           e della sua dimissione ad opera del personale di accettazione. Inoltre il sistema deve
           assistere i medici ottimizzando il loro percorso di visite.
           In particolare, il sistema deve permettere di calcolare, su richiesta di un medico, il
           suo itineriario delle visite, ovvero un insieme ordinato delle stanze cui accedere (che sono
           tutte e sole le stanze che ospitano i pazienti che ha in cura).
           L’ordinamento è dato in primo luogo dal piano delle stanze dei pazienti da visitare, ed
           in secondo luogo dal settore di appartenenza di tali stanze (entrambi in ordine crescente).
           I settori sono infatti numerati secondo un criterio di vicinanza topologica. Pertanto se
           un dato medico deve visitare le stanze {(7, 4), (7, 1), (1, 3), (1, 1), (3, 4)} dove la prima
           componente di ognuna è il piano e la seconda il settore, l’itinerario di visita proposto
           deve essere [(1, 1), (1, 3), (3, 4), (7, 1), (7, 7)].
                 1Si assuma per semplicità che durante il periodo di un ricovero il paziente non possa cambiare letto.
                                                                             Progetto P.20080110

    QuickHospital
    2. Specifica dei Requisiti
              Oltre ai pazienti dell’ospedale, il sistema gestisce anche prestazioni mediche fatte
              da medici dell’ospedale a pazienti esterni. L’anagrafica di tali pazienti è registrata nel
              sistema (ad opera del personale addetto alle prenotazioni), con l’informazione aggiun-
              tiva della particolare prestazione medica richiesta al personale ospedaliero (oltre che la
              data richiesta). Le prestazioni sono caratterizzate da una specializzazione richiesta (ad.,
              ortopedia, dermatologia, ecc.) e una descrizione più estesa.
              Di ogni medico il sistema deve conoscere la sua specializzazione primaria e le sue
              specializzazioni secondarie.
              Data una prestazione richiesta da un paziente esterno (per una specializzazione s), il
              sistema deve restituire l’insieme dei medici maggiormente idonei a soddisfarla. Il criterio
              di idoneità è il seguente: se esistono medici con specializzazione primaria pari ad s, il
              risultato è l’insieme di tali medici. Altrimenti, il risultato è l’insieme dei medici che hanno
              s tra le loro specializzazioni secondarie.
              Il sistema QuickHospital è accessibile ai medici, al personale amministrativo e a quelli
              dell’ufficio prenotazioni.
                                                                             Progetto P.20080110
