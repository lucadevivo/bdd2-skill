# SafeOnTheBeach, prova del 4 settembre 2020 — svolgimento di studente-E (trascrizione)

> **Fonte:** `2020-09-04-SafeOnTheBeach-svolgimento-studente-E.pdf`, 25 pagine fotografate.
> Trascritto da Claude leggendo le pagine come immagini: **il documento è il PDF, questo è
> una copia a macchina e contiene errori di lettura.** I punti dubbi sono marcati `[?]`,
> quelli tagliati dalla foto `[testo tagliato]`. Matricola e percorsi di file omessi.
>
> **È l'unico svolgimento del corpus con un voto e una correzione: 25/30.** L'elenco degli
> errori è in `2020-09-04-SafeOnTheBeach-errori.md`; qui sotto è richiamato **nel punto
> esatto in cui l'errore si trova**, nei riquadri `> ⚠️ CORREZIONE`.
>
> La traccia è `tracce-esame/BD2_2020-09-04_SafeOnTheBeach.pdf`.
>
> ⚠️ **Notazione del 2020: diagramma ER.** Il tuo ordinamento non lo usa più — il modulo
> d'esame passa a UML con la `Versione 2024-06-05.UML`. Vincoli in FOL, use-case,
> ristrutturazione, schema relazionale e specifiche realizzative **non cambiano** con la
> notazione; cambia solo il disegno. Per questo in fondo, nella sezione **«Il diagramma in
> UML»**, lo stesso diagramma è riscritto in classi e associazioni: leggi quella e ignora
> pure la Domanda 2 in ER.

---

## Domanda 1 — Raffinamento dei requisiti

1. Dati sui **litorali**: 1.1 nome · 1.2 estensione in Km · 1.3 comuni su cui si sviluppa
   (R.2) · 1.4 mari che lo bagnano · 1.5 zone presenti (R.3)
2. Dati sui **comuni**: 2.1 nome · 2.2 provincia
3. Dati sulle **zone**: 3.1 litorale di appartenenza (R.1) · 3.2 destinazione
   {"riserva ambientale", "spiaggia"} · 3.3 capacità massima · 3.4 nome · 3.5 superficie in
   m² · 3.6 località (R.4) · 3.7 SE "riserva ambientale": 3.7.1 nome (R.3.4), 3.7.2
   descrizione, 3.7.3 data istituzione · 3.8 SE "spiaggia": 3.8.1 stabilimenti balneari
   (R.5) [testo tagliato], 3.8.2 bar o ristoranti (R.6), 3.8.3 servizi igienici presenti
4. Dati sulle **località**: 4.1 frazione di comune (0,1) · 4.2 comune di appartenenza (R.2)
   · 4.3 longitudine del centro · 4.4 latitudine del centro · 4.5 accessibilità animali
   domestici
5. Dati sugli **stabilimenti balneari**: 5.1 numero di telefono · 5.2 prezzo ingresso ·
   5.3 affitto giornaliero attrezzature [testo tagliato]
6. Dati su **bar e ristoranti**: 6.1 nome · 6.2 numero di telefono
7. Dati sugli **utenti**: 7.1 privati o commercianti · 7.2 SE "privato": 7.2.1 nome e
   cognome, 7.2.2 genere {M, F}, 7.2.3 data nascita e luogo, 7.2.4 CF · 7.3 SE
   "commerciante": 7.3.1 ragione sociale, 7.3.2 CF, 7.3.3 attività titolare (R.5 o R.6),
   7.3.3.1 accessibilità animali [testo tagliato]
   · 7.3.4 **evento pubblico**: 7.3.4.1 nome, 7.3.4.2 descrizione, 7.3.4.3 costo biglietto
   (0,1), 7.3.4.4 capacità massima, 7.3.4.5 zona (R.3), 7.3.4.6 giorno e ora, 7.3.4.7
   giorno e ora termine
