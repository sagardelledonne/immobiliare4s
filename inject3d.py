# -*- coding: utf-8 -*-
# Inserisce (o aggiorna) la sezione 3D dentro src/page.html, prima della sezione LAVORI.
import os, re
ROOT = os.path.dirname(os.path.abspath(__file__)).replace(os.sep, "/")
page = ROOT + "/src/page.html"
part = ROOT + "/src/_scene3d.part.html"

s = open(page, encoding="utf-8").read()
blk = open(part, encoding="utf-8").read().strip()

start, end = "<!-- SCENE3D:START -->", "<!-- SCENE3D:END -->"
if start in s and end in s:
    i = s.index(start)
    j = s.index(end) + len(end)
    s = s[:i] + blk + s[j:]
    print("sezione 3D aggiornata")
else:
    anchor = "  <!-- LAVORI -->"
    if anchor not in s:
        raise SystemExit("ancora LAVORI non trovata")
    s = s.replace(anchor, blk + "\n\n" + anchor, 1)
    print("sezione 3D inserita")

open(page, "w", encoding="utf-8", newline="\n").write(s)
