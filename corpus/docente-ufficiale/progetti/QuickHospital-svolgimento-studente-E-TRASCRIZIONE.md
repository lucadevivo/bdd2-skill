# QuickHospital — svolgimento di studente-E (trascrizione)

> **Fonte:** `QuickHospital-svolgimento-studente-E.pdf`, 10 pagine di inchiostro digitale
> (export OneNote, giugno 2020). Trascritto da Claude leggendo le pagine come immagini:
> **il documento è il PDF, questo è una copia a macchina e può contenere errori di lettura.**
> I punti dubbi sono marcati `[?]`.
>
> **Vale doppio** perché è l'unico svolgimento del corpus che ha anche la correzione:
> `QuickHospital-correzioni-tutor.md`. Leggi i due insieme — lì il tutor dice quali di
> queste scelte sono sbagliate e perché (la generalizzazione completa Paziente/Medico, i
> vincoli sulle prestazioni nella stessa data, il vincolo mancante sui ricoveri sovrapposti,
> il numero di letto mancante).
>
> ⚠️ **Doppio avviso.** Primo: di QuickHospital esiste già la **soluzione ufficiale del
> docente**, in `soluzioni-ufficiali/QuickHospital.md` (621 righe) — ed è **già in UML**.
> Studia quella. Questa trascrizione serve solo a vedere, accanto alla correzione del tutor,
> quali scelte un correttore boccia.
>
> Secondo, la notazione: è del 2020, quando il corso usava il **diagramma ER**
> (entità, relationship, cardinalità `(min,max)` sui rami). Oggi la Domanda 2 chiede un
> **diagramma UML delle classi** con molteplicità sui lati opposti. Struttura, vincoli in
> FOL, use-case, ristrutturazione, schema relazionale e specifiche realizzative restano
> validi; il disegno va rifatto in UML.
>
> I diagrammi qui sono descritti a parole, elemento per elemento, perché tu possa
> ridisegnarli in Visual Paradigm.

---

## 1. Diagramma ER

**Entità e attributi**

| Entità | Attributi |
|---|---|
| `Persona` | nome, cognome, nascita |
| `Paziente` | telefono (1,N), email, indirizzo |
| `Medico` | — (eredita da Persona) |
| `Ricovero` | data |
| `RicoveroTerminato` | dimissione |
| `Letto` | — |
| `Stanza` | settore, piano |
| `Specializzazione` | nome |
| `Prestazione` | descrizione, data |
| `PrestAssegnata` | — |

**Generalizzazioni** (freccia a triangolo vuoto verso il padre)

- `Paziente` → `Persona`
- `Medico` → `Persona`
- `RicoveroTerminato` → `Ricovero`
- `PrestAssegnata` → `Prestazione`

**Relationship** (cardinalità come lette sul disegno)

| Relationship | Estremo 1 | Estremo 2 |
|---|---|---|
| `ricovPaz` | `Ricovero` (1,1) | `Paziente` (0,N) |
| `ricovLetto` | `Ricovero` (1,1) | `Letto` (0,N) |
| `lettoStanza` | `Letto` (1,1) | `Stanza` (1,N) |
| `ricovMed` | `Ricovero` (1,1) | `Medico` (0,N) |
| `specPrim` | `Medico` (1,1) | `Specializzazione` (0,N) |
| `specSecon` | `Medico` (0,N) | `Specializzazione` (0,N) |
| `specPrest` | `Prestazione` (1,1) | `Specializzazione` (0,N) |
| `medPrest` | `PrestAssegnata` (1,1) | `Medico` (0,N) |
| `pazPrestaz` | `Prestazione` (1,1) | `Paziente` (0,N) |

`Ricovero` compare due volte nel disegno: una come entità piena, una come riquadro
tratteggiato accanto a `ricovMed` — è la stessa entità, ridisegnata per non incrociare le
linee.

## 2. Specifiche dei dati

