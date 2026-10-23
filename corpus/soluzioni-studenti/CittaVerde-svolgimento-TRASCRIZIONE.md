# Città Verde — svolgimento di studente-A (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-A/Progetti/Città Verde/Città Verde.pdf`, 28 pagine
> (le prime 4 sono il testo del progetto, il modulo risposte comincia a pagina 5), modulo
> **`Versione 2024-06-05.UML`** compilato a mano. Trascritto da Claude leggendo le pagine come
> immagini: **il documento è il PDF, questo è una copia a macchina e può contenere errori di
> lettura.** I punti dubbi sono marcati `[?]`.
>
> ✅ **Svolgimento completo:** tutte e 8 le domande hanno risposta. Le pagine di continuazione
> (6, 8, 12, 20 del PDF) sono in bianco: gli spazi previsti sono bastati.
>
> Testo del progetto: `progetti/14 - Città Verde.md`. **Non è una soluzione ufficiale e nessuno
> l'ha corretta**: il modulo non porta né nome né voto. Secondo
> `soluzioni-studenti/INVENTARIO-FONTI.md` è la traccia dell'appello che l'utente ha tentato;
> come testo è il progetto 14 del corso, non una delle 40 tracce d'esame.
>
> **La barra laterale** (il rettangolo nero nel margine) è visibile sulla pagina della Domanda 5:
> l'ambito delle Domande 5 e 8 è quello dei requisiti barrati, e infatti lo studente sviluppa solo
> tre operazioni — `SQUADREPOSSIBILIINTERVENTO`, `NOINTERVENTI`, `CALCTASSO`.
>
> Numerazione: le pagine citate qui sotto sono quelle **stampate** sul modulo.

---

## Domanda 1 — Raffinamento dei requisiti (pagina 5)

Non un elenco numerato: un abbozzo del dizionario dei dati, in due colonne.

**Sogg Verde:**
- dataPia : Data
- lat : Reale
- long : Reale
- rischio : Rischio
- specializzazione:
  - Rimosso:
    - dataRim : Data
    - associato alla CausaRim
- associato all'Area Verde
- associato alla Specie
- associato alle Misure con valore : Reale > 0

**Area Verde:**
- nome : Stringa
- specializzazione:
  - Fruibile
    - Sensibile
  - Non Fruibile
- associato al TipoArea

**Attrezzo:**
- nome : Stringa
- tipoAttr : TipoAttr

**Intervento:**
- inInt : Data
- durataGg : Intero > 0
- fineInt : Data [0..1]
- nPers : Intero > 0
- prio : 1..10
- associato al TipoInt
- associato agli Attrezzi

**Squadra:**
- cod : CodSquadra
- dataForm : Data [0..1]  `[?]` il `[0..1]` sul diagramma sta su `dataSc`, non su `dataFor`
- associato agli Operatori

**Operatore:**
- nome : Stringa
- cognome : Stringa
- dataIn : Data
- dataFine : Data [0..1]
- CF : CodiceFiscale

**Malattia:**
- nomeCom : Stringa
- nomeSc : Stringa
- gravità : Grav

---

## Domanda 2 — Diagramma UML concettuale delle classi (pagina 7)

### Classi

| Classe | Attributi | Operazioni |
|---|---|---|
| `SPECIE` | nomeCom : Stringa `{id1}` · nomeSc : Stringa `{id2}` | |
| `MALATTIA` | nomeCom : Stringa `{id1}` · nomeSc : Stringa `{id2}` · grav : Grav | |
| `SOGG VERDE` | dataPia : Data · lat : Reale · long : Reale · rischio : Rischio | |
| `SOGGRIM` | dataRim : Data | sottoclasse di `SOGG VERDE` |
| `CAUSARIM` | nome : Stringa `{id}` | |
| `TIPOMISURA` | nome : Stringa · unita : Stringa | |
| `PERIODOMAL` | inMal : Data · fineMal : Data [0..1] | |
| `AREA VERDE` | nome : Stringa `{id}` | |
| `TIPOAREA` | nome : Stringa `{id}` | |
| `INTERVENTO` | inInt : Data · durataGg : Intero > 0 · fineInt : Data [0..1] · nPers : Intero > 0 · prio : 1..10 | |
| `TIPOINT` | nome : Stringa `{id}` | |
| `ATTREZZO` | nome : Stringa `{id}` · tipoAtt : TipoAtt | |
| `SQUADRA` | cod : CodSqua `{id}` · dataFor : Data · dataSc : Data [0..1] | |
| `OPERATORE` | nome : Stringa · cognome : Stringa · dataIn : Data · dataFine : Data [0..1] · CF : CodiceFiscale `{id}` | |
| `PARTECIPA` | inPar : Data · finePar : Data | classe che reifica la partecipazione |
| `CAPO` | — | sottoclasse di `PARTECIPA` |

