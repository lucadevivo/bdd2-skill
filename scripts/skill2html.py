#!/usr/bin/env python3
"""Compone la skill bdd2 in un unico HTML leggibile, con indice e ancore.

Uso:  skill2html.py [-s cartella-skill] [-o file.html]

Serve a rileggere la skill per intero e segnalare errori indicando la sezione. Ogni titolo ha
un'ancora numerata (§2.3) che compare a lato: cliccandola si copia il link, e citarla basta a
individuare il punto.
"""
import argparse, html, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
sys.path.insert(0, os.path.join(QUI, "..", "tools", "pylib"))
import markdown
from componi import CSS

# ordine di lettura: prima il documento principale, poi i reference dal generale al particolare
ORDINE = [
    ("SKILL.md",                  "Il documento principale"),
    ("references/analisi.md",     "Analisi concettuale — Domande 1-5"),
    ("references/fol.md",         "La logica del primo ordine"),
    ("references/progettazione.md", "Progettazione — Domande 6-8"),
    ("references/sql.md",         "Esercitazioni SQL"),
    ("references/errori.md",      "Cosa i correttori considerano errore"),
    ("references/corpus.md",      "Dove trovare cosa"),
]

EXTRA = """
.indice { background:var(--codice); border:1px solid var(--bordo); border-radius:6px;
          padding:1rem 1.4rem; margin:2rem 0 3rem; font-family:system-ui,sans-serif;
          font-size:.9rem }
.indice ol { margin:.3rem 0; padding-left:1.4rem }
.indice > ol > li { margin:.5rem 0; font-weight:600 }
.indice ol ol li { font-weight:400 }
.indice a { color:inherit; text-decoration:none }
.indice a:hover { text-decoration:underline }
.file { margin:4rem 0 0; padding:.6rem 0 .2rem; border-top:3px solid var(--accento) }
.file .nomefile { font:.78rem/1 ui-monospace,monospace; color:var(--tenue);
                  letter-spacing:.02em }
.file h2 { border:none; margin:.2rem 0 0; font-size:1.5rem }
.sez { color:var(--tenue); font-weight:400; font-size:.75em; margin-right:.45em;
       font-family:ui-monospace,monospace }
.righe { float:right; font:.75rem system-ui,sans-serif; color:var(--tenue) }
.frontmatter { background:#fffbe9; border:1px solid #e8d9a0; border-radius:6px;
               padding:.8rem 1rem; margin:1.2rem 0; font:.83rem/1.5 system-ui,sans-serif }
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--skill", default=os.path.expanduser("~/.claude/skills/bdd2"))
    ap.add_argument("-o", "--out", default=os.path.join(QUI, "..", "skill-bdd2.html"))
    a = ap.parse_args()

    corpo, indice, tot = [], [], 0
    for n_file, (rel, titolo) in enumerate(ORDINE, 1):
        percorso = os.path.join(a.skill, rel)
        if not os.path.exists(percorso):
            continue
        testo = open(percorso, encoding="utf-8").read()
        righe = testo.count("\n") + 1
        tot += righe
        # il frontmatter YAML non e' prosa: va mostrato a parte, non come testo
        frontmatter = ""
        mfm = re.match(r"\A---\n(.*?)\n---\n", testo, re.S)
        if mfm:
            testo = testo[mfm.end():]
            desc = re.search(r"^description:\s*(.+)$", mfm.group(1), re.M)
            if desc:
                frontmatter = ('<div class="frontmatter"><b>description</b> — è il testo che '
                               'decide quando la skill si attiva<br>'
                               + html.escape(desc.group(1).strip()) + "</div>")
        # il titolo H1 del file diventa l'intestazione della sezione
        testo = re.sub(r"\A\s*#\s+.+?\n", "", testo)

        corpo.append(f'<div class="file" id="f{n_file}">'
                     f'<span class="righe">{righe} righe · {html.escape(rel)}</span>'
                     f'<div class="nomefile">§{n_file}</div>'
                     f'<h2>{html.escape(titolo)}</h2></div>')
        voci = []
        htm = markdown.markdown(testo, extensions=["tables", "fenced_code", "sane_lists"])

        # numera e ancora i titoli di secondo livello del file
        cont = [0]
        def ancora(m):
            cont[0] += 1
            sez = f"{n_file}.{cont[0]}"
            testo_t = re.sub(r"<[^>]+>", "", m.group(2))
            voci.append((sez, testo_t))
            return (f'<h{m.group(1)} id="s{sez}">'
                    f'<span class="sez">§{sez}</span>{m.group(2)}</h{m.group(1)}>')
        htm = re.sub(r"<h([12])[^>]*>(.*?)</h\1>", ancora, htm)
        corpo.append(frontmatter + htm)
        indice.append((n_file, titolo, rel, voci))

    toc = ['<div class="indice"><ol>']
    for n, titolo, rel, voci in indice:
        toc.append(f'<li><a href="#f{n}">{html.escape(titolo)}</a> '
                   f'<span class="nomefile">{html.escape(rel)}</span><ol>')
        for sez, t in voci:
            toc.append(f'<li><a href="#s{sez}">{html.escape(t)}</a></li>')
        toc.append("</ol></li>")
    toc.append("</ol></div>")

    pagina = (f"<!doctype html>\n<html lang=it><meta charset=utf-8>\n"
              f"<meta name=viewport content='width=device-width,initial-scale=1'>\n"
              f"<title>Skill bdd2 — testo completo</title>\n<style>{CSS}{EXTRA}</style>\n"
              f"<h1>Skill <code>bdd2</code></h1>\n"
              f"<div class=sotto>Testo completo, {len(indice)} file, {tot} righe. "
              f"Ogni sezione ha un numero §: citalo per segnalare un errore.</div>\n"
              + "\n".join(toc) + "\n" + "\n".join(corpo) + "\n</html>")
    dest = os.path.abspath(a.out)
    open(dest, "w", encoding="utf-8").write(pagina)
    print(dest)

if __name__ == "__main__":
    main()