**Dominio Indirizzo** — record composto dai seguenti campi:

- `via` : stringa
- `civico` : intero > 0, (0,1)
- `CAP` : stringa numerica di 5 cifre

**Dominio Telefono** — record composto dai seguenti campi:

- `prefisso` : stringa numerica di 2 cifre
- `numero` : stringa numerica di 10 cifre

| Entità | attributo | tipo |
|---|---|---|
| Persona | nome | stringa |
| | cognome | stringa |
| | nascita | data |
| Paziente | telefono (1,N) | Telefono |
| | email | stringa |
| | indirizzo | Indirizzo |
| Ricovero | data | data |
| RicoveroTerminato | dimissione | data |
| Stanza | piano | intero > 0 |
| | settore | intero > 0 |
| Specializzazione | nome | stringa |
| Prestazione | data | data |
| | descrizione | stringa |

## 3. Vincoli esterni (logica del primo ordine)

**[V.RicoveroTerminato.dimissione.dopoDataRicovero]**

    ∀rt,d,dd  RicoveroTerminato(rt) ∧ data(rt,d) ∧ dimissione(rt,dd) → d ≤ dd

**[V.Ricovero.periodoStessoLetto]**

    ∀r,d,l  Ricovero(r) ∧ data(r,d) ∧ ricovLetto(r,l) →
      ( ( ∃dd RicoveroTerminato(r) ∧ dimissione(r,dd) →
            ¬∃r2,d2 Ricovero(r2) ∧ data(r2,d2) ∧ d2 ≥ d ∧ d2 ≤ dd ∧ ricovLetto(r2,l) ∧ r ≠ r2 )
      ∨ ( ¬∃r2,d2 Ricovero(r2) ∧ data(r2,d2) ∧ d2 ≥ d ∧ ricovLetto(r2,l) ∧ r2 ≠ r ) )

**[V.Ricovero.periodoStessoPaziente]** — identico al precedente con `ricovPaz` al posto di
`ricovLetto` e `p` al posto di `l`.

**[V.Persona.nascita.primaRicovero]**

    ∀e,pe,d ( Ricovero(e) ∧ (ricovPaz(e,pe) ∨ ricovMed(e,pe)) ∧ nascita(pe,d) )
      → ¬∃de data(e,de) ∧ de < d

**[V.Persona.nascita.primaPrestazione]**

    ∀e,pe,d ( Prestazione(e) ∧ (pazPrestaz(e,pe) ∨ medPrest(e,pe)) ∧ nascita(pe,d) )
      → ¬∃de data(e,de) ∧ de < d

**[V.Persona.medicoPaziente.almenoUno]**

    ∀p  Persona(p) → Medico(p) ∨ Persona(p)

> Sul foglio c'è scritto `Persona(p)` anche nel conseguente: è un lapsus, il senso è
> `Medico(p) ∨ Paziente(p)`.

**[V.Stanza.maxLetti]**

    ∀s  Stanza(s) → | { l | lettoStanza(s,l) } | ≤ 8

**[V.Medico.spec.disp]**

    ∀m  Medico(m) → ( ∃s specPrim(m,s) → ¬specSecon(m,s) )

**[V.Paziente.ricovPrestaz.almenoUno]**

    ∀p  Paziente(p) → ∃e ricovPaz(p,e) ∨ pazPrestaz(p,e)

## 4. Diagramma UML degli use-case

| Attore | Use-case |
|---|---|
| `Medico` | `StrumentiMedici` |
| `UfficioPrenotazioni` | `StrumentiRicoveri`, `StrumentiPrestazioni` |

## 5. Specifiche degli use-case

### Use-case `StrumentiRicoveri`

**`postiDisponibili(d : data) : intero ≥ 0`**