### Associazioni

| Associazione | Estremo 1 | Estremo 2 | Note |
|---|---|---|---|
| `SOGSPE` | `SPECIE` 1 | `SOGG VERDE` 0..* | |
| `MISSOG` | `TIPOMISURA` 0..* | `SOGG VERDE` 0..* | **classe associativa**, con `valore : Reale > 0` |
| `CAURIM` | `CAUSARIM` 1 | `SOGGRIM` 0..* | la causa della rimozione |
| `MALPER` | `MALATTIA` 1 | `PERIODOMAL` 0..* | |
| `MALSOG` | `SOGG VERDE` 1 | `PERIODOMAL` 0..* | |
| `AREASOG` | `AREA VERDE` 1 | `SOGG VERDE` 0..* | |
| `AREATIPO` | `AREA VERDE` 0..* | `TIPOAREA` 1 | |
| `AREAINT` | `AREA VERDE` 1 | `INTERVENTO` 0..* | |
| `INTSOG` | `SOGG VERDE` 0..* | `INTERVENTO` 0..* | |
| `INTTIPO` | `INTERVENTO` 0..* | `TIPOINT` 0..* | |
| `ATTINT` | `INTERVENTO` 0..* | `ATTREZZO` 0..* | |
| `ATTOPE` | `ATTREZZO` 0..* | `OPERATORE` 0..* | l'abilitazione dell'operatore all'attrezzo |
| `INTSQU` | `INTERVENTO` 0..* | `SQUADRA` 0..1 | **classe associativa**, con `istAcq : DataOra` |
| `PARSQU` | `SQUADRA` 1 | `PARTECIPA` 0..* | |
| `OPEPAR` | `PARTECIPA` 0..* | `OPERATORE` 1 | |
| `CAPSQU` | `SQUADRA` 1 | `CAPO` 0..* | |
| `CAPOPE` | `CAPO` 0..* | `OPERATORE` 1 | |

### Generalizzazioni

- `SOGGRIM` specializza `SOGG VERDE` (nessun vincolo)
- `FRUIBILE` e `NON FRUIBILE` specializzano `AREA VERDE` `{compl, disj}`
- `SENSIBILE` specializza `FRUIBILE`
- `CAPO` specializza `PARTECIPA` _(fra classi: `PARTECIPA` è la reificazione dell'associazione,
  non una classe associativa disegnata sul link)_

`FRUIBILE`, `NON FRUIBILE` e `SENSIBILE` sono riquadri senza attributi.

### Specifiche delle classi e delle associazioni (pagine 9-10)

**1 — Classe `SOGG VERDE`**

```
V.RIMDOPOPIA
∀s SOGGRIM(s) → ∃p, m  DATAPIA(s, p) ∧ DATARIM(s, m) → p <= m

V.MALINVITA
∀s, m, dp, i   MALSOG(s, m) ∧ DATAPIA(dp, s) ∧ INMAL(i, m)
  → i >= dp ∧ (∀u DATARIM(u, s) → ∃f FINEMAL(f, m) ∧ f <= u)
```

**2 — Classe `SOGG VERDE`**

```
V.STESSAMALDISG
∀s SOGGVERDE(s) → ¬∃ p, p', i, i', m, t
  MALSOG(p, s) ∧ MALSOG(p', s) ∧ MALPER(m, p) ∧ p ≠ p' ∧ MALPER(m, p')
  ∧ INMAL(p, i) ∧ INMAL(p', i') ∧ DATA(t) ∧ t >= i ∧ t >= i'
  ∧ (∀f FINEMAL(p, f) → t <= f) ∧ (∀f' FINEMAL(p', f') → t <= f')
```

**3 — Classe `SOGG VERDE`**

