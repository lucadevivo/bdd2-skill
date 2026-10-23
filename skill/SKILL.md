---
name: bdd2
description: Risolve esercizi, progetti e tracce d'esame di Basi di Dati Modulo 2 (Sapienza) seguendo la metodologia esatta del corso. Copre l'intera pipeline - raffinamento dei requisiti, diagramma UML delle classi concettuale, diagramma degli use-case, specifiche di classi/associazioni/tipi di dato, vincoli esterni e specifiche di operazioni in logica del primo ordine, ristrutturazione, schema relazionale con vincoli, specifiche realizzative in pseudo-codice con SQL immerso, DDL e DML PostgreSQL. Usa questa skill ogni volta che l'utente nomina BDD2, BD2, "basi di dati modulo 2", una traccia o un progetto del corso (QuickHospital, Travel to the Moon, eBuy, TuTubi, SnowPass, e simili), oppure chiede di produrre un diagramma UML concettuale, vincoli esterni in FOL, pre/postcondizioni di operazioni, uno schema relazionale con vincoli, o query sui database Accademia e Cielo - anche se non nomina esplicitamente il corso.
---

# Basi di Dati, Modulo 2 — metodologia del corso

Questa skill riproduce la metodologia di progetto del corso di **Basi di Dati, Modulo 2**
(Sapienza, Laurea in Informatica). Non è una guida generica di
progettazione di basi dati: la notazione, l'ordine dei passi e le convenzioni sono quelle
specifiche del corso, ed è su quelle che una soluzione va costruita e valutata.

Il corpus completo — slide, soluzioni ufficiali, 40 tracce d'esame, videolezioni trascritte,
criteri di correzione — è in `__BDD2_ROOT__/corpus/`. La mappa è in
`references/corpus.md`: leggila quando serve un esempio o una fonte.

**Se il compito è un'esercitazione SQL** (Accademia 3-8, Cielo 1-5), quasi nulla di questo
documento ti serve: vai a `references/sql.md` e alla sezione *Verificare l'SQL* qui sotto.

**Se il compito è correggere una soluzione già scritta** — dell'utente, di uno studente, o tua —
il mestiere è un altro e sta in `references/correzione.md`: si valuta quello che c'è, si dice cosa
non regge e perché, e non si riscrive.

## Prima di tutto: due regole non negoziabili

**Si produce UML, mai ER.** L'Entity-Relationship apparteneva all'ordinamento vecchio.
Molte soluzioni nel corpus lo usano ancora: si leggono per la logica, i vincoli e l'SQL, ma
il diagramma va sempre riespresso in UML. La trappola nel tradurre: in ER le molteplicità
stanno sull'estremo **opposto** dell'associazione, in UML sul **proprio**. Vanno ribaltate.

**Quattro passi sono eliminatori.** La pagina del corso e il modulo risposte ufficiale
concordano: una risposta insufficiente su uno solo di questi fa fallire la prova, e l'orale
non può sanarla.

| Passo | Errore che chiude l'esame |
|---|---|
| Domanda 2 | diagramma UML concettuale inadeguato o con gravi errori |
| Domanda 5 | errori sostanziali nell'uso della logica |
| Domanda 7 | errori sostanziali nello schema relazionale o nei vincoli |
| Domanda 8 | errori sostanziali nella specifica realizzativa (es. nel codice SQL) |

Su questi quattro, **la correttezza vale più della ricchezza**. Una specifica breve e giusta
batte una lunga e traballante. Se un requisito è genuinamente ambiguo, modella
l'interpretazione più difendibile e annota l'assunzione in una riga, invece di inventare
struttura che poi non regge.

## Nessun passaggio si salta, niente resta abbozzato

Ogni artefatto che il compito richiede va prodotto **per intero**. Non si omette un passo perché
sembra minore, non si lascia un segnaposto, non si scrive "per esercizio" o "analogamente agli
altri". Se un tipo di dato ha un formato, quel formato va scritto; se una classe ha
un'operazione, la sua specifica va data; se un vincolo esterno esiste, la sua realizzazione in
SQL va sviluppata.

**Questo vale anche quando il materiale ufficiale abbrevia.** Le soluzioni del corso sono piene
di `Stringa ~ '...'`, di `... // per esercizio` e di note come *"tutti gli altri vincoli per
disjoint/complete, v. diagramma"*: sono scorciatoie didattiche del docente, che lascia
volutamente del lavoro allo studente. Sono un modello per **la forma**, mai per il livello di
completezza. Dove l'originale mette dei puntini, la risposta mette il contenuto.

**Completezza è degli artefatti, non della prosa.** «Niente resta abbozzato» vuol dire che ogni
vincolo ha la sua formula, ogni operazione la sua specifica, ogni tipo il suo formato: **non** che
la risposta sia lunga. Quanto lungo è troppo lungo lo dice la sezione *Le proporzioni di una prova
vera*, più sotto, con i numeri misurati: si tagliano prosa, esempi e ripetizioni, mai artefatti.
Le due regole non sono in tensione — la prima dice *cosa* ci deve stare, la seconda *quanto*
spazio prendersi per dirlo.

**Non si salta nemmeno quello che il compito non elenca, se la tua modellazione lo rende
necessario.** L'elenco degli obiettivi dice quali *passi* svolgere, non quali specifiche servono
dentro quei passi: quelle le decide ciò che hai modellato. Se introduci un tipo di dato
concettuale, la sua specifica è obbligatoria anche se la traccia non la nomina. Se metti
un'operazione nel diagramma, va specificata. Se un vincolo non è esprimibile con i costrutti del
diagramma, va scritto come vincolo esterno.

Il controllo, prima di consegnare, è meccanico: **scorri il diagramma e verifica che ogni
elemento che lo richiede abbia la sua specifica.**

| Nel diagramma c'è | Allora deve esserci |
|---|---|
| un tipo non di base su un attributo | la sua specifica fra i tipi di dato |
| un tipo strutturato | tutti i suoi campi, e i vincoli sui suoi valori |
| un'operazione di classe o di tipo di dato | segnatura, `pre`, `post`, formula |
| una specializzazione di associazione | la verifica che le molteplicità implicate siano quelle volute |
| un vincolo enunciato a parole nei requisiti | la sua formula in FOL, non la parafrasi |
| un risultato che è una **sequenza ordinata** | l'operazione `sorted`, vedi `fol.md` |

