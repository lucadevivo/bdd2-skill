# La logica del primo ordine nel corso

Il corso usa la FOL in tre punti: la **semantica del diagramma** (quali formule il diagramma
implica automaticamente), i **vincoli esterni** (quello che il diagramma non riesce a esprimere)
e le **specifiche delle operazioni** (pre e postcondizioni). Le convenzioni sono specifiche del
corso, e sono la fonte più frequente di errori sostanziali — uno dei quattro passi eliminatori.

## Due notazioni, entrambe valide

Le slide usano i simboli, i documenti di specifica ufficiali usano l'ASCII:

| Simboli (slide) | ASCII (specifiche) |
|---|---|
| `∀x` | `ALL x` |
| `∃x` | `EXISTS x` |
| `→` | `-->` |
| `∧` `∨` `¬` | `and` `or` `not` |
| `↔` | `<-->` |

Usa l'**ASCII** nei documenti di specifica, perché è la forma delle soluzioni del corso. I
simboli vanno bene per una formula isolata dentro una spiegazione.

Le formule chiudono con un punto. Le parentesi quadre `[ ... ]` raggruppano il conseguente di
un'implicazione lunga; sono una convenzione di leggibilità delle soluzioni ufficiali, non un
operatore.

## L'alfabeto viene dal diagramma — ed è scritto sul modulo d'esame

Ogni elemento del diagramma UML diventa un simbolo di predicato. Questo è il punto: la Domanda 5
dice esplicitamente *"si assuma lo stesso vocabolario definito alla Domanda 2"*.

**Il modulo risposte lo detta alla lettera** (`docente-ufficiale/modulo-risposte-UML-2024-06-05.md`),
e questa è la lista da cui non si esce:

| Simbolo | Per | Semantica, come la scrive il modulo |
|---|---|---|
| `C/1` | ogni classe `C` | `C(x)`: x è una istanza di C |
| `T/1` | ogni tipo di dato `T` | `T(x)`: x è un valore di T |
| `assoc/2` | ogni associazione binaria | `assoc(c1, c2)`: (c1, c2) è una istanza di assoc |
| `attr/2` | ogni attributo **di classe** | `attr(c, v)`: uno dei valori di attr dell'istanza c è v |
| `attr/3` | ogni attributo **di associazione binaria** | `attr(c1, c2, v)`: uno dei valori di attr del link (c1, c2) è v |
| `op/(n+2)` | ogni operazione di classe a `n` argomenti | `op(c, arg1…argn, v)`: v è un valore di ritorno |
| `=/2`, più predicati e funzioni di mondo reale | i tipi di dato | fra cui `adesso/0`, l'istante corrente |

Da leggere due volte: **gli attributi di una classe associativa sono `attr/3` sui due estremi**,
non attributi di un oggetto-link. Il voto di una recensione fra lettore e libro si scrive
`voto(l, b, v)`, non `voto(r, v)` con `r` la recensione.

La tabella qui sotto è la stessa cosa vista dal diagramma:

