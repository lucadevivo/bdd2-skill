# BD2_2025-07-17_IttiesseWeb — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2025-07-17_IttiesseWeb.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Proff. Toni Mancini, Marco Esposito
Dipartimento di Informatica
https://raise.uniroma1.it /teaching

Esame Es.20250717 — Prova scritta del 17 luglio 2025

Si vuole progettare lIttiesseWeb, un sistema informativo per la gestione di un ITS (Istituto
Tecnologico Superiore), una scuola di eccellenza ad alta specializzazione tecnologica post diploma
che permette di conseguire il titolo di tecnico superiore. |

Il sistema deve permettere al personale amministrativo, ai docenti e agli studenti di gestire Corsip
moduli; esami e GCarrieré.

L'ITS offre diversi percorsi di formazione, della durata di due anni (suddivisi in un periodo di
lezioni frontali e uno di tirocinio in azienda), chiamati corsi. Ogni corso è identificato dal proprio
nome.

Ogni anno, per ogni corso può essere attivata un'edizione (ad es. "Sviluppo Web e Cloud 2025").

Di ogni edizione interessa conoscere l'anno, il numero di crediti che è necessario accumulare,
superando esami, per poter accedere al tirocinio in azienda, e il numero di crediti necessari per poter
accedere all'esame di stato finale.

Ogni studente (di cui interessa conoscere nome, cognome, data di nascita e codice fiscale) può
essere iscritto a una sola edizione alla volta.

Gli insegnamenti erogati in un'edizione di un corso vengono chiamati moduli (ad es. “"Basi di
Dati 1", “Python 3”, ecc.). Di ogni modulo interessa il nome e i docenti che lo insegnano (con nome,
cognome, indirizzo email e codice fiscale).

| moduli di un'edizione sono raggruppati in blocchi. Tutti i moduli devono far parte di esatta-
mente un blocco.

| progressi degli studenti nei vari moduli vengono valutati periodicamente per mezzo di esami
scritti. Un esame è relativo a un blocco di moduli ed è formato da più prove (un qualsiasi numero,
ma almeno una). Di ogni esame interessa conoscere un codice identificativo (una stringa) e il
periodo di inizio e di fine.

Di ogni prova interessa conoscere il nome (unico rispetto all’esame relativo) e la data (che deve
essere all'interno del periodo dell’esame). Quando uno studente supera l'esame di un blocco, ottiene
dei crediti (un numero intero positivo che dipende dal blocco, non dall'esame), i quali serviranno
per accedere al tirocinio e, in seguito, all'esame finale.

Ogni studente può sostenere esami di un certo blocco un qualsiasi numero di volte, ma solo fino
al superamento (non è possibile “rifiutare” il superamento).

Quando uno studente partecipa ad una prova, ottiene un voto da O a 10. Un esame è considerato
superato da uno studente quando quest'ultimo ha ottenuto un punteggio pari ad almeno 6 in tutte
le prove dell'’esame.

Per evitare che gli studenti seguano un percorso poco strutturato, sono previste delle propedeu-
ticità tra blocchi di moduli. In altre parole, per poter sostenere l'esame di alcuni blocchi è necessario
aver prima superato gli esami di altri blocchi. Di ogni blocco di moduli è di interesse quindi conoscere
i blocchi i cui esami devono essere sostenuti prima di esso.

Una volta che uno studente ha accumulato un numero di crediti sufficienti (tale numero dipende
dall'edizione, si veda sopra), può sostenere il tirocinio in azienda. Di ogni tirocinio interessa conoscere
la data di inizio, quella di fine (alla sua conclusione) e l'azienda coinvolta (di cui sono di interesse

la partita IVA e la ragione sociale, una stringa).

Scansionato con CamScanner

## Pagina 2

Quando lo studente ha terminato il tirocinio e accumulato un numero di crediti sufficienti per
accedere all’esame di stato finale (anch'esso dipendente dall'edizione, si veda sopra) può accedere
a quest'ultimo. L'esame di stato viene considerato superato se si riceve una votazione di almeno
6/10 e non può essere ripetuto.

IttiesseWeb deve essere utilizzato dal personale amministrativo (che gestisce i corsi, le edizioni,
i moduli, i gruppi e gli esami), dai docenti, che somministrano le prove d'esame, e dagli studenti,
che devono poter visualizzare le informazioni riguardanti la propria carriera. Il sistema deve offrire
le seguenti funzionalità avanzate:

e Dato un corso, calcolare l'edizione che ha avuto il numero minore di studenti che hanno
raggiunto i requisiti per sostenere l'esame di stato finale. Uno studente non può accedere
all'esame di stato se (1) non ha accumulato il numero totale di crediti necessari e (2) non ha
terminato il tirocinio.

Scansionato con CamScanner