```
V.INTINVITA
∀s, i, ii, dp   INTSOG(s, i) ∧ DATAPIA(s, dp) ∧ ININT(i, ii) ∧ ii >= dp
  ∧ (∀u DATARIM(u, s) → ∃f FINEINT(i, f) ∧ f <= u)
```

`[?]` la formula è scritta come congiunzione, senza l'implicazione principale.

**4 — Classe `SQUADRA`**

```
V.CAPIDISG
∀s SQUADRA(s) → ¬∃ c, c', i, i', f, f', t
  CAPSQU(s, c) ∧ CAPSQU(s, c') ∧ c ≠ c' ∧ INPAR(c, i) ∧ FINEPAR(c, f)
  ∧ INPAR(c', i') ∧ FINEPAR(c', f') ∧ DATA(t) ∧ i <= t <= f ∧ i' <= t <= f'

V.FINEDOPOINIZIO
∀s, is, fs   SQUADRA(s) ∧ DATAFOR(s, is) ∧ DATASC(s, fs) → fs >= is
```

**5 — Classe `PARTECIPA`**

```
V.DENTROSQUADRAOPE
∀p, o, s, ip, fp, is, io   OPEPAR(o, p) ∧ PARSQU(p, s) ∧ INPAR(p, ip)
  ∧ FINEPAR(p, fp) ∧ DATAIN(o, io) ∧ DATAFOR(s, is)
  → is >= ip ∧ io >= ip                                    [?] letto così: forse ip >= is ∧ ip >= io
  ∧ (∀fs DATASC(s, fs) → fp <= fs)
  ∧ (∀fo DATAFINE(o, fo) → fp <= fo)

V.FINEDOPOINIZIO
∀p, i, f   PARTECIPA(p) ∧ INPAR(p, i) ∧ FINEPAR(p, f) → f >= i
```

**6 — Classe `INTERVENTO`**

```
V.SOGGINAREA
∀i, s, a   INTSOG(i, s) ∧ AREAINT(a, i) → AREASOG(a, s)

V.FINEDOPOINIZIO
∀i, ii, fi   INTERVENTO(i) ∧ ININT(i, ii) ∧ FINEINT(i, fi) → fi >= ii
```

**7 — Classe `OPERATORE`**

```
V.PARTDISG
∀o OPERATORE(o) → ¬∃ p, p', i, i', f, f', t
  OPEPAR(o, p) ∧ OPEPAR(o, p') ∧ p ≠ p' ∧ INPAR(p, i) ∧ INPAR(p', i')
  ∧ FINEPAR(p, f) ∧ FINEPAR(p', f') ∧ DATA(t) ∧ i <= t <= f ∧ i' <= t <= f'

V.FINEDOPOINIZIO
∀o, i, f   OPERATORE(o) ∧ DATAIN(o, i) ∧ DATAFINE(o, f) → i <= f
```

**8 — Classe `PERIODOMAL`**

```
V.FINEDOPOINIZIO
∀p, i, f   PERIODOMAL(p) ∧ INMAL(p, i) ∧ FINEMAL(p, f) → f >= i
```

Lo schema del vincolo `V.FINEDOPOINIZIO` è ripetuto identico su quattro classi: `SQUADRA`,
`PARTECIPA`, `INTERVENTO`, `OPERATORE`, `PERIODOMAL`.

### Specifiche dei tipi di dato e ulteriori vincoli esterni (pagina 11)

```
V.INTSQU.DENTROINTSQUA
∀i, s, ia, ii, is   INTSQU(i, s) ∧ ISTACQ(i, s, ia) ∧ ININT(i, ii) ∧ DATAFOR(s, is)
  → ∃d DATA(ia, d) ∧ d <= ii ∧ d >= is ∧ (∀fs DATASC(s, fs) → d <= fs)

V.AREA.INTERVENTIDISG
∀a AREAVERDE(a) → ¬∃ i, i', ii, ii', t
  AREAINT(a, i) ∧ AREAINT(a, i') ∧ ININT(i, ii) ∧ ININT(i', ii') ∧ DATA(t) ∧ ii <= t
  ∧ (∀fi FINEINT(fi, i) → t <= fi) ∧ (∀fi' FINEINT(fi', i') → t <= fi') ∧ ii' <= t

V.INTERVENTO.SQUAPOSSIBILE
∀i, s, a   INTSQU(i, s) ∧ ATTINT(a, i)
  → ∃ii, is  ININT(i, ii) ∧ DATAFOR(s, is)
  ∧ (∀fs DATASC(s, fs) → ∃fi FINEINT(fi, i) ∧ fi <= fs)
  ∧ ∃o, io, fo  ATTOPE(a, o) ∧ OPEPAR(o, p) ∧ PARSQU(p, s) ∧ INPAR(io, p)
      ∧ FINEPAR(fo, p) ∧ io <= ii ∧ (∀fi FINEINT(fi, i) → fi <= fo)
  ∧ ∃n NPERS(i, n) ∧ n <=
      | { o | OPERATORE(o) ∧ ∃p PARSQU(p, s) ∧ OPEPAR(o, p)
              ∧ ∃ip, fp INPAR(p, ip) ∧ FINEPAR(p, fp) ∧ ip <= ii
              ∧ (∀fi FINEINT(fi, i) → fi <= fp) } |
```

