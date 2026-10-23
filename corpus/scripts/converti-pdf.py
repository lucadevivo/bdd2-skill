#!/usr/bin/env python3
"""PDF con livello di testo -> markdown greppabile.

    python3 converti-pdf.py <destinazione> <file.pdf> [altri.pdf ...]

Usa PyMuPDF. Le alternative di poppler perdono qualcosa: `pdftotext` mangia le
legature ("speci che" al posto di "specifiche"), `pdftohtml -xml` le conserva ma butta
via le formule composte con i font matematici. PyMuPDF tiene entrambe, e da' le
coordinate con cui si ricostruisce il rientro.

Richiede l'ambiente in ~/.local/venv-bdd2:
    python3 converti-pdf.py ...

Toglie le intestazioni e i pie' di pagina che si ripetono su ogni pagina, e i frammenti
dei diagrammi che le slide ridisegnano decine di volte. Rifiuta i PDF di sole immagini
invece di produrre un file vuoto.
"""
import re, sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("serve PyMuPDF: pip install pymupdf")

RUMORE = re.compile(
    r'^\s*(Sapienza Università|Facoltà di Ing\.|Laurea in Informatica|'
    r'Prof\.\s*Toni Mancini|Dipartimento di Informatica|http://tmancini|'
    r'Basi di Dati, Modulo 2|Versione \d{4}-|–\s*\d+\s*–|'
    r'S\.[AB]\.[\d.]*\s*$|\d+\s*$)', re.I)

# filigrana personale stampata dentro gli sbarramenti: porta il nome dello studente a cui
# la copia era stata concessa, sparso fra le righe del testo. Va via sempre, sia perche' e'
# rumore sia perche' e' il nome di una persona.
FILIGRANA = re.compile(
    r'Questo materiale|esclusivamente per uso personale|vietata la sua di.+usione', re.I)

# Nella filigrana il nome sta su una riga per conto suo, fra le due frasi. Si riconosce
# dalla forma (due o tre parole capitalizzate, nient'altro) e si toglie *solo* nei
# documenti che la filigrana ce l'hanno: cosi' il nome non finisce scritto qui dentro.
NOME_IN_FILIGRANA = re.compile(r'^\s*[A-Z][a-zà-ù\']+(?: [A-Z][a-zà-ù\']+){1,2}\s*$')

# sintassi che compare solo dentro un diagramma UML, mai in una frase della slide
ETICHETTA_DI_DIAGRAMMA = re.compile(
    r'\{\s*(id|disjoint|complete)|\b\d\.\.(\*|\d)|[A-Za-z_][\w ]* : [A-Z]')


def codice(titolo: str) -> str:
    """"A.4 - Logica del primo ordine (FOL)..." -> "A.4". Il codice della slide e' univoco,
    corto e senza parentesi: nei nomi delle figure evita richiami markdown rotti, perche'
    `](...)` si chiude alla prima parentesi tonda."""
    primo = titolo.split(" - ")[0].strip()
    pulito = re.sub(r'[^\w.]+', '', primo)
    return pulito if 1 <= len(pulito) <= 12 else re.sub(r'[^\w.-]+', '-', titolo)[:40]


def nome_pulito(pdf: Path) -> str:
    """"Slide A.3 - Logica del primo ordine (FOL) - BD2.pdf" -> "A.3 - Logica del primo ordine (FOL)"."""
    n = re.sub(r'^\s*(Slide|Documento|Esercitazione)\s+', '', pdf.stem)
    n = re.sub(r'^\s*\((\d+)\)\s*-?\s*(Progetto\s+)?', r'\1 - ', n)   # "(05) Progetto Out!" -> "05 - Out!"
    return re.sub(r'\s*-\s*BD2\s*$', '', n).strip()


