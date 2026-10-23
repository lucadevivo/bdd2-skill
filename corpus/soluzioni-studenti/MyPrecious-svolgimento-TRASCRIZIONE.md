# My Precious — svolgimento di studente-A (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-A/Progetti/My Precious/My Precious.pdf`, 30 pagine
> (le prime 3 sono il testo del progetto, il modulo risposte comincia a pagina 5 stampata), modulo
> **`Versione 2024-06-05.UML`** compilato a mano. Trascritto da Claude leggendo le pagine come
> immagini: **il documento è il PDF, questo è una copia a macchina e può contenere errori di
> lettura.** I punti dubbi sono marcati `[?]`.
>
> ✅ **Svolgimento completo:** tutte e 8 le domande hanno risposta, e le **tre pagine di minute
> sono usate come continuazione**: dalla pagina della Domanda 7 parte un rimando esplicito
> «CONTINUA A MINUTE 2,3» e da quella della Domanda 8 «CONTINUA MINUTE 1». È il modo corretto di
> usarle: la pagina delle minute non viene valutata *a meno che non sia puntata da pagine
> precedenti*.
>
> Testo del progetto: `progetti/15 - My Precious.md`. Esiste anche la traccia d'esame omonima,
> `tracce-esame/BD2_2022-09-09_MyPrecious.pdf`. **Non è una soluzione ufficiale e nessuno l'ha
> corretta**: il modulo non porta né nome né voto.
>
> **La barra laterale** è visibile sulla pagina della Domanda 5: le Domande 5 e 8 sviluppano solo
> le sei operazioni di statistica (`BIGLDATA`, `BIGLMEDIA`, `ESPTEMPPOPOLARE`,
> `RESOCONTOCORRENTI`, `NORESTARTISTA`, `OPERERESTVECCHIE`), non quelle di gestione.
>
> Numerazione: le pagine citate qui sotto sono quelle **stampate** sul modulo.

---

## Domanda 1 — Raffinamento dei requisiti (pagina 5)

Dizionario dei dati abbozzato, in tre colonne.

**Opera:**
- nomeOpe : Stringa
- annoOpe : Intero
- associato all'Autore
- associato alla Categoria
- associato alla Tecnica [0..1]
- associato alle Correnti

**Autore:**
- nomeAut : Stringa
- annoNasc : Intero
- annoMor : Intero [0..1]
- associato alla Città
- associato alle Opere

**Prestito:**
- inizioPre : DataOra
- finePre : DataOra
- associato all'Opera
- associato al Museo
- generalizzazione:
  - Prestito Dato
  - Prestito Preso

**Restauro:**
- inizioRes : DataOra
- fineRes : DataOra [0..1]
- associato all'Opera

**Esposizione:**
- inizioEsp : DataOra
- sezione : Stringa
- associato alle Opere
- generalizzazione:
  - Esp Perm
  - Esp Temp:
    - fineEsp : DataOra
    - nomeEsp : Stringa
    - associato a un Tema

**Biglietto:**
- dataBigl : Data
- generalizzazione:
  - Bigl Full
  - Bigl Perm
  - Bigl Temp
    - associato all'Esp Temp

---

## Domanda 2 — Diagramma UML concettuale delle classi (pagina 7)

### Classi

| Classe | Attributi | Note |
|---|---|---|
| `NAZIONE` | nome : Stringa `{id}` | |
| `CITTA` | nome : Stringa `{id1}` | identificazione esterna: `{id1}` comprende il ruolo `1` verso `NAZIONE` |
| `AUTORE` | nomeAut : Stringa `{id}` · annoNas : Intero · annoMor : Intero [0..1] | |
| `CATEGORIA` | nome : Stringa `{id}` | |
| `TECNICA` | nome : Stringa `{id}` | |
| `CORRENTE` | nome : Stringa `{id}` | |
| `OPERA` | nomeOpe : Stringa · annoOpe : Intero · prestabile : Booleano | **senza identificatore** |
| `PRESTITO` | inizioPre : DataOra · finePre : DataOra | |
| `PRESTITODATO`, `PRESTITOPRESO` | — | sottoclassi di `PRESTITO`, `{disj, compl}` |
| `MUSEO` | nome : Stringa | **senza identificatore** |
| `RESTAURO` | inizioRes : DataOra · finePres : DataOra [0..1] | |
| `ESPOSIZIONE` | inizioEsp : DataOra · sezione : Stringa | |
| `ESPPERM` | — | sottoclasse di `ESPOSIZIONE` |
| `ESPTEMP` | fineEsp : DataOra · nomeEsp : Stringa | sottoclasse di `ESPOSIZIONE`, `{disj, compl}` |
| `TEMA` | nome : Stringa `{id}` | |
| `BIGLIETTO` | dataBigl : Data | |
| `BIGLFULL`, `BIGLPERM`, `BIGLTEMP` | — | sottoclassi di `BIGLIETTO`, `{disj, compl}` |

