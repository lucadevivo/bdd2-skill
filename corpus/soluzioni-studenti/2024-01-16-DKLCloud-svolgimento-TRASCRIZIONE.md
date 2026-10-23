# DKLCloud, prova del 16 gennaio 2024 — svolgimento di studente-B (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-B/altra roba_DKL.pdf`, 28 pagine, modulo
> **`Versione 2024-06-05.UML`** compilato a stilo. Trascritto da Claude leggendo le pagine
> come immagini: **il documento è il PDF, questo è una copia a macchina e può contenere
> errori di lettura.** I punti dubbi sono marcati `[?]`.
>
> ⚠️ **Svolgimento parziale.** Solo la **Domanda 2** (diagramma delle classi e specifiche)
> e la **Domanda 5** (operazioni di use-case) sono state fatte: 4 pagine su 28 hanno
> inchiostro. Domande 1, 3, 4, 6, 7, 8 in bianco. È l'unica copia che abbiamo di questa
> prova.
>
> Traccia: `tracce-esame/BD2_2024-01-16_DKLCloud.pdf`. **Non è una soluzione ufficiale e
> nessuno l'ha corretta.**

---

## Domanda 2 — Diagramma UML concettuale delle classi

### Classi

| Classe | Attributi | Operazioni |
|---|---|---|
| `Continente` | nome : Stringa `{id}` | |
| `Nazione` | nome : Stringa `{id}` | |
| `Citta` | nome : Stringa `{id}` | |
| `Utente` | codice : COD `{id}` | |
| `Privato` | nome : Stringa · cognome : Stringa | |
| `Commerciale` | ragione : Stringa | |
| `Carta` | scad : Data · titolare : Stringa · numero : NumCarta | |
| `Tariffa` | peso : Range `{id}` · def : Data `{id}` · prezzo : Valuta | |
| `Spedizione` | oraRitiro : Ora · istSped : DataOra · pesoKG : Reale ≥ 0 · importoAssicurato : Valuta | `prezzo() : Valuta` |
| `InCarico` | _(nessun attributo)_ | |
| `SpedConsegnata` | istCons : DataOra | |
| `Corriere` | nome : Stringa | |
| `Depot` | _(nessun attributo)_ | |
| `Mezzo` | _(nessun attributo)_ | |
| `TipoMezzo` | nome : Stringa `{id}` | |

Classi associative: **`ritira`** (`indirizzo : Ind`), **`spedisce`** (senza attributi) e
**`spe_dep`** (`inizio : DataOra`, `fine : DataOra`).

Fra `Utente` e `Spedizione` ci sono **due** associazioni, `ritira` e `spedisce`, ed
entrambe sono classi associative: da `ritira` parte `rit_cit` verso la città di ritiro, da
`spedisce` partono `spe_cit` verso la città di spedizione e `spe_car` verso la carta usata.
È il motivo per cui nella Domanda 5 compare `spe_cit(this,u,c)` con **tre** argomenti: il
legame parte da una coppia (spedizione, utente), non da una spedizione sola.

### Associazioni

| Associazione | Classe A | mult. A | mult. B | Classe B |
|---|---|---|---|---|
| `con_naz` | Continente | `1..1 {id}` | `0..*` | Nazione |
| `cit_naz` | Nazione | `1..1 {id}` | `0..*` | Citta |
| `rit_cit` | Citta | `1..1` | `0..*` | ritira |
| `spe_cit` | Citta | `1..1` | `0..*` | spedisce |
| `ute_car` | Utente | `0..*` | `0..*` | Carta |
| `spe_car` | spedisce _(classe assoc.)_ | `0..*` | `1..1` | Carta |
| `spedisce` | Utente | `1..1` | `0..*` | Spedizione |
| `ritira` | Utente | `1..1` | `0..*` | Spedizione |
| `cor_spe` | Corriere | `1..1` | `0..*` | InCarico |
| `spe_dep` | Spedizione | `0..*` | `0..*` | Depot |
| `spe_mez` | spe_dep | `0..*` | `1..1` | Mezzo |
| `mez_tip` | Mezzo | `0..*` | `1..1` | TipoMezzo |
| `cit_dep` | Depot | `0..*` | `1..1` | Citta |

### Generalizzazioni

- `Utente` generalizza `Privato` e `Commerciale`, con vincolo **`{complete, disj}`**
- `Spedizione` generalizza `InCarico`, che a sua volta generalizza `SpedConsegnata`
  (catena di due livelli, con le frecce a triangolo vuoto in fila)

## Specifiche delle classi e delle associazioni

**1 · Classe `Spedizione`**

    [V.istante_depot]
    ∀s,d,is,id [ Spedizione(s) ∧ Depot(d) ∧ spe_dep(s,d) ∧ istSped(s,is) ∧
                 [ Inizio(s,d,id) ∨ Fine(s,d,id) ] ] →
      id ≥ is ∧ [ ∀k istCons(s,k) → k > id ]

    [V.spedito_poi_ritirata]
    ∀s,is,ir [ istSped(s,is) ∧ istCons(s,ir) ] → ir > is

    [V.continuita_depot]
    ∀s,d,i,F [ spe_dep(s,p) ∧ inizio(s,p,i) ∧ Fine(s,p,i) ] → i < F

