# CozyRooms, prova dell'11 settembre 2023 — svolgimento di studente-B (trascrizione)

> **Fonte:** `05-soluzioni-studenti/studente-B/altra roba_CozyRooms.pdf`, 28 pagine, modulo
> **`Versione 2024-06-05.UML`** compilato a stilo (inchiostro vettoriale). Trascritto da
> Claude leggendo le pagine come immagini: **il documento è il PDF, questo è una copia a
> macchina e può contenere errori di lettura.** I punti dubbi sono marcati `[?]`.
>
> ✅ **Notazione attuale.** Diagramma UML delle classi, alfabeto della logica del nuovo
> modulo (`C/1`, `assoc/2`, `attr/2`, `attr/3`, `op/(n+2)`). È quella che ti serve.
>
> La traccia è `tracce-esame/BD2_2023-09-11_CozyRooms.pdf` — la stessa della simulazione
> del Giorno 9. Esiste anche la copia di studente-A, pure in UML, e quella di studente-C in
> ER: si possono confrontare.
>
> **Non è una soluzione ufficiale e non è corretta da nessuno.** In un punto lo dice lui
> stesso: sul trigger `T.tariffa_per_ogni_posto` ha scritto a margine *«so che è sbagliata
> ma il concetto è quello»*.
>
> Domanda 1 (raffinamento) e Domanda 4 (segnature) sono rimaste **in bianco**: sul foglio
> non c'è niente.

---

## Domanda 2 — Diagramma UML concettuale delle classi

### Classi

| Classe | Attributi | Operazioni |
|---|---|---|
| `Utente` | nome : Stringa · cognome : Stringa · email : Mail · num : Cell | `Fedelta(ist : Data) : Intero ≥ 0` |
| `Gestore` | cod : CF `{id}` | |
| `Struttura` | nome : Stringa · stelle : 1..7 · via : Indirizzo | |
| `Citta` | nome : Stringa | |
| `Tipologia` | nome : Stringa `{id}` | |
| `Sistemazione` | nome : Stringa · posti : Intero > 0 | |
| `Tariffa` | posti : Intero > 0 `{id}` · giorno : Data `{id}` · prezzo : Reale ≥ 0 | |
| `Livello` | nome : Stringa · pren : Intero ≥ 0 `{id}` | |
| `MetodoPay` | nome : Stringa `{id}` | |
| `Prenotazione` | istPren : DataOra · inizio : Data · fine : Data | |
| `Accettata` | istAcc : DataOra | |
| `Rifiutata` | istRif : DataOra | |
| `Annullata` | istAnn : DataOra | |
| `Sconto` _(classe associativa)_ | val : int_unit | |

### Associazioni

| Associazione | Classe A | mult. A | mult. B | Classe B |
|---|---|---|---|---|
| `ges_str` | Gestore | `1..*` | `0..*` | Struttura |
| `cit_str` | Citta | `1..1` | `0..*` | Struttura |
| `str_tip` | Tipologia | `1..1` | `0..*` | Struttura |
| `sis_str` | Struttura | `1..1` | `1..*` | Sistemazione |
| `sis_tar` | Sistemazione | `1..1 {id}` | `0..*` | Tariffa |
| `pre_ute` | Utente | `1..1` | `0..*` | Prenotazione |
| `pag_pre` | MetodoPay | `1..1` | `0..*` | Prenotazione |
| `pre_sis` | Prenotazione | `1..*` | `1..*` | Sistemazione |
| _(sconto)_ | Struttura | `0..*` | `0..*` | Livello |

Due **classi associative**: `Sconto` (sulla `Struttura`–`Livello`) con `val : int_unit`, e
sulla `pre_sis` una con `occupanti : Intero > 0`.

### Generalizzazioni

- `Utente` generalizza `Gestore`
- `Prenotazione` generalizza `Annullata`, e generalizza `Accettata` e `Rifiutata`
  con vincolo **`{disjoint}`**

## Specifiche delle classi e delle associazioni

