# Slimmy, prova del 30 gennaio 2023 — svolgimento di studente-B (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-B/Slimmy_Slimmy.pdf`, 27 pagine, modulo
> **`Versione 2024-06-05.UML`** compilato a stilo. Trascritto da Claude leggendo le pagine
> come immagini: **il documento è il PDF, questo è una copia a macchina e può contenere
> errori di lettura.** I punti dubbi sono marcati `[?]`.
>
> ✅ **Notazione attuale**, tutte e otto le domande svolte. Traccia:
> `tracce-esame/BD2_2023-01-30_Slimmy.pdf`. Esistono anche le copie di studente-A (UML) e
> studente-C (ER).
>
> **Non è una soluzione ufficiale e nessuno l'ha corretta.**
>
> È lo svolgimento con **più operazioni di classe** del corpus: `valido()`, `invalido()`,
> `Fedelta()` e compagnia mostrano bene come si scrive un'operazione in FOL e poi la si
> realizza in SQL.

---

## Domanda 1 — Raffinamento dei requisiti

1. **Utente**: 1.1 nome · 1.2 cognome · 1.3 nazionalità · 1.4 email · 1.5 password
2. **Alimento**: 2.1 nome · 2.2 marca `[0..1]` · 2.3 grandezza confezione `[0..1]` ·
   2.4 cod. identificativo · 2.5 cod. barre `[0..1]` · 2.6 `[kcal/unità]` · 2.7 unità ·
   2.8 porzione standard (quantità) · 2.9 quantità nutriente per unità

Accanto, uno schizzo del diagramma: `Utente` che **crea** `Scheda`, **valida**
`SchedaUtente`, **non valida** `Scheda`; `SchedaUtente` specializza `Scheda`; `Valida` e
`Invalida` sotto; `Premium` e `Dieta` a sinistra; `Diario Giorno` e `Pasto` a destra.

## Domanda 2 — Diagramma UML concettuale delle classi

### Classi

| Classe | Attributi | Operazioni |
|---|---|---|
| `Nazione` | nome : Stringa `{id}` | |
| `Utente` | nome : Stringa · cognome : Stringa · email : Mail `{id}` · password : Stringa | |
| `Abbonamento` | inizio : Data · fine : Data | |
| `DurataDieta` | inizio : Data · Fine : Data `[0..1]` | |
| `Dieta` | kCalMin : Intero ≥ 0 · kCalMax : Intero ≥ 0 `[0..1]` · nome : Stringa | |
| `Nutriente` | nome : Stringa `{id}` | |
| `Alimento` | nome : Stringa · codice : COD `[0..1]` · kCal : Intero ≥ 0 · porzione : Reale ≥ 0 · quantita : Reale ≥ 0 · istante : Data | `invalido(d : Data) : bool` |
| `AlimentoU` | | `valido(d : Data) : bool` |
| `AlimentoS` | | `valido(d : Data) : bool` |
| `Marca` | nome : Stringa `{id}` | |
| `Unita` | nome : Stringa `{id}` | |
| `TipoPasto` | nome : Stringa `{id}` | |
| `Pasto` | giorno : Date | |

Classi associative: `die_nut` (`min : Reale ≥ 0`, `max : Reale ≥ 0 [0..1]`),
`nut_al` (`grammatura : Reale ≥ 0`), `pas_ali` (`quantita : Reale ≥ 0`),
`valida` (`ist : Data`), `invalida` (`ist : Data`).

`NutOpz` **non è una classe associativa**: sul foglio è un riquadro con la freccia a
triangolo vuoto verso `Nutriente`, cioè una sottoclasse senza attributi (il nutriente
opzionale). Lo conferma la logica della Domanda 2, dove è usata come predicato unario:
`¬NutOpz(n)`.

### Associazioni

| Associazione | Classe A | mult. A | mult. B | Classe B |
|---|---|---|---|---|
| `ute_naz` | Utente | `0..*` | `1..1` | Nazione |
| `ute_abb` | Utente | `1..1` | `0..*` | Abbonamento |
| `ute_die` | Utente | `1..1` | `0..*` | DurataDieta |
| `dur_die` | DurataDieta | `0..*` | `1..1` | Dieta |
| `die_nut` | Dieta | `0..*` | `0..*` | Nutriente |
| `nut_al` | Nutriente | `0..*` | `0..*` | Alimento |
| `ute_ali` | Utente | `1..1` | `0..*` | AlimentoU |
| `valida` | Utente | `0..*` | `0..*` | AlimentoU |
| `invalida` | Utente | `0..*` | `0..*` | Alimento |
| `ute_pas` | Utente | `1..1` | `0..*` | Pasto |
| `tip_pas` | TipoPasto | `1..1` | `0..*` | Pasto |
| `pas_ali` | Pasto | `0..*` | `1..*` | Alimento |
| `ali_mar` | Alimento | `0..*` | `0..1` | Marca |
| `ali_uni` | Alimento | `0..*` | `1..1` | Unita |

