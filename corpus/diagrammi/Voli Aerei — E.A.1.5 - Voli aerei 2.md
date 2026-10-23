# Diagramma UML delle classi — Voli Aerei — E.A.1.5 - Voli aerei 2

> Fonte: export XML di Visual Paradigm, diagramma «Diagramma UML delle classi concettuale».

## Tipi di dato

`CodiceAeroporto`, `Intero`, `Intero > 0`, `Intero > = 0`, `Stringa`

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

### ModelloVelivolo
- `nome`: Stringa

### Nazione
- `nome`: Stringa

### Tappa
- `n`: Intero > 0

### Volo
- `codice`: CodiceAeroporto
- `durata_minuti`: Intero > 0

### VoloCharter
_(nessun attributo)_

### tappa
- `n`: Intero > 0

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| aer_tappa | Tappa `0..*` | Aeroporto `1..1` |
| aerop_citta | Aeroporto `0..*` | Citta `1..1` |
| arrivo | Volo `0..*` | Aeroporto `1..1` |
| cit_naz | Citta `0..*` | Nazione `1..1` |
| comp_volo | Volo `0..*` | CompagniaAerea `1..1` |
| modvel_charter | VoloCharter `0..*` | ModelloVelivolo `1..1` |
| partenza | Volo `0..*` | Aeroporto `1..1` |
| sede_direz | CompagniaAerea `0..*` | Citta `1..1` |
| tappa | VoloCharter `0..*` | Aeroporto `0..*` |
| tappa_volocharter | VoloCharter `1..1` | Tappa `0..*` |

## Generalizzazioni

- `Volo` generalizza `VoloCharter`
