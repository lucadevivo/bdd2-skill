# E.A.1.5 - Voli aerei 2 — soluzione ufficiale

## 01 - Raffinamento dei requisiti

> Fonte: `01 - Raffinamento dei requisiti.txt`

```
1. Requisiti sui voli. Di ogni volo il sistema deve rappresentare:
	1.1. codice (una stringa secondo lo standard IATA)
	1.2. durata (espressa in minuti, un intero positivo)
	1.3. aeroporto di partenza (v. req. 2)
	1.4. aeroporto di arrivo (v. req. 2)
	1.5. compagnia aerea (v. req. 5)

2. Requisiti susli aeroporti. Di ogni aeroporto il sistema deve rappresentare:
	2.1. codice (stringa)
	2.2. nome (stringa)
	2.3. città (v. req. 3)
	
3. Requisiti sulle città. Di ogni città il sistema deve rappresentare:
	3.1. nome (stringa)
	3.2. numero abitanti (intero >= 0)
	3.3. nazione (v. req. 4)

4. Requisiti sulle nazioni. Di ogni nazione il sistema deve rappresentare:
	4.1. nome (stringa)

5. Requisiti sulle compagnie aeree. Di ogni compagnia aerea il sistema deve rappresentare:
	5.1. nome (stringa)
	5.2. anno di fondazione (intero)
	5.3. città della sede della direzione (v. req. 3).

6. Requisiti sui voli charter, un tipo particolare di voli. Di ognuno il sistema deve rappresentare:
	6.1. le eventuali tappe intermedie. Per ognuna:
		6.1.1. l'aeroporto della tappa
		6.1.2. il numero d'ordine della tappa
	6.2. il modello di velivolo usato.
```

## 03 - Specifica dei tipi di dato

> Fonte: `03 - Specifica dei tipi di dato.txt`

```
Specifica dei tipi di dato


CodiceAeroporto
	Stringa che soddisfa l'espressione regolare:
		...secondo lo standard IATA...
```
