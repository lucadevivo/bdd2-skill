#!/usr/bin/env python3
"""Rende graficamente un diagramma UML delle classi scritto nel formato testuale del corso.

Uso:  uml2png.py <file.md> [-o cartella] [--svg] [--puml]

Legge lo stesso formato di `confronta_uml.py` — `## Classi` con `### Nome`, gli attributi come
elenco puntato, la tabella delle associazioni, l'elenco delle generalizzazioni — e produce un
PNG (o SVG) con PlantUML, senza bisogno di graphviz: usa il layout interno Smetana.

Funziona sia sulle soluzioni prodotte dalla skill sia sui diagrammi ufficiali estratti in
`BDD2-corpus/diagrammi/ufficiali/`, perche' condividono il formato.
"""
import argparse, html, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from confronta_uml import parse, norm

JAR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "plantuml.jar")

def esc(t):
    """Le graffe di {id} o {disjoint} confliggono con il corpo della classe: vanno in entita'.
    I backtick sono marcatura markdown e nel disegno non ci vanno."""
    return t.replace("`", "").replace("{", "&#123;").replace("}", "&#125;")

def leggi_extra(path, sezione):
    """Legge le sezioni che il parser del confronto non modella: classi associative e
    specializzazioni di associazione. Ritorna coppie (nome, riferimento)."""
    out, dentro = [], False
    for riga in open(path, encoding="utf-8"):
        r = riga.strip()
        m = re.match(r"^##\s+(.+)$", r)
        if m:
            dentro = norm(m.group(1)) == norm(sezione)
            continue
        if dentro and r.startswith("-"):
            mm = re.match(r"^-\s+`?([\w À-ÿ]+?)`?\s+(?:su|specializza)\s+`?([\w À-ÿ]+?)`?\s*(?:—|--|$)", r)
            if mm:
                out.append((mm.group(1).strip(), mm.group(2).strip()))
                continue
            # "- `a`, `b` **{disjoint, complete}** rispetto a `gen`": e' il vincolo
            # che regge il modello, prima veniva scartato in silenzio
            mm = re.match(r"^-\s+(.+?)\s*\*{0,2}(\{[^}]*\})\*{0,2}\s*rispetto a\s+`?([\w À-ÿ]+?)`?\s*$", r)
            if mm:
                figli = ", ".join(re.findall(r"`([^`]+)`", mm.group(1))) or mm.group(1)
                out.append((f"{figli} {mm.group(2)}", mm.group(3).strip()))
    return out

