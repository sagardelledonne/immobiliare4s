# Costruisce site/ (pagine HTML in italiano e inglese) a partire da config.py e dai testi qui sotto.
# Uso:  python3 build.py
# I testi sono nei dizionari T["it"] e T["en"]: modificare li' e rilanciare.
import os
from urllib.parse import quote_plus

import config as C

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

# pagina -> nome file per lingua (la stessa pagina ha un nome per ogni lingua)
PAGES = {
    "home":     {"it": "index.html",    "en": "index.html"},
    "company":  {"it": "azienda.html",  "en": "company.html"},
    "products": {"it": "prodotti.html", "en": "products.html"},
    "contacts": {"it": "contatti.html", "en": "contacts.html"},
}

T = {
    "it": {
        "lang": "it", "locale": "it_IT", "other": "en", "other_label": "EN",
        "nav": {"home": "Home", "company": "Profilo aziendale", "products": "Prodotti", "contacts": "Contatti"},
        "skip": "Vai al contenuto",
        "tagline": "Thermal Management",
        "title": {
            "home": "Bosari Thermal Management | Scambiatori e raffreddatori a heat pipe",
            "company": "Profilo aziendale | Bosari Thermal Management",
            "products": "Prodotti | Bosari Thermal Management",
            "contacts": "Contatti e come raggiungerci | Bosari Thermal Management",
        },
        "desc": {
            "home": "Bosari Thermal Management progetta e produce scambiatori di calore e raffreddatori a heat pipe per l'elettronica di potenza e le applicazioni ferrotranviarie. Opera (MI).",
            "company": "Chi è Bosari Thermal Management: competenza nella gestione termica con tecnologia heat pipe, a Opera (Milano).",
            "products": "Le linee di prodotto Bosari: scambiatori di calore a heat pipe, raffreddatori isolati elettricamente fino a 12 kV, soluzioni su specifica del cliente.",
            "contacts": "Contatti, richiesta di informazioni e mappa per raggiungere Bosari Thermal Management a Opera (MI).",
        },
        "home": {
            "h1": "Gestione termica con tecnologia heat pipe",
            "sub": "Scambiatori di calore e raffreddatori per l'elettronica di potenza: più superficie di scambio, meno peso e ingombro rispetto ai sistemi di raffreddamento tradizionali.",
            "cta1": "Scopri i prodotti", "cta2": "Richiedi informazioni",
            "intro_h": "Raffreddare bene, in poco spazio",
            "intro": "Bosari Thermal Management si occupa di gestione termica per apparati elettrici ed elettronici. Le nostre soluzioni si basano sulla tecnologia heat pipe, che permette superfici radianti più ampie a parità di peso e dimensioni.",
            "cards_h": "Le linee di prodotto",
            "cards": [
                ("Scambiatori di calore a heat pipe", "Superfici di scambio ampie, peso e dimensioni ridotti rispetto ai sistemi di raffreddamento convenzionali.", "products#scambiatori"),
                ("Raffreddatori isolati elettricamente", "Raffreddatori a heat pipe con isolamento elettrico fino a 12 kV, per apparati di potenza.", "products#isolati"),
                ("Soluzioni su specifica", "Progettazione e sviluppo di soluzioni termiche a partire dalle esigenze e dai disegni del cliente.", "products#specifica"),
            ],
            "more": "Maggiori informazioni",
            "app_h": "Dove lavorano le nostre soluzioni",
            "app": "Le applicazioni tipiche comprendono gli apparati per metropolitane e tram e, più in generale, l'elettronica di potenza dove peso, ingombro e isolamento contano.",
            "cta_h": "Avete un progetto o una specifica?",
            "cta": "Scriveteci: valutiamo insieme la soluzione termica più adatta.",
        },
        "company": {
            "h1": "Profilo aziendale",
            "sub": "Competenza termica al servizio dell'elettronica di potenza.",
            "who_h": "Chi siamo",
            "who": [
                "Bosari Thermal Management S.r.l. è un'azienda con sede a Opera, alle porte di Milano, specializzata nella gestione termica di apparati elettrici ed elettronici.",
                "La tecnologia di riferimento è quella delle heat pipe: tubi sigillati che trasportano il calore in modo molto efficiente, consentendo scambiatori e raffreddatori più leggeri e compatti dei sistemi convenzionali.",
            ],
            "facts": [(C.FOUNDED, "anno di fondazione"), ("Opera (MI)", "sede"), ("12 kV", "isolamento elettrico dei raffreddatori"), ("IT · EN", "assistenza in italiano e inglese")],
            "val_h": "Il nostro approccio",
            "vals": [
                ("Su misura", "Ogni applicazione ha i suoi vincoli: partiamo dal disegno e dalle condizioni di lavoro del cliente."),
                ("Leggerezza e compattezza", "Maggiore superficie radiante con meno peso e meno ingombro."),
                ("Sicurezza elettrica", "Soluzioni con isolamento elettrico adatto agli apparati di potenza."),
            ],
            "ref_h": "Settori",
            "ref": ["Trazione ferrotranviaria (metropolitane e tram)", "Elettronica di potenza e convertitori", "Apparati industriali che richiedono raffreddamento senza ventilazione dedicata"],
            "note": "Testi da completare e verificare con l'azienda: storia, certificazioni, numeri e referenze.",
        },
        "products": {
            "h1": "Prodotti", "sub": "Le linee di prodotto Bosari.",
            "items": [
                ("scambiatori", "Scambiatori di calore a heat pipe",
                 "Gli scambiatori a heat pipe offrono superfici radianti più ampie e permettono di risparmiare peso e dimensioni rispetto ai sistemi di raffreddamento convenzionali.",
                 ["Superfici di scambio ampie", "Peso e ingombro ridotti", "Adatti ad apparati per trazione e potenza"],
                 [("Tecnologia", "Heat pipe")]),
                ("isolati", "Raffreddatori a heat pipe isolati",
                 "Raffreddatori a heat pipe che garantiscono l'isolamento elettrico tra componente da raffreddare e dissipatore, per apparati di potenza ad alta tensione.",
                 ["Isolamento elettrico fino a 12 kV", "Impiego su apparati per metropolitane e tram", "Raffreddamento di moduli di potenza"],
                 [("Tecnologia", "Heat pipe"), ("Isolamento elettrico", "fino a 12 kV")]),
                ("specifica", "Soluzioni su specifica del cliente",
                 "Per esigenze particolari sviluppiamo il dissipatore o lo scambiatore a partire dal disegno e dalle condizioni di funzionamento.",
                 ["Dimensionamento termico", "Disegno e prototipo", "Produzione in serie"],
                 []),
            ],
            "spec_h": "Caratteristiche", "request": "Richiedi informazioni su questa linea",
            "note": "Schede tecniche, dimensioni e codici prodotto da inserire con i dati forniti dall'azienda.",
        },
        "contacts": {
            "h1": "Contatti", "sub": "Richiedete informazioni o un'offerta.",
            "where_h": "Dove siamo", "tel": "Telefono", "mail": "Email", "vat": "Partita IVA",
            "form_h": "Richiesta di informazioni",
            "name": "Nome e cognome", "company": "Azienda", "email": "Email", "msg": "Messaggio",
            "send": "Prepara la richiesta",
            "form_note": "Il pulsante apre il vostro programma di posta con il messaggio già pronto da inviare.",
            "map_h": "Come raggiungerci",
            "map_p": "Siamo a Opera, a sud di Milano. Aprite il percorso dal vostro punto di partenza:",
            "map_dir": "Indicazioni stradali (Google Maps)", "map_osm": "Apri su OpenStreetMap",
            "subject": "Richiesta di informazioni dal sito",
        },
        "footer": {"nav": "Sezioni", "contact": "Contatti", "rights": "Tutti i diritti riservati."},
    },
    "en": {
        "lang": "en", "locale": "en_GB", "other": "it", "other_label": "IT",
        "nav": {"home": "Home", "company": "Company Profile", "products": "Products", "contacts": "Contacts"},
        "skip": "Skip to content",
        "tagline": "Thermal Management",
        "title": {
            "home": "Bosari Thermal Management | Heat pipe heat exchangers and coolers",
            "company": "Company Profile | Bosari Thermal Management",
            "products": "Products | Bosari Thermal Management",
            "contacts": "Contacts and how to reach us | Bosari Thermal Management",
        },
        "desc": {
            "home": "Bosari Thermal Management designs and manufactures heat pipe heat exchangers and coolers for power electronics and rail applications. Opera (Milan), Italy.",
            "company": "About Bosari Thermal Management: thermal management expertise based on heat pipe technology, in Opera (Milan), Italy.",
            "products": "Bosari product lines: heat pipe heat exchangers, electrically insulated coolers up to 12 kV, customer-specific solutions.",
            "contacts": "Contacts, information requests and map to reach Bosari Thermal Management in Opera (Milan), Italy.",
        },
        "home": {
            "h1": "Thermal management with heat pipe technology",
            "sub": "Heat exchangers and coolers for power electronics: wider heat-exchange surfaces, less weight and smaller size than conventional cooling systems.",
            "cta1": "Discover the products", "cta2": "Request information",
            "intro_h": "Efficient cooling in a small space",
            "intro": "Bosari Thermal Management provides thermal management for electrical and electronic equipment. Our solutions are based on heat pipe technology, which allows wider radiating surfaces for the same weight and size.",
            "cards_h": "Product lines",
            "cards": [
                ("Heat pipe heat exchangers", "Wide exchange surfaces, reduced weight and dimensions compared with conventional cooling systems.", "products#scambiatori"),
                ("Electrically insulated coolers", "Heat pipe coolers with electrical insulation up to 12 kV, for power equipment.", "products#isolati"),
                ("Customer-specific solutions", "Design and development of thermal solutions starting from the customer's requirements and drawings.", "products#specifica"),
            ],
            "more": "Learn more",
            "app_h": "Where our solutions work",
            "app": "Typical applications include equipment for subways and trams and, more generally, power electronics where weight, size and electrical insulation matter.",
            "cta_h": "Do you have a project or a specification?",
            "cta": "Write to us: we will assess the most suitable thermal solution together.",
        },
        "company": {
            "h1": "Company Profile",
            "sub": "Thermal expertise at the service of power electronics.",
            "who_h": "Who we are",
            "who": [
                "Bosari Thermal Management S.r.l. is based in Opera, on the edge of Milan, and specialises in thermal management of electrical and electronic equipment.",
                "Our reference technology is the heat pipe: a sealed tube that carries heat very efficiently, making heat exchangers and coolers lighter and more compact than conventional systems.",
            ],
            "facts": [(C.FOUNDED, "year founded"), ("Opera (MI)", "headquarters"), ("12 kV", "electrical insulation of the coolers"), ("IT · EN", "support in Italian and English")],
            "val_h": "Our approach",
            "vals": [
                ("Tailor-made", "Every application has its own constraints: we start from the customer's drawing and operating conditions."),
                ("Light and compact", "More radiating surface with less weight and less space."),
                ("Electrical safety", "Solutions with electrical insulation suited to power equipment."),
            ],
            "ref_h": "Sectors",
            "ref": ["Rail traction (subways and trams)", "Power electronics and converters", "Industrial equipment needing cooling without dedicated ventilation"],
            "note": "Text to be completed and checked with the company: history, certifications, figures and references.",
        },
        "products": {
            "h1": "Products", "sub": "Bosari product lines.",
            "items": [
                ("scambiatori", "Heat pipe heat exchangers",
                 "Heat pipe heat exchangers offer wider radiating surfaces and save weight and dimensions compared with conventional cooling systems.",
                 ["Wide exchange surfaces", "Reduced weight and size", "Suited to traction and power equipment"],
                 [("Technology", "Heat pipe")]),
                ("isolati", "Insulated heat pipe coolers",
                 "Heat pipe coolers that provide electrical insulation between the component to be cooled and the heat sink, for high-voltage power equipment.",
                 ["Electrical insulation up to 12 kV", "Used in subway and tram equipment", "Cooling of power modules"],
                 [("Technology", "Heat pipe"), ("Electrical insulation", "up to 12 kV")]),
                ("specifica", "Customer-specific solutions",
                 "For special needs we develop the heat sink or heat exchanger starting from the drawing and operating conditions.",
                 ["Thermal sizing", "Design and prototype", "Series production"],
                 []),
            ],
            "spec_h": "Features", "request": "Request information on this line",
            "note": "Data sheets, dimensions and product codes to be added from the data supplied by the company.",
        },
        "contacts": {
            "h1": "Contacts", "sub": "Ask for information or a quotation.",
            "where_h": "Where we are", "tel": "Phone", "mail": "Email", "vat": "VAT number",
            "form_h": "Information request",
            "name": "Full name", "company": "Company", "email": "Email", "msg": "Message",
            "send": "Prepare the request",
            "form_note": "The button opens your email program with the message ready to send.",
            "map_h": "How to reach us",
            "map_p": "We are in Opera, south of Milan. Open the route from your starting point:",
            "map_dir": "Driving directions (Google Maps)", "map_osm": "Open on OpenStreetMap",
            "subject": "Information request from the website",
        },
        "footer": {"nav": "Sections", "contact": "Contacts", "rights": "All rights reserved."},
    },
}

