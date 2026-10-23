# Diagramma UML delle classi — Impiegati e Studenti — A.1.7 Impiegati e studenti

> Fonte: export XML di Visual Paradigm, diagramma «A.1.7 Impiegati e studenti».

## Tipi di dato

`CF`, `Data`, `Intero > = 0`, `Matricola {id 1}`, `Reale > 0`, `Stringa`, `Stringa {id 2}`, `Stringa {id}`

## Classi

### Donna
- `numero maternità`: Intero > = 0

### Impiegati
- `stipendio`: Reale > 0

### Persona
- `nome`: Stringa
- `cognome`: Stringa
- `codice fiscale`: CF
- `data di nascita`: Data

### Posizione Militare
- `nome`: Stringa {id}

### Progettista
_(nessun attributo)_

### Progetto
- `nome`: Stringa

### Ruolo
- `nome`: Stringa {id 2}

### Studenti
- `matricola`: Matricola {id 1}

### Uomo
_(nessun attributo)_

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| Pos_Uomo | Posizione Militare `0..*` | Uomo `1..1` |
| Prog_Res | Progetto `0..*` | Progettista `1..*` |

## Generalizzazioni

- `Impiegati` generalizza `Ruolo`  **Ruolo**
- `Persona` generalizza `Donna`  **{disj, compl}**
- `Persona` generalizza `Impiegati`  **{disjoint}**
