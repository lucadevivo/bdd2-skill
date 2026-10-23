# 10 - smart2go

> Fonte: `(10) smart2go - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20170606 (P.20170606)
                                     smart2go
                                                                             Progetto P.20170606

    smart2go
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20170606

    smart2go
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare smart2go, un sistema informatico per la gestione di un
              servizio cittadino di car sharing.
              Il servizio di car sharing permette ai soci di noleggiare delle autovetture disseminate
              nel territorio anche solo per pochi minuti, pagando l’uso effettivo del veicolo (ovvero un
              costo al minuto, mentre il carburante è compreso). I vantaggi sono molteplici, soprattut-
              to per coloro che non usano frequentemente l’auto, potendo evitare i costi (assicurazione,
              tassa di proprietà, manutenzione) derivanti dal possesso di un’auto privata.
              Si vuole progettare un’applicazione che permetta di gestire il servizio di car sharing,
              relativamente ai soci e alle auto noleggiate.
                                                                             Progetto P.20170606

    smart2go
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
           Ogni socio deve potersi pre-registrare al servizio (ad es., via web), comunicando il suo
           codice fiscale, nome, cognome, data di nascita e gli estremi della sua patente di guida (in
           corso di validità). Deve quindi recarsi in un centro di supporto smart2go per mostrare la
           sua patente ad un operatore, il quale completerà o rifiuterà la registrazione. In caso di
           successo, il socio riceverà una smart card che gli consentirà di effettuare noleggi di auto.
           Ogni socio può iscriversi al servizio come privato oppure come dipendente di una
           società. All’atto della registrazione, i soci privati devono comunicare anche l’indirizzo
           di residenza e il numero di una carta di credito (in corso di validità) dove addebitare gli
           estratti conto, mentre i soci dipendenti di società devono comunicare il nome della società
           presso cui lavorano. Affinché la pre-registrazione di un socio dipendente di società abbia
           buon fine, la società deve essere già conosciuta al sistema, in termini di ragione sociale,
           indirizzo della sede legale, coordinate bancarie (IBAN) dove addebitare gli estratti conto
           relativi ai noleggi dei suoi dipendenti, e i riferimenti della persona responsabile del servizio
           smart2go nella società. Quest’ultima è la persona (nella società) deputata ad autorizzare
           le registrazioni dei dipendenti al servizio smart2go. In particolare, all’atto della pre-
           registrazione di un socio che si dichiara essere dipendente della società s, smart2go invia
           al responsabile smart2go di s una notifica che lo invita ad approvare o rifiutare tale
           richiesta di registrazione. Solo se la richiesta viene approvata dal responsabile smart2go
           della società, il socio dipendente può recarsi al centro di supporto smart2go per finalizzare
           la sua iscrizione e ritirare la smart card.
           Le auto a disposizione del servizio smart2go sono dislocate nel territorio cittadino.
           Quelle non utilizzate sono parcheggiate sulla pubblica via come le altre. Le auto sono
           equipaggiate di un dispositivo GPS per la loro localizzazione. Quindi, il sistema smart2go
           deve poter rappresentare le coordinate geografiche (latitudine e longitudine) di ogni auto
           della flotta smart2go parcheggiata.
              Un socio con registrazione completata può noleggiare un’auto parcheggiata: rag-
              giunge l’auto utilizzando una opportuna funzionalità di ricerca (ad es., disponibile nel
                                                                             Progetto P.20170606

    smart2go
    2. Specifica dei Requisiti
              sito web e/o in una app per smartphone), si identifica utilizzando la propria smart card
              (le portiere delle auto sono equipaggiate con sensori per smart card) ed entra nell’auto.
              Da quel momento parte il meccanismo di tariffazione, che consiste nell’addebitare una
              quota fissa per ogni minuto. All’atto dello spegnimento del motore e dell’uscita del socio
              dall’autovettura parcheggiata, il meccanismo di tariffazione viene sospeso.
              Il sistema deve permettere di rappresentare le informazioni per ogni noleggio neces-
              sarie a procedere alla corretta tariffazione del servizio, ovvero data e ora di entrata e di
              uscita del socio dal veicolo. Il sistema deve anche rappresentare le coordinate geografiche
              dell’auto quando questa è in sosta in attesa di un nuovo noleggio.
              Delle auto della flotta smart2go, è di interesse conoscere targa, modello, numero di
              posti, data dell’ultima manutenzione, e la categoria a cui appartengono. Le categorie
              delle auto (che hanno un nome, ad es. “city car”, “berlina”, ecc.) sono di interesse per
              l’applicazione, dato che da queste dipendono le tariffe al minuto applicate ai noleggi
              delle relative vetture.
              Alcuni soci vengono considerati clienti abituali e, in quanto tali, hanno diritto a sconti
              sulle tariffe dei noleggi. Attualmente un socio è considerato abituale se ha effettuato
              noleggi per almeno 60 ore nel corso degli ultimi 12 mesi in caso sia un privato, o almeno
              100 se usa il servizio per conto di una società.
              Le auto si dividono in due tipologie, in base al tipo della loro alimentazione: auto ad
              alimentazione tradizionale (benzina o diesel) ed auto a carburanti ecocompatibili (me-
              tano, GPL, elettrica, ecc.). Delle auto ad alimentazione tradizionale interessa conoscere
              il numero di chilometri che percorrono al litro, mentre di quelle ecocompatibili il tipo di
              alimentazione e la loro autonomia (in Km).
              Le società possono stipulare delle convenzioni con il servizio, che permettono di
              ottenere ulteriori sconti sui noleggi. In particolare, le convenzioni (di cui interessa il
              nome e il tasso di sconto applicato), si dividono in due categorie: quelle che incentivano
              il noleggio di auto ecocompatibili, e quelle che invece applicano lo sconto sui noleggi
              delle auto di alcune categorie (almeno una). Di ogni convenzione, interessa conoscere
              lo sconto applicato.
              Durante il noleggio di un’auto, è possibile che accadano dei sinistri. Di ogni sinistro,
              interessa conoscere, oltre alla sua descrizione, e alle informazioni sulla data, l’ora e il
              luogo dove è avvenuto, anche se ha provocato feriti, e qual è l’ammontare economico dei
              danni provocati. I sinistri sono di due tipi: quelli per cui esiste una controparte (ovvero
              incidenti con altri veicoli), e quelli senza controparte (ad es., incidenti dovuti ad altre
              cause). Dei primi interessa conoscere la targa dell’altro veicolo coinvolto, e sapere se il
              socio del servizio è responsabile (ovvero ha colpa).
                 Il sistema deve offrire le seguenti funzionalità:
                1. I soci devono poter effettuare la pre-registrazione al servizio via web, indicando i
                loro dati anagrafici e gli estremi della loro patente di guida.
                2. Il responsabile smart2go di una società deve poter approvare o rifiutare le pre-
                registrazioni dei soci che dichiarano di volersi registrare al servizio per conto della
                società.
                                                                             Progetto P.20170606

    smart2go
    2. Specifica dei Requisiti
                3. Il personale del centro di supporto smart2go deve poter accettare o rifiutare la
                pre-registrazione di un socio, rilasciando una smart card (di cui interessa il codice
                identificativo) in caso di accettazione.
           4. I soci devono poter effettuare noleggi di auto in autonomia (via web o app per
           smartphone), come descritto.
                5. I soci, all’atto del loro accesso ad un veicolo (per noleggiarlo), devono poter de-
                nunciare, utilizzando il computer di bordo, eventuali danni visibili al veicolo (una
                stringa).
           6. L’Ufficio Sinistri, dato un socio, vuole calcolare la sua classe di rischio, che dipende
           dal numero n di sinistri senza controparte più quelli con controparte di cui è stato
           responsabile avvenuti negli ultimi 3 anni. In particolare, la classe di rischio è 0 se
           n = 0, è pari ad n se 0 < n < 10, ed è pari a 10 se n ≥10.
           7. L’Ufficio Sinistri, dati un’auto (di cui si è scoperto un danno), ed un’istante di
           tempo (nella forma di una data ed un’ora), vuole conoscere l’ultimo utente che
           l’ha guidata (a quel dato istante di tempo).
                8. Il sistema di fatturazione, dato un socio ed un intervallo di tempo (nella forma di
                due date), ha bisogno di calcolare l’importo complessivo dei noleggi effettuati da
                quel socio nell’intervallo di tempo indicato (al fine di addebitare tale somma sul
                suo conto bancario). Il meccanismo di tariffazione prevede la possibilità di sconti:
           • Se il socio è una società che ha stipulato convenzioni con il servizio, tutti i
           suoi noleggi che rientrano nella convenzione sono scontati secondo i termini
           della convenzione.
           • In relazione alla classe di rischio c del socio, si applica un ulteriore sconto
           o sovrapprezzo. In particolare, se c < 2 si applica uno sconto del 10%; se
           c ≥5, si applica un sovrapprezzo di (c ∗10)% (ovvero 50% per c = 5, 60%
           per c = 6, ecc.).
                     • Se il socio è un cliente abituale (tale al momento dell’addebito), ottiene uno
                     sconto ulteriore del 15%.
                   Gli sconti vengono applicati l’uno dopo l’altro nell’ordine dato.
          9. L’ufficio comunicazioni esterne del servizio smart2go, dato un socio, vuole co-
          noscere le categorie delle auto che preferisce, ovvero quelle che ha noleggiato il
          maggior numero di volte.
          10. Il sistema di fatturazione, data una categoria di auto, vuole conoscere le società
          che hanno le convenzioni più vantaggiose (ovvero con tassi di sconto più elevati)
          per auto di quella categoria.
                                                                             Progetto P.20170606

    smart2go
    2. Specifica dei Requisiti
               11. Il sistema di fatturazione, dato un insieme di società, vuole conoscere quelle che
               hanno stipulato con il servizio smart2go almeno una convenzione per noleggiare
               auto ecocompatibili.
                                                                             Progetto P.20170606