**1 · Classe `Utente`**

    Fedelta(ist : Data) : Intero ≥ 0
      • pre-cond: nessuna
      • post-cond:
          P = { p |  Accettata(p) ∧ ¬Annullata(p) ∧ ¬Rifiutata(p) ∧ pre_ute(p, this) ∧
                     ∃i inizio(p,i) ∧ i ≤ ist ∧ ∃k  k = ist − '2 anni' ∧ i ≥ k }
          Result = |P|

**2 · Classe `Sistemazione` — [V.tariffa_per_ogni_posto]**

    ∀s,p,t,g [ Sistemazione(s) ∧ posti(s,p) ∧ giorno(t,g) ∧ Tariffa(t) ∧ sis_tar(s,t) ] →
             [ ∀n Intero(n) ∧ n ≤ p ∧ n > 0 ] →
             ∃t1 Tariffa(t1) ∧ posti(t1,n) ∧ giorno(t1,g) ∧ sis_tar(s,t1) ]

> Le parentesi sul foglio non tornano del tutto: l'implicazione interna sembra dover
> abbracciare tutto il resto. Il senso è: per ogni sistemazione e per ogni giorno per cui
> esiste una tariffa, ne esiste una per **ogni** numero di occupanti da 1 al numero di
> posti. `[?]`

**3 · Classe `Prenotazione`**

    [V.no_intersezione_pren]
    ∀p1,p2,s,i1,i2,f1,f2 [ Prenotazione(p1) ∧ inizio(p1,i1) ∧ Prenotazione(p2) ∧
                           inizio(p2,i2) ∧ Fine(p1,f1) ∧ Fine(p2,f2) ∧ p1 ≠ p2 ∧
                           pre_sis(p1,s) ∧ pre_sis(p2,s) ] → f1 < i2 ∨ f2 < i1

    [V.posti_pren]
    ∀p,s,ps,pp [ Prenotazione(p) ∧ pre_sis(p,s) ∧ posti(s,ps) ∧
                 occupanti(p,s,pp) ] → pp ≤ ps

    [V.continuita_pren]
    ∀p,i,f [ Prenotazione(p) ∧ inizio(p,i) ∧ Fine(p,f) ] → i ≤ f

**4 · Classe `Prenotazione` — [V.interazioni_pren]**

    ∀p,ip,i,i2,ii [ Prenotazione(p) ∧ istPren(p,ip) ∧ inizio(p,i) ∧ DataOra(i,ii) ∧
                    [ istAcc(p,i2) ∨ istRif(p,i2) ∨ istAnn(p,i2) ] ] → ip ≤ i2 ≤ ii

**6 · Classe `Prenotazione`**

    [V.prenota_poi_va]
    ∀p,i,ip,g [ Prenotazione(p) ∧ inizio(p,i) ∧ istPren(p,ip) ∧ Giorno(ip,g) ] → g ≤ i

    [V.prenota_stessa_str]
    ∀p,s1,s2,st1,st2 [ s1 ≠ s2 ∧ Prenotazione(p) ∧ pre_sis(p,s1) ∧ pre_sis(p,s2) ∧
                       sis_str(s1,st1) ∧ sis_str(s2,st2) ] → st1 = st2

    [V.annullata_se_non_rif]
    ∀p [ ∃i istAnn(p,i) ] → ¬[ ∃i' istRif(p,i') ]

    [V.ann_dopo_acc]
    ∀p,ian,iac [ Prenotazione(p) ∧ istAcc(p,iac) ∧ istAnn(p,ian) ] → ian > iac

## Specifiche dei tipi di dato

    Indirizzo : (via : Stringa, civico : Intero > 0)
    Mail      : stringa secondo standard
    Cell      : stringa secondo standard
    CF        : stringa secondo standard
    int_unit  : Reale ∈ (0,1)

## Domanda 3 — Diagramma UML degli use-case

| Attore | Use-case |
|---|---|
| `Utente` | `RicercaStanze` · `InformazioniAccount` · `RichiestaPrenotazioni` |
| `Gestore` → generalizza `Utente` | `RegistraStrutture` · `StrutturePiene` · `GestionePrenotazioni` |