**Il controllo dei contenitori, che è quello che si sbaglia più spesso.** Prima di dichiarare
finita la Domanda 2, scorri la traccia e segna **ogni nome di luogo, di contenitore o di
collezione** che compare: città, nazione, regione, padiglione, piano, settore, casa produttrice,
tipologia — **e ogni insieme di valori condiviso fra le istanze**: metodi di pagamento, valute,
modelli, categorie. E anche le collezioni che la traccia tratta come una cosa a sé, *«un servizio di
**cronologia**»*, *«il **carrello**»*, *«il **catalogo**»*. Per ognuno la
domanda è una sola: **nel mio diagramma è una classe o è finito dentro un attributo?** Se è un
attributo, la giustificazione deve essere esplicita (il nome del casello *è* il nome della località,
lo dice la traccia), altrimenti è una classe.

La versione insidiosa non è il luogo, è la **collezione nominata**: in TuTubi la traccia dice
*«TuTubi deve fornire un servizio di cronologia, ricordando la sequenza di tutte le
visualizzazioni»*, e il ristrutturato ufficiale ha la classe `Cronologia` fra `Utente` e
`Visualizzazione`. Attaccare le visualizzazioni direttamente all'utente sembra equivalente e non lo
è: la cronologia è **la cosa che il requisito nomina**, ed è l'unica classe mancante in un
confronto che per il resto coincideva.

È l'errore più frequente della skill, misurato: in tre confronti su tre con un diagramma ufficiale
la catena geografica o di contenimento è stata schiacciata — QuickHospital
(`Padiglione→Piano→Settore→Stanza` diventati attributi), Officine 1 (`Città` e `Nazione`
mancanti, e con loro `CasaProduttrice`), Università 1 (`Città`, `Regione`, `Nazione` tenute come
stringhe duplicate su due classi). Ogni volta il ragionamento sembrava difendibile; ogni volta
mancavano da tre a quattro classi rispetto all'ufficiale. La regola c'è in `analisi.md`, ma non
scatta da sola: **questo controllo va fatto a mano, alla fine, sulla traccia**.

I vincoli `{disjoint}` e `{complete}` di una generalizzazione **non** vanno riscritti come vincoli
esterni in fase di analisi: li esprime il diagramma. Nella soluzione ufficiale di QuickHospital
non ce n'è nessuno nei documenti di analisi, e compaiono solo in **ristrutturazione**, quando la
generalizzazione viene sciolta e il diagramma smette di garantirli. Lo stesso vale per il
`{disjoint, complete}` fra link di associazione e per l'unicità implicata da una classe
associativa.

Un vincolo lasciato in italiano — *"i due anni solari sono consecutivi"* — è un segnaposto quanto
un `~ '...'`: va formalizzato.

**Ignora gli elenchi di costrutti ammessi che trovi nelle esercitazioni.** Molte tracce
`E.A.1.x` dicono *"utilizzando solo i costrutti di classe, associazione, attributo, vincolo di
identificazione di classe e generalizzazione"*. Non è una scelta di modellazione: è un artefatto
del momento in cui l'esercitazione è stata assegnata, a lezione, quando gli altri costrutti non
erano ancora stati spiegati. Oggi il programma è completo, e limitarsi produce una soluzione
peggiore.

Usa sempre **tutti** i costrutti che il caso richiede — classi associative, operazioni di classe,
specializzazioni di attributi, associazioni e operazioni, generalizzazioni fra link di
associazione — e la FOL per i vincoli esterni, anche nelle esercitazioni della Parte A.

**L'unica eccezione: le esercitazioni che vanno in coppia.** Quando un'esercitazione dice
esplicitamente di *rivedere il diagramma della precedente* — Università 1 e 2, Voli aerei 1 e 2,
Officine 1 e 3 — la limitazione dei costrutti nella prima **è il compito**, non un residuo: la
seconda esiste proprio per introdurre ciò che alla prima mancava. Risolvendo la prima con tutti i
costrutti si produce la risposta della seconda. Misurato: nel confronto con l'ufficiale di
Università 1 la superclasse `Persona` risulta «classe in più», ed è la soluzione di Università 2.
Fuori da queste coppie — e in ogni traccia d'esame — la regola sopra vale senza sconti.

Questo spiega anche perché alcune soluzioni ufficiali di quelle esercitazioni sono **volutamente
incomplete**, e lo dichiarano. Quella di Voli aerei 2 annota che a quel punto del corso non si
sapeva ancora imporre valori progressivi alle tappe, e che modellare la tappa come classe lascia
passare un volo che tocca due volte lo stesso aeroporto. È un limite dichiarato, non un modello
da imitare: oggi quel vincolo si scrive.

Le uniche soluzioni **non** limitate sono quelle degli esami e dei progetti — QuickHospital, le
tracce d'esame, le soluzioni raccolte su GitHub. Sono quelle da prendere come riferimento di
completezza.

In concreto, i punti dove la tentazione di abbreviare è più forte:

- **specifica dei tipi di dato** — le espressioni regolari vanno scritte davvero, i campi dei
  tipi strutturati elencati tutti, i vincoli sui valori espressi
- **vincoli esterni** — vanno scritti tutti, non solo il primo con un "gli altri analoghi"
- **specifiche delle operazioni** — ogni operazione richiesta ha pre, post e formula; se ne
  richiama un'altra, anche quella va specificata
- **realizzazione dei vincoli in SQL** — ogni `[V....]` dell'analisi deve arrivare a un check,
  un trigger o una politica di accesso, scritti per esteso

Se il tempo o lo spazio non bastano per tutto, si dichiara cosa manca e perché — ma non si
consegna un segnaposto facendolo passare per una risposta.

La completezza riguarda **ciò che il compito chiede**, non ciò che la skill sa fare: se nessuna
delle operazioni richieste ha un side effect di cancellazione, non se ne inventa una per
mostrarlo. Sviluppare operazioni non richieste è un errore quanto lasciarne una a metà.

## Le proporzioni di una prova vera

Completezza non vuol dire abbondanza. Misurate sulle sette prove trascritte del corpus
(`soluzioni-studenti/*TRASCRIZIONE.md`, svolgimenti veri di chi ha seguito il corso, quattro ore e
mezza di tempo), le grandezze di una prova completa stanno in questi ordini:

