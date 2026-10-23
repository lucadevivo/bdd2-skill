# BD2_2022-09-09_MyPrecious — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2022-09-09_MyPrecious.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Facoltà di Ing. dell'lnfurmar.'iane, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Toni Mancini
Dipartimento di Informatica
http: / /tmancini.di.uniromaL.it

Esame Es.20220909 — Prova scritta del 9 Settembre 2022

Si vuole progettare e realizzare MyPrecious, un sistema di gestione di opere d’arte e df:!!& relative
ÉìP_"-'-ÉIMÎ per conto di un museo,. finalizzato all'utilizzo interno. Tramite il sistema, i \fUG!E che
i responsabili del museo possano gestire il patrimonio artistico e organizzare delle esposizioni delle

g 1 — — e ii ia

opere e che il management possa ottenere delle statistiche sulle visite.
Gli utenti di MyPrecious sono i résponsabili della gestione delle opere d'arte del museo e
dell’organizzazione delle esposizioni, __ — t ì
I f È di interesse rappresentare(fe opere à disposizione del museo, con il nome, la categoria (p.es., di-
ì | Pinto, scultura, mosaico, manoscritto, ecc.), l’autore, l’anno di realizzazione, la tecnica (se rilevante)
‘ } e le correnti artistiche alle quali è associata.
i Di un/autore’interessano il nome d'arte, il luogo e la data di nascita, la data di morte e le opere
realizzate che sono di proprietà del museo.
| Alcune opere di proprietà del museo possono essere oggetto di l[estagì’ji. nel qual caso interessa
il periodo di restauro; un'opera in restauro non può essere esposta nel museo” Il sistema deve

fi —

mantenere le informazioni riguardo a tutti i restauri ai quali è stata sottoposta ogni opera di proprietà

&Èî_mrl5ìeì:_Îîj__-:jua_ndu è di sua proprietà. E .
| | responsabili della gestione del patrimonio del museo organizzano le 'esposizioni delle opere, le
quali possono essere permanenti oppure temporanee. EEO e

Le ésposizioni permanenti,) espongono le opere di proprietà del museo e le raggruppano, ad
esempio, per periodo storico.

Lesposizioni temporanee, invece, sono esposizioni speciali che si tengono per periodi di tempo
più o meno brevi (in genere qualche mese) e hanno un tema particolare, come un artista, un gruppo
di artisti, una corrente artistica o un periodo storic

f Di un’ésposizione è di interesse conoscere IQEÈÈ del museo nella quale ha luogo e le opere
| coinvolte. E u

Di un'esposizione temporanea interessa il nome e il periodo di tempo nel quale si tiene.

Il museo vende diversi tipi di bigliettà. Ogni biglietto può essere utilizzato solamente nella data
scelta al momento del suo acquisto, —

Le tipologie di biglietto in vendita sono le seguenti:

1. il biglietto all-access, che dà accesso a tutte le esposizioni, permanenti e temporanee;
2. un biglietto valido per tutte e sole le esposizioni permanenti;

3. un biglietto valido per tutte le esposizioni permanenti ed una sola esposizione temporanea,
quest 'ultima a scelta del visitatore,

Il sistema deve offrire le seguenti funzionalità ai responsabili del patrimonio artistico e al Mmana-
gement:

Fi

. inserimento e rimozione di opere d'arte;

h

registrazione del restauro di un'opera d'arte;

FU .C

## Pagina 2

3. creazione di un'esposizione, con le opere relative;
4. calcolo del numero dei biglietti venduti in un dato giorno;

5. Dato un periodo di tempo, calcolare un resoconto che contenga, per ognuna delle correnti
artistiche note, il numero di artisti che ha realizzato almeno un’opera di proprietà del museo
appartenente a quella corrente, nel periodo dato,

6. dato un periodo di tempo, calcolare l’esposizione temporanea per la quale sono stati venduti
più biglietti nel periodo (considerando tutti i tipi di biglietto rilevanti).
