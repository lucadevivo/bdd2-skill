#!/usr/bin/env python3
"""Verifica che diagrammi/{ufficiali,mie}/ siano ancora fedeli ai .vpp originali.

Rigenera in memoria da ogni .vpp e confronta con quanto sta su disco. Esce con
codice 1 al primo disallineamento, cosi' e' usabile come controllo automatico.

Uso:  python3 verifica_diagrammi.py [--aggiorna]
"""
import glob, os, sys, shutil

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import vpp2uml

BDD2 = "~/BDD2"
DIAG = os.path.join(QUI, "..", "diagrammi")

def chiave(v):
    return os.path.relpath(v, BDD2)[:-4].replace("/", "_")

def cartella(v):
    return os.path.join(DIAG, "mie" if "soluzione mia" in v else "ufficiali")

def png_ufficiale(v):
    d = os.path.dirname(v)
    cand = glob.glob(f"{d}/*.png") or glob.glob(f"{os.path.dirname(d)}/*.png")
    return next((p for p in cand if "Class" in os.path.basename(p)
                 or "classi" in os.path.basename(p)), None)

def main(aggiorna=False):
    guai = []
    for v in sorted(glob.glob(f"{BDD2}/**/*.vpp", recursive=True)):
        k, dest = chiave(v), cartella(v)
        for ext, testo in (("md", vpp2uml.markdown(v) + "\n"),
                           ("puml", vpp2uml.puml(v, k) + "\n")):
            f = f"{dest}/{k}.{ext}"
            vecchio = open(f).read() if os.path.exists(f) else None
            if vecchio != testo:
                guai.append(f"{k}.{ext} " + ("assente" if vecchio is None else "diverso dal .vpp"))
                if aggiorna:
                    open(f, "w").write(testo)
        off = png_ufficiale(v)
        f = f"{dest}/{k}.png"
        if off and (not os.path.exists(f)
                    or os.path.getsize(f) != os.path.getsize(off)):
            guai.append(f"{k}.png non e' l'export ufficiale")
            if aggiorna:
                shutil.copy2(off, f)
        elif not os.path.exists(f):
            guai.append(f"{k}.png assente (va reso con PlantUML)")
    for g in guai:
        print("  -", g)
    print(f"{len(guai)} disallineamenti" if guai else "tutti i diagrammi sono fedeli ai .vpp")
    return 1 if guai and not aggiorna else 0

if __name__ == "__main__":
    sys.exit(main("--aggiorna" in sys.argv))
