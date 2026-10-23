# Travel to the moon — soluzione ufficiale

## requisiti

> Fonte: `requisiti.txt`

```
1. Requisiti sulle crociere:
	1.1. codice 
	1.2. data di inizio
	1.3. data di fine
	1.4. nave utilizzata (v. req. 2)
	1.5. itinerario (v. req. 4)
	1.6. il tipo, uno tra:
		1.6.1. luna di miele, di cui interessa:
			1.6.1.1. sottotipo, uno tra:
				1.6.1.1.1. tradizionali: 
					quelle che prevedono un numero di destinazioni romantiche (v. req. 3.4) maggiore o uguale al numero di destinazioni divertenti
				1.6.1.1.2. alternative
					quelle non tradizionali
		1.6.2. per famiglie, di cui interessa:
			1.6.3. se adatte ai bambini (booleano)


2. Requisiti sulle navi
	2.1. nome
	2.2. comfort (3..5)
	2.3. capienza



3. Requisiti sulle destinazioni:
	3.1. nome
	3.2. continente
	3.3. posti da vedere (v. req. 5)
	3.4. tipo, almeno uno tra:
		3.4.1. romantico
		3.4.2. divertente
	3.5. se è esotica, ovvero se è fuori dall'Europa


4. Requisiti sugli itinerari: di ogni itinerario interessa
	4.1. sequenza ordinata di elementi, di cui interessa:
		4.1.1. destinazione (v. req. 3)
		4.1.2. arrivo:
			4.1.2.1. il numero d'ordine del giorno (rispetto alla data di inizio della crociera)
			4.1.2.2. ora

		4.1.3. ripartenza	
			4.1.3.1. il numero d'ordine del giorno (rispetto alla data di inizio della crociera)
			4.1.3.2. ora


5. Requisiti sui posti da vedere:
	5.1. nome
	5.2. descrizione
	5.3. orari di apertura, nella forma di una mappa che associa ad ogni giorno della settimana (lunedì, ..., domenica) un insieme di fasce orarie, dove ogni fascia oraria è definita in termini di una coppia di orari

6. Requisiti sui clienti:
	6.1. nome
	6.2. cognome 
	6.3. età 
	6.4. indirizzo

7. Requisiti sulle prenotazioni di crociere da parte dei clienti:
	7.1. cliente
	7.2. crociera
	7.3. istante di prenotazione
	7.4. numero di posti prenotati



8. Requisiti sulle funzionalità
	8.1. Accedute dal personale dell'Ufficio Prenotazioni:
		8.1.1. Effettuare la prenotazione, per conto di un cliente, di un certo numero di posti per una crociera (non ancora partita), solo se la nave ha ancora un numero di posti disponibili sufficiente

	8.2. Accedute dall'Ufficio Marketing:
		8.2.1. Dato un periodo 'p', calcolare l'età media dei clienti che hanno prenotato, durante 'p', almeno una crociera che prevede una destinazione esotica (v. req. 3.5)

		8.2.2. Dato un periodo 'p', calcolare la percentuale delle destinazioni 'gettonate' in 'p', ovvero raggiunte, durante 'p', da almeno dieci crociere di luna di miele, oppure da almeno quindici crociere per famiglie.
```

## Passo A.1 (1-4) — Specifica classe Crociera

> Fonte: `Specifica classe Crociera.txt`

```
Specifica classe Crociera

	fine(): Data
		pre: nessuna
		post:
			Sia i:Itinerario t.c. (this,i):croc_itin.			
			result = this.inizio + i.durata_g()
```

## Passo A.1 (1-4) — Specifica classe Destinazione

> Fonte: `Specifica classe Destinazione.txt`

```
Specifica classe Destinazione

	esotica(): Booleano
		pre: nesuna
		post:
			L'operazione non fa side-effect.

			Sia c:Continente tale che (this,c):dest_cont.
			result = true se e solo se c.esotico = True
```

## Passo A.1 (1-4) — Specifica classe Itinerario

> Fonte: `Specifica classe Itinerario.txt`

```
Specifica classe Itinerario

	durata_g(): Intero > 0
		pre: nessuna
		post: 
			Sia (this,d) il link di assoc. arrivo_finale che coinvolge 'this' (con una qualche Destinazione d).

			result = (this, d).istante.giorno
```

## Passo A.1 (1-4) — Specifica dei tipi di dato

> Fonte: `Specifica dei tipi di dato.txt`

```
Specifica dei tipi di dato

DeltaDataOra:
	- giorno: Intero > 0
	- ora: Ora
```

## Passo A.2 (5-7) — Classe Cliente

> Fonte: `Classe Cliente.txt`

