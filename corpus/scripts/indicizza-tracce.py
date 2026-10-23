#!/usr/bin/env python3
"""Le tracce d'esame sono PDF di sole immagini: qui si genera l'indice per sfogliarle.

    python3 indicizza-tracce.py <cartella-tracce>

Scrive `INDICE.md` nella cartella. Per ogni traccia: data, sistema, pagine, geometria e se
esiste un livello di testo (3 su 40; per quelle c'e' anche il markdown).

La geometria e' solo la misura della pagina PDF: 595x842 punti e' un A4 intero, qualunque
altra misura e' un ritaglio o una striscia. Non dice niente sulla qualita' della
scansione: una foto storta puo' stare dentro una pagina A4. Quello sta nelle note.

**Niente colonna per la barra verticale** che nel testo d'esame delimita la porzione di
requisiti a cui si riferiscono le Domande 5 e 8. Provato a rilevarla dai pixel (colonna
scura nel margine sinistro, con e senza vincoli su spessore e altezza): sulle scansioni
pulite funziona, sulle foto no. Il fondo scuro attorno al foglio e' anch'esso una colonna
scura e si fonde con la barra, e nei ritagli in formato striscia la barra occupa mezza
altezza. Ogni soglia che toglieva i falsi positivi (SafeOnTheBeach 2020, FaiDaNoi)
toglieva anche barre vere (WizardAir, My Precious). La barra si guarda a occhio aprendo
il PDF, che e' comunque il modo in cui queste tracce vanno lette.
"""
import re, sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("serve PyMuPDF: pip install pymupdf")

NOME = re.compile(r"BD2_(\d{4})-(\d{2})-(\d{2})_(.+)")
A4 = (595, 842)  # punti PDF, con la tolleranza di sotto

# guardate a occhio, una per una: non si deducono dal file
NOTE = {
    "BD2_2020-09-04_SafeOnTheBeach": "foto di uno schermo (esame da remoto), su 4 pagine",
    "BD2_2023-09-11_CozyRooms": "copia annotata a penna da uno studente",
    "BD2_2025-02-07_Vendify": "foto del foglio, dominante gialla; sottolineature a matita",
    "BD2_2025-07-17_IttiesseWeb": "CamScanner, evidenziature arancioni; **senza barra verticale**",
    "BD2_2025-03-28_WizardAir": "foto su fondo scuro; traccia di una sola pagina",
    "BD2_2026-02-03_DigiLab": "traccia di una sola pagina",
}


def testo_disponibile(pdf: Path, caratteri: int) -> str:
    if caratteri:
        return f"[`.md`]({pdf.stem}.md)"
    if (pdf.parent / f"{pdf.stem}.ocr.md").exists():
        return f"[`.ocr.md`]({pdf.stem}.ocr.md)"
    return "—"


def geometria(doc) -> str:
    for pag in doc:
        r = pag.rect
        if abs(r.width - A4[0]) > 15 or abs(r.height - A4[1]) > 15:
            return "ritaglio"
    return "A4"


INTRO = """\
Le tracce **si leggono come immagini**, aprendo il PDF a pagine: sono scansioni, e
l'estrazione del testo restituisce il vuoto tranne in tre casi.

Nella colonna «testo», `.md` e' il testo vero del PDF, `.ocr.md` e' quello riconosciuto da
tesseract su una scansione: **serve a cercare, non a studiare**, perche' contiene errori.
Trovata la traccia, si apre il PDF.

Ogni traccia porta le stesse 8 domande d'esame; quello che cambia e' il dominio. Nel
testo, una **barra verticale nera nel margine sinistro** delimita la porzione di requisiti
a cui si riferiscono le Domande 5 e 8: va cercata a occhio, non e' rilevabile in modo
affidabile dai pixel (vedi `scripts/indicizza-tracce.py`).

«Pagina» e' solo la misura del foglio PDF — A4 intero o ritaglio — non la qualita' della
scansione: quella, dove l'ho guardata, sta nelle note.
"""


def main(cartella: Path):
    righe = []
    for pdf in sorted(cartella.glob("*.pdf")):
        doc = pymupdf.open(pdf)
        anno, mese, giorno, sistema = NOME.match(pdf.stem).groups()
        testo = sum(len(p.get_text().strip()) for p in doc)
        righe.append(
            "| {}-{}-{} | [{}]({}) | {} | {} | {} | {} |".format(
                giorno, mese, anno,
                sistema, pdf.name,
                len(doc),
                geometria(doc),
                testo_disponibile(pdf, testo),
                NOTE.get(pdf.stem, ""),
            )
        )

    (cartella / "INDICE.md").write_text(
        f"# Tracce d'esame — {len(righe)} prove, dal 2016 al 2026\n\n"
        f"{INTRO}\n"
        "| Data | Sistema | Pag. | Pagina | Testo | Note |\n"
        "|---|---|---|---|---|---|\n" + "\n".join(righe) + "\n",
        encoding="utf-8",
    )
    print(f"{len(righe)} tracce nell'indice")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
