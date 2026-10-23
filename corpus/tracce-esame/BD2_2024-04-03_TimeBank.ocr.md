# BD2_2024-04-03_TimeBank — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2024-04-03_TimeBank.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma |
Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Toni Mancini
Dipartimento di Informatica
http://tmancini.di.uniromaLl.it

Esame Es.20240403 — Prova scritta del 03 aprile 2024

Si vuole progettare e realizzare TimeBank, un sistema che fornisca i servizi di una “banca del
tempo”. Tale sistema sarà utilizzato tramite client quali applicazioni per smartphone e browser web.

Gli utenti di TimeBank possono prendere in prestito ed offrire ore del loro tempo libero ad altri
utenti, per soddisfare i loro bisogni reciproci. Lo scopo è quello di supportare forme di scambio e
aiuto reciproco instaurando una rete di relazioni sociali. i

In breve, tutti gli utenti dichiarano l’intenzione di volersi mettere a disposizione per un certo
insieme di prestazioni (ad es., “riparazioni domestiche", “corsi di inglese”, ecc.). Queste vengono
chiamate le abilità messe a disposizione dai singoli utenti. Tali abilità possono essere richieste dagli
altri utenti per risolvere delle loro necessità.

Ad esempio, I' utente Alice (esperta di corsi di inglese e babysitting), lamenta una perdita d'acqua
in casa; utilizzando TimeBank, si mette in contatto con l’utente Biagio —che sa effettuare riparazioni
domestiche. | due utenti si accordano per una prestazione della durata di 2 ore in un certo giorno.

Queste interazioni tra utenti vengono chiamate "scambi di tempo”. Al momento dello scambio i
di tempo, Alice (l’utente richiedente lo scambio) “pagherà” Biagio (utente offerente) un importo
per il servizio richiesto. Pertanto il ’saldo-tempo” di Alice subirà un addebito pari al valore dello
scambio, mentre quello di Biagio subirà un accredito dello stesso importo. D'altro canto, Alice potrà
aumentare il proprio “saldo-tempo” offrendo ore per insegnare l'inglese agli altri utenti di TimeBank,
ricevendo da questi i rispettivi pagamenti. i

Si osservi che il valore di uno scambio di tempo si basa sulla sua durata, e non sulla tipologia
del servizio offerto. Infine, si noti che TimeBank non prevede, in nessun caso, scambio di denaro
tra gli utenti.

Degli utenti dell’applicazione sono di interesse iîl nome, il cognome, l'indirizzo email e il numero
di telefono. Inoltre, per ognuno interessa conoscere le abilità messe a disposizione (di cui interessa
il nome), e gli scambi di tempo che intercorrono tra coppie di utenti (non è prevista la possibilità di
scambi di tempo che coinvolgano più di due utenti. Degli scambi interessa la data e l’ora di inizio,
la durata (in ore), e la particolare abilità richiesta all'utente offerente.

TimeBank deve permettere ad ogni utente che richieda una prestazione di esprimere un giudizio
(feedback) da 1 a 10 sulla qualità del servizio ricevuto.

Il valore del tempo scambiato non è sempre lo stesso, ma dipende dalla qualità dei feedback
ricevuti dall'utente offerente. In particolare, deve essere possibile calcolare, per ogni utente e per
ogni sua abilità, il suo moltiplicatore; il valore di uno scambio sarà quindi dato dal prodotto della
sua durata e del moltiplicatore associato all’utente rispetto all'abilità oggetto dello scambio.

Più precisamente, sia d la durata dello scambio, t l'istante in cui avviene lo scambio, u l’utente
offerente, a l'abilità richiesta, m la media dei feedback ottenuti da u per tutti gli scambi avvenuti
prima di t în cui ha offerto la propria abilità a, il valore dello scambio è calcolato come:

vlu,a,t, d) = d (1 + arctan(0.05 * m)).
AI momento di inizio di uno scambio di tempo, il saldo-tempo dell'utente offerente viene ac-

creditato di un importo pari al valore dello scambio, mentre quello dell'utente richiedente viene
addebitato dello stesso importo,

## Pagina 2

In ogni momento, per gli utenti di TimeBank si deve poter calcolare il saldo-tempo, che è pari
alla somma dei valori degli scambi offerti meno i valori di quelli richiesti.

Si noti che, in ogni momento, il saldo di tutti gli utenti deve essere maggiore o uguale a zero
(cioè gli utenti non possono andare in ‘rosso”"). Pertanto, un utente non può richiedere uno scambio
di tempo se si prevede che, al momento di inizio di tale scambio, non abbia credito sufficiente a
pagarlo. Tuttavia, al fine di garantire il buon funzionamento del sistema nelle sue fasi iniziali, tutti i
correntisti ricevono, al momento della loro iscrizione, un accredito bonus di un determinato numero
zx di ore (pertanto il saldo-tempo di un utente, al momento dell'iscrizione, è pari a x).

Il sistema deve offrire le seguenti funzionalità agli utenti:

1.

S GS E

registrarsi con un accredito iniziale di x ore bonus;

trovare gli utenti con una certa abilità e con una media di feedback maggiore o uguale a un
valore dato;

calcolare il proprio moltiplicatore corrente rispetto a una data abilità
ottenere le abilità di un dato utente;

modificare le proprie abilità;

dare un feedback per uno scambio in cui ha partecipato come richiedente;

calcolare il proprio saldo corrente.
