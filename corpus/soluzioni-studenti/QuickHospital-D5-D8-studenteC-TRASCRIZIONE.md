# QuickHospital — svolgimento di studente-C, Domande 5-8 (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-C/QuickHospital.pdf`, 39 pagine, modulo
> **`Versione 2021-10-13`** (notazione **ER**), compilato a mano. Trascritte le sole **Domande 5,
> 6, 7 e 8**. Il documento è il PDF; questa è una copia a macchina e può contenere errori di
> lettura, marcati `[?]`.
>
> **Perché questa vale più delle altre.** QuickHospital è l'**unico** progetto di cui esiste la
> soluzione **ufficiale** del docente fino allo schema relazionale
> (`soluzioni-ufficiali/QuickHospital.md`). Qui c'è la stessa cosa fatta da uno studente: è
> l'unico punto del corpus in cui si può leggere **la stessa Domanda 7 e la stessa Domanda 8 in
> due versioni**, una delle quali è quella giusta per definizione.
>
> **Non è una soluzione ufficiale e nessuno l'ha corretta.**

---

## Le due convenzioni di metodo che questo svolgimento porta

1. **Ogni vincolo ristrutturato è marcato in margine con la sua strategia di realizzazione**, e
   c'è pure la legenda, scritta a penna blu: *«NOTA: indica che sia stato implementato senza
   trigger (es. come v. di ennupla)»*. Una **X** = realizzato dichiarativamente e lo si ritrova
   come `ENN:`/`DOM:` nella Domanda 7; una **T** = serve un trigger e lo si ritrova fra gli
   ulteriori vincoli esterni. È il modo più rapido di dimostrare al correttore che **nessun
   vincolo dell'analisi è stato perso**, che è il controllo numero uno di `correzione.md`.
2. **`sorted(S, criterio)` con il criterio scritto come operazione a parte.** La Domanda 5 chiede
   il percorso di visite *ordinato*: lui definisce `sortByPianoSettore(s, s'): Boolean` come
   operazione di confronto e poi scrive `RESULT = sorted(S, sortByPianoSettore)`. È esattamente
   la forma che `fol.md` prescrive per i risultati ordinati, con il criterio formalizzato e non
   descritto a parole.

---

## Domanda 5 — Specifiche concettuali delle operazioni (pagine 19-20)

```
CALCOLAMEDIDONEI(s: Specializ) : Medico (0, N)
- pre:
- post:
  M_p = { m | SPECPRIMMED(m, s) }
  M_s = { m | SPECMED(m, s) }

  (M_p ≠ ∅ → RESULT = M_p) ∧ (M_p = ∅ → RESULT = M_s)
```

Il ripiego è scritto **come due implicazioni sul risultato**, non come un `if` procedurale: è la
stessa semantica dell'ufficiale (prima i medici che hanno `s` come specializzazione primaria, e
solo se non ce ne sono tutti quelli che ce l'hanno fra le altre), ma senza uscire dalla logica.

```
CALCOLAPERCORSO(m: Medico) : (s: Stanza, n: Intero > 0) (0, N)
- pre:
- post:
  S = { s | STANZA(s) ∧ (∃l, r  STLETTO(l, s) ∧ LETTORIC(r, l) ∧ MEDRIC(r, m)
            ∧ ¬RICOVEROTERM(r)) }

  RESULT = sorted(S, sortByPianoSettore)
```

```
SORTBYPIANOSETTORE(s: Stanza, s': Stanza) : Boolean
- pre:
- post:
  siano p, p', st, st' tali che
    PIANO(s, p) ∧ PIANO(s', p') ∧ SETTORE(s, st) ∧ SETTORE(s', st')

  ((p < p' ∨ (p = p' ∧ st < st')) → RESULT = TRUE)
  ∧
  ((p > p' ∨ (p = p' ∧ st > st')) → RESULT = FALSE)
```

> Il confronto è fra **i numeri** di piano e settore, non fra gli oggetti. È il punto in cui è
> facile scivolare: confrontare `Piano` con `<` non vuol dire niente finché non si prende il suo
> numero.