## Domanda 5 — Specifiche delle operazioni di use-case

**`struttura_piene(s : Struttura, u : Gestore) : (1..12, Intero ≥ 0) [12..12]`**

- pre-cond: `ges_str(u,s)`
- post-cond:

      M = { (m, |n|)  |  Mese(m) ∧
            n = { g | Data(g) ∧ Mese(g,m) ∧ ∃an Anno(adesso,an) ∧ Anno(g,an) ∧
                      [ ∀sis Sistemazione(sis) ∧ sis_str(sis,s) ] →
                      [ ∃p,i,f Accettata(p) ∧ ¬Annullata(p) ∧ pre_sis(p,sis) ∧
                        inizio(p,i) ∧ fine(p,f) ∧ i ≤ g ≤ f ] } }
      Result = M

**`cerca_sistemazioni(i : Data, f : Data, c : Citta, t : Tipologia, st : 1..7, pr : Reale ≥ 0, nper : Intero ≥ 0, u : Utente) : Struttura [0..*]`**

- pre-cond: `i ≤ f`
- post-cond:

      SG = { (g, S) |  str_tip(str,t) ∧ ∃k stelle(str,k) ∧ k ≥ st ∧ cit_str(str,c) ∧
             S = { (sis, np, cos) |
                   sis_str(sis,str) ∧ ∃k' posti(sis,k') ∧ k' ≥ np ∧ ∃tar sis_tar(sis,tar) ∧
                   posti(tar,np) ∧ prezzo(tar,cos) ∧ giorno(tar,g) ∧
                   ∀pren,ip,fp pre_sis(pren,sis) ∧ inizio(pren,ip) ∧ fine(pren,fp) →
                   g < ip ∨ fp < g }
             ∧ i ≤ g ≤ f }
           ∧ [ ∀g' (g',S) ∈ SG → Σ(sis,np,cos) ∈ S ∧ (g,S) ∈ SG  np = nper ]
           ∧ [ Σ(sis,np,cos) ∈ S, ∃s' (s',g) ∈ SG  cos · m ≤ pr ]

      R = { str |
            [ ∃mol,npren,fed,npl
              Fedelta(u, adesso, npren) ∧ Livello(fed) ∧ pren(fed,npl) ∧ npren ≥ npl ∧
              sconto(str,fed) ∧ val(str,fed,mol) ∧
              ¬[ ∃fed2,npl2 sconto(str,fed2) ∧ pren(fed2,npl2) ∧ npren ≥ npl2 ∧ npl2 > npl ]
              → m = mol ]
            ∧
            [ ¬∃mol,npren,fed,npl
              Fedelta(u, adesso, npren) ∧ Livello(fed) ∧ pren(fed,npl) ∧ npren ≥ npl ∧
              sconto(str,fed) ∧ val(str,fed,mol) ∧
              ¬[ ∃fed2,npl2 sconto(str,fed2) ∧ pren(fed2,npl2) ∧ npren ≥ npl2 ∧ npl2 > npl ]
              → m = 1 ] }
      Result = R

> È la risposta più lunga e più intricata del foglio: la parte sullo sconto serve a
> scegliere **il livello di fedeltà più alto fra quelli raggiunti**, e a mettere il
> moltiplicatore a 1 quando non ce n'è nessuno. Le sommatorie e l'annidamento delle
> parentesi sono stati letti come si vedono, ma qui il rischio di errore di lettura è più
> alto che altrove. `[?]`

## Domanda 6 — Ristrutturazione

**DBMS: PostgreSQL.** La tabella di corrispondenza fra tipi concettuali e domini SQL è
**rimasta in bianco**.

### Diagramma UML ristrutturato — cosa cambia

- spariscono le sottoclassi `Accettata`, `Rifiutata`, `Annullata`: diventano tre attributi
  di `Prenotazione`, `istAcc : Timestamp [0..1]`, `istAnn : Timestamp [0..1]`,
  `istRif : Timestamp [0..1]`;