Il vincolo sul numero di persone è scritto con la **cardinalità di un insieme definito per
comprensione**, non con una somma.

```
RISCHIO       : (TRASC, BASSO, MEDIO, ALTO)
GRAV          : (BASSA, MEDIA, ALTA, MORTALE)
CODSQUA       : Stringa secondo standard
CODICEFISCALE : Stringa secondo standard
TIPOATTR      : (LEGGERO, VEICOLO, VEISPECIALE)
```

---

## Domanda 3 — Diagramma degli use-case (pagina 13)

```
## Use case

Attori: COMUNE, MANAGEMENT, OPERATORE, SISTEMA

COMUNE     — GESTISCI VERDE, GESTISCI ATTREZZI
MANAGEMENT — GESTIONE SQUADRA, GESTIONE INTERVENTI, AREE SENSIBILI
OPERATORE  — INTERVENTI ESEGUITI
SISTEMA    — CERCA SQUADRE, TASSO MALATTIA
```

Nessuna generalizzazione fra attori, nessun `«include»`/`«extend»`. `SISTEMA` è un attore a sé,
per le due funzionalità che il sistema svolge da solo.

---

## Domanda 4 — Segnature delle operazioni di use-case (pagina 15)

```
GESTISCI VERDE:
- NEWAREA(n: Stringa, t: TipoArea) : AreaVerde
- NEWSOGG(lat: Reale, long: Reale, r: Rischio, s: Specie) : SoggVerde

GESTISCI ATTREZZI:
- DAIPERMESSO(a: Attrezzo, o: Operatore)

GESTISCI SQUADRA:
- NEWSQUADRA(c: CodSqua) : Squadra
- ASSUMI(s: Squadra, o: Operatore, i: Data, f: Data) : Partecipa

GESTISCI INTERVENTI:
- NEWINT(i: Data, d: Intero > 0, n: Intero > 0, p: 1..10, t: TipoInt [0..*],
         a: Attrezzo [0..*], ar: AreaVerde) : Intervento

AREESENSIBILI:
- NOINTERVENTI(i: Data, f: Data) : AreaVerde [0..*]

INTERVENTI ESEGUITI:
- INTDATA(o: Operatore, d: Data) : Intervento [0..*]
- INTPIANTA(o: Operatore, s: SoggVerde) : Intervento [0..*]

CERCASQUADRE:
- SQUADREPOSSIBILIINTERVENTO(i: Intervento) : Squadra [0..*]

TASSOMALATTIA:
- CALCTASSO(m: Malattia [1..*], i: Data, f: Data) : (Malattia, Reale >= 0) [0..*]
```

---

## Domanda 5 — Specifiche concettuali delle operazioni (pagine 17-18)

Sviluppate **tre** operazioni: quelle che ricadono sotto la barra laterale.

```
SQUADREPOSSIBILIINTERVENTO(i: Intervento) : Squadra [0..*]
- pre: ¬∃s INTSQU(i, s)
- post: siano ii, d, n tali che:
        ININT(i, ii) ∧ DURATA(i, d) ∧ NPERS(i, n)

  A = { a | ATTINT(a, i) }

  RESULT = { s | SQUADRA(s) ∧ ∀a ∈ A  ∃p, ip, fp, o
                   ATTOPE(a, o) ∧ OPEPAR(p, o) ∧ PARSQU(p, s) ∧ INPAR(p, ip)
                   ∧ FINEPAR(p, fp) ∧ ip <= ii ∧ fp >= ii + d 'GIORNI'
                 ∧ n <= | { o | OPERATORE(o) ∧ ∃p, ip, fp  PARSQU(p, s) ∧ OPEPAR(p, o)
                               ∧ INPAR(p, ip) ∧ FINEPAR(p, fp)
                               ∧ fp >= ii + d 'GIORNI' ∧ ii >= ip } | }
```

