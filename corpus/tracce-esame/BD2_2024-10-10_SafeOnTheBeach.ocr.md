# BD2_2024-10-10_SafeOnTheBeach — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2024-10-10_SafeOnTheBeach.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Toni Mancini
Dipartimento di Informatica
http://tmancini.di.uniromal.it

Esame Es.20241010 - Prova scritta del 10 ottobre 2024

I| Ministero dell’Ambiente e della Tutela del Territorio e del Mare congiuntamente con il Ministero
della Salute, per far fronte a un'epidemia causata da un virus particolarmente contagioso e pericoloso,
emette un bando per il progetto e lo sviluppo di un sistema per la gestione controllata degli accessi
turistici alle zone costiere, al fine di favorire un turismo litoraneo responsabile e minimizzare il rischio
di contagio

Si richiede di progettare il sistema SafeOnTheBeach da presentare al Ministero come risposta al
bando esposto

—

Le aree costiere nazionali si classificano in litorali. Di un litorale interessa conoscere, oltre al
nome, la sua estensione in chilometri (km), la lista dei comuni su cui si sviluppa (comuni di cui
interessa sapere il nome e la provincia di appartenenza) e la lista dei mari che lo bagnano. Ad
esempio, il “Litorale di Santa Marinella” si sviluppa nel comune di Santa Marinella (RM), è bagnato
dal (solo) Mar Tirreno e ha un'estensione di 22 km. Un litorale è suddiviso in zone. Una zona, di cui

si vuole conoscere il litorale di appartenenza, è interamente destinata a riserva ambientale oppure a
spiaggia L __

AT fine di garantire il distanziamento fisico tra i visitatori di un litorale, é previsto che ad ogni
zona sia associata una capacità massima, ovvero il numero massimo di visitatori che possono essere
presenti contemporaneamente.

Delle zone è di interesse conoscere anche il nome, la superficie in metri quadrati e la località
dove sono situate. Le località sono caratterizzate da una eventuale frazione di comune, da un
comune di appartenenza e dalle coordinate geografiche del centro. Ogni zona può essere o non

essere accessibile da animali domestici accompagnati (cani, gatti, etc.)

DI ogni riserva ambientale interessano il nome, una descrizione (contenente ad esempio in-
formazioni sulla flora e sulla fauna locale) e la data di istituzione di quel luogo come riserva

ambientale. E

Di ogni spiaggia si vuole conoscere la disponibilità di stabilimenti balneari a pagamento, di servizi
igienici, di servizi bar e di ristorazione. In caso di presenza di bar o ristoranti, se ne vuole conoscere
anche il nome e il numero di telefono. Degli stabilimenti balneari a pagamento, si vuole conoscere
il numero di telefono, il prezzo d'ingresso, il costo dell’affitto giornaliero delle diverse attrezzature
disponibili (ad es., ombrelloni, sedie a sdraio, lettini, etc.)

Gli uUtenti di SafeOn TheBeach possono essere privati o commercianti.

Un commerciante è contraddistinto dalla ragione sociale e dal codice fiscale. | commercianti
possono essere titolari di tre tipi di attività commerciali: stabilimenti balneari a pagamento, bar o
ristoranti. All’iscrizione di un utente commerciante, il sistema deve poter permettere a tale utﬁl1ft dl
associare ciascuna delle proprie attività alla corrispondente zona di appartenenza, purché non si tmtﬂ
di una riserva ambientale. Ogni attività può essere o non essere accessibile da animali domestici
accompagnati (cani, gatti, etc.).

l commercianti devono poter creare eventi pubblici visibili a tutti gli altri utenti di SEE OnThe-
Beach. Di ogni evento pubblico interessa conoscere il nome, una descrizione, il costo del biglietto
(se a pagamento), la portata in termini di numero massimo di persone accettabili, I' attività, tlàemug
e l’ora in cui avrà luogo. Ad esempio, uno stabilimento a pagamento potrebbe o:p%ﬁ il concerto

## Pagina 2

estivo di un famosissimo gruppo blues, facendolo pagare un prezzo maggiorato rispetto all'usuale \
prezzo di ingresso allo stabilimento, e accettare 100 persone i a
\
\
\
|
\

a Gli utenti privati sono 1 reali fruitori finali dei servizi balneari e della movida litoranea. Un utente

privato è contraddistinto dal suo nome, cognome, genere, data e luogo di nascita e dal suo codice
fiscale a iaà e __

— Ùn utente privato deve poter usare SafeOnTheBeach per poter cercare zone (riserve ambientali 1
_ o spiagge) o eventi pubblici di suo interesse. ‘

Gruppi di utenti possono usare SafeOn TheBeach per effettuare prenotazioni, indicando la zona 3
di interesse, il numero di animali accompagnati che compongono il gruppo, l’ora prevista di arrivo e ‘
l'ora prevista di abbandono della zona. __
H AI momento della prenotazione per una zona, gli utenti possono scegliere di prenotare anche ”
|l'accesso a eventi che si svolgono presso attività che si trovano al suo interno. Il sistema rifiutera

prenotazioni che violino il vincolo di capacità massima della zona o degli eventi prenotati (se ve ne

sono).
Per questioni di sicurezza, monitoraggio e tracciamento sanitario, si vuole gestire lo storico degli

accessi da parte degli utenti privati. Pertanto, quando un utente accede ad una zona, il sistema
deve registrare la sua presenza effettiva, l’ora reale di arrivo e di abbandono.
|| sistema SafeOn TheBeach deve fornire le seguenti funzionalità.

|
\
nn
|
\
1
\

PE

{

Inserimento, da parte del Ministero, di un comune italiano

a

|scrizione utente (privato o commerciante)
3 Creazione di un evento da parte di un commerciante
4 Prenotazione dell’accesso a una zona da parte di un gruppo di utenti privati

5 Cancellazione, da parte di un utente, di una prenotazione

6. Accesso di un utente privato a una zona prenotata

7. Data una posizione (latitudine e longitudine), un istante e un intero positivo k, deve essere
possibile calcolare le k zone balneari più vicine alla posizione data, ordinate per densità turistica
attesa, nell’istante dato, crescente. La densità turistica di una zona in un istante (futuro) t
è il rapporto tra la capienza della zona e il numero di utenti che si prevede (in base alle
prenotazioni già effettuate) saranno presenti nella zona all'istante i. (In fase di analisi, si
assuma di avere a disposizione un simbolo di funzione distanza/4, soggetto alla semantica di
mondo reale, che, date le coordinate geografiche di due punti (lat,. lon,) e (lata. lona), valuti
alla distanza tra loro espressa in metri. In fase di progettazione, si assuma che sia disponibile
una funzione definita nel DBMS che la implementi.)

8 Data una località / e un periodo di tempo, il sistema deve permettere di calcolare tutte
le spiagge che si trovano in / presso le cui attività non è stato organizzato nessun evento

all'interno del periodo dato. i
