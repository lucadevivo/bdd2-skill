#!/usr/bin/env python3
"""Compone una soluzione BDD2 in un unico file HTML autosufficiente.

Uso:  componi.py <soluzione.md> [-o cartella] [--titolo "..."]

Prende la soluzione scritta nel formato testuale del corso e produce **un solo file** che
contiene il diagramma UML disegnato (SVG incorporato, quindi ingrandibile e senza file
esterni) e tutto il resto dell'esercizio: raffinamento, tipi di dato, vincoli, specifiche.

Si apre con un doppio clic e si stampa in PDF dal browser. Serve a mettere la propria soluzione
accanto a quella ufficiale e annotare a mano cosa non va.
"""
import argparse, html, os, re, subprocess, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
sys.path.insert(0, os.path.join(QUI, "..", "tools", "pylib"))
import markdown
from uml2png import puml, puml_usecase

JAR = os.path.join(QUI, "..", "tools", "plantuml.jar")

CSS = """
:root { --testo:#1a1a1a; --tenue:#666; --bordo:#d8d8d8; --sfondo:#fff; --codice:#f6f6f4;
        --accento:#8a1c1c; }
* { box-sizing:border-box }
body { max-width:52rem; margin:0 auto; padding:2.5rem 1.5rem 6rem; background:var(--sfondo);
       color:var(--testo); font:16px/1.65 Georgia,'Times New Roman',serif; }
h1 { font-size:1.7rem; margin:0 0 .3rem; letter-spacing:-.01em }
h1 + .sotto { color:var(--tenue); font-size:.9rem; margin-bottom:2.5rem;
              font-family:system-ui,sans-serif }
h2 { font-size:1.25rem; margin:2.6rem 0 .8rem; padding-bottom:.3rem;
     border-bottom:1px solid var(--bordo) }
h3 { font-size:1.02rem; margin:1.6rem 0 .4rem; font-family:system-ui,sans-serif }
h4 { font-size:.95rem; margin:1.2rem 0 .3rem; color:var(--tenue);
     font-family:system-ui,sans-serif }
p, li { margin:.5rem 0 }
code { background:var(--codice); padding:.1em .35em; border-radius:3px;
       font:.87em/1.5 ui-monospace,'SF Mono',Menlo,Consolas,monospace }
pre { background:var(--codice); padding:1rem 1.1rem; border-radius:6px; overflow-x:auto;
      border:1px solid var(--bordo) }
pre code { background:none; padding:0; font-size:.83rem; line-height:1.55 }
table { border-collapse:collapse; margin:1rem 0; font-size:.9rem; display:block;
        overflow-x:auto; max-width:100% }
th, td { border:1px solid var(--bordo); padding:.4rem .7rem; text-align:left; vertical-align:top }
th { background:var(--codice); font-family:system-ui,sans-serif; font-size:.85rem }
blockquote { border-left:3px solid var(--accento); margin:1rem 0; padding:.2rem 0 .2rem 1rem;
             color:var(--tenue) }
/* il diagramma esce dalla colonna di testo: e' l'unica cosa che ha bisogno di larghezza */
.diagramma { border:1px solid var(--bordo); border-radius:6px; padding:1.2rem; margin:1.6rem 0;
             text-align:center; background:#fdfdfc; overflow-x:auto;
             width:92vw; max-width:92vw; position:relative;
             left:50%; right:50%; margin-left:-46vw; margin-right:-46vw }
.diagramma svg { max-width:none; height:auto }
@media (max-width:60rem) { .diagramma{width:auto;max-width:100%;left:auto;right:auto;
                                       margin-left:0;margin-right:0} }

/* le formule non si leggono se scritte di fila: blocco a se', a interlinea larga */
pre.fol { background:#fbfaf7; border:1px solid var(--bordo); border-left:3px solid var(--accento);
          border-radius:0 4px 4px 0; padding:.75rem 1rem; margin:.5rem 0 1rem;
          font:.85rem/1.75 ui-monospace,'SF Mono',Menlo,Consolas,monospace;
          white-space:pre-wrap; overflow-x:auto }
h4 + pre.fol, p + pre.fol { margin-top:.35rem }

/* liste: piu' respiro e rientri visibili, l'analisi dei requisiti e' tutta annidata */
ol, ul { padding-left:1.5rem }
li > ul, li > ol { margin:.35rem 0 .6rem }
li { margin:.35rem 0 }
li > p { margin:.2rem 0 }
.nota { font-family:system-ui,sans-serif; font-size:.82rem; color:var(--tenue);
        margin-top:.5rem }
@page { size:A4; margin:18mm 15mm }
@media print {
  body { max-width:none; padding:0; font-size:10.5pt }
  /* in stampa il fuori-colonna non ha senso: il diagramma torna nel flusso e si adatta */
  .diagramma { width:auto; max-width:100%; left:auto; right:auto;
               margin-left:0; margin-right:0; break-inside:avoid }
  .diagramma svg { max-width:100% }
  h2 { break-after:avoid } h3, h4 { break-after:avoid }
  pre, pre.fol, table { break-inside:avoid }
}
"""