```
NUMPOSTIDISPONIBILI(s: Stanza, d: DataOra) : Intero >= 0
- pre:
- post:
  L = { l | STLETTO(l, s) ∧ ¬(∃r, i  RICOVERO(r) ∧ RICLETTO(l, r)
            ∧ ¬RICOVEROTERM(r) ∧ INIZIO(r, i) ∧ i <= d) }

  RESULT = |L|
```

```
AMMETTIPAZIENTE(p: Paziente, m: Medico, d: DataOra) : Ricovero
- pre: ∃s  STANZA(s) ∧ NUMPOSTIDISPONIBILI(s, d) > 0
- post:
  · sia l tale che
      LETTO(l) ∧ (∃s STANZA(s) ∧ STLETTO(l, s) ∧ NUMPOSTIDISPONIBILI(s, d) > 0)
  · viene aggiunto l'elemento α
  · vengono aggiunti i predicati:
      RICOVERO(α)
      RICLETTO(l, α)
      PAZPREST(α, p)
      MEDPREST(α, m)
      INIZIO(α, d)
```

L'operazione con **side effect** si scrive elencando l'oggetto nuovo (`α`) e **i predicati che
diventano veri**: è la forma del corso, e la precondizione parla del parametro (`NUMPOSTI… > 0`),
non di un esistenziale generico.

---

## Domanda 6 — Ristrutturazione (pagine 21-24)

**DBMS: PostgreSQL.**

```sql
CREATE DOMAIN INT_GZ  AS INTEGER CHECK (VALUE > 0);
CREATE DOMAIN INT_GEZ AS INTEGER CHECK (VALUE >= 0);
CREATE DOMAIN STR     AS VARCHAR(200);
CREATE DOMAIN CF      AS STR CHECK (isValidCF(VALUE));
CREATE DOMAIN EMAIL   AS STR CHECK (isValidEmail(VALUE));
CREATE TYPE INDIRIZZO AS (via STR, civico INT_GZ, cap INT_GZ, città STR, nazione STR);
CREATE TYPE TELEFONO  AS (pre STR, suff STR);
CREATE TYPE TIPO_PREST AS ENUM ('RIC', 'EST');
```

Da notare: i tipi con formato (`CF`, `EMAIL`) diventano **domini con un `CHECK` che richiama una
funzione**, non espressioni regolari scritte a mano; `INDIRIZZO` e `TELEFONO` diventano **tipi
composti**; la gerarchia delle prestazioni diventa un `ENUM` di due valori.

### Il diagramma ER ristrutturato (pagina 22), in parole

`PERSONA` (cf identificatore, nome, cognome, nascita) con le due sottoclassi sciolte in
`PAZIENTE` (email [0..1], indirizzo) e `MEDICO` (specPrim), legate da `PAZPERS` (0,1)-(1,1) e
`MEDPERS` (0,1)-(1,1); `TELEFONO` (id, tel) legato a `PAZIENTE` da `TELPAZ` (1,1)-(0,N);
`SPECIALIZ` (nome) con `SPECMED` (1,N)-(0,N) e `SPECPRIMMED` (1,1)-(0,N); `PRESTAZIONE` (id,
inizio, fine [0..1], tipo, desc [0..1]) con `PAZPREST` (1,1)-(0,N), `MEDPREST` (1,1)-(0,N),
`LETRIC` (0,1)-(0,N) verso `LETTO`, `SPECPREST` (0,1)-(0,N) verso `SPECIALIZ`; `LETTO` (id) e
`STANZA` (id, num, piano, settore, maxLetti `[1,8]`) legati da `STLETTO` (1,1)-(1,N).

**La catena `Padiglione→Piano→Settore→Stanza` dell'ufficiale qui non c'è**: piano e settore sono
attributi di `STANZA`. È la divergenza più grossa rispetto alla soluzione del docente, ed è la
stessa che il primo test in cieco della skill aveva commesso — con la differenza che qui la
perdita è dichiarata dal fatto che `STANZA` prende un identificatore surrogato.

### Vincoli esterni introdotti o modificati (pagine 23-24)