| Elemento UML | Simbolo | Arietà |
|---|---|---|
| classe `Persona` | `Persona(x)` | 1 |
| attributo `nome` di `Persona` | `nome(x, v)` | 2 |
| associazione `prest_copia` | `prest_copia(p, c)` | 2 |
| attributo `voto` della classe associativa `Recensione` su `let_libro` | `voto(l, b, v)` | 3 |
| operazione `durata_gg()` di `TipoPrestito` | `durata_gg(t, d)` | 2 (l'oggetto, il risultato) |
| generalizzazione `Ricovero` IS-A `Prestito` | vedi sotto: dipende dalla fase | |
| tipo di dato `Stringa` | `Stringa(v)` | 1 |

**L'alfabeto del modulo non ha un simbolo per le operazioni di use-case**, che pure sono l'oggetto
della Domanda 5: quelle si specificano con `pre:`/`post:` e `result`, come nelle soluzioni
ufficiali, non introducendo un predicato `op/(n+2)` per esse.

Gli attributi e le operazioni si scrivono come **predicati che legano l'oggetto al valore**, non
come funzioni con la notazione a punto. `nome(x, v)` legge "il nome di x è v".

**Operazioni con parametri.** Il predicato ha un posto per l'oggetto, uno per ogni parametro e
uno per il risultato, nell'ordine: `scaduto_al(d)` di `Prestito` diventa
`scaduto_al(this, d, result)`, arietà 3. Le operazioni dei tipi di dato non hanno `this`:
`interseca(p1, p2)` diventa `interseca(p1, p2, result)`, arietà 3.

**Operazioni booleane come atomo.** Quando il risultato è un booleano, la forma
`interseca(p1, p2, vero)` è pesante, e le soluzioni ufficiali scrivono l'operazione direttamente
come atomo dentro la congiunzione:

```
not EXISTS p, r1, r2
	let_prest(p, r1) and let_prest(p, r2) and r1 != r2 and
	Ricovero(r1) and Ricovero(r2) and
	interseca( r1.periodo(), r2.periodo() ).
```

È un'abbreviazione di `interseca(..., vero)`, ed è accettata. Nota che dentro gli argomenti la
notazione a punto si usa liberamente: la regola dei predicati vale per la struttura della
formula, non per i termini.

Nelle spiegazioni discorsive dentro una specifica la notazione `this.inizio` o `t.durata_gg()` si
usa liberamente; la formula che segue, introdotta da *"Formalmente"*, è quella che conta.

## Quello che il diagramma già dice

Queste formule sono implicate dal diagramma e **non vanno riscritte come vincoli esterni**.
Scriverle è rumore; il correttore si aspetta nei vincoli esterni solo ciò che il diagramma non
può esprimere.

**Disgiunzione dei tipi** — classi e tipi di dato diversi non condividono istanze:

```
ALL x  Persona(x) --> not Citta(x).
ALL x  Persona(x) --> not Intero(x).
```

I predicati di tipo (`Intero(v)`, `Stringa(v)`) restano comunque **usabili dentro un vincolo
esterno** quando servono a esprimere una condizione — per esempio che un valore calcolato sia
intero. Quello che non si fa è riscriverli per dichiarare una tipizzazione che il diagramma
già dà.

**Tipizzazione degli attributi** — il valore di un attributo appartiene al suo tipo:

```
ALL x, v  cf(x, v) and Persona(x) --> Stringa(v).
```

**Tipizzazione delle associazioni** — gli oggetti coinvolti appartengono alle classi agli estremi:

```
ALL p, c  prest_copia(p, c) --> Prestito(p) and Copia(c).
```

**Generalizzazione** — ogni sottoclasse è una superclasse:

```
ALL x  Uomo(x) --> Persona(x).
```

### La generalizzazione cambia forma fra le due fasi

È la distinzione più facile da sbagliare, e comparirebbe in un passo eliminatorio.

Nel **concettuale** (Domande 2 e 5) sottoclasse e superclasse sono **lo stesso oggetto**, visto
sotto due predicati. Un'istanza di `Ricovero` *è* un'istanza di `Prestito`, quindi gli
attributi della superclasse si applicano direttamente:

```
ALL x   Ricovero(x) --> Prestito(x).
ALL r, i   Ricovero(r) and istante_rich(r, i) --> ...     // attributo ereditato, diretto
```

Nel **ristrutturato** (Domande 6-8) la generalizzazione è stata sciolta: superclasse e
sottoclasse diventano relazioni distinte, e il legame diventa un **link binario esplicito** fra
ennuple diverse:

```
ALL prest   Prestito(prest) --> EXISTS r  ps_isa_p(r, prest) or ...
```

I predicati `ps_isa_p`, `let_isa_pers`, `bib_isa_pers` che si trovano nelle soluzioni ufficiali
appartengono **solo** a questa seconda fase: nel materiale del corso non compaiono mai nei
documenti di analisi. Usarli nella Domanda 2 o nella Domanda 5 significa scrivere notazione
della fase sbagliata.

**Specializzazione di associazione** — se `dirige` specializza `lavora`:

```
ALL x, y  dirige(x, y) --> lavora(x, y).
```

## Quello che invece va scritto: i vincoli esterni

Si nominano `[V.Nome]`, con un nome che dice a cosa si riferisce: `[V.Persona.gen_complete]`,
`[V.let_gen_pref_isa_let_gen]`. Il nome serve, perché in fase di progettazione ogni vincolo va
ritrovato e realizzato in SQL.

**`{disjoint}` e `{complete}` non sono vincoli esterni dell'analisi.** Li dice il diagramma, e in
un documento di analisi non si riscrivono: nella soluzione ufficiale di QuickHospital
`[V.Persona.gen_complete]` compare **solo** nella sezione *«Specifica ristrutturata vincoli
esterni»*, cioè in Domanda 6, quando la generalizzazione è stata sciolta e il diagramma ha smesso
di garantirli. Scriverli in Domanda 2 è il rumore che il correttore legge come riempitivo.

Le forme che seguono servono quindi **in ristrutturazione**, e questa è quella da usare quando la
fusione ha lasciato sottoclasse e superclasse nello stesso oggetto:

```
[V.Persona.gen_complete]
	ALL p   Persona(p) --> [ Paziente(p) or Bibliotecario(p) ].
```

È il caso più frequente: i requisiti raramente impongono anche la disgiunzione.

**Disjoint e complete insieme** — le due parti si scrivono separate e commentate:

```
[V.Prestito.gen_disj_complete]
	ALL prest   Prestito(prest) --> [
		// disjoint
		not ( Ricovero(prest) and PrestitoDomicilio(prest) )
		and
		// complete
		( Ricovero(prest) or PrestitoDomicilio(prest) )
	].
```

Quando invece la generalizzazione è stata sciolta in **relazioni distinte** legate da `X_isa_Y`,
gli stessi due vincoli passano ai link binari. È la forma che si trova nelle soluzioni ufficiali,
ed è la più frequente:

```
[V.Prestito.gen_disj_complete]
	ALL prest   Prestito(prest) --> [
		// disjoint
		not EXISTS r, pe   ps_isa_p(r, prest) and pd_isa_p(pe, prest)
		and
		// complete
		( EXISTS x  ps_isa_p(x, prest) or pd_isa_p(x, prest) )
	].
```

**Inclusione tra associazioni: dipende da come l'hai disegnata.** Se nel diagramma
`let_gen_pref` è dichiarata **specializzazione** di `let_gen`, l'inclusione è implicata e
nell'analisi non si scrive — è il caso della sezione precedente. Se le due associazioni sono
disegnate indipendenti, l'inclusione è un vincolo esterno e va scritta:

```
[V.let_gen_pref_isa_let_gen]
	ALL l, g   let_gen_pref(l, g) --> let_gen(l, g).
```

Lo stesso nome ricompare **in ristrutturazione** anche nel primo caso: sciolta la
specializzazione, il diagramma non la garantisce più e il vincolo diventa esplicito — lì si
realizza con una foreign key verso la relazione più generale (vedi `progettazione.md`).

La regola che governa tutti questi casi è una: **un vincolo che il diagramma esprime non si scrive
nell'analisi, e si scrive nella fase in cui il diagramma smette di esprimerlo.**

**L'identificazione non va scritta fra i vincoli esterni.** È un costrutto del diagramma —
`{id}` su un attributo, o su un estremo di associazione per l'identificazione esterna — e la sua
semantica è implicata come quella delle molteplicità. Nei documenti di analisi ufficiali del
corso non compare **nessun** vincolo esterno di identificazione: si segna `{id}` e basta.



La formula che il diagramma implica, per riferimento, è:

```
not EXISTS x, y, v   Persona(x) and Persona(y) and x != y and
                     cf(x, v) and cf(y, v).
```

**Non va scritto** nemmeno che "ogni persona ha esattamente un nome": è la molteplicità `1..1`
dell'attributo, già espressa dal diagramma. La coppia esistenza + unicità

```
ALL x   Persona(x) --> EXISTS y  nome(x, y).
not EXISTS x, y, z   nome(x, z) and nome(x, y) and z != y.
```

serve solo quando si sta esercitando la formalizzazione della semantica del diagramma (le
esercitazioni di FOL pura come *Crociere* e *Dipendenti* la chiedono esplicitamente), non fra i
vincoli esterni di un'analisi. Vale per entrambe: identificazione e molteplicità si formalizzano
solo se l'esercizio chiede la semantica del diagramma.

**Classe associativa** (association class) — l'associazione che porta attributi. Nell'alfabeto
del modulo **non c'è nessun oggetto-link**: i suoi attributi sono `attr/3` sui due estremi, e si
scrivono così.

```
// Recensione porta voto e data sull'associazione molti-a-molti fra Lettore e Libro

[V.Recensione.voto_sensato]
	ALL l, b, v   voto(l, b, v) --> v >= 1 and v <= 5.
```

L'unicità *non* si scrive: la slide A.1 dice che *«il diagramma permette ad una stessa coppia di
oggetti di formare al più un link dell'associazione»*, quindi «una sola recensione per coppia» è
già implicato — ed è esattamente il motivo per cui si reifica in una classe a sé quando i
duplicati devono essere ammessi.

Un predicato che parla del **link come oggetto** serve solo se la classe associativa è a sua volta
terminale di un'altra associazione o radice di una IS-A — il caso che la slide A.1 nomina. Allora
lo si dichiara sul posto prima di usarlo, e si dice che cosa lega:

```
rec_link(r, l, b)   con r:Recensione, l:Lettore, b:Libro
```

Fuori da quel caso è notazione inventata, e la Domanda 5 è eliminatoria: attieniti all'alfabeto.

**Cardinalità massima** — "nessuno lavora in più di due dipartimenti" si esprime negando
l'esistenza di tre distinti:

```
not EXISTS x, a, b, c   Persona(x) and
	lavora(x, a) and lavora(x, b) and lavora(x, c) and
	a != b and b != c and a != c.
```

## Le specifiche delle operazioni

Struttura fissa: segnatura, `pre:`, `post:`. La spiegazione discorsiva viene prima, la formula
dopo, introdotta da *"Formalmente"*.

```
scadenza(): Data
	pre: nessuna
	post:
		Sia t:TipoPrestito t.c. (this,t):prest_tipo.
		result = this.inizio + t.durata_gg()

		Formalmente, result soddisfa la seguente formula:

		ALL ini, tipo, dur   inizio(this, ini) and prest_tipo(this, tipo) and
		                     durata_gg(tipo, dur) -->
		                         result = ini + dur.
```

Il risultato si chiama sempre `result`. Se non ci sono precondizioni si scrive `pre: nessuna`,
non si omette la riga.

### Insiemi e aggregati

Gli insiemi si definiscono per comprensione, e **la variabile va sempre legata alla sua classe**.
Vale anche quando l'esercizio propone opzioni che la classe non la legano: alcune formule delle
prove ufficiali scrivono `{s | ALL p [Studente(s) and ...] --> ...}`, con la tipizzazione dentro
l'antecedente universale — e in quella forma un `s` che non è uno studente entra nell'insieme per
vacuità. La forma da produrre è con la tipizzazione **fuori**, in congiunzione:
`{s | Studente(s) and [ALL p ...]}`.

```
Sia C = { c | c:Copia and (c,l):copia_libro }
Sia P = { p | p:Prestito and EXISTS c  c in C and (p,c):prest_copia and p.aperto() }

result = |C| - |P|
```

La **cardinalità** di un insieme si scrive `|P|`: è la forma di `COUNT`.

La **sommatoria** si scrive con l'espressione fra parentesi e, sotto, la variabile con il suo
insieme:

```
Sia G = { p | p:Prestito and (p,let):prest_paziente and p.aperto() }

result = SUM  (p.giorni_ritardo())
         p:G
```

L'espressione fra parentesi usa la notazione a punto sulla variabile legata. Non inventare una
forma funzionale tipo `SUM({ (p, g) | ... })` su insiemi di coppie: è più difficile da leggere e
non è quella del corso.

Se l'espressione da sommare è un attributo, si scrive direttamente — `p.posti`, `i.durata` —
perché un attributo è funzionale: a ogni oggetto ne corrisponde un solo valore.

**Se l'attributo è di una classe associativa**, nell'alfabeto è `attr/3` sui due estremi
(`n_inseriti(r, p, v)`), e la notazione a punto non ha un oggetto su cui appoggiarsi. Vale la
stessa funzionalità — un link ha un solo valore per ciascun suo attributo — quindi si dichiara la
**forma funzionale** in testa alla specifica e poi la si usa dentro la sommatoria:

```
Notazione: n_inseriti(r, p) denota l'unico v tale che n_inseriti(r, p, v).

result = SUM  (n_inseriti(r, p))
         (r,p):R
```

Dichiararla è obbligatorio: senza, è un simbolo che l'alfabeto del modulo non contiene.

**Il nome di un attributo di associazione è un simbolo globale, non locale all'associazione.**
`attr/3` prende il nome dall'attributo: se quattro classi associative diverse chiamano `istante`
il proprio attributo, l'alfabeto ha **un solo** `istante/3` e le quattro relazioni si confondono.
Vale anche fra un'operazione di classe a zero argomenti e un attributo omonimo: `punteggio()`
genera `punteggio/2` e l'attributo `punteggio` pure. E vale fra un attributo e un'associazione con
lo stesso nome. La regola pratica: **prima di scrivere la prima formula, si scorre l'alfabeto e si
controlla che non ci siano due simboli con lo stesso nome e la stessa arietà**; se ci sono, si
rinomina nel diagramma (`ist_accesso`, `ist_consegna`, …), non nella formula.

**Due classi associative sulla stessa coppia di classi collidono.** Se `Prelievo` e `Inserimento`
insistono entrambe su `Rifornimento`–`Prodotto` e chiamano `pezzi` il proprio attributo,
l'alfabeto genera due `pezzi/3` con la stessa segnatura e la formula diventa ambigua. I nomi degli
attributi vanno differenziati (`n_prelevati`, `n_inseriti`): è l'unico modo, e conviene accorgersene
disegnando invece che scrivendo la prima formula.

**Un vincolo che chiede una chiusura transitiva non è esprimibile al primo ordine.** «Una
categoria non può essere sottocategoria di se stessa, nemmeno indirettamente», «la gerarchia delle
parti non ha cicli», «ogni nodo è raggiungibile dalla radice»: il predicato `sottocat/2` c'è, ma la
sua chiusura transitiva no, e nessuna formula finita la definisce. Si tratta **come i vincoli
dinamici**: si enuncia in italiano sotto il suo nome `[V....]`, si dichiara *perché* non ha
formula, e si rimanda la realizzazione alla Domanda 6 — dove diventa un trigger con
`WITH RECURSIVE`. Scriverne una formula finta che «quasi» lo esprime (due o tre livelli di
annidamento) è peggio che dichiararlo: dice che il limite non lo hai visto.

**Capienza più finestra temporale** è il pattern che ricorre in ogni traccia con posti, sale o
mezzi da prenotare, e si scrive combinando la sommatoria con un ausiliario `dove`: l'insieme non
è "tutte le prenotazioni della sala" ma "quelle che si sovrappongono a questa".

```
[V.Prenotazione.capienza_sala]
	Per ogni prenotazione, la somma delle persone delle prenotazioni della stessa sala
	che si sovrappongono nel tempo non supera i posti della sala.

	Formalmente:
	ALL pren, sala   pren:Prenotazione and (pren,sala):pren_sala --> [
		SUM  (p.n_persone)  <=  sala.posti
		p:S
	]
	dove S = { p | p:Prenotazione and (p,sala):pren_sala
	                 and sovrapposte(p.periodo, pren.periodo) }

	dove sovrapposte(a:Periodo, b:Periodo): Booleano
		a.da <= b.a and b.da <= a.a
```

La prenotazione stessa appartiene a `S` — si sovrappone a se stessa — e va contata: è il
motivo per cui il confronto è `<=` e non `<`.

Un massimo o un minimo non si esprime con una funzione ma **negando l'esistenza di un valore
migliore**, perché in quella forma il vincolo è direttamente verificabile:

```
result = { p | p:Libro and
               not EXISTS p2  Libro(p2) and copie(p2) > copie(p) }
```

Attenzione al tipo del risultato: se più oggetti pareggiano il massimo, il risultato è un
**insieme**, non un singolo oggetto.

Questo è l'errore che i correttori segnalano per primo. Se scrivi l'insieme dei letti occupati
senza mai nominare `Letto(x)` dentro la formula, quell'insieme non è "i letti occupati": è
l'insieme universo quando la condizione è soddisfacibile, e l'insieme vuoto altrimenti. Il
vincolo che ne deriva non vincola niente.

### «Solo», «soltanto», «nessun altro»: dove mettere il fatto

**Il corso legge «solo» in modo vacuo, e lo si può dimostrare.** L'esercitazione Accademia 8
chiede *«le persone che hanno avuto assenze **solo** nei giorni in cui non avevano alcuna
attività»*, e il risultato stampato dal docente ha **20 righe**: 6 persone che hanno assenze tutte
in giorni liberi, più **le 14 che non hanno mai avuto assenze**. Chi aggiunge la condizione
«esiste almeno un'assenza» ne trova 6 e sbaglia. La lettura è quella dell'implicazione universale:
*ogni* assenza cade in un giorno libero — e su un insieme vuoto è vera.

Se l'esistenza serve davvero, la traccia la chiede a parte («che hanno avuto almeno un'assenza
e…»). Nel dubbio si scrive la lettura vacua e si dichiara l'assunzione in una riga.


