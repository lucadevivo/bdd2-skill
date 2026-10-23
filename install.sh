#!/usr/bin/env bash
# Installa la skill bdd2 per Codex, Claude Code o un altro agente, sostituendo il
# segnaposto __BDD2_ROOT__ con il percorso reale di questo repository.
#
#   ./install.sh            -> Codex      (~/.codex/skills/bdd2)
#   ./install.sh claude     -> Claude Code (~/.claude/skills/bdd2)
#   ./install.sh altro DEST -> una cartella qualsiasi
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-codex}"

case "$TARGET" in
  codex)  DEST="$HOME/.codex/skills/bdd2" ;;
  claude) DEST="$HOME/.claude/skills/bdd2" ;;
  altro)  DEST="${2:?indica la cartella di destinazione}" ;;
  *) echo "uso: ./install.sh [codex|claude|altro <cartella>]"; exit 1 ;;
esac

echo "Sorgente:     $ROOT/skill"
echo "Destinazione: $DEST"

if [ -e "$DEST" ]; then
  printf "%s esiste gia'. Sovrascrivo? [s/N] " "$DEST"
  read -r ans
  case "$ans" in s|S) rm -rf "$DEST" ;; *) echo "annullato"; exit 1 ;; esac
fi

mkdir -p "$DEST"
cp -R "$ROOT/skill/." "$DEST/"

# sostituzione del segnaposto, in una forma che funziona sia con GNU sed sia con
# il sed di macOS
find "$DEST" -name '*.md' -type f | while read -r f; do
  sed "s|__BDD2_ROOT__|$ROOT|g" "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done

echo
echo "Skill installata. Il corpus a cui punta e': $ROOT/corpus"
echo
echo "Dipendenze:"
have() { command -v "$1" >/dev/null 2>&1; }
have python3  && echo "  [ok]    python3"            || echo "  [manca] python3 — servono confronta_uml.py, componi.py, uml2png.py"
have java     && echo "  [ok]    java"               || echo "  [manca] java — senza, i diagrammi non vengono disegnati"
have docker   && echo "  [ok]    docker"             || echo "  [manca] docker — senza, l'SQL non si puo' eseguire prima di consegnarlo"
have pdftoppm && echo "  [ok]    pdftoppm (poppler)" || echo "  [manca] pdftoppm — serve per leggere la barra laterale delle tracce"

cat <<EOF

Prossimi passi
  1. PlantUML (una volta sola):   bash "$ROOT/scripts/scarica-plantuml.sh"
  2. database di prova:           bash "$ROOT/scripts/carica-database.sh"
  3. una traccia d'esame:         bash "$ROOT/scripts/prepara-traccia.sh" <traccia.pdf>

Leggi il README: la barra laterale delle tracce e' l'unico punto in cui il
risultato dipende da come passi la traccia al modello, e sbagliarla costa due
domande eliminatorie.
EOF