### Associazioni

| Associazione | Estremo 1 | Estremo 2 |
|---|---|---|
| `CITNAZ` | `NAZIONE` 1 `{id1}` | `CITTA` 0..* |
| `AUTCIT` | `CITTA` 1 | `AUTORE` 0..* |
| `AUTOPE` | `AUTORE` 1 | `OPERA` 0..* |
| `CATOPE` | `CATEGORIA` 1 | `OPERA` 0..* |
| `OPETEC` | `TECNICA` 0..1 | `OPERA` 0..* |
| `COROPE` | `CORRENTE` 0..* | `OPERA` 0..* |
| `OPEPRE` | `OPERA` 1 | `PRESTITO` 0..* |
| `OPERES` | `OPERA` 1 | `RESTAURO` 0..* |
| `ESPOPE` | `OPERA` 0..* | `ESPOSIZIONE` 0..* |
| `MUSPRE` | `MUSEO` 1 | `PRESTITO` 0..* |
| `ESPTEMA` | `TEMA` 1 | `ESPTEMP` 0..* |
| `BIGESP` | `ESPTEMP` 1 | `BIGLTEMP` 0..* |

### Generalizzazioni

- `PRESTITODATO` e `PRESTITOPRESO` specializzano `PRESTITO` `{disj, compl}`
- `ESPPERM` e `ESPTEMP` specializzano `ESPOSIZIONE` `{disj, compl}`
- `BIGLFULL`, `BIGLPERM` e `BIGLTEMP` specializzano `BIGLIETTO` `{disj, compl}`

Tre gerarchie, tutte disgiunte e complete, tutte senza attributi propri tranne `ESPTEMP`.

### Specifiche delle classi e delle associazioni (pagine 9-10)

**1 — Classe `AUTORE`**

```
V.NASCEPRIMAMUORE
∀a, an, am   AUTORE(a) ∧ ANNONASC(an, a) ∧ ANNOMOR(a, am) → an < am

V.OPERAINVITA
∀o, o', an, ao   AUTORE(o, o') ∧ ANNOOPE(o', ao) ∧ ANNONASC(a, an)
  → an < ao ∧ (∀am ANNOMOR(a, am) → ao <= am)
```

**2 — Classe `PRESTITO`**

```
V.FINEDOPOINIZIO
∀p, i, f   PRESTITO(p) ∧ INIZIOPRE(p, i) ∧ FINEPRE(p, f) → i < f

V.DISGIUNTI
∀o OPERA(o) → ¬∃ p, p', i, i', f, f', d
  OPEPRE(p, o) ∧ OPEPRE(p', o) ∧ INIZIOPRE(p, i) ∧ INIZIOPRE(p', i')
  ∧ FINEPRE(p, f) ∧ FINEPRE(p', f') ∧ DATAORA(d) ∧ d > i ∧ d > i' ∧ d < f ∧ d < f'

V.DOPOANNOOPERA
∀p, i, o, a   OPEPRE(p, o) ∧ INIZIOPRE(p, i) ∧ ANNOOPE(o, a) → ∃d ANNO(i, d) ∧ a <= d
```

**3 — Classe `RESTAURO`**

```
V.FINEDOPOINIZIO
∀r, i   RESTAURO(r) ∧ INIZIORES(r, i) → (∀f FINERES(r, f) → f > i)

V.DISGIUNTI
∀o OPERA(o) → ¬∃ r, r', i, i', d
  OPERES(o, r) ∧ OPERES(o, r') ∧ INIZIORES(r, i) ∧ INIZIORES(r', i')
  ∧ DATAORA(d) ∧ d > i ∧ d > i'
  ∧ (∀f FINERES(r, f) → f > d) ∧ (∀f' FINERES(r', f') → f' > d)

V.DOPOANNOOPERA
∀r, o, i, a   OPERES(r, o) ∧ INIZIORES(i, r) ∧ ANNOOPE(o, a) → ∃d ANNO(i, d) ∧ d >= a
```

**4 — Classe `BIGLIETTO`**

