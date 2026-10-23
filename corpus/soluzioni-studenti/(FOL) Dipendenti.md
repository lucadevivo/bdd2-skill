# (FOL) Dipendenti

> Fonte: `(FOL) Dipendenti.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

(FOL) Dipendenti (gruppo 42)
         Simboli di predicato :
                        P = {Persona/1, CellPersonale/2, Numero/1, Nome/2}
                          ∪{Stringa/1, Dipartimento/1, Lavora/2, Direttore/2}
         Variabili :
                                        V = {x, y, z, a, b, c}
            1) Tutte le persone hanno almeno un numero di telefono
         Con la seguente affermo che ogni Persona ha almeno un CellPersonale, che `e un Numero
                         ∀x Persona(x) →∃y CellPersonale(x, y) ∧Numero(y)
         L’Interpretazione `e la seguente:
                                           D = {α, γ, δ}
         Persona/1 = {α}
         Numero/1 = {γ, δ}
         CellPersonale/2 = {(α, γ), (α, δ)}
            2) Ogni persona ha esattamente un nome
         Con la seguente affermo che ogni Persona ha almeno un Nome, che `e una Stringa
                             ∀x Persona(x) →∃y Nome(x, y) ∧Stringa(y)
         Con la seguente affermo che non esiste una Persona che ha due Nomi o pi`u
                              ¬∃x, y, z Nome(x, z) ∧Nome(x, y) ∧z̸ = y
         L’Interpretazione `e la seguente:
                                          D = {α, β, γ, δ}
         Persona/1 = {α, β}
         Stringa/1 = {γ, δ}
         Nome/2 = {(α, γ), (β, δ)}

            3) Non ci sono dipendenti che lavorano in pi`u di due dipartimenti
         Con la seguente dico che gli oggetti implicati nella relazione Lavora sono una Persona ed un
         Dipartimento
                          ∀x, y Lavora(x, y) →Persona(x) ∧Dipartimento(y)
         Con la seguente dico che, non esiste una persona che lavora in tre (o pi`u) distinti dipartimenti
                        ¬∃x, a, b, c Persona(x) ∧
                        Dipartimento(a) ∧Dipartimento(b) ∧Dipartimento(c) ∧
                          Lavora(x, a) ∧Lavora(x, b) ∧Lavora(x, c) ∧a̸ = b̸ = c
         L’Interpretazione `e la seguente:
                                         D = {α, β, γ, δ, ϵ}
         Persona/1 = {α, β}
         Dipartimento/1 = {γ, δ, ϵ}
         Lavora/2 = {(α, γ), (α, ϵ), (β, γ), (β, δ)}
            4) Ogni dipartimento ha esattamente un direttore che `e una persona
         Con la seguente dico che gli oggetti implicati nella relazione Direttore sono una Persona ed
         un Dipartimento
                         ∀x, y Direttore(x, y) →Persona(x) ∧Dipartimento(y)
         Con la seguente affermo che ogni Dipartimento ha almeno un Direttore
                                 ∀y Dipartimento(y)∃x Direttore(x, y)
         Con la seguente affermo che non esiste un Dipartimento con due o pi`u Direttori
                           ¬∃x, a, b
                           Persona(a) ∧Persona(b) ∧Dipartimento(x) ∧a̸ = b
                                   Direttore(a, x) ∧Direttore(b, x)
         L’Interpretazione `e la seguente:
                                         D = {α, β, γ, δ, ϵ}
         Persona/1 = {α, β}
         Dipartimento/1 = {γ, δ, ϵ}
         Direttore/2 = {(α, γ), (α, δ), (β, ϵ)}
