# BD2_2023-06-27_VirgilioGo — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2023-06-27_VirgilioGo.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Prof. Tani Mancini
Dipartimento di Informatica
http://tmancini.di.uniromal.it

Esame Es.20230627 - Prova scritta del 27 Giugno 2023

un'applicazione per dispositivi mobili per la mobilità urbana.
gare le soste veicolari

i*mezzi pubblicijo per

Si richiede di progettare VirgilioGo,
Gli utenti di VirgilioGo sono privati che utilizzano l'applicazione per pa

- nelle zone a pagamento dellaà città, per acquistare biglietti/e abbonamenti/per

Al'momento dell'iscrizione a VirgilioGo, gli Jutenti
gnome, data di nascita), e l'indirizzo email. Ogni utente può quindi

W. pagamento. '

i AI fine di differenziare le tariffej per il\parcheggio in diverse Jaree
solitamente suddivise in |zone di sosta. VirgilioGo deve mantenere |

| sosta delle città che vogliano permettere l'accesso ai suoi servizi.
| In VirgilioGo, una zona di sosta è rappresentata da un codice alfanumerico (ad es. "Zana01"),

"-l la fascia oraria in cui la sosta è a pagamento (separatamente per i giorni feriali e per i festivi), una

| tariffa oraria (espressa in euro/ minuto), ed eventualmente un pacchetto, cioè una tariffa forfettaria

| che copre un certo numero di ore. Un esempio di pacchetto è “4 euro/8 ore .

| La tariffa applicata a una sosta è sempre la più conveniente applicabile. Ad esempio, un par-
cheggio di 5 ore in una zona di sosta che preveda una tariffa oraria di 1 euro/ora e un pacchetto

“3 euro/4 ore" verrà tariffato a 4 euro (3 con il pacchetto e 1 con la tariffa oraria, assumendo che

J. l’intero intervallo di tempo cada in una fascia oraria a pagamento].
— Gli utenti possono aggiungere uno o più veicoli al proprio profil
un nome (unico tra i veicoli di uno stesso utente), e il colore.

le iniziare una sosta, sceglie uno dei suoi veicoli da parcheggiare, seleziona
tudine), seleziona la zona di sosta, € sceglie la durata voluta

forniscono i loro dati anagrafici (nome, co-
registrare uno o più metodi di

delle città, queste ultime sonò
e informazioni circa le aree di

o. Di ogni veicolo interessa la

| targa (una stringa),
| Quando un utente vuo
| Ea']g‘aìîîîîgìî'del veicolo (latitudine/longi
= Wi daella sosta. |
s f VirgilioGo memorizza queste informazioni, insieme all'istante di inizio della sosta. Gli operatori |
del comune (o di un'azienda terza) addetti al controllo dei pagamenti delle soste e della riscossione | /
delle multe possono verificare l'effettivo pagamento della sosta di un veicolo semplicemente fornendo
a VirgilioGo la sua targa.

In ogni istante, l'utente che ha parc
accorciare la sosta fintanto che questa non è terminata.
E Alcune città prevedono abbonamenti alle zone di sosta. Questi permettono di parcheggiare
liberamente in alcune delle aree di sosta della città per un certo periodo di tempo, dietro il pagamento
di una cifra fissa (ad esempio, 70 eluro/mese per sostare nelle aree di sosta del centro storico di

Roma). _
— Ogni città può prevedere diverse tipo
un costo, una durata, e le zone di sosta

Un abbonamento ha quindi una tipo

esattamente un veicolo. _
éÎ Si vuole che, in a!:_ag.unﬂ‘-=mt_l:à,…'V:g;gr.'m[ì«'a; possa anche essere utilizzata per acquistare biglietti o
abbonamenti per i mg';-:a.f'i-'="ﬁu_bî_:'il_i_’_-:;-':î_-i:"_‘;?;E°gff:eyrenti'.

Ogni città può emr&.'iegaléa'l'-ii;uriîèg:%'gî%’ìji_ùì.a_=é.iè;'1"dè';

si occupa della vendita di alcune tipologie di titoli {(biglietti).

heggiato il veicolo e iniziato la sosta può prolungare ©

logie di abbonamento alla sosta, ognuna delle quali definisce

della città per le quali è valida.
logia è una data di inizio. Ogni abbonamento è legato ad

delle quali interessa il nome, ognuna delle quali

=
i

## Pagina 2

Un titolo può essere un biglietto ad utilizzo singolo (ad esempio, un 1JÌEÌ"'E“È dEH1HUÌFIJUÉ G per
un concerto), è un abbonamento. Di ogni tipologia di titolo interessa conoscere il nome, il prezzo, e
la durata. Di ogni titolo acquistato interessa CONoOscere la tipologia, l'istante di acquisto e un codice
identificativo. Degli abbonamento interessa conoscere il codice fiscale dell'utilizzatore. a

Al contrario degli abbonamenti, i biglietti ad utilizzo singolo non sono immediatamente attivi al

mamento dell'acquisto.
Quando un utente vuole attivare un biglietto precedentemente acquistato, accede A va"£“'"?"'l5f’ E
|l'istante di attivazione e, quindi,

L|r_ti|_i22El la funzionalità relativa (tramite la quale VirgilioGo registra |
l'inizio del periodo di validità). Al termine del periodo di validità del biglietto, questo diventa scaduto

e non può più essere utilizzato.

| titoli sono anche suddivisi in titoli di viaggio (per | mezzi pubblici) e titoli per eventi. Dei titoli
per eventi interessa anche conoscere il nome e il cognome dell'utilizzatore (l'utilizzatore può non
essere l'acquirente).

Il sistema deve permettere agli utenti di registrare veicoli, visualizzare le aree di sosta e le
relative tariffe per una certa città, registrare soste, verificare la validità di una sosta, acquistare
titoli, visualizzare i titoli acquistati (sia attivi che scaduti), e verificare che un titolo di viaggio sia

attualmente valido.

Incltre, Iil sistema deve permettere:
e a ogni utente di calcolare, dato un periodo di tempo, le proprie spese legate alle soste. L'utente

deve poter ottenere un resoconto (in forma tabellare) che, per ognuno dei suoi veicoli e per
ognuna delle città in cui ha sostato, indica il totale dei pagamenti effettuati. Si noti che

questo valore deve tener conto sia delle soste pagate tramite tariffa oraria e pacchetti, sia di

eventuali abbonamenti acquistati.
sostenibilità ambientale di tutte le

e ai responsabili di VirgilioGo di calcolare una classifica di
bilità di una città è definito come

città, per un dato intervallo di tempo. Il punteggio di sosteni
il rapporto tra
— il numero minimo di titoli di viaggio ad utilizzo singolo attivati in un singolo giorno nel

periodo, e
— il numero massimo di soste effettuate in un singolo giorno nel periodo.

|| risultato conterrà le città ordinate in ordine decrescente per punteggio, insieme al punteggio

stesso per ognuna di esse.
