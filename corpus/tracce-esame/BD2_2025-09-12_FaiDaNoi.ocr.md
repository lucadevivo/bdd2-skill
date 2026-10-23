# BD2_2025-09-12_FaiDaNoi — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2025-09-12_FaiDaNoi.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell’Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Proff. Toni Mancini, Marco Esposito
Dipartimento di Informatica
https:/ /raise.uniromal.it /teaching

Esame Es.20250912 — Prova scritta del 12 settembre 2025

Si vuole progettare FaiDaNoi, un sistema informativo per la gestione di un negozio specializzato
nella vendita e noleggio di attrezzatura per il fai da te. Il sistema ha lo scopo di modernizzare e
integrare la gestione delle vendite, dei servizi di noleggio, della prenotazione di spazi di lavoro e
dell'organizzazione di corsi di formazione per la clientela.

l sistema dovrà essere utilizzato da diverse tipologie di utenti: | clienti che acquistano prodotti
e usufruiscono dei servizi, il personale di vendita che gestisce le transazioni e il magazzino, | tecnici
responsabili della manutenzione delle attrezzature e i manager del negozio, che necessitano di
accedere a report e statistiche per l'analisi delle performance.

— | dati di interesse principali riguardano i prodotti in vendita, le attrezzature a noleggio, | clienti
registrati, le postazioni di lavoro, i corsi di formazione e tutte le transazioni economiche e logistiche
che ne derivano. FE NEE

Ogni _E1'ÉÉÈÌEP_Ì_D_HÉEÉÌ'EEI è caratterizzato da un codice a barre univoco, nome, marca, una © più
categorie di appartenenza (es. “utensili elettrici”, ‘“viteria”, “legnami”"), una descrizione e il prezzo di
vendita.

Non è richiesto che il sistema FaiDaNoi gestisca le scorte di prodotti disponibili in magazzino
(numero di pezzi, carichi in ingresso, ecc.), che sono invece gestite tramite un servizio esterno.

Alcuni prodotti possono esistere in più varianti (ad esempio, un trapano può avere diverse potenze
o un set di chiavi diverse misure), ognuna con _uì_1 proprio codice specifico e prezzo.

| clienti possono registrarsi al cistema fornendo i propri dati anagrafici (nome, cognome, codice
fiscale, indirizzo email e numero di telefono). La registrazione permette di accedere a una cronologia
dei propri acquisti e noleggi. Il sistema deve supportare un programma fedeltà a più_ livelli (ad
esempio “Bronzo”, "Argento”, “Oro"”, ecc.). Ogni livello è definito da un nome, una soglia di spesa
per essere raggiunto e una percentuale di sconto applicata automaticamente su tutti gli acquisti e
noleggi effettuati da clienti con tale livello. Si noti che per il raggiungimento di un livello contano

Ktutte le spese effettuate dal cliente a partire dal momento della registrazione. Dunque, una v-:;-1taì
raggiunto un livello, non se ne perderanno mai i vantaggi (ma sarà sempre possibile raggiungere
livelli superiori).

Il servizio di noleggio attrezzaturé gestisce un parco di macchinari specifici (ad es. levigatrici
professionali, seghe a nastro, ecc.). Di ogni attrezzatura a noleggio interessa conoscere un codice
identificativo unico, il modello, lo stato attuale (uno tra “disponibile’, “noleggiato”, “in manutenzio-
ne", “rotto”), la tariffa di noleggio giornaliera e l'ammontare della cauzione richiesta. Ogni operazione
di giolepgio deve registrare il cliente, l’attrezzatura noleggiata, la data di inizio e la data di fine previ-

iGi

sta. AI momento della restituzione, viene registrata ]a data di rientro effettiva e l'esito del controllo
sull’integrità del bene.

Il negozio mette a disposizione dei clienti delle postazioni di lavoro attrezzate, noleggiabili a ore.
Di ogni postazione interessa conoscere un codice identificativo, la tariffa oraria e le attrezzature
pesanti incluse (es. ' banco da falegname con morsa”, "postazione di saldatura”). Le postazioni

possono essere pienota e-dai clienti per uno specifico giorno e un intervallo di orari (con “scatti
_ |l sistema deve gestire un calendario delle prenotazioni per ogni postazione, evitando

di/mezz'

sovrapposizioni. P
q——_— _ e

## Pagina 2

Vengono inoltre organizzati corsi di gruppo su specifiche tematiche (es. ‘ Corso base di fale-
gnameria”, “Tecniche di verniciatura”). Per ogni corso sono specificati un titolo, una descrizione
dettagliata degli argomenti, ‘l costo di iscrizione, la data e l'ora di svolgimento, il numero massimo
di partecipanti e il membro del personale che lo terrà in qualità di istruttore. | clienti registrati
possono iscriversi ai corsi fino al raggiungimento della capienza massima. Îl sistema deve tracciare
le iscrizioni di ogni cliente.

|l sistema deve offrire le seguenti funzionalità avanzate:

e Dato un intervallo di date, il management deve poter generare Uf report che, per ognuna
delle categorie di prodotto, mostri il ricavo totale derivante dalle vendite e quello derivante
dai noleggi (considerando, quindi, anche gli sconti applicati grazie al programma fedeltà).

e || sistema deve permettere al personale di ‘dentificare i “super clienti" da invitare a eventi
esclusivi. Un “super cliente" è definito come un cliente che possiede il livello più alto del
programma fedeltà e che ha partecipato ad almeno due corsi diversi nell'anno solare corrente.
