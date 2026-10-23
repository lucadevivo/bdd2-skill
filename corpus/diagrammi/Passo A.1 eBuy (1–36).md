# Diagramma UML delle classi — Passo A.1 eBuy (1–36)

> Fonte: export XML di Visual Paradigm, diagramma «Passo A.1 eBuy».

## Tipi di dato

`Data`, `DataOra`, `Duarata_Usato`, `Durata_Nuovo {id}`, `Prezzo`, `Stringa {id}`, `{bonifico,carta di credito,entrambi} {id}`, `{ottimo, buono, discreto, da sistemare} {id}`

## Classi

### Asta
- `base`: Prezzo
- `rialzo`: Prezzo
- `scadenza`: DataOra

### Bid
- `istante`: DataOra

### Categoria
- `nome`: Stringa {id}

### Offerta
_(nessun attributo)_

### Oggetto in vendita
- `descrizione`: Stringa {id}
- `metodo_pagamento`: {bonifico,carta di credito,entrambi} {id}

### Oggetto nuovo
- `garanzia`: Durata_Nuovo {id}

### Oggetto usato
- `condizione`: {ottimo, buono, discreto, da sistemare} {id}
- `garanzia`: Duarata_Usato [0..1] {id}

### Post
_(nessun attributo)_

### Utente
- `nome`: Stringa {id}
- `registrazione`: Data

### Vendita
- `prezzo`: Prezzo

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| Bidder | Utente `1..1` | Bid `0..*` |
| Offerta | Bid `0..*` | Asta `1..1` |
| Ogg_Cat  | Oggetto in vendita `0..*` | Categoria `1..1` |
| Po_Og | Post `1..1` | Oggetto in vendita `0..1` |
| Ut_Po | Utente `1..1` | Post `0..*` |

## Generalizzazioni

- `Oggetto in vendita` generalizza `Oggetto nuovo`  **{disj,complete}**
- `Oggetto in vendita` generalizza `Oggetto usato`  **Stato**
- `Post` generalizza `Vendita`  **{disj,compl}**
- `Post` generalizza `Asta`  **Modalità**
