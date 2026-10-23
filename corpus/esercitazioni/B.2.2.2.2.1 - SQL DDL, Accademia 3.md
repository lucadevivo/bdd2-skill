# B.2.2.2.2.1 - SQL DDL, Accademia 3

> Fonte: `Esercitazione B.2.2.2.2.1 - SQL DDL, Accademia 3 - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Esercitazione B.2.2.2.2.1 (E.B.2.2.2.2.1)
                          Basi di dati
                          Sistemi di Gestione di Basi di Dati Relazionali
                   Il Linguaggio SQL
                   Data Definition Language
                   Domini Definiti dall’Utente
                                 Accademia 3
                                       – Solo Testo –
                                                                         Esercitazione E.B.2.2.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Definition Language
    Domini Definiti dall’Utente
    Accademia 3
                           Obiettivi
              Si vuole realizzare una base dati relazionale con vincoli di nome “Accademia”, per la
              gestione delle tabelle orarie relative a progetti di ricerca per Ricercatori e Professori
              universitari.
              Dato l’output della fase di Progettazione della Base Dati, si chiede di definire gli
              opportuni comandi SQL create domain, create type as enum e create table per definire
              i domini e creare le tabelle della base dati.
                                                                       Esercitazione E.B.2.2.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Definition Language
    Domini Definiti dall’Utente
    Accademia 3
    1.
    Domini e Schema Relazionale con Vincoli
    della Base Dati
                 Domini e Schema
                 Relazionale con Vincoli
                 della Base Dati
              Il database Accademia è definito sul seguente insieme di domini e sul seguente schema
              relazionale con vincoli.
              Definizione dei domini
                     • Strutturato
                     enum (’Ricercatore’, ’Professore Associato’, ’Professore Ordinario’)
                     • LavoroProgetto
                     enum (’Ricerca e Sviluppo’, ’Dimostrazione’, ’Management’, ’Altro’)
                     • LavoroNonProgettuale
                     enum (’Didattica’, ’Ricerca’, ’Missione’, ’Incontro Dipartimentale’, ’Incontro
                     Accademico’, ’Altro’)
                     • CausaAssenza
                     enum (’Chiusura Universitaria’, ’Maternita’, ’Malattia’)
                     • PosInteger
                     integer ≥0
                     • StringaM
                     varchar(100)
                     • NumeroOre
                     integer tra 0 e 8
                     • Denaro
                     real ≥0
                                                                         Esercitazione E.B.2.2.2.2.1

    Basi di dati
    Sistemi di Gestione di Basi di Dati Relazionali
    Il Linguaggio SQL
    Data Definition Language
    Domini Definiti dall’Utente
    Accademia 3
    1.
    Domini e Schema Relazionale con Vincoli
    della Base Dati
              Schema relazionale con vincoli della base dati
                   Persona (id: PosInteger, nome: StringaM, cognome: StringaM, posizione: Strut-
                   turato, stipendio: Denaro)
                   Progetto (id: PosInteger, nome: StringaM, inizio: date, fine: date, budget:
                   Denaro)
                    [VincoloDB.1]
                    altra chiave: (nome)
                    [VincoloDB.2]
                    ennupla: inizio < fine
                   WP (progetto: PosInteger, id: PosInteger, nome: StringaM, inizio: date, fine:
                   date)
                    [VincoloDB.3]
                    ennupla: inizio < fine
                    [VincoloDB.4]
                    altra chiave: (progetto, nome)
                    [VincoloDB.5]
                    foreign key: progetto references Progetto(id)
                   AttivitaProgetto (id: PosInteger, persona: PosInteger, progetto: PosInteger,
                   wp: PosInteger, giorno: date, tipo: LavoroProgetto, oreDurata: NumeroOre)
                    [VincoloDB.6]
                    foreign key: persona references Persona(id)
                    [VincoloDB.7]
                    foreign key: (progetto, wp) references WP(progetto, id)
                   AttivitaNonProgettuale (id: PosInteger, persona: PosInteger, tipo: Lavoro-
                   NonProgettuale, giorno: date, oreDurata: NumeroOre)
                    [VincoloDB.8]
                    foreign key: persona references Persona(id)
                   Assenza (id: PosInteger, persona: PosInteger, tipo: CausaAssenza, giorno: date)
                    [VincoloDB.9]
                    altra chiave: persona, giorno
                    [VincoloDB.10]
                    foreign key: persona references Persona(id)
                                                                         Esercitazione E.B.2.2.2.2.1
