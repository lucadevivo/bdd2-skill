# Diagramma UML delle classi — E.A.1.11 - Officine 1

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram1».

## Tipi di dato

`CodiceFiscale`, `Data`, `DataOra`, `Indirizzo`, `Stringa`, `Targa`, `Telefono`

## Classi

### CasaProduttrice
- `nome`: Stringa

### Città
- `nome`: Stringa

### Cliente
_(nessun attributo)_

### Dipendente
- `assunzione`: Data

### Direttore
- `nascita`: Data

### Modello
- `nome`: Stringa

### Nazione
- `nome`: Stringa

### Officina
- `nome`: Stringa
- `indirizzo`: Indirizzo
- `attribute`: 

### Persona
- `nome`: Stringa
- `cognome`: Stringa
- `cf`: CodiceFiscale
- `indirizzo`: Indirizzo
- `tel`: Telefono

### Riparazione
- `accettazione`: DataOra

### RiparazioneTerminata
- `riconsegna`: DataOra

### Staff
_(nessun attributo)_

### Tipologia
- `nome`: Stringa

### Veicolo
- `targa`: Targa

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| casa_mod | Modello `?` | CasaProduttrice `1..1 {id}` |
| citta_naz | Città `0..*` | Nazione `1..1` |
| citta_off | Officina `0..*` | Città `1..1` |
| cliente_veic | Cliente `1..1` | Veicolo `1..*` |
| dirige | Officina `0..1` | Direttore `1..1` |
| lavora | Staff `0..*` | Officina `1..1` |
| mod_tip | Modello `?` | Tipologia `1..1` |
| mod_veic | Veicolo `?` | Modello `1..1` |
| rip_veic | Veicolo `1..1` | Riparazione `0..*` |

## Generalizzazioni

- `Persona` generalizza `Staff`
- `Persona` generalizza `Cliente`
- `Riparazione` generalizza `RiparazioneTerminata`
- `Staff` generalizza `Direttore`  **{complete}**
- `Staff` generalizza `Dipendente`
- `lavora` generalizza `dirige` _(fra associazioni)_
