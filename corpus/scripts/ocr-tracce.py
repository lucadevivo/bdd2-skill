#!/usr/bin/env python3
"""Riconoscimento del testo delle tracce d'esame scansionate.

    python3 ocr-tracce.py <cartella-tracce>
    python3 ocr-tracce.py <cartella-tracce> --prova

37 tracce su 40 sono PDF di sole immagini: senza OCR l'archivio d'esame non si puo'
cercare. Per ognuna si scrive `<nome>.ocr.md` accanto al PDF.

**Il documento buono resta il PDF.** L'OCR serve a *trovare* la traccia giusta, non a
studiarla: in questo corso una parola sbagliata cambia una molteplicita'. Per questo il
file prodotto ha estensione `.ocr.md`, diversa dai `.md` veri, e porta l'avvertenza in
testa.

`--prova` misura quanto sbaglia, invece di indovinare: rifa' l'OCR delle 3 tracce che un
livello di testo ce l'hanno davvero e confronta con quel testo. E' l'unico controllo
possibile che possa fallire.

I PDF sono **hardlink alle fonti**: si scrive solo in file nuovi, mai dentro i PDF.
Serve tesseract con la lingua italiana:  sudo pacman -S tesseract tesseract-data-ita
"""
import difflib, re, subprocess, sys, tempfile
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("serve PyMuPDF: pip install pymupdf")

PLAUSIBILE = 400  # sotto questa soglia una pagina di traccia non e' stata letta
DPI = 300  # sotto i 300 tesseract perde le lettere piccole delle scansioni storte

INTESTAZIONE = """\
# {nome} — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `{pdf}`.** Questo testo viene da un OCR
> (tesseract, italiano, {dpi} dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

"""


def tesseract(percorso: str) -> str:
    fatto = subprocess.run(
        ["tesseract", percorso, "stdout", "-l", "ita", "--psm", "3"],
        capture_output=True, text=True,
    )
    if fatto.returncode:
        sys.exit(f"tesseract: {fatto.stderr.strip().splitlines()[-1]}")
    return fatto.stdout.strip()


def ocr_immagine(pagina, clip=None) -> str:
    with tempfile.NamedTemporaryFile(suffix=".png") as png:
        pagina.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip).save(png.name)
        return tesseract(png.name)


def ocr_pagina(pagina) -> str:
    """Scaletta di ripieghi: su certe scansioni tesseract non restituisce *niente* dalla
    pagina intera e le stesse identiche righe se la pagina e' rientrata. Il perche' non
    l'ho trovato — non e' la risoluzione, ne' il dpi dichiarato, ne' i bordi scuri (il
    bordo esterno di quelle pagine e' bianco al 100%), ne' il rasterizzatore: fallisce
    anche con `pdftoppm`. Quindi non lo diagnostico, lo aggiro: si prova la pagina intera,
    poi la pagina rientrata del 10%, poi le immagini estratte dal PDF una per una.
    Non basta fermarsi alla prima resa non vuota: su DigiLab la pagina intera rende 57
    caratteri di spazzatura e il rientro 3672 di testo buono. Si prosegue finche' una resa
    non e' *plausibile* (una pagina di traccia sta sulle migliaia di caratteri) e in ogni
    caso si tiene la piu' lunga."""
    def immagini_estratte():
        doc = pagina.parent
        for riferimento in pagina.get_images(full=True):
            immagine = doc.extract_image(riferimento[0])
            with tempfile.NamedTemporaryFile(suffix="." + immagine["ext"]) as f:
                f.write(immagine["image"])
                f.flush()
                yield tesseract(f.name)

    r = pagina.rect
    rientro = pymupdf.Rect(r.width * .1, r.height * .1, r.width * .9, r.height * .9)
    rese = []
    for resa in (lambda: ocr_immagine(pagina),
                 lambda: ocr_immagine(pagina, rientro),
                 lambda: "\n".join(x for x in immagini_estratte() if x)):
        rese.append(resa())
        if len(rese[-1]) >= PLAUSIBILE:
            break
    return max(rese, key=len)


def ocr_documento(doc) -> str:
    pagine = [ocr_pagina(p) for p in doc]
    return "\n\n".join(f"## Pagina {i}\n\n{t}" for i, t in enumerate(pagine, 1) if t)


def normalizza(t: str) -> str:
    """Per il confronto conta il testo, non come e' andato a capo."""
    return re.sub(r"\s+", " ", t).strip().lower()


def prova(cartella: Path):
    """Confronta l'OCR con il testo vero, sulle sole tracce che ce l'hanno."""
    for pdf in sorted(cartella.glob("*.pdf")):
        doc = pymupdf.open(pdf)
        vero = "\n".join(p.get_text() for p in doc)
        if not vero.strip():
            continue
        somiglianza = difflib.SequenceMatcher(
            None, normalizza(vero), normalizza(ocr_documento(doc))
        ).ratio()
        print(f"{somiglianza*100:5.1f}% di somiglianza col testo vero  {pdf.name}")


def main(cartella: Path):
    fatti = 0
    for pdf in sorted(cartella.glob("*.pdf")):
        doc = pymupdf.open(pdf)
        if any(p.get_text().strip() for p in doc):
            continue  # ha gia' il testo vero: l'OCR sarebbe un peggioramento
        testo = ocr_documento(doc)
        (cartella / f"{pdf.stem}.ocr.md").write_text(
            INTESTAZIONE.format(nome=pdf.stem, pdf=pdf.name, dpi=DPI) + testo + "\n",
            encoding="utf-8",
        )
        fatti += 1
        print(f"{len(testo):6d} caratteri  {pdf.stem}.ocr.md", flush=True)
    print(f"\n{fatti} tracce riconosciute")


if __name__ == "__main__":
    cartella = Path(sys.argv[1])
    prova(cartella) if "--prova" in sys.argv else main(cartella)