LOGO_SVG = """<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false"><rect width="14.67" height="44" fill="#008c45"/><rect x="14.67" width="14.66" height="44" fill="#fff" stroke="#d6ddd8"/><rect x="29.33" width="14.67" height="44" fill="#cd212a"/></svg>"""


def href(page, lang, anchor=""):
    return PAGES[page][lang] + (("#" + anchor) if anchor else "")


def link_target(raw, lang):
    page, _, anchor = raw.partition("#")
    return href(page, lang, anchor)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def head(page, lang, t):
    other = t["other"]
    canon = C.BASE_URL + lang + "/" + PAGES[page][lang]
    alt_it = C.BASE_URL + "it/" + PAGES[page]["it"]
    alt_en = C.BASE_URL + "en/" + PAGES[page]["en"]
    robots = '<meta name="robots" content="noindex">\n' if C.PREVIEW else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t['title'][page])}</title>
<meta name="description" content="{esc(t['desc'][page])}">
{robots}<meta name="theme-color" content="#008c45">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="it" href="{alt_it}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="x-default" href="{alt_it}">
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:site_name" content="{C.COMPANY}">
<meta property="og:title" content="{esc(t['title'][page])}">
<meta property="og:description" content="{esc(t['desc'][page])}">
<meta property="og:image" content="{C.BASE_URL}img/hero.jpg">
<link rel="stylesheet" href="../css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"{C.COMPANY}","url":"{C.BASE_URL}","address":{{"@type":"PostalAddress","streetAddress":"{C.ADDRESS_LINE}","postalCode":"20090","addressLocality":"Opera","addressRegion":"MI","addressCountry":"IT"}}{(',"telephone":"' + C.PHONE + '"') if C.PHONE else ''},"email":"{C.EMAIL}"}}</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
"""


def header(page, lang, t):
    items = "".join(
        f'<li><a href="{href(p, lang)}"{" aria-current=\"page\"" if p == page else ""}>{t["nav"][p]}</a></li>'
        for p in PAGES
    )
    other = t["other"]
    return f"""<header class="site-header">
