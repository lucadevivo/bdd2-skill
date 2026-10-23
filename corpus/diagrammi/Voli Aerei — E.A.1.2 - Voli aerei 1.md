# Diagramma UML delle classi — Voli Aerei — E.A.1.2 - Voli aerei 1

> Fonte: export XML di Visual Paradigm, diagramma «Diagramma UML delle classi concettuale».

## Tipi di dato

`Intero`, `Intero > 0`, `Intero > = 0`, `Stringa`

## Classi

### Aeroporto
- `codice`: Stringa
- `nome`: Stringa

### Citta
- `nome`: Stringa
- `n_abitanti`: Intero > = 0

### CompagniaAerea
- `nome`: Stringa
- `anno_fondaz`: Intero

### Nazione
- `nome`: Stringa

### Volo
- `codice`: Stringa
- `durata_minuti`: Intero > 0

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| aerop_citta | Aeroporto `0..*` | Citta `1..1` |
| arrivo | Volo `0..*` | Aeroporto `1..1` |
| cit_naz | Citta `0..*` | Nazione `1..1` |
| comp_volo | Volo `0..*` | CompagniaAerea `1..1` |
| partenza | Volo `0..*` | Aeroporto `1..1` |
| sede_direz | CompagniaAerea `0..*` | Citta `1..1` |
