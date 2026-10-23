# BD2_2017-04-05_ecoParks — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2017-04-05_ecoParks.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Esame — 20170405 — ecoParks.it

l Ministero dell’Ambiente e della Tutela del Territorio e del Mare emette un bando per il progetto è
lo sviluppo di un sistema per la gestione controllata degli accessi turistici alle aree naturali protette,
al fine di favorire un tunsmo eco=-sostenibile in Italia.

Si richiede di progettare il sistema ecoParks.it da presentare al Ministero come risposta al bando
esposto.

II sistema ecoParks.it intente catalogare le aree protette italiane e i turisti che vogliono accedere
{utenti del s1stemal.

Di ogni area si vuole mantenere il nome di quel luogo come area protetta e la lista dei comuni su cui
l’area si estende. Le aree protette di interesse per ecoParks.it sono i parchi nazionali è le riserve
naturali. Da un lato, i parchi sono accessibili agli utenti del sistema (per monitorare il carico
turistico ove possibile, alcuni parchi più sensibili all’impatto antropico verranno dotati di ingressi e
si richiede di registrare tutti gli accessi degli utenti, in ingresso e in uscita, a tali parchi sensibili).
Dall‘altro lato. Le riserve naturali hanno esigenze più protezionistiche che impongono diverse
limitazioni. La prima è che una riserva naturale può anche non essere visitabile (se visitabile sì deve
mantenere il numero massimo di visitatori che possono essere presenti contemporaneamente al suo
interno). Inoltre, l’accesso alle riserve naturali visitabili può avvenire solo attraverso escursioni
organizzate {(cfr. seguito). Infine, una riserva può permettere oppure no l’accesso da parte di animali
domestici accompagnati (cani, satti, etc.).

Nelle aree protette accessibili al turismo (parchi e riserve visitabili) sono organizzate delle
CSCUrsIoni. Di ogni escursione 1l sistema deve mantenere la data e l'ora di partenza, la durata, una
descrizione e il numero massimo di persone che vi possono partecipare.

Gli utenti sono i reali fruitori del sistema. Un utente è contraddistinto dal suo nome, cognome,
genere data e luogo di nascita. Un utente usa ecoParks.it per cercare le aree protette è le escursioni
più adatte alle sue esigenze.

Una volta trovata l’escursione di suo interesse, un utente deve prenotarsi, specificando il mnumero di
persone e, separatamente, di animali accompagnati che compongono 1l suo gruppo. Il sistema non
deve accettare prenotazioni con animali a escursioni su riserve in cui non è permesso l'accesso agli
animali. Un utente può infine decidere di dare un feedback all’escursione, nel qual caso esprimerà
un voto da 1 a 5 accompagnato, opzionalmente, da una valutazione testuale,

Negli ultirmi anni è stata fatta molta ricerca per caratterizzare la Capacità di Carnco Turistico di una
zona (CCT} definita come “i]l numero massimo di persone che possono visitare una destinazione
turistica dello stesso momento, senza causare distruzione dell’ambiente fisito, economico è socio-
culturale e un inaccettabile decremento della qualità delle soddisfazioni dei visitatori"". Secondo
alcune ricerche, un valore accettabile di CCOT è di 3.8 metri quadrati per persona. Dala una zona di
superficie £ in cui siano presenti # persone in un dato momento, si dice ché tale zona ha densità

furistica (13 x 1U'Ù) a.

Una densità turistica maggiore al 100% indica un’eccessiva [requentazione della zona in questione.

## Pagina 2

l sistema ecaParks.it deve fomrnire le seguenti funzionalità.

Iscrizione di un utente.

Accesso di un utente in un parco nazionale sensibile, con il numero di persone e animali che
accompagnano l'utente.

Prenotazione di una escursione da parte di un utente privato.

Ricerca delle riserve naturali più apprezzate nell’ultimo anno.

Ricerca delle aree protette più vicine, ordinate per densità turistica non decrescente.

Ricerca delle escursioni non ancora partite più “gettonate”” nelle aree protette di una data
città. cioè delle escursioni con un numero di prenotazioni più alto della media su tutte le
escursioni della data città (una prenotazione conta per il numero di partecipanti del gruppo).
Data un’area protetta visitabile e controllata (parco nazionale sensibile o riserva naturale
visitabile), il sistema deve poter calcolare la disponibilità di posti in tale area rispetto alla
densità turistica al 100%. In altri termini, se un’area ha 100 m° di superficie è 10 persone al
+Uo interno (accessi a parchi sensibili © escursioni attive), ha una densità turistica del 38%.
Siccome la zona sopporta ancora il 62% di densità turistica, il numero di persona che vi
possono ancora accedere mantenendo una sana CCT è [62/3.8] = [16.32] = 16.