```
V.DURANTEESPOSIZIONE
∀b, e, i, f, d   BIGLESP(b, e) ∧ INIZIOESP(e, i) ∧ FINEESP(e, f) ∧ DATABIGL(b, d)
  → ∃di, df  DATA(i, di) ∧ DATA(f, df) ∧ d >= di ∧ d <= df
```

**6 — Classe `ESPOSIZIONE`**

```
V.DOPOANNOOPERA
∀e, o, i, a   ESPOPE(e, o) ∧ INIZIOESP(i, e) ∧ ANNOOPE(a, o) → ∃d ANNO(i, d) ∧ d >= a

V.DISGIUNTE
∀o OPERA(o) → ¬∃ e, e', i, i', d
  ESPOPE(e, o) ∧ ESPOPE(e', o) ∧ INIZIOESP(e, i) ∧ INIZIOESP(e', i')
  ∧ DATAORA(d) ∧ d > i ∧ d > i'
  ∧ (∀f FINEESP(e, f) → d < f) ∧ (∀f' FINEESP(e', f') → d < f')

V.FINEDOPOINIZIO
∀e, i, f   ESPTEMP(e) ∧ INIZIOESP(e, i) ∧ FINEESP(e, f) → i < f
```

**7 — Classe `OPERA`**

```
V.NOPRESTITOSERESTAURO
∀o OPERA(o) → ¬∃ p, r, ip, ir, fp, d
  OPEPRE(o, p) ∧ OPERES(o, r) ∧ INIZIOPRE(p, ip) ∧ INIZIORES(r, ir)
  ∧ FINEPRE(p, fp) ∧ DATAORA(d) ∧ d > ir ∧ d > ip ∧ d < fp
  ∧ (∀fr FINERES(r, fr) → d < fr)

V.NOESPTEMPDURANTERESTAURO
∀o OPERA(o) → ¬∃ e, r, ie, ir, fe, d
  ESPOPE(o, e) ∧ OPERES(o, r) ∧ INIZIOESP(e, ie) ∧ INIZIORES(r, ir)
  ∧ FINEESP(e, fe) ∧ DATAORA(d) ∧ d > ir ∧ d > ie ∧ d < fe
  ∧ (∀fr FINERES(r, fr) → d < fr)

V.NOESPTEMPDURANTEPRESTITODATO
∀o OPERA(o) → ¬∃ p, e, ip, ie, fp, fe, d
  OPEPRE(o, p) ∧ PRESTITODATO(p) ∧ INIZIOPRE(ip, p) ∧ INIZIOESP(ie, e)
  ∧ FINEPRE(p, fp) ∧ FINEESP(fe, e) ∧ DATAORA(d) ∧ d > ip ∧ d > ie ∧ d < fe ∧ d < fp
```

I riquadri 5 e 8 sono in bianco.

Lo schema del vincolo di **disgiunzione temporale** («due periodi non si sovrappongono») è ripetuto
identico su prestiti, restauri ed esposizioni, sempre con l'istante testimone `d` e il quantificatore
universale sulla fine, per gestire il caso in cui la fine manchi.

### Specifiche dei tipi di dato e ulteriori vincoli esterni (pagina 11)

```
V.PRESTITO.SEPRESTABILE
∀o, p   OPEPRE(o, p) → PRESTABILE(o, TRUE)
```

Nessun tipo di dato definito: sono tutti tipi base del corso.

---

## Domanda 3 — Diagramma degli use-case (pagina 13)

```
## Use case

Attori: PATRIMONIO ARTISTICO, MANAGEMENT, BIGLIETTERIA

PATRIMONIO ARTISTICO — GESTIONE OPERE, GESTIONE RESTAURI
MANAGEMENT          — GESTIONE ESPOSIZIONI, GESTIONE PRESTITI, STATISTICHE OPERE
BIGLIETTERIA        — GESTIONE BIGLIETTI, STATISTICHE BIGLIETTI
```

Nessuna generalizzazione fra attori, nessun `«include»`/`«extend»`.

---

## Domanda 4 — Segnature delle operazioni di use-case (pagina 15)