```
NOINTERVENTI(i: Data, f: Data) : AreaVerde [0..*]
- pre: i <= f
- post:
  RESULT = { a | SENSIBILE(a) ∧ ¬∃ int, ii, t  INTERVENTO(int) ∧ ININT(int, ii)
                 ∧ DATA(t) ∧ i <= t <= f ∧ t >= ii
                 ∧ (∀fi FINEINT(int, fi) → t <= fi) }
```

```
CALCTASSO(m: Malattia [1..*], i: Data, f: Data) : (Malattia, Reale >= 0) [0..*]
- pre: i >= f            [?] verosimilmente i <= f
- post:
  M = { (mal, n) | mal ∈ m ∧
        n = | { s | SOGGVERDE(s) ∧ ∃p, ip, fp, t  MALSOG(s, p) ∧ MALPER(m, p)
                    ∧ DATA(t) ∧ i <= t <= f ∧ ip <= t <= fp
                    ∧ INMAL(p, ip) ∧ FINEMAL(p, fp) } | }

  T = { s | SOGGVERDE(s) ∧ ∃p, ip, fp, t  MALSOG(s, p) ∧ DATA(t)
            ∧ i <= t <= f ∧ ip <= t <= fp ∧ INMAL(p, ip) ∧ FINEMAL(p, fp) }

  RESULT = { (mal', tas) | ∃n' (mal', n') ∈ M ∧ tas = n' / |T| }
```

Il tasso è il rapporto fra due cardinalità di insiemi, definite come insiemi ausiliari `M` e `T`
prima del `RESULT`.

---

## Domanda 6 — Ristrutturazione (pagine 19-21)

**DBMS da utilizzare: PostgreSQL.**

### Corrispondenza fra tipi di dato concettuali e domini

```sql
CREATE DOMAIN STRINGA AS VARCHAR NOT NULL;
CREATE DOMAIN INTGZ AS INTEGER CHECK (VALUE > 0);
CREATE DOMAIN REALGZ AS REAL CHECK (VALUE > 0);
CREATE DOMAIN REALGEZ AS REAL CHECK (VALUE >= 0);
CREATE DOMAIN CODSQUADRA AS VARCHAR;
CREATE DOMAIN CODICEFISCALE AS VARCHAR;
CREATE TYPE GRAV AS ENUM ('BASSA', 'MEDIA', 'ALTA', 'MORTALE');
CREATE TYPE TIPOATT AS ENUM ('LEGGERO', 'VEICOLO', 'VEISPECIALE');
CREATE DOMAIN PRIO AS INTEGER CHECK (VALUE >= 1 AND VALUE <= 10);
```

### Diagramma UML ristrutturato (pagina 20)

Rispetto al concettuale:

- `SOGG VERDE` assorbe `SOGGRIM`: prende `id : SERIAL {id}` e `dataRim : DATE [0..1]`, e
  l'associazione `CAURIM` si attacca a `SOGG VERDE` (`CAUSARIM` 1 — `SOGG VERDE` 0..*);
- `AREA VERDE` assorbe la gerarchia `FRUIBILE`/`NON FRUIBILE`/`SENSIBILE` in due booleani:
  `fruibile : BOOL` e `sensibile : BOOL`;
- `CAPO` viene **staccata** da `PARTECIPA` e diventa una classe a sé con
  `id : SERIAL {id}`, `inizio : DATE`, `fine : DATE`, legata a `SQUADRA` (`CAPSQU`) e a
  `OPERATORE` (`CAPOPE`);
- identificatori primari tecnici dove servivano: `id : SERIAL {id}` su `SOGG VERDE`,
  `PERIODOMAL`, `TIPOMISURA`, `INTERVENTO`, `PARTECIPA`, `CAPO`;
- i tipi concettuali diventano domini SQL: `Data` → `DATE`, `Reale` → `REAL`,
  `Intero > 0` → `INTGZ`, `Reale > 0` → `REALGZ`, `DataOra` → `TIMESTAMP`, `1..10` → `PRIO`;