def figure_della_pagina(pagina):
    """Le figure delle slide sono di tre tipi: disegni vettoriali (diagrammi delle classi),
    immagini incorporate (gli omini degli use-case, gli schermi, gli schemi relazionali) e
    misti. Si trovano tutte allo stesso modo: si raggruppano gli elementi grafici vicini fra
    loro, e ogni grappolo abbastanza grande e' una figura.

    Cercare la sintassi delle classi non basterebbe: un diagramma degli use-case non ha
    ne' molteplicita' ne' tipi, quindi non verrebbe mai riconosciuto."""
    pag = pagina.rect
    area_pagina = pag.get_area() or 1

    elementi = [pymupdf.Rect(d["rect"]) for d in pagina.get_drawings()]
    elementi += [pymupdf.Rect(i["bbox"]) for i in pagina.get_image_info()]
    # via il fondo pagina, le cornici a tutta pagina, le righe di intestazione e di piede
    elementi = [r for r in elementi
                if 50 < r.get_area() < 0.7 * area_pagina
                and r.y0 > pag.height * 0.06 and r.y1 < pag.height * 0.94]

    grappoli = []                      # [(riquadro, quanti elementi)]
    for r in elementi:
        box, quanti, altri = pymupdf.Rect(r), 1, []
        for g, n in grappoli:
            if (g + (-45, -35, 45, 35)).intersects(box):
                box |= g; quanti += n
            else:
                altri.append((g, n))
        grappoli = altri + [(box, quanti)]

    figure = []
    for box, quanti in grappoli:
        abbastanza = quanti >= 4 or (quanti >= 2 and box.get_area() > 0.05 * area_pagina)
        if not abbastanza or box.get_area() < 0.02 * area_pagina:
            continue
        # allarga per prendere le etichette: nomi delle classi, degli attori, degli use-case
        for _ in range(2):
            for riquadro, _testo in righe_con_riquadro(pagina):
                if pymupdf.Rect(riquadro).intersects(box):
                    box |= pymupdf.Rect(riquadro)
        figure.append((box + (-10, -8, 10, 8)) & pag)

    # due grappoli vicini sono quasi sempre pezzi della stessa figura: si fondono
    fuse = []
    for f in figure:
        unito = pymupdf.Rect(f)
        resto = []
        for g in fuse:
            if (g + (-60, -45, 60, 45)).intersects(unito):
                unito |= g
            else:
                resto.append(g)
        fuse = resto + [unito]
    figure = fuse

    # rete di sicurezza: un diagramma disegnato con pochi tratti puo' sfuggire al
    # raggruppamento, ma le sue etichette (0..*, {id}, nome : Tipo) lo tradiscono
    etichette = [pymupdf.Rect(b) for b, s in righe_con_riquadro(pagina)
                 if ETICHETTA_DI_DIAGRAMMA.search(s)]
    if len(etichette) >= 3 and not any(f.intersects(etichette[0]) for f in figure):
        box = etichette[0]
        for r in etichette[1:]:
            box |= r
        box += (-30, -25, 30, 25)
        for _ in range(2):
            for riquadro, _testo in righe_con_riquadro(pagina):
                if pymupdf.Rect(riquadro).intersects(box):
                    box |= pymupdf.Rect(riquadro)
        figure.append(box & pag)

    return [f for f in figure if f.width > 40 and f.height > 25]


def firma_grafica(pagina):
    """Cosa c'e' di disegnato sulla pagina, in forma confrontabile. Serve a riconoscere le
    slide a costruzione progressiva: ridisegnano la stessa figura aggiungendo una riga di
    testo per volta, e la firma resta identica."""
    figure = figure_della_pagina(pagina)
    if not figure:
        return None
    elementi = [pymupdf.Rect(d["rect"]) for d in pagina.get_drawings()]
    elementi += [pymupdf.Rect(i["bbox"]) for i in pagina.get_image_info()]
    return tuple(sorted((round(r.x0), round(r.y0), round(r.x1), round(r.y1))
                        for r in elementi if r.get_area() > 50))


def pagine_da_rendere(documento):
    """Le pagine che contengono una figura, senza le ripetizioni: di ogni sequenza di slide
    con la stessa figura si tiene l'ultima, che e' quella completa."""
    da_rendere, precedente, ultima = [], None, None
    for pagina in documento:
        firma = firma_grafica(pagina)
        if firma is None:
            if ultima is not None:
                da_rendere.append(ultima)
            precedente, ultima = None, None
            continue
        if firma == precedente:
            ultima = pagina.number            # stessa figura: scorre in avanti
        else:
            if ultima is not None:
                da_rendere.append(ultima)
            precedente, ultima = firma, pagina.number
    if ultima is not None:
        da_rendere.append(ultima)
    return set(da_rendere)


def rendi_pagina(pagina, cartella_figure: Path, nome_base: str):
    """La pagina intera come PNG. Ritagliare la sola figura non e' affidabile: sulle slide
    non c'e' un confine certo, e i tentativi tagliavano i riquadri o isolavano una classe
    sola. La pagina intera e' sempre completa e conserva il contesto."""
    cartella_figure.mkdir(parents=True, exist_ok=True)
    nome = f"{nome_base}-pag-{pagina.number + 1:03d}.png"
    pagina.get_pixmap(matrix=pymupdf.Matrix(1, 1)).save(cartella_figure / nome)
    return nome