| Cosa | Intervallo osservato | Tipico |
|---|---|---|
| classi nel diagramma concettuale | 11-17 | ~14 |
| operazioni sviluppate in Domanda 5 | 2-6 | 3 |
| relazioni nello schema della Domanda 7 | 13-20 | ~15 |
| trigger progettati | 3-11 | 5 |
| operazioni realizzate in Domanda 8 | le stesse della Domanda 5 | — |

Le due letture pratiche:

- **la barra laterale è ciò che tiene bassi i numeri.** Le Domande 5 e 8 non sviluppano tutte le
  operazioni del diagramma, ma solo quelle dei requisiti barrati: in Città Verde sono tre su otto,
  in My Precious sei. Sviluppare le altre non è completezza, è lavoro fuori tema;
- **se il tuo diagramma ha il doppio delle classi della prova tipica, è più probabile che tu abbia
  reificato ciò che era un attributo che non che la traccia fosse il doppio più ricca.** Il
  controllo è quello di `analisi.md`: ogni classe deve avere un'identificazione, e ogni classe
  senza attributi propri e senza un ruolo strutturale è un attributo travestito.

Vale il contrario per i passi eliminatori: **niente si abbrevia là dentro**. La misura serve a
calibrare quanto *estendere*, non a giustificare quello che manca.

### Il budget, che è un vincolo e non un consiglio

La consegna d'esame **si ricopia a mano sul modulo**: una risposta giusta che non entra nella
prova non vale niente. Il budget, in righe di contenuto per domanda, viene dalle sette prove
trascritte — `tipico` è la mediana, `limite` è il tetto:

| | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | totale |
|---|---|---|---|---|---|---|---|---|---|
| tipico | 18 | 103 | 7 | 24 | 25 | 24 | 81 | 43 | ~325 |
| limite | 30 | 160 | 15 | 40 | 90 | 60 | 160 | 120 | ~675 |

**Il tetto vale per una traccia d'esame, non per un progetto.** I numeri vengono da prove con la
**barra laterale**, dove le Domande 5 e 8 sviluppano tre operazioni su otto. Un progetto non ha la
barra e le vuole tutte: lì il budget di D5 e D8 si riscala sul numero di operazioni (il tipico è
~8 righe di specifica per operazione, il limite ~30), e il totale sale di conseguenza. Misurato su
eBuy: otto operazioni, D5 82 e D8 120, con circa un terzo del tempo speso a comprimere invece che
a modellare. Non comprimere contro un tetto che non è il tuo.

**Come si usa, in tre mosse:**

1. **prima di scrivere una domanda**, dichiara in una riga che cosa ci metterai — quante classi,
   quante operazioni, quante relazioni — e confrontalo con il tipico;
2. **dopo averla scritta**, misura:
   `python3 scripts/misura-lunghezza.py soluzione.md`;
3. **se sfori il limite, tagli** — e si taglia sempre la stessa roba, in quest'ordine: la prosa che
   spiega la scelta invece di farla, gli esempi, le assunzioni ovvie, le ripetizioni fra D5 e D8.
   Non si tagliano mai vincoli, operazioni o relazioni: se sono quelli a sforare, allora il
   modello è troppo grande, e il problema era a monte.

Misurato sulle due prove in cieco più recenti: **3,4 e 3,5 volte una prova vera**, con la
Domanda 6 fino a **12 volte** il tipico — la ristrutturazione è dove si dilaga di più, perché è
facile riscrivere per esteso quello che il diagramma dice già.

## Il flusso di lavoro

Una traccia d'esame chiede l'intera pipeline in otto domande. La struttura completa, con
tempi e convenzioni del modulo risposte, è in `__BDD2_ROOT__/corpus/STRUTTURA-ESAME.md`.

```
ANALISI CONCETTUALE                    PROGETTAZIONE
 1. Raffinamento requisiti  (non valutata)   6. Ristrutturazione + domini SQL
 2. Diagramma UML + specifiche      (*)      7. Schema relazionale con vincoli   (*)
 3. Diagramma use-case                       8. Specifiche realizzative          (*)
 4. Segnature delle operazioni
 5. Specifiche operazioni in FOL    (*)
```

I **progetti** del corso numerano gli stessi passi come "Passo A.1, A.2, A.3, A.4" e li
consegnano a tappe: A.1 copre il raffinamento e il primo diagramma, A.2 le specifiche di classi
e tipi di dato, A.3 gli use-case con le loro specifiche, A.4 la revisione complessiva. È la
stessa pipeline delle Domande 1-5, spezzata diversamente: se una consegna nomina un Passo, mappa
sui contenuti, non sulla numerazione.

Segui l'ordine. Ogni passo consuma l'output del precedente, e saltarne uno si paga più a
valle: uno schema relazionale prodotto senza aver prima ristrutturato è quasi sempre
sbagliato.

Se l'utente chiede un solo passo, fai quello — ma verifica di avere l'**input** che gli serve, e
se manca ricostruiscilo brevemente prima, riportandolo nella risposta perché sia leggibile:

| Passo | Ha bisogno di |
|---|---|
| Domanda 5 | il diagramma e le specifiche della Domanda 2 |
| Domanda 6 | il diagramma concettuale e i vincoli esterni |
| Domanda 7 | il diagramma **ristrutturato** |
| Domanda 8 | lo **schema relazionale**, e le specifiche concettuali della Domanda 5 |

**Quando l'input arriva incompleto**, e capita spesso — le soluzioni ufficiali del corso sono
dichiaratamente parziali, un diagramma può avere una molteplicità illeggibile, un elenco di
vincoli può chiudersi con *"gli altri per esercizio"* — non ti fermi e non tiri a indovinare in
silenzio. Apri la risposta con un paragrafo che **elenca le lacune**, per ognuna dà la
ricostruzione più difendibile con la sua motivazione, e prosegui su quella base. Il resto della
risposta si appoggia a quel paragrafo. È la stessa regola dell'assunzione dichiarata, applicata
al rapporto fra un passo e il precedente invece che ai requisiti.

**Quando due requisiti si contraddicono** — e capita, le tracce sono scritte a mano — non si
sceglie in silenzio e non ci si blocca: si modella il **nucleo comune** alle due letture, si
dichiara il conflitto citando le due frasi, e si adotta la lettura che serve ai **requisiti
barrati**, perché è quella su cui si viene valutati nelle domande eliminatorie. Un conflitto
dichiarato è una risposta; un conflitto risolto in silenzio è una scelta che il correttore legge
come svista.

### Il file di lavoro: `controlli.md`