```
GESTIONE OPERE:
- NEWOPERA(n: Stringa, a: Intero, p: Booleano, a: Autore) : Opera    [?] due argomenti chiamati «a»
- RIMUOVIOPERA(o: Opera) : Opera

GESTIONE RESTAURI:
- NEWRESTAURO(o: Opera, i: DataOra) : Restauro
- FINERESTAURO(r: Restauro, f: DataOra) : Restauro

GESTIONE PRESTITI:
- NEWPRESTITO(o: Opera, i: DataOra, f: DataOra, m: Museo) : Prestito

GESTIONE ESPOSIZIONI:
- NEWESPPERM(i: DataOra, s: Stringa) : EspPerm
- NEWESPTEMP(n: Stringa, i: DataOra, f: DataOra, s: Stringa, t: Tema) : EspTemp
- AGGIUNGIOPERA(e: Esposizione, o: Opera)

STATISTICHE OPERE:
- RESOCONTOCORRENTI(i: Intero, f: Intero) : (Corrente, Intero >= 0) [0..*]
- NORESTARTISTA(a: Autore, i: Data, f: Data) : Opera [0..*]
- OPERERESTVECCHIE() : (Opera, Data) [0..*]

GESTIONE BIGLIETTI:
- NEWBIGLFULL(d: Data) : BiglFull
- NEWBIGLPERM(d: Data) : BiglPerm
- NEWBIGLTEMP(d: Data, e: EspTemp) : BiglTemp

STATISTICHE BIGLIETTI:
- BIGLDATA(d: Data) : Intero >= 0 [3]
- BIGLMEDIA(i: Data, f: Data) : Reale >= 0
- ESPTEMPPOPOLARE(i: Data, f: Data) : EspTemp [0..*]
```

`BIGLDATA` ritorna una **tripla di conteggi** (`[3]`), non una relazione: un valore per tipo di
biglietto.

---

## Domanda 5 — Specifiche concettuali delle operazioni (pagine 17-18)

Sei operazioni, tutte di statistica.

```
BIGLDATA(d: Data) : Intero >= 0 [3]
- pre:
- post:
  BF = { b | BIGLFULL(b) ∧ DATABIGL(b, d) }
  BP = { b | BIGLPERM(b) ∧ DATABIGL(b, d) }
  BT = { b | BIGLTEMP(b) ∧ DATABIGL(b, d) }

  RESULT = (|BF|, |BP|, |BT|)
```

```
BIGLMEDIA(i: Data, f: Data) : Reale >= 0
- pre: i <= f
- post:
  B = { b | BIGLIETTO(b) ∧ ∃d DATABIGL(b, d) ∧ d >= i ∧ d <= f }

  sia g tale da soddisfare: GIORNO(f - i, g)

  RESULT = |B| / g
```

```
ESPTEMPPOPOLARE(i: Data, f: Data) : EspTemp [0..*]
- pre: i <= f
- post:
  E = { (e, n) | ESPTEMP(e) ∧ ∃ie, fe, di, df  INIZIOESP(e, ie) ∧ FINEESP(e, fe)
                 ∧ DATA(i, di) ∧ DATA(f, df) ∧
                 n = | { b | [BIGLFULL(b) ∨ BIGLTEMP(b) ∧ BIGLESP(b, e)]
                             ∧ ∃d DATABIGL(b, d) ∧ d >= i ∧ d >= ie ∧ d <= f ∧ d <= fe } | }

  RESULT = ARGMAX(n) con (e, n) ∈ E
```

```
RESOCONTOCORRENTI(i: Intero, f: Intero) : (Corrente, Intero >= 0) [0..*]
- pre: i <= f
- post:
  RESULT = { (c, a) | CORRENTE(c) ∧
             a = | { aut | AUTORE(aut) ∧ ∃o, an  OPERA(o) ∧ COROPE(c, o)
                           ∧ AUTOPE(aut, o) ∧ ANNOOPE(o, an) ∧ an >= i ∧ an <= f } | }
```

```
NORESTARTISTA(a: Autore, i: Data, f: Data) : Opera [0..*]
- pre: i <= f
- post:
  RESULT = { o | AUTOPE(a, o) ∧ ¬∃ r, ir, d, di  OPERES(o, r) ∧ INIZIORES(r, ir)
                 ∧ DATA(d) ∧ DATA(ir, di) ∧ d > i ∧ d > di ∧ d < f
                 ∧ (∀fr, df  FINERES(fr, r) ∧ DATA(df, fr) → d < df) }
```

```
OPERERESTVECCHIE() : (Opera, Data) [0..*]
- pre:
- post:
  OP = { (o, d) | ∃r OPERES(o, r) ∧ ¬∃f FINERES(r, f)
                  ∧ ∃ir INIZIORES(r, ir) ∧ ir < ADESSO
                  ∧ ∃e, i  ESPPERM(e, r) ∧ ESPOPE(e, o) ∧ INIZIOESP(e, i)   [?] ESPPERM(e, r)
                  ∧ i < ir ∧ DATA(d, ir) }

  OT = { (o, d) | ∃r OPERES(o, r) ∧ ¬∃f FINERES(r, f)
                  ∧ ∃ir INIZIORES(ir, r) ∧ ir < ADESSO
                  ∧ ∃e, fe  ESPTEMP(e) ∧ ESPOPE(e, o) ∧ FINEESP(e, fe)
                  ∧ ¬∃e', ie'  ESPOSIZIONE(e') ∧ INIZIOESP(e', ie') ∧ ie' >= fe ∧ ie' <= ir
                  ∧ ESPOPE(e', o) ∧ DATA(fe, d) }

  O = OT ∪ OP
  RESULT = ARGMIN(d) con (o, d) ∈ O
```