8. **Prenotazioni di gruppo**: 8.1 zona (R.3) · 8.2 numero animali · 8.3 ora arrivo ·
   8.4 ora abbandono · 8.5 evento (R.7.3.4) · 8.6 partecipanti (R.7.2)
9. **Accessi a zone**: 9.1 utente privato (R.7.2) · 9.2 zona acceduta (R.3) · 9.3 ora
   arrivo · 9.4 ora abbandono

## Domanda 2 — Diagramma ER concettuale

**Entità e attributi** (dal dizionario dei dati, riquadri 1-20)

| # | Entità | Attributi |
|---|---|---|
| 1 | `Mare` | nome : stringa |
| 2 | `Litorale` | nome : stringa · estensioneKm : reale > 0 |
| 3 | `Comune` | nome : stringa · provincia : Provincia |
| 4 | `RiservaAmb` | descrizione : stringa · istituzione : data |
| 5 | `Zona` | nome : stringa · pax : intero > 0 · superficiem2 : reale > 0 · animali : booleano |
| 6 | `Spiaggia` | serviziIgienici : booleano |
| 7 | `Località` | posCentro : Posizione |
| 9 | `StabilimentoBaln` | prezzo : reale > 0 |
| 10 | `Bar` | nome : stringa |
| 11 | `Ristorante` | nome : stringa |
| 12 | `Utente` | CF : CodiceFiscale |
| 13 | `AttivitàComm` | numeroTelefono : Telefono |
| 14 | `UtenPrivato` | nome : stringa · cognome : stringa · genere : {'M','F'} · dataNascita : data · luogoNascita : stringa |
| 15 | `UtenCommerciante` | ragioneSociale : stringa |
| 16 | `Accesso` | arrivo : dataora |
| 17 | `Evento` | nome : stringa · descrizione : stringa · prezzo : reale > 0 (0,1) · pax : intero > 0 · inizio : dataora · fine : dataora |
| 18 | `Prenotazione` | arrivo : dataora · abbandono : dataora · nAnimali : intero ≥ 0 |
| 19 | `AccTerminato` | abbandono : dataora |
| 20 | `Attrezzatura` | nome : stringa |

**Relationship** (riquadro 8 = `StabAttr`, le altre lette dal disegno)

| Relationship | Estremo 1 | Estremo 2 | Attributi |
|---|---|---|---|
| `litMar` | `Litorale` (1,N) | `Mare` (0,N) | |
| `litCom` | `Litorale` (1,N) | `Comune` (0,N) | |
| `litZon` | `Litorale` (1,N) | `Zona` (1,1) | |
| `zonLoc` | `Zona` (1,1) | `Località` (0,N) | |
| `locCom` | `Località` (1,1) | `Comune` (0,N) | |
| `locFrazCom` | `Località` (0,1) | `Comune` (0,N) | |
| `spiAtt` | `Spiaggia` (0,N) | `StabilimentoBaln` (1,1) | |
| `stabAttr` | `StabilimentoBaln` (0,N) | `Attrezzatura` (0,N) | prezzoGiorn : reale > 0 |
| `comAtt` | `AttivitàComm` (1,1) | `UtenCommerciante` (0,N) | |
| `accUten` | `Accesso` (1,1) | `UtenPrivato` (0,N) | |
| `accZon` | `Accesso` (1,1) | `Zona` (0,N) | |
| `prenZon` | `Prenotazione` (1,1) | `Zona` (0,N) | |
| `prenEven` | `Prenotazione` (0,N) | `Evento` (0,N) | |
| `prenUten` | `Prenotazione` (1,N) | `UtenPriv` (0,N) | |
| `evenZon` | `Evento` (1,1) | `Zona` (0,N) | |
| `commEven` | `Evento` (1,1) | `UtenCommerciante` (0,N) | |

**Generalizzazioni**

- `RiservaAmb` e `Spiaggia` → `Zona` (freccia a triangolo vuoto)
- `StabilimentoBaln`, `Bar`, `Ristorante` → `AttivitàComm`
- `UtenPrivato` e `UtenCommerciante` → `Utente`
- `AccTerminato` → `Accesso`