def righe_con_riquadro(pagina):
    """Ogni riga di testo della pagina con il suo rettangolo."""
    for blocco in pagina.get_text("dict")["blocks"]:
        for riga in blocco.get("lines", []):
            testo = "".join(s["text"] for s in riga["spans"]).strip()
            if testo:
                yield riga["bbox"], testo


def righe_dal_pdf(pdf: Path, cartella_figure: Path = None, nome_base: str = ""):
    """Blocchi di testo con le loro coordinate -> righe con il rientro della colonna.
    Dove la pagina contiene un diagramma, inserisce il richiamo alla figura ritagliata."""
    documento = pymupdf.open(pdf)
    righe, figure = [], []
    da_rendere = pagine_da_rendere(documento) if cartella_figure is not None else set()
    for pagina in documento:
        larghezza = pagina.rect.width or 1
        blocchi = [b for b in pagina.get_text("blocks") if b[6] == 0]
        blocchi.sort(key=lambda b: (round(b[1]), b[0]))
        for x0, _y0, _x1, _y1, testo, _n, _tipo in blocchi:
            rientro = " " * int(100 * x0 / larghezza)          # in centesimi di pagina
            for riga in testo.splitlines():
                righe.append(rientro + riga.strip() if riga.strip() else "")
        if pagina.number in da_rendere:
            nome = rendi_pagina(pagina, cartella_figure, nome_base)
            righe.append("")
            righe.append(f"![slide con figura, pag. {pagina.number + 1}](figure/{nome_base}/{nome})")
            figure.append(nome)
        righe.append("")
    return righe, figure


def togli_frammenti_di_diagramma(righe, soglia=5, rientro_minimo=20):
    """Le slide ridisegnano lo stesso diagramma su decine di pagine. I suoi frammenti si
    riconoscono cosi': la riga ricompare molte volte, e' rientrata come una figura e ha la
    sintassi di un diagramma. Le intestazioni di sezione si ripetono anche loro, ma partono
    da sinistra e non hanno quella sintassi, quindi restano."""
    chiave = lambda r: re.sub(r'\s+', ' ', r.strip())
    conta = {}
    for r in righe:
        k = chiave(r)
        if k:
            conta[k] = conta.get(k, 0) + 1

    tenute, scartate = [], []
    for r in righe:
        k = chiave(r)
        rientro = len(r) - len(r.lstrip())
        if ("Powered By Visual Paradigm" in r or
                (k and conta.get(k, 0) >= soglia and rientro >= rientro_minimo
                 and ETICHETTA_DI_DIAGRAMMA.search(k))):
            scartate.append(r)
        else:
            tenute.append(r)
    return tenute, scartate


def converti(pdf: Path, dest: Path):
    titolo = nome_pulito(pdf)
    try:
        righe, figure = righe_dal_pdf(pdf, dest / "figure" / codice(titolo), codice(titolo))
    except Exception as e:
        return f"errore: {e}", 0, 0, 0

    if sum(len(r.split()) for r in righe) < 50:
        return "PDF di sole immagini: non convertito", 0, 0, 0

    filigranato = any(FILIGRANA.search(r) for r in righe)
    righe = [r for r in righe if not RUMORE.match(r) and not FILIGRANA.search(r)
             and not (filigranato and NOME_IN_FILIGRANA.match(r))]
    righe, scartate = togli_frammenti_di_diagramma(righe)

    out, vuote = [], 0
    for r in righe:
        if r.strip():
            out.append(r); vuote = 0
        else:
            vuote += 1
            if vuote == 1:
                out.append("")

    testo = (f"# {titolo}\n\n"
             f"> Fonte: `{pdf.name}`\n"
             f"> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di "
             f"intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono "
             f"ritagliati in `figure/` e richiamati nel punto in cui compaiono.\n\n---\n\n"
             + "\n".join(out).strip() + "\n")

    destinazione = dest / f"{titolo}.md"
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(testo, encoding="utf-8")
    return destinazione.name, len(out), len(scartate), len(set(figure))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    dest = Path(sys.argv[1])
    for pdf in sys.argv[2:]:
        nome, righe, scartate, figure = converti(Path(pdf), dest)
        print(f"{righe:>6} righe  ({scartate:>4} etichette tolte, {figure:>3} diagrammi ritagliati)  {nome}")
