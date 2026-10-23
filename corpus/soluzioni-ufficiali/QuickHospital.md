# QuickHospital — soluzione ufficiale

## 01 - Analisi — Classe Letto

> Fonte: `Classe Letto.txt`

```
Classe Letto


[V.Letto.no_due_ricoveri_simult]
	not EXIST l, r1, r2 Letto(l) and
						r1 != r2 and 
						let_ric(l, r1) and let_ric(l, r2) and
						interseca(  r1.periodo(), r2.periodo()  ).
```

## 01 - Analisi — Classe Prestazione

> Fonte: `Classe Prestazione.txt`

```
Classe Prestazione e sottoclassi


Class Prestazione

[V.Pretazione.istante_presunto_dopo_istante_pren]
	ALL p, ipren, ipres Prestazione(p) and istante_pren(p, ipren) and inizio_presunto(p, ipres) --> ipres >= ipren


Classe PretazioneFinalizzata
	periodo():Periodo
		pre: nessuno
		post:
			result soddisfa:

			EXISTS i
				da(result, i) and inizio(this, i)
				and
				(not EXISTS f  a(result, f))


[V.PrestazioneFinalizzata.inizio_dopo_istante_pren]
	ALL p, ipren, ipres PrestazioneFinalizzata(p) and istante_pren(p, ipren) and inizio(p, i) --> i >= ipren



[V.Ricovero.no_due_ricoveri_simult_stesso_paziente]
	not EXISTS p, r1, r2
		paz_prest(p, r1) and paz_prest(p, r2) and r1 != r2 and
		Ricovero(r1) and Ricovero(r2) and
		interseca( r1.periodo(), r2.periodo() ).


Classe PrestazioneEseguita

	periodo():Periodo
		pre: nessuno
		post:
			result = [ this.inizio, this.fine() ]

			EXISTS i, f
				da(result, i) and inizio(this, i)
				and
				a(result, f) and fine(this, f)


fine(): DataOra
	pre: nessuna
	post:
		result = this.inizio + this.durata

		Formalmente, result soddisfa la formula:

			EXISTS i, d
				inizio(this, i) and durata(this, d) and result = i + d



[V.PrestazioneFinalizzata.specializzazioni]
Ogni specializzazione necessaria ad una prestazione finalizzata è coperta da un medico assegnato.
	ALL prest, spec
		PrestazioneFinalizzata(prest) and Specializzazione(spec) and
		prest_spec(prest, spec) -->
			EXISTS m  	Medico(m) and med_spec(m, spec) and
						med_prest(m, prest).


[V.Prestazione.medico_non_paziente]
Un paziente non può essere anche medico di una sua prestazione:
	not EXISTS prest, paz  
			Prestazione(prest) and 
			paz_prest(paz, prest) and
			med_prest(paz, prest).
```

## 01 - Analisi — Specifica dei tipi di dato

> Fonte: `Specifica dei tipi di dato.txt`

```
Specifica dei tipi di dato

Periodo:
	- da:DataOra [0..1]
	- a:DataOra [0..1]

	[V.Periodo.legale]
		ALL p, x,y   Periodo(p) and da(p,x) and a(p,y) --> y >= x.

	interseca(p1:Periodo, p2:Periodo):Booleano
		pre: nessuna
		post: 
			... // per esercizio

CodiceFiscale: Stringa ~ '...'
Email: Stringa ~ '...'
Telefono: Stringa ~ '...'

Indirizzo: 
	- via: Stringa
	- civico: Stringa ~ '...'
	- cap: Stringa ~ '...'



CapienzaStanza:
	- n_letti_tipico: Intero > 0
	- n_letti_max: Intero > 0


[V.CapienzaStanza.n_letti_max]	
	ALL c, t m
		CapacitaStanza(c) and
		n_letti_tipico(c, t) and
		n_letti_max(c,m)
			--> m >= t
```

## 01 - Analisi — Use-case Gestione prestazioni

> Fonte: `Use-case Gestione prestazioni.txt`

