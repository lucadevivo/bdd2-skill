#!/usr/bin/env python3
"""Da una descrizione compatta a un progetto Visual Paradigm da importare.

    python3 genera-vpp-xml.py <descrizione.json> <destinazione.xml>

In Visual Paradigm: `Project -> Import -> XML`, e scegliere il file prodotto. Le classi, gli
attributi, le associazioni e le generalizzazioni compaiono nel Model Explorer; da lì si
trascinano su un diagramma nuovo e VP disegna da solo i collegamenti.

**Il `.vpp` non si genera**: è un database SQLite con uno schema interno non documentato.
L'XML dell'export è invece la stessa porta, aperta nell'altro verso.

## Come è fatto

Non sintetizza gli elementi da zero: **li clona da un progetto vero esportato da VP**
(`MODELLO`, il progetto Go). Ogni elemento di VP si porta dietro una trentina di proprietà
di default — colori, stato di avanzamento, punteggi di qualità — e indovinare quali siano
obbligatorie è un lavoro inutile: clonando restano quelle che VP scrive di suo, e si
riscrivono solo identificatore, nome e riferimenti.

## Il formato della descrizione

    {
      "nome": "CozyRooms",
      "classi": {
        "Utente":   [["email", "Stringa {id}"], ["nome", "Stringa"]],
        "Struttura": [["nome", "Stringa"], ["stelle", "Intero 1..7"]]
      },
      "associazioni": [
        {"nome": "gestisce", "da": "Utente", "molt_da": "1..*",
                              "a": "Struttura", "molt_a": "0..*"}
      ],
      "generalizzazioni": [
        {"padre": "Utente", "figlie": ["UtentePrivato", "UtenteGestore"]}
      ],

      "attori":  ["Ospite", "Gestore"],
      "usecase": ["Prenota", "GestisciStrutture"]
    }

Attori e use-case sono elementi come le classi: si collegano con le stesse `associazioni`
(attore-use-case) e le stesse `generalizzazioni` (fra attori). Un diagramma degli use-case
si descrive quindi con `attori`, `usecase`, `associazioni` e nient'altro.

**`molt_da` è la molteplicità che si scrive accanto alla classe `da`**, cioè quanti oggetti
di `da` partecipano per ogni oggetto di `a`. È la convenzione UML, ed è l'opposto di dove
la scriverebbe un diagramma ER: in ER la cardinalità sta sul ramo dell'entità a cui si
riferisce.

Due trappole del formato, già gestite: **la molteplicità di VP sta nel *nome* dell'estremo**
(la proprietà `multiplicity` resta `Unspecified`), e il tipo di un attributo sta in un
`TextModelProperty[type]`, non in un attributo XML.
"""
import json, sys
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

URI = "http://www.visual-paradigm.com/product/vpuml/modelexporter"
NS = "{" + URI + "}"
# il modello di partenza deve contenere almeno un esemplare di ogni cosa che si vuole
# generare: QuickHospital ha classi, attributi, associazioni, generalizzazioni, attori e
# use-case tutti insieme.
MODELLO = (Path.home() /
           "Scrivania/BDD2-vpp-da-esportare/03 - QuickHospital — Analisi — QuickHospital/project.xml")
# QuickHospital non ha classi associative: quelle si prendono in prestito da Go, che ne ha una.
DONATORE = Path.home() / "Scrivania/BDD2-vpp-da-esportare/02 - Go/project.xml"


def q(nome):
    return NS + nome


class Identificatori:
    """VP usa chiavi di 16 caratteri. Bastano univoche dentro il file."""

    def __init__(self):
        self.n = 0

    def __call__(self):
        self.n += 1
        return f"BDD2gen{self.n:09d}"


def proprieta(modello, tipo, nome):
    for p in modello.findall(f"{q('ModelProperties')}/{q(tipo)}"):
        if p.get("name") == nome:
            return p
    return None


def scrivi_stringa(modello, nome, valore):
    p = proprieta(modello, "StringProperty", nome)
    if p is not None:
        p.set("value", valore)