### Generalizzazioni

- `Alimento` generalizza `AlimentoU` e `AlimentoS`, con vincolo **`{disjoint, complete}`**
- `Nutriente` generalizza `NutOpz` — sottoclasse semplice, senza vincolo

## Specifiche delle classi e delle associazioni

**1 · Classe `AlimentoS` — operazione `valido()`**

    valido(d : Data) : bool
      • pre: d ≤ adesso
      • post: V = { (u,dv) | invalida(u,this) ∧ ist(u,this,dv) ∧ dv ≤ d }
              |V| ≥ 100 → result = False    ∧    |V| < 100 → result = True

**2 · Classe `AlimentoU`**

    [V.invalidato_se_valido]
    ∀a,dinv [ AlimentoU(a) ∧ ∃u invalida(u,a) ∧ ist(u,a,dinv) ] →
             [ | { (u,dv) | valida(u,a) ∧ ist(u,a,dv) ∧ dv ≤ dinv } | ≥ 10 ]

    valido(d : Data) : bool
      • pre: d ≤ adesso
      • post: V  = { (u,dv) | invalida(u,this) ∧ ist(u,this,dv) ∧ dv ≤ d }
              Vv = { (u,dv) | valida(u,this)  ∧ ist(u,this,dv) ∧ dv ≤ d }
              |Vv| ≥ 10 ∧ |V| ≤ 100 → result = True
              ∧ [ |Vv| ≤ 10 ∨ (|Vv| ≥ 10 ∧ |V| ≥ 100) ] → result = False

**3 · Classe `Alimento`**

    [V.validato_dopo_creato]
    ∀a,da,u,dv [ AlimentoU(a) ∧ valida(u,a) ∧ ist(u,a,dv) ∧ istante(a,da) ] → da < dv

    [V.invalidato_dopo_creato]
    ∀a,da,u,dv [ Alimento(a) ∧ invalida(u,a) ∧ ist(u,a,dv) ∧ istante(a,da) ] → da < dv

    [V.nutrienti_obbligatori]
    ∀a,n [ Alimento(a) ∧ Nutriente(n) ∧ ¬NutOpz(n) ] → nut_ali(a,n)

    [V.cod_unico]
    ∀a1,a2,c1,c2 [ Alimento(a1) ∧ codice(a1,c1) ∧ Alimento(a2) ∧ codice(a2,c2) ∧
                   a1 ≠ a2 ] → c1 ≠ c2

**4 · Classe `Dieta`**

    [V.intervallo_calorie]
    ∀d,m,M [ Dieta(d) ∧ kCalMin(d,m) ∧ kCalMax(d,M) ] → m ≤ M

    [V.durata_dieta]
    ∀d,i,f [ DurataDieta(d) ∧ inizio(d,i) ∧ Fine(d,f) ] → i ≤ f

    [V.intervallo_nutrienti]
    ∀n,d,m,M [ Dieta(d) ∧ min(d,n,m) ∧ max(d,n,M) ] → m ≤ M

    [V.no_intersezione_dieta]
    ∀u,d1,d2,i1,i2 [ DurataDieta(d1) ∧ DurataDieta(d2) ∧ inizio(d1,i1) ∧ inizio(d2,i2) ∧
                     ute_die(u,d1) ∧ ute_die(u,d2) ∧ d1 ≠ d2 ] →
      [ ¬∃t t ≥ i1 ∧ t ≥ i2 ∧ [ ∃f Fine(d1,f) → t ≤ f ] ∧ [ ∃f Fine(d2,f) → t ≤ f ] ]

**5 · Classe `Alimento` — operazione `invalido()`**

    invalido(d : Data) : bool
      • pre: d ≤ adesso
      • post: V = { (u,dv) | invalida(u,this) ∧ ist(u,this,dv) ∧ dv ≤ d }
              |V| ≥ 100 → result = True    ∧    |V| < 100 → result = False