```
Use-case GestionePrestazioni

medici_idonei(s:Specializzazione): Medico [0..*]
	pre: nessuna

	post: 
		se esistono medici con spec. primaria s, restituiscili;
		altrimenti restituisci i medici con spec. sec. s

		Formalmente

		Sia MSP = { m  | 	Medico(m) and
						med_spec_prim(m,s)
				  }			


		Sia MSS = { m  | 	Medico(m) and
						med_spec(m,s)
				  }.

		Se MSP è vuoto, allora result = MSS altrimenti result = MSP.


aggiungiMedico(p:Prestazione, m:Medico)
	pre: not PrestazioneEseguita(p)
	post:
		Side effect: 
			med_prest(m,p)


	
finalizzaPrestazione(p:Prestazione, i:DataOra)
	pre: (not PrestazioneFinalizzata(p)) and
		(i >= adesso) and
		( EXISTS ipren istante_pren(p, ipren) and ipren <= i )
		and (
				ALL s  prest_spec(p,s) --> 
						EXISTS m med_prest(m,p) and med_spec(m,s)
		).
	post:
		Side effect:
		- PrestazioneFinalizzata(p)
		- inizio(p, i)


registra_termine(p:Prestazione)
	pre: PrestazioneFinalizzata(p) and 
		 not PrestazioneEseguita(p) and 
		 EXISTS i inizio(p, i) and i <= adesso
	
	post:
		Sia i t.c.  inizio(p,i).

		- PrestazioneEseguita(o)
		- durata(p, adesso - i)
```

## 01 - Analisi — Use-case Gestione ricoveri

> Fonte: `Use-case Gestione ricoveri.txt`

```
Use-case GestioneRicoveri


medici_idonei(s:Specializzazione): Medico [0..*]
	pre: nessuna
	post: 
		result = GestionePrestazioni.medici_idonei(s)


aggiungiMedico(r:Ricovero, m:Medico)	
	pre: not PrestazioneEseguita(r)
	post: 
		Gestione_prestazioni.aggiungiMedico(r, m)
```

## 01 - Analisi — Use-case Itinerari visite

> Fonte: `Use-case Itinerari visite.txt`

```
Use-case Itinerari visite

itinerario(): (r:Ricovero, pos:Intero > 0) [0..*]

	pre: nessuna
	post:
		Sia m:Medico l'oggetto associato all'attore che ha invocato l'operazione.

		R = { r  |  Ricovero(r) and not PrestazioneEseguita(r) and
						med_prest(m, r)
			}

		result = sorted(R; ricovero_LEQ)


		dove ricovero_LEQ(r1:Ricovero, r2:Ricovero): Booleano
				pre: nessuna
				post: 
					Siano p1, p2, sett1, sett2 tali da soddisfare:

						EXISTS l1, l2, st1, st2
							let_ric(l1, r1) and let_stanza(l1, st1) and
							sett_stanza(sett1, st1), and set_piano(sett1, p1) and
							let_ric(l2, r2) and let_stanza(l2, st2) and
							sett_stanza(sett2, st2), and set_piano(sett2, p2).

					result = true <--> 
						[ p2 > p1 or (p2 = p1 and sett2 >= sett1) ]
```

## 02 - Progettazione / 01 - Ristrutturazione — Progettazione dei tipi di dato

> Fonte: `Progettazione dei tipi di dato.txt`

```
CREATE DOMAIN Stringa AS VARCHAR;
CREATE DOMAIN DataOra AS timestamp;

CREATE DOMAIN CodiceFiscale AS Stringa 
	CHECK (value ~ '...');

CREATE DOMAIN Email AS Stringa 
	CHECK (value ~ '...');

CREATE DOMAIN Telefono AS Stringa 
	CHECK (value ~ '...');

CREATE TYPE Indirizzo (
	... // per esercizio
);

CREATE DOMAIN DurataPrest as INTERVAL
	CHECK (value > 0);

CREATE DOMAIN IntegerGZ as Integer
	CHECK (value > 0);

CREATE TYPE __CapienzaStanza__ AS (
	n_letti_tipico IntegerGZ,
	n_letti_max IntegerGZ
);

CREATE DOMAIN CapienzaStanza as __CapienzaStanza__
	CHECK ( value.n_letti_tipico IS NOT NULL and value.n_letti_max IS NOT NULL and value.n_letti_tipico <= value.n_letti_max);


CREATE TYPE __Periodo__ (
	da DataOra,
	a DataOra
);	

CREATE DOMAIN Periodo as __Periodo__
	CHECK (value.a >= value.da);
```

