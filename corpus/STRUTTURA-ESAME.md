# Struttura della prova d'esame

Due fonti concordi:

1. **`BD2.Esame.Risposte.UML.pdf`** — modulo risposte ufficiale, versione **2024-06-05.UML**,
   34 pagine: `docente-ufficiale/modulo-risposte-UML-2024-06-05.pdf`, testo in
   `docente-ufficiale/modulo-risposte-UML-2024-06-05.md`.
2. **Pagina del corso** — struttura delle prove e metodologia di valutazione (trascritta in
   fondo a questo file).

Sostituiscono il facsimile 2020 in notazione ER, che il corpus non tiene piu'.

## Formato

**Prova scritta + prova orale.**

Lo scritto è una sola traccia con l'intera pipeline da sviluppare end-to-end. Nessun quiz.
La traccia è *"una specifica dei requisiti testuale del tipo di quelle disponibili nella sezione
Progetti del materiale didattico"* — quindi **i 15 progetti del corso sono il modello diretto
delle tracce d'esame**, non solo esercizio.

**Tempi: la prova è dimensionata per 3 ore, il limite di consegna è 5 ore.** I tempi per singola
domanda qui sotto sono indicativi e sommano a meno del totale disponibile.

Cinque domande sono marcate `(*)`:

> Una risposta soddisfacente a questa domanda è **condizione necessaria (ma non sufficiente)**
> per superare la prova.

Sono le **Domande 2, 5, 7, 8** (e il diagramma UML dentro la 2). Una risposta insufficiente su
una qualsiasi di queste fa fallire la prova a prescindere dal resto.

## Le otto domande

| # | Tempo (max) | Cosa produrre | `(*)` |
|---|---|---|---|
| 1 | 10' | Raffinamento dei requisiti: elenco numerato, senza inconsistenze, omissioni, ridondanze | **non valutata** |
| 2 | 45' (75') | Diagramma UML concettuale delle classi + specifiche di classi, associazioni, tipi di dato, vincoli esterni | ✅ |
| 3 | 5' (10') | Diagramma UML degli use-case: tutte le funzionalità richieste, ad alto livello | |
| 4 | 10' | Segnatura delle operazioni di ogni use-case | |
| 5 | 30' (60') | Specifiche concettuali delle operazioni di use-case: segnatura, precondizioni, postcondizioni in FOL | ✅ |
| 6 | 20' (30') | Scelta del DBMS + ristrutturazione dello schema UML, del dizionario dei dati e dei vincoli esterni; corrispondenza tipi concettuali → domini SQL; eliminazione di attributi multivalore o composti | |
| 7 | 30' (60') | Schema relazionale della base dati con i relativi vincoli | ✅ |
| 8 | 30' (45') | Specifiche realizzative: segnatura con domini SQL, algoritmo in pseudo-codice con SQL immerso, e **dove implementarla — DBMS o back-end** | ✅ |

I tempi suggeriti sommano a circa 3 ore, coerenti col dimensionamento dichiarato. Il tempo
massimo reale di consegna è **5 ore**.

## L'orale non salva lo scritto

> La prova orale non potrà sanare errori compiuti dallo studente nella prova scritta. […] la
> prova orale può concludersi immediatamente con una insufficienza, in caso lo svolgimento della
> prova scritta dovesse contenere errori o lacune sostanziali in passi chiave.

La pagina del corso elenca gli errori che chiudono subito l'esame — e **corrispondono uno a uno
alle quattro domande marcate `(*)` nel modulo risposte**, che è una conferma indipendente di
quali passi siano eliminatori:

| Errore fatale (pagina del corso) | Domanda |
|---|---|
| diagramma UML delle classi concettuale inadeguato o con gravi errori | 2 |
| errori sostanziali nell'uso della logica | 5 |
| errori sostanziali nello schema relazionale e/o nell'implementazione dei vincoli associati | 7 |
| errori sostanziali nella specifica realizzativa degli use-case (es. nel codice SQL) | 8 |

La lista è dichiarata **non esaustiva**.