**6 · Classe `Pasto` — [V.nel_pasto_se_valido_e_creato]**

    ∀p,dp,a,u [ Pasto(p) ∧ giorno(p,dp) ∧ pas_ali(p,a) ∧ Utente(u) ∧ ute_pas(u,p) ∧
                Alimento(a) ∧ istante(a,da) ] →
      da ≤ dp ∧ [ valido(a,dp,True) ∨
                  [ ¬invalido(a,dp,False) ∧ ∃k valida(u,a) ∧ ist(u,a,k) ∧ k ≤ dp ] ∨
                  ute_ali(u,a) ]

**7 · Classe `Abbonamento`**

    [V.durata_abbonamento]
    ∀a,i,f [ Abbonamento(a) ∧ inizio(a,i) ∧ Fine(a,f) ] → i ≤ F

    [V.no_intersezione_abbonamento]
    ∀a1,a2,u,i1,i2,f1,f2 [ Abbonamento(a1) ∧ Abbonamento(a2) ∧ inizio(a1,i1) ∧
                           inizio(a2,i2) ∧ Fine(a1,f1) ∧ Fine(a2,f2) ∧ a1 ≠ a2 ∧
                           ute_abb(a1,u) ∧ ute_abb(a2,u) ] → [ f1 < i2 ] ∨ [ f2 < i1 ]

**8 · Classe `AlimentoU` — [V.no_auto_validazione]**

    ∀a,u [ Alimento(a) ∧ valida(u,a) ] → ¬ute_ali(u,a)

