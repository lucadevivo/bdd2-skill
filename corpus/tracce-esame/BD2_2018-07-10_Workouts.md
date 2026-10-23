# BD2_2018-07-10_Workouts

> Fonte: `BD2_2018-07-10_Workouts.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina.

---

Esame Basi di Dati – Modulo II
                              Toni Mancini – Federico Mari
                                       10 Luglio 2018
         Si richiede di progettare Workouts, un sistema web che realizza una rete
         sociale per la gestione delle attività sportive personali e collettive, amatoriali e
         competitive. A tal fine si trascrive di seguito il risultato della raccolta dei
         requisiti con alcuni esperti del dominio.
         Gli utenti di Workouts sono gli sportivi. Uno sportivo (o utente) è identificato
         dal proprio nome utente (una stringa). Inoltre, di uno sportivo è di interesse
         conoscere nome, cognome, il genere (maschio o femmina) e la sua data di
         nascita. Opzionalmente, un utente può anche fornire al sistema il proprio peso
         e la propria altezza. La socialità del sistema Workouts si realizza nella
         possibilità per due sportivi di essere amici. Un utente può avere molti amici.
         Gli utenti usano Workouts per tracciare la loro attività sportiva. Di ogni sport
         memorizzato nel sistema interessa il nome ed una descrizione testuale.
         Gli sportivi interagiscono con Workouts comunicando le loro attività di
         allenamento quotidiane (via web o app per smartphone). In particolare, di ogni
         attività di allenamento di un utente, Workouts memorizza lo sport esercitato,
         gli istanti di inizio e di fine, e (opzionalmente) un valore tra 1 e 5 che
         rappresenta la "difficoltà" dell'allenamento, come percepita dallo stesso utente.
         Inoltre, durante un allenamento, uno sportivo può chiedere a Workouts di
         memorizzare il percorso seguito, usando il suo smartphone. In questo caso,
         l'app per smartphone di
         Workouts, durante l'allenamento, comunica
         periodicamente (ogni qualche secondo) al sistema le coordinate geografiche
         (latitudine e longitudine) della posizione dell'utente. Il percorso rappresentato
         dalla sequenza di tali coordinate (con i relativi istanti di tempo) viene associato
         all'attività di allenamento. Successivamente, l'utente può decidere di rendere
         pubblico tale percorso (assegnandogli un nome ed un commento testuale), di
         modo che anche gli altri utenti possano visualizzarlo su una mappa.
         Una caratteristica innovativa del sistema Workouts è la possibilità per gli
         sportivi di sfidarsi, singolarmente oppure in squadre. In particolare, ogni
         utente può creare una nuova sfida, assegnandole una tipologia ("tra squadre"
         o "tra singoli"), un nome, il periodo di durata, la durata minima di un
         allenamento affinché sia valido per la sfida, gli sport esercitabili (uno o più) e la
         categoria ("più chilometri" o "più allenamenti"). In caso una sfida sia tra
         squadre, l'utente creatore della sfida deve anche definire il numero massimo di
         partecipanti per ogni squadra.
         Una volta che una sfida viene creata, ogni utente può parteciparvi,
         singolarmente (se la sfida è "tra singoli") oppure iscrivendosi ad una squadra
         (se la sfida è "tra squadre"). Delle squadre, che sono limitate ad una singola
         sfida, interessa il nome e l'insieme dei componenti. Si noti che uno sportivo
         non può appartenere a due squadre nell'ambito di una stessa sfida.

         La partecipazione da parte di uno sportivo ad una sfida si sostanzia
         nell'effettuare attività di allenamento relative agli sport e nell'arco temporale
         previsti dalla sfida. La sfida è vinta dall'individuo o squadra che totalizza il
         massimo punteggio. Per le sfide di categoria "più chilometri", il punteggio di un
         utente o squadra è la somma dei chilometri percorsi nelle sue attività di
         allenamento validi per la sfida. Per le sfide di categoria "più allenamenti", il
         punteggio è invece dato dal numero complessivo di allenamenti validi.
         Workouts deve associare ad ogni utente tutte le sfide da lui create o a cui ha
         partecipato.
         Il sistema Workouts deve fornire le seguenti funzionalità:
            1. Registrazione al servizio da parte di un utente web.
            2. Inserimento di un nuovo sport da parte di un amministratore del
            sistema.
            3. Inserimento di una nuova attività di allenamento da parte di uno
            sportivo, con tutte le informazioni richieste.
            4. Creazione di una sfida da parte di uno sportivo, con tutte le
            caratteristiche necessarie.
            5. Creazione di una squadra per una sfida da parte di uno sportivo, con
            tutte le caratteristiche necessarie.
            6. Sottoscrizione di uno sportivo a una sfida (come singolo o come membro
            di una squadra).
            7. Calcolo del resoconto degli allenamenti effettuati da un solo sportivo in
            un dato periodo di tempo. In particolare, per ogni sport praticato, si
            vuole conoscere il tempo totale di allenamento ed il numero totale di
            chilometri percorsi.
            8. Calcolo dello sport maggiormente praticato dagli amici di un certo
            sportivo in un dato periodo di tempo. In particolare, lo sport
            maggiormente praticato è quello a cui è stato dedicato il maggior tempo
            totale (si noti che potrebbero esserci più sport nel risultato, in caso il
            tempo totale praticato per questi dovesse essere lo stesso).
