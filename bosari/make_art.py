# Illustrazioni vettoriali dei prodotti (stile piatto, colori del marchio), generate in site/img/art-*.svg.
# Sono disegni illustrativi INVENTATI, non in scala, che sostituiscono le foto a bassa risoluzione
# nelle schede e nell'elenco prodotti. Le foto vere restano nella galleria della scheda.
import math
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "site", "img")

BG = "#eef3ef"
INK = "#17211c"
GREEN = "#008c45"
RED = "#cd212a"

DEFS = f"""<defs>
<radialGradient id="al" cx="38%" cy="32%" r="80%"><stop offset="0" stop-color="#f4f6f5"/><stop offset=".55" stop-color="#bcc5c0"/><stop offset="1" stop-color="#7f8a84"/></radialGradient>
<linearGradient id="alv" x1="0" x2="1"><stop offset="0" stop-color="#e9edeb"/><stop offset=".5" stop-color="#b9c2bd"/><stop offset="1" stop-color="#8a958f"/></linearGradient>
<linearGradient id="cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e0a46a"/><stop offset="1" stop-color="#a8642a"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="150%" height="150%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#0b1f15" flood-opacity=".25"/></filter>
</defs>"""


def wrap(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">'
            f'{DEFS}<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')


def hexnut(cx, cy, w, h, horizontal=False):
    """Raccordo esagonale visto di lato."""
    if horizontal:
        w, h = h, w
    return (f'<g><rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="3" fill="url(#alv)" stroke="#6b756f" stroke-width="1.5"/>'
            f'<rect x="{cx - w / 2 + 3}" y="{cy - h / 2 + 3}" width="{w - 6}" height="{h - 6}" rx="2" fill="none" stroke="#fff" stroke-opacity=".5"/></g>')


def disc(cx, cy, r, flow=True):
    out = [f'<g filter="url(#sh)">']
    out.append(hexnut(cx, cy - r - 8, r * 0.30, r * 0.34))
    out.append(hexnut(cx, cy + r + 8, r * 0.30, r * 0.34))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#al)" stroke="#5f6a64" stroke-width="2"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.86}" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="2"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.78}" fill="none" stroke="#5f6a64" stroke-opacity=".45" stroke-width="1.5"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.07}" fill="#4d5752"/>')
    out.append("</g>")
    if flow:   # frecce acqua: ingresso verde, uscita rossa
        out.append(f'<path d="M{cx} {cy - r - 38} v18" stroke="{GREEN}" stroke-width="5" stroke-linecap="round"/>'
                   f'<path d="M{cx - 7} {cy - r - 28} l7 10 l7 -10" fill="none" stroke="{GREEN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
        out.append(f'<path d="M{cx} {cy + r + 24} v18" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>'
                   f'<path d="M{cx - 7} {cy + r + 34} l7 10 l7 -10" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(out)


def art_bae6():
    return wrap(400, 300, disc(200, 150, 82), "ATLANTIS BAE6")


def art_bae9():
    return wrap(400, 300, disc(200, 150, 100), "ATLANTIS BAE9")


def fan(cx, cy, r):
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#2a312d" stroke="#0f1512" stroke-width="2"/>']
    for k in range(7):
        a = k * 2 * math.pi / 7
        x2, y2 = cx + math.cos(a) * r * 0.82, cy + math.sin(a) * r * 0.82
        xm, ym = cx + math.cos(a + .55) * r * 0.55, cy + math.sin(a + .55) * r * 0.55
        out.append(f'<path d="M{cx} {cy} Q{xm:.1f} {ym:.1f} {x2:.1f} {y2:.1f}" stroke="#4b564f" stroke-width="{r * 0.17:.1f}" fill="none" stroke-linecap="round"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.22}" fill="#8a958f"/>')
    for rr in (0.45, 0.7, 0.95):   # griglia di protezione
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * rr}" fill="none" stroke="#c8d0cb" stroke-width="1.6" stroke-opacity=".8"/>')
    out.append(f'<path d="M{cx - r} {cy} H{cx + r} M{cx} {cy - r} V{cy + r}" stroke="#c8d0cb" stroke-width="1.6" stroke-opacity=".8"/>')
    return "".join(out)


def art_columbus():
    w, h = 400, 300
    body = ['<g filter="url(#sh)">']
    body.append('<rect x="110" y="20" width="180" height="260" rx="8" fill="url(#alv)" stroke="#5f6a64" stroke-width="2"/>')
    body.append('<rect x="118" y="28" width="164" height="244" rx="5" fill="none" stroke="#fff" stroke-opacity=".5"/>')
    body.append(fan(160, 78, 34))
    body.append(fan(240, 78, 34))
    for k in range(9):   # feritoie
        y = 150 + k * 11
        body.append(f'<rect x="132" y="{y}" width="136" height="5" rx="2.5" fill="#5f6a64" fill-opacity=".55"/>')
    body.append(f'<rect x="118" y="254" width="164" height="6" fill="{GREEN}"/>')
    body.append("</g>")
    # flussi: aria dell'armadio (rosso) e aria ambiente (verde)
    body.append(f'<path d="M62 78 H100" stroke="{GREEN}" stroke-width="5" stroke-linecap="round"/><path d="M92 70 l10 8 l-10 8" fill="none" stroke="{GREEN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    body.append(f'<path d="M338 190 H300" stroke="{RED}" stroke-width="5" stroke-linecap="round"/><path d="M308 182 l-10 8 l10 8" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    return wrap(w, h, "".join(body), "COLUMBUS 1000")


def art_ucool():
    w, h = 400, 300
    b = ['<g filter="url(#sh)">']
    # alette: pacco in prospettiva obliqua dietro la piastra
    for i in range(29, -1, -1):
        x = 236 - i * 6.4
        y = 72 - i * 1.5
        b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="4" height="170" fill="#2b312e" stroke="#475049" stroke-width=".6"/>')
    # heat pipe in rame che escono dal pacco
    for k in range(3):
        yy = 62 + k * 20
        b.append(f'<rect x="30" y="{yy - 2.5}" width="64" height="6" rx="3" fill="url(#cu)"/>')
    # piastra di base e moduli IGBT
    b.append('<rect x="236" y="40" width="26" height="206" fill="url(#alv)" stroke="#5f6a64" stroke-width="2"/>')
    for yy in (56, 108, 160):
        b.append(f'<rect x="262" y="{yy}" width="34" height="42" rx="3" fill="#232a26" stroke="#0f1512" stroke-width="1.5"/>')
        b.append(f'<rect x="268" y="{yy + 7}" width="22" height="7" fill="#8a958f"/><rect x="268" y="{yy + 28}" width="22" height="7" fill="#8a958f"/>')
    b.append("</g>")
    return wrap(w, h, "".join(b), "U-COOL 1200/50")


FILES = {
    "art-atlantis-bae6.svg": art_bae6,
    "art-atlantis-bae9.svg": art_bae9,
    "art-columbus.svg": art_columbus,
    "art-ucool.svg": art_ucool,
}

if __name__ == "__main__":
    for name, fn in FILES.items():
        path = os.path.join(IMG, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(fn())
        print("scritto", path)
