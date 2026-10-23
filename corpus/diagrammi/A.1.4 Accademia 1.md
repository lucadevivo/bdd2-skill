# Diagramma UML delle classi — A.1.4 Accademia 1

> Fonte: export XML di Visual Paradigm, diagramma «A.1.4 Accademia 1».

## Tipi di dato

`Data`, `Matricola`, `Ora`, `Posizione_Uni`, `Stringa`

## Classi

### Impegno
- `giorno`: Data
- `durata`: Ora
- `tipologia`: 
- `motivazione`: Stringa

### Professore
- `nome`: Stringa
- `cognome`: Stringa
- `data di nascita`: Data
- `matricola`: Matricola
- `posizione universitaria`: Posizione_Uni

### Progetto
- `nome`: Stringa
- `acronimo Stringa`: 
- `data di inizio`: Data
- `data di fine`: Data

### Work Package
- `nome`: Stringa
- `data di inizio`: Data
- `data di fine`: Data

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| Partecipazione | Professore `0..*` | Progetto `0..*` |
| Prof_Imp | Professore `1..*` | Impegno `0..*` |
| Prog_WP | Progetto `1...1` | Work Package `0..*` |
