# TimeBank, prova del 3 aprile 2024 — svolgimento di studente-A (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-A/Prove D'Esame/2024-4-7-TimeBank/TimeBank.pdf`,
> 26 pagine (le prime 2 sono la traccia scansionata, il modulo risposte comincia a pagina 3),
> modulo **`Versione 2024-06-05.UML`** compilato a mano. Trascritto da Claude leggendo le
> pagine come immagini: **il documento è il PDF, questo è una copia a macchina e può
> contenere errori di lettura.** I punti dubbi sono marcati `[?]`.
>
> ✅ **Svolgimento completo:** tutte e 8 le domande hanno risposta. Le pagine di
> continuazione (4, 6, 10, 14, 18, 20, 21, 22, 24) sono in bianco: gli spazi previsti sono
> bastati.
>
> Traccia: `tracce-esame/BD2_2024-04-03_TimeBank.pdf`. **Non è una soluzione ufficiale e
> nessuno l'ha corretta**: il modulo non porta né nome né voto.
>
> ⚠️ **Esiste una seconda copia di TimeBank, di studente-B**
> (`05-soluzioni-studenti/studente-B/TimeBank_TimeBank.pdf`, 19 pagine, data 12/06/2024):
> è però compilata sul modulo **`BD2.Esame.Risposte.ER`**, cioè in notazione ER, e per
> questo non è stata trascritta. Vi si trovano solo la Domanda 2 (diagramma) e un vincolo
> «no 2 scambi contemporaneamente».

---

## Domanda 1 — Raffinamento dei requisiti

Non un elenco numerato: un abbozzo del dizionario dei dati, in due colonne.

**Utente:**
- nome : Stringa
- cognome : Stringa
- mail : Email
- tel : Tel
- istIsc : DataOra
- associato alle Abilità

**Abilità:**
- nome : Stringa
- associato agli Utenti con `media(t: Data): Reale >= 0`

**Scambio:**
- inizioSca : DataOra
- durataOre : Reale > 0
- associato agli Utenti che danno e ricevono
- associato all'Abilità
- associato all'Utente che riceve tramite Feedback: `voto : 1..10`

---

## Domanda 2 — Diagramma UML concettuale delle classi

### Classi

| Classe | Attributi | Operazioni |
|---|---|---|
| `ABILITA` | nome : Stringa `{id}` | |
| `UTENTE` | nome : Stringa · cognome : Stringa · mail : Email · tel : Tel · istIsc : DataOra | `saldo(t: DataOra) : Reale >= 0` |
| `SCAMBIO` | inizioSca : DataOra · durataOre : Reale > 0 | `valore() : Reale > 0` |

### Associazioni

| Associazione | Estremo 1 | Estremo 2 | Note |
|---|---|---|---|
| `ABISCA` | `ABILITA` 1 | `SCAMBIO` 0..* | l'abilità richiesta nello scambio |
| `ABIUTE` | `ABILITA` 0..* | `UTENTE` 0..* | **classe associativa**, con l'operazione `media(t: DataOra) : Reale >= 0` |
| `DASCA` | `UTENTE` 1 | `SCAMBIO` 0..* | l'utente offerente |
| `CHIEDESCA` | `UTENTE` 1 | `SCAMBIO` 0..* | l'utente richiedente |
| `FEEDBACK` | `UTENTE` 1 | `SCAMBIO` 0..* | **specializzazione di `CHIEDESCA`** (generalizzazione fra associazioni), con attributo `voto : 1..10` |

`FEEDBACK` è disegnata con il triangolo vuoto puntato su `CHIEDESCA`: è
un'associazione che ne specializza un'altra, non una classe.

### Specifiche delle classi e delle associazioni

**1 — Classe `UTENTE`**

```
V.NOSALDONEGATIVO
∀u, sc, v, sa, i   CHIEDESCA(u, sc) ∧ VALORE(sc, v)
  ∧ SALDO(u, i, sa) ∧ INIZIOSCA(sc, i) → sa >= v
```

**2 — Classe `UTENTE`**