Formalizzare *«non esiste un cliente che ha acquistato solamente titoli rischiosi»* ha due letture,
e il corso ne sceglie una. La differenza è **il cliente che non ha comprato niente**: soddisfa
«solamente titoli rischiosi» per vacuità, e cade dentro o fuori a seconda di come scrivi.

La forma che le prove ufficiali danno per corretta mette il **fatto vero nell'antecedente**:

```
ALL c, r   Cliente(c) and Titolo(r) and Rischioso(r) and acquista(c, r) -->
           EXISTS t  Titolo(t) and not Rischioso(t) and acquista(c, t).
```

Si legge: *chi ha comprato almeno un titolo rischioso deve averne comprato anche uno non
rischioso.* Chi non ha comprato nulla non è toccato dal vincolo, perché l'antecedente è falso.

La forma `not EXISTS c  Cliente(c) and [ALL t acquista(c,t) --> Rischioso(t)]` sembra la
traduzione letterale ed è **più forte**: vieta anche i clienti senza acquisti. Se la scegli, o è
un errore o è un'assunzione da dichiarare.

**La regola pratica:** quando il requisito parla di *«chi fa X, deve anche Y»*, X sta
nell'antecedente come fatto positivo — non nella negazione di un universale. E prima di
consegnare, prova la formula sul caso vuoto: *un oggetto che non ha nessun legame, ci finisce
dentro?* Se ci finisce e non doveva, la quantificazione è nel posto sbagliato.

