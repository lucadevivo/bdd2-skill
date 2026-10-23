# Diagramma UML delle classi — E.A.1.10 - Accademia 2

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram».

## Tipi di dato

`Data`, `DataOra`, `Intero > 0`, `Matricola`, `Stringa`

## Classi

### Assenza
_(nessun attributo)_

### Docente
- `nome`: Stringa
- `cognome`: Stringa
- `nascita`: Data
- `matricola`: Matricola {id}

### Giornaliero
_(nessun attributo)_

### Impegno
- `inizio`: DataOra
- `durata`: Intero > 0
- `motivazione`: Stringa

### Istituzionale
_(nessun attributo)_

### Orario
_(nessun attributo)_

### ProfessoreAssociato
_(nessun attributo)_

### ProfessoreOrdinario
_(nessun attributo)_

### Progetto
- `nome`: Stringa
- `scronimo`: Stringa
- `inizio`: Data
- `fine`: Data

### Progettuale
_(nessun attributo)_

### Ricercatore
_(nessun attributo)_

### WorkPackage
- `nome`: Stringa
- `inizio`: Data
- `fine`: Data

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| coinvolto | Docente `0..*` | Progetto `0..*` |
| doc_imp | Docente `1..1` | Impegno `0..*` |
| prog_work | Progetto `1..1` | WorkPackage `0..*` |

## Generalizzazioni

- `Docente` generalizza `ProfessoreOrdinario`
- `Docente` generalizza `ProfessoreAssociato`
- `Docente` generalizza `Ricercatore`
- `Impegno` generalizza `Assenza`
- `Impegno` generalizza `Giornaliero`
- `Impegno` generalizza `Istituzionale`
- `Impegno` generalizza `Orario`
- `Impegno` generalizza `Progettuale`