```
V.SCAMBIDISGIUNTI
∀u, sc, i, d  [CHIEDESCA(u, sc) ∨ DASCA(u, sc)]
  ∧ INIZIOSCA(sc, i) ∧ DURATA(sc, d) →
¬∃ sc', i', d', t  [CHIEDESCA(sc', u) ∧ DASCA(sc', u)]
  ∧ INIZIOSCA(sc', i') ∧ DATAORE(sc', d') ∧ DATAORA(t)     [?] «DATAORE» sta per DURATAORE
  ∧ i <= t <= i + d ORE  ∧  i' <= t <= i' + d' ORE
```

**3 — Classe `SCAMBIO`**

```
V.ABILITAPOSSEDUTA
∀u, sc, a   DASCA(u, sc) ∧ ABISCA(sc, a) → ABIUTE(a, u)

V.DANONCHIEDE
∀u, u', sc   DASCA(u, sc) ∧ CHIEDESCA(u', sc) → u ≠ u'

V.DOPOISCRIZIONE
∀sc, u, u', i, i', is   DASCA(u, sc) ∧ CHIEDESCA(u', sc) ∧ ISTISC(u, i)
  ∧ ISTISC(u', i') ∧ INIZIOSCA(sc, is) → i <= is ∧ i' <= is
```

**4 — Associazione `ABIUTE`**

```
MEDIA(t: DataOra) : Reale >= 0
- pre:
- post:
  F = { (s, u) | ∃u FEEDBACK(u, s) ∧ VOTO(u, s, v)
                 ∧ DASCA(s, this.u) ∧ ABISCA(s, this.a)
                 ∧ ∃i INIZIOSCA(i, s) ∧ i <= t }

  (|F| = 0 → RESULT = 0) ∧
  (|F| > 0 → RESULT = Σ_{(s,v) ∈ F} v / |F|)
```

**6 — Classe `SCAMBIO`**

```
VALORE() : Reale >= 0
- pre:
- post:
  siano d, m tali che:
  DURATAORE(this, d) ∧ ∃a, u, i  DASCA(this, u)
    ∧ ABISCA(this, a) ∧ MEDIA(a, u, i, m) ∧ INIZIOSCA(this, i)
  RESULT = d (1 + ARCTAN(0.05 * m))
```

I riquadri 5, 7 e 8 sono in bianco.

### Specifiche dei tipi di dato e ulteriori vincoli esterni

```
EMAIL : Stringa secondo standard
TEL   : Stringa secondo standard

UTENTE.SALDO(t: DataOra) : Reale >= 0
- pre: ∃i ISTISC(this, i) ∧ t >= i
- post:
  S = { (s, v) | SCAMBIO(s) ∧ CHIEDESCA(this, s) ∧ VALORE(s, v)
                 ∧ ∃is INIZIOSCA(is, s) ∧ is <= t }
  G = { (s, v) | SCAMBIO(s) ∧ DASCA(this, s) ∧ VALORE(s, v)
                 ∧ ∃is INIZIOSCA(is, s) ∧ is <= t }

  RESULT = x + Σ_{(s,v) ∈ G} v + Σ_{(s,v) ∈ S} v
```

> Nota di lettura: il secondo addendo dovrebbe essere sottratto (il saldo è la somma dei
> valori offerti **meno** quelli richiesti), ma sul foglio i due segni sono entrambi `+`.
> Nella Domanda 8 la stessa operazione è scritta come `x + G.s − S.s`, cioè con la
> sottrazione.

---

## Domanda 3 — Diagramma UML degli use-case

| Attore | Use-case |
|---|---|
| `UTENTE` | `REGISTRAZIONE` |
| `UTENTE REGISTRATO` | `CERCA UTENTE` · `GESTIONE ABILITA` · `FEEDBACK` |

I due attori non sono legati da una generalizzazione. Non compaiono use-case per il
calcolo del saldo corrente e per l'elenco delle abilità di un dato utente: quest'ultimo
rientra però nelle segnature della Domanda 4, dentro `CERCA UTENTE`.

---

## Domanda 4 — Segnature delle operazioni di use-case

