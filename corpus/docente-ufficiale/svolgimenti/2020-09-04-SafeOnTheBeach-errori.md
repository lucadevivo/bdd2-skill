# SafeOnTheBeach 2020-09-04 — elenco degli errori dello svolgimento

> Fonte: l'elenco errori allegato allo svolgimento nel sito del docente (`esami/svolgimenti/`).
> Si riferisce a `2020-09-04-SafeOnTheBeach-svolgimento-studente-E.pdf`, che è una
> scansione manoscritta: questo file è l'unica parte leggibile come testo.
> **Vale come metro di correzione**: dice cosa è stato considerato errore e perché.

---

VOTO FINALE: 25

- a pagina 13 i vincoli in FOL sul numero di persone dell'entità 18 sono parzialmente corretti; sono semanticamente corretti ma non risolvono completamente il problema in quanto controllo solo che la prenotazione non ecceda la capacità, invece credo andasse richiamato lo UC per i posti disponibili

- lo UC in FOL sulla ricerca Eventi non è completo, ho calcolato solo la media senza poi ritornare gli eventi come richiesto

- l'unico trigger che ho implementato è toppato

- nello UC in SQL ci sono alcuni errori NON gravi:
    - il group by è superfluo, nel senso che non è un errore ma il risultato sarebbe stato uguale senza scriverlo
    - la Zona nella clausola from non era necessaria, quindi anche l'ultima riga z.id = a.zona si poteva omettere
    - il risultato lo ritorno esternamente ad SQL facendo la differenza, mentre si poteva fare direttamente nella select: SELECT z.pax - count(*)