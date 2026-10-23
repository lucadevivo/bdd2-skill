# Esercitazioni SQL

Le dieci esercitazioni SQL del corso (Accademia 3-8, Cielo 1-5) girano su due database di
esempio, e hanno una proprietà che le rende diverse da tutto il resto: **il PDF contiene i
risultati attesi**. C'è una verità di riferimento oggettiva, quindi non c'è motivo di consegnare
una query non verificata.

## Prima di scrivere una riga

1. **Leggi i risultati attesi.** Sezione *"Risultati Attesi delle Query"* nel PDF stesso. Dicono
   quante righe aspettarsi, quali colonne, e con quali alias — informazioni che il testo della
   domanda spesso non dà.
2. **Ispeziona lo schema reale**, non quello delle slide (vedi sotto: i PDF hanno refusi).
3. **Guarda i dati.** Poche decine di ennuple: contarle a mano risolve in anticipo le ambiguità
   del testo, invece di scoprirle dopo.

Le esercitazioni sono già in markdown in `BDD2-corpus-nuovo/esercitazioni/`, una per file, e le
soluzioni ufficiali in `soluzioni-ufficiali/`. Guarda lì per primo. Il ragionamento a voce sulle
query, con gli errori tipici commentati dal docente, è in `videolezioni/`.

## Il confronto con i risultati attesi è a occhio

`pdftotext` distrugge tipograficamente quelle pagine: le intestazioni escono come
`c o d i c e _ v o l o`, i nomi come `G i n e v r a`, i separatori diventano trattini Unicode.
Vale anche per il testo pre-estratto, che non è un rimedio. **Un `diff` meccanico è impossibile**:
si confrontano numero di righe e valori leggendo. Non perderci tempo a cercare una via pulita.

Due conseguenze:

- **Il confronto è sull'insieme delle ennuple, non sulla sequenza.** L'ordine delle righe attese
  non è significativo, salvo un `ORDER BY` chiesto dalla domanda. Non provare a dedurre la query
  del docente dall'ordine: dipende dal piano di esecuzione.
- **Gli alias vanno riprodotti** quando l'intestazione attesa li mostra (`codice_volo`, `scalo`).

### I blocchi "Versione 2"

Alcune esercitazioni (Accademia 8, Cielo 4) riportano per la stessa domanda **due blocchi di
output**, marcati `1) Versione 2`, `3) Versione 2` e così via. Sono le due formulazioni
alternative che la sottounità vuole far esercitare — tipicamente una con annidamento nella
`WHERE` e una con outer join o aggregato.

Quando ci sono, **produci entrambe le versioni**, ciascuna conforme al proprio output atteso.
A volte le due proiezioni differiscono (in Accademia 8 la seconda versione della domanda 3
aggiunge `posizione`): non è una contraddizione da risolvere scegliendo, sono due query diverse
e ognuna riproduce la sua.

## Quale costrutto usare

Il titolo dell'esercitazione dice quale costrutto va esercitato, e va rispettato in due
direzioni.