```
REGISTRAZIONE:
- NEWUTENTE(n: Stringa, c: Stringa, e: Email, t: Tel) : Utente

CERCAUTENTE:
- CERCAMEDIA(a: Abilita, m: Reale >= 0) : Utente[0..*]
- ABILITAUTENTE(u: Utente) : Abilita[0..*]

GESTIONE ABILITA:
- NEWABILITA(u: Utente, a: Abilita)
- REMOVEABILITA(u: Utente, a: Abilita)
- MOLTABI(u: Utente, a: Abilita) : Reale >= 0

FEEDBACK:
- NEWFEEDBACK(u: Utente, s: Scambio, v: 1..10)
```

---

## Domanda 5 — Specifiche concettuali delle operazioni di use-case

Svolte solo le due operazioni contrassegnate dalla barra laterale.

```
CERCAMEDIA(a: Abilita, m: Reale >= 0) : Utente[0..*]
- pre:
- post:
  RESULT = { u | UTENTE(u) ∧ ABIUTE(u, a) ∧ ∃m' MEDIA(a, u, m') ∧ m' >= m }
```

```
MOLTABI(u: Utente, a: Abilita) : Reale >= 0
- pre: ABIUTE(u, a)
- post: sia m tale che: MEDIA(a, u, ADESSO, m)
        RESULT = m
```

---

## Domanda 6 — Ristrutturazione

**DBMS scelto:** PostgreSQL.

### Domini

```sql
CREATE DOMAIN STRINGA AS VARCHAR NOT NULL;
CREATE DOMAIN REALGZ AS REAL CHECK (VALUE > 0);
CREATE DOMAIN REALGEZ AS REAL CHECK (VALUE >= 0);
CREATE DOMAIN EMAIL AS VARCHAR;
CREATE DOMAIN TEL AS VARCHAR;
CREATE DOMAIN VOTO AS INTEGER CHECK (VALUE >= 1 AND VALUE <= 10);
```

### Diagramma ristrutturato

| Classe | Attributi | Operazioni |
|---|---|---|
| `ABILITA` | nome : Stringa `{id}` | |
| `UTENTE` | id : Serial `{id}` · nome : Stringa · cognome : Stringa · mail : Email · tel : Tel · istIsc : Timestamp | `saldo(t: Timestamp) : RealGEZ` |
| `SCAMBIO` | id : Serial `{id}` · inizioSca : Timestamp · durataOre : RealGZ | `valore() : RealGZ` |

Associazioni invariate — `ABISCA` (1 – 0..*), `ABIUTE` classe associativa con
`media(t: Timestamp) : RealGEZ`, `DASCA` (1 – 0..*), `CHIEDESCA` (1 – 0..*) — con
`FEEDBACK` (`voto : Voto`) ora **associazione autonoma**, non più specializzazione.

**Scelte dichiarate:** «eliminata generalizzazione su FEEDBACK».

**Vincoli esterni introdotti o modificati:**

```
V.FEEDBACK.SECHIEDE
∀u, s   FEEDBACK(u, s) → CHIEDESCA(u, s)
```

---

## Domanda 7 — Schema relazionale

**1 — `ABILITA`** (da classe)

| attributo | dominio |
|---|---|
| **nome** | Stringa |

**2 — `UTENTE`** (da classe)

| attributo | dominio |
|---|---|
| **id** | Serial |
| nome | Stringa |
| cognome | Stringa |
| mail | Email |
| tel | Tel |
| istIsc | Timestamp |

**3 — `ABIUTE`** (da associazione)

| attributo | dominio |
|---|---|
| **abilita** | Stringa |
| **utente** | Integer |

```
FK (abilita) REF ABILITA(nome)
FK (utente)  REF UTENTE(id)
```

**4 — `SCAMBIO`** (da classe)

| attributo | dominio |
|---|---|
| **id** | Serial |
| inizioSca | Timestamp |
| durataOre | RealGZ |
| da | Integer |
| chiede | Integer |
| voto * | Voto |
| abilita | Stringa |

```
FK (da)      REF UTENTE(id)
FK (chiede)  REF UTENTE(id)
FK (abilita) REF ABILITA(nome)
CHECK (da <> chiede)
(da, abilita) ⊆ ABIUTE(utente, abilita)
```

La relazione accorpa le associazioni **FEEDBACK, ABISCA, DASCA, CHIEDESCA**.
Le relazioni 5-10 sono in bianco: lo schema è di quattro relazioni.

### Ulteriori vincoli esterni — trigger

