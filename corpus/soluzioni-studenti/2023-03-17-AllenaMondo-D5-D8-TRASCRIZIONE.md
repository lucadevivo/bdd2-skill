# AllenaMondo, prova del 17 marzo 2023 — svolgimento di studente-C, Domande 5-8 (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-C/AllenaMondo.pdf`, 38 pagine, modulo
> **`Versione 2021-10-13`** — quello **in notazione ER** — compilato a mano. Trascritte le sole
> **Domande 5, 6, 7 e 8**, che della notazione non risentono: la Domanda 2 chiede il diagramma ER
> e resta fuori. Il documento è il PDF; questa è una copia a macchina e può contenere errori di
> lettura, marcati `[?]`.
>
> **Perché questa trascrizione esiste.** Delle dodici soluzioni ufficiali del docente una sola
> arriva allo schema relazionale (QuickHospital), e la usiamo già come metro altrove: sulle
> Domande 6-8 il corpus era quasi senza metro esterno. Questa prova, completa fino alla Domanda 8,
> serve a vedere **che forma ha una risposta vera** su ristrutturazione, schema, trigger e
> specifiche realizzative.
>
> **Non è una soluzione ufficiale e nessuno l'ha corretta.**
> Traccia: `tracce-esame/BD2_2023-03-17_AllenaMondo.pdf`.

---

## Che cosa si impara sul metodo, prima ancora che sul contenuto

1. **Ogni vincolo ristrutturato porta in margine la sua strategia.** Nella Domanda 6 lo studente
   segna a penna blu, accanto a ciascun vincolo, una **X** (realizzabile in modo dichiarativo, e
   infatti quel vincolo ricompare come `ENN:` nello schema) o una **T** (serve un trigger, e
   infatti ricompare fra gli «ulteriori vincoli esterni»). È il modo più economico di dimostrare
   che nessun vincolo è stato perso: la Domanda 7 si limita a raccogliere le due liste.
2. **Una relazione che non entra in un riquadro si spezza in `9a` e `9b`.** `ATTIVITA'` occupa due
   riquadri numerati a mano, con gli attributi divisi e i vincoli di ennupla nel secondo. Il
   modulo non lo prevede: se lo spazio non basta, si numera così invece di scrivere più fitto.
3. **Le operazioni della Domanda 8 dichiarano dove vivono**: il prefisso `DB.` davanti al nome
   (`DB.calcolaKmAttività`) dice che l'operazione è realizzata **nel DBMS**, ed è quello che
   permette alle altre di richiamarla dentro una `SELECT`.
4. **I parametri si scrivono `:nome`**, come le variabili host dell'SQL immerso.
5. **La pagina delle minute serve a rifare meglio, non solo a continuare.** `RESOCONTOALLENAMENTI`
   è scritta due volte: nel corpo con una nota a margine *«è inefficiente (versione efficiente a
   MINUTA 33)»*, e nelle minute in versione efficiente. Dichiarare l'inefficienza e mostrare la
   versione buona vale più che consegnare solo la seconda.

---

## Domanda 5 — Specifiche concettuali delle operazioni (pagine 19-20)

```
CALCOLAKMATTIVITÀ(a: AttConPercorso) : Reale >= 0
- pre:
- post:
  P = { (p, p', d) | POSIZIONE(p) ∧ POSIZIONE(p') ∧ POSPERC(a, p) ∧ POSPERC(a, p') ∧ p ≠ p'
        ∧ (∃lt, lt', lg, lg', i, i'  LAT(p, lt) ∧ LAT(p', lt') ∧ LONG(p, lg) ∧ LONG(p', lg')
           ∧ DISTANZA(lt, lg, lt', lg') = d ∧ ISTANTE(p, i) ∧ ISTANTE(p', i')
           ∧ (¬∃p'', i''  POSPERC(a, p'') ∧ ISTANTE(p'', i'') ∧ i < i'' ∧ i'' < i')) }

  RESULT = Σ_{(p,p',d) ∈ P} d
```

Il predicato `DISTANZA` è una funzione esterna sui tipi di dato (due coppie di coordinate), e
l'insieme `P` è quello delle **coppie consecutive**: la condizione «non esiste una posizione in
mezzo» è ciò che rende la somma una polilinea e non un prodotto cartesiano.