**Conseguenza operativa per la skill:** su queste quattro il livello di accuratezza richiesto è
diverso dal resto. Meglio una risposta più breve e sicuramente corretta che una ricca e
traballante. In particolare ogni comando SQL prodotto va **eseguito** prima di essere consegnato
(vedi `INDICE.md`, sezione database di esempio).

## Vincoli di ambito da rispettare

**La barra laterale decide cosa sviluppare.** Le domande 5 e 8 non chiedono *tutte* le
operazioni, ma solo quelle necessarie a modellare **i requisiti contrassegnati dalla barra
verticale nel margine sinistro della traccia**, incluse le operazioni ausiliarie che servono.

È un segno grafico: la traccia va letta come immagine, mai passata per un OCR
(vedi `INDICE.md`).

**Vocabolario condiviso.** La Domanda 5 dice esplicitamente: *"Si assuma lo stesso vocabolario
definito alla Domanda 2"*. I simboli di predicato usati nelle pre/postcondizioni devono essere
quelli del diagramma e delle specifiche della Domanda 2, non nuovi.

**Coerenza tra fasi.** La Domanda 8 chiede specifiche realizzative *"in modo conforme alla loro
specifica concettuale prodotta nella fase di Analisi"*: l'algoritmo deve verificare le
precondizioni e garantire le postcondizioni scritte alla Domanda 5.

## Due requisiti che il modulo risposte non rende espliciti

Vengono dalla pagina del corso e vanno trattati come parte delle Domande 6 e 7.

**I vincoli esterni si realizzano in SQL.** La fase di progettazione include la *"definizione di
vincoli esterni allo schema mediante condizioni SQL che devono essere sempre verificate"*: ogni
vincolo esterno scritto in FOL nell'analisi va portato fino a una realizzazione SQL — check,
trigger, o politica di accesso ai dati — non lasciato in forma logica.

**La ristrutturazione è anche una scelta di prestazioni.** *"Effettuando opportune scelte per
aumentare le prestazioni complessive del sistema"*: le decisioni della Domanda 6 vanno motivate
in termini di efficienza delle operazioni, non solo di correttezza. È lo stesso punto che il
tutor fa nelle correzioni di QuickHospital, dove suggerisce di tenere separate `Ricovero` e
`RicoveroTerminato` perché *"mantenendo in Ricovero solamente dati freschi rendiamo più
efficienti diverse operazioni"*.

## Convenzioni del modulo risposte

Sono la notazione attesa nelle risposte, non dettagli di stampa.

- **Specifiche di classi e associazioni** (Domanda 2): fino a 8 riquadri, ognuno con
  `Tipo: Classe | Associazione`.
- **Schema relazionale** (Domanda 7): fino a 20 relazioni, ognuna con nome, attributi, domini e
  `Derivante da: classe | associazione`. Ogni relazione va quindi tracciata all'elemento UML da
  cui deriva.
- Nello schema relazionale: **gli attributi della chiave primaria vanno sottolineati, quelli che
  possono essere NULL contrassegnati con `*`**.
- Le pagine dalla 31 in poi sono minute e non vengono valutate.

---

## Nota sulla versione ER

La pagina del corso ammette ancora l'ER come alternativa: il modulo risposte esiste in due
versioni, e quella ER resta *"aderente al programma di edizioni precedenti del corso di laurea
in presenza e a tutte le edizioni del corso di laurea in modalità teledidattica"*.

Per questo corpus la scelta è comunque **solo UML** (vedi `NOTAZIONE.md`): è la versione del
corso di laurea in presenza dal 2023-2024 in poi. Da notare che scegliendo l'ER si dovrebbero
**omettere le specifiche delle classi** — un'ulteriore ragione per non mescolare le due strade.

## Autovalutazione

> Si invitano caldamente gli studenti a provvedere ad opportune autovalutazioni prima di
> prenotarsi a sostenere l'esame.

È il ruolo dei 4 sbarramenti in `docente-ufficiale/sbarramenti/`: non rispecchiano il
formato d'esame, ma sono l'unico materiale con risposte oggettivamente corrette.