def scrivi_testo(modello, nome, valore):
    p = proprieta(modello, "TextModelProperty", nome)
    if p is None:
        return
    v = p.find(q("StringValue"))
    if v is None:
        v = ET.SubElement(p, q("StringValue"))
    v.set("value", valore)


def scrivi_riferimento(modello, nome, id_puntato):
    p = proprieta(modello, "ModelRefProperty", nome)
    if p is None:
        return
    for vecchio in list(p):
        p.remove(vecchio)
    ET.SubElement(p, q("ModelRef")).set("id", id_puntato)


RELAZIONI = ("FromSimpleRelationships", "ToSimpleRelationships",
             "FromEndRelationships", "ToEndRelationships")


def ripulisci(modello, nuovo_id):
    """Identificatore nuovo, via i riferimenti a diagrammi che qui non esistono e via i
    **riferimenti alle relazioni** che l'esemplare si porta dietro dal progetto di
    partenza: puntano a id che in questo file non esistono più."""
    modello.set("id", nuovo_id)
    for nome in ("referencedByDiagramIds", "referencedByModelAddresses"):
        p = proprieta(modello, "StringArrayProperty", nome)
        if p is not None:
            for vecchio in list(p):
                p.remove(vecchio)
    for e in list(modello):
        if e.tag.split("}")[-1] in RELAZIONI:
            modello.remove(e)


def relaziona(modello, tag, id_rel, id_from, id_to):
    """La contro-referenza che VP scrive su ogni capo di una relazione.

    Senza di questa un'associazione si ricostruisce lo stesso (i suoi estremi puntano alle
    classi), ma una **generalizzazione fra associazioni** no: il solo `from`/`to` sulla
    generalizzazione non basta e VP la lascia cadere. Va scritta su entrambi i capi:
    `FromSimpleRelationships` sul generale, `ToSimpleRelationships` sullo specifico."""
    cont = modello.find(q(tag))
    if cont is None:
        cont = ET.Element(q(tag))
        # nei file veri i contenitori stanno dopo ChildModels e prima di FromEnd/ToEnd
        posizioni = [i for i, e in enumerate(modello)
                     if e.tag.split("}")[-1] in ("FromEnd", "ToEnd")]
        modello.insert(posizioni[0], cont) if posizioni else modello.append(cont)
    ET.SubElement(cont, q("RelationshipRef"), {"from": id_from, "id": id_rel, "to": id_to})


def figli(modello):
    c = modello.find(q("ChildModels"))
    if c is None:
        c = ET.SubElement(modello, q("ChildModels"))
    return c


def prototipi(modelli):
    """Un esemplare per tipo, preso dal progetto vero e messo da parte prima della potatura."""
    def primo(tipo):
        for e in modelli.iter(q("Model")):
            if e.get("modelType") == tipo:
                return deepcopy(e)
        sys.exit(f"nel modello non c'e' nessun {tipo}: serve un export che lo contenga")

    classe = primo("Class")
    attributo = primo("Attribute")
    for c in list(figli(classe)):
        figli(classe).remove(c)
    return {"Class": classe, "Attribute": attributo, "Operation": primo("Operation"),
            "Association": primo("Association"), "Generalization": primo("Generalization"),
            "Actor": primo("Actor"), "UseCase": primo("UseCase")}


def contenitore(modelli, nome):
    """Associazioni e generalizzazioni non stanno sotto `Models`: VP le raccoglie in
    `ModelRelationshipContainer` annidati, uno per tipo di relazione."""
    for e in modelli.iter(q("Model")):
        if e.get("modelType") == "ModelRelationshipContainer" and e.get("name") == nome:
            return e
    if nome in ("Association", "Generalization"):
        sys.exit(f"nel modello manca il contenitore delle relazioni «{nome}»")
    return None


def estremi_associazione(assoc):
    """Gli estremi non sono in `ChildModels` ma in due elementi propri, `FromEnd` e `ToEnd`."""
    fuori = []
    for lato in ("FromEnd", "ToEnd"):
        c = assoc.find(q(lato))
        fuori.append(c.find(q("Model")) if c is not None else None)
    return fuori