```
CALCOLAKMSPORT(u: SportNo, s: Sport, i: DataOra, f: DataOra) : Reale >= 0
- pre: i < f
- post:
  A = { (a, k) | ATTCONPERCORSO(a) ∧ CALCOLAKMATTIVITÀ(a) = k ∧ SPORTATT(a, s)
        ∧ SVOLGE(u, a) ∧ (∃i' INIZIO(a, i') ∧ i <= i' ∧ (∃f' FINE(a, f') → f' <= f)) }

  RESULT = Σ_{(a,k) ∈ A} k
```

```
CALCOLATEMPOSPORT(u: SportNo, s: Sport, i: DataOra, f: DataOra) : Intero >= 0
- pre: i < f
- post:
  A = { (a, t) | ATTIVITÀ(a) ∧ SVOLGE(u, a) ∧ SPORTATT(a, s)
        ∧ (∃i INIZIO(a, i) ∧ (∃f' FINE(a, f') → t = f' - i ∧ f' <= f)
           ∧ (¬∃f'' FINE(a, f'') → t = ADESSO - i) ∧ i <= i') }

  RESULT = Σ_{(a,t) ∈ A} t
```

L'attività **ancora in corso** contribuisce con `ADESSO - inizio`: il caso «senza fine» non si
esclude, si calcola.

```
RESOCONTOALLENAMENTI(u: SportNo, i: DataOra, f: DataOra) : (s: Sport, t: Intero >= 0, k: Reale >= 0)
- pre: i < f
- post:
  S = { (s, t, k) | SPORT(s) ∧ CALCOLAKMSPORT(u, i, f) = k ∧ CALCOLATEMPOSPORT(u, i, f) = t }

  RESULT = S
```

```
SPORTPIÙPRATICATOAMICI(u: Sportivo, i: DataOra, f: DataOra) : Sport [0..*]
- pre: i < f
- post:
  A = { a | UTENTE(a) ∧ (AMICO(u, a) ∨ AMICO(a, u)) }

  S = { (s, t) | SPORT(s) ∧ t = Σ_{a ∈ A} CALCOLATEMPOSPORT(a, i, f) }

  S_max = ARGMAX(t) con (s, t) ∈ S

  RESULT = { s' | ∃t' (s', t') ∈ S_max }
```

L'amicizia è simmetrica e il diagramma la tiene con **due ruoli** (`S1`, `S2`) su una sola
associazione: la disgiunzione `AMICO(u,a) ∨ AMICO(a,u)` è il prezzo, e va scritta.

---

## Domanda 6 — Ristrutturazione (pagine 21-24)

**DBMS: PostgreSQL.**

```sql
CREATE DOMAIN INT_GZ  AS INTEGER CHECK (VALUE > 0);
CREATE DOMAIN INT_GEZ AS INTEGER CHECK (VALUE >= 0);
CREATE DOMAIN REAL_GEZ AS REAL   CHECK (VALUE >= 0);
CREATE DOMAIN INT_1_5 AS INTEGER CHECK (VALUE >= 1 AND VALUE <= 5);
CREATE DOMAIN STR     AS VARCHAR(200);
CREATE TYPE SEX   AS ENUM ('M', 'F');
CREATE TYPE WIN_T AS ENUM ('più all.', 'più km');
```

### Il diagramma ER ristrutturato (pagina 22), in parole

Entità e attributi, come si leggono dal disegno:

- `POSIZIONE` — `id` (identificatore), `lat`, `long`, `istante`
- `SPORTIVO` — `nickname` (identificatore), `nome`, `cognome`, `nascita`, `altezza [0..1]`,
  `peso [0..1]`
- `ATTIVITÀ` — `id`, `nome`, `inizio`, `commento [0..1]`, `nomePerc [0..1]`, `pubblico: bool`,
  `conPercorso: bool`, `fine [0..1]`, `diff [0..1]`
- `SPORT` — `nome` (identificatore), `desc`
- `SQUADRA` — `id`, `nome`
- `SFIDA` — `id`, `nome`, `inizio`, `fine`, `durataSecAll`, `aSquadre`, `maxMembri [0..1]`,
  `criterioVincita`

Relationship, con le cardinalità scritte: `POSPERC` (`POSIZIONE` (1,1) — `ATTIVITÀ` (0,N)),
`SVOLGE` ((0,N) — (1,1)), `SPATT` (`ATTIVITÀ` (1,1) — `SPORT` (0,N)), `AMICO` (`SPORTIVO` (0,N)
con sé stesso, ruoli `S1`/`S2`), `MEMBRO` (`SPORTIVO` (0,N) — `SQUADRA` (1,N)), `CAPO`
(`SPORTIVO` (0,N) — `SQUADRA` (1,1)), `PARTECIPA` (`SPORTIVO` (0,N) — `SFIDA` (0,N)), `CREA`
(`SPORTIVO` (0,N) — `SFIDA` (1,1)), `SQSFIDA` (`SQUADRA` (1,1) — `SFIDA` (0,N)), `SASFIDA`
(`SPORT` (0,N) — `SFIDA` (1,N)).