<div class="tricolor" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="header-in">
<a class="brand" href="{href('home', lang)}" aria-label="{C.COMPANY}">{LOGO_SVG}<div><b>BOSARI</b><span>{t['tagline']}</span></div></a>
<nav aria-label="Menu"><ul>{items}</ul></nav>
<div class="lang" role="group" aria-label="Language / Lingua"><span aria-current="true">{lang.upper()}</span><a href="../{other}/{PAGES[page][other]}" hreflang="{other}" lang="{other}">{t['other_label']}</a></div>
</div>
</header>
<main id="main">
"""


def hero(h1, sub, big=False, ctas=""):
    cls = "hero" if big else "hero small"
    return f"""<section class="{cls}"><div class="wrap"><h1>{h1}</h1><p>{sub}</p>{ctas}</div><div class="tricolor" aria-hidden="true"><i></i><i></i><i></i></div></section>
"""


def address_block(t, lang):
    c = t["contacts"]
    country = C.COUNTRY_IT if lang == "it" else C.COUNTRY_EN
    rows = [f"<p><strong>{C.COMPANY}</strong><br>{C.ADDRESS_LINE}<br>{C.ZIP_CITY}, {country}</p>"]
    if C.PHONE:
        rows.append(f'<p>{c["tel"]}: <a href="tel:{C.PHONE.replace(" ", "")}">{C.PHONE}</a></p>')
    if C.EMAIL:
        rows.append(f'<p>{c["mail"]}: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>')
    if C.VAT:
        rows.append(f'<p>{c["vat"]}: {C.VAT}</p>')
    return "<address>" + "".join(rows) + "</address>"


def footer(page, lang, t):
    f = t["footer"]
    nav = "".join(f'<li><a href="{href(p, lang)}">{t["nav"][p]}</a></li>' for p in PAGES)
    return f"""</main>
