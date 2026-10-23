# BD2_2024-07-05_NoleggiAmico — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2024-07-05_NoleggiAmico.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Analisi chcﬂtﬂ£fÈ

Matricola: -- --
“pra
sisf
A di . : iversità
Facoltà di Ing. dell Informazione, |'“'°fme;.rî.'l.;a : :
Insegnamento dj Basi di pati. mModulo
| Prof. Toni Man4:.ini |
Dl|:an:imenm di |n+-ar…gt|ca
http://tmancini di …1ir0|1131.|t
ga del 5 luglio 2024

Roma ;
atistica, Laurea in Informatica

Esame Es.20240705 — PE scrit

|'azienda NoleggiAmico, la quale si

si vuole progettare è realizzare un sistema di gestione per
occupa di noleggi e compravendite di veicoli di vario gen€"e-
| olegg!

In particolare, i clienti di NoleggiAmico, dopo aver f
scelta, possono aFtenere "!n.Ù sconto sull'acquisto del veicolo SI’EE$5C". S . iL
Per l'applicazione è di interesse conoscere le informazion elative a) QÈICOL nclla disponivilità
: M modellp (nome e anno), la-tipologia (au-

dell'azienda. Di cgni veicolo interessa fa t —
PE o foggljt._èc_g.]. eLu argeéct$i‘;î\‘ìeèwal &| suo stato. Poiché NoleggiAmico
cioccupa anche della gompravendita-di veicoli, è di interess® anche rappresentare il prezzo-e la data
…del veicolo, e il prezzo al quale lo si vuole vendere:

| veicoli a disposizione di NoleggiAmico sono oggetto di manutenzione periodica (effettuata
da officine esterne). Si vogliono mantenere nel sistema le informazioni circa tutti gli episodi di
manutenzione dei veicoli. Per ogni episodio di manutenzioNne interessa il ÈÉÈÈÉÌZ_EÈ_!*_Q[JQÈ una
crizione testuale, il costo, e ll'officina chel'ha.effettuatan

—ccati a noleggiare veicoli. Di ogni cliente

| clienti di NoleggiAmico sono privati o aziende ll interessa
interessa conoscere l'indirizzo email. Dei clienti privati interessa anche l'anagrafica (nome, cognome,
ssa la ragione sociale e il numero di partita

data di nascita, codice fiscale), mentre delle aziende intere

ato un veicolo con una tariffa a loro

[NA.

“ Per ogni noleggio, il sistema deve mantenere le informazioni circa il …È_I'_?-—ef[‘ìﬂua-
il veicolo scelto, la data di inizio, la data di fine prevista, la data di fine effettiva (per i noleggi
terminati) la patente di guida utilizzata, la dypata (un numero intero re la tariffa scelta.

di tariffazione molto flessibile. Per ogni modello di veicolo,
oleggio a éosto variabile,in base alla durata del
), come a medio-lungo termine
per un'unità di tempo e,

NoleggiAmico prevede un sistema
il team di NoleggiAmico prevede delle tariffe di n
noleggio stesso, che può essere a breve termine (uno o più giorni
(settimane, mesi o anni) Di ogni tariffa interessa conoscere il prezzo

per unità di tempo multiple.

Ad esempio, una tariffa di noleggio per un certo modello potrebbe essere calcolata per settimana
e prevedere i seguenti costi: 150 Euro/settimana per noleggi di una settimana, 145 /Euro a settimana
per noleggi di due settimane, e 140 Euro/settimana per noleggi di tre o più settimane.

In ogni momento, un cliente che abbia noleggiato un veicolo in passato può scegliere di acquistarlo
direttamente da NoleggiAmico. L'azienda offre al cliente un credito sul prezzo di acquisto di un
veicolo proporzionale al denaro speso fino a quel momento dal cliente stesso nel noleggio di veicoli

dello stesso modello.
In particolare, ogni tariffa prevede anche un tasso di cred

di acquistare un certo veicolo di modello 1n, il prezzo di vendita

credito totale in Euro accumulato grazie a noleggi di veicoli di modello m.
giato un veicolo di modello rn due volte, la prima spendendo 1500 Euro

Ad esempio, se c ha noleg

con una tariffa che offriva un credito del 10%, e la seconda spendendo 1000 Euro con un credito

del 5%, il costo del veicolo gli verrà scontato di 150 + 50 = 200 Euro.
Infine, NoleggiAmico premia i suoi clienti più affezionati con un programma fedeltà, offrendo un

cashback, cioè restituendo loro,-in-contanti,.una parte del_totale-speso.in_noleggi. In particolare, un
1 -

opzionalmente, | prezzi

ito percentuale s. Se un cliente decide
verrà scontato di un valore pari al

## Pagina 2

certo livello di fedeltà offre un cashback in percentuale in base alla spesa media giornaliera fatta da
un utente nei 12 mesi precedenti.

Il sistema deve permettere al team di NoleggiAmico di inserire livelli di fedeltà diversi (che
possono cambiare nel tempo), ognuno dei quali è lappresentato dalla spesa media giornaliera richiesta
(un reale positivo) e dal cashback offerto (un reale tra 0 e 1). Îl sistema deve permettere di calcolare
il livello di fedeltà attuale di un cliente (cioè il livello più alto raggiungibile in base alla spesa totale
negli ultimi 12 mesi).

Il sistema deve inoltre permettere al team di NoleggiAmico di calcolare il guadagno totale dell'a-
zienda su tutte le compravendite di veicoli effettuate in un dato periodo. In particolare, il guadagno

effettivo sulla compravendita di un certo veicolo è dato dalla differenza tra il prezzo di acquisto
iniziale e il prezzo di vendita effettivo al cliente (considerando il credito da esso accumulato tramite
tutti i noleggi effettuati di veicoli di quel modello). A questo valore va poi sottratto il totale delle

spese di manutenzione effettuate su quel veicolo.