Le due gerarchie del concettuale (`AttConPercorso`, `SfidaASquadre`) sono **fuse** nei booleani
`conPercorso` e `aSquadre`, e gli attributi delle sottoclassi diventano opzionali. È da lì che
nascono quasi tutti i vincoli qui sotto.

### Vincoli esterni introdotti o modificati (pagine 23-24)

Ogni riga porta in margine la strategia: **X** = dichiarativo, **T** = trigger.

```
X  [V.ATTIVITÀ.DIFF]
   ∀a ATTIVITÀ(a) → (∃d DIFF(a, d) → ∃f FINE(a, f))

X  [V.ATTIVITÀ.NOME&COMMENTO]
   ∀a ATTIVITÀ(a) → (∃n, c  NOME(a, n) ∧ COMMENTO(a, c) ⟺ PUBBLICO(a, TRUE))

X  [V.ATTIVITÀ.PUBBLICO]
   ∀a ATTIVITÀ(a) → (PUBBLICO(a, TRUE) → CONPERCORSO(a, TRUE))

T  [V.ATTIVITÀ.POSIZIONE]
   ∀a ATTIVITÀ(a) → (∃p POSPERC(a, p) → CONPERCORSO(a, TRUE))

X  [V.SFIDA.MAX_PART]
   ∀s SFIDA(s) → (∃m MAXMEMBRI(s, m) ⟺ ASQUADRE(s, TRUE))

T  [V.SFIDA.PARTECIPA]
   ∀s SFIDA(s) → (∃u PARTECIPA(u, s) → ASQUADRE(s, FALSE))

T  [V.SFIDA.SQSQUADRA]
   ∀s SFIDA(s) → (∃sq SQSFIDA(s, sq) → ASQUADRE(s, TRUE))

X  [V.CAPO.ISA]
   ∀u, s   SPORTIVO(u) ∧ CAPO(u, s) → MEMBRO(u, s)

T  [V.ASQUADRE.MAXMEMBRI]
   ∀s, sq, m   SFIDA(s) ∧ ASQUADRE(s, TRUE) ∧ SQSFIDA(s, sq) ∧ MAXMEMBRI(s, m)
     → | { u | UTENTE(u) ∧ MEMBRO(u, sq) } | <= m
```

---

## Domanda 7 — Schema relazionale (pagine 25-30)

Undici relazioni. Chiave primaria in **grassetto**, `*` = ammette NULL.