<footer class="site-footer">
<div class="tricolor" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="foot">
<div><h3>{C.COMPANY}</h3>{address_block(t, lang)}</div>
<div><h3>{f['nav']}</h3><ul>{nav}</ul></div>
<div><h3>{f['contact']}</h3><ul>{('<li><a href="mailto:' + C.EMAIL + '">' + C.EMAIL + '</a></li>') if C.EMAIL else ''}{('<li>' + C.PHONE + '</li>') if C.PHONE else ''}</ul></div>
</div>
<div class="legal">© {C.COMPANY} · {f['rights']}</div>
</footer>
</body>
</html>
"""


def page_home(lang, t):
    h = t["home"]
    ctas = f'<a class="btn btn-red" href="{href("products", lang)}">{h["cta1"]}</a><a class="btn btn-line" href="{href("contacts", lang)}">{h["cta2"]}</a>'
    cards = "".join(
        f'<article class="card"><h3>{esc(n)}</h3><p>{esc(d)}</p><a class="more" href="{link_target(l, lang)}">{h["more"]} →</a></article>'
        for n, d, l in h["cards"]
    )
    return (
        hero(h["h1"], h["sub"], True, ctas)
        + f'<section><div class="wrap"><h2>{h["intro_h"]}</h2><div class="rule"></div><p class="lead">{h["intro"]}</p></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{h["cards_h"]}</h2><div class="rule"></div><div class="grid g3">{cards}</div></div></section>'
        + f'<section><div class="wrap"><h2>{h["app_h"]}</h2><div class="rule"></div><p class="lead">{h["app"]}</p></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{h["cta_h"]}</h2><div class="rule"></div><p class="lead">{h["cta"]}</p><p><a class="btn btn-green" href="{href("contacts", lang)}">{h["cta2"]}</a></p></div></section>'
    )


def page_company(lang, t):
    c = t["company"]
    who = "".join(f"<p class=\"lead\">{p}</p>" for p in c["who"])
    facts = "".join(f"<div><b>{v}</b><span>{l}</span></div>" for v, l in c["facts"])
    vals = "".join(f'<article class="card"><h3>{n}</h3><p>{d}</p></article>' for n, d in c["vals"])
    refs = "".join(f"<li>{r}</li>" for r in c["ref"])
    return (
        hero(c["h1"], c["sub"])
        + f'<section><div class="wrap"><h2>{c["who_h"]}</h2><div class="rule"></div>{who}</div></section>'
        + f'<section class="alt"><div class="wrap"><div class="facts">{facts}</div></div></section>'
        + f'<section><div class="wrap"><h2>{c["val_h"]}</h2><div class="rule"></div><div class="grid g3">{vals}</div></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{c["ref_h"]}</h2><div class="rule"></div><ul class="ticks">{refs}</ul></div></section>'
    )


def page_products(lang, t):
    p = t["products"]
    sub = "".join(f'<li><a href="#{i}">{esc(n)}</a></li>' for i, n, *_ in p["items"])
    blocks = []
    for ident, name, desc, bullets, specs in p["items"]:
        ul = "".join(f"<li>{b}</li>" for b in bullets)
        spec = ""
        if specs:
            rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in specs)
            spec = f'<div class="spec"><h4>{p["spec_h"]}</h4><dl>{rows}</dl></div>'
        blocks.append(
            f'<div class="product" id="{ident}"><div><h2>{esc(name)}</h2><div class="rule"></div><p>{desc}</p><ul class="ticks">{ul}</ul>'
            f'<a class="btn btn-green" href="{href("contacts", lang)}">{p["request"]}</a></div><div>{spec}</div></div>'
        )
    return (
        hero(p["h1"], p["sub"])
        + f'<section><div class="wrap"><ul class="subnav">{sub}</ul>{"".join(blocks)}</div></section>'
    )


def page_contacts(lang, t):
    c = t["contacts"]
    q = quote_plus(C.MAP_QUERY)
    embed = f"https://www.google.com/maps?q={q}&output=embed"
    directions = f"https://www.google.com/maps/dir/?api=1&destination={q}"
    osm = f"https://www.openstreetmap.org/search?query={q}"
    subject = esc(c["subject"])
    form = f"""<form id="req" action="mailto:{C.EMAIL}" method="post" enctype="text/plain">