Due operazioni su sei si chiudono con un **`ARGMAX`/`ARGMIN` su un insieme di coppie** costruito
prima: è lo schema che il corso usa per «il più …».

---

## Domanda 6 — Ristrutturazione (pagine 19-21)

**DBMS da utilizzare: PostgreSQL.**

### Corrispondenza fra tipi di dato concettuali e domini

```sql
CREATE DOMAIN STRINGA AS VARCHAR NOT NULL;
CREATE DOMAIN REALGEZ AS REAL CHECK (VALUE >= 0);
CREATE DOMAIN INTGEZ AS INTEGER CHECK (VALUE >= 0);
```

### Diagramma UML ristrutturato (pagina 20)

Rispetto al concettuale:

- **tre gerarchie fuse verso l'alto**, ognuna con il proprio discriminante booleano:
  - `PRESTITO` assorbe `PRESTITODATO`/`PRESTITOPRESO` con `dato : Bool`;
  - `ESPOSIZIONE` assorbe `ESPPERM`/`ESPTEMP` con `temp : Bool`, e prende gli attributi della
    sottoclasse resi opzionali: `fineEsp : Timestamp [0..1]`, `nomeEsp : Stringa [0..1]`;
  - `BIGLIETTO` assorbe le tre sottoclassi con `temp : Bool [0..1]` — **un booleano opzionale per
    tre casi**: `NULL` = full, `false` = perm, `true` = temp;
- identificatori primari tecnici `id : SERIAL {id}` su `OPERA`, `PRESTITO`, `RESTAURO`,
  `ESPOSIZIONE`, `BIGLIETTO`, `MUSEO`;
- `DataOra` → `TIMESTAMP`, `Data` → `DATE`, `Intero` → `INTEGER`, `Booleano` → `BOOL`;
- `ESPTEMA` diventa `TEMA` 0..1 — `ESPOSIZIONE` 0..*, e `BIGLESP` diventa
  `ESPOSIZIONE` 0..1 — `BIGLIETTO` 0..*: le molteplicità si allentano perché il vincolo «solo
  le temporanee» non è più espresso dalla gerarchia.

### Breve descrizione delle scelte (pagina 21)

```
FUSIONE SU ESPOSIZIONE
FUSIONE SU BIGLIETTO
FUSIONE SU PRESTITO
```

### Vincoli esterni introdotti o modificati (pagina 21)

```
V.BIGLIETTO.ESPSOLOTEMPDURANTE
∀b, e   BIGLESP(b, e) → TEMP(b, TRUE) ∧ TEMP(e, TRUE)
  ∧ ∃i, f, d  INIZIOESP(i, e) ∧ FINEESP(f, e) ∧ DATABIGL(d, b) ∧ d >= i ∧ d <= f

V.ESPOSIZIONE.TEMPINFO
∀e ESPOSIZIONE(e) ∧ TEMP(e, TRUE) → ∃f, n  NOMEESP(e, n) ∧ FINEESP(e, f)

V.ESPOSIZIONE.FINEDOPOINIZIO
∀e, i, f   ESPOSIZIONE(e) ∧ INIZIOESP(e, i) ∧ FINEESP(e, f) → i < f
```

Il primo vincolo è il prezzo di due fusioni insieme: il legame biglietto-esposizione vale solo se
entrambi sono temporanei. Il secondo è il prezzo della fusione su `ESPOSIZIONE`: gli attributi resi
opzionali devono esserci quando `temp` è vero.

---

## Domanda 7 — Schema relazionale (pagine 23-25)

Quattordici relazioni; il riquadro 15 è vuoto. Chiave primaria in **grassetto**, `*` = può essere
NULL.