- `AREATIPO` diventa `AREA VERDE` 0..* — `TIPOAREA` 1;
- `INTSQU` resta classe associativa con `istAcq : TIMESTAMP` fra `INTERVENTO` 0..* e
  `SQUADRA` 0..1.

### Breve descrizione delle scelte (pagina 21)

```
FUSIONE SU SOGG VERDE
FUSIONE SU AREA VERDE
DIVISIONE SU CAPO
```

Tre parole per tre scelte: due fusioni di gerarchia verso l'alto e una divisione della
sottoclasse `CAPO` in classe autonoma.

### Vincoli esterni introdotti o modificati (pagina 21)

```
V.CAPO.SEPARTECIPA
∀o, c, s, ic, f   CAPOPE(c, o) ∧ CAPSQU(c, s) ∧ INIZIO(c, ic) ∧ FINE(c, if)
  → ∃p  OPEPAR(o, p) ∧ PARSQU(s, p) ∧ INPAR(p, ic) ∧ FINEPAR(p, fc)

V.SOGGVERDE.CAUSASERIMOSSO
∀s SOGGVERDE(s) → (∃d DATARIM(d, s) ⟺ ∃c CAUSARIM(c, s))

V.AREAVERDE.SENSIBILESEFRUIBILE
∀a AREAVERDE(a) ∧ SENSIBILE(a, TRUE) → FRUIBILE(a, TRUE)
```

I tre vincoli sono esattamente il prezzo delle tre scelte: la divisione di `CAPO` richiede che il
capo partecipi davvero, la fusione di `SOGGRIM` richiede che `dataRim` e la causa ci siano o
manchino insieme, la fusione della gerarchia delle aree richiede che «sensibile» implichi
«fruibile».

---

## Domanda 7 — Schema relazionale (pagine 23-28)

Venti relazioni. Chiave primaria sottolineata (qui in **grassetto**), `*` = può essere NULL.