- precondizioni: nessuna
- postcondizioni:
  - Modifica livello estensionale dei dati: nessuna
  - Valore di ritorno:

        Ltot = { l | ∃s Stanza(s) ∧ lettoStan(l,s) }
        Locc = { l | ∃r,dr ( Ricovero(r) ∧ ¬RicoveroTerminato(r) ∧ data(r,dr) ∧ d > dr )
                          ∨ ( RicoveroTerminato(r) ∧ data(r,dr) ∧ d < dr ) }
        result = |Ltot| − |Locc|

> In `Locc` manca il legame fra `r` e `l` (`ricovLetto(r,l)`): così scritto l'insieme non
> dipende da `l`. [?] — così è sul foglio.

**`registraRicovero(p : PazInterno, l : Letto, m : Medico) : Ricovero`**

- precondizioni: `postiDisponibili(ADESSO) ∧ ¬∃r ricovLetto(r,l)`
- postcondizioni — Modifica livello estensionale dei dati:
  - Variazioni dominio di interpretazione: nuovo elemento `α`
  - Variazioni ennuple di predicato: `Ricovero(α)`, `data(α, ADESSO)`, `ricovPaz(α,p)`,
    `ricovLetto(α,l)`, `ricovMed(α,m)`
  - Valore di ritorno: `result = α`

**`dimissioneRicovero(r : Ricovero) : RicoveroTerminato`**

- precondizioni: nessuna
- postcondizioni — Modifica dominio di interpretazione:
  - Variazioni dominio di interpretazione: nessuna
  - Variazioni ennuple di predicato: `RicoveroTerminato(r)`, `dimissione(r, ADESSO)`
  - Valore di ritorno: `result = r`

### Use-case `StrumentiPrestazioni`

**`mediciIdonei(p : Prestazione) : Medico (0,N)`**

- precondizioni: `¬PrestAssegnata(p)`
- postcondizioni:
  - Modifica livello estensionale dei dati: nessuna
  - Valore di ritorno:

        Pri = { m | ∃sp specPrest(p,sp) ∧ specPrim(m,sp) }
        Sec = { m | ∃sp specPrest(p,sp) ∧ specSecon(m,sp) }
        result = Pri  se |Pri| > 0
                 Sec  altrimenti

### Use-case `StrumentiMedici`

**`itinerarioVisite(m : Medico)`**

- precondizioni: nessuna
- postcondizioni:
  - Modifica dominio di interpretazione: nessuna
  - Valore di ritorno:

        V = { (pi, se) | ∃r,l,s ricovMed(m,r) ∧ ricovLetto(r,l) ∧ lettoStan(l,s) ∧
                          piano(s,pi) ∧ settore(s,se) ∧ ¬RicoveroTerminato(r) }
        result = V

> NOTA (sua): l'insieme `V` dovrà, in fase di progettazione, essere ordinato in base al
> piano, e a parità di piano in base al settore.

## 6. Ristrutturazione ER

**Cosa cambia nel diagramma**

- spariscono le generalizzazioni `RicoveroTerminato → Ricovero` e `PrestAssegnata →
  Prestazione`, sostituite da attributi booleani: `Ricovero` prende `terminato` e
  `dimissione (0,1)`, `Prestazione` prende `assegnata`;
- l'attributo composto e multivalore `telefono` diventa l'entità **`ValoreTelefono`**
  (`valorePrefisso`, `valoreNumero`, entrambi identificanti) legata a `Paziente` dalla
  relationship `telefono` (1,N)–(1,N);
- l'attributo composto `indirizzo` viene spianato negli attributi `via`, `civico (0,1)`,
  `CAP` di `Paziente`;
- gli attributi di `Persona` (nome, cognome, nascita) scendono in `Paziente` e `Medico`, che
  prendono anche un identificatore: `email` per `Paziente`, `id` per `Medico`;
- prendono un `id` anche `Ricovero`, `Letto`, `Stanza`, `Prestazione`;
- `medPrest` diventa `Medico` (0,N) – `Prestazione` (0,1).