Un passo che non produce niente è un passo che viene saltato — è già successo, con il controllo
dei contenitori: la regola c'era e non scattava. Quindi i controlli che non hanno un artefatto
proprio se ne fanno uno. Accanto alla soluzione tieni **`controlli.md`, che non si consegna**, e
lo riempi mentre lavori:

```
Ambito (barra): requisiti 4, 7, 8 — dichiarati dall'utente e confermati
Contenitori nella traccia: padiglione → classe · casello → attributo (il nome del casello *è*
  la località, lo dice la traccia) · carrello → classe · cronologia → classe
Precedenti cercati: "capienza" in soluzioni-ufficiali → QuickHospital [V.Stanza.capienza]
Vincoli: V.a → trigger T1 · V.b → check · V.c → (ancora niente)
Operazioni: pubblica_video D4 ✓ D5 ✓ D8 ✓ · censura_video D4 ✓ D5 ✓ D8 —
```

Non è documentazione: è il posto dove la decomposizione **diventa visibile**, e quindi
verificabile in trenta secondi. Le colonne vuote sono la lista delle cose da finire.

### Passo zero: cercare i precedenti, sempre

**Non è il ripiego di quando sei in dubbio: è il primo passo di ogni domanda.** Il corpus contiene
la stessa situazione di modellazione risolta più volte, e una convenzione vista in due soluzioni
vale più di qualunque ragionamento. Prima di scrivere una risposta, cerca chi l'ha già scritta.

Si cerca per **forma del requisito**, non per dominio: le parole della traccia non ricompaiono
altrove, la struttura sì. «Capienza più finestra temporale», «sequenza ordinata», «due ruoli
distinti sulla stessa coppia di classi», «valore corrente contro valore storico», «stato che porta
struttura diversa» — sono i pattern che ricorrono, e ognuno ha già il suo precedente.

Le fonti, in ordine di autorevolezza — quando due si contraddicono, vince quella più in alto:

| # | Fonte | Che cosa ti dà | Dove |
|---|---|---|---|
| 1 | **teoria** | che cosa *significa* un costrutto, e i suoi limiti sintattici | `teoria/` |
| 2 | **modulo risposte** | che cosa il compito chiede, campo per campo, e l'alfabeto della FOL | `docente-ufficiale/modulo-risposte-UML-2024-06-05.md` |
| 3 | **soluzioni ufficiali e diagrammi del docente** | come il corso modella davvero: convenzioni, molteplicità, forma | `soluzioni-ufficiali/`, `diagrammi/` |
| 4 | **correzioni, sbarramenti, elenco errori** | che cosa un correttore segna come errore, e le verità oggettive | `docente-ufficiale/` |
| 5 | **esercitazioni** | il caso tipico isolato, spesso più vicino al tuo di una soluzione intera | `esercitazioni/` |
| 6 | **prove d'esame trascritte di studenti** | come si compila il modulo nei tempi, e quali trappole scattano davvero | `soluzioni-studenti/*-TRASCRIZIONE.md` |

Le ultime **non sono autorità**: nessuno le ha corrette, e le note di lettura in fondo a ognuna
elencano gli errori dei loro autori. Servono a un'altra cosa — vedere quanto si riesce a scrivere
in 45 minuti, come si riempiono i riquadri delle specifiche, quali domande gli studenti lasciano
in bianco. Un precedente lì vale come indizio, mai come prova; un precedente in `soluzioni-ufficiali/`
vale come prova.

In pratica, due o tre `grep` prima di ogni domanda difficile:

```bash
C=__BDD2_ROOT__/corpus
grep -ril "sovrappo"  $C/soluzioni-ufficiali $C/teoria      # vincoli temporali
grep -ril "capienza\|posti"  $C/soluzioni-ufficiali $C/diagrammi
grep -ril "sorted\|ordinat"  $C/teoria $C/soluzioni-ufficiali
grep -rl  "specializza"       $C/diagrammi                  # ruoli distinti
```

**Un livello per volta, e ci si ferma al primo che risponde.** Un `grep` su più cartelle insieme
restituisce righe che hanno perso la propria autorità: una trascrizione di studente e una
soluzione ufficiale escono identiche, e la gerarchia qui sopra non serve più a niente. Prima
`soluzioni-ufficiali/` e `diagrammi/`, poi `esercitazioni/`, e solo alla fine
`soluzioni-studenti/` — che è un indizio, mai una prova.

Poi si legge il precedente **intero**, non la riga che il grep ha trovato: quello che serve è
quasi sempre nel contesto — quale molteplicità ha scelto, quale vincolo ha scritto accanto, cosa
ha lasciato al diagramma.

**Il precedente guida la risposta, ma non ci entra.** Nel documento consegnato non si scrive «come
in QuickHospital» né si cita il corpus: è un compito d'esame, non una relazione. La traccia del
precedente resta nelle scelte, non nel testo.

### Leggere il testo: le tracce d'esame sono immagini, le esercitazioni no

Sono due casi diversi e vanno trattati diversamente.

**Le tracce d'esame** (`tracce-esame/`, 40 file `BD2_<data>_<Nome>.pdf` più `INDICE.md`) sono
PDF di sole immagini — 37 su 40 non hanno alcun livello di testo — e vanno lette con Read a pagine (`pages: "1"`, poi
"2"…). Vanno lette come immagini **anche se il testo ci fosse**: i requisiti le cui operazioni
si sviluppano nelle Domande 5 e 8 sono contrassegnati da una **barra verticale nera nel margine
sinistro**, un segno puramente grafico. Perderlo significa sviluppare le operazioni sbagliate,
cioè fallire due dei quattro passi eliminatori. Prima di iniziare, **fatti dire dall'utente dove
sono le barre** (vedi sotto) e ripeti l'ambito che ne ricavi.

**La barra restringe anche il diagramma, ma solo nelle operazioni.** Il modulo chiede alla
Domanda 2 le operazioni di classe *«necessarie a modellare i requisiti contrassegnati dalla barra
laterale»*: quindi nel diagramma non si mettono operazioni che nascono da funzionalità non
barrate. Non è una sottigliezza — ogni operazione disegnata va poi specificata con pre, post e
formula, e riempire il diagramma di operazioni derivate costa tempo su una domanda eliminatoria
senza aggiungere niente. Classi, attributi, associazioni e vincoli restano invece su tutto il
dominio.