### Vincoli esterni scritti nei riquadri

**Riquadro 12 — `Utente`**

    ∀u  Utente(u) → UtenPrivato(u) ∨ UtenCommerciante(u)

**Riquadro 16 — `Accesso`**

    ∀a,ar,ab  Accesso(a) ∧ arrivo(a,ar) ∧ AccTerminato(a) ∧ abbandono(a,ab) → ar ≤ ab

**Riquadro 17 — `Evento`**

    ∀e,i,f  Evento(e) ∧ inizio(e,i) ∧ fine(e,f) → i < f

    ∀e,z,pe,pz  Evento(e) ∧ evenZona(e,z) ∧ pax(e,pe) ∧ pax(z,pz) → pe ≤ pz

**Riquadro 18 — `Prenotazione`**

    ∀p,e,pe  Prenotazione(p) ∧ prenEven(p,e) ∧ pax(e,pe) → | { u | prenUten(u,p) } | ≤ p[e?]
    ∀p,z,pz  Prenotazione(p) ∧ prenZon(p,z) ∧ pax(z,pz) → | { u | prenUten(u,p) } | ≤ [testo tagliato]

> ⚠️ **CORREZIONE (voto 25):** «a pagina 13 i vincoli in FOL sul numero di persone
> dell'entità 18 sono parzialmente corretti; sono semanticamente corretti ma non risolvono
> completamente il problema in quanto controllo solo che la prenotazione non ecceda la
> capacità, invece credo andasse richiamato lo UC per i posti disponibili.»
> Cioè: confrontare con `pax` della zona non basta, perché non tiene conto degli accessi
> già in corso. Andava invocata l'operazione `calcolaDisponibilitàZona`.

**Riquadro 19 — `AccTerminato`**

    ∀a,ab  AccTerminato(a) ∧ abbandono(a,ab) → ab ≤ ADESSO

### Domini concettuali non di tipo base

- dominio **Posizione**, composto da: longitudine : reale · latitudine : reale
- dominio **Telefono**, composto da: prefisso : stringa numerica · numero : stringa numerica
- dominio **CodiceFiscale**: stringa secondo standard, da 16 caratteri
- dominio **Provincia**: stringa di 2 caratteri

## Domanda 3 — Diagramma UML degli use-case

| Attore | Use-case |
|---|---|
| `UtenteWeb` (attore generale) | `StrumentiRicerca` |
| `Ministero` → UtenteWeb | `GestioneComuni` |
| `UtenteNonRegistrato` → UtenteWeb | `StrumentiIscrizione` |
| `UtenteCommerciante` → UtenteWeb | `GestioneEventi` |
| `UtentePrivato` → UtenteWeb | `StrumentiPrenotazioni` |

Sul foglio un sesto use-case, `StrumentiAccesso`, è **cancellato**.

## Domanda 4 — Segnature delle operazioni

**1. `GestioneComuni`**

    inserisciComune(nome : stringa, provincia : stringa) : Comune

**2. `StrumentiIscrizione`**

    iscriviPrivato(nome : stringa, cognome : stringa, genere : {M,F},
                   dataNascita : data, CF : CodiceFiscale,
                   luogoNascita : stringa) : UtenPrivato
    iscriviCommerciante(CF : CodiceFiscale, ragioneSociale : stringa) : UtenCommerciante

**3. `GestioneEvento`**

    creaEvento(nome : stringa, descrizione : stringa, prezzo : reale > 0,
               pax : intero > 0, inizio : dataora, fine : dataora) : Evento

**4. `StrumentiPrenotazioni`**

    prenotaZona(arrivo : dataora, abbandono : dataora, nAnimali : intero ≥ 0,
                zona : Zona, utenti : UtenPriv (1,N)) : Prenotazione
    cancellaPrenot(prenotazione : Prenotazione)
    accedi(arrivo : dataora, utente : UtentePriv, zona : Zona) : Accesso

