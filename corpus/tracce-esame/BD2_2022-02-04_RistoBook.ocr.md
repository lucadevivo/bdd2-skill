# BD2_2022-02-04_RistoBook — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2022-02-04_RistoBook.pdf`.** Questo testo viene da un OCR
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
http:/ /tmancimni . di.uniromal.it

Esame Es.20220204 — Prova scritta del 4 febbraio 2022

gà

Si vuole progettare e realizzare RistoBook, un'applicazione web per creare e gestire prenotazioni per
__ — _-_—_\_\_\-\- ;

ristoranti-
Il sistema deve permettere ai clienti di effettuare prenotazioni presso i@tnran‘tl iscritti, usufruendo,

; I ."-""—"-'=:- Fi s I è E # i T d ; a i
eventualmente, di.\pfùf'ﬂ-[_]_jgghf. il ristoratori, INVvECE, possono Iscriversi per registrare 1 propri ristoranti

e gestire le loro prenotazioni € le loro promaozioni.
Èg[,aìì.t_ìﬁntereaaa il nome,

Deì@nteressa conoscere il nome e l’indirizzo e-mail, mentre deiîr
la partita IVA (una stringa numerica), l'indirizzo, la città e l'insieme di tipologie di cucina offerte

(scelte da una lista tenuta sotto controllo dallo staff di RistoBook).

I clienti possono prenotare presso un ristorante specificando il giorno, l'ora e il numero di commensali.
Le prenotazioni dei clienti devono essere confermate (o rifiutate) dal personale incaricato dei rispettivi

ristoranti, che devono poter accedere ad RistoBook tramiteé una interfaccia dedicata.

Uno dei punti di forza del modello di business di RistoBook è la possibilità per i ristoranti di offrire e

pubblicizzare scontistiche (dette promozioni). In particolare, | ristoratori devono poter definire una
promozione specificando una percentuale di sconto sulle prenotazioni consumateé in un certo periodo

di tempo. Tali promozioni sono valide per al massimo un certo numero di coperti al giorno.

Ad esempio, un ristorante potrebbe definire la seguente promozione: sconto del 20% sulle prenota-
zioni dalle 20 alle 22 da martedì 15 giugno 2022 a venerdì 18 giugno 2022, valido per al massimo

10 coperti al giorno. Un altro ristorante potrebbe definire invece una promozione del tipo: sconto
del 25% sulle prenotazioni dalle 18 alle 19 di tutti | martedì e giovedì dal 1 ottobre al 31 dicembre

2022.
AI momento della prenotazione, il cliente può scegliere una delle promozioni ancora disponibili {anche

nessuna, se lo desidera).

- . AME

quando una prenotazione viene creata, questa è nello stato “pendente”. Iliristoratore] può scegliere se
e S ;
notazione, questa viene

accettarla o rifiutarla. Quando il cliente usufruisce effettivamente della pre
contrassegnata come “completata”. Se, invece, il cliente non dovesse presentarsi al ristorante, il
ristoratore contrassegnerà la prenotazione come “non utilizzata . Inoltre, in ogni momento {prima
del giorno ed ora prenotati) i clienti possono annullare le proprie prenotazioni, anche se già accettate.
Infine, in caso di tutto esaurito (o per altre ragioni, ad es. giorni di chiusura), il responsabile di un

ristorante deve poter chiudere le prenotazioni per un certo lasso di tempo (ad es., una certa data
e fascia oraria, o un'intera settimana): da quel momento in poi, RistoBook non consentirà più ai

clienti di richiedere prenotazioni in quel lasso di tempo (a meno che il ristoratore non le riapra).

Il sistema deve otfftrire, oltre quelle già descritte, le seguenti funzionalità ai suoi attori:

| e Il sistema deve permettere ristoratori di RistoBook di calcolare alcune statistiche di utilizzo
delle loro promozioni. In particolare, dato un periodo di tempo, RistoBook deve permettere
ti al giorno

— —
calcolare, per ogni promozione del ristorante considerato, il numero medio di clien
” ai — | H---_\—-_-'-——-u-l——-.__.-— __ —

## Pagina 2

’ (dove la media è calcolata sui giorni di validità della promozione) che
promozione-in_una prenotazione.

ha_utilizzato quella

e Data una città x, un insieme di tipologie di cucina C, un tasso di sconto minimo s ed una

data dî clienti devono poter trovare quali sono i ristoranti nella città x che offrono almeno

| una delle tipologie di cucina in C' e prevedono promozioni con sconti di tasso almeno s nella
| data d ancora utilizzabili per il numero di coperti che sono interessati a prenotare.

!
i
