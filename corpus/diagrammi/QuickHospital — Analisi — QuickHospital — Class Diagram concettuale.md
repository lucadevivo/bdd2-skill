# Diagramma UML delle classi — QuickHospital — Analisi — QuickHospital

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram concettuale».

## Tipi di dato

`CapienzaStanza`, `CodiceFiscale`, `Data`, `DataOra`, `Durata > 0`, `Email`, `Indirizzo`, `Intero`, `Intero > 0`, `Stringa`, `Telefono`

## Classi

### Città
- `nome`: Stringa

### Class
_(nessun attributo)_

### Letto
- `n`: Intero > 0 {id}

### Medico
_(nessun attributo)_

### Nazione
- `nome`: Stringa {id}

### Padiglione
- `nome`: Stringa {id}

### Paziente
- `email`: Email
- `telefono`: Telefono [1..*]
- `indirizzo`: Indirizzo

### Persona
- `cf`: CodiceFiscale {id}
- `nome`: Stringa
- `cognome`: Stringa
- `nascita`: Data

### Piano
- `n`: Intero {id}

### Prestazione
- `istante_pren`: DataOra
- `inizio_presunto`: DataOra

### PrestazioneEseguita
- `durata`: Durata > 0

### PrestazioneEsterna
_(nessun attributo)_

### PrestazioneFinalizzata
- `inizio`: DataOra

### Ricovero
_(nessun attributo)_

### Settore
- `n`: Intero > 0 {id}

### Specializzazione
_(nessun attributo)_

### Stanza
- `capienza`: CapienzaStanza
- `n`: Intero > 0 {id}

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| (senza nome) | Nazione `1..1` | Città `0..*` |
| let_ric | Ricovero `0..*` | Letto `1..1` |
| let_stanza | Letto `0..*` | Stanza `1..1 {id}` |
| med_prest | Medico `0..*` | Prestazione `0..*` |
| med_resp_prest | Medico `0..1` | Prestazione `0..*` |
| med_resp_prest_fin | PrestazioneFinalizzata `0..*` | Medico `1..1` |
| med_spec | Medico `0..*` | Specializzazione `1..*` |
| med_spec_prim | Medico `0..*` | Specializzazione `1..1` |
| paz_prest | Paziente `1..1` | Prestazione `0..*` |
| piano_pad | Piano `0..*` | Padiglione `1..1` |
| prest_spec | Specializzazione `1..*` | Prestazione `0..*` |
| residenza | Paziente `?` | Città `1..1` |
| set_piano | Settore `0..*` | Piano `1..1 {id}` |
| sett_stanza | Stanza `0..*` | Settore `1..1 {id}` |

## Generalizzazioni

- `Persona` generalizza `Medico`  **{complete}**
- `Persona` generalizza `Paziente`
- `Prestazione` generalizza `PrestazioneFinalizzata`
- `Prestazione` generalizza `PrestazioneEsterna`
- `Prestazione` generalizza `Ricovero`  **{disjoint, complete}**
- `PrestazioneFinalizzata` generalizza `PrestazioneEseguita`
- `med_prest` generalizza `med_resp_prest` _(fra associazioni)_
- `med_resp_prest` generalizza `med_resp_prest_fin` _(fra associazioni)_
- `med_spec` generalizza `med_spec_prim` _(fra associazioni)_
