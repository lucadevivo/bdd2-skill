# Diagramma UML delle classi — E.A.1.3 - Universita 2

> Fonte: export XML di Visual Paradigm, diagramma «Diagramma UML delle classi concettuale».

## Tipi di dato

`CodiceFiscale`, `CodiceInsegnamento`, `Data`, `Intero > = 0`, `Intero >0`, `Matricola`, `Stringa`

## Classi

### Citta
- `nome`: Stringa

### CorsoDiLaurea
- `nome`: Stringa

### Facolta
- `nome`: Stringa

### Insegnamento
- `codice`: CodiceInsegnamento
- `nome`: Stringa
- `n_ore`: Intero > = 0

### Nazione
- `nome`: Stringa

### Persona
- `cf`: CodiceFiscale {id}
- `nome`: Stringa
- `cognome`: Stringa
- `nascita`: Stringa

### Professore
- `cf`: CodiceFiscale
- `nome`: Stringa
- `cognome`: Stringa
- `nascita`: Data

### Regione
- `nome`: Stringa

### Studente
- `matricola`: Matricola
- `anno_immatr`: Intero >0

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| cdl_facolta | CorsoDiLaurea `0..*` | Facolta `1..*` |
| cdl_insegn | Insegnamento `1..*` | CorsoDiLaurea `1..*` |
| cit_reg | Citta `0..*` | Regione `1..1` |
| citta_nascita | Citta `1..1` | Persona `0..*` |
| esame_superato | Studente `0..*` | Insegnamento `0..*` |
| insegna | Insegnamento `0..*` | Professore `0..*` |
| iscrizione | Studente `0..*` | CorsoDiLaurea `1..1` |
| reg_naz | Regione `0..*` | Nazione `1..1` |

## Generalizzazioni

- `Persona` generalizza `Professore`
- `Persona` generalizza `Studente`