## 02 - Progettazione / 01 - Ristrutturazione — Specifica ristrutturata vincoli esterni

> Fonte: `Specifica ristrutturata vincoli esterni.txt`

```
Specifica ristrutturata vincoli esterni:

[V.Persona.gen_complete]
	ALL p Persona(p) --> [
				( EXISTS paz   paz_isa_pers(paz, p) )
				or
				( EXISTS m     m_isa_pers(m, p) )
	].


[V.Prestazione.gen_disj_complete]	
	ALL prest    Prestazione(prest) --> [
					// disjoint
					not EXISTS r, pe   
							r_isa_p(r, prest) and pe_isa_p(pe, prest)
					and
					// complete
					(  EXISTS x r_isa_p(x, prest) or pe_isa_p(x, prest) )
	
	].

[Tutti gli altri vincoli per disjoint/complete, v. diagramma]


[V.med_spec_prim_isa_med_spec]
	ALL m,s   med_spec_prim(m,s) --> med_spec(m,s)

[V.med_resp_prest_isa_med_prest]
	ALL m, p  med_resp_prest(m,p) --> med_prest(m,p).

[V.med_resp_prest_fin_isa_med_rest_prest]
	ALL m,p   med_resp_prest_fin(m,p) --> med_resp_prest(m,p).

	

Eventuali altri vincoli: per esercizio.
```

## 02 - Progettazione / 02 - Schema relazionale con vincoli — V.Prestazione.gen_disj_complete

> Fonte: `V.Prestazione.gen_disj_complete.txt`

```
Progettazione del vincolo esterno ristrutturato (si lasciano tutti gli altri per esercizio!!):

[V.Prestazione.gen_disj_complete]	
	ALL prest    Prestazione(prest) --> [
					// disjoint
					not EXISTS r, pe   
							r_isa_p(r, prest) and pe_isa_p(pe, prest)
					and
					// complete
					(  EXISTS x r_isa_p(x, prest) or pe_isa_p(x, prest) )
	
	].

Strategia:
	- Politiche di accesso ai dati + trigger




Politiche di accesso ai dati:
	impedisci:
		UPDATE su Prestazione(id)
		UPDATE su PrestazioneFinalizzata(id)
		UPDATE su PrestazioneNonFinalizzata(id)


Trigger:
	Istante di intercettazione: AFTER
	Eventi intercettati:
		INSERT(new) in Prestazione
		INSERT(new) in PrestazioneNonFinalizzata
		INSERT(new) in PrestazioneFinalizzata
		DELETE(old) in PrestazioneNonFinalizzata
		DELETE(old) in PrestazioneNonFinalizzata

	Funzione(old, new):
		// a causa degli eventi, esattamente una tra old e new è non-NULL.

		id integer = NULL 

		if evento è INSERT:
			id = new.id
		else if evento è DELETE
			id = old.id
		else:
			errore, evento non previsto

		error Boolean = FALSE
		
		SELECT count(*) <> 1 INTO STRICT error
		FROM PrestazioneFinalizzata pf, PrestazioneNonFinalizzata pnf
		WHERe pf.prestazione = id AND pnf.prestazione = id;

		if error:
			errore, disjoint e complete non soddisfatti

		return NULL;


	Nota: Dato che intercettiamo eventi su tre tabelle, abbiamo bisogno di tre trigger, ma riusciamo ad usare la stessa funzione.
```

## 02 - Progettazione / 02 - Schema relazionale con vincoli — schema_relazionale

