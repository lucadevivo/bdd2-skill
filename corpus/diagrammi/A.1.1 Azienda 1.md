# Diagramma UML delle classi — A.1.1 Azienda 1

> Fonte: export XML di Visual Paradigm, diagramma «A.1.1 Azienda 1».

## Tipi di dato

`data`

## Classi

### Afferenza
- `Data Afferenza`: data

### Dipartimento1
- `Nome`: 
- `Telefono centralino`: 

### Impiegato
- `Nome`: 
- `Cognome`: 
- `Data di nascita`: data
- `Stipendio`: 

### Progetto
- `Nome`: 
- `Budget`: 

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| Aff_Imp | Impiegato `1..1` | Afferenza `0..*` |
| Dip_Aff | Dipartimento1 `0..*` | Afferenza `1..1` |
| Dirigenza | Dipartimento1 `1..1` | Impiegato `0..*` |
| Imp_Prog | Impiegato `0..*` | Progetto `0..*` |