**Nuovi vincoli**

    ∀r  ( Ricovero(r) ∧ terminato(r,true) )  ↔  ∃d dimissione(r,d)

    ∀pr ( Prestazione(pr) ∧ assegnata(pr,true) )  ↔  ∃m medPrest(m,pr)

**Vincoli modificati** — i tre vincoli sui ricoveri, riscritti con `terminato(r,true)` al
posto di `RicoveroTerminato(r)`:

    [V.RicoveroTerminato.dimissione.dopoDataRicovero]
    ∀rt,d,dd  Ricovero(rt) ∧ terminato(rt,true) ∧ data(rt,d) ∧ dimissione(rt,dd) → d ≤ dd

    [V.Ricovero.periodoStessoLetto]
    ∀r,d,l  Ricovero(r) ∧ data(r,d) ∧ ricovLetto(r,l) →
      ( ( ∃dd terminato(r,true) ∧ dimissione(r,dd) →
            ¬∃r2,d2 Ricovero(r2) ∧ data(r2,d2) ∧ d2 ≥ d ∧ d2 ≤ dd ∧ ricovLetto(r2,l) ∧ r ≠ r2 )
      ∨ ( ¬∃r2,d2 Ricovero(r2) ∧ data(r2,d2) ∧ d2 ≥ d ∧ ricovLetto(r2,l) ∧ r2 ≠ r ) )

    [V.Ricovero.periodoStessoPaziente]  — idem con ricovPaz

## 7. Ristrutturazione delle specifiche dei dati

```sql
create domain StringS as varchar(100);
create domain StringM as varchar(200);
create domain IntegerGZ as integer check (value > 0);
create domain PrefissoTelefono as varchar(5) check (value ~ '^\+[0-9]+$');
create domain NumeroTelefono as char(10) check (value ~ '^[0-9]{10,6}$');  -- [?] cifre poco leggibili
create domain CAP as char(5) check (value ~ '^[0-9]{5,5}$');
```

| Entità | attributo : tipo |
|---|---|
| Medico | id : integer · nome : StringS · cognome : StringS · nascita : date |
| Paziente | nome : StringS · cognome : StringS · nascita : date · email : StringS · via : StringM · civico : IntegerGZ · CAP : CAP |
| Ricovero | id : integer · data : date · terminato : boolean · dimissione : date |
| Letto | id : integer |
| Stanza | id : integer · piano : IntegerGZ · settore : IntegerGZ |
| Specializzazione | nome : StringS |
| Prestazione | id : integer · data : date · descrizione : stringa · assegnata : boolean |
| ValoreTelefono | valorePrefisso : PrefissoTelefono · valoreNumero : NumeroTelefono |

## 8. Schema relazionale

    Stanza(id: serial, piano: IntegerGZ, settore: IntegerGZ)
      inclusione: id ⊆ Letto(stanza)

    Letto(id: serial, stanza: integer)
      foreign key: stanza references Stanza(id)

    Ricovero(id: serial, data: date, terminato: boolean, dimissione*: date,
             letto: integer, paziente: StringS, medico: integer)
      foreign key: letto references Letto(id)
      foreign key: paziente references Paziente(email)
      foreign key: medico references Medico(id)
      ennupla: terminato = true ↔ dimissione ≠ NULL
      ennupla: dimissione ≠ NULL → dimissione ≥ data

    Paziente(email: StringS, nome: StringS, cognome: StringS, nascita: date,
             via: StringM, civico*: IntegerGZ, CAP: CAP)
      inclusione: email ⊆ Telefono(paziente)
      chiave: (via, civico, CAP)

    Telefono(valorePrefisso: PrefissoTelefono, valoreNumero: NumeroTelefono,
             paziente: StringS)
      foreign key: paziente references Paziente(email)

    Prestazione(id: serial, descrizione: StringM, data: date, assegnata: boolean,
                medico*: integer, paziente: StringS, specializzazione: StringS)
      foreign key: medico references Medico(id)
      foreign key: paziente references Paziente(email)
      foreign key: specializzazione references Specializzazione(nome)
      ennupla: medico ≠ NULL ↔ assegnata = true

    Medico(id: serial, nome: StringS, cognome: StringS, nascita: date,
           specPrim: StringS)
      foreign key: specPrim references Specializzazione(nome)

    Specializzazione(nome: StringS)

    specSecon(medico: integer, specializzazione: StringS)
      foreign key: medico references Medico(id)
      foreign key: specializzazione references Specializzazione(nome)

