# BD2_2018-09-10_Alimentary — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2018-09-10_Alimentary.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma

dfìl'lnlﬁn'u.i:nmn, Informatica e Statistica. Laurea n Informatka
Insegnamento di Basiì dî Dati, Modula 2

Prof. Toni Mancini, Prof Fedenco Man
Dipartimanto di Informatica
http:/ ftmancini di miromal.it

Ì‘lHi" Mman d UNTOMmMAal t
Esame Es. 20180910 - Prova scritta del 10 Settembre 2018

i vuole progettare Aliment

kor ary, una nuova applicazione che permetta agli utenti di monitorare La
QNO

alimentazione, tracciando ! cibi che ingeriscono giornalmente (con relative quantià e nutrienti)
) ’ - i
Per tenere sotto controllo ‘Pporto calorico ed equilibrio della loro dieta.

A seguito di interviste con il committente, è stata stilata la seguente specifica dei requisiti.

È'"‘"*"'ÌJW deve consentire agli utenti di registrarsi al servizio fornendo nome. Cognome, namo-
nalità, email e password. a

Alimentary deve fornire un archivio di schede_alimenti (cibi e bevande). Tale archivio vene
continuamente esteso, oltre che dalla redaîÈî.£cîî#.ﬁnmntary. anche dagli stessi utenti. Per ogni
alimento presente nell'archivio, la relativa scheda deve permettere di rappresentare il nome. la marca
(se disponibile), la grandezza della confezione (se disponibile), il codice identificativo (una stringa)
coditficato nel codice a barre della confezione (se disponibile), il relativo apporto calorico (in “; al) per
unità diì alimento. il valore di tale unità (ad es., grammi o lîtri), la quantità (in unità di alimento)

di una porzione standard, oltre che la quantità (questa volta sempre in grammi, per garantire
unitormità) di ogni nutriente

La lista dei nutrienti è

tipicamente stabile ed uguale per tutti gli alimenti {(ad es., carbodrati
totali, zuccheri, proteine.

grassi totali, grassi saturi, grassi insaturi, sodio, potassio, fibre, £|ll‘tî‘iî.ìlî
etc.), ma Alimentary deve fare in modo che tale lista sia estendibile dall’autore delì‘ìn‘-ì£fﬁmenm ®
una scheda alimento. Viceversa, Alimentary deve permettere l'inserimento di schede i|i_l-"'lìf"l'f'lt-'l che
er 1 nutrienti definiti ‘opzionali'. La lista dei nutrienti opzionali è deiîìnltifl dalla
redazione di Alimentary. Inoltre, tutti ì nutrienti aggiunti dagli utenti alla lista dei nutrienti sono

non hanno valoriì p

per definizione, opzionali

Come detto, schede relative a nuovi alimenti possono essere aggiunte in ogni man1Ejtù df|îh
redazione di Alimentary, ma anche da parte degli utenti, che quindi possono contribuìre în P
persona all ampliamento dell’archivio degli alimenti di Alimentary h-1entrg* le schede di ;lì…tì
inserite dalla redazione diventano subito pubbliche e visibilìi a tutti gli utenti, le schede aggiunte da

utenti devono attraversare un processo di validazione. Una volta validate diventano invece pubbliche
esattamente come quelle inserite dalla redazione

Una scheda alimento inserita da un utente viene resa pubblica quando almeno 10 utenti l’'hanno

Cesso di validazione, può ancora essere
ssere utilizzata (ad es., inserita in un diario alimen-
e di quelli che l'hanno dichiarata valida fino a quel
e gli utenti interessatì ad inserire quell’alimento a

dichiarata valida. Fintantochèé una scheda non supera il pro
ottenuta come risultato di una l…-*r-f.ì. ma può e
tare) solo da parte dell’utente che l'ha compilata
momento (In questo “.‘Ùd“ ”" "-*—":—‘.|'-'lu‘*-r1-._w. incentivar
contribuire alla 1|.-'.i“l‘,'iﬂlî-.“'li‘ della relativa 5—…'hn‘d.ìì'.

Nel tempo, le schede alimenti (sia quelle i

nserite dalla redazione che quelle inserite dagli utenti

POSsOnO essere invalidate (ad es., perchè obsolete, sì

cambia profilo nutrizionale perchè prodotto con una
nuova ricetta). Questo avviene quando 100 utenti le hanno dichiarate non più valide. Le schede

\tranne che, per le schede inizialmente inserite da

liventate l"'l_fLÎ"*.j1lllli'.:Ì'll"-\ll d S@gliito |.,Îil 'L‘J-l1l.,i.Ì:1--..."n]"|î‘uì
C L CGIITLOL

pensi al caso in Cu n atmento contezionato

invalidate diventano inaccessibili a tutti gli utenti
un utente, —-1“i“tﬂ.l'ì Che le ha inserite)

## Pagina 2

alimî:-l1tl;ìr)ìtl'i :L::;arf::;en!ac:u:'.:tral Biornata, inseriscono in Alimentary la composizione dei loro pasti (diario
definito-a li aNE imEenti Ingeriti e relative quantità. L'insieme dei pasti è attualmente

©) alla redazione di Alimentary come: colazione, pranzo, snack e cena, ma potrebbe essere
oggetto di estensioni e perfino di personalizzazioni in futuro.

l 51%tema deve permettere di calcolare una serie di statistiche riguardo il diario alimentare di un
utente in un certo giorno. In particolare:

e Numero totale di kCal ingerite

e Percentuali (del totale del peso in grammi) dei seguenti nutrienti: carboidrati totali, proteine,
grassi

e Grammi totali ingeriti di ogni nutriente.

Gli utenti di Alimentary possono acquistare abbonamenti Premium della durat;a di 30 giorni,
durante i quali avranno accesso a servizi non offerti ai clienti Free. Il servizio prinr:1pìale uffertg.n da
Alimentary ai clienti Premium è relativo alla assitenza di coloro chg desiderano seguire una d‘ieita.*
Le diete sono definite dai singoli utenti e sono private. Una dieta definisce dglìe regole, in terrmr&1 di
soglie minime e massime per alcune delle statistiche di cui sopra. Ad ra|:5&mprn. un ute_nte Preml|ur"f'1
che vuole perdere peso può definire una dieta, che decide di chiamare “ipocalorica ed iperproteica ,
con le seguenti regole:

e kCal totali ingerite: tra 1300 e 1500

* Percentuali (del totale del peso in grammi) dei nutrienti carboidrati totali, proteine, grassi:
rispettivamente [45%, 55%], [17%, 25%]), [25%, 35%]

Grassi saturi ingeriti: al più 10 grammi
Sodio ingerito: al più 2 grammi
e Fibre ingerite: tra 35 e 40 grammi.

Alimentary deve restituire, all'utente Premium -
. - che sta seguendo una di de &
che ha violato in un certo giorno. 8 eta, le regole della dieta
