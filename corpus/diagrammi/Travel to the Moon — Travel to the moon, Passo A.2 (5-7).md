# Diagramma UML delle classi — Travel to the Moon — Travel to the moon, Passo A.2 (5-7)

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram concettuale».

## Tipi di dato

`3..5`, `Apertura`, `Booleano`, `Data`, `DataOra`, `DeltaDataOra`, `Indirizzo`, `Intero > 0`, `Ora`, `Stringa`, `{trad, altern}`

## Classi

### Città
- `nome`: Stringa

### Class
_(nessun attributo)_

### Cliente
- `nome`: Stringa
- `cognome`: Stringa
- `nascita`: Data
- `indirizzo`: Indirizzo

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

### Nazione
- `nome`: Stringa {id}

### PerFamiglie
- `bambini`: Booleano

### PostoDaVedere
- `nome`: Stringa
- `descrizione`: Stringa
- `apertura`: Apertura [0..*]

### Prenotazione
- `istante`: DataOra
- `posti`: Intero > 0

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
| (senza nome) | Destinazione (Porto) `0..*` | PostoDaVedere `0..*` |
| (senza nome) _(classe associativa: partenza_iniziale)_ | Itinerario `0..*` | Destinazione (Porto) `1..1` |
| (senza nome) _(classe associativa: arrivo_finale)_ | Itinerario `0..*` | Destinazione (Porto) `1..1` |
| citta_naz | Città `0..*` | Nazione `1..1` |
| cliente_indirizzo_citta | Cliente `0..*` | Città `1..1` |
| croc_itin | Crociera `0..*` | Itinerario `1..1` |
| croc_nave | Crociera `0..*` | Nave `0..1` |
| dest_cont | Destinazione (Porto) `0..*` | Continente `1..1` |
| dest_tipo | Destinazione (Porto) `0..*` | TipoDestinazione `1..1` |
| itin_tappa | TappaIntermedia `0..*` | Itinerario `1..1` |
| pren_cliente | Prenotazione `0..*` | Cliente `1..1` |
| pren_croc | Prenotazione `0..*` | Crociera `1..1` |
| tappa_dest | TappaIntermedia `0..*` | Destinazione (Porto) `1..1` |

## Generalizzazioni

- `Crociera` generalizza `PerFamiglie`  **{disjoint, complete}**
- `Crociera` generalizza `LunaDiMiele`