Sottolineati sul foglio (quindi chiave): `Stanza.id`, `Letto.id`, `Ricovero.id`,
`Paziente.email`, `Prestazione.id`, `Medico.id`, `Specializzazione.nome`, tutta la relazione
`Telefono` e tutta `specSecon`. L'asterisco marca gli attributi che ammettono NULL.

## 9. Progettazione dei vincoli esterni (trigger)

### Vincolo `V.Stanza.maxLetti`

    Trigger:
      Operazioni intercettate: inserimento ennupla relazione Letto
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla da inserire
        Q =
          select count(*) < 8 as lettoAggiungibile
          from Stanza s
          where s.id = new.stanza
        IF il valore della colonna lettoAggiungibile di Q == true
          permetti l'operazione
        ELSE blocca l'operazione

### Vincolo `V.Medico.spec.disp` — due trigger

    Trigger (1):
      Operazioni intercettate: inserimento o modifica ennupla relazione Medico
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla da inserire o risultato modifica
        hasError = exists (
          select *
          from specSecon ss
          where ss.medico = new.id
            and ss.specializzazione = new.specPrim
        )
        IF hasError THEN blocca operazione
        ELSE permetti operazione

    Trigger (2):
      Operazioni intercettate: inserimento o modifica ennupla relazione specSecon
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla da inserire o risultato modifica
        hasError = exists (
          select *
          from Medico m
          where m.id = new.medico
            and m.specPrim = new.specializzazione
        )
        IF hasError THEN blocca operazione
        ELSE permetti operazione

### Vincolo `V.Ricovero.periodoStessoLetto`

    Trigger:
      Operazioni intercettate: inserimento o modifica ennupla relazione Ricovero
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla da inserire o risultato modifica
        hasError = exists (
          select *
          from Ricovero r
          where new.id <> r.id
            and new.letto = r.letto
            and (new.data, new.dimissione) overlaps (r.data, r.dimissione) );
        IF hasError THEN blocca operazione
        ELSE permetti operazione

### Vincolo `V.Ricovero.periodoStessoPaziente`

Identico al precedente con `new.paziente = r.paziente` al posto del letto.

### Vincolo `V.Persona.nascita.primaRicovero` — tre trigger

    Trigger (1):
      Operazioni intercettate: inserimento o modifica ennupla relazione Ricovero
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla da inserire o risultato modifica
        hasError = exists (
          select *
          from Medico m, Paziente p
          where new.paziente = p.email
            and new.data < p.nascita
             or new.medico = m.id
            and new.data < m.nascita );
        IF hasError THEN blocca operazione
        ELSE permetti operazione

    Trigger (2):
      Operazioni intercettate: modifica ennupla relazione Medico
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla risultante modifica
        hasError = exists (
          select *
          from Ricovero r
          where r.medico = new.id
            and r.data < new.nascita );
        IF hasError THEN blocca operazione
        ELSE permetti operazione

    Trigger (3):
      Operazioni intercettate: modifica ennupla relazione Paziente
      Istante di invocazione: prima operazione intercettata
      Funzione:
        new = ennupla risultante modifica
        hasError = exists (
          select *
          from Ricovero r
          where r.paziente = new.email
            and r.data < new.nascita );
        IF hasError THEN blocca operazione
        ELSE permetti operazione

### Vincolo `V.Persona.nascita.primaPrestazione`