def puml(path, titolo):
    classi, assoc, gen = parse(path)
    L = ["@startuml", "!pragma layout smetana", "hide circle",
         "skinparam classAttributeIconSize 0", "skinparam shadowing false",
         "skinparam classBackgroundColor White", "skinparam classBorderColor #333333",
         # un diagramma con molte classi e poca gerarchia esce largo e piatto, e una volta
         # ridotto alla larghezza della pagina diventa illeggibile: piu' spazio fra le file
         # e meno fra i vicini lo rende piu' alto che largo
         "skinparam ranksep 75", "skinparam nodesep 18",
         *( [f"title {esc(titolo)}"] if titolo and titolo.strip() else [] ), ""]

    for nome, attrs in sorted(classi.items()):
        corpo = [f"  {esc(a)}" for a in attrs.values()]
        L.append(f'class "{nome}" ' + ("{\n" + "\n".join(corpo) + "\n}" if corpo else "{\n}"))
    L.append("")

    noti = {norm(k) for k in classi}
    for nome, estremi in sorted(assoc.items()):
        (ca, ma), (cb, mb) = estremi[0], estremi[1]
        if norm(ca) not in noti or norm(cb) not in noti:
            continue                      # estremo non risolto: si salta invece di inventare
        L.append(f'"{ca}" "{esc(ma)}" -- "{esc(mb)}" "{cb}" : {nome} >')
    L.append("")

    # classi associative: tratteggio verso l'associazione che qualificano
    for nome_ac, assoc_ac in leggi_extra(path, "classi associative"):
        if norm(nome_ac) in noti and assoc_ac in assoc:
            (ca, _), (cb, _) = assoc[assoc_ac][0], assoc[assoc_ac][1]
            L.append(f'("{ca}", "{cb}") .. "{nome_ac}"')

    # specializzazioni di associazione: PlantUML non ha il costrutto, si rende come nota
    spec = leggi_extra(path, "specializzazioni di associazione")
    if spec:
        righe = "\n".join(
            "  " + esc(f"{a} rispetto a {b}" if "{" in a else f"{a} specializza {b}")
            for a, b in spec)
        L.append("note as N_spec\n  Specializzazioni di associazione:\n" + righe + "\nend note")

    for sup, figli, vinc in gen:
        for f in sorted(figli):
            if norm(f) in noti and norm(sup) in noti:
                L.append(f'"{sup}" <|-- "{f}"')
        if vinc and norm(sup) in noti:
            L.append(f'note on link : {esc("{" + vinc + "}")}')
    L.append("@enduml")
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("-o", "--out", default=".")
    ap.add_argument("--svg", action="store_true")
    ap.add_argument("--puml", action="store_true", help="scrive solo il sorgente PlantUML")
    a = ap.parse_args()

    base = re.sub(r"\.md$", "", os.path.basename(a.file))
    if base.lower() in ("soluzione", "diagramma"):      # nome generico: usa la cartella
        base = os.path.basename(os.path.dirname(os.path.abspath(a.file))) or base
    os.makedirs(a.out, exist_ok=True)
    src = os.path.join(a.out, base + ".puml")
    open(src, "w", encoding="utf-8").write(puml(a.file, base))
    if a.puml:
        print(src); return

    r = subprocess.run(["java", "-jar", os.path.abspath(JAR),
                        "-tsvg" if a.svg else "-tpng", "-o", os.path.abspath(a.out), src],
                       capture_output=True, text=True)
    uscita = os.path.join(a.out, base + (".svg" if a.svg else ".png"))
    if os.path.exists(uscita):
        print(uscita)
    else:
        print("PlantUML non ha prodotto l'immagine:", r.stderr.strip()[:300], file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()


def puml_usecase(path, titolo=""):
    """Rende il diagramma degli use-case dal formato del corpus:

        Attori: `A`, `B`
        Use case: `U1`, `U2`
        - `A` — `U1`
        - `A` generalizza `B`, `C`

    Lo stesso formato che vpp2uml.py produce dai .vpp ufficiali, piu' la riga di
    generalizzazione fra attori, che li' non c'e' perche' nessun .vpp la usa."""
    attori, usecase, legami, gen = [], [], [], []
    for riga in open(path, encoding="utf-8"):
        r = riga.strip()
        m = re.match(r"^Attori:\s*(.+)$", r, re.I)
        if m:
            attori = re.findall(r"`([^`]+)`", m.group(1)); continue
        m = re.match(r"^Use[ -]?case:\s*(.+)$", r, re.I)
        if m:
            usecase = re.findall(r"`([^`]+)`", m.group(1)); continue
        m = re.match(r"^-\s+`([^`]+)`\s+generalizza\s+(.+)$", r)
        if m:
            gen += [(m.group(1), f) for f in re.findall(r"`([^`]+)`", m.group(2))]; continue
        m = re.match(r"^-\s+`([^`]+)`\s*(?:—|--|-)\s*`([^`]+)`\s*$", r)
        if m:
            legami.append((m.group(1), m.group(2)))
    if not attori or not usecase:
        return None
    ida = {a: f"A_{i}" for i, a in enumerate(attori)}
    idu = {u: f"U_{i}" for i, u in enumerate(usecase)}
    ref = lambda n: ida.get(n) or idu.get(n) or f'"{n}"'
    L = ["@startuml", "!pragma layout smetana", "skinparam shadowing false",
         "skinparam packageStyle rectangle", "left to right direction",
         *( [f"title {esc(titolo)}"] if titolo and titolo.strip() else [] ), ""]
    L += [f'actor "{a}" as {ida[a]}' for a in attori]
    L += [f'usecase "{u}" as {idu[u]}' for u in usecase]
    L.append("")
    L += [f"{ref(p)} <|-- {ref(f)}" for p, f in gen]
    L += [f"{ref(a)} -- {ref(u)}" for a, u in legami]
    L.append("@enduml")
    return "\n".join(L)
