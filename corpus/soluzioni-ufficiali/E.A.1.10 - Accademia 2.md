# E.A.1.10 - Accademia 2 — soluzione ufficiale

## 01 - Raffinamento dei requisiti

> Fonte: `01 - Raffinamento dei requisiti.txt`

```
1. Requisiti sui docenti. Di ogni docente il sistema deve rappresentare:
	1.1. nome (stringa)
	1.2. cognome (stringa)
	1.3. data di nascita (data)
	1.4. matricola (stringa secondo un certo standard)
	1.5. posizione universitaria:
		1.5.1. ricercatore
		1.5.2. professore associato
		1.5.3. professore ordinario
 	1.6. progetti a cui partecipa (v. req. 2)

2. Requisiti sui progetti. Di ogni progetto il sistema deve rappresentare:
	2.1. nome (stringa)
	2.2. acronimo (stringa)
	2.3. data di inizio (data)
	2.4. data di fine (data)
	2.5. workpackage (zero o più) di cui è composto (v. req. 3)
	2.6. docenti coinvolti (v. req. 1.)

3. Requisiti sui workpackage. Di ogni workpackage il sistema deve rappresentare:
	3.1. nome (stringa) 
	3.2. data di inizio (data)
	3.3. data di fine (data)

4. Requisiti sugli impegni dei docenti. Di ogni impegno il sistema deve rappresentare:
	4.1. docente impegnato (v. req. 1)
	4.2. data dell'impegno (data)
	4.3. durata (intero positivo)
	4.4. unità di misura { ore, giorni }
	4.5. tipologia dell'impegno:
		4.5.1. Assenza
		4.5.2. Impegni istituzionali
		4.5.3. Impegni Progettuali
	4.6. motivazione (stringa)
```

## 03 - Specifica dei tipi di dato

> Fonte: `03 - Specifica dei tipi di dato.txt`

```
Specifica dei tipi di dato


Matricola
	Stringa che soddisfa l'espressione regolare:
		...secondo lo standard dell'università...
```
