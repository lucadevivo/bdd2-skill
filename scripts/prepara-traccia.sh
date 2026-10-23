#!/usr/bin/env bash
# Converte un PDF di traccia d'esame in immagini JPEG, una per pagina, da allegare
# al prompt. Serve perche' 39 tracce su 41 sono PDF di sole immagini, e perche' la
# barra verticale nel margine sinistro (che decide le Domande 5 e 8) e' un segno
# grafico che nessuna estrazione di testo conserva.
set -euo pipefail

PDF="${1:-}"
[ -n "$PDF" ] && [ -f "$PDF" ] || { echo "uso: ./prepara-traccia.sh <traccia.pdf> [cartella-uscita]"; exit 1; }

OUT="${2:-$(cd "$(dirname "$PDF")" && pwd)/$(basename "${PDF%.pdf}")-pagine}"
mkdir -p "$OUT"

command -v pdftoppm >/dev/null || { echo "serve pdftoppm: brew install poppler"; exit 1; }

# 150 dpi e lato lungo ~1600px: la barra resta visibile e la richiesta non diventa
# troppo pesante per il modello.
pdftoppm -jpeg -r 150 -scale-to 1600 "$PDF" "$OUT/pag"

echo "Pagine in: $OUT"
ls -1 "$OUT"
cat <<'EOF'

Allega TUTTE le pagine al primo messaggio, e comincia chiedendo:

  $bdd2 Queste sono le pagine della traccia. Prima di ogni altra cosa dimmi
  quali requisiti hanno la barra verticale nera nel margine sinistro, citando
  le frasi esatte. Poi fermati e aspetta la mia conferma.

La barra e' un rettangolo nero spesso NEL MARGINE, non un trattino dentro il
testo e non una sottolineatura a penna: quelle sono annotazioni di studenti.
EOF
