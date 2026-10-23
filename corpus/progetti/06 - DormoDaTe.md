# 06 - DormoDaTe

> Fonte: `(06) DormoDaTe - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20070703 (P.20070703)
                                 DormoDaTe
                                                                             Progetto P.20070703

    DormoDaTe
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20070703

    DormoDaTe
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare DormoDaTe.com, un sistema per un portale web che
              consenta agli iscritti di chiedere ospitalità, durante i loro viaggi, a casa di altri iscritti.
              Lo scopo, oltre che quello banale di ridurre le spese di viaggio, è soprattuto quello di
              incentivare scambi sociali e senso di ospitalità, e di favorire nuove conoscenze.
                                                                             Progetto P.20070703

    DormoDaTe
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              Il sistema DormoDaTe.com1 deve consentire agli utenti di iscriversi al portale web, di-
              chiarando il loro profilo, ovvero nome, cognome, sesso, età, città di residenza, oltre che
              informazioni circa la tipologia di ospitalità che sono disposti ad offrire.
           In particolare, è necessario che gli iscritti possano inserire nel loro profilo le seguenti
           informazioni:
                 • Distanza della loro abitazione dal centro città;
                 • Distanza dalla stazione autobus/metro/treno più vicina;
                 • Numero di membri della famiglia (numero di adulti e di bambini);
           • Numero di persone che sono disposti ad ospitare contemporaneamente (posti let-
           to); dei posti letto va specificato (nel modo più preciso e strutturato possibile) se
           si tratta di letti (singoli/doppi) in camere separate, divani in stanze comuni, ecc.
           (ad esempio, un iscritto può dichiarare di avere un posto in letto singolo più due
           posti in letto doppio in una camera, ed un posto in soggiorno sul divano).
           In ogni momento ogni iscritto ha la facoltà di aggiornare le informazioni circa le
           sue disponibilità ad ospitare altre persone, sulla base dei suoi impegni. In particolare,
           il sistema deve permettere ad ogni iscritto la possibilità di dichiarare delle date o dei
           periodi nei quali non è disponibile a ricevere ospiti, ad es. perché fuori (la ragione non è
           di interesse per il sistema).
           I viaggiatori che desiderano organizzare un viaggio usufruendo del servizio devono
           poter interrogare il sistema per ottenere l’insieme di tutti gli iscritti della città desiderata
           che sono disposti a ricevere ospiti nel periodo richiesto e hanno, per le date richieste,
           posti sufficienti disponibili.
                 1Il sistema vuole mettersi in diretta concorrenza con il ben più famoso couchsurfing.com.
                                                                             Progetto P.20070703

    DormoDaTe
    2. Specifica dei Requisiti
              Una volta scelta una soluzione di alloggio, i viaggiatori possono effettuare la relativa
              richiesta di prenotazione, specificando tutte le informazioni necessarie (date, persone,
              scelta dei posti letto, ecc.). Si noti che è possibile per un viaggiatore prenotare anche per
              eventuali accompagnatori: tuttavia il sistema impone che tutti (chi prenota ed eventuali
              accompagnatori) siano iscritti al sistema (questo per monitorare la qualità e l’affidabilità
              degli ospiti, cfr. seguito). Il relativo ospitante (membro padrone di casa) può decidere
              liberamente se accettare la richiesta o rifiutarla (in quest’ultimo caso deve specificare
              una motivazione). Tutte le richieste di prenotazioni, quelle accettate e quelle rifutate,
              devono essere mantenute in modo persistente dal sistema.
              La difficoltà maggiore che si riscontra in sistemi del genere è quella relativa alla sicu-
              rezza, visto che, di fatto, gli iscritti offrono ospitalità a casa propria a perfetti estranei (e,
              dualmente, un viaggiatore va a dormire a casa di sconosciuti). Per questo motivo, sono di
              grande importanza quei meccanismi che permettono di avere maggiore confidenza circa
              la qualità e l’affidabilità dell’ospitante e degli ospitati. In particolare, DormoDaTe.com
              deve permettere dei meccanismi di feedback per valutare la qualità e l’affidabilità sia dei
              padroni di casa che dei viaggiatori. In dettaglio:
                 • Ogni viaggiatore, dopo aver alloggiato presso un iscritto ospitante, deve necessa-
                 riamente esprimere una valutazione su quest’ultimo, in termini di un intero da 0
                 (scarso) a 5 (ottimo);
                 • Ogni ospitante, all’atto della partenza di un ospite, può esprimere una valutazione
                 su quest’ultimo, anche qui in termini di un intero da 0 a 5.
              Si noti che, la valutazione di un ospitante su un ospitato è facoltativa, mentre quella
              opposta è obbligatoria.
              In particolare, sebbene quest’ultima possa essere effettuata
              anche in un tempo successivo, il sistema deve fare in modo che un viaggiatore non possa
              prenotare più alcuna nuova sistemazione se non ha valutato tutti gli ospitanti presso cui
              ha alloggiato.
                                                                             Progetto P.20070703