**5. `StrumentiRicerca`**

    ricercaEventi(zona : Zona) : Evento (0,N)
    calcolaDisponibilitàZona(zona : Zona) : intero

## Domanda 5 — Specifiche delle operazioni contrassegnate dalla barra

**`calcolaDisponibilitàZona(zona : Zona) : intero`**

- precondizioni: nessuna
- postcondizioni:
  - Variazioni nel dominio di interpretazione: nessuna
  - Valore di ritorno:

        sia A = { u | ∃a,ar  accZona(a, zona) ∧ arrivo(a,ar) ∧ ¬AccTerminato(a)
                            ∧ accUten(a,u) ∧ ar ≤ ADESSO }

        sia "capienza" il valore tale da rendere vera la formula   pax(zona, capienza)

        result = capienza − |A|

**`ricercaEventi(zona : Zona) : Evento (0,N)`**

- precondizioni: nessuna
- postcondizioni:
  - Variazioni nel dominio di interpretazione: nessuna
  - Valore di ritorno:

        sia E = { e | ∃p,f  prenZon(p, zona) ∧ prenEven(p,e) ∧ fine(e,f) ∧ f > ADESSO }

        sia P = Σ(e ∈ E) | { u | ∃p  prenEven(p,e) ∧ prenUten(p,u) } |

        result = P / |E|

> ⚠️ **CORREZIONE (voto 25):** «lo UC in FOL sulla ricerca Eventi non è completo, ho
> calcolato solo la media senza poi ritornare gli eventi come richiesto.»
> La segnatura promette `Evento (0,N)` ma `result` è un numero: manca il passo che
> restituisce gli eventi.

## Domanda 6 — Ristrutturazione

**DBMS scelto: PostgreSQL.**

Corrispondenza fra domini concettuali e domini SQL:

```sql
create domain StringS as varchar(50);
create domain StringM as varchar(150);
create domain StringL as varchar(400);
create domain RealPos as real check (value > 0);      -- reale > 0
create domain IntPos as integer check (value > 0);    -- intero > 0
create domain IntPos0 as integer check (value >= 0);  -- intero ≥ 0
-- booleano  -> boolean
-- data      -> date
-- dataora   -> timestamp
create type Genere as enum ('M','F');                 -- {'M','F'}
create domain CodiceFiscale as char(16);
create domain Provincia as char(2);
```

**Diagramma ER ristrutturato** — cosa cambia:

- le generalizzazioni `RiservaAmb`/`Spiaggia` → `Zona` diventano le relationship
  `risIsZon` (0,1)–(1,1) e `spiIsZon` (0,1)–(1,1);
- le generalizzazioni `StabilimentoBaln`/`Bar`/`Ristorante` → `AttivitàComm` diventano
  `staIsAtt`, `barIsAtt`, `risIsAtt`, tutte (1,1)–(0,1);
- `Utente` resta, con `UtenPrivato` e `UtenCommerciante` legati da `privIsUt` e `comIsUt`;
- entrano gli identificatori: `id` su `Zona`, `AttivitàComm`, e `CF` resta su `Utente`;
- l'attributo composto `Telefono` si spiana in `numeroTelefono` + `prefissoTelefono` su
  `AttivitàComm`; `Posizione` si spiana in `longCentro` e `latCentro` su `Località`;
- `Accesso` prende `arrivo`, `Terminato` (booleano) e `abbandono (0,1)`: la
  generalizzazione `AccTerminato` sparisce.

**Descrizione delle scelte, come scritta:** «Sostituzione con relationship per mantenere
struttura. Fusione is-a per semplicità.»

