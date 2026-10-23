# Diagramma UML delle classi — Esercitazioni universitarie 1

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram concettuale».

## Tipi di dato

`Data`, `Intero > 0`, `Stringa`

## Classi

### Class
_(nessun attributo)_

### Docente
- `matricola`: Stringa
- `nome`: Stringa
- `cognome`: Stringa

### Esercitazione
- `data`: Data

### Esercizio
- `testo`: Stringa
- `soluzione`: Stringa [0..*]

### Insegnamento
- `nome`: Stringa
- `crediti`: Intero > 0
- `aa_inizio`: Intero > 0

### Soluzione
- `testo`: Stringa

### esercizio_in_esercitazione _(classe associativa)_
_(nessun attributo)_

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| (senza nome) _(classe associativa: esercizio_in_esercitazione)_ | Esercitazione `0..*` | Esercizio `0..*` |
| eserc_sol | Esercizio `1` | Soluzione `0..*` |
| ins_esercitazione | Insegnamento `1` | Esercitazione `0..*` |
| insegna | Insegnamento `0..*` | Docente `0..*` |
| sol_presentata | esercizio_in_esercitazione `0..*` | Soluzione `0..1` |