> Fonte: `schema_relazionale.txt`

```
Nazione(__nome__)

Citta(__id__, nome, nazione)
	fk: nazione references Nazione(nome)

Persona(__cf__, nome, cognome, nascita)

Paziente(__persona__, email, indirizzo)
	fk: persona references Persona(cf)
	incl.: persona compare in telefono(paziente) 

Medico(__persona__, spec_prim)
	fk: persona references Persona(cf)
	incl:  persona compare in med_spec(medico)
	fk:    persona compare in med_spec_prim(medico)
	fk:    spec_prim references Specializzazione(nome)
	fk:    (persona, spec_prim) references med_spec(medico, spec) -- [V.med_spec_prim_isa_med_spec]




telefono(
	__paziente__:CodiceFiscale,
	__valtel__:Telefono
)
	fk: paziente ref. Paziente(persona)

Padiglione(__nome__)

Piano(__n__, __padiglione__)
	fk: padiglione references Padiglione(nome)
		ON UPDATE CASCADE

Settore(__n__, __piano__, __padiglione__)
	fk: (piano, padiglione) references Piano(n, padiglione)
		ON UPDATE CASCADE

Stanza(__n__, __sett__, __piano__, __padiglione__,  capienza)
	fk: (sett, piano, padiglione) references Settore(n, piano, padiglione) 
		ON UPDATE CASCADE

Letto(__n__, __stanza__, __sett__, __piano__, __padiglione__)
	fk: (stanza, sett, piano, padiglione) references Stanza(n, sett, piano, padiglione)


med_spec(__medico__:CodiceFiscale, __spec__)
	fk: medico references Medico(persona)
	fk: spec references Specializzazione(nome)


Prestazione(__id__:serial, istante_pren, inizio_presunto, medico_resp*:CodiceFiscale)
	check: inizio_presunto >= istante_pren -- [V.Prestazione.istante_presunto_dopo_istante_pren]
	fk: medico_resp references Medico(persona)

PrestazioneFinalizzata(__id__:integer, inizio)
	fk: id references Prestazione(id)

PrestazioneFinalizzataNonEseguita(__id__)
	fk: id references PrestazioneFinalizzata(id)


Ricovero(__id__:integer, letto, stanza, sett, piano, padiglione)
	fk: (letto, stanza, sett, piano, padiglione) references Letto(n, stanza, sett, piano, padiglione)

Nota: la scelta dei vincoli di identificazioni primari per le classi Letto, Stanza, Settore, Piano, e il combinato e il conseguente l'accorpamento delle associazioni let_ric, let_stanza, sett_stanza, set_piano, piano_pad ha portato a duplicazioni di dati (aspetto negativo), con il vantaggio di avere tutte le info necessari alla operazione di use-case itinerario() nella tabella Ricovero!  Si raccomanda di provare alternative e confrontarne pro e contro.
```

## 02 - Progettazione / 03 - Progettazione operazioni — Use-case GestionePrestazioni

> Fonte: `Use-case GestionePrestazioni.txt`

