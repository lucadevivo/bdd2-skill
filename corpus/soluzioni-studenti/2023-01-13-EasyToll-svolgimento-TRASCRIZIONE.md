# EasyToll, prova del 13 gennaio 2023 — svolgimento di studente-B (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-B/EasyToll_EasyToll.pdf`, 29 pagine, modulo
> **`Versione 2024-06-05.UML`** compilato a stilo. Trascritto da Claude leggendo le pagine
> come immagini: **il documento è il PDF, questo è una copia a macchina e può contenere
> errori di lettura.** I punti dubbi sono marcati `[?]`.
>
> ✅ **Notazione attuale** (UML delle classi, alfabeto `C/1`, `assoc/2`, `attr/2`, `attr/3`,
> `op/(n+2)`), e **tutte e otto le domande sono svolte** — è il più completo del corpus.
> Traccia: `tracce-esame/BD2_2023-01-13_EasyToll.pdf`. Esiste anche la copia di studente-A
> (UML) e quella di studente-C (ER).
>
> **Non è una soluzione ufficiale e nessuno l'ha corretta.** In un punto lo dice lui stesso,
> a margine di un vincolo di inclusione: *«2 volte minimo, non so come dirlo»*.

---

## Domanda 1 — Raffinamento dei requisiti

1. **Autostrada**: 1.1 `codice` _(identificante)_ · 1.2 `nome` * · 1.3 località 1 ·
   1.4 località 2
2. **Casello**: 2.1 autostrada · 2.2 `nome` e 2.3 `codice` — **univoci nella rete** ·
   2.4 posizione · 2.5 volume traffico (veicoli/ora) · 2.6 pagamenti ammessi (telepass o
   no?) · 2.7 presenza servizio clienti · 2.8 tariffe
3. **Cliente telepass**: 3.1 nome · 3.2 cognome · 3.3 `CF` _(identificante)_ · 3.4 IBAN
4. **Tagliando**: 4.1 `COD` * · 4.2 classe veicolo

Annotazione sua in testa: *«pos. conf. ← una delle 2 definisce da dove si calcola la
distanza»*, con un abbozzo di diagramma a lato che lega `Autostrada`, `Casello`,
`terminale` e `t1`/`t2`.

## Domanda 2 — Diagramma UML concettuale delle classi

### Classi

| Classe | Attributi | Operazioni |
|---|---|---|
| `ClienteTelepass` | nome : Stringa · cognome : Stringa · codFis : CF `{id}` · Iban : IBAN | |
| `Autostrada` | codice : COD `{id}` · nome : Stringa `[0..1]` | |
| `Casello` | nome : Stringa `{id}` · codCasello : COD `{id}` · volumeMax : Intero ≥ 0 · servizio : bool · posKM : Reale ≥ 0 `{id2}` | |
| `CaselloTelepass` | _(nessun attributo)_ | |
| `Localita'` | nome : Stringa `{id}` | |
| `Pagamento` | nome : Stringa `{id}` | |
| `Tagliando` | senso : bool · codice : COD `{id}` | `costo() : Reale ≥ 0` |
| `Veicolo` | targa : Targa `{id}` | |
| `ClasseVeicolo` | nome : Stringa `{id}` | |
| `Tutor` | posInizioKM : Reale ≥ 0 · posFineKM : Reale ≥ 0 | `senso() : booleano` |
| `Rilevazione` | istInizio : DataOra · istFine : DataOra | `velocita() : Reale > 0` |

Tre **classi associative**: `entrata` e `uscita` (entrambe con `ist : DataOra`, sulla
`Tagliando`–`Casello`), `tariffa` (`euroKM : Reale ≥ 0`, sulla `Autostrada`–`ClasseVeicolo`)
e `velocitaMax` (`vel : Intero > 0`, sulla `Tutor`–`ClasseVeicolo`).

### Associazioni