### Precondizioni sui parametri, non esistenziali

La precondizione parla degli argomenti che l'operazione riceve.

```
nuovo_prestito(let:Paziente, c:Copia) : Prestito
	pre:
		# la copia data in input non deve essere gia' in prestito
		not c.in_prestito()

		Formalmente:
		in_prestito(c, esito) --> esito = falso
```

"Il letto **dato in input** è libero", non "esiste un letto libero": sono due condizioni
diverse, e la seconda lascia passare chiamate che devono fallire.

C'è però un secondo tipo di precondizione, che è legittimamente un esistenziale: la
**precondizione di buona definizione**, quella che garantisce che il calcolo abbia senso. Se
un'operazione divide per la cardinalità di un insieme ricavato dallo stato, la non-vuotezza di
quell'insieme non dipende dai parametri e non può che essere espressa così:

```
durata_media_prestiti(da:Data, a:Data): Reale >= 0
	pre:
		- da <= a                                    // precondizione sui parametri
		- l'insieme P dei prestiti conclusi nel periodo è non vuoto   // buona definizione

		Formalmente:
		da <= a  and  EXISTS p  p in P.
```

Le due convivono: quelle sui parametri controllano l'input, quelle di buona definizione
proteggono l'operazione da stati in cui il risultato non esiste.