```
T  [V.PERSONA.COMPLETEZZA]
   ∀x PERSONA(x) → (∃p PAZPERS(x, p)) ∨ (∃m MEDPERS(x, m))

X  [V.PERSONA.NOSUOMEDICO]
   ∀x, p, pr, m   PERSONA(x) ∧ PAZPERS(x, p) ∧ PAZPREST(p, pr) ∧ MEDPREST(m, pr)
     → ¬MEDPERS(x, m)

X  [V.SPECPRIMMED.ISA]
   ∀m, s   MEDICO(m) ∧ SPECPRIMMED(m, s) → SPECMED(m, s)

X  [V.PRESTAZIONE.RICOVERO]
   ∀p PRESTAZIONE(p) → (∃l LETRIC(p, l) ⟺ TIPO(p, 'RIC'))

X  [V.PRESTAZIONE.ESTERNA]
   ∀p PRESTAZIONE(p) → (∃s, d  SPECPREST(p, s) ∧ DESC(p, d) ⟺ TIPO(p, 'RIC'))   [?] 'EST'

X  [V.PRESTAZIONE.FINE]
   ∀p PRESTAZIONE(p) → (∃f FINE(p, f) → TIPO(p, 'RIC'))

X  [V.RICOVEROTERM.FINE]
   ∀p, i   PRESTAZIONE(p) ∧ INIZIO(p, i) → (∀f FINE(p, f) → i < f)

   [V.SPECIALIZ.CICLOMEDICO]
   ∀s, m, p   SPECIALIZ(s) ∧ PRESTAZIONE(p) ∧ TIPO(p, 'EST') ∧ SPECPREST(p, s)
     ∧ MEDPREST(p, m) → SPECMED(m, s)
```

Solo il primo porta la **T**: la completezza della gerarchia di `PERSONA` è l'unica cosa che qui
non si esprime con un vincolo di ennupla, e infatti diventa il secondo trigger della Domanda 7.

---

## Domanda 7 — Schema relazionale (pagine 25-26)

Nove relazioni. Chiave primaria in **grassetto**, `*` = ammette NULL.

| # | Relazione | Da | Attributi (domini) | Vincoli | Accorpa |
|---|---|---|---|---|---|
| 1 | `TELEFONO` | entità | **id** (Integer) · tel (Telefono) · paz (CF) | `SERIAL: id` · `FK(paz) REF PAZIENTE(pers)` | `TELPAZ` |
| 2 | `PERSONA` | entità | **cf** (CodFis) · nome (Str) · cognome (Str) · nascita (Timestamp) | | |
| 3 | `PAZIENTE` | entità | **pers** (CF) · email* (Email) · indirizzo (Indirizzo) | `FK(pers) REF PERSONA(cf)` | `PAZPERS` |
| 4 | `MEDICO` | entità | **pers** (CF) · specPrim (Str) | `FK(pers) REF PERSONA(cf)` · `FK(specPrim) REF SPECIALIZ(nome)` · `FK(pers, specPrim) REF SPECMED(med, spec)` | `MEDPERS`, `SPECPRIMMED` |
| 5 | `SPECMED` | relationship | **med** (CF) · **spec** (Str) | `FK(med) REF MEDICO(pers)` · `FK(spec) REF SPECIALIZ(nome)` | |
| 6 | `SPECIALIZ` | entità | **nome** (Str) | | |
| 7 | `PRESTAZIONE` | entità | **id** (Integer) · inizio (Timestamp) · fine* (Timestamp) · paz (CF) · med (CF) · tipo (Tipo_Prest) · desc* (Str) · letto* (Integer) · spec* (Str) | `SERIAL: id` · `FK(paz) REF PAZIENTE(pers)` · `FK(med) REF MEDICO(pers)` · `FK(letto) REF LETTO(id)` · `FK(spec) REF SPECIALIZ(nome)` · `ENN: tipo = 'EST' ⟺ spec ≠ NULL` · `ENN: fine ≠ NULL → inizio < fine` · `ENN: desc ≠ NULL → tipo = 'EST'` · `ENN: paz ≠ med` · `ENN: tipo = 'RIC' ⟺ letto ≠ NULL` · `ENN: fine ≠ NULL → tipo = 'RIC'` | `PAZPREST`, `MEDPREST`, `LETRIC`, `SPECPREST` |
| 8 | `LETTO` | entità | **id** (Integer) · stanza (Integer) | `SERIAL: id` · `FK(stanza) REF STANZA(id)` | `STLETTO` |
| 9 | `STANZA` | entità | **id** (Integer) · num (Int_GZ) · piano (Int_GZ) · settore (Int_GZ) · maxLetti (Integer) | `SERIAL: id` · `INC: (stanza) ⊆ LETTO(stanza)` · `DOMINIO: maxLetti >= 1 ∧ maxLetti <= 8` | |

