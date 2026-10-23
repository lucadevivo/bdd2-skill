# Diagramma UML delle classi — Passo A.2 eBuy

> Fonte: export XML di Visual Paradigm, diagramma «Passo A.1 eBuy».

## Tipi di dato

`Data`, `DataOra`, `Duarata_Usato`, `Durata_Nuovo {id}`, `Feedback`, `Intero> = 1`, `Prezzo`, `Stringa {id}`, `Url`, `{bonifico,carta di credito,entrambi} {id}`, `{ottimo, buono, discreto, da sistemare} {id}`

## Classi

### Asta
- `base`: Prezzo
- `rialzo`: Prezzo
- `scadenza`: DataOra

### Bid
- `istante`: DataOra

### Categoria
- `nome`: Stringa {id}
- `livello`: Intero> = 1

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
- `feedback`: Feedback [0..1]

### Privato
_(nessun attributo)_

### Professionale
- `url`: Url

### Utente
- `nome`: Stringa {id}
- `registrazione`: Data

### Vendita
- `prezzo`: Prezzo

### compro_subito
- `istante`: DataOra

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| Bidder | Privato `1..1` | Bid `0..*` |
| Offerta | Bid `0..*` | Asta `1..1` |
| Ogg_Cat  | Oggetto in vendita `0..*` | Categoria `1..1` |
| Po_Og | Post `1..1` | Oggetto in vendita `0..1` |
| Sottocategoria | Categoria `Padre (0..*)` | Categoria `1..1` |
| Ut_Po | Utente `1..1` | Post `0..*` |
| compro_subito | Privato `0..1` | Vendita `0..*` |

## Generalizzazioni

- `Oggetto in vendita` generalizza `Oggetto nuovo`  **{disj,complete}**
- `Oggetto in vendita` generalizza `Oggetto usato`  **Stato**
- `Post` generalizza `Vendita`  **{disj,compl}**
- `Post` generalizza `Asta`  **Modalità**
- `Utente` generalizza `Privato`  **Tipologia**
- `Utente` generalizza `Professionale`  **{disj,compl}**
