# Voli aerei 1

> Fonte: `Voli aerei 1.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Voli aerei 1 (gruppo 42)
         Requisiti
         I dati di interesse per il sistema sono Voli, Compagnia ed Aeroporti.
           1. Volo
               1.1 codice - Serie di caratteri alfanumerici che identificano univocamente un Volo.
               1.2 durata - Si usa un dato composto, consistente in un intero positivo per identificare
               la durata in ore, e due interi compresi fra 0 e 59, rispettivamente per i minuti ed i
               secondi.
               1.3 compagnia - La compagnia che fornisce il volo.
               1.4 aereoporto di partenza
               1.5 aereoporto di arrivo
           2. Aereoporto
               2.1 codice - Serie di caratteri alfanumerici che identificano univocamente un Aereoporto.
               2.2 nome
               2.3 citt`a - La citt`a in cui risiede l’Aereoporto.
               2.4 nazione - La nazione in cui si trova la citt`a.
           3. Compagnia
               3.1 nome
               3.2 anno di fondazione
               3.3 citt`a sede direzione
         Saranno necessarie due classi Citt`a e Nazione.

         Considerazioni
         Un Volo pu`o appartenere a pi`u di una Compagnia? No.
         Un Volo pu`o cambiare Compagnia? Se si, si vuole mantenere uno storico? No, non si vuole far si
         che uno stesso Volo possa cambiare compagnia mantenendo lo stesso codice, sar`a semplicemente
         un altro Volo, con codice diverso e Compagnia diversa, ma con il tragitto e durata identici.
         Una Nazione ha almeno una Citt`a, data l’esistenza di nazioni a citt`a unica, come San Marino
         o Singapore.
         UML
