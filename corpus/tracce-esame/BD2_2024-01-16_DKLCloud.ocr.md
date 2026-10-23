# BD2_2024-01-16_DKLCloud — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2024-01-16_DKLCloud.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell’Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Toni Mancini
Dipartimento di Informatica
http://tmancini.di.uniroma1l.it

Esame Es.20240116 — Prova scritta del 16 gennaio 2024

Delivery & inter-Kontinental Logistics (DKL) è una compagnia che si occupa della consegna di
plichi e pacchi a livello globale spediti da utenti privati e commerciali. ‘

Sì vuole progettare e realizzare DKL-Cloud, un piattaforma per la gestione delle spedizioni di
DKL.

In particolare, si desidera che il sistema consenta ai clienti (privati cittadini o aziende, anche
detti utenti commerciali) di gestire personalmente le loro spedizioni, accedendo al canale online di
DKL-Cloud, previa registrazione e autenticazione. In particolare, gli utenti, dopo essersi registrati
al sistema fornendo alcuni dati di interesse (nome e cognome per gli utenti privati, e ragione sociale
per gli utenti commerciali) e aver ricevuto un codice cliente univoco, possono prenotare il ritiro di
merce presso un indirizzo a loro scelta e la consegna presso il destinatario desiderato. Sebbene il
ritiro della merce non possa essere prenotato per un orario preciso (per motivi logistici), il sistema
deve consentire ai clienti di inserire una fascia oraria di 4 ore nella quale vogliono il ritiro,

I| pagamento di un invio di merce avviene al momento della prenotazione online. Per questo
motivo, il sistema deve permettere agli utenti di registrare una o più carte di credito (di cui interessa
nominativo del titolare, numero e data di scadenza) da utilizzare per i pagamenti. Al momento di
ogni transazione, il cliente sarà chiamato a scegliere la carta di credito (tra quelle registrate) da
utilizzare.

La tariffa di ogni invio dipende da diversi fattori: 1. I| peso della merce (in Kg); 2. L'importo per
il quale la merce è assicurata. Per cercare di ritagliarsi più spazio nel complesso mercato dei corrieri
espressi, DKL non fa alcuna differenza di prezzo tra spedizioni nello stesso continente e spedizioni
in continenti diversi.

| prezzi vengono definiti per le diverse fasce di peso della merce. Ad esempio, i prezzi attuali
sono: 10 Eur (fino a 2 Kg), 20 Eur (oltre 2 e fino a 10 Kg), 50 Eur (oltre 10 e fino a 30 Kg), 70 Eur
(oltre i 30 Kg e fino a 100 Kg). (Attualmente DKL non consegna merce oltre i 100 Kg.) I| prezzo
così ottenuto viene poi maggiorato dello 0.1% dell'importo assicurato (se il cliente ha optato per
una assicurazione), ottenendo quindi il prezzo finale tariffato al cliente. Si noti che le soglie di peso
per il calcolo del prezzo sono quelle utilizzate attualmente da DKL. Il sistema deve permettere al
management della compagnia di modificarle in qualunque momento. Tali modifiche non si applicano
ai ritiri di merce già prenotati (ma non ancora eseguiti).

DKL possiede diversi centri di smistamento (depot) dislocati geograficamente nei 5 continenti e
una flotta di mezzi diversi (autocarri, navi, aerei cargo) per trasportare le merci dal cliente mittente
al cliente destinatario, passando per i propri depot. DKL-Cloud deve mantenere queste informazioni
per consentire ai clienti il tracciamento delle proprie spedizioni. In particolare, di ogni movimento
di merce il sistema deve mantenere il mezzo utilizzato oltre ai depot di arrivo e di partenza, con
relative informazioni temporali.

Il sistema viene utilizzato dai clienti (via web), dal management (via web) e dai corrieri di DKL
(via app su smartphone).

| corrieri devono poter interrogare il sistema per ottenere la lista degli indirizzi dove sono previsti
ritiri di merce nel giorno corrente e prendere in carico le diverse prenotazioni ancora pendenti. In
dettaglio, il sistema, data una città in input, restituisce al corriere la lista degli indirizzi di quella

1

## Pagina 2

città, presso i quali è stato prenotato un ritiro merce nel giorno corrente ancora pendente (ovvero
che non è stato ancora eseguito o preso in carico da un altro corriere). Infine,

e | clienti devono poter tracciare una spedizione. In particolare, data una spedizione, il sistema
deve restituire la lista ordinata temporalmente dei depot per cui è passata la merce e i mezzi
utilizzati (oltre allo stato attuale e al nome del corriere che ha preso in carico la spedizione,

se questa non è pendente).

e Infine, il sistema deve permettere al management di monitorare la redditività delle spedizioni
tra continenti diversi, misurata in termini di prezzo medio delle spedizioni tra i due continenti.
In particolare, dati in input due continenti c1 (continente di partenza) e ca (continente di
arrivo) ed un periodo temporale, il sistema deve considerare tutte le spedizioni (iniziate nel
periodo richiesto) che partono da una qualunque città di c, e arrivano in una qualunque città
di ca e restituire il prezzo finale medio di tali consegne.
