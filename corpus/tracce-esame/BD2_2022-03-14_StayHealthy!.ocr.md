# BD2_2022-03-14_StayHealthy! — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2022-03-14_StayHealthy!.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Toni Mancini
Dipartimento di Informatica
http://tmancini.di.uniromal.it

Esame Es.20220314 — Prova scritta del 14 marzo 2022

Si vuole progettare StayHealthy!, una nuova applicazione che permetta agli utenti di monitorare
|…azun…ne tracciando i cibi-che-ingeriscono-giornalmente (con relative quantità e nutrienti)
per tenere sotto controllo apporto calorico ed equilibrio della loro dieta.

A seguito di interviste con il committente, è stata stilata la seguente specifica dei requisiti.

StayHealthy! deve consentire agli utenti di registrarsi al servizio fornendo nome, cognome,
nazionalità, email e : l | j
- StayHealthy! deve fornire un archivio di schede alimenti (cibi e bevande). Tale arehivio_viene
continuamente esteso, oltre che dalla redazione di SÎayHealthy' anche dagli stessi utenti. Per

ai i_

ogni alimento presente nell'archivio, la relativa scheda deve permettere di r. rappresentare il nome, la
marca (se disponibile), la grandezza della confezione (se d|5pùﬂlbll&) il codice identificativo (una
stringa) codificato nel codice a barre della confezione (se disponibile), il relativo apporto calorieo
…]…dLBJLDJEDID il_valore di tale unità (ad es., per i cibi liquidi: Wîanl1ch
grammi o ettogrammi o chnlogrammu per alimenti come le uova, unità), la a quantità (in unità di
alimento) di una par:«::un_g;;f.anclazd…-qlt_re che la quantità (questa volta sempre in grammi, per
garantire uniformità) di ogni nutriente per unità di alimento.

‘ La lista dei nutrienti è tipicamente stabile ed uguale per tutti gli alimenti (ad es., carboidrati
totali, zuccheri, proteine, grassi totali, grassi saturi, grassi insaturi, sodio, potassio, fibre, alcol,
etc.)[ ma StayHealthy! deve fare in modo che tale lista sia estendibile dall'autore dell’inserimento di

RE

una scheda a alimento.] Viceversa, StayHealthy! deve permetteîl "inserimento di schede alimenti che
non h

q…u&lg____ger i nu;rmn_t,___deﬁmtu up:mnah La h5ta den nutnentu DDEIÙHE|I è dehmta dalla

A NLoLA

per er definizione, ap:mnah .5. mu5tranu di seguito alcuni"esempi di schede alimento:

— l

“tin, a s = Siniilil RO EE IE

Fusilli Di Chicco (formato n. 34)

e Codice identificativo: "8033829843"
e Unità di alimento: 100 grammi

e kCal per unità di alimento (ovvero per 100 grammi): 351
.

L

Porzione standard: 0.7 unità di alimento (ovvero 70 grammi)

i

Nutrienti (in grammi per 100 grammi di prodotto; *: nutrienti obbligatori):

— Grassi totali*: 1.5 g — Zuccheri*: 3.4 g — Sale: O g
— Grassi saturi*: 0.3 g — Fibre": 2.9 g
— Carboidrati*: 69 g — Proteine*: 14 g

Buzz Cola

e Codice identificativo: "11928322032"

e Unità di alimento: 100 mil

® kCal per unità di alimento (ovvero per 100 ml): 42

® Porzione standard: 3.3 unità di alimento (ovvero 330 mil)

e Nutrienti (in grammi per 100 ml di prodotto; *: nutrienti obbligatori):

## Pagina 2

— Grassi totali*: O g - Fibre“: 0 g - Fosforo: 0.01 g

— Grassi saturi*: O g - Proteine": 0 g — Potassio: 0.002 g \
— Carboidrati*: 11 g — Caffeina: 0.008 g — Ferro: 0.00011 g