| Associazione | Classe A | mult. A | mult. B | Classe B |
|---|---|---|---|---|
| `cli_tel` | ClienteTelepass | `0..1` | `0..*` | Tagliando |
| `tag_vei` | Tagliando | `0..*` | `1..1` | Veicolo |
| `entrata` | Tagliando | `0..*` | `1..1` | Casello |
| `uscita` | Tagliando | `0..*` | `0..1` | Casello |
| `aut_cas` | Autostrada | `1..1 {id}{id1}{id2}` | `2..*` | Casello |
| `cas_pay` | Casello | `0..*` | `1..*` | Pagamento |
| `cas_loc` | Casello | `0..*` | `1..1` | Localita' |
| `aut_tut` | Autostrada | `1..1` | `0..*` | Tutor |
| `tut_ril` | Tutor | `1..1` | `0..*` | Rilevazione |
| `ril_vei` | Rilevazione | `0..*` | `1..1` | Veicolo |
| `cla_vei` | ClasseVeicolo | `1..1` | `0..*` | Veicolo |
| _(tariffa)_ | Autostrada | `0..*` | `1..*` | ClasseVeicolo |
| _(velocitaMax)_ | Tutor | `0..*` | `1..*` | ClasseVeicolo |

### Generalizzazioni

- `Casello` generalizza `CaselloTelepass`

## Specifiche delle classi e delle associazioni

**1 · Classe `Rilevazione` — [V.coerenza_rilevazione], caso `senso = True`**

    ∀r,ir,fr,v,t,it,ft
      [ Rilevazione(r) ∧ istInizio(r,ir) ∧ istFine(r,fr) ∧ ril_vei(r,v) ∧ tut_ril(r,t) ∧
        posInizioKM(t,it) ∧ posFineKM(t,ft) ∧ senso(t,true) ] →
      [ ∃tag,c,iec,pe
        Tagliando(tag) ∧ senso(tag,true) ∧ tag_vei(tag,v) ∧ Casello(c) ∧ entrata(tag,c) ∧
        iec ≤ ir ∧ ist(tag,c,iec) ∧ posKM(c,pe) ∧ pe ≤ it ∧
        [ ∃c2,iuc,pu Casello(c2) ∧ posKM(c2,pu) ∧ uscita(tag,c2) ∧ ist(tag,c2,iuc) ] →
        [ iuc ≥ fr ∧ pu ≥ ft ] ]

**2 · Classe `Rilevazione`**

    [V.rilevato_veicolo_classe]
    ∀r,v,t,c [ Rilevazione(r) ∧ ril_vei(r,v) ∧ cla_vei(v,c) ∧ tut_ril(t,r) ] →
             velocitaMax(t,c)

    [V.inizio_poi_fine]
    ∀r,i,f [ Rilevazione(r) ∧ inizio(r,i) ∧ fine(r,f) ] → i < f

**3 · Classe `Tagliando`**

    [V.senso_di_marcia]
    ∀t,ce,cu,pe,pu [ Tagliando(t) ∧ entrata(t,ce) ∧ uscita(t,cu) ∧
                     posKM(ce,pe) ∧ posKM(cu,pu) ] → [ senso(t,True) ↔ pe < pu ]

    [V.tagliando_classe_veicolo]
    ∀t,v,a,cl [ Tagliando(t) ∧ tag_vei(t,v) ∧ [ entrata(t,c) ∨ uscita(t,c) ] ∧
                cla_vei(v,cl) ∧ aut_cas(a,c) ] → tariffa(a,cl)

**4 · Classe `Tagliando` — operazione `costo()`**

    costo() : Reale ≥ 0
      • pre-cond: ∃u uscita(this,u)
      • post-cond: sia tar :=
          ∃c,a,v,cl  tag_vei(this,v) ∧ [ entrata(this,c) ∨ uscita(this,c) ] ∧
                     aut_cas(c,a) ∧ tariffa(a,cl) ∧ cla_vei(cl,v) ∧ euroKM(a,cl,tar)
        siano p1,p2 :=
          ∃c1,c2  entrata(this,c1) ∧ posKM(c1,p1) ∧ uscita(this,c2) ∧ posKM(c2,p2)
        Result = |p1 − p2| · tar

