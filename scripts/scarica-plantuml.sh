#!/usr/bin/env bash
# Scarica plantuml.jar in tools/. Serve a uml2png.py e componi.py per disegnare
# i diagrammi. Non e' nel repository perche' e' un binario di terze parti.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/tools"
VER="${1:-1.2025.4}"

mkdir -p "$DEST"
URL="https://github.com/plantuml/plantuml/releases/download/v${VER}/plantuml-${VER}.jar"

echo "scarico PlantUML $VER..."
curl -fL --progress-bar -o "$DEST/plantuml.jar" "$URL"

command -v java >/dev/null || { echo "attenzione: java non e' installato, il jar non e' utilizzabile"; exit 0; }
java -jar "$DEST/plantuml.jar" -version | head -2
echo "ok: $DEST/plantuml.jar"
echo "Il layout usato e' Smetana (interno a PlantUML): non serve installare graphviz."