| # | Relazione | Da | Attributi (domini) | Vincoli | Accorpa |
|---|---|---|---|---|---|
| 1 | `OPERA` | classe | **id** (Serial) · nomeOpe (Stringa) · annoOpe (Integer) · prestabile (Bool) · autore (Stringa) · cat (Stringa) · tec* (Stringa) | `FK(autore) REF AUTORE(nomeAut)` · `FK(tec) REF TECNICA(nome)` · `FK(cat) REF CATEGORIA(nome)` | `AUTOPE`, `CATOPE`, `OPETEC` |
| 2 | `AUTORE` | classe | **nomeAut** (Stringa) · annoNas (Integer) · annoMor* (Integer) · citta (Stringa) · nazione (Stringa) | `FK(citta, nazione) REF CITTA(nome, nazione)` · `CHECK(annoNasc < annoMor)` | `AUTCIT` |
| 3 | `CITTA` | classe | **nome** (Stringa) · **nazione** (Stringa) | `FK(nazione) REF NAZIONE(nome)` | `CITNAZ` |
| 4 | `NAZIONE` | classe | **nome** (Stringa) | | |
| 5 | `CATEGORIA` | classe | **nome** (Stringa) | | |
| 6 | `TECNICA` | classe | **nome** (Stringa) | | |
| 7 | `CORRENTE` | classe | **nome** (Stringa) | | |
| 8 | `COROPE` | associazione | **opera** (Integer) · **corrente** (Stringa) | `FK(opera) REF OPERA(id)` · `FK(corrente) REF CORRENTE(nome)` | |
| 9 | `RESTAURO` | classe | **id** (Serial) · inizioRes (Timestamp) · fineRes* (Timestamp) · opera (Integer) | `FK(opera) REF OPERA(id)` · `CHECK(inizioRes < fineRes)` | `OPERES` |
| 10 | `PRESTITO` | classe | **id** (Serial) · inizioPre (Timestamp) · finePre (Timestamp) · dato (Bool) · opera (Integer) · museo (Integer) | `FK(opera) REF OPERA(id)` · `FK(museo) REF MUSEO(id)` · `CHECK(inizioPre < finePre)` | `OPEPRE`, `MUSPRE` |
| 11 | `MUSEO` | classe | **id** (Serial) · nome (Stringa) | | |
| 12 | `ESPOSIZIONE` | classe | **id** (Serial) · inizioEsp (Timestamp) · fineEsp* (Timestamp) · sezione (Stringa) · nomeEsp* (Stringa) · temp (Bool) · tema (Stringa) | `FK(tema) REF TEMA(nome)` · `CHECK(inizioEsp < fineEsp)` · `CHECK((temp IS NULL) = (fineEsp IS NULL) AND (temp IS NULL) = (nomeEsp IS NULL))` | `ESPTEMA` |
| 13 | `ESPOPE` | associazione | **esp** (Integer) · **opera** (Integer) | `FK(esp) REF ESPOSIZIONE(id)` · `FK(opera) REF OPERA(id)` | |
| 14 | `BIGLIETTO` | classe | **id** (Serial) · data (Date) · temp* (Bool) · espTemp* (Integer) | `FK(espTemp) REF ESPOSIZIONE(id)` · `CHECK((temp IS NULL) = (espTemp IS NULL))` | `BIGLESP` |

`CITTA` è l'unica relazione con **chiave composta** (`nome`, `nazione`): viene
dall'identificazione esterna del concettuale, e `AUTORE` la riferisce con una foreign key a due
attributi.

### Ulteriori vincoli esterni — progetto dei trigger (pagine 27-28, con seguito nelle minute 2 e 3)

```
T.AUTORE.OPERAINVITA
- INSERT OR UPDATE OPERA
ERROR = EXIST (SELECT * FROM AUTORE
               WHERE (ANNONAS > NEW.ANNOOPE OR ANNOMOR < NEW.ANNOOPE)
                 AND NOME = NEW.AUTORE)
IF ERROR: ERRORE
ELSE: COMMIT
```

```
T.PRESTITO.DISGIUNTI
- INSERT OR UPDATE PRESTITO
VALID = NOT EXIST (SELECT * FROM PRESTITO
                   WHERE ID <> NEW.ID AND OPERA = NEW.OPERA
                     AND (INIZIOPRE, FINEPRE) OVERLAPS (NEW.INIZIOPRE, NEW.FINEPRE))
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.RESTAURO.DISGIUNTI
- INSERT OR UPDATE RESTAURO
VALID = NOT EXIST (SELECT * FROM RESTAURO
                   WHERE ID <> NEW.ID AND OPERA = NEW.OPERA
                     AND (INIZIORES, FINERES) OVERLAPS (NEW.INIZIORES, NEW.FINERES))
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.ESPOSIZIONE.DOPOANNOOPERA
- INSERT OR UPDATE ESPOPE
VALID = EXIST (SELECT * FROM ESPOSIZIONE e, OPERA o
               WHERE o.ID = NEW.OPERA AND e.ID = NEW.ESP
                 AND EXTRACT(YEAR FROM e.INIZIOESP) >= o.ANNOOPE)
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.BIGLIETTO.ESPSOLOTEMPDURANTE
- INSERT OR UPDATE BIGLIETTO
ERROR = EXIST (SELECT * FROM ESPOSIZIONE
               WHERE NEW.ESP = ID AND (e.TEMP = FALSE
                 OR NEW.DATABIGL > e.FINEESP OR NEW.DATABIGL < e.INIZIOESP))
IF ERROR: ERRORE
ELSE: COMMIT
```