```
T.UTENTE.NOSALDONEGATIVO
- INSERT OR UPDATE SCAMBIO
VALID = EXISTS (SELECT * FROM SCAMBIO
                WHERE VALORE(id) < SALDO(da, inizioSca) AND id = NEW.id)
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.UTENTE.SCAMBIDISGIUNTI
- INSERT OR UPDATE SCAMBIO
VALID = NOT EXISTS (SELECT * FROM SCAMBIO
                    WHERE [da = NEW.da OR da = NEW.chiede OR chiede = NEW.chiede
                           OR chiede = NEW.da]
                      AND id <> NEW.id
                      AND (inizioSca, INTERVAL '1 HOUR' * durataOre)
                          OVERLAPS (NEW.inizioSca, INTERVAL '1 HOUR' * NEW.durataOre))
IF VALID: COMMIT
ELSE: ERRORE
```

```
T.SCAMBIO.DOPOISCRIZIONE
- INSERT OR UPDATE SCAMBIO
VALID = EXISTS (SELECT * FROM UTENTE u1, UTENTE u2
                WHERE u1.id = NEW.da AND u2.id = NEW.chiede
                  AND u1.istIsc <= NEW.inizioSca AND u2.istIsc <= NEW.inizioSca)
IF VALID: COMMIT
ELSE: ERRORE
```

---

## Domanda 8 — Specifiche realizzative

```
CERCAMEDIA(a: Stringa, m: RealGZ) : Integer[0..*]
R = SELECT u.id FROM UTENTE u, ABIUTE au
    WHERE au.utente = u.id AND au.abilita = a
      AND MEDIA(u.id, a) >= m
RETURN R
```

```
MOLTABI(u: Integer, a: Stringa) : RealGEZ
ERROR = NOT EXISTS (SELECT * FROM ABIUTE
                    WHERE utente = u AND abilita = a)
IF ERROR: ERRORE
R = SELECT MEDIA(u, a, NOW())
RETURN R
```

```
CREATE FUNCTION MEDIA(u: Integer, a: Stringa, t: Timestamp) : RealGEZ
R = WITH F AS (SELECT AVG(voto) m FROM SCAMBIO
               WHERE da = u AND abilita = a AND inizioSca <= t)
    SELECT CASE
    WHEN m IS NULL THEN 0
    ELSE m
    END
    FROM F
RETURN R
```

```
CREATE FUNCTION VALORE(s: Integer) : RealGEZ
R = SELECT durataOre (1 + ARCTAN(0.05 * MEDIA(da, abilita, inizioSca)))
    FROM SCAMBIO
    WHERE id = s
RETURN R
```

```
CREATE FUNCTION SALDO(u: Integer, t: Timestamp) : RealGEZ
IF t < (SELECT istIsc FROM UTENTE
        WHERE id = u): ERRORE
R = WITH S AS (SELECT SUM(VALORE(id)) s FROM SCAMBIO
               WHERE chiede = u AND inizioSca <= t),
         G AS (SELECT SUM(VALORE(id)) s FROM SCAMBIO
               WHERE da = u AND inizioSca <= t)
    SELECT x + G.s − S.s FROM S, G
RETURN R
```

Non è detto, per nessuna operazione, se vada implementata nel DBMS o nel back-end, come
la Domanda 8 chiede esplicitamente.

---

## Note di lettura

- Il numero `x` (l'accredito bonus all'iscrizione) è usato in `SALDO` sia nella specifica
  concettuale sia in quella realizzativa, ma non è mai dichiarato: né come attributo, né
  come costante, né come relazione di configurazione.
- `MEDIA` compare con **arietà diverse**: `MEDIA(a, u, m)` nella Domanda 5,
  `MEDIA(a, u, i, m)` nella specifica di `VALORE`, `MEDIA(u.id, a)` a due argomenti nella
  Domanda 8 e `MEDIA(u, a, NOW())` a tre. La funzione SQL dichiarata è a tre argomenti.
- Nella Domanda 8, `MEDIA` calcola la media dei `voto` degli scambi con `inizioSca <= t`,
  cioè include lo scambio in corso; la traccia dice «tutti gli scambi avvenuti **prima** di
  `t`».
- `VALORE` scrive `durataOre (1 + ...)`: manca l'operatore di moltiplicazione.