### Insiemi ordinati

Quando un'operazione deve restituire una **sequenza ordinata**, in logica un insieme non ha
ordine: serve la convenzione del `Documento A.4.1 - Definire insiemi ordinati`
(`BDD2-corpus-nuovo/teoria/A.4.1 - Definire insiemi ordinati.md`).

Il risultato non è una lista ma un **insieme di coppie (elemento, posizione)**:

```
scaffali_da_visitare(): (s:Scaffale, pos:Intero > 0) [0..*]
```

Il calcolo si scrive con `sorted`, che prende **due argomenti separati da punto e virgola**:
l'insieme da ordinare e il **criterio d'ordine**.

```
	post:
		S = { s | Scaffale(s) and EXISTS c  copia_scaffale(c, s) and c.da_ricollocare() }

		result = sorted(S; scaffale_LEQ)
```

`sorted` da sola non saprebbe con quale criterio ordinare: il secondo argomento è una funzione
booleana che, dati due elementi, dice se il primo precede o pareggia il secondo. Il suffisso
`_LEQ` (*less or equal*) è la convenzione di denominazione usata dal corso.

### `dove`: le operazioni ausiliarie si definiscono sul posto

Il criterio d'ordine, e in generale ogni operazione che serve solo a scrivere una formula, si
definisce **subito sotto**, introdotta da `dove`. Non va nel diagramma né fra le segnature degli
use-case: quelle elencano ciò che il sistema offre, non gli strumenti interni di una specifica.
Per la stessa ragione **un `dove` non eredita lo status di barrato** dell'operazione che lo usa:
non è un requisito, quindi non compare in Domanda 4 e non conta nell'ambito delle Domande 5 e 8.