**2 · Classe `Mezzo` — [V.mezzi_non_si_sdoppiano]**

    ∀s1,d1,s2,d2,i1,i2,F1,F2,m1,m2
      [ s1 ≠ s2 ∧ Spedizione(s1) ∧ Spedizione(s2) ∧ Depot(d1) ∧ Depot(d2) ∧
        spe_dep(s1,d1) ∧ spe_dep(s2,d2) ∧ spe_mez(s1,d1,m1) ∧ spe_mez(s2,d2,m2) ∧
        inizio(s1,d1,i1) ∧ inizio(s2,d2,i2) ∧ Fine(s1,d1,F1) ∧ Fine(s2,d2,F2) ∧
        ∃t DataOra(t) ∧ i1 ≤ t ≤ F1 ∧ i2 ≤ t ≤ F2 ] → m1 ≠ m2

**3 · Classe `Utente`**

    [V.usa_carta_valida]
    ∀u,s,c,is,ds [ Spedizione(s) ∧ Utente(u) ∧ spedisce(s,u) ∧ Carta(c) ∧ spe_car(s,u,c) ∧
                   istSped(s,is) ∧ Data(is,ds) ] →
      [ ∃dsc scad(c,dsc) ∧ dsc > ds ∧ ute_car(c,u) ]

    [V.no_auto_spedizioni]
    ∀s,u1,u2 [ Spedizione(s) ∧ ritira(s,u1) ∧ spedisce(s,u2) ] → u1 ≠ u2

**4 · Associazione `spe_dep` — [V.no_tratte_che_si_intersecano]**

    ∀s,d1,d2,i1,i2,f1,f2 [ Spedizione(s) ∧ spe_dep(s,d1) ∧ spe_dep(s,d2) ∧
                           inizio(s,d1,i1) ∧ inizio(s,d2,i2) ∧ Fine(s,d1,f1) ∧
                           Fine(s,d2,f2) ∧ d1 ≠ d2 ] → f1 < i2 ∨ f2 < i1

**6 · Classe `Spedizione` — operazione `prezzo()`**

    prezzo() : Valuta
      • pre-cond: nessuna
      • post-cond: siano pr, ia tali da soddisfare:

          importoAssicurato(this,ia) ∧ ∃t,r,dt,i,F,k  Tariffa(t) ∧ def(t,dt) ∧
          prezzo(t,pr) ∧ peso(t,r) ∧ da(r,i) ∧ a(r,F) ∧ pesoKG(this,k) ∧ i ≤ k ≤ F ∧
          ∃is,ds istSped(this,is) ∧ Data(is,ds) ∧ ds ≥ dt

          ∧ [ ∀t',r',dt',i',f'  def(t',dt') ∧ Tariffa(t') ∧ peso(t',r') ∧ da(r',i') ∧
              a(r',f') ∧ pesoKG(this,k) ∧ i' ≤ k ≤ f' ∧ ds ≥ dt' → dt' < dt ]

        Result = pr + ia · 0.1

> La seconda parte è il modo di dire «fra tutte le tariffe applicabili prendi **la più
> recente** fra quelle già in vigore alla data della spedizione». È lo stesso schema
> `¬∃ qualcosa di più recente` che compare in CozyRooms per il livello di fedeltà: vale la
> pena impararlo, torna in quasi tutte le tracce.

## Domanda 5 — Specifiche delle operazioni di use-case

**`traccia_sped(s : Spedizione) : ((Depot, DataOra, Mezzo)[0..*], Corriere [0..1])`**

- pre-cond: nessuna
- post-cond:

      D = { (d,i,m) | Depot(d) ∧ spe_dep(this,d) ∧ inizio(s,d,i) ∧ spe_mez(s,d,m) }

      C è tale che:
        InCarico(this)  → cor_spe(this,C)
        ¬InCarico(this) → C = NULL

      DS = Sorted(D, ordina)
      Result = DS ∪ C

**`ordina(a : (d : Depot, i : DataOra, m : Mezzo), b : (d : Depot, i : DataOra, m : Mezzo)) : bool`**

- pre-cond: nessuna
- post-cond: siano `ia, ib` tali che `i(a,ia) ∧ i(b,ib)`

      ia ≥ ib → Result = True
      ia < ib → Result = False

**`redditivita_continenti(c1 : Continente, c2 : Continente, i : DataOra, F : DataOra) : Valuta`**

- pre-cond: `i < F ∧ c1 ≠ c2`
- post-cond:

      S = { (s,v) | Spedizione(s) ∧ ∃is istSped(s,is) ∧ i ≤ is ≤ F ∧
                    ∃u,c,n,u',c',n'  spedisce(this,u) ∧ spe_cit(this,u,c) ∧
                    cit_naz(c,n) ∧ con_naz(c1,n) ∧ ritira(this,u') ∧
                    spe_cit(this,u',c') ∧ cit_naz(c',n') ∧ con_naz(c2,n') }

      |S| = 0 → Result = 0
      |S| ≠ 0 → Result = Σ_{(s,v) ∈ S} v · 1/|S|

---

## Come usarlo

Vale per due cose sole, ma buone:

1. **la catena di generalizzazioni a due livelli** — `Spedizione` → `InCarico` →
   `SpedConsegnata` — che è un modo di modellare uno stato che avanza, alternativo agli
   attributi booleani che usa in CozyRooms;
2. **lo schema «prendi il più recente»** dentro `prezzo()`: si sceglie la tariffa giusta
   dicendo che *non ne esiste una più recente ancora applicabile*. È il pattern che ricorre
   in quasi tutte le tracce (sconto, tariffa, listino) e che in FOL si scrive sempre così.

Per il resto è **incompleta**: dalla Domanda 6 in poi non c'è niente.