**5 · Classe `Tutor` — [V.no_intersezioni_tutor]**

    ∀t1,t2,e1,u1,e2,u2,a
      [ Tutor(t1) ∧ Tutor(t2) ∧ aut_tut(a,t1) ∧ aut_tut(a,t2) ∧
        posInizioKM(t1,e1) ∧ posFineKM(t1,u1) ∧ posInizioKM(t2,e2) ∧ posFineKM(t2,u2) ∧
        u1 > e1 ∧ u2 > e2 ∧ senso(t1,true) ∧ senso(t2,true) ] → [ u2 < e1 ∨ u1 < e2 ]

    ∀t1,t2,e1,u1,e2,u2,a
      [ Tutor(t1) ∧ Tutor(t2) ∧ aut_tut(a,t1) ∧ aut_tut(a,t2) ∧
        posInizioKM(t1,e1) ∧ posFineKM(t1,u1) ∧ posInizioKM(t2,e2) ∧ posFineKM(t2,u2) ∧
        u1 < e1 ∧ u2 < e2 ∧ senso(t1,false) ∧ senso(t2,false) ] → [ u2 > e1 ∨ u1 > e2 ]

**6 · Classe `Tagliando`**

    [V.entra_poi_esce]
    ∀t,c1,c2,e,u [ Tagliando(t) ∧ entrata(t,c1) ∧ uscita(t,c2) ∧
                   ist(t,c2,u) ∧ ist(t,c1,e) ] → e < u

    [V.casello_telepass]
    ∀t,c [ Tagliando(t) ∧ [ entrata(t,c) ∨ uscita(t,c) ] ∧ ∃cl cli_tal(cl,t) ] →
          CaselloTelepass(c)

**7 · Classe `Tutor`**

    senso() : bool
      • pre-cond: nessuna
      • post-cond: siano i,F :=  posInizioKM(this,i) ∧ posFineKM(this,F)
          i < F → Result = True    ∧    i > F → Result = False

    [V.compreso_in_autostrada]
    ∀t,a,et,ut [ Tutor(t) ∧ posInizioKM(t,et) ∧ posFineKM(t,ut) ∧ aut_tut(a,t) ] →
      [ ∃c1,c2,e,u  aut_cas(a,c1) ∧ aut_cas(a,c2) ∧ posKM(c1,u) ∧ posKM(c2,e) ∧
        e ≤ et ∧ u ≥ ut ]

**8 · Classe `Rilevazione` — operazione `velocita()`**

    velocita() : Reale ≥ 0
      • pre-cond: nessuna
      • post-cond: siano pi, pF, ii, iF tali da soddisfare:
          istInizio(this,ii) ∧ istFine(this,iF) ∧ ∃t tut_ril(this,t) ∧
          posInizioKM(t,pi) ∧ posFineKM(t,pF)
        sia σ := oreTrascorse(ii, iF, σ)      ← semantica di mondo reale
        Result = |pi − pF| / σ

## Ulteriori vincoli esterni e tipi di dato

    [V.no_tagliandi_che_si_intersecano]
    ∀v,t1,t2,e1,e2
      [ Tagliando(t1) ∧ Tagliando(t2) ∧ tag_vei(t1,v) ∧ tag_vei(t2,v) ∧
        ∃c entrata(t1,c) ∧ t1 ≠ t2 ∧ ist(t1,c,e1) ∧ ∃k entrata(t2,k) ∧ ist(t2,k,e2) ] →
      ¬∃t [ t ≥ e1 ∧ [ ∀u,tu uscita(t1,u) ∧ ist(t1,u,tu) → tu ≥ t ] ∧
            t ≥ e2 ∧ [ ∀u,tu uscita(t2,u) ∧ ist(t1,u,tu) → tu ≥ t ] ]

    [V.no_rilevazioni_che_si_intersecano]
    ∀r1,r2,i1,i2,f1,f2,v
      [ Rilevazione(r1) ∧ Rilevazione(r2) ∧ istInizio(r1,i1) ∧ istInizio(r2,i2) ∧
        istFine(r1,f1) ∧ istFine(r2,f2) ∧ ril_vei(r1,v) ∧ ril_vei(r2,v) ∧ r1 ≠ r2 ] →
      [ f1 < i2 ∨ f2 < i1 ]

    [V.no_tagliandi_che_si_intersecano_cli]
    — identico al primo, con `cli_tal(t1,c)` e `cli_tal(t2,c)` al posto di `tag_vei`

    [V.tagliando_caselli_stessa_autostrada]
    ∀t,e,u [ Tagliando(t) ∧ entrata(t,e) ∧ uscita(t,u) ] →
           ∃a  aut_cas(a,e) ∧ aut_cas(a,u)

    [V.coerenza_rilevazione], caso `senso = False`
    — speculare al caso `True` della casella 1: `iuc ≥ fr ∧ pu ≤ ft`