```
		dove scaffale_LEQ(s1:Scaffale, s2:Scaffale): Booleano
				pre: nessuna
				post:
					Siano sala1, sala2, n1, n2 tali da soddisfare:

						EXISTS sa1, sa2
							scaff_sala(s1, sa1) and numero(sa1, sala1) and numero(s1, n1) and
							scaff_sala(s2, sa2) and numero(sa2, sala2) and numero(s2, n2).

					result = vero <-->
						[ sala2 > sala1 or (sala2 = sala1 and n2 >= n1) ]
```

Il criterio si legge: prima per sala, e a parità di sala per numero di scaffale. Ordinamenti a
più chiavi si scrivono sempre così, con la disgiunzione fra "la chiave principale è maggiore" e
"le chiavi principali pareggiano e decide la successiva".

Questo risolve anche la tentazione di dare all'elemento un attributo `posizione` nel diagramma:
se l'ordine è **derivabile** da dati già presenti, l'attributo è ridondante e l'ordine si calcola.
Un attributo `ordine` si giustifica solo quando la posizione è un dato indipendente, scelto e
memorizzato.

### I tipi di dato hanno vincoli e operazioni, come le classi

Un tipo strutturato non è solo un elenco di campi: porta i suoi **vincoli nominati** e le sue
**operazioni**, scritti esattamente come quelli di una classe. È la forma della specifica ufficiale
dei tipi di QuickHospital:

```
Periodo:
	- da:DataOra [0..1]
	- a:DataOra [0..1]

	[V.Periodo.legale]
		ALL p, x,y   Periodo(p) and da(p,x) and a(p,y) --> y >= x.

	interseca(p1:Periodo, p2:Periodo):Booleano
		pre: nessuna
		post: ...
```

Due conseguenze pratiche. Un tipo che deve rispettare una condizione — orari a scatti di
mezz'ora, capienze coerenti — la esprime con un `[V.Tipo.nome]` in logica, non con una frase in
italiano sotto il nome. E un vincolo esterno che confronta due valori dello stesso tipo — due
periodi che non si sovrappongono — si scrive appoggiandosi a **un'operazione del tipo**, non
ripetendo le disuguaglianze incrociate a ogni uso.

Per le stringhe resta la forma breve `Stringa ~ '...'`.

### Un'operazione che non calcola non si scrive

Se il corpo si limita a navigare un'associazione e restituire un attributo che sta già lì, non è
un'operazione: nella formula si naviga direttamente. Un'operazione si giustifica quando **calcola**
— applica uno sconto, moltiplica una tariffa per una durata, sceglie un massimo.

### Costanti e aritmetica temporale

Le soluzioni ufficiali usano `adesso` senza definirlo. Vale la pena dichiarare le costanti in
testa alla specifica, una volta, invece di introdurle di soppiatto:

```
Costanti: adesso : DataOra   // l'istante corrente
          oggi   : Data      // la data corrente, = data(adesso)
```

**L'aritmetica su date ha una convenzione ufficiale, ed è questa.** La regola che la governa
tutta: **la differenza fra due date è una `Durata`, non un numero.**

| Cosa | Come si scrive | Dove lo fa il prof |
|---|---|---|
| data + durata → data | `this.inizio + i.durata_g()`, `this.inizio + this.durata` | `fine()` di Travel to the Moon |
| data − data → durata | `d - this.nascita`, `adesso - i` | `eta()` di Cliente; `registra_termine` di QuickHospital |
| durata → numero di unità | un **predicato** dichiarato sul posto: `anni(d - n, result)` | `eta()` di Cliente |
| confronto fra istanti | direttamente: `i <= adesso`, `ipres >= ipren` | QuickHospital, ovunque |
| confronto fra una `DataOra` e una `Data` | si porta l'istante a data con `data(·)`, dichiarata come funzione di mondo reale — `data(i) >= installazione` | analogo di `oggi = data(adesso)` |