**Vincoli introdotti o modificati nella ristrutturazione**

    ∀z  Zona(z) → [ (∃zr risIsZon(z,zr) → ¬∃zs spiIsZon(z,zs))
                  ∧ (∃zisa risIsZon(z,zisa) ∨ spiIsZon(z,zisa)) ]

    ∀at AttivitàComm(at) → [ (∃st staIsAtt(at,st) → ¬∃at2 barIsAtt(at,at2))
                           ∧ (∃ba barIsAtt(at,ba) → ¬∃at2 risIsAtt(at,at2))
                           ∧ (∃st staIsAtt(at,st) → ¬∃at2 risIsAtt(at,at2))
                           ∧ (∃at2 staIsAtt(at,at2) ∨ barIsAtt(at,at2) ∨ risIsAtt(at,at2)) ]

    ∀u  Utente(u) → ∃u2 privIsUT(u,u2) ∨ comIsUT(u,u2)

    ∀a  Accesso(a) ∧ Terminato(a,true) ↔ ∃ab abbandono(a,ab)

Sul foglio, fra questi, due formule su `Utente` sono **cancellate**.

## Domanda 7 — Schema relazionale

Chiave primaria sottolineata, `*` = ammette NULL.

     1  Litorale(id: serial, nome: StringM, estensioneKm: RealPos)          [da entità]
          inclusione: id ⊆ litCom(litorale)
          inclusione: id ⊆ Zona(litorale)

     2  Mare(nome: StringM)                                                 [da entità]

     3  litMar(litorale: integer, mare: StringM)                            [da relationship]
          foreign key: litorale references Litorale(id)
          foreign key: mare references Mare(nome)

     4  litCom(litorale: integer, comune: Provincia)                        [da relationship]
          foreign key: litorale references Litorale(id)
          foreign key: comune references Comune(id)

     5  Comune(nome: StringM, provincia: Provincia)                         [da entità]

     6  Zona(id: serial, nome: StringM, pax: IntPos, superficiem2: RealPos,
             animali: boolean, litorale: integer, località: integer)        [da entità]
          foreign key: litorale references Litorale(id)
          foreign key: località references Località(id)
          accorpa: litZon, zonLoc

     7  RiservaAmb(zona: integer, descrizione: StringL, istituzione: date)  [da entità]
          foreign key: zona references Zona(id)
          accorpa: risIsZon

     8  Spiaggia(zona: integer, serviziIgienici: boolean)                   [da entità]
          foreign key: zona references Zona(id)
          accorpa: spiIsZon

     9  Località(id: serial, longCentro: real, latCentro: real,
                 comune: Provincia, frazComune*: Provincia)                 [da entità]
          foreign key: comune references Comune(provincia)
          foreign key: frazComune references Comune(provincia)
          accorpa: locCom, locFrazCom

    10  StabilimentoBaln(attività: integer, prezzo: RealPos)                [da entità]
          foreign key: attività references AttivitàComm(id)
          accorpa: staIsAtt

    11  StabAttr(stabilimento: integer, attrezzatura: integer,
                 prezzoGiorn: RealPos)                                      [da relationship]
          foreign key: stabilimento references StabilimentoBaln(attività)
          foreign key: attrezzatura references Attrezzatura(id)

    12  Attrezzatura(id: serial, nome: StringS)                             [da entità]

    13  Bar(attività: integer, nome: StringM)                               [da entità]
          foreign key: attività references AttivitàComm(id)
          accorpa: barIsAtt

    14  Ristorante(attività: integer, nome: StringM)                        [da entità]
          foreign key: attività references AttivitàComm(id)
          accorpa: risIsAtt

    15  AttivitàComm(id: serial, prefissoTelefono: Prefisso,
                     numeroTelefono: Telefono, animali: boolean,
                     spiaggia: integer, utente: CodiceFiscale)              [da entità]
          foreign key: spiaggia references Spiaggia(zona)
          foreign key: utente references UtenCommerciante(utente)
          accorpa: spiAtt, comAtt

    16  Utente(CF: CodiceFiscale)                                           [da entità]

    17  UtenPrivato(utente: CodiceFiscale, nome: StringS, cognome: StringS,
                    genere: Genere, dataNascita: date, luogoNascita: StringM)
          foreign key: utente references Utente(CF)
          accorpa: privIsUT

    18  UtenCommerciante(utente: CodiceFiscale, ragioneSociale: StringM)
          foreign key: utente references Utente(CF)
          accorpa: comIsUT

    19  Evento(id: serial, nome: StringM, descrizione: StringL, prezzo*: RealPos,
               pax: IntPos, inizio: timestamp, fine: timestamp, zona: integer,
               utente: CodiceFiscale)                                       [da entità]
          foreign key: zona references Zona(id)
          foreign key: utente references UtenCommerciante(utente)
          ennupla: inizio < fine
          accorpa: commEven, evenZon

    20  Accesso(id: serial, arrivo: timestamp, Terminato: boolean,
                abbandono*: timestamp, zona: integer, utente: CodiceFiscale)
          foreign key: zona references Zona(id)
          foreign key: utente references UtentePriv(utente)
          ennupla: Terminato = true ↔ abbandono <> NULL
          ennupla: abbandono <> NULL → arrivo ≤ abbandono
          accorpa: accZon, accUten

    21  Prenotazione(id: serial, arrivo: timestamp, abbandono: timestamp,
                     nAnimali: IntPos, zona: integer)                       [da entità]
          foreign key: zona references Zona(id)
          ennupla: arrivo ≤ abbandono
          inclusione: id ⊆ prenUten(prenotazione)
          accorpa: prenZon

    22  prenUten(prenotazione: integer, utente: CodiceFiscale)              [da relationship]
          foreign key: prenotazione references Prenotazione(id)
          foreign key: utente references UtenPrivato(utente)

    23  prenEven(prenotazione: integer, evento: integer)                    [da relationship]
          foreign key: prenotazione references Prenotazione(id)
          foreign key: evento references Evento(id)

