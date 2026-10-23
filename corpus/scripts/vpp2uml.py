"""Estrae i diagrammi UML da un progetto Visual Paradigm (.vpp = database SQLite).

A differenza del vecchio vpp2md.py, legge la tabella DIAGRAM_ELEMENT: cio' che conta
e' quello che sta *sul diagramma*, non gli elementi orfani rimasti nel modello.

Preserva: molteplicita' (che VP salva in due posti diversi a seconda di come
l'autore le ha scritte), i marcatori di identificazione {id}, i nomi di ruolo,
le classi associative, i vincoli delle generalizzazioni e le note.

Uso:  python3 vpp2uml.py file.vpp [--puml] [--titolo NOME]
"""
import sqlite3, re, os, sys

# ---------------------------------------------------------------- utilita'

def _txt(d):
    return d.decode("utf-8", "replace") if isinstance(d, bytes) else (d or "")

def _blocco(s, i):
    """Ritorna il testo del blocco {...} che inizia in s[i]."""
    dep = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            dep += 1
        elif s[j] == "}":
            dep -= 1
            if dep == 0:
                return s[i:j + 1]
    return s[i:]

def _sotto(d, chiave):
    m = re.search(r"\n\t%s=\{" % chiave, d)
    return _blocco(d, m.end() - 1) if m else None

def _prop(s, k):
    m = re.search(r'\b%s="?([^";\n]*)"?;' % k, s)
    return m.group(1) if m else None

# ------------------------------------------------------------- estrazione

def _attributi(mdef):
    out = []
    for m in re.finditer(r'\{[\w.$]+:"([^"\n]*)":Attribute\s*\{', mdef):
        b = _blocco(mdef, m.end() - 1)
        g = lambda k: (re.search(r'\b%s="([^"]*)"' % k, b) or [None, None])[1]
        out.append({"nome": m.group(1), "tipo": g("type_string"),
                    "mod": g("typeModifier"), "mult": g("multiplicity"),
                    "default": g("initialValue_string")
                    or g("initialValue") or None})
    return out

def _operazioni(mdef):
    out = []
    for m in re.finditer(r'\{[\w.$]+:"([^"\n]*)":Operation\s*\{', mdef):
        b = _blocco(mdef, m.end() - 1)
        rt = re.search(r'returnType_string="([^"]*)"', b)
        out.append({"nome": m.group(1), "ritorno": rt.group(1) if rt else None})
    return out

def _estremo(blk):
    """Un AssociationEnd. VP mette la molteplicita' o nel NOME dell'estremo
    (se l'autore l'ha digitata li') o nella proprieta' multiplicity."""
    h = re.match(r'\{[\w.$]+:(?:"([^"\n]*)"|NULL):AssociationEnd', blk)
    nome = h.group(1) if h and h.group(1) is not None else ""
    corpo = re.sub(r"qualifier=\{.*?\n\t\t\}\};", "", blk, flags=re.S)
    tid = re.search(r"\btype=<([\w.$]+)>", corpo)
    return {"etichetta": nome, "multiplicity": _prop(corpo, "multiplicity"),
            "aggregazione": _prop(corpo, "AggregationKind"),
            "tid": tid.group(1) if tid else None}

def molteplicita(e):
    """Testo da mostrare sull'estremo: etichetta scritta a mano, o la proprieta'."""
    if e["etichetta"] and e["multiplicity"] and e["etichetta"] != e["multiplicity"]:
        return f"{e['etichetta']} ({e['multiplicity']})"
    return e["etichetta"] or e["multiplicity"] or ""

