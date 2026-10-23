# Diagramma UML delle classi — Travel to the Moon — Travel to the moon, Passo A.1 (1-4)

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram concettuale».

## Tipi di dato

`3..5`, `Booleano`, `Data`, `DeltaDataOra`, `Intero > 0`, `Ora`, `Stringa`, `{trad, altern}`

## Classi

### Class
_(nessun attributo)_

### Continente
- `nome`: Stringa {id}
- `esotico`: Booleano

### Crociera
- `codice`: Stringa {id}
- `inizio`: Data

### Destinazione (Porto)
- `nome`: Stringa

### Itinerario
- `nome`: Stringa {id}

### LunaDiMiele
- `tipo`: {trad, altern}

### Nave
- `nome`: Stringa {id}
- `comfort`: 3..5
- `capienza`: Intero > 0

### PerFamiglie
- `bambini`: Booleano

### TappaIntermedia
- `arrivo`: DeltaDataOra
- `ripartenza`: DeltaDataOra

### TipoDestinazione
- `nome`: Stringa {id}

### arrivo_finale _(classe associativa)_
- `istante`: DeltaDataOra

### partenza_iniziale _(classe associativa)_
- `orario`: Ora

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| (senza nome) _(classe associativa: partenza_iniziale)_ | Itinerario `0..*` | Destinazione (Porto) `1..1` |
| (senza nome) _(classe associativa: arrivo_finale)_ | Itinerario `0..*` | Destinazione (Porto) `1..1` |
| croc_itin | Crociera `0..*` | Itinerario `1..1` |
| croc_nave | Crociera `0..*` | Nave `0..1` |
| dest_cont | Destinazione (Porto) `0..*` | Continente `1..1` |
| dest_tipo | Destinazione (Porto) `0..*` | TipoDestinazione `1..1` |
| itin_tappa | TappaIntermedia `0..*` | Itinerario `1..1` |
| tappa_dest | TappaIntermedia `0..*` | Destinazione (Porto) `1..1` |

## Generalizzazioni

- `Crociera` generalizza `PerFamiglie`  **{disjoint, complete}**
- `Crociera` generalizza `LunaDiMiele`
