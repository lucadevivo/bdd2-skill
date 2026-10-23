# Diagramma UML delle classi — Ristrutturazione TuTubi

> Fonte: export XML di Visual Paradigm, diagramma «Passo A.1 TuTubi».

## Tipi di dato

`Data`, `DataOra`, `Durata`, `Path`, `Stringa`, `Stringa {id1}`, `Stringa{id1}`, `intero_05`, `intero_g1`, `intero_gz {id1}`, `stato_playlist`, `stato_video`

## Classi

### Categoria
- `nome`: Stringa {id1}

### Commento
- `valore`: 
- `id`: intero_gz {id1}

### Contiene
- `ordine`: intero_g1

### Cronologia
- `id`: intero_gz {id1}

### Playlist
- `nome`: Stringa
- `creazione`: Data
- `stato`: stato_playlist
- `id`: intero_gz {id1}

### Tag
- `nome`: Stringa{id1}

### Utente
- `nome`: Stringa {id1}
- `iscrizione`: Data

### Valutazione _(classe associativa)_
- `voto`: intero_05

### Video
- `titolo`: Stringa
- `durata`: Durata
- `file`: Path
- `stato`: stato_video
- `descrizione`: Stringa
- `id`: intero_gz {id1}

### Visualizzazione
- `istante`: DataOra
- `id`: intero_gz {id1}

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| Cat_Vid | Categoria `1..1` | Video `0..*` |
| Contiene | Playlist `0..*` | Video `0..*` |
| Cr_Vis | Cronologia `1..1` | Visualizzazione `0..*` |
| Creatore | Playlist `0..*` | Utente `1..1` |
| Pubblicato | Utente `1..1` | Video `0..*` |
| Risponde  | Video `Risposta (0..*)` | Video `Ascolta (0..1)` |
| Tag_Vid | Tag `1..*` | Video `0..*` |
| Ut_Commento | Utente `1..1` | Commento `0..*` |
| Ut_Cr | Utente `0..1` | Cronologia `1..1` |
| Valutazione _(classe associativa: Valutazione)_ | Utente `0..*` | Video `0..*` |
| Vid_Commento | Video `1..1` | Commento `0..*` |
| Visualizzato | Visualizzazione `0..*` | Video `1..1` |