| # | Relazione | Da | Attributi (domini) | Vincoli | Accorpa |
|---|---|---|---|---|---|
| 1 | `POSIZIONE` | entità | **id** (Integer) · lat (Real_GEZ) · long (Real_GEZ) · istante (Timestamp) · att (Integer) | `SERIAL: id` · `FK(att) REF ATTIVITÀ(id)` · `CHIAVE: (istante, att)` | `POSPERC` |
| 2 | `SPORTIVO` | entità | **nickname** (Str) · nome (Str) · cognome (Str) · nascita (Date) · altezza* (Real_GEZ) · peso* (Real_GEZ) | | |
| 3 | `AMICO` | relationship | **sportivo1** (Str) · **sportivo2** (Str) | `FK(sportivo1) REF SPORTIVO(nickname)` · `FK(sportivo2) REF SPORTIVO(nickname)` · `ENN: sportivo1 ≠ sportivo2` | |
| 4 | `SQUADRA` | entità | **id** (Integer) · nome (Str) · capo (Str) · sfida (Integer) | `FK(capo) REF SPORTIVO(nickname)` · `FK(sfida) REF SFIDA(id)` · `CHIAVE: (nome, sfida)` · `INC: (id) ⊆ MEMBRO(sq)` · `FK(capo, id) REF MEMBRO(spo, sq)` | `CAPO`, `SQSFIDA` |
| 5 | `MEMBRO` | relationship | **spo** (Str) · **sq** (Integer) | `FK(spo) REF SPORTIVO(nickname)` · `FK(sq) REF SQUADRA(id)` | |
| 6 | `SFIDA` | entità | **id** (Integer) · nome (Str) · inizio (Timestamp) · fine (Timestamp) · aSquadre (Boolean) · maxMembri* (Integer) · creatore (Str) · durataSecAll (Int_GEZ) · criterioVincita (Win_T) | `SERIAL: id` · `DOM: maxMembri >= 1` · `ENN: aSquadre = TRUE ⟺ maxMembri ≠ NULL` · `ENN: inizio < fine` · `FK(creatore) REF SPORTIVO(nickname)` · `INC: (id) ⊆ SASFIDA(sfida)` | `CREA` |
| 7 | `SPORT` | entità | **nome** (Str) · desc (Str) | | |
| 8 | `SASFIDA` | relationship | **sfida** (Integer) · **sport** (Str) | `FK(sfida) REF SFIDA(id)` · `FK(sport) REF SPORT(nome)` | |
| 9a | `ATTIVITÀ` | entità | **id** (Integer) · nome (Str) · sportivo (Str) · sport (Str) · inizio (Timestamp) · fine* (Timestamp) · diff* (Int_1_5) · conPercorso (Boolean) | `SERIAL: id` · `FK(sportivo) REF SPORTIVO(nickname)` · `FK(sport) REF SPORT(nome)` · `ENN: fine ≠ NULL → inizio < fine` · `ENN: diff ≠ NULL → fine ≠ NULL` | `SVOLGE`, `SPATT` |
| 9b | `ATTIVITÀ` _(seguito)_ | entità | pubblico (Boolean) · nomePerc* (Str) · commento* (Str) | `ENN: pubblico = TRUE → conPercorso = TRUE` · `ENN: nomePerc ≠ NULL ∧ commento ≠ NULL ⟺ pubblico = TRUE` | |
| 11 | `PARTECIPA` | relationship | **sportivo** (Str) · **sfida** (Integer) | `FK(sportivo) REF SPORTIVO(nickname)` · `FK(sfida) REF SFIDA(id)` | |

I riquadri 12-15 sono vuoti.

### Ulteriori vincoli esterni — progetto dei trigger (pagine 29-30)

Cinque trigger, tutti con lo stesso schema: evento, istante (**pre-operazione**), una query di
controllo, `IF … COMMIT ELSE GENERA ERRORE`.

```
T.ATTIVITÀ.POSIZIONE
- inserimento in POSIZIONE, pre-operazione
isValid = EXISTS (SELECT * FROM Attività a
                  WHERE a.id = NEW.att AND a.conPercorso = TRUE)
IF isValid COMMIT ELSE GENERA ERRORE
```

```
T.SFIDA.SQSQUADRA
- inserimento in SQUADRA, pre-operazione
isValid = EXISTS (SELECT * FROM Sfida s
                  WHERE s.id = NEW.sfida AND s.aSquadre = TRUE)
IF isValid COMMIT ELSE GENERA ERRORE
```

```
T.SFIDA.PARTECIPA
- inserimento in PARTECIPA, pre-operazione
isValid = EXISTS (SELECT * FROM Sfida s
                  WHERE s.id = NEW.sfida AND s.aSquadre = FALSE)
IF isValid COMMIT ELSE GENERA ERRORE
```

```
T.ASQUADRE.MAXMEMBRI
- inserimento in MEMBRO, pre-operazione
M = (SELECT s.maxMembri AS max FROM Sfida s, Squadra sq
     WHERE s.id = sq.sfida AND sq.id = NEW.squadra)
C = (SELECT COUNT(*) AS c FROM Membro m WHERE m.squadra = NEW.squadra)
IF C.c < M.m COMMIT ELSE GENERA ERRORE
```

Il confronto è `<` e non `<=` **perché il trigger è pre-operazione**: la riga nuova non è ancora
contata, quindi il conteggio corrente deve stare **sotto** il massimo. È l'altra faccia della
trappola del `BEFORE`, risolta senza spostare il trigger.

```
T.SQUADRA.SOLOUNASQUADRA
- inserimento in MEMBRO, pre-operazione
isError = EXISTS (SELECT * FROM Membro m, Squadra sq, Squadra sq'
                  WHERE m.squadra = sq.id AND m.sportivo = NEW.sportivo
                    AND NEW.squadra = sq'.id AND sq.sfida = sq'.sfida)
IF isError GENERA ERRORE ELSE COMMIT
```

---

## Domanda 8 — Specifiche realizzative (pagine 31-32, con seguito nella minuta 33)

