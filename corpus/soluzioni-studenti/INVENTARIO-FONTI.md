# Che cosa c'è davvero in `05-soluzioni-studenti`

> Inventario misurato il 02/09/2026 sui PDF di `~/Scrivania/BDD2-fonti/05-soluzioni-studenti`.
> Nasce da una correzione dell'utente: la convinzione precedente — «di leggibile ci sono solo le
> soluzioni a macchina di studente-B, il resto sono moduli in bianco» — **era sbagliata**. Sono
> **45 documenti con inchiostro**, quasi tutti svolti fino alla Domanda 8.

Come è stato misurato: per ogni pagina, `get_images() > 1` (studente-A e -C incollano le risposte
come immagini) oppure `get_drawings() > 400` (studente-B scrive a stilo). La domanda a cui una
pagina appartiene si legge dal testo del modulo in bianco (`Risposta alla Domanda N`), che il
livello di testo conserva sempre.

## La distinzione che conta: quale modulo

L'utente **non legge l'ER**. Il discrimine è la versione del modulo, stampata sul bordo:
fino a `2024-03-29` la Domanda 2 chiede il diagramma **ER**, dalla `2024-06-05.UML` in poi il
diagramma **UML delle classi**. Le versioni `2024-02-08` di studente-A sono già UML.

Una soluzione in ER **resta utile**: se ne legge tutto tranne il diagramma — FOL, ristrutturazione,
schema relazionale, trigger, SQL — e vale la regola di `NOTAZIONE.md`, si legge e non si imita.

## studente-A (risposte incollate come immagini)

| Documento | Modulo | Pagine con inchiostro | Fin dove |
|---|---|---|---|
| **Città Verde** | **UML** | 20 / 28 | **D8** — è la traccia dell'appello che l'utente ha tentato. **Trascritta** (`CittaVerde-svolgimento-TRASCRIZIONE.md`) |
| **My Precious** | **UML** | 22 / 30 | **D8** — di questa esiste anche la traccia in `tracce-esame/`. **Trascritta** (`MyPrecious-svolgimento-TRASCRIZIONE.md`) |
| EasyToll, Slimmy, CozyRooms, TimeBank | UML | 15-22 | D8 (TimeBank già trascritta) |
| AmaZZon, Out!, QuickHospital, RainAir, RistoBook, TravelPlan, AllenaMondo | ER | 11-23 | D8, tranne RainAir (D6) |

## studente-B (stilo, inchiostro vettoriale — il più leggibile)

| Documento | Modulo | Fin dove |
|---|---|---|
| Slimmy, EasyToll, CozyRooms | UML | D8 (tutte già trascritte) |
| DKLCloud | UML | D5 (già trascritta) |
| RistoBook, AllenaMondo, TravelPlan, DormoDaTe, TuTubi | ER | D8 |
| AmaZZon, Out! | ER | D7 |
| QuickHospital, «altra roba» Out! | ER | D5 |
| SafeOnTheBeach | ER | D4 |
| Città Verde, My Precious | da verificare a occhio (nessuna versione nel livello di testo) | |
| Appunti di teoria | — | 29 pagine di riassunto, già nel corpus |

## studente-C (risposte incollate come immagini) — **tutto ER**, ma quasi tutto completo

| Documento | Fin dove |
|---|---|
| Città Verde, TravelPlan, RistoBook, My Precious, QuickHospital, AllenaMondo, SafeOnTheBeach, CozyRooms, EasyToll, Slimmy | D8 |
| ecoParks, eBuy | D5 |

## studente-D

Solo un documento con inchiostro (Università 4, una pagina): le sue ristrutturazioni sono
scansioni con pochissimo contenuto estraibile.

## Che cosa ne consegue

1. **Le prove sul modulo UML non sono cinque ma sette**, e dal 02/09/2026 **sono trascritte tutte
   e sette**: alle cinque precedenti si sono aggiunte **Città Verde** e **My Precious** di
   studente-A, entrambe complete fino alla Domanda 8.
2. **Le soluzioni in ER sono una miniera per le Domande 5-8**, che della notazione non risentono:
   studente-C da solo ha dieci documenti completi.
3. Il criterio con cui era stata liquidata la cartella — «i PDF hanno il testo identico fra loro,
   quindi sono moduli in bianco» — misurava il **livello di testo**, che è il modulo, e non
   l'inchiostro sopra. È l'errore da non ripetere: si conta `get_images()`/`get_drawings()`, mai
   `get_text()`.