def leggi(path):
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    me = {i: (t, n, _txt(d)) for i, t, n, d in
          con.execute("select ID,MODEL_TYPE,NAME,DEFINITION from MODEL_ELEMENT")}
    de = list(con.execute("select ID,SHAPE_TYPE,DIAGRAM_ID,MODEL_ELEMENT_ID,PARENT_ID,DEFINITION"
                          " from DIAGRAM_ELEMENT"))
    dia = list(con.execute("select ID,DIAGRAM_TYPE,NAME from DIAGRAM"))
    con.close()
    shape2model = {r[0]: r[3] for r in de}
    # le classi associative sono forme AssociationClass che legano una classe
    # (_fromShape) all'associazione che decorano (_toConnector)
    assoc_cls = {}
    for r in de:
        if r[1] != "AssociationClass":
            continue
        f = re.search(r"_fromShape=<([\w.$:]+)>", _txt(r[5]))
        t = re.search(r"_toConnector=<([\w.$:]+)>", _txt(r[5]))
        if f and t:
            assoc_cls[shape2model.get(f.group(1).split(":")[-1])] = \
                shape2model.get(t.group(1).split(":")[-1])

    def per_shape(m):
        """Risale al modello dal riferimento a una forma (<diagramma:forma>)."""
        if not m:
            return None
        return shape2model.get(m.group(1).split(":")[-1])

    out = []
    for did, dtype, dname in dia:
        el = [r for r in de if r[2] == did]
        if not el:
            continue
        d = {"nome": dname, "tipo": dtype, "classi": {}, "associazioni": [],
             "generalizzazioni": [], "note": [], "attori": [], "usecase": [],
             "include": [], "tipi_dato": set(), "vincoli_posati": [], "altro": []}
        ancore = {}
        for sid, stype, _, mid, pid, sdef in el:
            if stype != "Anchor":
                continue
            sdef = _txt(sdef)
            capi = [me.get(shape2model.get(m.group(2).split(":")[-1]))
                    for m in re.finditer(r"_(from|to)Shape=<([\w.$:]+)>", sdef)]
            nota = next((c for c in capi if c and c[0] == "NOTE"), None)
            cls = next((c for c in capi if c and c[0] == "Class"), None)
            if nota and cls:
                ancore[nota[2]] = cls[1]
        for sid, stype, _, mid, pid, sdef in el:
            sdef = _txt(sdef)
            mt, mn, mdef = me.get(mid, ("?", None, ""))
            if mt == "Class":
                d["classi"][mn] = {"attributi": _attributi(mdef),
                                   "operazioni": _operazioni(mdef),
                                   "associativa": mid in assoc_cls,
                                   "astratta": bool(re.search(r"\bAbstract=T;", mdef))}
                d["tipi_dato"].update(re.findall(r'type_string="([^"]+)"', mdef))
            elif mt == "Association":
                a, b = _sotto(mdef, "from"), _sotto(mdef, "to")
                a = _estremo(a) if a else {}
                b = _estremo(b) if b else {}
                fs = re.search(r"_fromShape=<([\w.$:]+)>", sdef)
                ts = re.search(r"_toShape=<([\w.$:]+)>", sdef)
                def cl(e, sh):
                    k = e.get("tid") or per_shape(sh)
                    return me[k][1] if k in me else "?"
                d["associazioni"].append({
                    "nome": mn or "",
                    "classe_associativa": next((me[c][1] for c, aid in assoc_cls.items()
                                                if aid == mid and c in me), None),
                    "A": {"classe": cl(a, fs), "molt": molteplicita(a),
                          "aggregazione": a.get("aggregazione")},
                    "B": {"classe": cl(b, ts), "molt": molteplicita(b),
                          "aggregazione": b.get("aggregazione")}})
            elif mt == "Generalization":
                fm = re.search(r"fromModel=<([\w.$]+)>", mdef)
                tm = re.search(r"toModel=<([\w.$]+)>", mdef)
                fs = re.search(r"_fromShape=<([\w.$:]+)>", sdef)
                ts = re.search(r"_toShape=<([\w.$:]+)>", sdef)
                def res(mm, sh):
                    k = (mm.group(1) if mm else None) or per_shape(sh)
                    return (me[k][0], me[k][1]) if k in me else (None, None)
                tsup, sup = res(fm, fs)
                tsub, sub = res(tm, ts)
                d["generalizzazioni"].append(
                    {"vincolo": mn or "", "super": sup, "sub": sub,
                     "fra_associazioni": tsup == "Association" or tsub == "Association"})
            elif mt == "NOTE":
                m = re.search(r'documentation_plain="(.*?)";\n', mdef, re.S)
                if m:
                    d["note"].append((ancore.get(mdef), m.group(1)))
            elif mt == "Constraint":
                d["vincoli_posati"].append(mn)
            elif mt == "Actor":
                d["attori"].append(mn)
            elif mt == "UseCase":
                d["usecase"].append(mn)
            elif mt == "Include":
                fm = re.search(r"fromModel=<([\w.$]+)>", mdef)
                tm = re.search(r"toModel=<([\w.$]+)>", mdef)
                d["include"].append((me.get(fm.group(1), ("", "?"))[1] if fm else "?",
                                     me.get(tm.group(1), ("", "?"))[1] if tm else "?"))
            elif stype not in ("Freehand",):
                d["altro"].append((stype, mn))
        d["tipi_dato"] = sorted(x for x in d["tipi_dato"] if x)
        out.append(d)
    return out