**Per il resto la barra restringe le operazioni, non il modello.** Il modulo risposte la nomina solo per le
Domande 5 e 8 (*"le operazioni definite per modellare i requisiti contrassegnati dalla barra
laterale"*): il diagramma della Domanda 2, i suoi vincoli esterni, la ristrutturazione e lo
schema relazionale coprono **l'intero dominio**, requisiti barrati e non. Un vincolo di capienza
che serve solo a una funzionalità non barrata va scritto lo stesso: senza, lo schema è
incompleto.

**Chi decide dov'è la barra: l'utente.** La traccia la ha davanti lui, e la legge meglio di
qualunque analisi dei pixel. Il protocollo viene prima di ogni altra cosa:

1. l'utente manda la **foto della traccia** e **dichiara dove le barre cominciano e finiscono**
   («dal capoverso *Il sistema deve permettere…* fino a *…entro sette giorni*»);
2. tu **ripeti l'ambito in una riga** — quali requisiti sono barrati e quali no — e **aspetti
   conferma** prima di scrivere qualunque cosa;
3. l'ambito confermato apre `controlli.md` ed è ciò che governa le Domande 5 e 8.

Non dedurre la barra dall'immagine quando l'utente può dirtela: è l'unico passo del sistema
**senza nessuna misura alle spalle**, e governa due domande eliminatorie. Il costo di chiedere è
una riga; il costo di sbagliarla è la prova.

Quando invece lavori **da solo** su una traccia del corpus — una prova, un ripasso, un benchmark —
la barra va cercata nell'immagine, e come si fa (com'è fatta, cosa non è, come si misura su una
foto storta) sta in **`references/barra.md`**.

**I progetti del corso non hanno la barra laterale**: lì le operazioni si sviluppano tutte.

