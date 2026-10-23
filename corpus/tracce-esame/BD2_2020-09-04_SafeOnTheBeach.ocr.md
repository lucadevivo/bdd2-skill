# BD2_2020-09-04_SafeOnTheBeach — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2020-09-04_SafeOnTheBeach.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Il Ministero dell'Ambiente e della Tutela del Territorio e del Mare congiuntamente con il Ministero
della Salute, per far fronte a un'epidemia causata da un virus particolarmente contagioso e pericoloso,
emette un bando per il progetto e lo sviluppo di un sistema per la gestione controllata degli accessi
turistici alle zone costiere, al fine di favorire un turismo litoraneo responsabile e minimizzare il rischio
di contagio.

Si richiede di progettare il sistema SafeOnTheBeach da presentare al Ministero come risposta al
bando esposto.

Le aree costiere nazionali si classificano in litorali. Di un litorale interessa conoscere, oltre al
nome, la sua estensione in chilometri (km), la lista dei comuni su cui si sviluppa (comuni di cui
interessa sapere il nome e la provincia di appartenenza) e la lista dei mari che lo bagnano. Ad
esempio, il “Litorale di Santa Marinella” si sviluppa nel comune di Santa Marinella (RM), è bagnato
dal (solo) Mar Tirreno e ha un'estensione di 22 km. Un litorale è suddiviso in zone. Una zona, di cui
si vuole conoscere il litorale di appartenenza, è interamente destinata a riserva ambientale oppure a
spiaggia.

AI fine di garantire il distanziamento fisico tra i visitatori di un litorale, è previsto che ad ogni
zona sia associata una capacità massima, ovvero il numero massimo di visitatori che possono essere
presenti contemporaneamente.

Delle zone è di interesse conoscere anche il nome, la superficie in metri quadrati e la località
dove sono situate. Le località sono caratterizzate da una eventuale frazione di comune, da un
comune di appartenenza e dalle coordinate geografiche del centro. Ogni zona può essere 0 non
essere accessibile da animali domestici accompagnati (cani, gatti, etec.)

Di ogni riserva ambientale interessano il nome, una descrizione (contenente ad esempio —m-

farmazmm sulla flora e suila fauna l0cale) e la data di istituzione di quel luogo come rise

vv n G j d B T SEO G D g e

## Pagina 2

Di ogni spiaggia si vuole conoscere la disponibilità di stabilimenti balneari a pagamento, di servizi
igienici, di servizi bar e di ristorazione. In caso di presenza di bar o ristoranti, se ne vuole conoscere
anche il nome e il numero di telefono. Degli stabilimenti balneari a pagamento, si vuole conoscere
il numero di telefono, il prezzo d'ingresso, il costo dell’affitto giornaliero di attrezzature (ad es.,
ombrelloni, sedie a sdraio, lettini, etc.)

Gli utenti di SafeOnTheBeach possono essere privati o commercianti.

Un commerciante è contraddistinto dalla ragione sociale e dal codice fiscale. | commercianti
possono essere titolari di tre tipi di attività commerciali: stabilimenti balneari a pagamento, bar o
ristoranti. All’iscrizione di un utente commerciante, il sistema deve poter permettere a tale utente di
associare ciascuna delle proprie attività alla corrispondente zona di appartenenza, purché non si tratti
di una riserva ambientale. Ogni attività può essere o non essere accessibile da animali domestici
accompagnati (cani, gatti, etc.).

| commercianti devono poter creare eventi pubblici visibili a tutti gli altri utenti di SafeOn The-
Beach. Di ogni evento pubblico interessa conoscere il nome, una descrizione, il costo del biglietto
(se a pagamento), la portata in termini di numero massimo di persone accettabili, la zona, il giorno
e l'ora in cui avrà luogo. Ad esempio, uno stabilimento a pagamento potrebbe ospitare il concerto

## Pagina 3

1

estivo di un famosissimo gruppo blues, facendolo pagare un prezzo maggiorato rispetto all'usuale
prezzo di ingresso allo stabilimento, e accettare 100 persone.

Gli utenti privati sono i reali fruitori finali dei servizi balneari e della movida litoranea. Un utente
privato è contraddistinto dal suo nome, cognome, genere, data e luogo di nascita e dal suo codice
fiscale.

Un utente privato deve poter usare SafeOnTheBeach per poter cercare zone (riserve ambientali
o spiagge) o eventi pubblici di suo interesse.

Gruppi di utenti possono usare SafeOnTheBeach per effettuare prenotazioni, indicando la zona
di interesse, il numero di animali accompagnati che compongono il gruppo, l'ora prevista di arrivo e
l'ora prevista di abbandono della zona.

A| momento della prenotazione per una zona, gli utenti possono scegliere di prenotare anche
l'accesso a eventi che si svolgono in attività che si trovano al suo interno. Il sistena rifiuterà
prenotazioni che violino il vincolo di capacità massima della zona o degli eventi prenotati (se ve ne
sono).

Per questioni di sicurezza, monitoraggio e tracciamento sanitario, si vuole gestire lo storico degli
accessi da parte degli utenti privati. Pertanto, quando un utente accede ad una zona, il sistena
deve registrare la sua presenza effettiva, l’ora reale di arrivo e di abbandono.

Il sistema SafeOnTheBeach deve fornire le seguecnti funzionalità.

1. Inserimento, da parte del Ministero, di un comune italiano

9. |scrizione utente (privato o commerciante)

3. Creazione di un evento da parte di un commerciante

## Pagina 4

1. Inserimento, da parte del Ministero, di un comune italiano
Iscrizione utente (privato o commerciante)
Creazione di un evento da parte di un commerciante

Prenotazione dell'accesso a una zona da parte di un gruppo di utenti privati

Cancellazione, da parte di un utente, di una prenotazione

R ET CMA

Accesso di un utente privato a una zona prenotata

7. Ricerca degli eventi non ancora terminati più gettonati nella zona, cioè con un numero di

prenotazioni (una prenotazione conta per il numero di partecipanti del gruppo) più alto della
media

8. Data una zona balneare, il sistema deve poter calcolare la disponibilità attuale di posti in tale
zona rispetto alla sua capienza massima. Ad esempio, se una zona ha una capienza di 100
persone e 10 persone al suo interno, il numero di posti disponibili-è 100 — 10 = 90.

LI
LL
LI
l
l
‘i
4
ii
j
|=)
[
KE
P
F
l