def in_prestito(tipo, nome_contenitore):
    """Un esemplare che il modello di partenza non ha: si va a prenderlo in un altro export."""
    radice = ET.parse(DONATORE).getroot()
    modelli = radice.find(q("Models"))
    esemplare = next((e for e in modelli.iter(q("Model")) if e.get("modelType") == tipo), None)
    contenitore = next((e for e in modelli.iter(q("Model"))
                        if e.get("modelType") == "ModelRelationshipContainer"
                        and e.get("name") == nome_contenitore), None)
    if esemplare is None or contenitore is None:
        sys.exit(f"nemmeno {DONATORE.parent.name} ha un {tipo}")
    contenitore = deepcopy(contenitore)
    for e in list(figli(contenitore)):
        figli(contenitore).remove(e)
    return deepcopy(esemplare), contenitore


def prop_diagramma(elemento, tipo, nome):
    for p in elemento.findall(f"{q('DiagramElementProperties')}/{q(tipo)}"):
        if p.get("name") == nome:
            return p
    return None


def scrivi_geometria(elemento, x, y, larghezza, altezza):
    for chiave, valore in (("x", x), ("y", y), ("width", larghezza), ("height", altezza)):
        elemento.set(chiave, str(valore))
        p = prop_diagramma(elemento, "IntegerProperty", chiave)
        if p is not None:
            p.set("value", str(valore))


def prepara_elemento(elemento, id_elemento, id_modello, nome):
    """Un esemplare di forma o di connettore ripulito e riattaccato al modello nuovo."""
    elemento.set("id", id_elemento)
    elemento.set("model", id_modello)
    elemento.set("name", nome)
    p = prop_diagramma(elemento, "ModelRefProperty", "metaModelElement")
    if p is not None:
        for vecchio in list(p):
            p.remove(vecchio)
        ET.SubElement(p, q("ModelRef")).set("id", id_modello)
    for nome_prop in ("referencedByDiagramIds", "referencedByModelAddresses", "layerIds"):
        p = prop_diagramma(elemento, "StringArrayProperty", nome_prop)
        if p is not None:
            for vecchio in list(p):
                p.remove(vecchio)


def prototipi_diagramma(progetto):
    """Un esemplare di diagramma, di forma e di connettore per tipo.

    Il diagramma va generato, non lasciato vuoto: VP disegna da solo le associazioni fra le
    classi che trascini, ma una **generalizzazione fra associazioni** ha per capi due
    connettori, non due forme — se il diagramma non ce l'ha, non c'e' modo di farla comparire.
    """
    forme, connettori, diagrammi = {}, {}, {}
    for sorgente in (progetto, ET.parse(DONATORE).getroot()):
        contenitore = sorgente.find(q("Diagrams"))
        if contenitore is None:
            continue
        for d in contenitore:
            diagrammi.setdefault(d.get("diagramType"), deepcopy(d))
            for gruppo, dove in ((q("Shapes"), forme), (q("Connectors"), connettori)):
                elenco = d.find(gruppo)
                for e in (elenco if elenco is not None else []):
                    # gli esemplari si tengono **per tipo di diagramma**: l'associazione di
                    # un diagramma degli use-case non ha i riquadri dei ruoli, e presa come
                    # esemplare in un diagramma delle classi fa sparire le molteplicità
                    dove.setdefault((d.get("diagramType"), e.get("shapeType")), deepcopy(e))
                    dove.setdefault(e.get("shapeType"), deepcopy(e))
    for d in diagrammi.values():
        for gruppo in (q("Shapes"), q("Connectors")):
            elenco = d.find(gruppo)
            if elenco is not None:
                for e in list(elenco):
                    elenco.remove(e)
    return diagrammi, forme, connettori


