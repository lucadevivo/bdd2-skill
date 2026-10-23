# E.A.1.6 - Università 2 — soluzione ufficiale

## 01 - Raffinamento dei requisiti

> Fonte: `01 - Raffinamento dei requisiti.txt`

```
1. Requisiti sulle persone. Di ogni persona il sistema deve rappresentare:
	1.1. nome (stringa)
	1.2. cognome (stringa)
	1.3. codice fiscale (stringa secondo standard)
	1.4. data di nascita (data)
	1.5. città di nascita (v. req. 7)

2. Requisiti sugli studenti. Di ogni studente il sistema deve rappresentare:
	2.1. matricola (stringa secondo standard)
	2.2. corso di laurea (unico) a cui è iscritto (v. req. 4)
	2.3. anno di immatricolazione (intero > 0)
	2.4. insegnamenti di cui ha superato l'esame (v. req. 6)

3. Requisiti sui professori. Di ogni professore il sistema deve rappresentare:
	3.1. insegnamenti erogati (zero o più)

4. Requisiti sui corsi di laurea (CdL). Di ogni CdL il sistema deve rappresentare:
	4.1. nome (stringa)
	4.2. le facoltà di appertenenza (almeno una, v. req. 5)

5. Requisiti sulle facoltà. Di ogni facoltà il sistema deve rappresentare:
	5.1. nome (stringa)

6. Requisiti sugli insegnamenti. Di ogni insegnamento il sistema deve rappresentare:
	6.1. codice (stringa secondo standard)
	6.2. nome (stringa)
	6.3. numero di ore di lezione (intero >= 0)
	6.4. corsi di laurea (CdL, v. req. 4) a cui appartiene (almeno uno)

7. Requisiti sulle città. Di ogni città il sistema deve rappresentare:
	7.1. nome (stringa)
	7.2. regione (v. req. 8)

8. Requisiti sulle regioni. Di ogni regione il sistema deve rappresentare:
	8.1. nome (stringa)
	8.2. nazione (v. req. 9)

9. Requisiti sulle nazioni. Di ogni nazione il sistema deve rappresentare:
	9.1. nome
```

## 03 - Specifica dei tipi di dato

> Fonte: `03 - Specifica dei tipi di dato.txt`

```
Specifica dei tipi di dato


CodiceFiscale
	Stringa che soddisfa l'espressione regolare:
	'[A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[A-Za-z][0-9]{3}[A-Za-z]'

Matricola
	Stringa che soddisfa l'espressione regolare:
		...secondo lo standard dell'università...

CodiceInsegnamento
	Stringa che soddisfa l'espressione regolare:
		...secondo lo standard dell'università...
```