- sparisce la sottoclasse `Gestore`: `Utente` prende `cod : CF [0..1] {id1}`;
- ogni classe prende un identificatore primario: `id : serial {id}` su `Utente`,
  `Struttura`, `Sistemazione`, `Tariffa`, `Citta`, `Prenotazione`;
- `Prenotazione.istPren` diventa `Timestamp`, `inizio` e `fine` restano `Date`;
- i domini si scrivono con i nomi SQL: `Int_G2` (intero > 0), `Int_GE2` (intero ≥ 0),
  `Real_GE2` (reale ≥ 0), `Star` per `stelle`, `Indirizzo`, `Mail`, `Cell`, `CF`,
  `int_unit`;
- `Tariffa` ha `posti : Int_G2 {id}`, `giorno : Date {id}`, `prezzo : Real_GE2`,
  `id : serial {id1}`; `Sistemazione` ha `id : serial {id}` e resta legata a `Tariffa` con
  `1..1 {id}` — `0..*`.

### Vincoli introdotti dalla ristrutturazione

    [V.utente_gestore]
    ∀u  Utente(u) ∧ ∃s ges_str(u,s) → ∃c cod(u,c)

    [V.acc_o_rif]
    ∀p  Prenotazione(p) ∧ ∃i istAcc(p,i) → ¬∃i' istRif(p,i')

La casella «breve descrizione delle scelte effettuate» è rimasta **in bianco**.

## Domanda 7 — Schema relazionale

Chiave primaria sottolineata, `*` = ammette NULL.

     1  MetodoPay(nome: Stringa)                                    [da classe]

     2  Utente(nome: Stringa, cognome: Stringa, email: Mail, num: Cell,
               id: serial, cod*: CF)                                [da classe]
          unique(cod)

     3  Tipologia(nome: Stringa)                                    [da classe]

     4  Citta(nome: Stringa, id: serial)                            [da classe]

     5  Struttura(id: serial, nome: Stringa, stelle: Star, via: Indirizzo,
                  citta: Integer, tipo: nome)                       [da classe]
          foreign key: citta references Citta(id)
          foreign key: tipo references Tipologia(nome)
          accorpa: cit_str, str_tip

     6  ges_str(gestore: CF, struttura: Integer)                    [da associazione]
          foreign key: gestore references Utente(cod)
          foreign key: struttura references Struttura(id)
          inclusione: Struttura(id) ⊆ ges_str(struttura)

     7  Prenotazione(istPren: Timestamp, inizio: Date, fine: Date, istAcc*: Timestamp,
                     istRif*: Timestamp, istAnn*: Timestamp, id: serial,
                     metodo: Stringa)                               [da classe]
          foreign key: metodo references MetodoPay(nome)
          check(inizio <= fine)
          check(istRif ≥ istPren ∧ istAcc ≥ istPren ∧ istAnn ≥ istPren ∧
                istRif ≤ cast(inizio as Date) ∧ istAnn ≤ cast(inizio as Date) ∧
                istAcc ≤ cast(inizio as Date))
          accorpa: pre_pag

     8  Prenotazione(utente: Integer)                               [da classe, seguito]
          foreign key: utente references Utente(id)
          check(istAnn > istAcc)
          check(istRif is null or istAcc is null)
          check(istRif is null or istAnn is null)
          check(cast(istPren as Date) <= inizio)
          accorpa: pre_ute

     9  Sistemazione(nome: Stringa, posti: Int_G2, id: serial, struttura: Integer)
          foreign key: struttura references Struttura(id)
          accorpa: sis_str

    10  pre_sis(occupanti: Int_G2, prenotazione: Integer, sistemazione: Integer)
          foreign key: prenotazione references Prenotazione(id)
          foreign key: sistemazione references Sistemazione(id)
          inclusione: Prenotazione(id) ⊆ pre_sis(prenotazione)

    11  Tariffa(id: serial, posti: Int_G2, prezzo: real_GE2, giorno: Date,
                sistemazione: Integer)                              [da classe]
          foreign key: sistemazione references Sistemazione(id)
          unique(sistemazione, giorno, posti)
          accorpa: sis_tar

    12  Livello(nome: Stringa, pren: Int_GE2)                       [da classe]

    13  sconto(struttura: Integer, livello: Int_GE2, val: int_unit) [da associazione]
          foreign key: livello references Livello(pren)
          foreign key: struttura references Struttura(id)