## Specifiche dei tipi di dato

    COD  = [0-9]{10}
    Mail = [a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{2,6}

## Domanda 3 — Diagramma UML degli use-case

| Attore | Use-case |
|---|---|
| `UtenteWeb` | `Registrazione` |
| `Redazione` | `ArchivioAlimenti` |
| `Utente` | `AcquistoAbbonamento` · `ValidazioneAlimento` · `Statistiche` · `RicercaAlimenti` · `ArchivioAlimenti` |
| `UtentePremium` → generalizza `Utente` | `ResocontoDieta` · `CreazioneDieta` |

## Domanda 4 — Segnature delle operazioni

    Registrazione
      registra(n : Stringa, c : Stringa, naz : Nazionalita, e : Mail, p : Stringa) : Utente

    ValidazioneAlimento
      valida(a : AlimentoU)
      invalida(a : Alimento)

    AcquistoAbbonamento
      compra(i : Data, f : Data) : Abbonamento

    ArchivioAlimenti
      aggiungi_nuovo(n : Stringa, c : COD [0..1], cal : Reale ≥ 0, q : Reale ≥ 0,
                     u : Unita, m : Marca [0..1],
                     nut : (Reale ≥ 0, Nutriente) [0..*]) : Alimento

    RicercaAlimenti
      cerca(n : Stringa, cal : Reale ≥ 0 [0..1]) : Alimento [0..*]

    Statistiche
      alimenti_comuni(p : TipoPasto) : (Alimento, Intero, Reale) [0..*]
      cal_giornaliere(u : Utente, d : Data) : Reale ≥ 0
      nut_giornalieri(u : Utente, d : Data) : (Reale ≥ 0, Nutriente) [0..*]
        ← nota sua: «numero minimo: nut obbligatori»

    CreazioneDieta
      crea_dieta(calmin : Reale ≥ 0, calmax : Reale ≥ 0 [0..1],
                 n : (m : Reale ≥ 0, M : Reale ≥ 0 [0..1], Nutriente)) : Dieta
      inizia(d : Dieta) : DurataDieta
      termina(d : Dieta) : DurataDieta

    ResocontoDieta
      nutrienti_rimanenti(u : Utente, d : Data)

## Domanda 5 — Specifiche delle operazioni di use-case

**`alimenti_comuni(p : TipoPasto) : (Alimento, Intero, Reale) [0..*]`**

- pre: nessuna
- post: `A = { (a,n,q) | Alimento(a) ∧ alimento_in_pasto(a,p,n,q) }`
  `Result = Argmax(n)` per `(a,n,q) ∈ A`

**`alimento_in_pasto(tp : TipoPasto, a : Alimento) : (Intero ≥ 0, Reale ≥ 0)`**

> Commento suo a margine: *«dato 1 tipo di pasto ed un alimento, restituisce il numero di
> pasti di quel tipo che includono tale alimento, con la quantità media.»*

- pre: nessuna
- post: `P = { (p,q) | tip_pas(p,tp) ∧ pas_ali(p,a) ∧ quantita(p,a,q) }`
  `Result = ( |P| , Σ_{(p,q) ∈ P} q · 1/|P| )`

**`nutrienti_rimanenti(u : Utente, d : Data) : (Nutriente, Reale ≥ 0) [0..*]`**

- pre: esiste un abbonamento attivo in `d` **e** una durata-dieta che copre `d`
- post: `N = { (n,r) | Nutriente(n) ∧ nutriente_rimanente(u,d,n,r) }`, `Result = N`

**`nutriente_rimanente(u : Utente, d : Data, n : Nutriente) : Reale ≥ 0`**

- pre: come sopra
- post:

      Q = { (p,a,g,q) | Alimento(a) ∧ nut_al(a,n) ∧ grammatura(a,n,g) ∧ Pasto(p) ∧
            giorno(p,d) ∧ pas_ali(a,p) ∧ quantita(a,p,q) ∧ ute_pas(p,u) ∧
            ∃dD,i DurataDieta(dD) ∧ ute_die(u,dD) ∧ inizio(dD,i) ∧ d ≥ i ∧
            [ ∃f fine(dD,f) → d ≤ f ] ∧ ∃D Dieta(D) ∧ dur_die(dD,D) ∧ die_nut(D,n) ∧
            ∃M max(D,n,M) }

      Qingerito = Σ_{(p,a,g,q) ∈ Q} g · q

      sia M tale che: ∃dD,i DurataDieta(dD) ∧ ute_die(u,dD) ∧ inizio(dD,i) ∧ d ≥ i ∧
                      [ ∃f fine(dD,f) → d ≤ f ] ∧ ∃D Dieta(D) ∧ dur_die(dD,D) ∧
                      die_nut(D,n) ∧ max(D,n,M)

      M ≥ Qingerito → Result = M − Qingerito
      M < Qingerito → Result = 0

## Domanda 6 — Ristrutturazione

**DBMS: PostgreSQL.**

```sql
create domain Stringa as varchar NOT NULL;
create domain Mail as varchar ~ '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{2,6}';
create domain COD as varchar ~ '[0-9]{10}';
create domain Int_GEZ as Integer check (value >= 0);
create domain Real_GEZ as Real check (value >= 0);
```

**Descrizione delle scelte:** *«Fusione su alimento. Fusione su nutriente.»* — le
sottoclassi `AlimentoU`/`AlimentoS` vengono fuse nel padre (che prende `utente [0..1]`), e
`NutOpz` diventa l'attributo booleano `opz` di `Nutriente`.

**Nel diagramma ristrutturato** ogni classe prende `id : serial {id}`; `Alimento` porta le
due operazioni `invalido(d : Date) : bool` e `valido(d : Date) : bool`; i domini passano ai
nomi SQL (`Int_GEZ`, `Real_GEZ`, `Date`).

**Vincoli introdotti o modificati**

    [V.nutrienti_obbligatori]
    ∀a,n [ Alimento(a) ∧ Nutriente(n) ∧ opz(n,False) ] → nut_ali(a,n)

    [V.validato_se_utente]
    ∀a,u [ Alimento(a) ∧ valida(u,a) ] → [ ∃u' ute_ali(u',a) ]

    [V.invalidato_se_valido]
    ∀a,dinv [ Alimento(a) ∧ ∃u invalida(u,a) ∧ ist(u,a,dinv) ] →
             [ | { (u,dv) | valida(u,a) ∧ ist(u,a,dv) ∧ dv ≤ dinv } | ≥ 10 ]

## Domanda 7 — Schema relazionale