# Le sezioni che alimentano il disegno — l'elenco delle classi con i loro attributi, la tabella
# delle associazioni, le generalizzazioni — nel documento finale sono rumore: il diagramma le
# mostra gia'. Si tolgono dal corpo, non dal sorgente, che serve a disegnare.
SEZIONI_NEL_DISEGNO = ("classi", "associazioni", "generalizzazioni", "classi associative",
                       "specializzazioni di associazione", "use case", "use-case",
                       "attributi")

def togli_sezioni_del_disegno(md):
    """Toglie le sezioni che il diagramma gia' mostra. Il salto finisce solo a un'intestazione
    di livello pari o superiore a quella che l'ha aperto: altrimenti il primo `### Nome` di
    classe lo interrompeva, e l'elenco delle classi ricompariva sotto il disegno."""
    fuori, livello_salto = [], None
    for riga in md.splitlines(True):
        m = re.match(r"^(#{2,6})\s+(.+?)\s*$", riga)
        if m:
            livello = len(m.group(1))
            titolo = re.sub(r"[`*]", "", m.group(2)).strip().lower()
            if titolo in SEZIONI_NEL_DISEGNO and (livello_salto is None or livello <= livello_salto):
                livello_salto = livello
                continue
            if livello_salto is not None and livello <= livello_salto:
                livello_salto = None
        if livello_salto is None:
            fuori.append(riga)
    return "".join(fuori)

# Una formula lunga scritta come `codice` in mezzo al testo e' illeggibile: diventa un blocco.
INIZI_FOL = ("ALL ", "EXISTS ", "NOT ", "result ", "SUM ", "R = ", "S = ", "I = ", "P = ",
             "NC = ", "{ ")

def blocchi_fol(html_corpo):
    def sostituisci(m):
        testo = m.group(1)
        grezzo = html.unescape(testo)
        if len(grezzo) < 60 or not grezzo.lstrip().startswith(INIZI_FOL):
            return m.group(0)
        # a capo dopo i quantificatori e prima dei connettivi principali
        f = re.sub(r"\s+(and|or)\s+", r"\n    \1 ", grezzo)
        f = re.sub(r"\s*-->\s*", "\n  --> ", f)
        f = re.sub(r"\s*<-->\s*", "\n  <--> ", f)
        return "<pre class=fol>" + html.escape(f.strip()) + "</pre>"
    return re.sub(r"<code>(.+?)</code>", sostituisci, html_corpo, flags=re.S)

# Una soluzione d'esame contiene piu' di un diagramma: quello concettuale della Domanda 2, gli
# use-case della Domanda 3, il ristrutturato della Domanda 6. Ognuno va disegnato dove sta, non
# fusi in uno solo.
def blocchi_diagramma(md):
    """Trova i blocchi che descrivono un diagramma e l'intestazione a cui agganciarli.
    Ritorna una lista di (titolo_ancora, tipo, testo_del_blocco)."""
    righe = md.splitlines(True)
    inizi, ancora = [], None
    for i, riga in enumerate(righe):
        m = re.match(r"^(#{2,4})\s+(.+?)\s*$", riga)
        if not m:
            continue
        titolo = re.sub(r"[`*]", "", m.group(2)).strip()
        chiave = titolo.lower()
        if chiave == "classi":
            inizi.append((i, ancora, "classi"))
        elif chiave in ("use case", "use-case", "diagramma degli use-case"):
            inizi.append((i, ancora or titolo, "usecase"))
        elif chiave not in SEZIONI_NEL_DISEGNO:
            ancora = titolo
    blocchi = []
    for k, (i, anc, tipo) in enumerate(inizi):
        fine = len(righe)
        for j in range(i + 1, len(righe)):
            m = re.match(r"^(#{2,4})\s+(.+?)\s*$", righe[j])
            if m and len(m.group(1)) <= 2:
                titolo = re.sub(r"[`*]", "", m.group(2)).strip().lower()
                if titolo not in SEZIONI_NEL_DISEGNO:
                    fine = j
                    break
        blocchi.append((anc, tipo, "".join(righe[i:fine])))
    return blocchi