**In negativo:** "Interrogazioni su singola tabella" **vieta** join e sottoquery. Diverse domande
di quelle esercitazioni sono formulate apposta per indurti a un join che non serve ("di tutti gli
strutturati", quando ogni persona è già uno strutturato).

**In positivo:** nell'esercitazione su un costrutto, quel costrutto si usa **anche dove sarebbe
ridondante**, purché non alteri il risultato. In "Interrogazioni su tabelle multiple" una domanda
rispondibile con la sola tabella dei voli va comunque scritta con il join sulla compagnia:
l'esercizio chiede di esercitare il join, non di trovare la formulazione più corta. Qui la regola
di minimalità di `errori.md` non si applica — torna a valere in sede d'esame, dove nessun
costrutto è prescritto.

**Quando titolo e pagina "Obiettivi" divergono, vince il titolo.** La pagina Obiettivi elenca
spesso tutto ciò che è stato visto fino a quel punto del programma (aggregati, raggruppamenti,
sottoquery nella `FROM`, `WITH`…): è il perimetro di ciò che *puoi* usare, non di ciò che
*devi*. Se il titolo nomina due costrutti ("annidamenti nella `WHERE` e outer join") non tutte le
domande devono usarli entrambi: alcune non hanno una formulazione sensata con uno dei due, e in
quel caso si sceglie l'altro senza forzare.

## Le ambiguità che cambiano il risultato

Queste formulazioni ricorrono nelle tracce e ognuna ha due letture che danno risultati diversi.
Risolvile **contando le righe attese**, che è il motivo per cui i risultati attesi si leggono
prima.

| Formulazione | Le due letture |
|---|---|
| *"terminati in data odierna"* | `fine = CURRENT_DATE` oppure `fine < CURRENT_DATE` ("già terminati"). Quasi sempre la seconda: la prima dà zero righe. |
| *"solo nei giorni in cui non avevano X"* | chi non ha **mai** avuto X rientra per vacuità, o va escluso? In Accademia 8 è la differenza fra 20 righe e 6. |
| *"sopra la media"* | media calcolata sui soli gruppi non vuoti, o su tutti contando zero per quelli vuoti? |
| *"non ha lavorato ad alcun progetto"* | "alcun" significa **qualsiasi**, non il progetto nominato poco prima nella frase. |
| *"tutti i dati di X"* | l'output atteso dice quali colonne: spesso include `id` anche quando la domanda dice "nome e cognome". |

**Un risultato vuoto o implausibile non è un esito, è un segnale.** Se una query gira senza errori
ma restituisce zero righe, quasi mai ha un bug di sintassi: ha un bug di comprensione. Torna al
testo prima di consegnarla.

## Eseguire

Container con i due database del corso:

```bash
docker start bdd2pg 2>/dev/null || docker run -d --name bdd2pg \
  -e POSTGRES_HOST_AUTH_METHOD=trust -p 55432:5432 postgres:16-alpine
docker exec bdd2pg psql -U postgres -lqt          # quali database ci sono
```

**Se `accademia` e `cielo` non ci sono** (container appena creato), vanno creati e popolati —
`psql -d accademia` su un container nuovo fallisce, perché il database non esiste ancora:

```bash
NM="__BDD2_ROOT__/corpus/database"
for db in accademia cielo; do docker exec bdd2pg psql -U postgres -q -c "create database $db;"; done
docker exec -i bdd2pg psql -U postgres -d accademia -q < "$NM/accademia 3/domains-tables.sql"
docker exec -i bdd2pg psql -U postgres -d accademia -q < "$NM/accademia 3/constraints.sql"
docker exec -i bdd2pg psql -U postgres -d accademia -q < "$NM/accademia 3/data.sql"
docker exec -i bdd2pg psql -U postgres -d cielo -q < "$NM/cielo/domains-tables.sql"
docker exec -i bdd2pg psql -U postgres -d cielo -q < "$NM/cielo/data.sql"
```

L'ordine conta: domini e tabelle, poi i trigger, poi i dati.

**Ispeziona sempre lo schema reale prima di scrivere.** Non è un consiglio di prudenza: i PDF
contengono refusi — in Cielo 1 il `VincoloDB.5` dice `partenza references Peroporto(codice)`,
dove si intende `Aeroporto` — e PostgreSQL ripiega gli identificatori in minuscolo, quindi la
`AttivitaProgetto` delle slide è `attivitaprogetto` nel database.

```bash
docker exec bdd2pg psql -U postgres -d cielo -c "\d volo"
```

Per eseguire un file intero e catturarne l'output leggibile servono `-i` su `docker exec` (per
passare il file dall'esterno) e `-a` su `psql` (per l'echo di query e commenti):

```bash
docker exec -i bdd2pg psql -U postgres -d cielo -a -f - < query.sql > risultati.txt 2>&1
```

Per una traccia con uno schema diverso vale lo stesso principio: crea un database temporaneo,
esegui il DDL che hai scritto, e verifica che le query girino davvero.

## Quando la traccia non dice quali colonne restituire

È il caso più frequente delle esercitazioni: *«quali sono i WP che hanno lo stesso nome ma
appartengono a progetti diversi?»* non elenca le colonne. Due regole, in quest'ordine:

1. **la domanda nomina l'attributo che individua le ennuple → quello è la proiezione.** Nel caso
   sopra la risposta del docente ha tre righe e una sola colonna, `nome`: `WP1`, `WP2`, `WP3`.
   Proiettare tutto il WP dà sei righe — la stessa informazione, ripetuta da entrambi i lati del
   self-join;
2. **se la domanda non nomina nulla**, si eredita la proiezione fissata poco sopra nella stessa
   esercitazione (quasi sempre `nome, cognome` o la chiave), e in mancanza si restituisce la
   chiave.

Il controllo che smaschera l'errore senza conoscere la risposta: **se il numero di righe è un
multiplo esatto di quello che ti aspetti** — il doppio, il triplo — non è la selezione che
sbaglia, è la proiezione che porta con sé una colonna di troppo.

## Trappole di plpgsql che si vedono solo eseguendo

- **`SELECT ... INTO` non riempie un dominio composito.** Se un tipo del corso è stato realizzato
  come tipo composito (un `Periodo` con inizio e fine), `SELECT p INTO v_periodo FROM ...` non
  compila: si dichiarano due variabili scalari, oppure una variabile `RECORD`.
- **`BEFORE` non vede la riga nuova**, e quindi ogni controllo che conta o somma va `AFTER`
  (vedi `progettazione.md`). Il caso che inganna di più è il vincolo «al più uno per…» su una
  classe associativa: `BEFORE` conta zero e passa sempre.
- **Il vincolo che deve tollerare uno stato intermedio va differito**: `CONSTRAINT TRIGGER …
  DEFERRABLE INITIALLY DEFERRED`. Vale per le molteplicità minime maggiori di 1 e per i vincoli
  che legano due tabelle inserite nella stessa transazione.

Il modo di trovarli è sempre lo stesso: **una prova costruita per fallire per ogni vincolo**, più
una controprova legale. Se la prova che deve fallire passa, il trigger non tiene.

## Come consegnare

Un file `query.sql` con le query in ordine, ognuna preceduta da un commento con il numero della
domanda e il suo testo, e un `risultati.txt` con l'output reale dell'esecuzione. Se una domanda
ha due versioni attese, entrambe, marcate come tali.

Nelle query si ricavano i valori dai dati, non si scrivono letterali copiati dal database: una
data presa a mano dalla tabella dei progetti risolve il caso di prova ma non risponde alla
domanda, e in un compito viene giudicata.