Le caselle 14 e 15 sono rimaste in bianco.

## Ulteriori vincoli esterni — trigger

**`T.no_intersezioni_pren`** — su `Insert` o `Update` di `pre_sis`

    Error = EXISTS (
      SELECT *
      FROM Prenotazione p1, Prenotazione p2, pre_sis ps
      WHERE p1.id = ps.prenotazione
        AND p2.id = new.prenotazione
        AND new.sistemazione = ps.sistemazione
        AND (p1.inizio, p1.fine) OVERLAPS (p2.inizio, p2.fine) );

**`T.prenota_stessa_str`** — su `Insert` o `Update` di `pre_sis`

    Error = EXISTS (
      SELECT * FROM Sistemazione s, pre_sis ps, Sistemazione s2
      WHERE ps.prenotazione = new.prenotazione
        AND s.id = ps.sistemazione AND s2.id = new.sistemazione
        AND s.struttura <> s2.struttura );

**`T.posti_pren`** — su `Insert` o `Update` di `pre_sis`

    Error = EXISTS (
      SELECT * FROM Sistemazione
      WHERE s.id = new.sistemazione AND s.posti < new.occupanti );

**`T.tariffa_per_ogni_posto`** — su `Insert` o `Update` di `Sistemazione`

    Error = EXISTS (
      WITH Q as ( SELECT t.giorno, count(*) as c
                  FROM Tariffa t
                  WHERE t.sistemazione = new.id
                  GROUP BY t.giorno )
      SELECT * FROM Q WHERE c <> 0 AND c <> new.posti );

> ✍️ **Annotazione sua, a margine, in rosso:** *«so che è sbagliata ma il concetto è
> quello»*. E ha ragione a diffidarne: `c <> 0 AND c <> new.posti` passa anche quando i
> posti coperti sono quelli giusti di numero ma non sono `1, 2, …, posti`, e non dice
> niente sui giorni per cui non esiste **nessuna** tariffa.

## Domanda 8 — Specifiche realizzative

**`create function struttura_piena(str : Integer) : Insieme(<Int_G2, Int_GE2>)`**

    WITH Q as
      ( SELECT pr.inizio, count(DISTINCT s.id) as sis_occ
        FROM Sistemazione s, Prenotazione pr, pre_sis ps
        WHERE s.struttura = str AND pr.id = ps.prenotazione
          AND ps.sistemazione = s.id
          AND extract('year' from pr.inizio) = extract('year' from NOW())
        GROUP BY pr.inizio ),
    N as ( SELECT count(*) FROM Sistemazione WHERE struttura = str )

    SELECT extract('month' from pr.inizio), count(pr.inizio)
    FROM Q, N
    WHERE Q.sis_occ = N.n
    GROUP BY extract('month' from pr.inizio);

La seconda funzione è appena cominciata — sul foglio c'è solo `create fu…` — e si ferma lì.

---

## Come usarlo

È lo svolgimento di uno studente, non una soluzione ufficiale: **non prenderlo come metro
di correttezza.** Vale per tre cose:

1. **la forma**: come si riempie il modulo `2024-06-05.UML`, casella per casella, con
   l'alfabeto giusto della logica (`assoc/2`, `attr/3`, `op/(n+2)`);
2. **il confronto**: la stessa traccia è svolta anche da studente-A (in UML) e studente-C
   (in ER); e tu la farai al Giorno 9. Tre risposte diverse alla stessa domanda dicono più
   di una sola;
3. **i buchi**: Domanda 1, Domanda 4, la tabella dei domini SQL e la descrizione delle
   scelte di ristrutturazione sono rimaste vuote. In una prova vera quelle caselle contano.