**Le esercitazioni** non hanno né immagini né barra laterale: sono **già in markdown** nel
corpus, una per file, in `BDD2-corpus-nuovo/esercitazioni/` (`E.A.1.x` analisi, `E.A.3.x` FOL,
`B.2.2.x` SQL), e le soluzioni ufficiali in `soluzioni-ufficiali/`. Guarda lì per primo (`ls` o
`grep -l` sul nome dell'esercitazione); i **16 progetti** stanno in `progetti/`.

Nel dubbio, `pdffonts` sul file: nessun font elencato significa PDF di immagini.

## I passi

I template esatti, con esempi presi dalle soluzioni ufficiali, sono in file separati. Leggi solo
quelli che servono al compito che hai davanti: caricarli tutti è sprecato.

| Compito | Cosa leggere |
|---|---|
| traccia d'esame o progetto completo | `analisi.md`, poi `progettazione.md`, e `fol.md` per le formule |
| esercitazione `E.A.1.x` (chiede 2-3 passi) | `analisi.md`, sezioni Domande 1-2, più `fol.md` per i vincoli esterni |
| solo analisi concettuale (Domande 1-5) | `analisi.md` + `fol.md` |
| solo progettazione (Domande 6-8) | `progettazione.md` |
| esercizio di FOL puro | `fol.md` |
| **esercitazione SQL** | `sql.md` — risultati attesi, vincoli sul costrutto, ambiguità ricorrenti, comandi |
| serve un esempio o una fonte | `corpus.md` |
| dubbi su cosa il correttore consideri errore | `errori.md` |
| devi trovare la barra laterale **da solo**, senza l'utente | `barra.md` |
| **correggere una soluzione** invece di produrne una | `correzione.md` |

La sintassi della logica del primo ordine usata nel corso, con i pattern ricorrenti (vincoli di
molteplicità, identificazione, generalizzazioni disjoint/complete, side effect con ALPHA) è in
**`references/fol.md`**. Consultala ogni volta che scrivi una formula: la notazione del corso ha
convenzioni proprie che non coincidono con la FOL "da manuale".

### Domanda 2 — il diagramma è il cuore di tutto

Produci il diagramma come **testo strutturato** (classi con attributi e tipi, tabella delle
associazioni con le molteplicità ai due estremi, generalizzazioni con i vincoli), non come
disegno ASCII. È la forma in cui le soluzioni ufficiali sono utilizzabili, ed è quella che
l'utente può poi ridisegnare in Visual Paradigm.

Il formato testuale non è la consegna finale: si converte automaticamente in un diagramma
disegnato (vedi *Come si consegna* più sotto). Non generare mai file `.vpp`.

Le scelte di modellazione si giudicano contro i requisiti, non contro l'eleganza. Due criteri
che i correttori applicano davvero:

- **Generalizzazione completa e disjoint solo se i requisiti o il senso comune la impongono.**
  Il test: un'istanza di A potrebbe mai essere anche di B? Se sì, niente disjoint. Un bibliotecario può
  benissimo essere anche paziente.
- **Meglio un attributo in più che un vincolo in più.** Se un vincolo esterno nasce solo per
  compensare un dato che la traccia ha dimenticato di chiedere, aggiungi il dato. I requisiti
  vanno letti in modo critico: dati ovviamente necessari vanno modellati anche se non scritti.
- **Un dato derivabile è un'operazione, non un attributo.** Il raffinamento deve eliminare le
  ridondanze, e un valore calcolabile dagli altri è ridondante: il numero di dipendenti si
  ricava dall'associazione, il saldo residuo dal saldo iniziale meno i consumi. Il caso più
  insidioso è quello dei dati che **variano col tempo**: si memorizza la data da cui derivano e
  si deriva il resto. Gli anni di servizio si memorizzano come `assunzione: Data`, con
  `anni_servizio()` come operazione — un numero di anni salvato in colonna invecchia da solo.
- **Una sottoclasse derivabile è un'operazione, non una generalizzazione.** Se l'appartenenza a
  una sottoclasse dipende interamente da dati già presenti — un lettore è "moroso" solo in
  base al suo tipo di prestito — la classificazione è ridondante come la è un attributo calcolabile:
  meglio un'operazione booleana sulla superclasse. La generalizzazione si giustifica quando la
  sottoclasse porta attributi, associazioni o operazioni proprie. È una decisione che cade nella
  Domanda 2, quindi eliminatoria: qualunque strada scegli, motivala contro i requisiti.
- **Una classe associativa impedisce i link duplicati.** Modellare `Prestito` o `Ricollocazione`
  come classe associativa fra due classi è tentante, ma vincola a **una sola istanza per coppia**: un
  lettore non potrebbe prendere in prestito due volte la stessa copia, e una copia non potrebbe
  passare due volte per la stessa sede. Se i duplicati hanno senso, reifica in una classe a sé con due
  associazioni binarie. La classe associativa va bene quando la coppia è davvero unica.
- **Un insieme di valori fissi o condivisi è spesso una classe, non un attributo stringa.** Le
  soluzioni ufficiali hanno classi `Modello`, `Tipologia`, `CasaProduttrice`, `Città`, `Nazione`
  dove la specifica diceva soltanto "modello", "tipo", "città". Ma non è una regola cieca: il
  criterio per decidere fra classe e tipo di dato sta in `references/analisi.md`, sezione
  *"Insiemi di valori chiusi"*, e in sintesi è **l'uso che ne fanno operazioni e associazioni**.

  Il caso in cui il corso è più costante è la **geografia**, e qui non c'è proporzionalità che
  tenga: **12 soluzioni ufficiali su 12** modellano `Città` associata a `Nazione` (o a `Regione`,
  e quella a `Nazione`) come classi, e **nessuna** usa un attributo `citta: Stringa` né una
  classe `Luogo` che le accorpa. Vale anche quando la città compare una sola volta come dettaglio
  di un indirizzo: QuickHospital ha `Città` e `Nazione` come classi per il solo indirizzo del
  paziente.

  **La stessa forma vale per ogni gerarchia di contenimento, non solo per la geografia.** Un
  padiglione che contiene piani, che contengono settori, che contengono stanze, che contengono
  letti è la stessa catena di `Città` → `Nazione`: **una classe per livello**, legate da
  associazioni `1..1` sul lato del contenitore, con l'identificazione esterna che si propaga lungo
  la catena. Schiacciare i livelli intermedi in attributi della classe più interna — `Stanza` con
  `piano: Intero` e `settore: Intero` — **perde l'identificazione**: due stanze possono stare sullo
  stesso piano e nello stesso settore, e quegli attributi non identificano più niente. Il segnale
  che stai schiacciando: la classe più interna resta senza identificatore e ti viene voglia di un
  surrogato già nel concettuale.

  **Vale anche quando la traccia li chiama attributi.** QuickHospital dice testualmente *«le stanze
  hanno un piano ed un settore (interi positivi)»*, e il concettuale ufficiale ne fa comunque le
  classi `Piano` e `Settore` dentro `Padiglione`. È la stessa mossa della geografia, dove le
  soluzioni hanno `Città` e `Nazione` là dove la specifica diceva soltanto «città»: il corso legge
  il contenimento come struttura, non come etichetta.

  **La regola dice come modellare la geografia, non di aggiungerla.** Se i requisiti non
  nominano nessun luogo, non ci vanno né `Città` né `Nazione`: l'ufficiale di Accademia 2 non ne
  ha nessuna delle due. Se invece i requisiti si fermano alla regione, la catena si chiude
  comunque su `Nazione` — l'ufficiale di Università 2 ha `Città`, `Regione` **e** `Nazione` pur
  parlando solo di città e regione. Il criterio è: se un luogo c'è, è una classe, e la catena
  arriva fino alla nazione; se non c'è, non si inventa.

### Domanda 5 — la logica

Le specifiche delle operazioni usano **lo stesso vocabolario della Domanda 2**: i simboli di
predicato sono le classi, gli attributi e le associazioni già definiti. Introdurre simboli nuovi
qui è un errore, perché rompe il legame tra diagramma e specifica.

**Se ti serve un simbolo che nel diagramma non c'è, il posto dove ripararlo è la Domanda 2**: ci
si torna e ci si aggiunge l'attributo, l'associazione o l'operazione, e poi la formula lo usa. Il
divieto non è «arrangiati»: senza questa uscita la strada che si apre da sola è inventare il
simbolo e tacere, che è l'errore misurato su TimeBank — un simbolo mai dichiarato, né attributo né
costante. `verifica-consegna.py` lo trova, ma il momento per accorgersene è adesso.

L'errore più comune, e uno di quelli che i correttori segnalano per primi: **definire un insieme
senza legare la variabile alla sua classe**. Se scrivi l'insieme dei letti occupati senza mai
nominare `Letto(x)` nella formula, quell'insieme non è "i letti occupati" — è l'insieme universo
o l'insieme vuoto. Ogni variabile quantificata va tipata.

Altro punto ricorrente: le **precondizioni riguardano i parametri effettivi**, non un
esistenziale generico. "Il letto dato in input è libero", non "esiste un letto libero".

### Domanda 7 — schema relazionale

La risposta è la **notazione testuale** del corso, che è quella che il modulo risposte chiede, più
il progetto dei trigger in pseudo-codice. Il **DDL SQL** che la realizza si scrive e si esegue —
è l'unico modo di accorgersi di un ciclo di foreign key o di un check che non compila — e si
allega **in appendice**: è una verifica, non la risposta. Vedi `progettazione.md`, che dà la forma
di entrambi.

Ogni relazione va tracciata all'elemento UML da cui deriva (il modulo risposte chiede di
indicare `Derivante da: classe | associazione`). Chiave primaria sottolineata, attributi che
possono essere NULL contrassegnati con `*`.

I vincoli esterni scritti in FOL nell'analisi **non restano in forma logica**: la fase di
progettazione chiede la loro realizzazione come condizioni SQL sempre verificate — `check`,
trigger, o politiche di accesso ai dati. Per ciascuno scegli la strategia e motivala.

### Domanda 8 — specifiche realizzative

Pseudo-codice con SQL immerso, non SQL puro. Per ogni operazione servono: segnatura con i
**domini SQL** degli argomenti e del ritorno, l'algoritmo, e la dichiarazione di **dove va
implementata — nel DBMS o nel back-end**.

L'algoritmo deve verificare le precondizioni e garantire le postcondizioni scritte alla Domanda
5: è quella la specifica a cui deve essere conforme, non una reinterpretazione libera.

Le operazioni che leggono e poi scrivono vanno in transazione, perché tra le due query il
database può cambiare sotto i piedi.

## Verificare l'SQL invece di fidarsi

Esiste un PostgreSQL con i due database di esempio del corso già caricati. **Ogni query o
comando SQL non banale va eseguito prima di essere consegnato** — è il passo eliminatorio dove
un errore è più facile da commettere e più facile da evitare.