<label for="f-name">{c['name']}</label><input id="f-name" name="name" autocomplete="name" required>
<label for="f-co">{c['company']}</label><input id="f-co" name="company" autocomplete="organization">
<label for="f-mail">{c['email']}</label><input id="f-mail" name="email" type="email" autocomplete="email" required>
<label for="f-msg">{c['msg']}</label><textarea id="f-msg" name="message" required></textarea>
<p><button class="btn btn-red" type="submit">{c['send']}</button></p>
<p class="note">{c['form_note']}</p>
</form>
<script>
document.getElementById('req').addEventListener('submit', function (e) {{
  e.preventDefault();
  var f = e.target;
  var body = {{n: f.name.value, c: f.company.value, e: f.email.value, m: f.message.value}};
  var text = '{c['name']}: ' + body.n + '\\n{c['company']}: ' + body.c + '\\n{c['email']}: ' + body.e + '\\n\\n' + body.m;
  window.location.href = 'mailto:{C.EMAIL}?subject=' + encodeURIComponent('{subject}') + '&body=' + encodeURIComponent(text);
}});
</script>"""
    return (
        hero(c["h1"], c["sub"])
        + f'<section><div class="wrap"><div class="contact-grid"><div><h2>{c["where_h"]}</h2><div class="rule"></div>{address_block(t, lang)}</div>'
        + f'<div><h2>{c["form_h"]}</h2><div class="rule"></div>{form}</div></div></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{c["map_h"]}</h2><div class="rule"></div><p>{c["map_p"]}</p>'
        + f'<p><a class="btn btn-green" href="{directions}" target="_blank" rel="noopener">{c["map_dir"]}</a> <a href="{osm}" target="_blank" rel="noopener">{c["map_osm"]}</a></p>'
        + f'<div class="map"><iframe title="{c["map_h"]}" src="{embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>'
    )


BUILDERS = {"home": page_home, "company": page_company, "products": page_products, "contacts": page_contacts}

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#fff"/><rect width="21.3" height="64" fill="#008c45"/><rect x="42.7" width="21.3" height="64" fill="#cd212a"/><text x="32" y="44" font-family="Arial,sans-serif" font-size="30" font-weight="700" text-anchor="middle" fill="#17211c">B</text></svg>"""

