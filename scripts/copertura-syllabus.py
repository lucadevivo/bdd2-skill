import re, os, subprocess
SKILL = "~/.claude/skills/bdd2"
testo = ""
for dp, _, fns in os.walk(SKILL):
    for fn in sorted(fns):
        if fn.endswith(".md"):
            testo += open(os.path.join(dp, fn), encoding="utf-8").read().lower()

# (unita syllabus, concetto, parole chiave che ne provano la copertura)
VOCI = [
 ("A.1.1.3","molteplicita su attributi",["molteplicit"]),
 ("A.1.1.4","association class",["classe associativ","association class"]),
 ("A.1.1.6","identificazione di classe",["{id}","identificazione"]),
 ("A.1.1.8","operazioni di classe",["operazione di classe","operazioni di classe"]),
 ("A.1.1.9","specializzazione di ATTRIBUTI",["specializzazione di attribut","specializzazioni di attribut"]),
 ("A.1.1.9","specializzazione di associazioni",["specializzazione di associazion"]),
 ("A.1.1.9","specializzazione di OPERAZIONI",["specializzazione di operazion"]),
 ("A.1.2.3","inclusione ed estensione use-case",["<<include>>","inclusione"]),
 ("A.1.2.4","generalizzazione tra attori/use-case",["generalizzazione tra attori","generalizzazione fra attori"]),
 ("A.2.2","specifica vincoli esterni",["vincoli esterni"]),
 ("A.4.2","semantica del diagramma in logica",["semantica del diagramma","quello che il diagramma"]),
 ("B.2.1.2","informazione incompleta / NULL",["informazione incompleta","valore nullo","null"]),
 ("B.2.2.2.2","domini definiti dall'utente",["create domain"]),
 ("B.2.2.2.3","generazione valori progressivi",["progressiv","serial","sequence"]),
 ("B.2.2.2.4","viste",["create view","vista","viste"]),
 ("B.2.2.2.5","controllo dell'accesso",["grant","controllo dell'accesso","politiche di accesso"]),
 ("B.2.2.2.6","indici",["create index","indice","indici"]),
 ("B.2.2.3.5","transazioni",["begin transaction","transazione"]),
 ("B.3.1.2.2.1","attributi multivalore",["multivalore"]),
 ("B.3.1.2.2.3","IS-A/generalizzazioni tra classi",["fusione","divisione","sostituzione"]),
 ("B.3.1.2.2.4","IS-A tra associazioni",["is-a fra associazioni","sotto-associazion"]),
 ("B.3.1.2.2.5","identificatori di entita",["identificatori estern","identificatore estern"]),
 ("B.3.1.2.2.6","STIMA DEI COSTI delle operazioni",["stima dei costi","tavola dei volumi","tavola degli accessi"]),
 ("B.3.1.2.2.7","aggiunta controllata di RIDONDANZA",["ridondanza controllata","aggiunta controllata"]),
 ("B.3.1.2.3.3","traduzione relationship binarie",["accorpa"]),
 ("B.3.1.2.3.5","traduzione relationship NON binarie",["non binari","ternaria","n-aria"]),
 ("B.3.2","progettazione delle funzionalita",["pseudo-codice","specifiche realizzative"]),
]
print(f"{'unita':<14} {'concetto':<42} esito")
print("-"*72)
mancanti = []
for u, c, kws in VOCI:
    ok = any(k in testo for k in kws)
    print(f"{u:<14} {c:<42} {'ok' if ok else 'MANCA'}")
    if not ok: mancanti.append((u, c))
print(f"\ncoperti {len(VOCI)-len(mancanti)}/{len(VOCI)} — mancanti: {len(mancanti)}")
