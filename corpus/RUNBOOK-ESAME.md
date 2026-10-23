# Runbook degli strumenti — la macchina, non la logica

Promemoria dei comandi meccanici per esercitarsi su una traccia già svolta senza perdere tempo in
operazioni ripetitive. Tutto quello che è marcato **verificato** è stato provato su un portatile
Linux, in locale. Gira senza dipendenze di rete: jar di PlantUML locale, layout interno, database
in container.

## Prima di cominciare: sei controlli, due minuti

```bash
docker start bdd2pg 2>/dev/null; docker ps --filter name=bdd2pg --format '{{.Status}}'
docker exec bdd2pg psql -U postgres -d accademia -qtAc "select count(*) from persona"   # 21
docker exec bdd2pg psql -U postgres -d cielo     -qtAc "select count(*) from aeroporto" # 5+
java -version                                    # serve a PlantUML
ls -l corpus/tools/plantuml.jar                  # ~22 MB
ls ~/.claude/skills/bdd2/SKILL.md                # la skill è installata
```

**Verificato:** il container ha `--restart unless-stopped`, quindi riparte da solo dopo un riavvio;
i due database rispondono; Java 17 c'è; il jar c'è.

Se il container manca del tutto, si ricrea e si ricarica con
`corpus/database/{accademia 3,cielo}/*.sql` — l'ordine è `domains-tables.sql`, `constraints.sql`,
`data.sql` (per `cielo` il file dei vincoli è vuoto **per scelta del docente**, non è rotto).

## I cinque comandi che servono davvero

**1. La traccia diventa immagini** — servono al modello per leggere il testo.

```bash
python3 - <<'EOF'
import pymupdf
d = pymupdf.open("traccia.pdf")
for i, p in enumerate(d): p.get_pixmap(dpi=200).save(f"pag{i+1}.png")
EOF
```

**Verificato: 0,7 s** per due pagine a 200 dpi. Poi le pagine si passano al modello **come
immagini**, e insieme **la barra la detti tu**: dove ogni tratto comincia e dove finisce, citando la
frase iniziale e quella finale. Non è pigrizia sua — la lettura della barra dai pixel è l'unico
passo del sistema senza nessuna misura alle spalle, e governa le Domande 5 e 8. Prima che scriva
qualsiasi cosa, fatti ripetere l'ambito e confermalo.

**2. Cercare un precedente nel corpus** — è il Passo zero della skill.

```bash
grep -ril "sovrapposizione temporale" corpus/{soluzioni-ufficiali,diagrammi,teoria}   # prima le fonti che fanno testo
grep -ril "sovrapposizione temporale" corpus/{esercitazioni,soluzioni-studenti}       # poi, solo se le prime tacciono
```

**3. Eseguire l'SQL prima di darlo per buono** — la Domanda 8 è eliminatoria.

```bash
docker exec -i bdd2pg psql -U postgres -d accademia -v ON_ERROR_STOP=1 < mio.sql
```

**4. I controlli meccanici** — dieci secondi, prima di comporre.

```bash
python3 scripts/verifica-consegna.py soluzione.md
python3 scripts/misura-lunghezza.py soluzione.md
```

Il primo stampa le cose da guardare, non un voto: vincoli senza realizzazione, operazioni
disegnate e mai specificate, variabili non legate, simboli inventati nelle formule, intestazioni
che sparirebbero dalla consegna. Restano fuori i contenitori, l'ambito della barra e il caso vuoto
di «solo»: quelli si guardano sulla traccia.

**5. Comporre il risultato** — un solo file HTML, con i diagrammi disegnati dentro.

```bash
python3 scripts/componi.py soluzione.md -o out/ --titolo "..."
```

**Verificato: 1,9 s** su una soluzione completa di 2301 righe, tre diagrammi SVG incorporati,
**nessuna richiesta di rete**. Il diagramma da solo, se serve separato:
`scripts/uml2png.py soluzione.md -o out/ --svg` — **1,5 s**.

## Quanto costa la macchina, in tutto

Meno di **cinque secondi**. Non è lì che si perde tempo: si perde a leggere male la barra, a
rifare un diagramma, a scrivere una formula che non regge il caso vuoto. Il runbook serve solo a
togliere di mezzo il resto.

## Le tre cose che possono andare storte, e cosa fare

| Sintomo | Causa | Rimedio |
|---|---|---|
| `psql: could not connect` | container spento | `docker start bdd2pg`, aspetta 3 secondi |
| `componi.py` scrive l'HTML ma senza `<svg>` | il diagramma non è nel formato del corso, oppure una sezione dopo `## Generalizzazioni` è a livello `###` | riportare le sezioni a livello `##` |
| PlantUML si pianta o non produce nulla | manca Java, o il jar non è dove lo cerca (`corpus/tools/plantuml.jar`) | `java -version`, e controllare il percorso |

Nessuno di questi passaggi usa la rete: jar locale, layout interno (Smetana), database in
container.