— Zuccheri*: 11 g - (Calcio: 0.002 g — Sale: 0.001 g ]

Come detto, schede relative a nuovi alimenti possono essere aggiunte in ogni momento dalla
redazione di StayHealthy!, ma anche da parte degli utenti, che quindi possono contribujre in prima
persona all’ampliamento dell'archivio degli alimenti di StayHealthy!. Mentre le schede di alimenti
inserite dalla redazione diventano subito pubbliche e visibili a tutti gli utenti, le schede aggiunte
da utenti devono attraversare un processo « di validazione, Una volta validate diventano pubbliche

————— _ —_—_— —

esattamente come quelle inserite dalla redazione.

| Una scheda alimento inserita da un utente viene resa pubblica quando almeno 10 utenti l'hanno
d|::hlarata valida) Fintantoché una scheda non supera il processo di validazione, può ancora essere
ottenuta come risultato di una ricerca, ma può essere utilizzata (ad es., inserita in un diario alimen-

rN cote tare) solo da parte dell'utente che l'ha cr;>mp]lata e di quelli che l'hanno dichiarata valida fino a quel
Èùrnle_îjfd'ﬁîqueatu modo si vogliono incentivare gli utenti interessati ad inserire quell'alimento a

contribuire alla validazione della relativa scheda).
Nel tempo, le schede alimenti (sia quelle inserite dalla redazione che quelle inserite dagli utenti
e diventate pubbliche a seguito di validazione) possono essere invalidate (ad es., perché obsolete,
vi .. « OLO si pensi al caso in cui un alimento confezionato cambi profilo nutrizionale perché prodotto con una
A s ii nuova ricetta). Questo avviene quando 100 utenti le hanno dichiarate non più valide. Le schede
AN "i“" :' a invalidate diventano inaccessibili a tutti gli utenti (tranne che, per le schede inizialmente inserite-da

PE e © iN un utente, all'utente che le ha msente)

u Gli utenti, durante la loro giornata, inseriscono in StayHealthy! la composizione dei loro pasti

(diario alimentare), in termini di alimenti ingeriti e relative quantità. L'insieme dei pasti è attual-
mente definito dalla redazione di StayHealthy! come: colazione, pranzo, snack e cena, ma potrebbe
essere oggetto di estensioni e perfino di personalizzazioni in futuro.

Il sistema deve permettere di calcolare una serie di statistiche riguardo il diario alimentare di
un utente in un certo giorno. In particolare: (i) Numero totale di kCal ingerite; (ii) grammi totali
ingeriti di ogni nutriente.

Gli utenti -di-StayHealthy! possono acquistare abbonamenti Premium (la cui durata dipende

dalla tipulugia di abbonamento scelta tra quelle previste), durante i quali avranno-accesso a servizi

non offerti ai clienti _ Free. IL servizio principale offerto da StayHealthy! ai clienti Premium è relativo

alla assis assistenza di coloro che desiderano seguire una dieta,
— te diete sono definite dai singoli utenti e sono private. Una dieta definisce delle regole, in

termini di soglie minime e massime per alcune delle statistiche giornaliere di cui sopra. Ad esempio,
un utente Premium che vuole perdere peso può definire una dieta, che decide di chiamare ‘ipocalorica
ed iperproteica”, con le seguenti regole circa le kCal totali e le quantità di nutrienti ingeriti al giorno:

Dieta: ‘ipocalorica ed iperproteica”

1. KkCal totali: tra 1300 e 1500 5. Grassi saturi: < 10 g
2. Carboidrati totali: tra 150 e 180 g 6. Sale:; < 3 g

3. Zuccheri: < 30 g 7. Fibre: tra 35 e 40 g
4. Proteine totali: tra 80 e 110 g

StayHealthy! deve restituire, all' utente Premium che sta seguendo una dieta, le regole della

“ii 7-

dieta che ha violato in un certo giorno.