```
Classe Cliente

	eta(d:Data): Intero >= 0
		pre: 
			d >= this.nascita
		post: 
			L'operazione non effettua side-effect sui dati.

			result =  (d - this.nascita) espressa in anni approssimata per difetto
```

## Passo A.2 (5-7) — Classe Crociera

> Fonte: `Classe Crociera.txt`

```
Specifica classe Crociera

	fine(): Data
		pre: nessuna
		post:
			Sia i:Itinerario t.c. (this,i):croc_itin.			
			result = this.inizio + i.durata_g()
```

## Passo A.2 (5-7) — Classe Destinazione

> Fonte: `Classe Destinazione.txt`

```
Specifica classe Destinazione

	esotica(): Booleano
		pre: nesuna
		post:
			L'operazione non fa side-effect.

			Sia c:Continente tale che (this,c):dest_cont.
			result = true se e solo se c.esotico = True
```

## Passo A.2 (5-7) — Classe Itinerario

> Fonte: `Classe Itinerario.txt`

```
Specifica classe Itinerario

	durata_g(): Intero > 0
		pre: nessuna
		post: 
			Sia (this,d) il link di assoc. arrivo_finale che coinvolge 'this' (con una qualche Destinazione d).

			result = (this, d).istante.giorno
```

## Passo A.2 (5-7) — Tipi di dato

> Fonte: `Tipi di dato.txt`

```
Specifica dei tipi di dato

DeltaDataOra:
	- giorno: Intero > 0
	- ora: Ora


GiornoSettimana = { lun, mar, mer, gio, ven, sab, dom }	

FasciaOraria: (
	da: Ora
	a: Ora
)

Apertura: (
	giorno: GiornoSettimana
	fascia: FasciaOraria
)



Indirizzo: (
	via: Stringa
	civico: Stringa ~ '...'
)
```

## Passo A.3 (8) — Classe Cliente

> Fonte: `Classe Cliente.txt`

```
Classe Cliente

	eta(d:Data): Intero >= 0
		pre: 
			d >= this.nascita
		post: 
			L'operazione non effettua side-effect sui dati.

			result =  (d - this.nascita) espressa in anni approssimata per difetto
```

## Passo A.3 (8) — Classe Crociera

> Fonte: `Classe Crociera.txt`

```
Specifica classe Crociera

	fine(): Data
		pre: nessuna
		post:
			Sia i:Itinerario t.c. (this,i):croc_itin.			
			result = this.inizio + i.durata_g()
```

## Passo A.3 (8) — Classe Destinazione

> Fonte: `Classe Destinazione.txt`

```
Specifica classe Destinazione

	esotica(): Booleano
		pre: nesuna
		post:
			L'operazione non fa side-effect.

			Sia c:Continente tale che (this,c):dest_cont.
			result = true se e solo se c.esotico = True
```

## Passo A.3 (8) — Classe Itinerario

> Fonte: `Classe Itinerario.txt`

```
Specifica classe Itinerario

	durata_g(): Intero > 0
		pre: nessuna
		post: 
			Sia (this,d) il link di assoc. arrivo_finale che coinvolge 'this' (con una qualche Destinazione d).

			result = (this, d).istante.giorno

	destinazioni(): Destinazione [0..*]
		pre: nessuna
		post:
			Sia dest_p:Destinazione l'oggetto tale che 
				(this, dest_p):partenza_iniziale

			Sia dest_a:Destinazione l'oggetto tale che 
				(this, dest_a):arrivo_finale

			Sia T l'insieme degli oggetti t:TappaIntermedia tali che
				(this, t):itin_tappa

			Sia Dest_T l'insieme degli oggetti d:Destinazione tali che:
				esiste t:T tale che (t, d):tappa_dest:

				Dest_T = { d | d:Destinazione and (t,d):tappa_dest 
									per qualche t:T }

			result = {dest_p, dest_a} unione Dest_T.
```

## Passo A.3 (8) — Tipi di dato

> Fonte: `Tipi di dato.txt`

```
Specifica dei tipi di dato

DeltaDataOra:
	- giorno: Intero > 0
	- ora: Ora


GiornoSettimana = { lun, mar, mer, gio, ven, sab, dom }	

FasciaOraria: (
	da: Ora
	a: Ora
)

Apertura: (
	giorno: GiornoSettimana
	fascia: FasciaOraria
)



Indirizzo: (
	via: Stringa
	civico: Stringa ~ '...'
)
```

## Passo A.3 (8) — Use-case Gestione prenotazioni

> Fonte: `Use-case Gestione prenotazioni.txt`