```
T.OPERA.NOPRESTITODURANTERESTAURO
- INSERT OR UPDATE PRESTITO OR RESTAURO
ERROR = EXIST (SELECT * FROM RESTAURO r, PRESTITO p
               WHERE r.OPERA = p.OPERA AND p.OPERA = NEW.OPERA
                 AND (r.INIZIORES, r.FINERES) OVERLAPS (p.INIZIOPRE, p.FINEPRE))
IF ERROR: ERRORE
ELSE: COMMIT
```

> **CONTINUA A MINUTE 2,3**

```
T.OPERA.NOESPTEMPDURANTERESTAURO                                        [minute 2]
- INSERT OR UPDATE ESPOPE OR RESTAURO
ERROR = EXIST (SELECT * FROM ESPOPE eo, PRESTITO p, ESPOSIZIONE e
               WHERE eo.OPERA = p.OPERA AND p.OPERA = NEW.OPERA
                 AND e.ID = eo.ESP AND e.TEMP = TRUE
                 AND (e.INIZIOESP, e.FINEESP) OVERLAPS (p.INIZIOPRE, p.FINEPRE))
IF ERROR: ERRORE
ELSE: COMMIT
```

`[?]` il nome dice «durante restauro» ma la query interroga `PRESTITO`: sembra un copia-e-incolla
non corretto dal trigger successivo.

```
T.OPERA.NOESPTEMPDURANTEPRESTITODATO                                    [minute 2]
- INSERT OR UPDATE ESPOPE OR PRESTITO
ERROR = EXIST (SELECT * FROM ESPOPE eo, PRESTITO p, ESPOSIZIONE e
               WHERE eo.OPERA = p.OPERA AND p.OPERA = NEW.OPERA
                 AND e.ID = eo.ESP AND e.TEMP = TRUE AND p.DATO = TRUE
                 AND (e.INIZIOESP, e.FINEESP) OVERLAPS (p.INIZIOPRE, p.FINEPRE))
IF ERROR: ERRORE
ELSE: COMMIT
```

```
T.PRESTITO.SEPRESTABILEDOPOANNOOPERA                                    [minute 2]
- INSERT OR UPDATE PRESTITO
VALID = EXIST (SELECT * FROM OPERA
               WHERE ID = NEW.OPERA AND PRESTABILE = TRUE
                 AND ANNOOPE <= EXTRACT(YEAR FROM NEW.INIZIOPRE))
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.RESTAURO.DOPOANNOOPERA                                                [minute 2]
- INSERT OR UPDATE PRESTITO                    [?] dovrebbe essere RESTAURO
VALID = EXISTS (SELECT * FROM OPERA
                WHERE ID = NEW.OPERA
                  AND ANNOOPE <= EXTRACT(YEAR FROM NEW.INIZIORES))
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.ESPOSIZIONE.DISGIUNTE                                                 [minute 3]
- INSERT OR UPDATE ESPOPE
VALID = NOT EXIST (WITH ESP AS (SELECT * FROM ESPOSIZIONE WHERE ID = NEW.ESP)
                   SELECT * FROM ESPOPE eo, ESPOSIZIONE e, ESP
                   WHERE eo.ESP = e.ID AND e.ID <> NEW.ESP
                     AND eo.OPERA = NEW.OPERA
                     AND (e.INIZIOESP, e.FINEESP) OVERLAPS (ESP.INIZIOESP, ESP.FINEESP))
IF VALID: COMMIT
ELSE: ERRORE
```

Dieci trigger in tutto, tutti con lo stesso schema `VALID`/`ERROR` + `EXIST(...)` +
`IF … COMMIT / ELSE ERRORE`, e la sovrapposizione sempre resa con `OVERLAPS`.

---

## Domanda 8 — Specifiche realizzative (pagine 29-30, con seguito nella minuta 1)

