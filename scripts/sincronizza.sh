#!/usr/bin/env bash
# Rigenera skill/ e corpus/ di questo repository dalle sorgenti locali, ripulendoli.
#
#   ./scripts/sincronizza.sh
#
# Cosa fa, e perche':
#   - skill/   <- ~/.claude/skills/bdd2, con i percorsi assoluti riportati al segnaposto
#                 __BDD2_ROOT__ che install.sh sostituisce;
#   - corpus/  <- ~/Scrivania/BDD2-corpus-nuovo, senza benchmark/ (sono le prove degli agenti, cioe'
#                 le soluzioni degli esercizi: pubblicarle toglierebbe valore agli esercizi stessi),
#                 senza il jar di PlantUML (lo scarica uno script),
#                 senza gli svolgimenti manoscritti (restano le trascrizioni), senza gli .xml dei
#                 diagrammi (si rigenerano dai .json) e senza il passaggio di consegne interno;
#   - le figure delle slide perdono la fascia del pie' di pagina, che porta il nome del docente;
#   - gli script del corpus perdono i percorsi della macchina di chi lo ha costruito.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL="${SKILL_SRC:-$HOME/.claude/skills/bdd2}"
CORPUS="${CORPUS_SRC:-$HOME/Scrivania/BDD2-corpus-nuovo}"

[ -d "$SKILL" ]  || { echo "skill non trovata: $SKILL"; exit 1; }
[ -d "$CORPUS" ] || { echo "corpus non trovato: $CORPUS"; exit 1; }

rsync -a --delete --exclude '.git' --exclude '.gitnexus' --exclude '.claude' "$SKILL/" "$ROOT/skill/"

rsync -a --delete \
  --exclude 'tools/plantuml.jar' --exclude '__pycache__' --exclude '*.html' \
  --exclude 'STATO.md' --exclude '.impeccable' --exclude 'benchmark' \
  --exclude 'docente-ufficiale/progetti/QuickHospital-svolgimento-studente-E.pdf' \
  --exclude 'docente-ufficiale/progetti/QuickHospital-correzioni-tutor.jpg' \
  --exclude 'docente-ufficiale/svolgimenti/*.pdf' \
  "$CORPUS/" "$ROOT/corpus/"

mkdir -p "$ROOT/docs" && cp "$CORPUS"/*.html "$ROOT/docs/"
find "$ROOT/corpus" -name '*.xml' -delete
mogrify -gravity South -chop 0x5% "$ROOT"/corpus/teoria/figure/*/*.png

python3 - "$ROOT" <<'PY'
import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
casa = str(pathlib.Path.home())

def sost(rel, coppie):
    f = root / rel
    if not f.exists():
        return
    s = f.read_text(encoding="utf-8")
    for a, b in coppie:
        s = s.replace(a, b)
    f.write_text(s, encoding="utf-8")

radici = [(f"{casa}/Scrivania/BDD2-corpus-nuovo", "__BDD2_ROOT__/corpus"),
          ("~/Scrivania/BDD2-corpus-nuovo", "__BDD2_ROOT__/corpus")]
sost("skill/SKILL.md", radici)
sost("skill/references/corpus.md", radici)
sost("skill/references/sql.md", radici +
     [(f'NM="{casa}/Scrivania/nuovo materiale"', 'NM="__BDD2_ROOT__/corpus/database"')])

# gli script del corpus: il venv locale diventa un python qualsiasi con PyMuPDF
for p in (root / "corpus" / "scripts").glob("*.py"):
    s = p.read_text(encoding="utf-8")
    if casa in s:
        s = s.replace(f"{casa}/.local/venv-bdd2/bin/python", "python3")
        s = s.replace("serve PyMuPDF: usa python3", "serve PyMuPDF: pip install pymupdf")
        p.write_text(s, encoding="utf-8")

# i markdown del corpus che citano cartelle della macchina
f = root / "corpus" / "NOTAZIONE.md"
if f.exists():
    s = f.read_text(encoding="utf-8")
    s = re.sub(rf"- `{re.escape(casa)}/Scrivania/BDD2/`[^\n]*",
               "- **il materiale del corso**, scaricabile dalla pagina ufficiale:", s)
    f.write_text(s, encoding="utf-8")

restano = [str(p) for p in root.rglob("*")
           if p.is_file() and ".git/" not in str(p) and p.suffix in {".md", ".py", ".sh", ".sql"}
           and casa in p.read_text(encoding="utf-8", errors="ignore")]
print("percorsi locali rimasti:", len(restano))
for r in restano[:10]:
    print("  ", r)
PY

echo "fatto. Ora: python3 skill/test-regressione.py && git add -A && git commit --amend"