```bash
docker start bdd2pg 2>/dev/null || docker run -d --name bdd2pg \
  -e POSTGRES_HOST_AUTH_METHOD=trust -p 55432:5432 postgres:16-alpine
docker exec bdd2pg psql -U postgres -d accademia -c "SELECT ..."
```

**Eseguire è una verifica, non la forma della risposta.** Il modulo risposte ufficiale è
esplicito su cosa va consegnato: alla Domanda 7 ogni vincolo esterno vuole *"un trigger che lo
implementi, definendo: (a) gli eventi da intercettare; (b) quando intercettare tali eventi; (c)
la relativa funzione **in pseudo-codice con SQL immerso**"*, e alla Domanda 8 *"un algoritmo in
pseudo-codice con SQL immerso"*. Il `create function ... language plpgsql` completo non è quello
che il compito chiede — è lo strumento con cui tu controlli che il tuo pseudo-codice regga prima
di consegnarlo. Scrivilo, eseguilo, e consegna il progetto in pseudo-codice; il codice reale si
allega solo se resta tempo, o se l'utente lo chiede perché gli serve un database funzionante.

**Eseguire non basta: il risultato va interpretato.** Una query che gira senza errori ma
restituisce zero righe, o un numero di righe implausibile, quasi sempre non ha un bug di
sintassi — ha un bug di comprensione del requisito. Prima di consegnarla, chiediti se quel
risultato ha senso per la domanda posta, e in caso contrario torna al testo.

**Se il compito è un'esercitazione SQL del corso, leggi `references/sql.md`**: i risultati attesi
sono stampati nel PDF stesso, il titolo vincola quale costrutto usare, e c'è un elenco delle
formulazioni ambigue che cambiano il risultato. Lì stanno anche i comandi per ricaricare i
database e per eseguire un file intero.

## Quando non sei sicuro: cerca, poi deduci, mai indovina

Questa skill è un distillato del metodo, non il corso. Davanti a un caso che non trova risposta
qui, l'ordine è sempre questo, e non va saltato:

1. **Cerca un caso analogo già risolto nel materiale**, con la gerarchia di fonti e i comandi del
   *Passo zero* qui sopra. Quasi ogni situazione di modellazione ricorre da qualche parte, e un
   precedente vale più di un ragionamento, perché mostra la convenzione effettiva del corso.
2. **Se non lo trovi, deduci dalla teoria.** La fonte è la slide, non l'intuizione né
   un'analogia con altre metodologie di progettazione. Le slide dicono cosa un costrutto
   *significa*, e da lì la risposta si ricava.
3. **Non inventare.** Se dopo i primi due passi resta un'ambiguità, dichiarala: scrivi
   l'interpretazione scelta e perché. Un'assunzione esplicita è una risposta; una convenzione
   inventata e taciuta è un errore che il correttore trova.

Le slide, tutte in markdown in `BDD2-corpus-nuovo/teoria/` (con le pagine che hanno figure
rese come PNG in `teoria/figure/`), sono organizzate
così: `A.1` per i costrutti UML (classi, associazioni, molteplicità, association class,
identificazione, generalizzazione, operazioni, specializzazioni, use-case), `A.2` per la forma
dei documenti di specifica, `A.3` e `A.4` per la logica, `B.1` per il modello relazionale,
`B.2.2` per l'SQL, `B.3.1` per ristrutturazione e traduzione, `B.3.2` per la progettazione delle
funzionalità.

```bash
grep -ril "specializzazione di attributi" __BDD2_ROOT__/corpus/teoria/
```

Due avvertenze. Il **syllabus elenca argomenti che le slide non coprono** — la stima dei costi
con tavola dei volumi e degli accessi, e l'aggiunta controllata di ridondanza, non compaiono in
nessuna slide disponibile: se una traccia li chiedesse, dillo invece di improvvisare. E le slide
più vecchie usano l'ER: vale la notazione, non il diagramma (vedi `NOTAZIONE.md`).

Poi, per la forma concreta, guarda come il corso ha risolto un caso analogo: il corpus contiene
soluzioni ufficiali complete, e `references/corpus.md` dice dove cercare.

Le due fonti più diverse tra loro e più istruttive:

- **QuickHospital** è l'unica soluzione ufficiale che copre tutta la pipeline, dall'analisi alla
  progettazione delle operazioni. È il riferimento per la forma di ogni artefatto.
- Le **correzioni di un tutor** in `docente-ufficiale/progetti/QuickHospital-correzioni-tutor.md`
  dicono cosa un correttore segna come errore, e perché. Vale più di dieci soluzioni corrette:
  mostra i confini, non solo il centro.

Gli errori tipici e i criteri di valutazione sono raccolti in **`references/errori.md`**.

## Come si consegna

**L'output di un esercizio è un unico file HTML**, che contiene il diagramma UML disegnato e
tutto il resto della soluzione. Se il compito non produce un diagramma delle classi — una
Domanda 8 da sola, un'esercitazione SQL — il markdown basta: non c'è nulla da disegnare. Scrivi prima la soluzione in markdown, nel formato testuale
descritto qui, poi componila:

```bash
python3 __BDD2_ROOT__/corpus/scripts/componi.py soluzione.md -o <cartella>
```

**Prima di comporre, i controlli meccanici.** Non sono facoltativi e costano dieci secondi:

```bash
python3 __BDD2_ROOT__/corpus/scripts/verifica-consegna.py soluzione.md
python3 __BDD2_ROOT__/corpus/scripts/misura-lunghezza.py soluzione.md
```

Il primo non dà voti: stampa **le cose da guardare**. Cerca i tipi non di base senza specifica, le
classi senza identificazione, le operazioni disegnate e mai specificate, i `[V....]` dell'analisi
che non arrivano alla progettazione, le variabili quantificate e non legate da nessun atomo, i
simboli usati nelle formule e mai dichiarati nella Domanda 2, le intestazioni che `componi.py`
inghiottirebbe, e le operazioni specificate alla Domanda 5 e non realizzate alla 8. Esiste perché
i controlli scritti in prosa **non scattano da soli**: la regola sui contenitori era in
`analisi.md` e la skill l'ha ignorata in tre confronti su tre. Un rilievo può essere un falso
positivo — si guarda e si va avanti; quello che non si può fare è non guardarlo.

Restano fuori i tre controlli che una macchina non fa, e sono quelli che il benchmark ha visto
fallire davvero: **i contenitori** (si fa sulla traccia, non sulla soluzione), **l'ambito della
barra**, e **il caso vuoto** di ogni «solo / tutti / nessun altro».