# ------------------------------------------------------------------ resa

def _attr_riga(a):
    r = f"- `{a['nome']}`"
    if a["tipo"]:
        r += f": {a['tipo']}"
    if a["mult"] or a["mod"]:
        r += f" {a['mult'] or a['mod']}"
    if a["default"]:
        r += f" = {a['default']}"
    return r

def markdown(path):
    """Markdown nel formato del corso (lo stesso che leggono confronta_uml.py e
    uml2png.py): un solo diagramma delle classi per file, gli use case in coda."""
    ds = leggi(path)
    cd = [d for d in ds if d["classi"]]
    titolo = "Diagramma UML delle classi" if cd else "Diagramma degli use-case"
    L = [f"# {titolo} — {os.path.basename(path)}", ""]
    for d in cd:
        if d["tipi_dato"]:
            L += ["## Tipi di dato", "", ", ".join(f"`{x}`" for x in d["tipi_dato"]), ""]
        L += ["## Classi", ""]
        for n, c in sorted(d["classi"].items()):
            tag = " _(classe associativa)_" if c["associativa"] else ""
            tag += " _(astratta)_" if c["astratta"] else ""
            L.append(f"### {n}{tag}")
            if not c["attributi"] and not c["operazioni"]:
                L.append("_(nessun attributo)_")
            L += [_attr_riga(a) for a in c["attributi"]]
            L += [f"- **{o['nome']}()**" + (f": {o['ritorno']}" if o["ritorno"] else "")
                  + "  _(operazione)_" for o in c["operazioni"]]
            L.append("")
        if d["associazioni"]:
            L += ["## Associazioni", "",
                  "| associazione | estremo A | estremo B |", "|---|---|---|"]
            for a in sorted(d["associazioni"], key=lambda x: x["nome"]):
                nome = a["nome"] or "(senza nome)"
                if a["classe_associativa"]:
                    nome += f" _(classe associativa: {a['classe_associativa']})_"
                L.append(f"| {nome} | {a['A']['classe']} `{a['A']['molt'] or '?'}` "
                         f"| {a['B']['classe']} `{a['B']['molt'] or '?'}` |")
            L.append("")
        if d["generalizzazioni"] or d["vincoli_posati"]:
            L += ["## Generalizzazioni", ""]
            for g in sorted(d["generalizzazioni"],
                            key=lambda x: (x["super"] or "~", x["sub"] or "")):
                if g["super"] and g["sub"]:
                    L.append(f"- `{g['super']}` generalizza `{g['sub']}`"
                             + (f"  **{g['vincolo']}**" if g["vincolo"] else "")
                             + ("  _(fra associazioni)_" if g["fra_associazioni"] else ""))
                else:
                    L.append("- ⚠ generalizzazione che il file non permette di risolvere"
                             + (f", vincolo **{g['vincolo']}**" if g["vincolo"] else "")
                             + " — leggerla sull'export PNG ufficiale")
            gruppi = sorted({g["super"] for g in d["generalizzazioni"] if g["super"]})
            for v in d["vincoli_posati"]:
                if len(gruppi) == 1:
                    dove = f", riferito a `{gruppi[0]}` (unico gruppo)"
                elif not gruppi:
                    dove = (" — sul diagramma non c'e' nessuna generalizzazione:"
                            " riguarda le gerarchie rese con associazioni `*_isa_*`")
                else:
                    dove = " — su quale gruppo lo dice solo il PNG ufficiale"
                L.append(f"- vincolo **{v}** posato sul diagramma senza collegamento" + dove)
            L.append("")
        for cls, n in d["note"]:
            cap = f"Nota su `{cls}`" if cls else "Nota sul diagramma"
            L += [f"> **{cap}.** " + n.replace("\n", "\n> "), ""]
        if d["altro"]:
            L += [f"_(altri elementi sul diagramma: {d['altro']})_", ""]
    for d in ds:
        if not d["attori"] and not d["usecase"]:
            continue
        L += ["## Use case", "",
              "Attori: " + ", ".join(f"`{a}`" for a in sorted(d["attori"])), "",
              "Use case: " + ", ".join(f"`{u}`" for u in sorted(d["usecase"])), ""]
        for a in sorted(d["associazioni"], key=lambda x: x["nome"]):
            L.append(f"- `{a['A']['classe']}` — `{a['B']['classe']}`"
                     + (f"  ({a['nome']})" if a["nome"] else ""))
        for x, y in d["include"]:
            L.append(f"- `{x}` «include» `{y}`")
        L.append("")
        for cls, n in d["note"]:
            cap = f"Nota su `{cls}`" if cls else "Nota sul diagramma"
            L += [f"> **{cap}.** " + n.replace("\n", "\n> "), ""]
    return "\n".join(L)