## Ulteriori vincoli esterni — trigger

    Trigger:
      evento intercettato: inserimento ennupla relazione Utente
      istante: prima
      funzione:
        new = ennupla da inserire
        hasError = exists (
          select *
          from UtenPrivato up, UtenCommerciante uc
          where new.cf <> up.utente
            and new.cf <> uc.utente );
        IF hasError THEN blocca operazione
        ELSE permetti operazione

> ⚠️ **CORREZIONE (voto 25):** «l'unico trigger che ho implementato è toppato.»
> Il difetto si vede a occhio: con `<>` e `and` la sottoquery è vera appena esiste una
> qualsiasi coppia di righe diverse dal nuovo CF, quindi il trigger blocca quasi sempre.
> Serviva `not exists (... where up.utente = new.cf or uc.utente = new.cf)` — e comunque
> il controllo va fatto **dopo** l'inserimento, non prima, perché la riga in `UtenPrivato`
> non esiste ancora.

## Domanda 8 — Specifiche realizzative

**`calcolaDisponibilitàZona(zona : integer) : integer`**

    res = risultato della seguente query SQL sostituendo a ':zona' il valore
          dell'omonimo parametro attuale
      select (z.pax), (count(*)) as postiOccupati
      from Accesso a, Zona z
      where ':zona' = a.zona
        and a.arrivo <= CURRENT_TIMESTAMP
        and a.Terminato = false
        and z.id = a.zona
      group by z.pax

    ritorna (valore della colonna "pax" dell'unica ennupla di res)
          − (valore della colonna "postiOccupati" dell'unica ennupla di res)

> ⚠️ **CORREZIONE (voto 25), errori non gravi:**
> - il `group by` è superfluo: il risultato sarebbe uguale senza scriverlo;
> - `Zona` nella `from` non era necessaria, quindi anche `z.id = a.zona` si poteva omettere;
> - la differenza è fatta fuori da SQL, mentre si poteva scrivere direttamente
>   `SELECT z.pax - count(*)`.

---

## Come leggerlo, in breve

Cosa gli è costato i 5 punti: **un vincolo FOL che guarda la capienza invece di chiamare
l'operazione che calcola i posti liberi**, **un use-case che restituisce un numero al posto
degli eventi promessi dalla segnatura**, **un trigger con la logica rovesciata** e **tre
sbavature di stile in SQL**. Tre errori su quattro non sono di notazione ma di *coerenza*:
la risposta non fa quello che la sua stessa segnatura, o il requisito, prometteva.


---

## Il diagramma in UML (conversione, non è farina del suo sacco)

Il suo diagramma è ER. Qui sotto lo stesso modello nella notazione che usi tu. La regola
che ci vuole a leggerlo, se ti capita ancora un ER: **in ER la cardinalità sta sul ramo
dell'entità a cui si riferisce; in UML la stessa molteplicità si scrive all'estremo
opposto dell'associazione.** ER `Litorale (1,N) — litMar — Mare (0,N)` significa «ogni
litorale bagna da 1 a N mari», e in UML quel `1..*` va scritto **accanto a Mare**.

### Classi

Le 20 entità diventano 20 classi con gli stessi attributi (li trovi nella tabella della
Domanda 2). Gli identificatori, che in ER sono il pallino pieno, in UML si scrivono `{id}`
accanto all'attributo.

### Associazioni

| Associazione | Classe A | mult. lato A | mult. lato B | Classe B |
|---|---|---|---|---|
| `litMar` | Litorale | `0..*` | `1..*` | Mare |
| `litCom` | Litorale | `0..*` | `1..*` | Comune |
| `litZon` | Litorale | `1..1` | `1..*` | Zona |
| `zonLoc` | Zona | `0..*` | `1..1` | Località |
| `locCom` | Località | `0..*` | `1..1` | Comune |
| `locFrazCom` | Località | `0..*` | `0..1` | Comune |
| `spiAtt` | Spiaggia | `1..1` | `0..*` | StabilimentoBaln |
| `stabAttr` | StabilimentoBaln | `0..*` | `0..*` | Attrezzatura |
| `comAtt` | AttivitàComm | `0..*` | `1..1` | UtenCommerciante |
| `accUten` | Accesso | `0..*` | `1..1` | UtenPrivato |
| `accZon` | Accesso | `0..*` | `1..1` | Zona |
| `prenZon` | Prenotazione | `0..*` | `1..1` | Zona |
| `prenEven` | Prenotazione | `0..*` | `0..*` | Evento |
| `prenUten` | Prenotazione | `0..*` | `1..*` | UtenPrivato |
| `evenZon` | Evento | `0..*` | `1..1` | Zona |
| `commEven` | Evento | `0..*` | `1..1` | UtenCommerciante |

`stabAttr` porta un attributo proprio (`prezzoGiorn : reale > 0`): in UML è una **classe di
associazione**.

### Generalizzazioni

| Padre | Figlie | Vincolo |
|---|---|---|
| `Zona` | `RiservaAmb`, `Spiaggia` | `{disjoint, complete}` |
| `AttivitàComm` | `StabilimentoBaln`, `Bar`, `Ristorante` | `{disjoint, complete}` |
| `Utente` | `UtenPrivato`, `UtenCommerciante` | `{disjoint, complete}` |
| `Accesso` | `AccTerminato` | sottoinsieme semplice, né disgiunta né completa |

I `{complete}` non me li sono inventati: sono esattamente i vincoli che lui ha dovuto
scrivere a mano in FOL nella ristrutturazione (`∀z Zona(z) → ∃zisa risIsZon ∨ spiIsZon`,
`∀u Utente(u) → privIsUT ∨ comIsUT`, e l'analogo su `AttivitàComm`). **In UML quei vincoli
non si scrivono: li dice il diagramma**, ed è una delle ragioni per cui il corso ha
cambiato notazione. `AccTerminato` invece resta una sottoclasse semplice, perché un accesso
può benissimo non essere ancora terminato.