| # | Relazione | Da | Attributi (domini) | Vincoli | Accorpa |
|---|---|---|---|---|---|
| 1 | `MALATTIA` | classe | nomeCom (Stringa) · **nomeSc** (Stringa) · grav (Grav) | `UNIQUE(nomeCom)` | |
| 2 | `PERIODOMAL` | classe | **id** (Serial) · inMal (Date) · fineMal* (Date) · mal (Stringa) · sogg (Integer) | `FK(mal) REF MALATTIA(nomeSc)` · `FK(sogg) REF SOGGVERDE(id)` · `CHECK(inMal <= fineMal)` | `MALPER`, `MALSOG` |
| 3 | `SOGGVERDE` | classe | **id** (Serial) · dataPia (Date) · dataRim* (Date) · lat (Real) · long (Real) · rischio (Rischio) · causa* (Stringa) · specie (Stringa) · area (Stringa) | `FK(causa) REF CAUSA(nome)` · `FK(area) REF AREAVERDE(nome)` · `FK(specie) REF SPECIE(nomeSc)` · `CHECK(dataPia < dataRim)` · `CHECK((dataRim IS NULL) = (causa IS NULL))` | `CAURIM`, `SOGSPE`, `AREASOG` |
| 4 | `CAUSARIM` | classe | **nome** (Stringa) | | |
| 5 | `SPECIE` | classe | nomeCom (Stringa) · **nomeSc** (Stringa) | `UNIQUE(nomeCom)` | |
| 6 | `TIPOMISURA` | classe | **id** (Serial) · **nome** (Stringa) · **unita** (Stringa) `[?]` sottolineati tutti e tre | | |
| 7 | `MISSOG` | associazione | **sogg** (Integer) · **misura** (Integer) · valore (RealGZ) | `FK(sogg) REF SOGGVERDE(id)` · `FK(misura) REF TIPOMISURA(id)` | |
| 8 | `AREAVERDE` | classe | **nome** (Stringa) · fruibile (Bool) · sensibile (Bool) · tipo (Stringa) | `FK(tipo) REF TIPOAREA(nome)` · `CHECK((sensibile = FALSE) OR (sensibile = TRUE AND fruibile = TRUE))` | `AREATIPO` |
| 9 | `TIPOAREA` | classe | **nome** (Stringa) | | |
| 10 | `INTERVENTO` | classe | **id** (Serial) · inInt (Date) · durataGg (IntGZ) · fineInt* (Date) · nPers (IntGZ) · prio (Prio) · squa* (CodSquadra) · istAcq* (Timestamp) | `FK(squa) REF SQUADRA(cod)` · `CHECK(inInt <= fineInt)` · `CHECK((squa IS NULL) = (istAcq IS NULL))` · `CHECK(CAST(istAcq AS DATE) < inInt)` | `INTSQU` |
| 11 | `INTSOG` | associazione | **int** (Integer) · **sogg** (Integer) | `FK(int) REF INTERVENTO(id)` · `FK(sogg) REF SOGGVERDE(id)` | |
| 12 | `TIPOINT` | associazione `[?]` è una classe | **nome** (Stringa) | | |
| 13 | `INTTIPO` | associazione | **int** (Integer) · **tipo** (Stringa) | `FK(int) REF INTERVENTO(id)` · `FK(tipo) REF TIPOINT(nome)` | |
| 14 | `ATTREZZO` | classe | **nome** (Stringa) · tipoAtt (TipoAtt) | | |
| 15 | `ATTINT` | associazione | **int** (Integer) · **att** (Stringa) | `FK(int) REF INTERVENTO(id)` · `FK(att) REF ATTREZZO(nome)` | |
| 16 | `OPERATORE` | classe | nome (Stringa) · cognome (Stringa) · dataIn (Date) · dataFine* (Date) · **cf** (CodiceFiscale) `[?]` la sottolineatura non si vede, ma `cf` è la chiave usata dalle FK | `CHECK(dataFine >= dataIn)` | |
| 17 | `ATTOPE` | associazione | **att** (Stringa) · **ope** (CodiceFiscale) | `FK(ope) REF OPERATORE(cf)` · `FK(att) REF ATTREZZO(nome)` | |
| 18 | `SQUADRA` | classe | **cod** (CodSquadra) · dataFor (Date) · dataSc* (Date) | `CHECK(dataFor < dataSc)` | |
| 19 | `PARTECIPA` | classe | **id** (Serial) · inPar (Date) · finePar (Date) · squadra (CodSquadra) · ope (CodiceFiscale) | `CHECK(inPar < finePar)` · `FK(ope) REF OPERATORE(cf)` · `FK(squadra) REF SQUADRA(cod)` | `PARSQU`, `OPEPAR` |
| 20 | `CAPO` | classe | **id** (Serial) · inizio (Date) · fine (Date) · squadra (CodSquadra) · ope (CodiceFiscale) | `CHECK(inPar < finePar)` · `(squadra, ope, inizio, fine) ⊆ PARTECIPA(squadra, ope, inizioPar, finePar)` _(vincolo di inclusione)_ · `FK(ope) REF OPERATORE(cf)` · `FK(squadra) REF SQUADRA(cod)` | `CAPSQU`, `CAPOPE` |

Da notare: il vincolo `V.CAPO.SEPARTECIPA` della Domanda 6 diventa qui un **vincolo di
inclusione** fra quattro attributi di `CAPO` e quattro di `PARTECIPA`, non un trigger.

### Ulteriori vincoli esterni — progetto dei trigger (pagine 27-28)

```
T.SOGGVERDE.MALATTIAINVITA
- INSERT OR UPDATE PERIODOMAL
VALID = EXISTS (SELECT * FROM SOGGVERDE
                WHERE ID = NEW.SOGG AND DATAPIA <= NEW.INMAL
                  AND (DATARIM IS NULL OR DATARIM >= NEW.FINEMAL))
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.SOGGVERDE.STESSAMALDISG
- INSERT OR UPDATE PERIODOMAL
ERROR = EXISTS (SELECT * FROM PERIODOMAL
                WHERE ID <> NEW.ID AND SOGG = NEW.SOGG AND MAL = NEW.MAL
                  AND (NEW.INMAL, NEW.FINEMAL) OVERLAPS (INMAL, FINEMAL))
IF ERROR: ERRORE
ELSE: COMMIT
```