def _q(s):
    return s.replace("{", "&#123;").replace("}", "&#125;")

def _uc_puml(d, titolo):
    L = ["@startuml", "!pragma layout smetana", "skinparam shadowing false",
         f"title {titolo}", ""]
    L += [f'actor "{a}" as A_{i}' for i, a in enumerate(sorted(d["attori"]))]
    L += [f'usecase "{u}" as U_{i}' for i, u in enumerate(sorted(d["usecase"]))]
    ida = {a: f"A_{i}" for i, a in enumerate(sorted(d["attori"]))}
    idu = {u: f"U_{i}" for i, u in enumerate(sorted(d["usecase"]))}
    ref = lambda n: ida.get(n) or idu.get(n) or f'"{n}"'
    L.append("")
    for a in d["associazioni"]:
        et = f" : {a['nome']}" if a["nome"] else ""
        L.append(f'{ref(a["A"]["classe"])} -- {ref(a["B"]["classe"])}{et}')
    for x, y in d["include"]:
        L.append(f'{ref(x)} ..> {ref(y)} : <<include>>')
    L.append("@enduml")
    return "\n".join(L)

def puml(path, titolo=None):
    tutti = leggi(path)
    ds = [d for d in tutti if d["classi"]]
    if not ds:
        return _uc_puml(tutti[0], titolo or os.path.basename(path)[:-4])
    d = ds[0]
    L = ["@startuml", "!pragma layout smetana", "hide circle",
         "skinparam classAttributeIconSize 0", "skinparam shadowing false",
         "skinparam classBackgroundColor White", "skinparam classBorderColor #333333",
         f"title {titolo or os.path.basename(path)[:-4]}", ""]
    for n, c in sorted(d["classi"].items()):
        L.append(f'class "{n}" {{')
        for a in c["attributi"]:
            r = a["nome"] + (f": {a['tipo']}" if a["tipo"] else "")
            if a["mult"] or a["mod"]:
                r += " " + (a["mult"] or a["mod"])
            L.append("  " + _q(r))
        for o in c["operazioni"]:
            L.append("  " + _q(f"{o['nome']}(): {o['ritorno']}" if o["ritorno"] else f"{o['nome']}()"))
        L.append("}")
    L.append("")
    for a in d["associazioni"]:
        et = a["nome"] or ""
        ma = f' "{_q(a["A"]["molt"])}"' if a["A"]["molt"] else ""
        mb = f' "{_q(a["B"]["molt"])}"' if a["B"]["molt"] else ""
        L.append(f'"{a["A"]["classe"]}"{ma} --{mb} "{a["B"]["classe"]}"'
                 + (f" : {et}" if et else ""))
    # classi associative: collegamento tratteggiato all'associazione omonima
    for a in d["associazioni"]:
        if a["classe_associativa"]:
            L.append(f'"{a["classe_associativa"]}" ..  "{a["A"]["classe"]}" '
                     f': <<classe associativa di {a["nome"] or "(senza nome)"}>>')
    L.append("")
    nid = 0
    for g in d["generalizzazioni"]:
        if g["super"] and g["sub"] and not g["fra_associazioni"]:
            L.append(f'"{g["super"]}" <|-- "{g["sub"]}"')
            if g["vincolo"]:
                L.append(f"note on link : {_q(g['vincolo'])}")
        elif g["vincolo"] or g["fra_associazioni"]:
            nid += 1
            L.append(f'note as N_g{nid}')
            L.append(f"  generalizzazione fra associazioni / non resa: {_q(g['vincolo'] or '(senza vincolo)')}")
            L.append("end note")
    for i, (cls, n) in enumerate(d["note"]):
        L.append(f'note as N_n{i}')
        L += ["  " + _q(x) for x in n.splitlines()]
        L.append("end note")
        if cls:
            L.append(f'N_n{i} .. "{cls}"')
    for i, v in enumerate(d["vincoli_posati"]):
        L += [f'note as N_v{i}', f"  vincolo posato sul diagramma: {_q(v)}", "end note"]
    L.append("@enduml")
    return "\n".join(L)

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tit = None
    if "--titolo" in sys.argv:
        tit = sys.argv[sys.argv.index("--titolo") + 1]
        args = [a for a in args if a != tit]
    for p in args:
        print(puml(p, tit) if "--puml" in sys.argv else markdown(p))