```
Specifica realizzativa dello Use-case GestionePrestazioni


medici_idonei(s:Stringa): Set[Medico.*]
	pre: nessuna

	post: 
		BEGIN TRANSACTION

		Q = SELECT m.*
			FROM Specializzazione spec LEFT OUTER JOIN Medico m
				ON spec.nome = m.spec_prim				
			WHERE spec.nome = s;

		Se Q è vuoto:
			error, s non è il nome di una specializzazione
		
		Se Q = (NULL, ..., NULL): 
			// nessun medico ha s come spec. primaria
			Q = SELECT m.*
				FROM Medico m, med_spec ms
				WHERE ms.medico = m.persona
				  AND ms.spec = s;
		COMMIT;	
			// Usiamo una transazione ogni per evitare risultati inaspettati in caso di modifiche concorrenti al DB che dovessero avvenire tra le due query.				  
		
		Restituisci Q;


aggiungiMedico(prest_id:integer, m:Codicefiscale)
	algoritmo: 
		BEGIN TRANSACTION;

		Q = SELECT peseg.* 
			FROM Prestazione p LEFT OUTER JOIN 
						PrestazioneEseguita peseg
			ON p.id = pseg.id
			WHERE p.id = prest_id;

		Se Q è vuoto:
			errore, prest_id non identifica una prestazione
		Se Q <> (NULL, ..., NULL):
			errore: La prestazione prest_id è già stata eseguita

		INSERT INTO med_prest(medico, prestazione) VALUES (m, prest_id);

		COMMIT;


	
finalizzaPrestazione(prest_id:integer, i:timestamp)
	// per esercizio


registra_termine(prest_id:integer)
	algoritmo:
		BEGIN TRANSACTION;
		SET CONSTRAINTS ALL DEFERRED;

		Q = SELECT pfin.*, pfne.*
			FROM Prestazione p 
				 LEFT OUTER JOIN
				 (
					PrestazioneFinalizzataNonEseguita pfne 
					JOIN 
					PrestazioneFinalizzata pfin 
					ON pfne.id = pfin.id
				 )
				 ON p.id = pfne.id
			WHERE p.id = prest_id;

		IF Q è vuoto:
			errore, prest_id non identifica una prestazione;
		IF Q = (NULL, ..., NULL):
			errore, la prestazione prest_id non tra quelle finalizzate ma non ancora eseguite;

		IF Q.inizio > NOW():
			errore, prest_id non è ancora iniziata;

		DELETE FROM PrestazioneFinalizzataNonEseguita WHERE
			id = prest_id;

		INSERT INTO PrestazioneEseguita(id, durata) VALUES
			(prest_id, NOW() - Q.inizio);

		COMMIT;
```

## 02 - Progettazione / 03 - Progettazione operazioni — Use-case Itinerari visite

> Fonte: `Use-case Itinerari visite.txt`

```
Use-case ItinerariVisite

itinerario(): List[ (letto:IntegerGZ, stanza:IntegerGZ, sett:IntegerGZ, piano:integer, padiglione:Stringa) ]

	algoritmo:
		Sia m:CodiceFiscale il valore del campo chiave della ennupla di tabella Medico associata all'attore che ha invocato l'operazione.

		Restituisci il risultato di:

			SELECT r.letto, r.stanza, r.sett, r.piano, r.padiglione
			FROM Ricovero r, PrestazioneFinalizzataNonEseguita pfne
			WHERE r.prestazione = pfne.prestazione 
			  AND r.medico = m
			ORDER BY r.piano, r.settore;
```

## README

> Fonte: `README.txt`

```
Questo svolgimento è stato condotto in aula il 2025-06-03, discutendo varie alternative proposte dagli studenti.

Sono state prese alcune licenze poetiche, estendendo alcuni requisiti a scopi didattici. Ad esempio, è stato permesso che:
 - una prestazione possa necessitare di più di una specializzazione, - una prestazione possa essere assegnata a più medici (di cui uno responsabile)
 - anche i ricoveri possano essere prenotabili (ad es., per un intervento chirurgico pianificato)
 - le prestazioni (sia ricoveri che prestazioni esterne) seguono lo stesso flusso: prenotate (con istante di inizio presunto), finalizzate (con i medici assegnati ed un istante di inizio certo), eseguite (con un istante di fine).


 Inoltre, per velocità:
  - nei diagrammi sono stati omessi alcuni dettagli (ad es., attributi, specifiche di tipi di dato già visti in precedenza)
  - alcuni vincoli esterni non sono stati modellati e sono lasciati per esercizio

  - i vincoli esterni non sono stati tutti ristrutturati
  - lo schema relazionale della base dati è parziale
  - la progettazione dei vincoli esterni è parziale.

  È infine possibile che lo svolgimento in diretta abbia comportato piccoli errori. Si invitano gli studenti a leggere questo materiale con spirito critico, a correggere in autonomia gli errori trovati ed a segnalarli.
```