```
Use-case Gestione prenotazioni

	posti_liberi(cr:Crociera): Intero
		pre:
			Esiste un link di associaione croc_nave che coinvolge cr.

		post:
			- Sia n:Nave l'oggetto tale che (cr, n):croc_nave.

			- Sia P = { p | p:Prenotazione and (p,cr):pren_croc }

			result = n.capienza - SUM  (p.posti)
				  					p:P



	nuova_prenotazione(cl:Cliente, cr:Crociera, posti: Intero > 0) : Prenotazione
		pre: 
			# il numero di posti liberi nella crociera cr deve almeno 'posti'
			posti_liberi(cr) >= posti



		post:
			Viene creato e restituito un nuovo oggetto result:Prenotazione tale che:
				- result.istante = l'istante corrente
				- result.posti = posti

			Viene creato il link (result, cl):pren_cliente.
			Viene creato il link (result, cr):pren_croc.
```

## Passo A.3 (8) — Use-case Statistiche età media esotiche

> Fonte: `Use-case Statistiche età media esotiche.txt`

```
Specifica use-case Statistiche età media esotiche:

	eta_media_esotiche(da:Data, a:Data): Reale >= 0
		pre: 
			- da <= a
			- Sia P l'insieme di tutti gli oggetti p:Prenotazione tali che:
				- p.istante >= da e p.istante <= a
				- esistono c:Crociera ed i:Itinerario tali che:
				 	- (p,c):pren_croc, e
				 	- (c,i):croc_itin
					- i.destinazioni() contiene una destinazione d t.c.
					d.esotica() = true.

			- Sia C l'insieme di tutti gli oggetti c:Cliente tali che:
				(p,c):pren_cliente per un qualche p:P.

			- Deve essere |C| > 0


		post:
			result = [ SUM  c.eta() ] / |C|
					    c:C
```

## Passo A.4 — Classe Cliente

> Fonte: `Classe Cliente.txt`

```
Classe Cliente

	eta(d:Data): Intero >= 0
		pre: 
			d >= this.nascita. Formalmente:

			ALL n  nascita(this, n) --> n <= d

			oppure, in modo equivalente:

			EXISTS n  nascita(this, n) and n <= d


		post: 
			L'operazione non effettua side-effect sui dati.

			result =  (d - this.nascita) espressa in anni approssimata per difetto.

			Formalmente, result deve soddisfare la seguente formula:

				ALL n,dn   nascita(this, n) and data(n, dn) --> 
								anni(d - dn, result )

			oppure, più semplicemente:

			ALL n   nascita(this, n) --> anni(d - n, result).


			Nota: 
				anni/2 è un simbolo di predicato per il tipo Durata soggetto alla semantica di mondo reale. La semantica di anni(d,x) è che d:Durata è pari a x anni (intero)
```

## Passo A.4 — Classe Crociera

> Fonte: `Classe Crociera.txt`

```
Specifica classe Crociera

	fine(): Data
		pre: nessuna
		post:
			Sia i:Itinerario t.c. (this,i):croc_itin.			
			result = this.inizio + i.durata_g()

			Formalmente, result soddisfa la seguente formula:

			ALL in, itin, dur   inizio(this, in) and croc_itin(this, itin) and
								durata_g(itin, dur) -->
									result = in + dur.
```

## Passo A.4 — Classe Destinazione

> Fonte: `Classe Destinazione.txt`

```
Specifica classe Destinazione

	esotica(): Booleano
		pre: nesuna
		post:
			L'operazione non fa side-effect.

			Sia c:Continente tale che (this,c):dest_cont.
			result = true se e solo se c.esotico = True
```

## Passo A.4 — Classe Itinerario

> Fonte: `Classe Itinerario.txt`

```
Specifica classe Itinerario

[V.Itinerario.arrivo]
	ALL i, d, arrivo_finale_i, t, rip_t
		Itinerario(i) and arrivo_finale(i, d) and istante(i,d, arrivo_finale_i) and
		TappaIntermedia(t) and itin_tappa(i,t) and ripartenza(t, rip_t)
			--> 
				ALL g1, o1, g2, o2
					giorno(rip_t, g1) and ora(rip_t, o1) and
					giorno(arrivo_finale_i, g2) and ora(arrivo_finale_i, o2) -->
						[ g1 < g2 or (g1 = g2 and o1 <= o2) ]


	durata_g(): Intero > 0
		pre: nessuna
		post: 
			Sia (this,d) il link di assoc. arrivo_finale che coinvolge 'this' (con una qualche Destinazione d).

			result = (this, d).istante.giorno

			Formalmente, result soddisfa la seguente formula:

				ALL dest, i    	arrivo_finale(this, dest) and 
								istante(this, dest, i) -->
														giorno(i, result)



	destinazioni(): Destinazione [0..*]
		pre: nessuna
		post:
			Sia dest_p:Destinazione l'oggetto tale che 
				(this, dest_p):partenza_iniziale

			Sia dest_a:Destinazione l'oggetto tale che 
				(this, dest_a):arrivo_finale

			Sia T l'insieme degli oggetti t:TappaIntermedia tali che
				(this, t):itin_tappa

			Sia Dest_T l'insieme degli oggetti d:Destinazione tali che:
				esiste t:T tale che (t, d):tappa_dest:

				Dest_T = { d | d:Destinazione and (t,d):tappa_dest 
									per qualche t:T }

			result = {dest_p, dest_a} unione Dest_T.
```

