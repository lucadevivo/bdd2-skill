# BD2_2023-03-17_AllenaMondo — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2023-03-17_AllenaMondo.pdf`.** Questo testo viene da un OCR
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
http:/ /tmancini.di.uniromaL.it

Esame Es.20230317 - Prova scritta del 17 Marzo 2023

Si richiede di progettare AllenaMondo, un sistema web che realizza una rete sociale per la
gestione delle attività sportive personali e collettive, amatoriali e competitive. A tal fine si trascrive
di seguito il risultato della raccolta dei requisiti con alcuni esperti del dominio.

Gli utenti di AllenaMondo sono gli sportivi. Uno sportivo (o utente) è identificato dal proprio
nome utente (una stringa). \Inoltre, di uno sportivo è di interesse conoscere nome, cognome, il
genere (maschio o femmina) e la sua data di naacil:î]ﬁpziunalmente, un utente può anche fornire
al sistema il proprio peso e la propria al_t_g;gj La socialità del sistema AllenaMondo sì realizza nella
possibilità per due sportivi di essere amici. Un utente può avere molti amici.

Gli utenti usano AllenaMondo per tracciare la loro attività 51::n::nrti1..r_i::\\_i5 Di ogni sport memorizzato
_ nel sistema interessa il nome ed una descrizione testuale.

Gli sportivi interagiscono con AllenaMondo comunicando le loro attività di allenamento quoti-
diane (via web o app per smartphone). In particolare, di ogni attività di allenamento di un utente,
AllenaMondo memorizza lo sport esercitato, gli istanti di inizio e di fine, e (opzionalmente) un
valore tra _1 e 5 che rappresenta la “difficoltà” dell'allenamento, come percepita dallo stesso uten-
te. | Inoltre, durante un allenamento, uno sportivo può chiedere a AllenaMondo di memorizzare il
percorso 5EEUiÈQ_.TUEEIFIEÌÙ il suo smartphone. In questo caso, l'app per smartphone di AllenaMondo,
durante l'allenamento, comunica periodicamente (ogni qualche secondo)/ al sistema le coordinate
geografiche (latitudine e longitudine) della posizione dell'utente. Il percorso rappresentato dalla se-
quenza di tali coordinate (con i relativi istanti di tempo) viene associato all'attività di allenamento.
Successivamente, l'utente può decidere di rendere pubblico tale percorso (assegnandogli un nome
ed un commento testuale), di modo che anche gli altri utenti possano visualizzarlo su una mappa.

Una caratteristica innovativa del sistema AllenaMondo è la possibilità per gli sportivi di sfidarsi,
singolarmente oppure in squadre. In particolare, ogni utente può creare una nuova sfida, assegnan-
dole una tipologia ("tra squadre" o “tra singoli"), un nome, il periodo di durata, la durata minima di
un allenamento affinché sia valido per la sfida, gli sport esercitabili (uno o più) e la categoria ("più
chilometri”" o “più allenamenti"). In caso una sfida sia tra squadre, l'utente creatore della sfida deve
anche definire il numero massimo di partecipanti per ogni squadra.

— Una volta che una sfida viene creata, ogni utente può parteciparvi, singolarmente (se la sfida è
“tra singoli") oppure iscrivendosi ad una squadra (se la sfida è “tra wdm-"i Delle squadre, che

sono limitate ad una singola sfida, interessa il nome e l'insieme dei componenti. Si noti che uno

sportivo non può appartenere a due squadre nell'ambito di una stessa sfida. _

La partecipazione da parte di uno sportivo ad una sfida si sostanzia nell'effettuare attività di
3llenamento relative agli sport e nell'arco temporale previsti dalla sfida. La sfida è vinta dall'individuo
o squadra che totalizza il massimo punteggio. Per le sfide di categoria “ più chilometri", il punteggio
di un utente o squadra è la somma dei chilometri percorsi nelle sue attività di allenamento validi
per la sfida. Per le sfide di categoria ‘ più allenamenti", il punteggio è invece dato dal numero
complessivo di allenamenti validi. AllenaMondo deve associare ad ogni utente tutte le sfide da lui

create o a cui ha partecipato.
Il sistema AllenaMondo deve fornire le seguenti funzionalità.

e Registrazione al servizio da parte di un utente web.

1

## Pagina 2

e Inserimento di un nuovo sport da parte di un amministratore del sistema. U

Inserimento di una nuova attività di allenamento da parte di uno sportivo, con tutte le

U

L
informazioni richieste. \/

e Creazione di una sfida da parte di uno sportivo, con tutte le caratteristiche necessarie.

Creazione di una squadra per una sfida da parte di uno sportivo, con tutte le caratteristiche

i F
necessarie. V

e Sottoscrizione di uno sportivo a una sfida (come singolo o come membro di una squadra) \/

Ogni utente deve poter calcolare un resoconto degli allenamenti che ha effettuato in un dato peric.-dc::
di tempo. In particolare, per ognuno degli sport praticati, si vuole conoscere il tempo-totale _ di

allenamento ed il numero f;nt_zie_;::li_-t_hiùme_t[i_p_l.ìll*:ﬁtìî. , L AO
Infine, il sistema deve permettere il calcolo dello sport maggiormente praticato dag-|1 amici di un
certo sportivo in un dato periodo di tempo. In particolare, lo sport maggiormente praticato è quello

a cui è stato dedicato il maggior tempo totale (si noti che potrebbero esserci più sport nel risultato,
in caso il tempo totale praticato per questi dovesse essere lo stesso).
