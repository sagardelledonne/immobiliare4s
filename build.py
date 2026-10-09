# Costruisce docs/index.html dal sorgente src/page.html + favicon e immagine social.
#
# QUANDO IL SITO VA SUL DOMINIO VERO:
#   - mettere BASE = "https://www.immobiliare4s.it/"
#   - mettere ANTEPRIMA = False  (toglie il noindex e fa entrare il sito su Google)
#   - rilanciare: python build.py
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__)).replace(os.sep, "/")
SRC  = ROOT + "/src/page.html"
SITE = ROOT + "/docs"
IMG  = SITE + "/img"

BASE      = "https://sagardelledonne.github.io/immobiliare4s/"
ANTEPRIMA = True

BRAND = (221, 153, 51)
INK   = (20, 19, 15)

def make_favicon():
    mark = Image.open(IMG + "/logo-mark-only.png")
    for size in (180, 512):
        canvas = Image.new("RGBA", (size, size), BRAND + (255,))
        w = int(size * 0.74)
        h = int(w * mark.height / mark.width)
        m = mark.resize((w, h), Image.LANCZOS)
        canvas.paste(m, ((size - w) // 2, (size - h) // 2), m)
        canvas.convert("RGB").save(SITE + "/favicon-%d.png" % size, optimize=True)
    ico = Image.open(SITE + "/favicon-512.png")
    ico.save(SITE + "/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

def make_webp():
    import glob
    for j in glob.glob(IMG + "/*.jpg"):
        Image.open(j).convert("RGB").save(j[:-4] + ".webp", "WEBP", quality=80, method=6)

def make_og():
    full = Image.open(IMG + "/logo-mark.png")
    canvas = Image.new("RGBA", (1200, 630), BRAND + (255,))
    w = 620
    h = int(w * full.height / full.width)
    m = full.resize((w, h), Image.LANCZOS)
    canvas.paste(m, ((1200 - w) // 2, (630 - h) // 2), m)
    canvas.convert("RGB").save(SITE + "/social.jpg", "JPEG", quality=88, optimize=True)

HEAD = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Immobiliare 4S Srl, impresa edile a Cinisello Balsamo (MI). Rifacimento tetti, lattoneria, facciate, bonifica amianto, muratura, cartongesso e ristrutturazioni. Sopralluogo e preventivo gratuiti.">
<meta name="theme-color" content="#DD9933">
{CANONICAL}
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="favicon-512.png">
<link rel="apple-touch-icon" href="favicon-180.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="Immobiliare 4S Srl">
<meta property="og:title" content="Immobiliare 4S — Impresa edile a Cinisello Balsamo">
<meta property="og:description" content="Tetti, facciate, lattoneria e ristrutturazioni complete nell'area nord di Milano. Quattro soci, oltre trent'anni di cantieri a testa.">
<meta property="og:url" content="{BASE}">
<meta property="og:image" content="{BASE}social.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "GeneralContractor",
  "name": "Immobiliare 4S Srl",
  "url": "{BASE}",
  "image": "{BASE}social.jpg",
  "telephone": "+390267177263",
  "email": "immobiliare4soci@gmail.com",
  "vatID": "IT12749360967",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Via Daniele Manin 48",
    "postalCode": "20092",
    "addressLocality": "Cinisello Balsamo",
    "addressRegion": "MI",
    "addressCountry": "IT"
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "20:00"
  }],
  "areaServed": ["Cinisello Balsamo","Sesto San Giovanni","Monza","Milano"],
  "description": "Impresa edile specializzata in rifacimento tetti, lattoneria, facciate, bonifica amianto, muratura, carpenteria, cartongesso, pavimenti, intonacatura e stuccatura."
}
</script>
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""

def build():
    with open(SRC, encoding="utf-8") as f:
        page = f.read()
    # tutto cio' che sta prima di <a class="skip"> appartiene a <head>
    cut = page.index('<a class="skip"')
    head, body = page[:cut], page[cut:]
    canonical = '<link rel="canonical" href="%s">' % BASE
    if ANTEPRIMA:
        canonical = '<meta name="robots" content="noindex, nofollow">\n' + canonical
    testa = HEAD.replace("{CANONICAL}", canonical).replace("{BASE}", BASE)
    out = testa + head + "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
    with open(SITE + "/index.html", "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print("scritto", SITE + "/index.html", len(out), "byte")

if __name__ == "__main__":
    make_favicon()
    make_webp()
    make_og()
    build()
