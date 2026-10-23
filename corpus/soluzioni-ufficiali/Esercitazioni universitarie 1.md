# Esercitazioni universitarie 1 — soluzione ufficiale

## Classe Insegnamento

> Fonte: ` Classe Insegnamento.txt`

```
Specifica classe Insegnamento

// Questa operazione può essere del tutto omessa, perché non richiesta dai requisiti
aa_fine(): Intero > 0
	pre: nessuna
	post: result = this.aa_inizio + 1
```

## Raffinamento dei requisiti

> Fonte: `Raffinamento dei requisiti.txt`

```
1. Requisiti sugli insegnamenti. Di ognuno interessa:
	1.1. nome
	1.2. numero crediti formativi
	1.3. docenti (uno o più)
	1.4. anno accademico
	1.5. esercitazioni (v. req. 3)


2. Requisiti sui docenti. Di ognuno interessa:	
	2.1. matricola
	2.2. nome
	2.3. cognome


3. Requisiti sulle esercitazioni. Di ognuna interessa:
	3.1. data
	3.2. esercizi compresi (v. req. 4), per ognuno:
		3.2.1. se è stato solo presentato, oppure
		3.2.2. se è stato anche risolto, in questo caso:
			3.2.2.1. quale delle soluzioni disponibili è stata mostrata


4. Requisiti sugli esercizi. Di ognuno interessa:	
	4.1. testo
	4.2. eventuali soluzioni
```

## Specifica associazione esercizio_in_esercitazione

> Fonte: `Specifica associazione esercizio_in_esercitazione.txt`

```
Specifica associazione esercizio_in_esercitazione

[V.esercizio_in_esercitazione.soluzione_propria]
	Per ogni (x:Esercitazione, e:Esercizio):esercizio_in_esercitazione,
		deve essere:

		Se esiste 
			  ( (x:Esercitazione, e:Esercizio):esercizio_in_esercitazione,   
				 s:Soluzione
			  ):sol_presentata

	    allora s deve essere legata ad 'e' da un link di assoc. eserc_sol.
	   	Formalmente, l'ultima frase può essere scritta come:  
	    		(e,s):eserc_sol
```
