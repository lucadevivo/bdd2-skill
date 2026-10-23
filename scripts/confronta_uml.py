#!/usr/bin/env python3
"""Confronta un diagramma UML prodotto con quello ufficiale.

Uso:  confronta_uml.py <soluzione.md> <ufficiale.md>

Legge il formato usato sia dalle soluzioni della skill sia da vpp2uml.py:
classi come `### Nome` (o `**Nome**`), attributi come `- \\`attr\\`: Tipo`,
associazioni in una tabella markdown, generalizzazioni come elenco puntato.

Il confronto e strutturale e volutamente grezzo: serve a far emergere classi
mancanti, attributi persi e molteplicita divergenti, non a dare un voto. Nomi
diversi per lo stesso concetto (Cliente / Proprietario) risultano come
divergenze e vanno letti da un umano.
"""
import re, sys, unicodedata

def norm(s):
    """Confronto insensibile ad accenti, maiuscole, underscore e spazi."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_]+", "", s).lower()

def raggruppa(g):
    """Le generalizzazioni si scrivono sia con i figli su una riga sola sia una
    riga per coppia (e' la forma che produce vpp2uml.py, perche' nel .vpp ogni
    arco e' un elemento a se'). Vanno fuse per superclasse: senza questo resta
    solo l'ultima riga e le altre sottoclassi spariscono dal confronto e dal
    disegno. Il vincolo lo porta una riga sola del gruppo."""
    out = {}
    for sup, figli, vinc in g:
        k = norm(sup)
        nome, f0, v0 = out.get(k, (sup, set(), ""))
        out[k] = (nome, f0 | figli, v0 or vinc)
    return out


def parse(path):
    testo = open(path, encoding="utf-8").read()
    classi, assoc, gen = {}, {}, []
    corrente = None
    in_classi = in_assoc = in_gen = False   # ogni sezione si legge solo sotto la propria intestazione
    dentro_codice = False
    for riga in testo.splitlines():
        r = riga.strip()

        if r.startswith("```"):          # dentro un blocco di codice non si parsa nulla
            dentro_codice = not dentro_codice
            continue
        if dentro_codice:
            continue

        m2 = re.match(r"^##\s+(.+)$", r)
        if m2:
            sez = norm(m2.group(1))
            in_classi = sez.startswith("class")          # "Classi", "Classi associative"
            in_assoc = sez.startswith("associazioni")
            in_gen = sez.startswith("generalizzazioni")
            corrente = None
        elif re.match(r"^\*\*\w[^*]*:\*\*", r):
            corrente = None

        m = (re.match(r"^###\s+(.+?)\s*$", r) or re.match(r"^\*\*([A-Z][\w À-ÿ]*)\*\*(?!:)", r)) if in_classi else None
        if m and not norm(m.group(1)).startswith(("classi", "associazioni", "generalizzazioni",
                                                  "tipididato", "vincoli")):
            corrente = re.sub(r"\s*\*?\(.*", "", m.group(1)).strip()
            classi.setdefault(corrente, {})
            continue


        # riga di tabella: | assoc | Classe `molt` | Classe `molt` |
        if in_assoc and r.startswith("|") and r.count("|") >= 3 and "---" not in r:
            celle = [c.strip() for c in r.strip("|").split("|")]
            if len(celle) < 3 or norm(celle[0]) in ("associazione", "assoc", ""):
                continue
            nome = celle[0].strip("`* ")
            estremi = []
            for c in celle[1:3]:
                # tollera sia "Classe `0..*`" sia "`Classe` 0..*": si tolgono i backtick
                # e si separa la molteplicita dal nome cercandone il pattern
                nudo = c.replace("`", " ").strip()
                # la molteplicita e' la coda di token senza lettere: regge "0..*",
                # "1..1 {id}", "?" e anche i refusi del prof come "0.:*"
                tok = nudo.split()
                i = len(tok)
                while i and not re.search(r"[A-Za-zÀ-ÿ]", tok[i - 1].replace("id", "")):
                    i -= 1
                estremi.append((" ".join(tok[:i]).strip(), " ".join(tok[i:]) or "?"))
            assoc[nome] = estremi
            continue

        m = re.match(r"^-\s+`?([\w À-ÿ]+?)`?\s+generalizza\s+(.+)$", r) if in_gen else None
        if m:
            figli = re.findall(r"`([^`]+)`", m.group(2))
            vinc = re.search(r"\{([^}]*)\}", m.group(2))
            gen.append((m.group(1).strip(), set(figli), vinc.group(1) if vinc else ""))
            continue
        # "- vincolo **{disjoint, complete}** posato ... riferito a `Persona`"
        m = re.match(r"^-\s+vincolo\s+\*\*\{([^}]*)\}\*\*.*riferito a `([^`]+)`", r) if in_gen else None
        if m:
            gen.append((m.group(2).strip(), set(), m.group(1)))
            continue

        m = re.match(r"^-\s+`([^`]+)`(.*)$", r)
        if m and corrente:
            nome_attr = m.group(1).split(":")[0].strip()
            classi[corrente][nome_attr] = (m.group(1) + m.group(2)).strip()
            continue
        m = re.match(r"^-\s+\*\*([^*]+)\*\*(.*)$", r)   # operazioni: - **nome()**: Tipo
        if m and corrente:
            classi[corrente][m.group(1).strip()] = (m.group(1) + m.group(2)).strip()
            continue
    return classi, assoc, [v for v in raggruppa(gen).values()]

def sezione(titolo, righe):
    print(f"\n## {titolo}")
    print("\n".join(f"  {r}" for r in righe) if righe else "  (nessuna differenza)")

def main(mia, uff):
    cA, aA, gA = parse(mia)
    cB, aB, gB = parse(uff)
    print(f"# Confronto\n\nprodotta:  {mia}\nufficiale: {uff}")
    print(f"\nclassi: {len(cA)} vs {len(cB)} | associazioni: {len(aA)} vs {len(aB)}")

    mapA = {norm(k): k for k in cA}
    mapB = {norm(k): k for k in cB}
    solo_a = [mapA[k] for k in mapA.keys() - mapB.keys()]
    solo_b = [mapB[k] for k in mapB.keys() - mapA.keys()]
    sezione("Classi solo nella soluzione prodotta", sorted(solo_a))
    sezione("Classi solo in quella ufficiale (MANCANTI)", sorted(solo_b))

    diff_attr = []
    for k in sorted(mapA.keys() & mapB.keys()):
        na, nb = {norm(x) for x in cA[mapA[k]]}, {norm(x) for x in cB[mapB[k]]}
        pers = {x for x in cB[mapB[k]] if norm(x) not in na}
        extra = {x for x in cA[mapA[k]] if norm(x) not in nb}
        if pers or extra:
            diff_attr.append(f"{mapB[k]}: mancanti {sorted(pers) or '-'} | in piu {sorted(extra) or '-'}")
    sezione("Attributi divergenti nelle classi comuni", diff_attr)

    # Le associazioni si accoppiano prima per nome, poi per coppia di classi
    # collegate: senza il secondo passo un nome diverso (`ins_prof` contro
    # `insegna`) nasconde una molteplicita sbagliata, che e' l'errore che conta.
    def coppia(estremi):
        return tuple(sorted(norm(c) for c, _ in estremi))

    amapA = {norm(k): k for k in aA}
    amapB = {norm(k): k for k in aB}
    accoppiate = [(amapA[k], amapB[k]) for k in amapA.keys() & amapB.keys()]
    restaA = {amapA[k] for k in amapA.keys() - amapB.keys()}
    restaB = {amapB[k] for k in amapB.keys() - amapA.keys()}
    per_coppia = {}
    for n in restaB:
        per_coppia.setdefault(coppia(aB[n]), []).append(n)
    for n in sorted(restaA):
        cand = per_coppia.get(coppia(aA[n]))
        if cand:
            m = cand.pop(0)
            accoppiate.append((n, m))
            restaA.discard(n)
            restaB.discard(m)

    sezione("Associazioni solo in quella ufficiale (MANCANTI)",
            sorted(f"{n}: {aB[n]}" for n in restaB))
    sezione("Associazioni solo nella soluzione prodotta",
            sorted(f"{n}: {aA[n]}" for n in restaA))

    def senza_id(estremi):
        return {(norm(c), re.sub(r"\{id\d*\}", "", m).strip()) for c, m in estremi}

    diff_molt, solo_id, rinominate = [], [], []
    for na, nb in sorted(accoppiate, key=lambda x: x[1]):
        ea, eb = aA[na], aB[nb]
        eti = nb if norm(na) == norm(nb) else f"{nb} (tu: {na})"
        # confronta a prescindere dall'ordine degli estremi
        if {(norm(c), m) for c, m in ea} == {(norm(c), m) for c, m in eb}:
            if norm(na) != norm(nb):
                rinominate.append(f"{nb} -> {na}  (stessi estremi, solo nome diverso)")
        elif senza_id(ea) == senza_id(eb):
            # il prof marca l'identificazione esterna sull'estremo solo in 5
            # diagrammi ufficiali su 25: la sua assenza non e' un errore
            solo_id.append(f"{eti}: prodotta {ea} | ufficiale {eb}")
        else:
            diff_molt.append(f"{eti}: prodotta {ea} | ufficiale {eb}")
    sezione("Molteplicita o estremi divergenti", diff_molt)
    sezione("Differiscono solo per l'annotazione {id} (non e' un errore)", solo_id)
    sezione("Associazioni corrette ma con altro nome", rinominate)

    gmapA = {norm(s): (s, f, v) for s, f, v in gA}
    gmapB = {norm(s): (s, f, v) for s, f, v in gB}
    diff_gen = []
    for k in sorted(gmapB):
        if k not in gmapA:
            diff_gen.append(f"MANCANTE: {gmapB[k][0]} generalizza {sorted(gmapB[k][1])} {gmapB[k][2]}")
        else:
            fa, fb = {norm(x) for x in gmapA[k][1]}, {norm(x) for x in gmapB[k][1]}
            if fa != fb or norm(gmapA[k][2]) != norm(gmapB[k][2]):
                diff_gen.append(f"{gmapB[k][0]}: prodotta {sorted(gmapA[k][1])} {{{gmapA[k][2]}}} | "
                                f"ufficiale {sorted(gmapB[k][1])} {{{gmapB[k][2]}}}")
    for k in sorted(gmapA.keys() - gmapB.keys()):
        diff_gen.append(f"IN PIU: {gmapA[k][0]} generalizza {sorted(gmapA[k][1])}")
    sezione("Generalizzazioni divergenti", diff_gen)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
