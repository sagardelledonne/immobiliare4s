# Genera site/img/ucool-it.svg e ucool-en.svg: schema ILLUSTRATIVO (inventato) del U-COOL 1200/50,
# vista laterale con piastra di base, moduli IGBT, 6 heat pipe a U e alette. Da sostituire con la foto vera.
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
LABELS = {
    "it": ("Moduli IGBT", "Piastra di base", "6 heat pipe in rame", "29 coppie di alette in alluminio", "Aletta di chiusura (3 mm)", "Schema illustrativo, non in scala"),
    "en": ("IGBT modules", "Base plate", "6 copper heat pipes", "29 couples of aluminium fins", "Closing fin (3 mm)", "Illustrative sketch, not to scale"),
}

def svg(lang):
    igbt, plate, pipes, fins, close, note = LABELS[lang]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" role="img" aria-label="U-COOL 1200/50">',
             '<rect width="640" height="380" fill="#f4f6f4"/>']
    # alette (29)
    x = 110
    for i in range(29):
        parts.append(f'<rect x="{x:.1f}" y="70" width="3" height="200" fill="#2b312e"/>')
        x += 14.2
    # heat pipe (6) che attraversano le alette
    for k in range(6):
        y = 92 + k * 32
        parts.append(f'<rect x="78" y="{y}" width="448" height="9" rx="4" fill="#b87333" stroke="#7a4a1c" stroke-width="1"/>')
    # aletta di chiusura
    parts.append('<rect x="520" y="62" width="10" height="216" fill="#59615d"/>')
    # piastra di base e moduli IGBT
    parts.append('<rect x="58" y="62" width="26" height="216" fill="#aeb7b2" stroke="#6b756f" stroke-width="1.5"/>')
    for yy in (84, 176):
        parts.append(f'<rect x="22" y="{yy}" width="38" height="70" fill="#2f3a35"/>')
        parts.append(f'<rect x="28" y="{yy+8}" width="26" height="8" fill="#8a948e"/><rect x="28" y="{yy+54}" width="26" height="8" fill="#8a948e"/>')
    # didascalie
    def label(x, y, tx, ty, text, anchor="start"):
        # ty = punto dove finisce la linea; il testo sta oltre la linea, mai sopra
        base = ty - 6 if ty < y else ty + 15
        return (f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="#17211c" stroke-width="1"/>'
                f'<text x="{tx}" y="{base}" font-family="Arial,sans-serif" font-size="15" fill="#17211c" text-anchor="{anchor}">{text}</text>')
    parts.append(label(41, 84, 41, 40, igbt))
    parts.append(label(71, 278, 71, 298, plate))
    parts.append(label(300, 92, 300, 40, pipes, "middle"))
    parts.append(label(360, 270, 360, 298, fins, "middle"))
    parts.append(label(525, 278, 600, 322, close, "end"))
    parts.append(f'<text x="320" y="368" font-family="Arial,sans-serif" font-size="12" fill="#55625b" text-anchor="middle">{note}</text>')
    parts.append('</svg>')
    return "\n".join(parts)

for lang in LABELS:
    p = os.path.join(ROOT, "site", "img", f"ucool-{lang}.svg")
    open(p, "w", encoding="utf-8").write(svg(lang))
    print("scritto", p)