def genera(spec: dict, modello: Path, destinazione: Path):
    ET.register_namespace("", URI)
    albero = ET.parse(modello)
    progetto = albero.getroot()
    progetto.set("name", spec["nome"])
    modelli = progetto.find(q("Models"))

    proto = prototipi(modelli)
    cont_assoc = contenitore(modelli, "Association")
    cont_gen = contenitore(modelli, "Generalization")

    # potatura: via le classi, le associazioni e le generalizzazioni del progetto di
    # partenza, e i diagrammi, che punterebbero a elementi ormai inesistenti. Resta
    # l'impalcatura (stili, tipi di dato, viewpoint) che VP si aspetta di trovare.
    for e in list(modelli):
        # NOTE: i tre commenti che il docente aveva lasciato sul diagramma di QuickHospital
        # («Svolgimento parziale…», «licenze poetiche…») finivano in ogni file generato
        if e.get("modelType") in ("Class", "Actor", "UseCase", "NOTE"):
            modelli.remove(e)
    for c in (cont_assoc, cont_gen, contenitore(modelli, "AssociationClass"),
              contenitore(modelli, "Include")):
        if c is not None:
            for e in list(figli(c)):
                figli(c).remove(e)
    proto_diagrammi, proto_forme, proto_connettori = prototipi_diagramma(progetto)
    diagrammi = progetto.find(q("Diagrams"))
    if diagrammi is not None:
        for e in list(diagrammi):
            diagrammi.remove(e)

    nuovo_id = Identificatori()
    id_di = {}        # nome -> id
    id_modello = {}   # id -> elemento, per scrivere le contro-referenze sui capi

    # il diagramma: use-case se la descrizione ha attori o use-case, altrimenti delle classi
    tipo_diagramma = "UseCaseDiagram" if (spec.get("attori") or spec.get("usecase")) else "ClassDiagram"
    diagramma = deepcopy(proto_diagrammi[tipo_diagramma])
    diagramma.set("id", nuovo_id())
    diagramma.set("name", spec["nome"])
    diagramma.set("imageFileName", "")
    forme = diagramma.find(q("Shapes"))
    connettori = diagramma.find(q("Connectors"))
    if forme is None:
        forme = ET.SubElement(diagramma, q("Shapes"))
    if connettori is None:
        connettori = ET.SubElement(diagramma, q("Connectors"))
    if diagrammi is not None:
        diagrammi.append(diagramma)
    elemento_di = {}   # id del modello -> id della forma o del connettore che lo disegna
    posto = [0]        # contatore per la disposizione a griglia

    centro = {}        # id del modello -> centro del suo elemento sul diagramma

    def disegna_forma(tipo, id_mod, nome, larghezza, altezza):
        n = posto[0]
        posto[0] += 1
        x, y = 60 + (n % 4) * 320, 60 + (n // 4) * 260
        esemplare = proto_forme.get((tipo_diagramma, tipo))
        s = deepcopy(esemplare if esemplare is not None else proto_forme[tipo])
        prepara_elemento(s, nuovo_id(), id_mod, nome)
        scrivi_geometria(s, x, y, larghezza, altezza)
        forme.append(s)
        elemento_di[id_mod] = s.get("id")
        centro[id_mod] = (x + larghezza // 2, y + altezza // 2)

    def etichetta(elemento, testo, x, y):
        """Il riquadro del nome. Se resta quello dell'esemplare — coordinate e larghezza del
        diagramma di QuickHospital — VP non ci fa stare il nome e disegna «...»."""
        cap = elemento.find(q("Caption"))
        if cap is None:
            return
        larghezza = max(24, 8 * len(testo) + 12)   # largo abbondante: se ci sta stretto VP scrive «...»
        cap.set("width", str(larghezza))
        cap.set("height", "15")
        cap.set("x", str(x - larghezza // 2))
        cap.set("y", str(y - 8))
        for nome_prop in ("internalWidth", "internalHeight"):
            cap.set(nome_prop, "-2147483648")

    def disegna_connettore(tipo, id_mod, nome, id_da, id_a):
        # i capi possono essere forme (classi) o altri connettori (specializzazione di
        # associazione): il formato non distingue, basta l'id dell'elemento di diagramma
        if id_da not in elemento_di or id_a not in elemento_di:
            return
        esemplare = proto_connettori.get((tipo_diagramma, tipo))
        c = deepcopy(esemplare if esemplare is not None else proto_connettori[tipo])
        prepara_elemento(c, nuovo_id(), id_mod, nome)
        c.set("from", elemento_di[id_da])
        c.set("to", elemento_di[id_a])
        (x1, y1), (x2, y2) = centro[id_da], centro[id_a]
        scrivi_geometria(c, min(x1, x2), min(y1, y2),
                         max(10, abs(x2 - x1)), max(10, abs(y2 - y1)))
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        centro[id_mod] = (mx, my)
        etichetta(c, nome, mx, my)
        # le molteplicità sono i nomi degli estremi: VP le disegna nei riquadri dei ruoli,
        # che vanno spostati anche loro vicino ai due capi
        for ruolo, (rx, ry) in (("RoleA", (x1 + (x2 - x1) // 4, y1 + (y2 - y1) // 4)),
                                ("RoleB", (x2 - (x2 - x1) // 4, y2 - (y2 - y1) // 4))):
            r = c.find(q(ruolo))
            cap = r.find(q("NameCaption")) if r is not None else None
            if cap is not None:
                cap.set("width", "44")
                cap.set("height", "18")
                cap.set("x", str(rx - 22))
                cap.set("y", str(ry - 9))
        punti = c.find(q("Points"))
        if punti is not None:
            for vecchio in list(punti):
                punti.remove(vecchio)
        for chiede in ("requestRebuild", "requestRebuildFromEnd", "requestRebuildToEnd",
                       "requestResetCaption", "requestResetCaptionSize"):
            pr = prop_diagramma(c, "BooleanProperty", chiede)
            if pr is not None:
                pr.set("value", "true")
        connettori.append(c)
        elemento_di[id_mod] = c.get("id")

    for nome, contenuto in spec.get("classi", {}).items():
        # una classe è una lista di attributi, oppure {"attributi": [...], "operazioni": [...]}
        attributi = contenuto if isinstance(contenuto, list) else contenuto.get("attributi", [])
        operazioni = [] if isinstance(contenuto, list) else contenuto.get("operazioni", [])
        classe = deepcopy(proto["Class"])
        ripulisci(classe, nuovo_id())
        classe.set("name", nome)
        scrivi_stringa(classe, "name", nome)
        for att_nome, att_tipo in attributi:
            att = deepcopy(proto["Attribute"])
            ripulisci(att, nuovo_id())
            att.set("name", att_nome)
            scrivi_stringa(att, "name", att_nome)
            scrivi_testo(att, "type", att_tipo)
            scrivi_testo(att, "initialValue", "")
            figli(classe).append(att)
        for op_nome, op_tipo in operazioni:
            op = deepcopy(proto["Operation"])
            ripulisci(op, nuovo_id())
            op.set("name", op_nome)
            scrivi_stringa(op, "name", op_nome)
            scrivi_testo(op, "returnType", op_tipo)
            for c in list(figli(op)):
                figli(op).remove(c)          # via i parametri dell'esemplare
            figli(classe).append(op)
        modelli.append(classe)
        id_di[nome] = classe.get("id")
        id_modello[classe.get("id")] = classe
        disegna_forma("Class", classe.get("id"), nome,
                      240, 40 + 18 * (len(attributi) + len(operazioni)))

    for tipo, chiave in (("Actor", "attori"), ("UseCase", "usecase")):
        for nome in spec.get(chiave, []):
            elemento = deepcopy(proto[tipo])
            ripulisci(elemento, nuovo_id())
            elemento.set("name", nome)
            scrivi_stringa(elemento, "name", nome)
            for c in list(figli(elemento)):
                figli(elemento).remove(c)
            modelli.append(elemento)
            id_di[nome] = elemento.get("id")
            id_modello[elemento.get("id")] = elemento
            disegna_forma(tipo, elemento.get("id"), nome,
                          *((45, 91) if tipo == "Actor" else (100, 50)))

    cont_ac = None
    if any(a.get("classe") for a in spec.get("associazioni", [])):
        proto_ac, cont_ac = in_prestito("AssociationClass", "AssociationClass")
        modelli.append(cont_ac)

    for n, a in enumerate(spec.get("associazioni", [])):
        for capo in (a["da"], a["a"]):
            if capo not in id_di:
                sys.exit(f"l'associazione {a['nome']} punta a {capo}, che non esiste")
        assoc = deepcopy(proto["Association"])
        ripulisci(assoc, nuovo_id())
        assoc.set("name", a["nome"])
        scrivi_stringa(assoc, "name", a["nome"])
        estremi = estremi_associazione(assoc)
        if any(e is None for e in estremi):
            sys.exit("l'associazione del modello non ha FromEnd e ToEnd")
        for estremo, (classe, molt) in zip(estremi, [(a["da"], a["molt_da"]),
                                                     (a["a"], a["molt_a"])]):
            ripulisci(estremo, nuovo_id())
            estremo.set("name", molt)          # la molteplicita' sta qui, non in `multiplicity`
            scrivi_stringa(estremo, "name", molt)
            scrivi_riferimento(estremo, "EndModelElement", id_di[classe])
        figli(cont_assoc).append(assoc)
        relaziona(id_modello[id_di[a["da"]]], "FromEndRelationships",
                  assoc.get("id"), id_di[a["da"]], id_di[a["a"]])
        relaziona(id_modello[id_di[a["a"]]], "ToEndRelationships",
                  assoc.get("id"), id_di[a["da"]], id_di[a["a"]])
        disegna_connettore("Association", assoc.get("id"), a["nome"],
                           id_di[a["da"]], id_di[a["a"]])
        # un'associazione con classe associativa non ha nome propriο: il nome lo porta la
        # classe. La chiave serve solo a chi la nomina (le specializzazioni di associazione).
        id_di[a["nome"] or f"·assoc{n}"] = assoc.get("id")
        id_modello[assoc.get("id")] = assoc
        if a.get("classe"):
            if a["classe"] not in id_di:
                sys.exit(f"la classe associativa {a['classe']} non e' fra le classi")
            legame = deepcopy(proto_ac)
            ripulisci(legame, nuovo_id())
            scrivi_riferimento(legame, "from", id_di[a["classe"]])   # from = la classe
            scrivi_riferimento(legame, "to", assoc.get("id"))        # to   = l'associazione
            figli(cont_ac).append(legame)
            relaziona(id_modello[id_di[a["classe"]]], "FromSimpleRelationships",
                      legame.get("id"), id_di[a["classe"]], assoc.get("id"))
            relaziona(assoc, "ToSimpleRelationships",
                      legame.get("id"), id_di[a["classe"]], assoc.get("id"))
            disegna_connettore("AssociationClass", legame.get("id"), "",
                               id_di[a["classe"]], assoc.get("id"))

    for g in spec.get("generalizzazioni", []):
        for capo in [g["padre"], *g["figlie"]]:
            if capo not in id_di:
                sys.exit(f"la generalizzazione punta a {capo}, che non esiste")
        for figlia in g["figlie"]:
            gen = deepcopy(proto["Generalization"])
            ripulisci(gen, nuovo_id())
            scrivi_riferimento(gen, "from", id_di[g["padre"]])   # from = il generale
            scrivi_riferimento(gen, "to", id_di[figlia])         # to   = lo specifico
            # il vincolo {disjoint, complete} non è una proprietà: VP lo tiene nel *nome*
            # della generalizzazione, ed è lì che lo scrivono gli autori del corso
            vincolo = g.get("vincolo", "")
            gen.set("name", vincolo)
            scrivi_stringa(gen, "name", vincolo)
            figli(cont_gen).append(gen)
            relaziona(id_modello[id_di[g["padre"]]], "FromSimpleRelationships",
                      gen.get("id"), id_di[g["padre"]], id_di[figlia])
            relaziona(id_modello[id_di[figlia]], "ToSimpleRelationships",
                      gen.get("id"), id_di[g["padre"]], id_di[figlia])
            disegna_connettore("Generalization", gen.get("id"), vincolo,
                               id_di[g["padre"]], id_di[figlia])

    albero.write(destinazione, encoding="UTF-8", xml_declaration=True)
    print(f"{len(spec.get('classi', {}))} classi, {len(spec.get('attori', []))} attori, "
          f"{len(spec.get('usecase', []))} use-case, {len(spec.get('associazioni', []))} associazioni, "
          f"{sum(len(g['figlie']) for g in spec.get('generalizzazioni', []))} generalizzazioni"
          f"  ->  {destinazione}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__.strip().splitlines()[2].strip())
    genera(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")),
           Path(sys.argv[3]) if len(sys.argv) > 3 else MODELLO,
           Path(sys.argv[2]))