### Tipi di dato (espressioni regolari)

    COD   = [A-Z0-9]+
    IBAN  = [A-Z]{2}[0-9]{2}[A-Z][0-9]{22}
    CF    = [A-Z]{6}[0-9]{2}[A-Z][0-9]{12}[A-Z][0-9]{3}[A-Z]
    Targa = [A-Z]{2}[0-9]{3}[A-Z]{2}

## Domanda 3 — Diagramma UML degli use-case

| Attore | Use-case |
|---|---|
| `SistemaFatturazione` | `CalcoloConto` |
| `Casello` | `RegistraTagliando` |
| `CaselloTelepass` → generalizza `Casello` | `Reg. Tagl. Virtuale` |
| `Tutor` | `Rilevazione` |

## Domanda 5 — Specifiche delle operazioni di use-case

**`calcola_conto(c : ClienteTelepass, m : 1..12, anno : Intero ≥ 0) : (Stringa, Stringa, DataOra, DataOra, Reale ≥ 0) [0..*]`**

- pre-cond: nessuna
- post-cond:

      C = { (ne, nu, de, du, im)  |
            ∃t Tagliando(t) ∧ cli_tal(c,t) ∧ ∃ce,cu entrata(t,ce) ∧ uscita(t,cu) ∧
            nome(ce,ne) ∧ nome(cu,nu) ∧ ist(t,ce,de) ∧ ist(t,cu,du) ∧
            Mese(de,m) ∧ Mese(du,m) ∧ Anno(de,anno) ∧ Anno(du,anno) ∧ costo(t,im) }
      Result = C

**`rileva_passaggio(t : Tutor, i : DataOra, f : DataOra, v : Veicolo) : Rilevazione`**

- pre-cond: `∃cl ClasseVeicolo(cl) ∧ cla_vei(v,cl) ∧ velocitaMax(t,cl)`
- post-cond: sia `α` un nuovo oggetto del dominio tale che

      Rilevazione(α) ∧ istInizio(α,i) ∧ istFine(α,f) ∧ ril_vei(α,v) ∧ tut_ril(α,t)

  sia `vMax` tale che
  `∃cl ClasseVeicolo(cl) ∧ cla_vei(v,cl) ∧ velocitaMax(t,cl) ∧ vel(t,cl,vMax)`
  sia `vel` tale che `velocita(α,vel)`

  - se `vel ≤ vMax`: termina l'operazione e `α` viene cancellato
  - se `vel > vMax`: `α` è un nuovo oggetto del dominio, `M_out = M_in ∪ {α}`

## Domanda 6 — Ristrutturazione

**DBMS: PostgreSQL.**

```sql
create domain COD as varchar ~ '[A-Z0-9]+';
create domain IBAN as varchar ~ '[A-Z]{2}[0-9]{2}[A-Z][0-9]{22}';
create domain Real_GEZ as Real check (value >= 0);
create domain Int_GEZ as Integer check (value >= 0);
create domain CF as varchar ~ '[A-Z]{6}[0-9]{2}[A-Z][0-9]{12}[A-Z][0-9]{3}[A-Z]';
create domain Stringa as varchar NOT NULL;
create domain Targa as varchar ~ '[A-Z]{2}[0-9]{3}[A-Z]{2}';
create domain Mese as Integer check (value >= 1 AND value <= 12);
```