```
BIGLDATA(d: DATE) : INTGEZ [3]

R = WITH BF AS (SELECT * FROM BIGLIETTO WHERE TEMP IS NULL),
         BP AS (SELECT * FROM BIGLIETTO WHERE TEMP = FALSE),
         BT AS (SELECT * FROM BIGLIETTO WHERE TEMP = TRUE)
    SELECT COUNT(DISTINCT BF.ID), COUNT(DISTINCT BP.ID), COUNT(DISTINCT BT.ID)
    FROM BF, BP, BT
RETURN R
```

`[?]` manca il filtro su `d` nelle tre CTE, e il prodotto cartesiano `FROM BF, BP, BT` con i
`COUNT(DISTINCT …)` è quello che salva il conteggio dalla moltiplicazione delle righe.

```
BIGLMEDIA(i: DATE, f: DATE) : REALGEZ

ERROR = i > f
R = SELECT COUNT(ID) / i - f FROM BIGLIETTO          [?] i - f, non f - i
    WHERE DATABIGL >= i AND DATABIGL <= f
RETURN R
```

```
ESPTEMPPOPOLARE(i: DATE, f: DATE) : INTEGER [0..*]

ERROR = i > f
R = WITH E AS (SELECT e.ID, COUNT(b.ID) c FROM ESPOSIZIONE e, BIGLIETTO b
               WHERE b.DATABIGL >= i AND b.DATABIGL <= f
                 AND b.DATABIGL >= e.INIZIOESP AND b.DATABIGL < e.FINEESP
                 AND (b.TEMP IS NULL OR b.TEMP = TRUE AND b.ESP = e.ID)
               GROUP BY e.ID)
    SELECT ID FROM E
    WHERE c = (SELECT MAX(c) FROM E)
RETURN R
```

```
RESOCONTOCORRENTI(i: INTEGER, f: INTEGER) : (STRINGA, INTGEZ) [0..*]

ERROR = i > f
R = SELECT co.CORRENTE, COUNT(DISTINCT o.AUTORE) FROM COROPE co, OPERA o
    WHERE co.OPERA = o.ID AND o.ANNOOPE >= i AND o.ANNOOPE <= f
    GROUP BY co.CORRENTE
RETURN R
```

```
NORESTARTISTA(a: STRINGA, i: DATE, f: DATE) : INTEGER [0..*]

ERROR = i > f
R = (SELECT ID FROM OPERA WHERE AUTORE = a)
    EXCEPT
    (SELECT o.ID FROM OPERA o, RESTAURO r
     WHERE o.AUTORE = a AND r.OPERA = o.ID
       AND (i, f) OVERLAPS (EXTRACT(DATE FROM r.INIZIORES), EXTRACT(DATE FROM r.FINERES)))
RETURN R
```

> **CONTINUA MINUTE 1**

```
OPERERESTVECCHIE() : (INTEGER, DATE) [0..*]                             [minuta 1]

R = WITH O AS ((SELECT o.ID, EXTRACT(DATE FROM r.INIZIORES) d
                FROM OPERA o, RESTAURO r, ESPOPE eo, ESPOSIZIONE e
                WHERE r.OPERA = o.ID AND eo.OPERA = o.ID AND eo.ESP = e.ID
                  AND r.INIZIORES < NOW() AND r.FINERES IS NULL
                  AND e.INIZIOESP < r.INIZIORES AND e.TEMP = FALSE)
               UNION
               (SELECT o.ID, EXTRACT(DATE FROM e.FINEESP) d
                FROM OPERA o, RESTAURO r, ESPOPE eo, ESPOSIZIONE e
                WHERE r.OPERA = o.ID AND eo.OPERA = o.ID AND eo.ESP = e.ID
                  AND r.INIZIORES < NOW() AND r.FINERES IS NULL
                  AND e.INIZIOESP < r.INIZIORES AND e.TEMP = TRUE
                  AND e.FINEESP = (SELECT MAX(e.FINEESP) FROM ESPOSIZIONE e, ESPOPE eo
                                   WHERE eo.ESP = e.ID AND eo.OPERA = o.ID)))
    SELECT * FROM O
    WHERE d = (SELECT MIN(d) FROM O)
RETURN R
```

L'unione delle due CTE ricalca esattamente `OP ∪ OT` della Domanda 5, e il `MIN` finale è
l'`ARGMIN`. Non è dichiarato, per nessuna delle sei operazioni, se vada implementata nel DBMS o nel
back-end: la Domanda 8 lo chiede e la risposta lo omette.
