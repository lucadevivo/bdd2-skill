# BD2_2023-10-20_Atletissimo — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2023-10-20_Atletissimo.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
mazione, Informatica e Gtatistica,
mento di Basi di Dati, Modulo 2

Prof. Toni Mancini

Dipartimento di Informatica

http:/ /tmancini.di uniromal .i

Laurea im Informatica

Facoltà di Ing. dell'Infor
Insegna

Esame Es.20231020 - Prova scritta del 20 Ottobre 2023

per dispositivi mobili che realizza una

Si vuole progettare e realizzare Atletissimo, un sistema
individuale. Dopo alcune interviste con

rete sociale per la gestione di attività di allenamento fisico

il committente è stata prodotta la seguente specifica dei requisiti. .
Cli UteRET di Atletissimo sono gli atleti. Un atleta (o utente) è identificato dal proprio_noma

‘utente (una strin a). Inoltre, di un atleta é di interesse cunaa::r:_,n1ur&n.:a;nnﬂll:..il …11.]11u4

data di nascita. Opzionalmente, un utente può anche fornire al sistema il_proprio.pesa.e.la propria
Jtezza. La socialità del sistema Atletissimo si realizza nella possibilità di due atleti di essere amici)

Un Utente può avere molti amici.
Gli utenti usano Atletissimo per tracciare la propria

nel sistema interessa conoscere Îl nome, una
ai quali è rivolto. Ad esempio, l’esercizio “Plank" indicherà “retto dell’addome”, "erettore spinale”

e “trasverso dell’addome” come muscoli presi di mira. Atletissimo mette a disposizione degli atleti
degli [allenamenti] cioè $equenze di eserr:izu}tudìate appositamente da esperti per allenare specifici

attività fisica. Di ogni lesercizioamemorizzato

gruppi di muscoli. Un allena nto-tra uni fiome, una descrizione ed è rappresentato da una sequenza
‘ordinata di esercizi (ogni esercizio può anche ripetersi) e di pause (una pausa può essere vista come

un esercizio “speciale"); di ogni/esercizio nella sequenza Anteressa CONOsCEre il numero di ripetizioni 7
(un intero). OgniGllenamento, inoltre, garantisce agli atleti che lo completano un certo numero di ‘
punti, con i quali vengono stilate delle classifiche.

Gli atleti interagiscono con Atletissimo scegliendo un allenamento e comunicando il completa-

mento dei singoli esercizi. Un atleta può anche decidere di non completare un allenamento; delle

xesgfan.-‘ completate parzialmente è comunque di interesse conoscere gli esercizi completati. Di ogni
sessione completata (totalmente o parzialmente) inte l'istante di fipe. Di ogni

;:-|::e d|'allecll1.'a;înenta interessa conoscere, oltre all'utente e all'allenamento scelto, l'istante di inizio

ermine della sessione, viene memorizzato l'istante di fine e vi o :

i ' : e viene data la possibilità all' i

comunicare al sistema il grado di difti in i E à all'atleta di

Una caratteristica innovativa del si ‘ecimo è ' :

sistema Atletissimo è la possibilità i i di i
s : ' i per gli atleti di sfid |
agli altri utenti. In particolare, ogni utente può creare una nuova sfida, assgegnandg]Eplrlnnpnùn"mE e È

ÉUÈId-ÈÉLÉ|!EÈ“ Esistono due tipi di sfida. Il primo è la Sfida "a tempo”) in.cui bisogna comolet
er_intero) una sessione di un certo allenamento entro in_cui bisogna completare
S certo allenamento entro un tempo massimo; il decor i S

a ac : :

“ogni atleta ﬁ…piﬂtt]E:rr:l:'!ulg%e.-;u"%l;îtjg' n!-lp.'l_erù—lîh—Punti (completando allenamenti a scelta di
d P Ine del periodo di durata della sfida. Una volta che una sfid

a

L
.|_' .I'-Ì':._dl,:‘:_-.":"‘:‘_.-|'l-

._..-e g:l partel::iparvi fintantoché essa è attiva.
a Atletissimo fornire le seguenti funzionalità:

d : A
parte di un amministratore del| sistema

d

## Pagina 2

e Creazione di una sfida da parte di un atleta, con tutte le caratteristiche necessarie.

e Partecipazione a una sfida da parte di un atleta.

e Dato un atleta e un insieme di esercizi, per ogni esercizio dato, il calcolo del numero di
sfide superate con successo dall'atleta che includano almeno un allenamento che, a sua volta,

‘ncluda l'esercizio. (€s@ — o , ia L)

e Il calcolo degli atleti che, in un periodo dato, hanno completato almeno una settimana pertetta.
Un atleta completa una settimana perfetta se completa totalmente almeno un allenamento

per 7 giorni consecutivi.