**Descrizione delle scelte:** *«Fusione su Casello.»* — cioè la sottoclasse
`CaselloTelepass` viene fusa nel padre, che prende l'attributo booleano `telepass`.

**Diagramma ristrutturato — cosa cambia:** `Casello` prende `id : serial {id3}` e
`telepass : bool`; `Tutor` prende `id : serial {id}` e `senso : bool` come attributo (non
più operazione); `Rilevazione` prende `id : serial {id}`; le classi associative `entrata` e
`uscita` restano; i domini passano ai nomi SQL (`Int_GEZ`, `Real_GEZ`, `DateTime`).

**Vincolo introdotto:**

    [V.casello_telepass]
    ∀t,c [ Tagliando(t) ∧ [ entrata(t,c) ∨ uscita(t,c) ] ∧ Casello(c) ∧
           ∃cl cli_tal(cl,t) ] → [ telepass(c,True) ]

## Domanda 7 — Schema relazionale

Chiave primaria sottolineata, `*` = ammette NULL.

     1  ClasseVeicolo(nome: Stringa)                                       [da classe]

     2  Veicolo(targa: Targa, classe: Stringa)                             [da classe]
          foreign key: classe references ClasseVeicolo(nome)
          accorpa: cla_vei

     3  Autostrada(codice: COD, nome*: Stringa)                            [da classe]

     4  Localita(nome: Stringa)                                            [da classe]

     5  Casello(nome: Stringa, codCasello: COD, volumeMax: Int_GEZ, servizio: bool,
                posKM: Real_GEZ, id: serial, telepass: bool, localita: Stringa)
          foreign key: localita references Localita(nome)
          inclusione: Casello(id) ⊆ cas_pay(casello)
          accorpa: cas_loc

     6  aut_cas(autostrada: COD, casello: Integer)                     [da associazione]
          inclusione: Casello(id) ⊆ aut_cas(casello)
          inclusione: Autostrada(codice) ⊆ aut_cas(autostrada)

> ✍️ **Annotazione sua, in arancione, accanto a questo secondo vincolo:** *«2 volte minimo,
> non so come dirlo»*. Ha ragione a segnarselo: la traccia chiede che ogni autostrada abbia
> **almeno due** caselli (`2..*` nel diagramma), e un vincolo di inclusione garantisce
> «almeno uno», non «almeno due». Serviva un vincolo esterno con un trigger.

     7  Pagamento(nome: Stringa)                                           [da classe]

     8  cas_pay(casello: Integer, pagamento: Stringa)                  [da associazione]
          foreign key: casello references Casello(id)
          foreign key: pagamento references Pagamento(nome)

     9  ClienteTelepass(nome: Stringa, cognome: Stringa, codFis: CF, iban: IBAN)

    10  Tagliando(senso: bool, codice: COD, cliente*: CF, veicolo: Targa,
                  entrata: Integer, istE: DateTime, uscita*: Integer, istU*: Integer)
          foreign key: cliente references ClienteTelepass(codFis)
          foreign key: veicolo references Veicolo(targa)
          foreign key: entrata references Casello(id)
          foreign key: uscita references Casello(id)
          check(istE < istU)
          check((istU is NULL AND uscita is NULL) OR (istU is NOT NULL AND uscita is NOT NULL))
          accorpa: cli_tel, tag_vei, entrata, uscita

    11  tariffa(autostrada: COD, classe: Stringa, euroKM: Real_GEZ)   [da associazione]
          foreign key: autostrada references Autostrada(codice)
          foreign key: classe references ClasseVeicolo(nome)

    12  Tutor(posInizioKM: Real_GEZ, posFineKM: Real_GEZ, id: serial,
              autostrada: COD, senso: bool)                                [da classe]
          foreign key: autostrada references Autostrada(codice)
          check(posInizioKM <> posFineKM)
          check((senso = True AND posInizioKM < posFineKM) OR
                (senso = False AND posInizioKM > posFineKM))
          accorpa: aut_tut

    13  Rilevazione(id: serial, istInizio: DateTime, istFine: DateTime,
                    tutor: Integer, veicolo: Targa)                        [da classe]
          check(istInizio < istFine)
          foreign key: tutor references Tutor(id)
          foreign key: veicolo references Veicolo(targa)
          accorpa: tut_ril, ril_vei

    14  velocitaMax(tutor: Integer, classe: Stringa, vel: Int_GEZ)    [da associazione]
          foreign key: tutor references Tutor(id)
          foreign key: classe references ClasseVeicolo(nome)
          inclusione: Tutor(id) ⊆ velocitaMax(tutor)

