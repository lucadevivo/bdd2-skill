# Go — soluzione ufficiale

## Raffinamento requisiti

> Fonte: `Raffinamento requisiti.txt`

```
1. Requisiti sui giocatori
	1.1. nick-name (univoco)
	1.2. nome
	1.3. cognome
	1.4. indirizzo
	1.5. rank dichiarato (Intero > 0)

2. Requisiti sulle partite
	2.1. due giocatori, ognuno di un colore diverso (bianco e nero)
	2.2. data
	2.3. luogo
	2.4. regole usate (giapponesi o cinesi)
	2.5. komi (reale tra 0 e 10)
	2.6. esito:
		2.6.1. rinuncia
			2.6.1.1. il giocatore rinunciatario
		2.6.2. punteggi
			2.6.2.1. i punteggi dei due giocatori (Intero >= 0)
	2.7. l'eventuale torneo (v. req. 3)

3. Requisiti sui tornei
	3.1. nome
	3.2. descrizione
	3.3. edizione (YYYY/YY+1)
```

## Specifica dei tipi di dato

> Fonte: `Specifica dei tipi di dato.txt`

```
Specifica dei tipi di dato


Indirizzo: (
	via: Stringa
	civico: Stringa ~ '[0-9]*[a-zA-Z]?'
)

Komi: Reale tra 0 e 10
```
