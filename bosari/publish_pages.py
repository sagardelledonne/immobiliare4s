# Pubblica l'anteprima su GitHub Pages: rigenera sito e PDF, poi copia site/ in ../docs/bosari/.
# GitHub Pages serve gia' la cartella docs/ del ramo main (sito Immobiliare 4S): questo aggiunge solo
# la sottocartella docs/bosari/, senza toccare il resto. Indirizzo: <pagina Pages del repo>/bosari/
# Uso:  python3 publish_pages.py   poi commit e merge su main.
import os
import shutil

import make_datasheets

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "site")
DST = os.path.join(os.path.dirname(ROOT), "docs", "bosari")

make_datasheets.main()                 # build.py + PDF
if os.path.isdir(DST):
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
open(os.path.join(DST, ".nojekyll"), "w").close()
print("copiato in", DST)
