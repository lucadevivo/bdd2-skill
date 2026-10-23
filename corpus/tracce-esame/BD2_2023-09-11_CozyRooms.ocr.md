# BD2_2023-09-11_CozyRooms — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2023-09-11_CozyRooms.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea In Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Toni Mancini
Dipartimento di Informatica
http: / /tmancini.di.uniromaL:it

Esame Es.20230911 = Prova scritta dell'11 Settembre 2023

Sì vuole progettare e realizzare CozyRooms, un sistema per la gestione di strutture ricettive e
dei soggiorni presso di esse.

Il sistema dovrà servire agli utenti per pubblicare offerte riguardo le proprie strutture (ad esempio
a!Èerghi. …î è c…j. gestire le prenotazioni e | soggiorni, ricercare strutture e
sistemazioni, e prenotare soggiorni.

Gli utenti si iscrivono a CozyRooms fornendo ngme. cagnome, … e numero di

Gli utenti gestori di strutture devono fornire anche il codice fiscale e superare un processo
di identificazione (ilquale è portato avanti utilizzando un servizio esterna).

| gestori di strutture ‘dentificati con successo possono registrare le proprie strutture. Di una
struttura interessa conoscere il nome, l'indirizzo, la tip clagia (albergo, casa vacanze, bed & breakfast,
ecc.), il numero di stelle (un intero compreso tra. edi ges.t…ncgg;i\[poiaunu essere più d'una).

Ogni É@'É ispone di una o più sisternazioni. Ad esempio, un hotel dispone in genere di
numerose camere, mentre un residence può includere diversi appartamenti. Di ogni sistemazione
interessa conoscere il nome, e il numero di posti letto; =

Il costo del pernottamento non é costante durante l'anno, ma dipende dalla data. l sistema
deve permettere ai gestori delle strutture di specificare, per ogni sistemazione, la tariffa applicata
per ogni giorno dell'anno solare.

Inoltre, il costo del pernottamento in una sistemazione dipende anche dal numero di occupanti.
Ad esempio, una camera doppia di un certo hotel, in una certa data, potrebbe cdstare 60 Euro a
notte per un solo accupante e 80 Euro a notte per due occupanti. Îl gestore deve specificare la
tariffa di per ogni numero di occupanti da 1 al numero di posti letto presenti nellà sistemazione.

Gli utenti di CozyRooms che vogliono soggiornare presso una struttura, lo fanno tramite: un
sermplice servizio di prenotazione. A| momento della prenotazione, un utente sceglie un intervallo di

date, una o pi…i offerte da una stessa struttura e un …É per ognuna

di esse, è fornisce un …o. È-l_Ùﬂ deve essere possibile richiedere la prenotazion
per una sistemazione che è già prenotata in almeno una data nel periodo richiesto. I| gestore della
struttura può quindi accettare o rifiutare le prenotazioni. L'utente che effettua la prenotazione può
cancellarla fino al momento del soggiorno (si assuma che la gestione delle penali per cancellazione
tardiva sia gestita da un sistema esterno).

CozyRooms prevede un sistema di fedeltà per i propri utenti, che li premia jn, base ai soggiorni
effettuati. Si vuole che tale sistema di fedeltà sia flessibile, dunque i | CozyRooms devo-
no poter definire dei livelli progressivi, ognuno rappresentato da un nome univoco e raggiungibile
completando un certo numero minimo di prenotazioni nei due anni solari precedenti. Ad esempio,
si potrebbero definire i livelli bronzo, argento e oro, raggiungibili completando, rispettivamente, 3,
10 e 20 prenotazioni negli ultimi due anni solari. -

| gestori delle strutture possono prevedere (ma non è obbligatorio), per ogni struttura, un tasso
di sconta differente per ogni livello di fedeltà. Tale tasso di sconto è definito tramite un numero
reale compreso tra Ò e 1 (esclusi) e si applica al'costo totale della prenotazione.

j Il sistema deve permettare ai propri utenti di registrare strutture, visualizzare le strutture ricettive
in una certa città, controllare la disponibilità di una sistemazione in un certo intervallo di date,

1

## Pagina 2

prenotare una o più sistemazioni presso una struttura, conoscere
un re;5ugug_t.;; di tutte le prenotazioni passate, future ed in corso,
\noltre, il sistema deve permettere: |

il proprio livello di fedeltà, ottenere
e calcolare il costo di un soggiorno.

: A l sistemazioni
e agli utenti registrati interessati a prenotare soggiorni di ottenere le guepeeo disponibili in un

certo intervallo di date e che rispettino un certo insieme di requisiti. In particolare, le strutture
restituite devono trovarsi in una data città, appartenere a UNa data tipologia, avere un dato
numero minimo di stelle, e, per le date richieste, avere uN prezzo totale (considerando il livello
di fedeltà dell'utente) al di sotto di una data soglia. e il numero di posti letto richiesti

e a ognì utente gestore di strutture di calcolare, data una struttura gestita, per ognuno dei
mesi dell'anno solare corrente, il numero aggagila di giorni in cui tale struttura era piena. pna
struttura è considerata piena in una data se ogni sua sistemazione ha almeno una prenotazione
per quella data, indipendentemente dal numero di posti letto prenotati.
