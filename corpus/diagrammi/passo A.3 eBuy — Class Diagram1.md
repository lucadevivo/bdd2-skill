# Diagramma UML delle classi — passo A.3 eBuy

> Fonte: export XML di Visual Paradigm, diagramma «Class Diagram1».

## Tipi di dato

`CondUsato`, `DataOra`, `Int_g2_not _null`, `Int_gz_not _null`, `Int_gz_not_null {id1}`, `Reale_gz`, `String`, `String*`, `URL`, `voto`

## Classi

### Bid
- `istante`: DataOra {id1}

### Categoria
- `nome`: String {id1}

### MetodoPagamento
- `nome`: String {id1}

### Post
- `descrizione`: String
- `pubblicazione`: DataOra
- `anni_garanzia`: Int_gz_not _null
- `prezzo`: Reale_gz
- `id`: Int_gz_not_null {id1}

### PostAsta
- `rialzo`: Reale_gz
- `scadenza`: DataOra

### PostCompraloSubito
_(nessun attributo)_

### PostConFeedback
- `voto`: voto
- `commento`: String*

### PostOggNuovo
- `anni_garanzia`: Int_g2_not _null

### PostOggUsato
- `condizioni`: CondUsato

### Privato
- `nome`: String {id1}
- `registrazione`: DataOra

### Valuta
- `nome`: String {id1}

### VenditoreProf
- `vetrina`: URL
- `nome`: String {id1}
- `registrazione`: DataOra

### acquirente _(classe associativa)_
- `istante`: DataOra

## Associazioni

| associazione | estremo A | estremo B |
|---|---|---|
| a_isa_p | PostAsta `0..*` | Post `1..1 {id1}` |
| acquirente _(classe associativa: acquirente)_ | Privato `0..1` | PostCompraloSubito `0..*` |
| bid_asta | Bid `0..*` | PostAsta `1..1 {id1}` |
| cat_post | Post `0..*` | Categoria `1..1` |
| cs_isa_p | PostCompraloSubito `0..*` | Post `1..1 {id1}` |
| metodopagam_post | Post `0..*` | MetodoPagamento `1..*` |
| pf_isa_p | PostConFeedback `0..1` | Post `1..1 {id1}` |
| pn_isa_p | PostOggNuovo `0..*` | Post `1..1 {id1}` |
| post_valuta | Post `0..*` | Valuta `1..1` |
| priv_bid | Privato `1..1` | Bid `0..*` |
| pu_isa_p | Post `1..1 {id1}` | PostOggUsato `0..*` |
| super_sotto_categoria | Categoria `sotto 0..*` | Categoria `super 0..1 {id1}` |
| venditore_priv | Privato `1..1` | Post `0..*` |
| venditore_prof | VenditoreProf `1..1` | Post `0..*` |