## Ulteriori vincoli esterni — trigger

**`T.coerenza_rilevazione`** — `Insert` o `Update` su `Rilevazione`

    OK = EXISTS ( SELECT *
      FROM Tagliando t, Casello c_ent, aut_cas ac, Tutor tut, Casello c_usc
      WHERE new.veicolo = t.veicolo AND t.entrata = c_ent.id AND ac.casello = c_ent.id
        AND ac.autostrada = tut.autostrada AND tut.id = new.tutor
        AND t.senso = tut.senso AND new.istInizio >= t.istE
        AND (( t.senso = True  AND c_ent.posKM < tut.posInizioKM) OR
             ( t.senso = False AND c_ent.posKM > tut.posInizioKM))
        AND ( t.uscita IS NULL OR ( t.uscita = c_usc.id AND new.istFine <= t.istU
        AND (( t.senso = True  AND c_usc.posKM > tut.posFineKM) OR
             ( t.senso = False AND c_usc.posKM < tut.posFineKM)))));
    if OK = True: commit  else: errore e rollback

**`T.senso_di_marcia`** — `Insert` o `Update` su `Tagliando`

    Error = EXISTS ( SELECT * FROM Casello e, Casello u
      WHERE new.entrata = e.id AND new.uscita = u.id
        AND ((new.senso = True  AND u.posKM < e.posKM)
          OR (new.senso = False AND u.posKM > e.posKM)));
    if Error: rollback  else: commit

**`T.no_tagliandi_che_si_intersecano`** — `Insert` o `Update` su `Tagliando`

    Error = EXISTS ( SELECT * FROM Tagliando t
      WHERE (t.cliente = new.cliente OR t.veicolo = new.veicolo)
        AND (new.istE, new.istU) OVERLAPS (t.istE, t.istU));

**`T.casello_telepass`** — `Insert` o `Update` su `Tagliando`

    OK = EXISTS ( SELECT * FROM Casello ce, Casello cu
      WHERE (new.entrata = ce.id AND ce.telepass = True
        AND (new.uscita IS False OR (new.uscita = cu.id AND cu.telepass = True)))
        OR new.cliente IS NULL);

**`T.tagliando_classe_veicolo`** — `Insert` o `Update` su `Tagliando`

    OK = EXISTS ( SELECT * FROM Casello c, tariffa t, aut_cas ac, Veicolo v
      WHERE c.id = new.entrata AND ac.casello = c.id AND ac.autostrada = t.autostrada
        AND t.classe = v.classe AND v.targa = new.veicolo);

**`T.no_intersezioni_tutor`** — `Insert` o `Update` su `Tutor`

    Error = EXISTS ( SELECT * FROM Tutor t
      WHERE t.autostrada = new.autostrada AND t.senso = new.senso
        AND (new.posInizioKM, new.posFineKM) OVERLAPS (t.posInizioKM, t.posFineKM));

**`T.no_rilevazioni_che_si_intersecano`** — `Insert` o `Update` su `Rilevazione`

    Error = EXISTS ( SELECT * FROM Rilevazione r
      WHERE r.veicolo = new.veicolo
        AND (new.istInizio, new.istFine) OVERLAPS (r.istInizio, r.istFine));

**`T.tagliando_caselli_stessa_autostrada`** — `Insert` o `Update` su `Tagliando`

    Error = EXISTS ( SELECT FROM Casello e, Casello u, aut_cas ace, aut_cas acu
      WHERE e.id = new.entrata AND u.id = new.uscita
        AND ace.casello = e.id AND acu.casello = u.id
        AND ace.autostrada <> acu.autostrada);