```
DB.calcolaKmAttività(a: Integer) : Real_GEZ

Q = (SELECT SUM(ext.distanza(p.lat, p.long, p'.lat, p'.long)) AS sum
     FROM Posizione p, Posizione p', Attività a'
     WHERE a'.id = :a AND a'.conPercorso = TRUE
       AND p.att = :a AND p'.att = :a
       AND NOT EXISTS (SELECT * FROM Posizione p''
                       WHERE p''.att = :a
                         AND p.istante <= p''.istante AND p''.istante <= p'.istante))
RETURN Q.sum
```

```
DB.calcolaKmSport(u: Str, s: Str, i: Timestamp, f: Timestamp) : Real_GEZ

IF :f <= :i GENERA ERRORE
Q = (SELECT SUM(DB.calcolaKmAttività(a.id)) AS sum
     FROM Attività a
     WHERE a.sportivo = :u AND a.sport = :s
       AND :i <= a.inizio AND (fine IS NULL OR a.inizio <= :f)
       AND a.conPercorso = TRUE)
RETURN Q.sum
```

```
DB.calcolaTempoSport(u: Str, s: Str, i: Timestamp, f: Timestamp) : Int_GEZ

IF :f <= :i GENERA ERRORE
Q = (SELECT SUM(CASE WHEN a.fine IS NOT NULL
                     THEN a.fine - a.inizio
                     ELSE current_timestamp - a.inizio END)
     FROM Attività a
     WHERE a.sportivo = :u AND a.sport = :s
       AND :i <= a.inizio AND (fine IS NULL OR a.inizio <= :f))
RETURN Q.sum
```

```
RESOCONTOALLENAMENTI(u: Str, i: Timestamp, f: Timestamp)
    : Insieme(<s: Str, t: Int_GEZ, k: Real_GEZ>)

IF :f <= :i GENERA ERRORE
Q = (SELECT s.nome AS s,
            DB.calcolaTempoSport(:u, s.nome, :i, :f),
            DB.calcolaKmSport(:u, s.nome, :i, :f)
     FROM Sport s)
RETURN Q
```

> ✍️ **Nota sua, a margine in blu:** *«è inefficiente (versione efficiente a MINUTA 33)»*.

```
SPORTPIÙPRATICATOAMICI(u: Str, i: Timestamp, f: Timestamp) : Insieme(<s: Str>)

IF :f <= :i GENERA ERRORE

tmpTable(__s: Str__, t: Int_GEZ)
  FK: (s) REF Sport(nome)

INSERT INTO tmpTable(s, t)
  (SELECT s.nome AS s, SUM(DB.calcolaTempoSport(u.nickname, s.nome, :i, :f)) AS t
   FROM Sportivo u', Sport s, Amico a
   WHERE (a.sportivo1 = :u AND a.sportivo2 = s.nickname)
      OR (a.sportivo2 = :u AND a.sportivo1 = s.nickname)
   GROUP BY s)

Q = (SELECT s FROM tmpTable
     WHERE tt.t = (SELECT MAX(tt.t) FROM tmpTable tt))
RETURN Q
```

`[?]` gli alias `u'` e `s.nickname` nella `FROM` non tornano del tutto: `nickname` è di
`Sportivo`, non di `Sport`. La forma è però quella che interessa — **una tabella temporanea per
appoggiare i totali, poi il massimo su quella**, che è il modo del corso di realizzare un `ARGMAX`
in SQL.

### La versione efficiente, nella minuta 33

```
RESOCONTOALLENAMENTI(u: Str, i: Timestamp, f: Timestamp)
    : Insieme(<s: Str, t: Int_GEZ, k: Real_GEZ>)   ★ Versione Efficiente

IF :f <= :i GENERA ERRORE
Q = (SELECT s.nome AS s,
            SUM(CASE WHEN a.fine IS NOT NULL
                     THEN a.fine - a.inizio
                     ELSE current_timestamp - a.inizio END) AS t,
            SUM(DB.calcolaKmAttività(a.id)) AS k
     FROM Attività a
     WHERE a.sportivo = :u AND a.sport = :s
       AND :i <= a.inizio AND (fine IS NULL OR a.inizio <= :f)
     GROUP BY s)
RETURN Q.sum
```

Una sola scansione con `GROUP BY` al posto di due chiamate di funzione per ogni sport: è lo stesso
risultato, e la differenza è **il numero di interrogazioni**. La nota nel corpo che rimanda alla
minuta è ciò che rende visibile al correttore che l'inefficienza era stata vista.