## Passo A.4 — Classe Prenotazione

> Fonte: `Classe Prenotazione.txt`

```
Classe Prenotazione


[V.Prenotazione.istante]
	Per ogni p:Prenotazione, p.istante deve essere < della data di partenza della crociera c associata a p.
	Formalmente:

	ALL p, istante_p, c, inizio_c
		Prenotazione(p) and istante(p, istante_p) and 
		pren_croc(p, c) and inizio(c, inizio_c) -->   istante_p < inizio_c.
```

## Passo A.4 — Classe TappaIntermedia

> Fonte: `Classe TappaIntermedia.txt`

```
Classe TappaIntermedia


[V.TappaIntermedia.arrivo_ripartenza]
	ALL t, a, r
		TappaIntermedia(t) and arrivo(t, a) and ripartenza(t, r)
			--> 
				ALL g1, o1, g2, o2
					giorno(a, g1) and ora(a, o1) and
					giorno(r, g2) and ora(r, o2) -->
						[ g1 < g2 or (g1 = g2 and o1 <= o2) ]
```

## Passo A.4 — Tipi di dato

> Fonte: `Tipi di dato.txt`

```
Specifica dei tipi di dato

DeltaDataOra:
	- giorno: Intero > 0
	- ora: Ora

GiornoSettimana = { lun, mar, mer, gio, ven, sab, dom }	

FasciaOraria: (
	da: Ora
	a: Ora
)

Apertura: (
	giorno: GiornoSettimana
	fascia: FasciaOraria
)



Indirizzo: (
	via: Stringa
	civico: Stringa ~ '...'
)
```

## Passo A.4 — Use-case Gestione prenotazioni

> Fonte: `Use-case Gestione prenotazioni.txt`

```
Use-case Gestione prenotazioni

	posti_liberi(cr:Crociera): Intero
		pre:
			Esiste un link di associaione croc_nave che coinvolge cr.

		post:
			- Sia n:Nave l'oggetto tale che (cr, n):croc_nave.

			- Sia P = { p | p:Prenotazione and (p,cr):pren_croc }

			result = n.capienza - SUM  (p.posti)
				  					p:P



	nuova_prenotazione(cl:Cliente, cr:Crociera, posti: Intero > 0) : Prenotazione
		pre: 
			# il numero di posti liberi nella crociera cr deve almeno 'posti'
			posti_liberi(cr) >= posti

			Formalmente:

			ALL p  posti_liberi(cr, p) --> p >= posti


		post:
			Viene creato e restituito un nuovo oggetto result:Prenotazione tale che:
				- result.istante = l'istante corrente
				- result.posti = posti

			Viene creato il link (result, cl):pren_cliente.
			Viene creato il link (result, cr):pren_croc.

			Formalmente:

			Side effect:
			- Variazioni degli elementi del dominio di int.: ALPHA
			- Variazioni nell'interpretazione dei simboli di predicato:
				Prenotazione(ALPHA)
				istante(ALPHA, adesso)
				posti(ALPHA, posti)
				pren_cliente(ALPHA, cl)
				pren_croc(ALPHA, cr)

			result = ALPHA
```

## Passo A.4 — Use-case Statistiche età media esotiche

> Fonte: `Use-case Statistiche età media esotiche.txt`

```
Specifica use-case Statistiche età media esotiche:

	eta_media_esotiche(da:Data, a:Data): Reale >= 0
		pre: 
			- da <= a
			- Sia P l'insieme di tutti gli oggetti p:Prenotazione tali che:
				- p.istante >= da e p.istante <= a
				- esistono c:Crociera ed i:Itinerario tali che:
				 	- (p,c):pren_croc, e
				 	- (c,i):croc_itin
					- i.destinazioni() contiene una destinazione d t.c.
					d.esotica() = true.

			- Sia C l'insieme di tutti gli oggetti c:Cliente tali che:
				(p,c):pren_cliente per un qualche p:P.

			- Deve essere |C| > 0


		post:
			result = [ SUM  c.eta() ] / |C|
					    c:C
```
