#!/usr/bin/env python3
"""Raccoglie le soluzioni ufficiali del corso (file .txt sparsi in sottocartelle) in un
markdown per esercizio, con una sezione per artefatto.

    python3 raccogli-soluzioni.py <cartella-fonti/01-corso> <destinazione>

I .txt sono gia' testo: qui non si converte niente, si mette ordine. Ogni sezione dichiara
il file da cui viene, cosi' resta tracciabile.
"""
import re, sys
from pathlib import Path


# cartelle della fonte con il codice sbagliato: Universita 2 e' l'esercitazione E.A.1.6
CORREZIONI = {"E.A.1.3 - Universita 2": "E.A.1.6 - Università 2",
              "E.A.1.3 - Universita 1": "E.A.1.3 - Università 1"}


def pulisci(nome: str) -> tuple[str, str]:
    """Nome dell'esercizio e, se c'e', il passo di consegna: le soluzioni dei progetti sono
    spezzate in "Passo A.1", "Passo A.2"... ma appartengono allo stesso esercizio."""
    nome = re.sub(r'^Soluzione\s+', '', nome).strip(" ,")
    nome = re.sub(r'-\d{8}$', '', nome)            # "QuickHospital-20260605" -> "QuickHospital"
    passo = ""
    trovato = re.search(r'[, ]\s*(Passo\s+[A-Z0-9.]+(?:\s*\([^)]*\))?)\s*$', nome)
    if trovato:
        passo = trovato.group(1).strip()
        nome = nome[:trovato.start()].strip(" ,")
    return CORREZIONI.get(nome, nome), passo


def raccogli(radice: Path, dest: Path):
    gruppi, nomi_visti = {}, {}                     # nome esercizio -> [(passo, sottopercorso, file)]
    for txt in sorted(radice.rglob("*.txt")):
        relativo = txt.relative_to(radice)
        materia = relativo.parts[0]
        if len(relativo.parts) == 2:                # il .txt sta subito sotto la materia
            nome, passo = pulisci(materia.replace("_", " "))
            sotto = Path(relativo.parts[1])
        else:
            nome, passo = pulisci(relativo.parts[1])
            sotto = Path(*relativo.parts[2:])
        chiave = nome.casefold()               # "Travel to the Moon" e "Travel to the moon"
        nomi_visti.setdefault(chiave, nome)     # sono lo stesso esercizio
        gruppi.setdefault(chiave, []).append((passo, sotto, txt))

    dest.mkdir(parents=True, exist_ok=True)
    for chiave, voci in sorted(gruppi.items()):
        nome = nomi_visti[chiave]
        pezzi = [f"# {nome} — soluzione ufficiale\n"]
        for passo, sotto, txt in sorted(voci):
            titolo = sotto.stem.strip()
            dentro = " / ".join(sotto.parts[:-1])
            intestazione = " — ".join(x for x in (passo, dentro, titolo) if x)
            corpo = txt.read_text(encoding="utf-8", errors="replace").strip()
            pezzi.append(f"## {intestazione}\n\n> Fonte: `{txt.name}`\n\n```\n{corpo}\n```\n")
        (dest / f"{nome}.md").write_text("\n".join(pezzi), encoding="utf-8")
        print(f"{len(voci):>3} artefatti  {nome}.md")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    raccogli(Path(sys.argv[1]), Path(sys.argv[2]))