Il file che ne esce è autosufficiente e contiene **tutti** i diagrammi della soluzione come SVG
incorporati, ognuno sotto l'intestazione della sua sezione: il concettuale della Domanda 2, gli
**use-case** della Domanda 3 e il **ristrutturato** della Domanda 6. Si apre con un doppio clic e
si stampa in PDF dal browser.

**Il diagramma degli use-case si scrive nel formato del corpus**, lo stesso che `converti-xml.py`
produce dagli export dei progetti ufficiali, sotto un'intestazione `## Use case`:

```
Attori: `Cliente`, `Personale`, `Manager`

Use case: `GestioneClienti`, `Reportistica`

- `Personale` generalizza `PersonaleVendita`, `Tecnico`
- `Cliente` — `GestioneClienti`
- `Manager` — `Reportistica`
```

La riga `generalizza` fra attori non compare nei `.vpp` ufficiali ma è ammessa e viene disegnata
come specializzazione: serve quando la gerarchia degli attori rispecchia quella delle classi.

**Trappola del livello delle intestazioni.** `componi.py` taglia le sezioni del disegno fino alla
successiva intestazione di **pari livello**: se dopo `## Generalizzazioni` metti i tipi di dato o
le specifiche di classe sotto `###`, spariscono dalla consegna insieme al diagramma, e finiscono
per di più dentro il sorgente passato al renderer. Tutto ciò che segue una sezione del diagramma
va a livello `##`.

**E il disegno si àncora all'ultima intestazione che non è del diagramma**: se togli
`### Diagramma ristrutturato` prima delle sue `## Classi` — magari per guadagnare una riga di
budget — il ristrutturato scivola sotto la sezione precedente e finisce nel posto sbagliato. Ogni
blocco di diagramma vuole la sua intestazione sopra, e quella riga non si taglia.

### Cosa NON si scrive nel documento

`componi.py` **toglie dal documento le sezioni che il disegno già mostra**: `## Classi` con i suoi
attributi, `## Associazioni`, `## Generalizzazioni`, `## Classi associative`, `## Use case`, e i
blocchi `#### Attributi` nella specifica delle classi. Restano nel markdown, perché è da lì che si
disegna, ma non finiscono nella consegna: ripetere a parole un elenco che sta nel diagramma è
rumore, e un correttore lo legge come riempitivo.

Quindi **dopo un diagramma non si riscrive mai l'elenco delle classi**. Quello che resta, e che il
disegno non dice, è: la specifica dei tipi di dato, le **operazioni** di ogni classe con pre, post
e formula, i vincoli esterni, le assunzioni.

### La struttura del documento consegnato

È questa, e non cambia:

1. **Domanda 1 — Raffinamento dei requisiti.** Gruppi numerati **per natura**, uno per concetto:
   clienti, personale e programma fedeltà sono tre gruppi distinti, non uno solo perché "riguardano
   le persone". Numerazione gerarchica `1.` / `1.1` / `1.1.1`, mai oltre tre livelli, un titolo di
   terzo livello per gruppo.
2. **Assunzioni**, in una sezione propria, ognuna col suo perché.
3. **Domanda 2** — il diagramma, poi i tipi di dato, poi la specifica delle classi (sole
   operazioni), poi i vincoli esterni.
4. Le domande successive nell'ordine.

Dentro la specifica di una classe, blocchi separati e sempre nello stesso ordine — `#### Operazioni`,
`#### Vincoli` — e ogni **formula sta in un blocco di codice recintato**, spezzata su più righe: il
quantificatore e le sue variabili su una riga, ogni congiunto rientrato sulla sua, `-->` e `<-->` a
inizio riga e mai in coda. Una formula lunga scritta di fila dentro una frase non si legge.

I **vincoli esterni** vanno uno per sottosezione, intestazione uguale al nome fra parentesi quadre,
sotto l'enunciato in italiano, sotto la formula nel suo blocco.

**Nel documento non si scrive niente del processo**: non chi o cosa ha prodotto quale parte, non i
percorsi dei file di lavoro, non i riferimenti alle iterazioni. È un compito d'esame, non un
rapporto di lavorazione.

Serve a una cosa precisa: mettere la propria soluzione accanto a quella ufficiale e annotare a
mano cosa non va. Per questo il markdown resta accanto all'HTML — è il file che si corregge, e
basta ricomporre.

Se serve solo il diagramma, `scripts/uml2png.py` produce un PNG o un SVG a sé. Funziona anche
sui diagrammi ufficiali in `BDD2-corpus-nuovo/diagrammi/`, che sono nello stesso formato: utile per
affiancarli. **Ma vuole un diagramma solo per file**: su una soluzione d'esame, che contiene il
concettuale e il ristrutturato, fonde i due blocchi e PlantUML si ferma. Per una soluzione intera
si usa `componi.py`, che li spezza per sezione.

## Lingua e forma

Tutto in italiano, con la terminologia del corso: *ennupla* non "tupla", *vincolo esterno* non
"business rule", *specifica realizzativa* non "implementazione".

La forma delle risposte imita i documenti di specifica ufficiali: **testo strutturato con
rientri, non prosa**. Le tabelle non sono vietate — il formato del diagramma ne prevede una per
le associazioni, ed è quella che rende il risultato confrontabile — ma servono a dati
tabellari, non a impaginare un discorso.

---

## Gli strumenti meccanici

`RUNBOOK-ESAME.md`, nella radice del corpus, raccoglie i controlli meccanici e i comandi che
tolgono di mezzo il lavoro ripetitivo quando ci si esercita su una traccia — traccia in immagini,
ricerca dei precedenti, esecuzione dell'SQL, composizione del risultato — con i tempi misurati e i
modi in cui la macchina può piantarsi.

## Manutenzione della skill

`test-regressione.py` è la fixture di regressione: verifica che le regole pagate con i test in
cieco siano ancora scritte dove devono, che ogni percorso citato esista, che il corpus abbia le
grandezze attese e che nessuna figura richiamata dalla teoria manchi.

```bash
python3 test-regressione.py                 # usa __BDD2_ROOT__/corpus
python3 test-regressione.py /altro/corpus
```

Si lancia dopo ogni modifica alla skill o al corpus. Quando una correzione nuova entra in una
reference, si aggiunge la riga corrispondente in `INVARIANTI`: è ciò che impedisce a una
riscrittura successiva di cancellarla senza accorgersene.
