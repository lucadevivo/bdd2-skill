# Diagramma UML delle classi — QuickHospital — Ristrutturazione — QuickHospital

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram concettuale».

## Tipi di dato

`CapienzaStanza`, `CodiceFiscale`, `DataOra`, `DurataPrest`, `Email`, `Indirizzo`, `Integer`, `IntegerGZ`, `Stringa`, `Telefono`, `date`, `serial`

## Classi

### Città
- `nome`: Stringa
- `id`: serial {id1}

### Class
_(nessun attributo)_

### Letto
- `n`: IntegerGZ {id1}

### Medico
_(nessun attributo)_

### Nazione
- `nome`: Stringa {id1}

### Padiglione
- `nome`: Stringa {id1}

### Paziente
- `email`: Email
- `indirizzo`: Indirizzo

### Persona
- `cf`: CodiceFiscale {id1}
- `nome`: Stringa
- `cognome`: Stringa
- `nascita`: date

### Piano
- `n`: Integer {id1}

### Prestazione
- `istante_pren`: DataOra
- `inizio_presunto`: DataOra
- `id`: serial {id1}

### PrestazioneEseguita
- `durata`: DurataPrest

### PrestazioneEsterna
- `descrizione`: Stringa

### PrestazioneFinalizzata
- `inizio`: DataOra

### PrestazioneFinalizzateNonEseguite
_(nessun attributo)_

### PrestazioneNonFinalizzata
_(nessun attributo)_

### Ricovero
_(nessun attributo)_

### Settore
- `n`: IntegerGZ {id1}

### Specializzazione
- `nome`: Stringa {id1}

### Stanza
- `capienza`: CapienzaStanza
- `n`: IntegerGZ {id1}

### ValoreTelefono
- `valore`: Telefono {id1}

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| citta_naz | Nazione `1..1` | Città `0..*` |
| let_ric | Ricovero `0..*` | Letto `1..1` |
| let_stanza | Letto `0..*` | Stanza `1..1 {id1}` |
| m_isa_pers | Persona `1..1 {id1}` | Medico `0..1` |
| med_prest | Medico `0..*` | Prestazione `0..*` |
| med_resp_prest | Medico `0..1` | Prestazione `0..*` |
| med_resp_prest_fin | PrestazioneFinalizzata `0..*` | Medico `1..1` |
| med_spec | Medico `0..*` | Specializzazione `1..*` |
| med_spec_prim | Medico `0..*` | Specializzazione `1..1` |
| paz_isa_pers | Persona `1..1 {id1}` | Paziente `0..1` |
| paz_prest | Paziente `1..1` | Prestazione `0..*` |
| pe_isa_p | Prestazione `1..1 {id1}` | PrestazioneEsterna `0..1` |
| peseg_isa_pfin | PrestazioneFinalizzata `1..1 {id1}` | PrestazioneEseguita `0..1` |
| pfin_isa_p | Prestazione `1..1 {id1}` | PrestazioneFinalizzata `0..1` |
| pfin_non_eseg_isa_pfin | PrestazioneFinalizzata `1..1 {id1}` | PrestazioneFinalizzateNonEseguite `0..1` |
| piano_pad | Piano `0..*` | Padiglione `1..1 {id1}` |
| pnonfin_isa_p | Prestazione `1..1 {id1}` | PrestazioneNonFinalizzata `0..1` |
| prest_spec | Specializzazione `1..*` | Prestazione `0..*` |
| r_isa_p | Prestazione `1..1 {id1}` | Ricovero `0..1` |
| residenza | Paziente `?` | Città `1..1` |
| set_piano | Settore `0..*` | Piano `1..1 {id1}` |
| sett_stanza | Stanza `0..*` | Settore `1..1 {id1}` |
| telefono | Paziente `1..*` | ValoreTelefono `1..*` |