Trigger analoghi a quelli di `V.Persona.nascita.primaRicovero`, sostituendo la relazione
`Ricovero` con la relazione `Prestazione`.

### Vincolo `V.Paziente.ricovPrestaz.almenoUno`

    Trigger:
      Operazioni intercettate: inserimento ennupla relazione Paziente
      Istante di invocazione: dopo operazione intercettata
      Funzione:
        new = ennupla da inserire
        hasError = not exists (
          select *
          from Ricovero r, Prestazione p
          where r.paziente = new.email
             or p.paziente = new.email );
        IF hasError THEN blocca operazione
        ELSE permetti operazione

## 10. Specifiche realizzative degli use-case

### Use-case `StrumentiPrestazioni`

**`mediciIdonei(p : integer) : Insieme(<id: integer, nome: StringS, cognome: StringS, nascita: date, specPrim: StringS>)`**

    res = risultato del comando SQL seguente sostituendo a ':p' il valore
          dell'omonimo parametro attuale
      select m.id, m.nome, m.cognome, m.nascita, m.specPrim
      from Medico m, Prestazione pr
      where :p = pr.id and pr.specializzazione = m.specPrim

    IF res == NULL THEN
      res = risultato del comando SQL seguente sostituendo a ':p' il valore del
            parametro attuale p
        select m.id, m.nome, m.cognome, m.nascita, m.specPrim
        from Medico m, Prestazione pr, specSecon ss
        where :p = pr.id
          and pr.specializzazione = ss.specializzazione
          and ss.medico = m.id

    IF res == NULL THEN genera l'errore 'non esistono medici con questa specializzazione'
    ELSE restituisci res

### Use-case `StrumentiMedici`

**`itinerarioVisite(m : integer) : Collezione(<piano: IntegerGZ, settore: IntegerGZ>)`**

    res = risultato del comando SQL seguente sostituendo a ':m' il valore del
          parametro attuale m
      select s.piano, s.settore
      from Stanza s, Ricovero r, Letto l
      where :m = r.medico
        and r.terminato = false
        and r.letto = l.id
        and l.stanza = s.id
      order by s.piano ASC, s.settore ASC;

    IF res == NULL THEN genera l'errore 'nessuna visita da mostrare'
    ELSE restituisci res

### Use-case `StrumentiRicoveri`

**`registraRicovero(p : integer, l : integer, m : integer) : integer`**

    IF DB.postiDisponibili(CURRENT_DATE) restituisce un errore
    THEN inoltra l'errore
    ELSE IF DB.postiDisponibili(CURRENT_DATE) < 1
    THEN termina con l'errore 'posti disponibili non sufficienti'
    res = risultato del comando SQL seguente sostituendo a ':p', ':l', ':m' i valori
          dei parametri
      insert into Ricovero(data, terminato, letto, paziente, medico)
      values (CURRENT_DATE, false, :l, :p, :m)
      returning id
    IF res rappresenta un errore THEN inoltra l'errore
    ELSE restituisci il valore della colonna 'id' dell'unica ennupla di res

**`dimissioneRicovero(r : integer)`**

    update Ricovero set terminato = true, dimissione = CURRENT_DATE
    where id = r;

### Funzioni definite nel DBMS

**`DB.postiDisponibili(d : date) : IntegerGEZ`**

    res = risultato della query SQL seguente sostituendo a ':d' il valore del
          parametro attuale d
      select x.postiTotali - y.postiOccupati as postiDisponibili
      from ( select count(*) as postiTotali
             from Letto ) x,
           ( select count(*) as postiOccupati
             from Ricovero r
             where (r.terminato = false
                and r.data <= :d)
                or (r.terminato = true
                and r.data <= :d
                and r.dimissione > :d) ) y

    IF res == NULL THEN genera l'errore 'non ci sono letti o ricoveri'
    ELSE restituisci la colonna 'postiDisponibili' dell'unica ennupla di res
