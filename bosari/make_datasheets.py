# Genera i PDF in site/download/: una scheda tecnica per prodotto (IT/EN) + catalogo completo (IT/EN).
# Usa gli stessi dati del sito (products.py) e Chromium per la stampa in PDF.
# Uso:  python3 make_datasheets.py     (poi rigenera il sito: lo fa da solo alla fine)
import os
import subprocess
import tempfile

import build as B
import config as C
import products as P

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
OUT = os.path.join(SITE, "download")
CHROME = next((p for p in ("/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "/opt/pw-browsers/chromium",
                           "chromium", "google-chrome", "chromium-browser") if os.path.exists(p) or "/" not in p), None)

CSS = """
@page { size: A4; margin: 11mm 14mm 12mm 14mm; }
* { box-sizing: border-box; }
body { font: 10pt/1.45 "Liberation Sans", Arial, sans-serif; color: #17211c; margin: 0; }
.tri { display: flex; height: 5px; margin-bottom: 5mm; } .tri i { flex: 1; } .tri i:nth-child(1){background:#008c45} .tri i:nth-child(2){background:#fff;border-top:1px solid #d6ddd8} .tri i:nth-child(3){background:#cd212a}
.top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4mm; }
.brand { display: flex; align-items: center; gap: 8px; } .brand svg { width: 34px; height: 34px; color: #17211c; }
.brand b { font-size: 16pt; letter-spacing: .14em; display: block; line-height: 1.1; } .brand span { font-size: 7.5pt; letter-spacing: .12em; text-transform: uppercase; color: #55625b; }
.kind { font-size: 8.5pt; letter-spacing: .12em; text-transform: uppercase; color: #cd212a; font-weight: 700; }
h1 { font-size: 20pt; margin: 0 0 2px; } .sub { font-size: 10.5pt; color: #55625b; margin: 0 0 4mm; }
.cols { display: grid; grid-template-columns: 1fr 1.15fr; gap: 8mm; align-items: start; }
.art { background: #eef3ef; border: 1px solid #d6ddd8; padding: 4mm; text-align: center; margin-bottom: 4mm; } .art img { width: 100%; max-height: 40mm; object-fit: contain; }
ul.k { list-style: none; padding: 0; margin: 0 0 4mm; } ul.k li { padding-left: 16px; position: relative; margin-bottom: 3px; font-weight: 600; }
ul.k li::before { content: ""; position: absolute; left: 0; top: .55em; width: 10px; height: 3px; background: #008c45; }
table { width: 100%; border-collapse: collapse; margin: 0 0 3mm; font-size: 8.6pt; break-inside: avoid; }
caption { text-align: left; background: #008c45; color: #fff; padding: 4px 8px; font-size: 8pt; letter-spacing: .08em; text-transform: uppercase; font-weight: 700; }
th, td { padding: 2px 8px; border: 1px solid #d6ddd8; text-align: left; vertical-align: top; } th { font-weight: 400; color: #55625b; width: 52%; } td { font-weight: 700; }
.fn { font-size: 7.5pt; color: #55625b; margin: -2mm 0 4mm; }
h2 { font-size: 11pt; margin: 3mm 0 2mm; border-bottom: 2px solid #008c45; padding-bottom: 1mm; }
.desc { columns: 2; column-gap: 8mm; font-size: 8.5pt; line-height: 1.38; } .desc p { margin: 0 0 2mm; } .desc h3 { font-size: 9.5pt; margin: 3mm 0 1mm; break-after: avoid; } .desc ol { margin: 0 0 2mm; padding-left: 16px; } .desc li { margin-bottom: 1.5mm; }
.foot { margin-top: 4mm; padding-top: 2mm; border-top: 1px solid #d6ddd8; font-size: 8pt; color: #55625b; display: flex; justify-content: space-between; gap: 8mm; }
.draft { margin-top: 3mm; font-size: 7.5pt; color: #a3151d; font-weight: 700; }
.sheet { break-after: page; } .sheet:last-child { break-after: auto; }
.cover { height: 245mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.cover h1 { font-size: 34pt; } .cover p { font-size: 13pt; color: #55625b; max-width: 120mm; }
.cover ul { font-size: 12pt; line-height: 1.9; }
"""

