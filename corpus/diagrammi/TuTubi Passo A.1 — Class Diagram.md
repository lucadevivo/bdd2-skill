# Diagramma UML delle classi — TuTubi Passo A.1

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram».

## Tipi di dato

`Data`, `DataOra`, `FileVideo`, `Reale`, `Stringa`, `Voto`

## Classi

### Categoria
- `nome`: Data

### Class
_(nessun attributo)_

### Commento
- `testo`: Stringa
- `istante`: DataOra

### Tag
- `nome`: Reale

### Utente
- `nome`: Stringa
- `iscrizione`: DataOra

### Video
- `titolo`: Stringa
- `descrizione`: Stringa
- `flusso`: FileVideo
- `istante`: DataOra

### Visualizzazione
- `istante`: DataOra

### valutazione
- `voto`: Voto
- `istante`: DataOra

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| cat_video | Video `0..*` | Categoria `1..1` |
| comm_ut | Utente `1..1` | Commento `0..*` |
| comm_vid | Commento `0..*` | Video `1..1` |
| risposta_a_video | Video `0..* risposta` | Video `0..1 originale` |
| tag_video | Video `0..*` | Tag `1..*` |
| ut_vis | Visualizzazione `0..*` | Utente `0..1` |
| utente_pubblica_video | Utente `1..1` | Video `0..*` |
| valutazione | Utente `0..*` | Video `0..*` |
| vid_vis | Visualizzazione `0..*` | Video `1..1` |