Chiave primaria sottolineata, `*` = ammette NULL.

     1  Nazione(nome: Stringa)

     2  Utente(nome: Stringa, cognome: Stringa, email: Mail, password: Stringa,
               id: serial, nazione: Stringa)
          foreign key: nazione references Nazione(nome)
          accorpa: ute_naz

     3  Abbonamento(inizio: Date, fine: Date, id: serial, utente: Integer)
          check(inizio <= Fine)
          foreign key: utente references Utente(id)
          accorpa: ute_abb

     4  Dieta(kCalMin: Real_GEZ, kCalMax*: Real_GEZ, nome: Stringa, id: serial)
          check(kCalMax >= kCalMin OR kCalMax is NULL)

     5  DurataDieta(id: serial, inizio: Date, Fine*: Date, utente: Integer, dieta: Integer)
          check(inizio <= Fine)
          foreign key: dieta references Dieta(id)
          foreign key: utente references Utente(id)
          accorpa: ute_die, dur_die

     6  Unita(nome: Stringa)

     7  Marca(nome: Stringa)

     8  Alimento(nome: Stringa, codice*: COD, kCal: Int_GEZ, porzione: Real_GEZ,
                 quantita: Real_GEZ, istante: Date, id: serial, unita: Stringa)
          unique(codice)
          foreign key: unita references Unita(nome)
          accorpa: ali_uni

     9  Alimento(marca*: Stringa, utente*: Integer)          [seguito della 8]
          foreign key: marca references Marca(id)
          foreign key: utente references Utente(id)
          accorpa: ali_mar, ute_ali

    10  invalida(utente: Integer, alimento: Integer, ist: Date)
          foreign key: utente references Utente(id)
          foreign key: alimento references Alimento(id)

    11  valida(utente: Integer, alimento: Integer, ist: Date)
          foreign key: utente references Utente(id)
          foreign key: alimento references Alimento(id)

    12  Nutriente(opz: bool, nome: Stringa)

    13  nut_al(nutriente: Stringa, alimento: Integer, grammatura: Real_GEZ)
          foreign key: nutriente references Nutriente(nome)
          foreign key: alimento references Alimento(id)

    14  die_nut(nutriente: Stringa, dieta: Integer, min: Real_GEZ, max*: Real_GEZ)
          foreign key: nutriente references Nutriente(nome)
          foreign key: dieta references Dieta(id)
          check(max is NULL OR max >= min)

    15  TipoPasto(nome: Stringa)

    16  Pasto(utente: Integer, tipo: Stringa, id: serial, giorno: Date)
          foreign key: utente references Utente(id)
          foreign key: tipo references TipoPasto(nome)
          accorpa: tip_pas, ute_pas

    17  pas_ali(pasto: Integer, alimento: Integer, quantita: Real_GEZ)
          foreign key: pasto references Pasto(id)
          foreign key: alimento references Alimento(id)

## Ulteriori vincoli esterni — trigger

**`T.nutrienti_obbligatori`** — `Insert` o `Update` su `Alimento`

    Error = EXISTS ( (SELECT nome FROM Nutriente WHERE opz = 'False')
                     EXCEPT
                     (SELECT n.nome FROM Nutriente n, die_nut dn
                      WHERE dn.alimento = new.id AND dn.nutriente = n.nome
                        AND n.opz = 'False') );

> `die_nut` qui è probabilmente un lapsus per `nut_al`: il nutriente si lega all'alimento
> con `nut_al`, non con `die_nut`. `[?]`

**`T.no_intersezione_abbonamento`** — `Insert` o `Update` su `Abbonamento`

    Error = EXISTS (SELECT * FROM Abbonamento a
                    WHERE a.utente = new.utente
                      AND (a.inizio, a.fine) OVERLAPS (new.inizio, new.fine));

**`T.validato_o_invalidato_dopo_creato`** — `Insert` o `Update` su `valida` o `invalida`

    Error = EXISTS (SELECT * FROM Alimento a
                    WHERE new.alimento = a.id AND a.ist > new.ist);

**`T.no_intersezione_dieta`** — `Insert` o `Update` su `DurataDieta`

    Error = EXISTS (SELECT * FROM DurataDieta d
                    WHERE d.utente = new.utente
                      AND (d.inizio, d.fine) OVERLAPS (new.inizio, new.Fine));

> ✍️ Nota sua a margine, in arancione: *«OVERLAPS può essere usato anche se una delle due
> date è NULL»*.

**`T.nel_pasto_se_valido_e_creato`** — `Insert` o `Update` su `pas_ali`

    OK = EXISTS (SELECT * FROM Pasto p, Utente u, Alimento a,
                      valida LEFT OUTER JOIN Utente u1 ON valida.utente = u1.id
                 WHERE new.pasto = p.id AND a.istante <= p.giorno
                   AND p.utente = u.id AND new.alimento = a.id
                   AND ((valido(a.id, pasto.giorno) = 'True') OR
                        (a.utente = u.id) OR
                        (invalido(a.id, pasto.giorno) = 'False' AND u1.id = u.id)));

**`T.no_auto_validazione`** — `Insert` o `Update` su `valida`

    Error = EXISTS (SELECT * FROM Alimento a
                    WHERE new.alimento = a.id AND a.utente = new.utente);

