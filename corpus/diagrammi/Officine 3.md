# Diagramma UML delle classi — Officine 3

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram1».

## Tipi di dato

`CodiceFiscale {id1}`, `Date`, `DateTime`, `Indirizzo`, `Integer {id1}`, `Integer{id2}`, `Targa {id1}`, `Telefono`, `varchar(100)`, `varchar(100) {id1}`, `varchar(100){id1}`

## Classi

### CasaProduttrice
- `nome`: varchar(100){id1}

### Città
- `nome`: varchar(100)
- `identificatore`: Integer {id1}

### Cliente
_(nessun attributo)_

### Dipendente
- `assunzione`: Date

### Direttore
- `nascita`: Date

### Modello
- `nome`: varchar(100) {id1}

### Nazione
- `nome`: varchar(100) {id1}

### Officina
- `nome`: varchar(100)
- `indirizzo`: Indirizzo
- `identificatore`: Integer {id1}

### Persona
- `nome`: varchar(100)
- `cognome`: varchar(100)
- `cf`: CodiceFiscale {id1}
- `indirizzo`: Indirizzo
- `tel`: Telefono

### Riparazione
- `accettazione`: DateTime
- `identificatore`: Integer {id1}

### RiparazioneTerminata
- `riconsegna`: DateTime

### Staff
- `identificatore`: Integer{id2}

### Tipologia
- `nome`: varchar(100) {id1}

### Veicolo
- `targa`: Targa {id1}

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| c_isa_p | Persona `1..1 {id1}` | Cliente `0..1` |
| casa_mod | Modello `?` | CasaProduttrice `1..1 {id1}` |
| citta_naz | Città `0..*` | Nazione `1..1` |
| citta_off | Officina `0..*` | Città `1..1` |
| cliente_veic | Cliente `1..1` | Veicolo `1..*` |
| dip_isa_s | Staff `1.1 {id1}` | Dipendente `0..1` |
| dir_isa_s | Direttore `0..1` | Staff `1..1 {id1}` |
| dirige | Officina `0..1` | Direttore `1..1` |
| lavora | Staff `0..*` | Officina `1..1` |
| mod_tip | Modello `?` | Tipologia `1..1` |
| mod_veic | Veicolo `?` | Modello `1..1` |
| rip_veic | Veicolo `1..1` | Riparazione `0..*` |
| rt_isa_r | Riparazione `1..1 {id1}` | RiparazioneTerminata `0..1` |
| s_isa_p | Staff `0..1` | Persona `1..1 {id1}` |