Il passaggio che si sbaglia è il terzo. Convertire una durata in giorni o anni **non è
un'operazione aritmetica**: è un predicato binario con semantica di mondo reale, che si dichiara
in una nota sotto la specifica. La soluzione ufficiale di Travel to the Moon lo scrive testualmente:

```
	ALL n   nascita(this, n) --> anni(d - n, result).

	Nota:
		anni/2 è un simbolo di predicato per il tipo Durata soggetto alla semantica di mondo
		reale. La semantica di anni(d,x) è che d:Durata è pari a x anni (intero)
```

Stessa forma per `giorni(d, x)`, `ore(d, x)`: dichiara il predicato una volta, poi usalo. Non
inventare `d.giorni()` né una divisione.

Per costruire una `DataOra` da una `Data` e un'`Ora` non c'è esempio ufficiale: dichiara la
notazione che usi prima di usarla.

### Side effect

Le operazioni che modificano lo stato descrivono la variazione dell'interpretazione. `ALPHA` è
il nuovo elemento del dominio.

```
post:
	Viene creato e restituito un nuovo oggetto result:Prestito tale che:
		- result.inizio = la data corrente
	Viene creato il link (result, let):prest_paziente.
	Viene creato il link (result, c):prest_copia.

	Formalmente:

	Side effect:
	- Variazioni degli elementi del dominio di int.: ALPHA
	- Variazioni nell'interpretazione dei simboli di predicato:
		Prestito(ALPHA)
		inizio(ALPHA, oggi)
		prest_paziente(ALPHA, let)
		prest_copia(ALPHA, c)

	result = ALPHA
```

Vanno elencate **tutte** le variazioni: la classe di appartenenza, ogni attributo valorizzato e
ogni link creato. Dimenticare un link è un errore sostanziale, perché lo stato risultante non
soddisfa più i vincoli del diagramma.

#### Cancellare e modificare

Il materiale del corso mostra solo la creazione, ma la semantica lo determina: un'interpretazione
è **dominio + interpretazione dei simboli di predicato**, e un side effect è il passaggio da
un'interpretazione all'altra. Le altre due forme seguono per simmetria.

**Cancellazione** — l'oggetto esce dal dominio, e con lui cessano tutti i fatti che lo nominano:

```
	Side effect:
	- Variazioni degli elementi del dominio di int.: rimozione di p
	- Variazioni nell'interpretazione dei simboli di predicato:
		cessano tutti i fatti che coinvolgono p
```

I link non si elencano uno per uno: eliminando l'oggetto si considerano rimossi automaticamente,
perché non esiste più nulla che possa stare agli estremi.

**Modifica di un attributo** — il dominio non cambia, cambia solo l'interpretazione del predicato
di quell'attributo: la coppia vecchia smette di valere, la nuova comincia.

```
	Side effect:
	- Variazioni degli elementi del dominio di int.: nessuna
	- Variazioni nell'interpretazione dei simboli di predicato:
		non piu'  stato(p, 'aperto')
		          stato(p, 'chiuso')
```

Lo stesso vale per rimuovere un singolo link senza cancellare gli oggetti: `non piu'` sul fatto
di associazione. Scrivere solo il fatto nuovo senza dichiarare che il vecchio cessa lascia uno
stato in cui l'attributo ha due valori, che viola la molteplicità del diagramma.

## Interpretazioni

Alcuni esercizi chiedono, dopo ogni formula, un'interpretazione che ne sia un modello. Si dà il
dominio e l'estensione di ogni predicato:

```
D = {α, β, γ, δ}
Persona/1 = {α, β}
Stringa/1 = {γ, δ}
nome/2 = {(α, γ), (β, δ)}
```

I predicati si dichiarano con l'arietà (`Persona/1`, `nome/2`). Un'interpretazione va scelta
piccola ma non degenere: deve rendere vera la formula **e** mostrare che dice qualcosa, quindi
evita domini in cui la formula è vera solo perché l'antecedente è sempre falso.