**`T.validato_se_utente`** — `Insert` o `Update` su `valida`

    OK = EXISTS (SELECT * FROM Alimento a
                 WHERE a.id = new.alimento AND a.utente IS NOT NULL);

**`T.invalidato_dopo_validazione`** — `Insert` o `Update` su `invalida`

    Q = SELECT count(*) FROM valida v
        WHERE new.alimento = v.alimento AND v.ist <= new.ist;
    if Q >= 10: permetti  else: errore e rollback

## Domanda 8 — Specifiche realizzative

**`create function invalido(d : Date, a : Integer) : bool`**

    Q = SELECT count(*) as n FROM invalida WHERE ist <= d AND alimento = a;
    if Q.n >= 100: result = True   else: result = False

**`create function valido(d : Date, a : Integer) : bool`**

    Q = EXISTS (SELECT * FROM Alimento WHERE id = a AND utente IS NOT NULL);
    V = NOT invalido(d,a);
    nValid = SELECT count(*) FROM valida WHERE alimento = a AND ist <= d;
    if Q AND nValid >= 10 AND V: result = true
    else if NOT Q AND V: result = true
    else result = False

**`alimento_in_pasto(tp : Stringa, a : Integer) : (Int_GEZ, Real_GEZ)`**

    Result = SELECT count(*) AS num, AVG(pa.quantita)
             FROM pas_ali pa, Pasto p
             WHERE p.tipo = tp AND pa.pasto = p.id AND pa.alimento = a;

**`alimenti_comuni(tp : Stringa) : Insieme(<Integer, Int_GEZ, Real_GEZ>)`**

    WITH massimo AS (SELECT max(num) as M
                     FROM (SELECT alimento_in_pasto(tp, id) FROM Alimento a)),
         alimenti_occorrenze AS (SELECT id, alimento_in_pasto(tp, id) FROM Alimento a)
    SELECT * FROM alimenti_occorrenze oc, massimo m WHERE oc.num = m.M;

**`nutriente_rimanente(u : Integer, d : Date, n : Stringa) : Real_GEZ`**

    pre-cond: EXISTS (SELECT * FROM Abbonamento
                      WHERE utente = u AND inizio >= d AND Fine <= d)
          AND EXISTS (SELECT * FROM DurataDieta
                      WHERE utente = u AND inizio >= d
                        AND (Fine IS NULL OR (Fine IS NOT NULL AND Fine >= d)))

    M = (SELECT dn.max as m
         FROM die_nut dn, DurataDieta DD
         WHERE dn.dieta = DD.dieta AND DD.utente = u AND dn.nutriente = n
           AND DD.inizio <= d AND (DD.fine IS NULL OR DD.fine >= d)
           AND dn.max IS NOT NULL)

    T = (SELECT SUM(a.quantita * pa.quantita) as tot
         FROM Pasto p, Alimento a, pas_ali pa, nut_al na, DurataDieta DD, die_nut dn
         WHERE pa.alimento = a.id AND pa.pasto = p.id
           AND na.alimento = a.id AND na.nutriente = n
           AND p.utente = u AND p.giorno = d
           AND dn.nutriente = n AND dn.dieta = DD.dieta
           AND DD.utente = u AND DD.inizio <= d
           AND (DD.fine IS NULL OR DD.fine >= d) AND dn.max IS NOT NULL)

    Q = SELECT M.m − T.tot FROM M, T
    if Q < 0: result = 0   else: result = Q

**`nutrienti_rimanenti(u : Integer, d : Date) : Insieme(<Stringa, Real_GEZ>)`**

- pre-cond: le stesse due `EXISTS` di sopra
- post-cond: `Result = SELECT nutriente_rimanente(u,d,n) FROM Nutriente n;`

---

## Come usarlo

Il pezzo forte sono le **operazioni di classe**: `valido()` e `invalido()` compaiono prima
come specifica in FOL (Domanda 2), poi come funzione SQL (Domanda 8), e in mezzo come
condizione dentro un trigger. È il percorso completo che il corso chiede e la cosa su cui
si viene bocciati più spesso.

Due cose da guardare con sospetto, segnalate sopra: nel trigger
`T.nutrienti_obbligatori` usa `die_nut` dove servirebbe `nut_al`, e alcune precondizioni
scrivono `inizio >= d` dove il senso vorrebbe `inizio <= d`.