**`T.compreso_in_autostrada`** — `Insert` o `Update` su `Tutor`

    OK = EXISTS ( SELECT FROM Casello e, Casello u, aut_cas ce, aut_cas cu
      WHERE ce.autostrada = cu.autostrada = new.autostrada
        AND ce.casello = e.id AND cu.casello = u.id
        AND ((new.senso = True  AND e.posKM <= new.posInizioKM AND u.posKM >= new.posFineKM)
          OR (new.senso = False AND e.posKM >= new.posInizioKM AND u.posKM <= new.posFineKM)));

## Domanda 8 — Specifiche realizzative

**`create function costo(tg : COD) : Real_GEZ`**

    Error = EXISTS (SELECT * FROM Tagliando WHERE id = tg AND uscita IS NULL);
    if (Error = true): termina operazione

    Q = SELECT (tariffa.euroKM * ABS(e.posKM − u.posKM))
        FROM Casello e, Casello u, Tagliando t, Autostrada a, Veicolo v,
             ClasseVeicolo vc, tariffa, aut_cas
        WHERE t.codice = tg AND t.entrata = e.id AND t.uscita = u.id
          AND v.targa = t.veicolo AND vc.nome = v.classe AND tariffa.classe = v.classe
          AND e.id = aut_cas.casello AND aut_cas.autostrada = a.codice;
    result = Q

**`create function velocita(ril : Integer) : Real_GEZ`**

    V = SELECT ABS(t.posKMInizio − posKMFine) /
               (EXTRACT(EPOCH FROM (r.istFine − r.istInizio)) / 3600)
        FROM Rilevazione r, Tutor t
        WHERE r.id = ril AND t.id = r.tutor;
    result = V

**`calcola_conto(cl : CF, m : Mese, anno : Intero >= 0) : Insieme(<Stringa, Stringa, DateTime, DateTime, Real_GEZ>)`**

    Q = SELECT e.nome, u.nome, istE, istU, costo(t.cod)
        FROM Tagliando t, Casello e, Casello u
        WHERE t.cliente = cl
          AND EXTRACT('month' FROM istE) = m AND EXTRACT('month' FROM istU) = m
          AND EXTRACT('year'  FROM istE) = anno AND EXTRACT('year' FROM istU) = anno
          AND t.entrata = e.id AND t.uscita = u.id;
    result = Q

**`rileva_passaggio(tut : Integer, i : DateTime, f : DateTime, vt : Targa) : Integer [0..1]`**

    OK = EXISTS (SELECT * FROM velocitaMax vm, Veicolo v
                 WHERE vm.tutor = tut AND vm.classe = v.classe AND v.targa = vt);
    if (OK = False): termina operazione

    ril = Insert INTO Rilevazione(i, f, tut, vt) returning id;

    D = EXISTS ( WITH V as (SELECT vel FROM velocitaMax vm, Veicolo v
                            WHERE v.targa = vt AND v.tutor = tut)
                 SELECT * FROM Rilevazione r, V
                 WHERE V.vel >= velocita(r.id) AND r.id = ril);

    if (D == True): DELETE FROM Rilevazione WHERE id = ril;
    else: result = ril

---

## Come usarlo

È lo svolgimento più **completo** del corpus in notazione attuale: tutte e otto le domande,
con il ciclo intero dal raffinamento dei requisiti fino alle funzioni SQL. Vale soprattutto
per vedere **come si distribuisce il tempo** fra le domande e come si tiene la coerenza fra
i tre livelli — vincolo in FOL, vincolo nello schema, trigger che lo implementa: qui gli
stessi vincoli (`no_intersezioni`, `senso_di_marcia`, `casello_telepass`,
`compreso_in_autostrada`) compaiono in tutti e tre, e si vede il passaggio.

**Non è corretto da nessuno.** Un punto lo segnala lui: il vincolo «almeno due caselli per
autostrada» reso con un'inclusione, che garantisce solo «almeno uno».
