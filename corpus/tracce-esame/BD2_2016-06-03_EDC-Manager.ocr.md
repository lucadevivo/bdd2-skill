# BD2_2016-06-03_EDC-Manager — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2016-06-03_EDC-Manager.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Esame di Basi di Dati - Modulo 2

dal 03-06-2016

EDC è una compagnia che sì occupa della consegna di plichi e pacchi a
livello giobale spediti da utenti privati e commaerciali.

Si vuole progettare e realizzare EDG-Manager, una piattaforma per la
gestione delle spedizioni di EDC.

In particolare, si desidera che il sistema consenta ai clienti { sia privati sia
aziende anche dette utenti commerdali) di gestire personalmente le proprie
spedizioni, accedendo al canale on-line di EDC-Manager, previa registrazione
a autenticazione. In particolare gli utenti, dopo essersi registrati al sistema,
fornendo alcuni dati d'interesse { nome e cognome per gli utenti privati,
ragione sociale per gli utenti commerciali ) è aver ricevuto un codice univoco
possono prenolare il ritiro di merce presso un indirizzo a loro scelta e la
consegna presso il destinatario voluto. Sebbene il ritiro della merce non
possa essere prenotalo per un orano preciso (per motivi logistici) il sistema
deve permaetterae all'utente di inserire, nella prenotazione, una fascia oraria di
4 ore nella quale si rende disponibile per il ritiro della merce. Il sistema deve
consentire ai clienti di registrare una o più carte di credito { di cui interessa il
titolare, numero, scadenza) da utiizzarne per i pagamenti.

AI maomento della transazione, il cliente sarà chiamato a scegliere la carta di
credito { tra quelle registrate ) da usare.

La tariffa dipende da diversi fattori: 1. peso della mercae (in kg) 2. le aree
geografiche di ritiro @ consegna 3. L'importo per il quale la merce è assicurata
4. la velocità di spedizione (standard, prioritaria o espressa) si prevede poi un
sovrapprezzo di una certa percentuale in caso di ritiro elo consegna nei giorni
festivi.

EDC divide il giobo in continenti, paesi è regioni. | prezzi vengono deliniti
esplicitamente per la diversa fasca di peso dalla merce, per consegne
standard tra paesi dello stesso continente. Tutti gli altri vengono calcolati a
partire dai primi. Ad esempio, | prezzi attuali per consegne standard tra paesi
daello stesso continaente sono: 10€/ fino a 2kg ) 201 oltre 2kg e fino a 10kg ),
50€/oltre 10kg e fino a 30kg), 70€/ottre i 30kg e fino a 100kg). (Attualmente
EDC non consegna merce superiore a 100kg).

In caso di consegna prioritaria il prezzo base viene maggiorato del 20%, in
caso di consegna espressa del 30%. ll prezzo ottenuto tenendo conto della
velocità di spedizione vienae ulteriormente modificato a seconda della
dislocazione del ritiro e della consegna. In particolare in caso la consegna sia
all'interno dello stasso paese i prezzi vengo ribassati di una certa percentuale
(altualmente 30%). Dualmente, in caso di consegna tra paesi di contenti
diversi, | prezzi sono incrementati (attualmente del 40%). ll prezzo così
ottenuto viene poi maggiorato dello 0.1% dell'importo assicurato, se il cliente

## Pagina 2

ha scello l'assicurazione, ottenendo quindi il prezzo finale tariffato al chente.
Si noti che le soglia di peso e le percentuali per il calcolo del prezzo devono
poter essere modificate dalla compagnia. Tall modifiche non si applicano ai
ritiri già prenotati (non ancora eseguiti). | clienti commerciali di EDC possono
sltipulare degli abbonamenti prapagati, che consentono loro di effettuare
spedizioni multiple a prezzi vantaggiosi. In particolare, EDC mette a
disposizione un servizio di abbonamaento del tutto simile a sim prepagate per i
telefoni: il chente carica il suo conto con un certo importo per poterlo usare
nelle prenotazioni successive.

| costi di tali spedizione saranno scontati di un tasso che varia a seconda
dell'importo dell’ultima ricarica (es. 5% se l'importo dell'ultima ricarica è stato
100€, 10% se 200€). Anche i pagamenti degli abbonamenti avvengono
maediante carta di credito registrata nel sistema.

il sistema viene ulilizzato dai clienti (via-wab) e dai corrieri di EDC (via app)
su smariphone). Questi ultimi devono poter interrogare l sistema per oltenere
la lista degli indirizzi dove ritirare la merce nel giorno corrente e prandearmne in
carica le diverse prenotazioni ancora pendenti. in dettaglio, l sistema data
una città in input, restituisce al comiere la lista degli indinzzi di quella città,
presso | quali è stato prenotato un riliro merce nel giorno comente ancora
pendente (ovvero che non è stato ancora eseguilto o preso n carica da un
allro cormene).,