```
T.INTERVENTO.SOGGETTOINAREA
- INSERT OR UPDATE INTSOG
VALID = EXISTS (SELECT * FROM SOGGVERDE s, INTERVENTO i
                WHERE s.ID = NEW.SOGG AND i.ID = NEW.INT AND s.AREA = i.AREA)
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.INTERVENTO.SQUAPOSSIBILE
- INSERT OR UPDATE INTERVENTO
VALID = EXISTS (SELECT * FROM SQUADREPOSSIBILIINTERVENTO(NEW.ID)
                WHERE SQUADRA = NEW.SQUADRA)
IF VALID: COMMIT
ELSE: ERRORE
```

Il trigger **richiama l'operazione della Domanda 8 come funzione**: `SQUADREPOSSIBILIINTERVENTO`
è usata come tabella nella `FROM`.

```
T.PARTECIPA.DENTROSQUAEOPE
- INSERT OR UPDATE PARTECIPA
VALID = EXISTS (SELECT * FROM SQUADRA s, OPERATORE o
                WHERE s.COD = NEW.SQUADRA AND o.CF = NEW.OPE
                  AND s.DATAFOR <= NEW.INPAR AND o.DATAIN <= NEW.INPAR
                  AND (s.DATASC IS NULL OR s.DATASC >= NEW.FINEPAR)
                  AND (o.DATAFINE IS NULL OR o.DATAFINE >= NEW.FINEPAR))
IF VALID: COMMIT
ELSE: ERRORE
```

Due schemi ricorrenti: `VALID = EXISTS(...)` seguito da `IF VALID: COMMIT / ELSE: ERRORE`, oppure
`ERROR = EXISTS(...)` seguito da `IF ERROR: ERRORE / ELSE: COMMIT`. L'evento intercettato e la
tabella sono sempre dichiarati sulla riga `- INSERT OR UPDATE <tabella>`.

---

## Domanda 8 — Specifiche realizzative (pagine 29-30)

Le stesse tre operazioni della Domanda 5.

```
SQUADREPOSSIBILIINTERVENTO(i: INTEGER) : CODSQUA [0..*]

ERROR = EXISTS (SELECT * FROM INTERVENTO
                WHERE ID = i AND SQUADRA IS NOT NULL)
IF ERROR: ERRORE

RETURN = WITH I AS (SELECT * FROM INTERVENTO WHERE ID = i),
              P AS (SELECT p.SQUADRA, ao.OPE, ao.ATT
                    FROM ATTOPE ao, PARTECIPA p, I
                    WHERE p.OPE = ao.OPE AND p.INPAR < I.ININT
                      AND p.FINEPAR > I.ININT + I.DURATA),
              A AS (SELECT ATT FROM ATTINT WHERE INT = i)
         SELECT PERS.SQUADRA FROM P PERS, I INFO
         WHERE (SELECT COUNT(OPE) FROM P WHERE SQUADRA = PERS.SQUADRA) >= INFO.NPERS
           AND (SELECT * FROM A
                EXCEPT
                SELECT ATT FROM P WHERE SQUADRA = PERS.SQUADRA) IS NULL
```

```
NOINTERVENTI(i: DATE, f: DATE) : STRINGA [0..*]

IF (i > f): ERRORE

RETURN = SELECT NOME FROM AREAVERDE
         WHERE SENSIBILE = TRUE
         EXCEPT
         SELECT a.NOME FROM AREAVERDE a, INTERVENTO int
         WHERE a.SENSIBILE = TRUE
           AND (int.ININT, int.FINEINT) OVERLAPS (i, f)
```

`[?]` manca il legame fra `a` e `int` nella seconda `SELECT`: come scritta, basta un intervento
qualsiasi nel periodo per escludere tutte le aree sensibili.

```
CALCTASSO(m: STRINGA [0..*], i: DATE, f: DATE) : (STRINGA, REALGEZ) [0..*]

IF (i > f): ERRORE

RETURN = WITH M AS (SELECT MAL, COUNT(DISTINCT SOGG) c FROM PERIODOMAL
                    WHERE (INMAL, FINEMAL) OVERLAPS (i, f) AND MAL IN m
                    GROUP BY MAL),
              T AS (SELECT COUNT(DISTINCT SOGG) tot FROM PERIODOMAL
                    WHERE (INMAL, FINEMAL) OVERLAPS (i, f))
         SELECT M.MAL, M.c / T.tot FROM M, T
```

Non è dichiarato, per nessuna delle tre, se vadano implementate nel DBMS o nel back-end: la
Domanda 8 lo chiede esplicitamente e la risposta lo omette.