def _rendi(sorgente):
    r = subprocess.run(["java", "-jar", os.path.abspath(JAR), "-tsvg", "-pipe"],
                       input=sorgente.encode(), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    i = out.find("<svg")
    if i < 0:
        return None
    svg = out[i:]
    if "Syntax Error" in svg or "Error line" in svg:
        print("PlantUML non ha reso il diagramma:\n" +
              "\n".join(l for l in svg.splitlines() if "Error" in l)[:400], file=sys.stderr)
        return None
    return re.sub(r'<svg([^>]*?)\s(width|height)="[^"]*"', r"<svg\1", svg)

def svg_dei_blocchi(md):
    """Un SVG per blocco, nell'ordine in cui compaiono."""
    import tempfile
    out = []
    for ancora, tipo, testo in blocchi_diagramma(md):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(testo); tmp = f.name
        try:
            sorgente = puml(tmp, "") if tipo == "classi" else puml_usecase(tmp, "")
            if not sorgente or (tipo == "classi" and sorgente.count("class ") == 0):
                continue
            svg = _rendi(sorgente)
            if svg:
                out.append((ancora, svg))
        finally:
            os.unlink(tmp)
    return out

def svg_del_diagramma(md_path):
    """Rende il diagramma in SVG e lo restituisce inline, senza file d'appoggio."""
    sorgente = puml(md_path, "")
    if sorgente.count("class ") == 0:
        return None
    r = subprocess.run(["java", "-jar", os.path.abspath(JAR), "-tsvg", "-pipe"],
                       input=sorgente.encode(), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    i = out.find("<svg")
    if i < 0:
        return None
    svg = out[i:]
    # PlantUML in caso di errore produce comunque un SVG, con dentro il messaggio:
    # incorporarlo darebbe una pagina che sembra a posto ma mostra l'errore
    if "Syntax Error" in svg or "Error line" in svg:
        print("PlantUML non ha reso il diagramma:\n" +
              "\n".join(l for l in svg.splitlines() if "Error" in l)[:400], file=sys.stderr)
        return None
    # via le dimensioni fisse: cosi si adatta alla pagina
    return re.sub(r'<svg([^>]*?)\s(width|height)="[^"]*"', r"<svg\1", svg)

def componi(md_path, titolo=None):
    testo = open(md_path, encoding="utf-8").read()
    nome = titolo or re.sub(r"\.md$", "", os.path.basename(md_path))
    if nome.lower() in ("soluzione", "diagramma"):
        nome = os.path.basename(os.path.dirname(os.path.abspath(md_path)))

    # il titolo del documento diventa quello della pagina: non lo ripetiamo nel corpo
    m_tit = re.match(r"\s*#\s+(.+?)\s*\n", testo)
    if m_tit:
        nome = m_tit.group(1).strip()
        testo = testo[m_tit.end():]

    # i diagrammi si ricavano dal testo intero: le sezioni che li descrivono vengono tolte
    # subito dopo, e cercarli nel testo gia' ripulito non troverebbe piu' niente
    diagrammi = svg_dei_blocchi(testo)
    testo = togli_sezioni_del_disegno(testo)
    corpo = markdown.markdown(testo, extensions=["tables", "fenced_code", "sane_lists"])
    corpo = blocchi_fol(corpo)
    svg = diagrammi[0][1] if diagrammi else None
    if svg is None:
        corpo = ('<div class="diagramma" style="border-color:#b34;background:#fff5f5">'
                 '<b>Il diagramma non è stato disegnato.</b><br>'
                 'Il testo della soluzione c\'è tutto, ma la resa grafica è fallita: '
                 'controlla il formato delle sezioni <code>## Classi</code>, '
                 '<code>## Associazioni</code> e <code>## Generalizzazioni</code>.'
                 '</div>') + corpo
    for ancora, s in diagrammi:
        blocco = ('<div class="diagramma">' + s +
                  '<div class="nota">Diagramma generato dal testo della soluzione.</div></div>')
        m = re.search(r"(<h[2-4][^>]*>\s*" + re.escape(html.escape(ancora or "")) +
                      r"\s*</h[2-4]>)", corpo) if ancora else None
        if m:
            corpo = corpo.replace(m.group(1), m.group(1) + blocco, 1)
        else:
            corpo += blocco

    return (f"<!doctype html>\n<html lang=it><meta charset=utf-8>\n"
            f"<meta name=viewport content='width=device-width,initial-scale=1'>\n"
            f"<title>{html.escape(nome)} — BDD2</title>\n<style>{CSS}</style>\n"
            f"<h1>{html.escape(nome)}</h1>\n"
            f"<div class=sotto>Basi di Dati, Modulo 2 — soluzione completa</div>\n{corpo}\n</html>")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("-o", "--out", default=".")
    ap.add_argument("--titolo")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    nome = re.sub(r"\.md$", "", os.path.basename(a.file))
    if nome.lower() in ("soluzione", "diagramma"):
        nome = os.path.basename(os.path.dirname(os.path.abspath(a.file)))
    dest = os.path.join(a.out, nome + ".html")
    open(dest, "w", encoding="utf-8").write(componi(a.file, a.titolo))
    print(dest)

if __name__ == "__main__":
    main()
