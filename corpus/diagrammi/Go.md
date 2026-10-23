# Diagramma UML delle classi — Go

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram concettuale».

## Tipi di dato

`Data`, `Indirizzo`, `Indrizzo`, `Intero > 0`, `Intero > = 0`, `Komi`, `Stringa`, `{G,C}`

## Classi

### Città
- `nome`: Stringa

### Giocatore
- `nickname`: Stringa {id}
- `nome`: Stringa
- `cognome`: Stringa
- `indirizzo`: Indrizzo
- `rank`: Intero > 0

### Nazione
- `nome`: Stringa

### Partita
- `data`: Data
- `regole`: {G,C}
- `indirizzo`: Indirizzo
- `komi`: Komi

### PartitaConPunteggi
_(nessun attributo)_

### PartitaConRinuncia
_(nessun attributo)_

### Torneo
- `nome`: Stringa
- `descrizione`: Stringa
- `edizione`: Intero > 0

### punteggio _(classe associativa)_
- `punti`: Intero > = 0

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| (senza nome) _(classe associativa: punteggio)_ | PartitaConPunteggi `0..*` | Giocatore `2..2` |
| bianco | Partita `0..*` | Giocatore `1..1` |
| cit_naz | Città `0..*` | Nazione `1..1` |
| gioc_citta | Giocatore `0..*` | Città `1..1` |
| gioca | Giocatore `2..2` | Partita `0..*` |
| luogo_part | Partita `0..*` | Città `1..1` |
| nero | Partita `?` | Giocatore `1..1` |
| part_torneo | Partita `0.:*` | Torneo `0..1` |
| rinunciatario | Giocatore `1..1` | PartitaConRinuncia `0..*` |

## Generalizzazioni

- `Partita` generalizza `PartitaConRinuncia`
- `Partita` generalizza `PartitaConPunteggi`  **{disjoint}**
- `gioca` generalizza `bianco` _(fra associazioni)_
- `gioca` generalizza `nero` _(fra associazioni)_  **{disjoint, complete}**
- `gioca` generalizza `(senza nome)` _(fra associazioni)_
- `gioca` generalizza `rinunciatario` _(fra associazioni)_
