# Genera site/img/hero.jpg: IMMAGINE SEGNAPOSTO.
# Cartiglio di un disegno tecnico leggermente sfuocato, con righello e matita appoggiati.
# Va sostituita con la foto vera di un cartiglio di un progetto in corso:
# basta salvare la foto come site/img/hero.jpg (consigliato 1920x900, sotto i 300 KB).
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site", "img", "hero.jpg")
W, H = 1920, 900

SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


INK = (38, 52, 70)
PAPER = (236, 238, 232)

# --- carta + disegno + cartiglio (verrà sfuocato) -------------------------
paper = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(paper)

# cornice del foglio
d.rectangle([60, 50, W - 60, H - 50], outline=INK, width=4)
d.rectangle([80, 70, W - 80, H - 70], outline=INK, width=2)

# scambiatore a heat pipe in vista laterale: pacco alette + tubi
x0, y0 = 170, 150
for i in range(34):
    x = x0 + i * 22
    d.rectangle([x, y0, x + 6, y0 + 330], outline=INK, width=2)
for k in range(5):
    y = y0 + 40 + k * 62
    d.rectangle([x0 - 40, y, x0 + 34 * 22 + 40, y + 14], outline=INK, width=3)
d.line([x0 - 40, y0 + 380, x0 + 34 * 22 + 40, y0 + 380], fill=INK, width=2)
for xs in range(x0 - 40, x0 + 34 * 22 + 40, 40):
    d.line([xs, y0 + 372, xs, y0 + 388], fill=INK, width=2)
d.text((x0, y0 + 400), "A - A   SCALA 1:2", font=font(MONO, 26), fill=INK)

# linee di quota e assi
for yy in (y0 - 40, y0 + 330 + 60):
    d.line([x0 - 60, yy, x0 + 34 * 22 + 60, yy], fill=INK, width=1)
d.line([x0 + 17 * 22 + 3, y0 - 70, x0 + 17 * 22 + 3, y0 + 460], fill=INK, width=1)

# cartiglio in basso a destra
tx0, ty0, tx1, ty1 = W - 1000, 250, W - 110, 510
d.rectangle([tx0, ty0, tx1, ty1], outline=INK, width=4)
rows = [ty0 + 70, ty0 + 130, ty0 + 190]
for y in rows:
    d.line([tx0, y, tx1, y], fill=INK, width=2)
d.line([tx0 + 580, ty0, tx0 + 580, ty1], fill=INK, width=2)
d.line([tx0 + 740, ty0 + 130, tx0 + 740, ty1], fill=INK, width=2)

d.text((tx0 + 20, ty0 + 14), "BOSARI THERMAL MANAGEMENT", font=font(BOLD, 31), fill=INK)
d.text((tx0 + 600, ty0 + 10), "DISEGNO N.", font=font(SANS, 18), fill=INK)
d.text((tx0 + 600, ty0 + 30), "BTM-2025-0417", font=font(MONO, 30), fill=INK)
d.text((tx0 + 20, ty0 + 84), "SCAMBIATORE A HEAT PIPE", font=font(BOLD, 30), fill=INK)
d.text((tx0 + 600, ty0 + 84), "REV.  C", font=font(MONO, 30), fill=INK)
d.text((tx0 + 20, ty0 + 144), "ISOLAMENTO 12 kV  /  ALETTE AL", font=font(SANS, 26), fill=INK)
d.text((tx0 + 600, ty0 + 144), "FOGLIO 1 / 3", font=font(MONO, 26), fill=INK)
d.text((tx0 + 20, ty0 + 204), "DISEGNATO  G.B.", font=font(MONO, 22), fill=INK)
d.text((tx0 + 300, ty0 + 204), "CONTROLL.  M.R.", font=font(MONO, 22), fill=INK)
d.text((tx0 + 760, ty0 + 204), "QUOTE IN mm", font=font(MONO, 22), fill=INK)

# lieve grana della carta, poi sfocatura "da fotografia"
paper = paper.filter(ImageFilter.GaussianBlur(5))

# --- strumenti appoggiati (sfocati meno, in primo piano) ------------------
tools = Image.new("RGBA", (W, H), (0, 0, 0, 0))
t = ImageDraw.Draw(tools)

# righello lungo, in basso, con tacche
ry0, ry1 = 700, 790
t.polygon([(0, ry0 + 20), (W, ry0 - 20), (W, ry1 - 20), (0, ry1 + 20)], fill=(212, 178, 96, 255))
for i in range(0, W, 12):
    yy_top = ry0 + 20 - int(i * 40 / W)
    ln = 34 if i % 120 == 0 else (22 if i % 60 == 0 else 14)
    t.line([i, yy_top, i, yy_top + ln], fill=(70, 50, 20, 255), width=2)
    if i % 120 == 0:
        t.text((i + 4, yy_top + 38), str(i // 12), font=font(SANS, 18), fill=(70, 50, 20, 255))

# matita
t.polygon([(220, 560), (1000, 480), (1010, 510), (230, 590)], fill=(200, 30, 40, 255))
t.polygon([(1000, 480), (1090, 472), (1096, 495), (1010, 510)], fill=(230, 200, 150, 255))
t.polygon([(1075, 474), (1120, 470), (1096, 495)], fill=(40, 40, 40, 255))
t.polygon([(220, 560), (200, 562), (205, 592), (230, 590)], fill=(180, 180, 190, 255))

tools = tools.filter(ImageFilter.GaussianBlur(2.2))
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
shadow.paste((0, 0, 0, 110), mask=tools.split()[3])
shadow = shadow.filter(ImageFilter.GaussianBlur(14))

img = paper.convert("RGBA")
img.alpha_composite(shadow, (10, 16))
img.alpha_composite(tools)

# velo verde molto leggero per richiamare i colori del marchio
veil = Image.new("RGBA", (W, H), (0, 70, 40, 60))
img.alpha_composite(veil)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.convert("RGB").save(OUT, "JPEG", quality=82, optimize=True)
print("scritto", OUT, os.path.getsize(OUT) // 1024, "KB")
