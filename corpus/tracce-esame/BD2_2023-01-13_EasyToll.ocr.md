# BD2_2023-01-13_EasyToll — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2023-01-13_EasyToll.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Fa | ’ Sapienza Università di
Coltà di Ing. dell fﬂfùrnrlariùne. 1nhniîtîîî ;‘ r5Îîtîéîica Laur
lm;e;namentu di Basi di Dati, Maduìr:- 2 ;
. Prof. Toni Mancini
D!partirner‘rtu di Informatica
htt;.1.'j;"ln:nn:::'hf.di.…nmmal.1t

Esame Es,. 2D23Ù113 - Prova SCr

a in Informatica

itta del 13 gennaio 2023

Eettare Easy7,; R A
Eﬁneﬂèieug: ra PPlicazione per la gestione della rete autostradale nazionale,
È'EÉE-E-È[ÈEÎ_ ella rete è ÎdEhtific;t;appresentare la struttura della rete autostradale italiana. Ogni

da un codice alfanumerico univoco, da un nome (opzionale) e
(ad €5., l'autostrada "Al" di nome “Autostrada del Sole” collega
aSelli permettono G î> uscita
îl si no ‘Î-..I.FÎIE."E$*.-.' eSl'uscita Uei veicol; ;n diisnc. i i

stema deve Po PP '{\__. dei veicoli in diversi punti della rete. Per ogni casello

—

autostrada lungo la quale è collocato, un codice ed il nome
’ il nome é quello della località in cui è ubicato), la sua posizione
EIÎDCEÎFÌ-SÌ estremi dell ‘autostrada (sempre la stessa per la stessa autostrada), il

Ibile in entrata ed in uscita (in termini di veicoli /ora), le modalità
: ‘ Contanti, carte di credito, bancomat, ViaCard, Telepass), e
di un Servizio di assistenza ai clienti.

‘spresse in Euro/Km. Queste possono essere diverse per

O: rse e per classi di veicoli diverse.
| ENI qualvolta un veicolo rete autostradale attraverso un <asello} il conducente è te-
| nuto -El|flf;r.a-r un tagli d—— a “IT a ° __ :
| _ -—.__É aglian o contrassegnato da un codice identificativo. Il sistema SsSOCcIa Îl tagliando

_virtuafe in caso il veicolo sia equipaggiato di s:5tanaTE . seguito.) AIl' alla
il conducente è tenuto ad inserire[il tagliando in suo pmessn_n"iféfl"-"lil_'fffìﬁît'a fessura dell'interf
hardware del casello oppure al’personale di servizio che provvede a tale inserimento. Il sistema .

Toll deve poter calcolare l'importo dovuto applicando la tariffa chilometrica (relativa alla classe del | CO t0
veicolo) per il numero di chilometri percorsi e mostrarla all'automobilista per avviare la procedura

di pagamento (per semplicità, in questa sede si ignori tale procedura).

In caso di utilizzo del sistema Telepass, le procedure di ingresso ed uscita da un casello avven-
gono senza l'arresto del veicolo. Ogni dispositivo]Telepast & univocamente associato ad un klient
abbonato al servizio. All'ingresso, il casello identifica (mediante un segnale radio) il cliente e genera
un tagliando virtuale (che viene memorizzato nel 5i5terna.} con le stesse infurTa:iunî dell'equivalen-
te cartaceo. All’uscita, il casello identifica nuovamente ’|I cliente e calcola | importo d:wutîa per il
tragitto. Di ogni cliente ahhanatr;: al 5en.rizi_q__Î&!;apaa H'IÈEJ’ESEB(1"I=D…E!. cognome, codice fiscale e

] BAN per l’addebito del conto mensile, a
CÙGÎF;?:*.È:m!B ji faîturaziane (un Sistema esterno a EasyToll), dato un{cliente Telepassi Ln mese ed ) calcodo
un anno) deve poter ottenere il{conto)di quel cliente nel dato mese del dato anno, contenente, per } CO®
logni singolo addebito del mese, il nome dei caselli e la data e l'ora di entrata ed uscita, oltre che
‘i itatﬂl a a ù I " P
’ rmgî :fs.?::eer?tivare )g[i eccessi di velocità, lungo la rete sono posizionati terminali del ms?emg T-u.-:-:;-r 1:…'òÙ
: iati di apposito software per il riconoscimento delle targhe dei veicoli. Il È.Ù-'-» RT
qUIPaggi 09 teiecameîe i ' ità media calcolata tenendo conto del tempo | . )0U
sistema Tutor permette di rilevare l'eccesso della velocità media c

y ; H i f lg
impiegato da un veicolo per viaggiare lungo un breve tratto delimitato da due terminali Tù (di | yueda
impiega

i i coppia di terminali Tutor il sistema deve potey

: izionati tra i 10 e 25 Km tra loro). Per ogni coppi mi i L POteI

<outo EÙHÎT; tsu.…=.« ubicazione (autostrada, senso di marcia, posizione del terminale di inizio e di
memorizza

quello di fine, in modo analogo alle posizioni dei caselli).

## Pagina 2

Ogni volta che un veicolo attraversa il terminale primo di una coppia di terminali Tutor (quello
di ingresso), EasyToll memorizza la \targa e la classe del veicolo, la coppia di terminali che lo u}UHÈ“*“’_‘""A
sta monitorando, la data e l'’ora.) Quando un veicolo attraversa il terminale Tutor di uscita, il | YOM"
sistema calcola la sua velocità media nel breve tratto controllato. Se questa è minore o uguale alla a.f*-““‘""tà
velocità massima consentita (un parametro del sistema che può dipendere anche dalla classe del
veicolo oggetto del controllo), il sistema elimina immediatamente i dati del passaggio, altrimenti lî

mantiene di modo che possano essere acceduti dal personale della Polizia Stradale.