REDIRECT = """<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bosari Thermal Management</title>
<meta name="robots" content="noindex">
<link rel="alternate" hreflang="it" href="it/index.html"><link rel="alternate" hreflang="en" href="en/index.html">
<script>
var l = (navigator.language || 'it').toLowerCase().indexOf('it') === 0 ? 'it' : 'en';
location.replace(l + '/index.html');
</script>
<noscript><meta http-equiv="refresh" content="0; url=it/index.html"></noscript>
</head><body><p><a href="it/index.html">Italiano</a> · <a href="en/index.html">English</a></p></body></html>
"""


def main():
    for lang, t in T.items():
        os.makedirs(os.path.join(SITE, lang), exist_ok=True)
        for page, fn in ((p, PAGES[p][lang]) for p in PAGES):
            html = head(page, lang, t) + header(page, lang, t) + BUILDERS[page](lang, t) + footer(page, lang, t)
            with open(os.path.join(SITE, lang, fn), "w", encoding="utf-8") as fh:
                fh.write(html)
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(REDIRECT)
    with open(os.path.join(SITE, "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(FAVICON)
    print("Sito scritto in", SITE)
    todo = [n for n, v in (("telefono", C.PHONE), ("partita IVA", C.VAT)) if not v]
    if todo:
        print("ATTENZIONE: dati mancanti in config.py ->", ", ".join(todo))
    print("ATTENZIONE: indirizzo, email e anno vanno confermati dal cliente (vedi config.py)")


if __name__ == "__main__":
    main()