LABELS = {
    "it": {"kind": "Scheda tecnica", "desc": "Descrizione", "web": "Dati soggetti a modifica senza preavviso.",
           "draft": "BOZZA – dati di contatto segnaposto.", "cat": "Catalogo prodotti", "cat_sub": "Raffreddatori ad acqua, scambiatori di calore e sistemi a heat pipe per l'elettronica di potenza.",
           "index": "Prodotti in questo catalogo"},
    "en": {"kind": "Data sheet", "desc": "Description", "web": "Data subject to change without notice.",
           "draft": "DRAFT – placeholder contact details.", "cat": "Product catalogue", "cat_sub": "Water coolers, heat exchangers and heat pipe systems for power electronics.",
           "index": "Products in this catalogue"},
}


def logo():
    return B.LOGO_SVG


def contact_line(lang):
    country = C.COUNTRY_IT if lang == "it" else C.COUNTRY_EN
    bits = [f"{C.COMPANY} · {C.ADDRESS_LINE}, {C.ZIP_CITY}, {country}"]
    cont = " · ".join(x for x in (C.PHONE, C.EMAIL) if x)
    return bits[0], cont


def sheet(pid, lang):
    pr = P.PRODUCTS[pid]
    L_ = LABELS[lang]
    addr, cont = contact_line(lang)
    keys = "".join(f"<li>{k}</li>" for k in pr["key"][lang])
    tables = ""
    for group, rows in pr["specs"]:
        trs = "".join(f'<tr><th>{B.v(k, lang)}</th><td>{B.v(val, lang)}</td></tr>' for k, val in rows)
        tables += f'<table><caption>{B.v(group, lang)}</caption>{trs}</table>'
    if pr.get("note"):
        tables += f'<p class="fn">{B.v(pr["note"], lang)}</p>'
    art = os.path.join(SITE, "img", pr["art"])
    draft = f'<div class="draft">{L_["draft"]}</div>' if C.PREVIEW else ""
    return f"""<section class="sheet">
<div class="tri"><i></i><i></i><i></i></div>
<div class="top"><div class="brand">{logo()}<div><b>BOSARI</b><span>Thermal Management</span></div></div><div class="kind">{L_['kind']}</div></div>
<h1>{pr['name']}</h1><p class="sub">{B.v(pr['subtitle'], lang)}</p>
<div class="cols"><div><div class="art"><img src="file://{art}" alt=""></div><ul class="k">{keys}</ul></div><div>{tables}</div></div>
<h2>{L_['desc']}</h2><div class="desc">{B.product_body(pr, lang)}</div>
<div class="foot"><div>{addr}<br>{cont}</div><div>{L_['web']}</div></div>{draft}
</section>"""


def doc(body, lang):
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def cover(lang):
    L_ = LABELS[lang]
    items = "".join(f"<li>{pr['name']} – {B.v(pr['subtitle'], lang)}</li>" for pr in P.PRODUCTS.values())
    addr, cont = contact_line(lang)
    return f"""<section class="cover"><div class="tri"><i></i><i></i><i></i></div>
<div class="brand">{logo()}<div><b>BOSARI</b><span>Thermal Management</span></div></div>
<h1 style="margin-top:20mm">{L_['cat']}</h1><p>{L_['cat_sub']}</p><h2>{L_['index']}</h2><ul>{items}</ul>
<div class="foot"><div>{addr}<br>{cont}</div><div>{L_['web']}</div></div></section>"""


def to_pdf(html, out_path, tmp):
    src = os.path.join(tmp, "in.html")
    with open(src, "w", encoding="utf-8") as fh:
        fh.write(html)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={out_path}", "file://" + src], check=True, capture_output=True, timeout=120)
    print("scritto", os.path.relpath(out_path, ROOT), os.path.getsize(out_path) // 1024, "KB")


def main():
    os.makedirs(OUT, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for lang in ("it", "en"):
            for pid in P.PRODUCTS:
                to_pdf(doc(sheet(pid, lang), lang), os.path.join(OUT, B.pdf_name(pid, lang)), tmp)
            body = cover(lang) + "".join(sheet(pid, lang) for pid in P.PRODUCTS)
            name = "bosari-catalogo-it.pdf" if lang == "it" else "bosari-catalogue-en.pdf"
            to_pdf(doc(body, lang), os.path.join(OUT, name), tmp)
    B.main()      # rigenera il sito: compaiono i pulsanti di download


if __name__ == "__main__":
    main()
