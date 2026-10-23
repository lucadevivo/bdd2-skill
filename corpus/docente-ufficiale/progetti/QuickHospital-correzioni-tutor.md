# QuickHospital — correzioni del tutor (trascrizione)

Fonte: `QuickHospital-correzioni-tutor.jpg` (screenshot di uno
scambio email, giugno 2020). Trascritto da Claude perché l'originale è solo un'immagine.
Interlocutori: uno studente e **il tutor**, tutor/docente del corso (di.uniroma1.it).
Riferito alla soluzione in `QuickHospital-svolgimento-studente-E.pdf`.

**Valore per la skill:** è una delle poche fonti che dice *cosa un correttore considera
errore e perché*. Indirizzi email e matricole omessi.

---

## 1. Prima revisione (tutor → studente, 7 giugno)

> Un po' di note sulla sua soluzione.
>
> - Non userei una generalizzazione completa tra *Paziente* e *Medico*, poiché un medico
>   potrebbe sempre trovarsi ad essere paziente. Idem per *PazInterno* e *PazEsterno*.
> - Perché è necessario il vincolo `V.Prestazione.data.medPrest`? Un medico non può offrire
>   due prestazioni diverse nella stessa data?
> - Idem per il successivo (esempio: mattina visita oculistica, pomeriggio gastroscopia).
> - Manca un vincolo che impedisca che un paziente sia oggetto di due ricoveri che si
>   sovrappongono nel tempo.
> - Manca il numero del letto! Ci sarebbero stati due vincoli esterni su questo.
> - Tecnicamente, mancherebbero dei vincoli che controllino che le varie date siano
>   successive alla data di nascita della Persona (ad esempio la data del Ricovero).

## 2. Risposta del tutor ai dubbi dello studente (17 giugno)

Sull'uso delle generalizzazioni:

> Le IS-A e le generalizzazioni vanno sempre usate in modo oculato, cercando di capire quali
> conseguenze sul sistema ha il loro utilizzo rispetto ciò che dicono i requisiti.
> In questo caso né i requisiti, né il senso comune dicono che un paziente non possa essere
> medico e viceversa, per cui non utilizziamo una generalizzazione.

Su vincoli vs. dati aggiuntivi:

> In questi casi è sempre meglio introdurre dati ulteriori, purché ragionevoli, invece che
> introdurre vincoli che potrebbero cozzare con le business rules del sistema.
> Nel caso in questione, con ogni probabilità chi ha raccolto i requisiti ha semplicemente
> dimenticato di richiedere anche l'orario della prestazione, in quanto è abbastanza palese
> che sia necessario in un sistema di questo tipo.
>
> I requisiti vanno anche letti in modo critico, usando il buon senso per capire quali dati
> sono di interesse, anche nel caso in cui non sono resi espliciti.
> Inoltre, pensi sempre anche alle conseguenze economiche delle scelte di modellazione. Ad
> esempio, secondo lei, come influisce la limitazione ad una prestazione esterna al giorno
> per ogni medico sulle finanze dell'ospedale che usa il sistema? Ha conseguenze auspicabili
> oppure no?

## 3. Revisione finale (tutor → studente, 22 giugno)

> Ecco i miei commenti alla sua soluzione.
>
> - Nella specifica concettuale dell'operazione *postiDisponibili*, quando definisce l'insieme
>   `L_occ` dei *Letti* occupati, non fa mai riferimento ai *Letti* nella formula, per cui
>   quell'insieme è l'insieme universo se esistono `d, dr` tali che la formula è vera, o
>   l'insieme vuoto altrimenti.
> - Nella stessa operazione, in ogni caso, il secondo termine della disgiunzione non sarebbe
>   corretto. Infatti, considera come occupati tutti i *Letti* relativi a *RicoveriTerminati*
>   che sono iniziati in una data successiva alla data `d` data in input. In questo modo, però,
>   sta includendo anche i *Ricoveri iniziati e terminati dopo la data d*!
> - La precondizione dell'operazione *registraRicovero* non torna: non deve controllare se
>   esiste un *Letto* libero, ma se il *Letto* dato in input lo è.
> - Nella specifica concettuale dell'operazione *itinerarioVisite*, provi a esprimere il
>   criterio di ordinamento in FOL.
> - Nella ristrutturazione, avrei mantenuto la separazione tra *Ricovero* e *RicoveroTerminato*.
>   Infatti, mantenendo in *Ricovero* solamente dati "freschi" rendiamo più efficienti diverse
>   operazioni, come ad esempio *itinerarioVisite*, perché non bisogna filtrare i *Ricoveri*
>   terminati.
> - Il trigger *V.Stanza.maxLetti* è palesemente scorretto, deve essersi confuso (esiste sempre
>   al più una sola stanza con un certo id). La query dovrebbe essere fatta sulla relazione *Letto*.
>
> Tutto il resto va bene.

---

## Regole ricavabili (per la skill)

1. **Generalizzazione completa e disjoint solo se i requisiti o il senso comune la impongono.**
   Default: non usarla. Test: "un'istanza di A potrebbe mai essere anche di B?"
2. **Preferire un attributo in più a un vincolo esterno in più**, quando il vincolo nascerebbe
   solo per compensare un dato mancante (qui: aggiungere l'orario invece di vincolare a una
   prestazione al giorno).
3. **Leggere i requisiti in modo critico**: modellare anche dati ovviamente necessari ma non
   scritti; valutare le conseguenze pratiche/economiche di ogni vincolo.
4. **Vincoli di non sovrapposizione temporale** (ricoveri, prenotazioni) sono attesi anche
   quando la traccia non li nomina.
5. **Vincoli di coerenza sulle date** rispetto alla data di nascita: attesi.
6. **Identificatori**: se un'entità è contata o assegnata (i letti), serve il suo identificatore.
7. **Negli insiemi definiti in FOL, legare esplicitamente la variabile alla sua classe**,
   altrimenti l'insieme degenera in universo o vuoto.
8. **Precondizioni sui parametri effettivi**, non su esistenziali generici ("il letto *dato in
   input* è libero", non "esiste un letto libero").
9. **In ristrutturazione, valutare se tenere separate le entità "storiche"** dalle correnti:
   è una scelta di efficienza, non solo di correttezza.
10. **In un trigger, interrogare la relazione giusta**: contare i letti si fa su `Letto`, non su `Stanza`.