**Il confronto con l'ufficiale, che è il motivo per cui questa trascrizione esiste:**

| | soluzione ufficiale | studente-C |
|---|---|---|
| contenimento | quattro relazioni `Padiglione`, `Piano`, `Settore`, `Stanza`, con chiavi che si propagano a cascata (`Letto(n, stanza, sett, piano, padiglione)`) | una sola `STANZA` con `piano` e `settore` come attributi, e `LETTO(id, stanza)` |
| identificatori | naturali e composti, `ON UPDATE CASCADE` sulle catene | surrogati `SERIAL` quasi ovunque |
| telefono del paziente | relazione a chiave composta `telefono(paziente, valtel)` | entità `TELEFONO` con `id` surrogato |
| gerarchia delle prestazioni | relazioni separate più vincoli di inclusione e un trigger per `disjoint/complete` | fusa in `PRESTAZIONE` con `tipo` e sei vincoli di ennupla |
| vincoli sui NULL | dichiarati a parole nella specifica | **sei `ENN:` scritti come equivalenze**, che è la forma che regge |

Nessuna delle due è «la» risposta: l'ufficiale conserva l'identificazione, lo studente conserva la
semplicità. Ma la colonna di destra mostra una cosa che vale sempre: **quando una gerarchia si
fonde, i vincoli che tengono insieme gli attributi opzionali si scrivono come equivalenze**, una
per attributo, e sono la prova che la fusione non ha perso informazione.

### Ulteriori vincoli esterni — progetto dei trigger (pagina 29)

```
T.STANZA.MAXLETTI
- inserimento in LETTO, pre-operazione
Q = (SELECT COUNT(l.id) AS c, s.maxLetti AS m
     FROM Letti l, Stanza s
     WHERE l.stanza = NEW.stanza AND l.stanza = s.id)
IF Q.c < Q.m COMMIT ELSE GENERA ERRORE
```

```
T.PERSONA.COMPLETEZZA
- inserimento in PERSONA, pre-operazione
isValid = EXISTS (SELECT * FROM Paziente p, Medico m
                  WHERE p.pers = NEW.cf OR m.pers = NEW.cf)
IF isValid COMMIT ELSE GENERA ERRORE
```

> Il secondo trigger **non può funzionare così**: al momento dell'inserimento della persona non
> esiste ancora né il paziente né il medico, e il prodotto cartesiano fra le due tabelle rende la
> `EXISTS` falsa anche quando una delle due ha la riga giusta. È il vincolo che vuole un
> **constraint trigger differito** a fine transazione — lo stesso caso su cui la skill ha appena
> preso una correzione. Vale come esempio di errore da riconoscere, non da imitare.

---

## Domanda 8 — Specifiche realizzative (pagina 31)

```
CALCOLAMEDIDONEI(s: Str) : Insieme(<m: CF>)

Q = (SELECT m.id FROM Medici m WHERE m.specPrim = :s)
IF Q ≠ NULL
    RETURN Q
ELSE
    Q' = (SELECT sp.med AS m FROM SpecMed sp WHERE sp.spec = :s)
    RETURN Q'
```

Il ripiego della Domanda 5 diventa **due query e un `IF`**, non una `LEFT OUTER JOIN`: è la
traduzione più diretta delle due implicazioni della postcondizione, e non ha il ramo morto che la
join interna produrrebbe.

```
CALCOLAPERCORSO(m: CF) : Lista(<s: Integer>)

Q = (SELECT s.id
     FROM Stanza s, Letto l, Prestazione p
     WHERE s.id = l.stanza AND p.tipo = 'RIC'
       AND p.letto = l.id AND p.med = :m
     ORDER BY s.piano, s.settore)
RETURN Q
```

L'`ORDER BY s.piano, s.settore` è la realizzazione dell'operazione di confronto
`sortByPianoSettore` della Domanda 5: **l'ordinamento formalizzato in logica diventa una clausola
`ORDER BY`**, ed è il modo di far vedere che le due domande parlano della stessa cosa.
