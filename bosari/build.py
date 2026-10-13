# Costruisce site/ (pagine HTML in italiano e inglese) a partire da config.py e dai testi qui sotto.
# Uso:  python3 build.py
# I testi sono nei dizionari T["it"] e T["en"]: modificare li' e rilanciare.
import os
import re
from urllib.parse import quote_plus

import config as C
import products as P

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

# pagina -> nome file per lingua (la stessa pagina ha un nome per ogni lingua)
PAGES = {
    "home":     {"it": "index.html",    "en": "index.html"},
    "company":  {"it": "azienda.html",  "en": "company.html"},
    "products": {"it": "prodotti.html", "en": "products.html"},
    "services": {"it": "servizi.html",   "en": "services.html"},
    "news":     {"it": "novita.html",    "en": "news.html"},
    "contacts": {"it": "contatti.html", "en": "contacts.html"},
}

T = {
    "it": {
        "lang": "it", "locale": "it_IT", "other": "en", "other_label": "EN",
        "nav": {"home": "Home", "company": "Profilo aziendale", "products": "Prodotti", "services": "Servizi", "news": "Novità", "contacts": "Contatti"},
        "skip": "Vai al contenuto",
        "draft": "BOZZA – contatti, orari, storia, novità e alcune immagini sono segnaposto inventati: da sostituire con i dati reali prima della pubblicazione.",
        "tagline": "Thermal Management",
        "title": {
            "home": "Bosari Thermal Management | Raffreddamento per elettronica di potenza",
            "company": "Profilo aziendale | Bosari Thermal Management",
            "products": "Prodotti | Bosari Thermal Management",
            "services": "Servizi | Bosari Thermal Management",
            "news": "Novità | Bosari Thermal Management",
            "contacts": "Contatti e come raggiungerci | Bosari Thermal Management",
        },
        "desc": {
            "home": "Bosari Thermal Management progetta e produce raffreddatori ad acqua ATLANTIS, scambiatori COLUMBUS e sistemi a heat pipe U-COOL per l'elettronica di potenza. Opera (MI).",
            "company": "Chi è Bosari Thermal Management: gestione termica per l'elettronica di potenza, a Opera (Milano).",
            "products": "Prodotti Bosari: raffreddatori ad acqua ATLANTIS BAE6 e BAE9, scambiatore COLUMBUS 1000, sistema a heat pipe U-COOL 1200/50, con schede tecniche.",
            "services": "Dall'analisi termica al prototipo, alla produzione e all'assistenza: i servizi di Bosari Thermal Management.",
            "news": "Novità e aggiornamenti da Bosari Thermal Management.",
            "contacts": "Contatti, richiesta di informazioni e mappa per raggiungere Bosari Thermal Management a Opera (MI).",
        },
        "home": {
            "h1": "Raffreddamento per l'elettronica di potenza",
            "sub": "Raffreddatori ad acqua, scambiatori di calore e sistemi a heat pipe per l'industria, la saldatura e la trazione ferroviaria.",
            "cta1": "Scopri i prodotti", "cta2": "Richiedi informazioni",
            "intro_h": "Dissipare tanto calore, in poco spazio",
            "intro": "Bosari Thermal Management (BTM) progetta e produce soluzioni per smaltire il calore di componenti elettronici di potenza come tiristori, GTO e IGBT, e per raffreddare armadi elettronici e camere ambientali.",
            "cards_h": "Le linee di prodotto",
            "more": "Scopri la linea",
            "figures": [("4.000 W", "dissipabili da un raffreddatore ATLANTIS BAE9, sulle due facce"), ("100 W/K", "efficienza di raffreddamento dello scambiatore COLUMBUS 1000"), ("1.200 W", "dissipati a convezione naturale dal sistema U-COOL 1200/50")],
            "app_h": "Dove lavorano le nostre soluzioni",
            "app": "Applicazioni industriali pesanti, saldatura, trazione elettrica leggera e pesante, veicoli ferroviari, armadi elettronici e camere ambientali.",
            "cta_h": "Avete un progetto o una specifica?",
            "cta": "Scriveteci: valutiamo insieme la soluzione termica più adatta, anche su misura.",
        },
        "company": {
            "h1": "Profilo aziendale",
            "sub": "Gestione termica per l'elettronica di potenza.",
            "who_h": "Chi siamo",
            "who": [
                "Bosari Thermal Management S.r.l. (BTM) ha sede a Opera, alle porte di Milano, e si occupa di gestione termica per l'elettronica di potenza.",
                "Le sue linee di prodotto sono i raffreddatori ad acqua ATLANTIS, gli scambiatori di calore COLUMBUS per armadi elettronici e i sistemi a heat pipe U-COOL.",
            ],
            "facts": [(C.FOUNDED, "anno di fondazione"), ("Opera (MI)", "sede"), ("4.000 W", "massima potenza dissipata da un raffreddatore ATLANTIS"), ("IP55 · NEMA 12", "grado di protezione degli scambiatori COLUMBUS")],
            "val_h": "Il nostro approccio",
            "vals": [
                ("Su misura", "Le soluzioni si adattano al cliente: diametro di contatto dei raffreddatori fino a 55 o 85 mm, raccordi del fluido in alluminio o titanio, sistemi di controllo su richiesta. Il sistema U-COOL è nato dalla specifica di un cliente."),
                ("Materiali controllati", "I materiali e i componenti sono selezionati e controllati per garantire la conformità alle specifiche richieste."),
                ("Pensati per ambienti severi", "Prodotti per applicazioni industriali e ferroviarie, con prove di urti e vibrazioni secondo IEC 77 §16."),
            ],
            "ref_h": "Settori",
            "ref": ["Trazione elettrica leggera e pesante, veicoli ferroviari", "Industria pesante e saldatura", "Armadi elettronici e camere ambientali"],
            "story_h": "La nostra storia",
            "story": [
                "Bosari Thermal Management nasce a Opera nel " + C.FOUNDED + ", con l'idea di portare nell'elettronica di potenza un raffreddamento più efficiente, leggero e affidabile. Nel tempo la gamma si è sviluppata in tre linee: i raffreddatori ad acqua ATLANTIS, gli scambiatori COLUMBUS per armadi elettronici e i sistemi a heat pipe U-COOL.",
                "Lavoriamo a stretto contatto con i progettisti dei nostri clienti: molte soluzioni, come il U-COOL, nascono da una loro specifica.",
            ],
            "proc_h": "Come lavoriamo",
            "proc": [("Ascolto", "Raccogliamo la specifica: potenza da dissipare, temperature, spazio e norme."), ("Progetto", "Dimensioniamo la soluzione termica e prepariamo il disegno."), ("Prototipo", "Realizziamo un campione per verificare la soluzione."), ("Produzione", "Produciamo in serie con materiali selezionati e controllati."), ("Assistenza", "Seguiamo il cliente nella scelta, nell'installazione e nell'uso.")],
        },
        "products": {
            "h1": "Prodotti", "sub": "Raffreddatori ad acqua, scambiatori di calore e sistemi a heat pipe.",
            "open": "Scheda tecnica", "back": "← Tutti i prodotti", "request": "Richiedi informazioni su questo prodotto",
            "spec_h": "Caratteristiche tecniche", "images_h": "Immagini",
            "title": "{name} | Bosari Thermal Management",
            "key_h": "In sintesi",
        },
        "services": {
            "h1": "Servizi", "sub": "Dalla specifica al prodotto, e oltre.",
            "intro": "Oltre ai prodotti a catalogo, aiutiamo i clienti a risolvere il loro problema termico, dalla prima analisi fino all'assistenza.",
            "items": [
                ("Analisi e dimensionamento termico", "Partiamo dalla potenza da dissipare, dalle temperature ammesse e dallo spazio disponibile per proporre la soluzione più adatta."),
                ("Progettazione e prototipi", "Disegno, scelta dei materiali e realizzazione di un campione per verificare la soluzione prima della serie."),
                ("Prove e verifiche", "Verifiche termiche e meccaniche con riferimento alle norme richieste dal cliente, per esempio IEC 77 §16 per urti e vibrazioni."),
                ("Produzione in serie", "Raffreddatori e scambiatori prodotti con materiali e componenti selezionati e controllati."),
                ("Assistenza tecnica", "Supporto nella scelta, nell'installazione e nell'uso dei prodotti Bosari."),
            ],
            "cta_h": "Avete un'esigenza particolare?", "cta": "Descriveteci la vostra applicazione: vi diciamo come possiamo aiutarvi.", "btn": "Richiedi informazioni",
        },
        "news": {
            "h1": "Novità", "sub": "Aggiornamenti da Bosari.",
            "items": [
                ("2026-09-15", "15 settembre 2026", "Nuovo sito Bosari", "Abbiamo rinnovato il sito: schede tecniche aggiornate, in italiano e in inglese."),
                ("2026-06-10", "10 giugno 2026", "Raccordi in alluminio o titanio per ATLANTIS", "I raffreddatori ad acqua ATLANTIS possono montare il raccordo del fluido più adatto all'applicazione, in alluminio o in titanio."),
                ("2026-03-02", "2 marzo 2026", "Scheda tecnica U-COOL 1200/50", "Pubblicata la scheda del sistema a heat pipe per il raffreddamento di inverter IGBT su veicoli ferroviari."),
            ],
        },
        "contacts": {
            "h1": "Contatti", "sub": "Richiedete informazioni o un'offerta.",
            "where_h": "Dove siamo", "hours": "Orari", "tel": "Telefono", "mail": "Email", "vat": "Partita IVA",
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
        "nav": {"home": "Home", "company": "Company Profile", "products": "Products", "services": "Services", "news": "News", "contacts": "Contacts"},
        "skip": "Skip to content",
        "draft": "DRAFT – contacts, opening hours, history, news and some images are invented placeholders: replace them with real data before publishing.",
        "tagline": "Thermal Management",
        "title": {
            "home": "Bosari Thermal Management | Cooling for power electronics",
            "company": "Company Profile | Bosari Thermal Management",
            "products": "Products | Bosari Thermal Management",
            "services": "Services | Bosari Thermal Management",
            "news": "News | Bosari Thermal Management",
            "contacts": "Contacts and how to reach us | Bosari Thermal Management",
        },
        "desc": {
            "home": "Bosari Thermal Management designs and manufactures ATLANTIS water coolers, COLUMBUS heat exchangers and U-COOL heat pipe systems for power electronics. Opera (Milan), Italy.",
            "company": "About Bosari Thermal Management: thermal management for power electronics, in Opera (Milan), Italy.",
            "products": "Bosari products: ATLANTIS BAE6 and BAE9 water coolers, COLUMBUS 1000 heat exchanger, U-COOL 1200/50 heat pipe system, with technical data.",
            "services": "From thermal analysis to prototype, production and support: the services of Bosari Thermal Management.",
            "news": "News and updates from Bosari Thermal Management.",
            "contacts": "Contacts, information requests and map to reach Bosari Thermal Management in Opera (Milan), Italy.",
        },
        "home": {
            "h1": "Cooling for power electronics",
            "sub": "Water coolers, heat exchangers and heat pipe systems for industry, welding and railway traction.",
            "cta1": "Discover the products", "cta2": "Request information",
            "intro_h": "Dissipating a lot of heat in a small space",
            "intro": "Bosari Thermal Management (BTM) designs and manufactures solutions to remove the heat of power electronic components such as thyristors, GTOs and IGBTs, and to cool electronic cabinets and environmental chambers.",
            "cards_h": "Product lines",
            "more": "Discover the line",
            "figures": [("4,000 W", "dissipated by one ATLANTIS BAE9 cooler, on both sides"), ("100 W/K", "cooling efficiency of the COLUMBUS 1000 heat exchanger"), ("1,200 W", "dissipated by natural convection by the U-COOL 1200/50 system")],
            "app_h": "Where our solutions work",
            "app": "Heavy industrial applications, welding, light and heavy electrical traction, railway vehicles, electronic cabinets and environmental chambers.",
            "cta_h": "Do you have a project or a specification?",
            "cta": "Write to us: we will assess the most suitable thermal solution together, tailor-made if needed.",
        },
        "company": {
            "h1": "Company Profile",
            "sub": "Thermal management for power electronics.",
            "who_h": "Who we are",
            "who": [
                "Bosari Thermal Management S.r.l. (BTM) is based in Opera, on the edge of Milan, and deals with thermal management for power electronics.",
                "Its product lines are the ATLANTIS water coolers, the COLUMBUS heat exchangers for electronic cabinets and the U-COOL heat pipe systems.",
            ],
            "facts": [(C.FOUNDED, "year founded"), ("Opera (MI)", "headquarters"), ("4,000 W", "maximum power dissipated by an ATLANTIS cooler"), ("IP55 · NEMA 12", "protection of the COLUMBUS exchangers")],
            "val_h": "Our approach",
            "vals": [
                ("Tailor-made", "Solutions adapt to the customer: cooler contact diameter up to 55 or 85 mm, aluminium or titanium fluid nipples, control systems on request. The U-COOL system was born from a customer's specification."),
                ("Controlled materials", "Materials and components are selected and quality controlled to ensure compliance with the requested specifications."),
                ("Made for severe environments", "Products for industrial and railway applications, with shock and vibration tests as per IEC 77 §16."),
            ],
            "ref_h": "Sectors",
            "ref": ["Light and heavy electrical traction, railway vehicles", "Heavy industry and welding", "Electronic cabinets and environmental chambers"],
            "story_h": "Our story",
            "story": [
                "Bosari Thermal Management was founded in Opera in " + C.FOUNDED + ", with the idea of bringing more efficient, lighter and more reliable cooling to power electronics. Over time the range has grown into three lines: the ATLANTIS water coolers, the COLUMBUS exchangers for electronic cabinets and the U-COOL heat pipe systems.",
                "We work closely with our customers' designers: many solutions, such as the U-COOL, start from their specification.",
            ],
            "proc_h": "How we work",
            "proc": [("Listening", "We collect the specification: power to dissipate, temperatures, space and standards."), ("Design", "We size the thermal solution and prepare the drawing."), ("Prototype", "We build a sample to verify the solution."), ("Production", "We produce in series with selected and controlled materials."), ("Support", "We follow the customer in choice, installation and use.")],
        },
        "products": {
            "h1": "Products", "sub": "Water coolers, heat exchangers and heat pipe systems.",
            "open": "Data sheet", "back": "← All products", "request": "Request information on this product",
            "spec_h": "Technical characteristics", "images_h": "Images",
            "title": "{name} | Bosari Thermal Management",
            "key_h": "At a glance",
        },
        "services": {
            "h1": "Services", "sub": "From specification to product, and beyond.",
            "intro": "Besides the catalogue products, we help customers solve their thermal problem, from the first analysis to support.",
            "items": [
                ("Thermal analysis and sizing", "We start from the power to dissipate, the allowed temperatures and the available space to propose the most suitable solution."),
                ("Design and prototypes", "Drawing, choice of materials and a sample to verify the solution before series production."),
                ("Tests and verifications", "Thermal and mechanical checks referring to the standards required by the customer, for example IEC 77 §16 for shocks and vibrations."),
                ("Series production", "Coolers and exchangers made with selected and quality-controlled materials and components."),
                ("Technical support", "Help with the choice, installation and use of Bosari products."),
            ],
            "cta_h": "Do you have a special need?", "cta": "Describe your application: we will tell you how we can help.", "btn": "Request information",
        },
        "news": {
            "h1": "News", "sub": "Updates from Bosari.",
            "items": [
                ("2026-09-15", "15 September 2026", "New Bosari website", "We have renewed the website: updated data sheets, in Italian and English."),
                ("2026-06-10", "10 June 2026", "Aluminium or titanium nipples for ATLANTIS", "ATLANTIS water coolers can mount the cooling fluid nipple best suited to the application, in aluminium or titanium."),
                ("2026-03-02", "2 March 2026", "U-COOL 1200/50 data sheet", "Published the data sheet of the heat pipe system for cooling IGBT inverters on railway vehicles."),
            ],
        },
        "contacts": {
            "h1": "Contacts", "sub": "Ask for information or a quotation.",
            "where_h": "Where we are", "hours": "Opening hours", "tel": "Phone", "mail": "Email", "vat": "VAT number",
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

LOGO_SVG = """<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false"><rect x="11" y="4" width="7" height="31" fill="#008c45"/><rect x="20.5" y="4" width="7" height="31" fill="#fff" stroke="#b4bfb8" stroke-width="1"/><rect x="30" y="4" width="7" height="31" fill="#cd212a"/><path d="M6 3 V28 A18 18 0 0 0 42 28 V3" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"/></svg>"""


def pfile(key, lang):
    if key in PAGES:
        return PAGES[key][lang]
    return P.PRODUCTS[key]["file"]      # stessa pagina in IT e EN


def href(page, lang, anchor=""):
    return pfile(page, lang) + (("#" + anchor) if anchor else "")


def link_target(raw, lang):
    page, _, anchor = raw.partition("#")
    return href(page, lang, anchor)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def head(page, lang, t, title, desc):
    other = t["other"]
    canon = C.BASE_URL + lang + "/" + pfile(page, lang)
    alt_it = C.BASE_URL + "it/" + pfile(page, "it")
    alt_en = C.BASE_URL + "en/" + pfile(page, "en")
    robots = '<meta name="robots" content="noindex">\n' if C.PREVIEW else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<meta name="theme-color" content="#008c45">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="it" href="{alt_it}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="x-default" href="{alt_it}">
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:site_name" content="{C.COMPANY}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{C.BASE_URL}img/hero.jpg">
<link rel="stylesheet" href="../css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"{C.COMPANY}","url":"{C.BASE_URL}","address":{{"@type":"PostalAddress","streetAddress":"{C.ADDRESS_LINE}","postalCode":"20090","addressLocality":"Opera","addressRegion":"MI","addressCountry":"IT"}}{(',"telephone":"' + C.PHONE + '"') if C.PHONE else ''},"email":"{C.EMAIL}"}}</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
"""


def header(page, lang, t):
    current = "products" if page not in PAGES else page
    items = "".join(
        f'<li><a href="{href(p, lang)}"{" aria-current=\"page\"" if p == current else ""}>{t["nav"][p]}</a></li>'
        for p in PAGES
    )
    other = t["other"]
    draft = f'<div class="draft" role="note">{t["draft"]}</div>' if C.PREVIEW else ""
    return f"""{draft}<header class="site-header">
<div class="tricolor" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="header-in">
<a class="brand" href="{href('home', lang)}" aria-label="{C.COMPANY}">{LOGO_SVG}<div><b>BOSARI</b><span>{t['tagline']}</span></div></a>
<nav aria-label="Menu"><ul>{items}</ul></nav>
<div class="lang" role="group" aria-label="Language / Lingua"><span aria-current="true">{lang.upper()}</span><a href="../{other}/{pfile(page, other)}" hreflang="{other}" lang="{other}">{t['other_label']}</a></div>
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
    hours = C.HOURS_IT if lang == "it" else C.HOURS_EN
    if hours:
        rows.append(f'<p>{c["hours"]}: {hours}</p>')
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


def family_cards(lang, t, more):
    out = []
    for f in P.FAMILIES:
        out.append(
            f'<article class="card"><h3>{esc(f["name"])} · {esc(f["title"][lang])}</h3><p>{esc(f["intro"][lang])}</p>'
            f'<a class="more" href="{href("products", lang, f["id"])}">{more} →</a></article>'
        )
    return "".join(out)


def page_home(lang, t):
    h = t["home"]
    ctas = f'<a class="btn btn-red" href="{href("products", lang)}">{h["cta1"]}</a><a class="btn btn-line" href="{href("contacts", lang)}">{h["cta2"]}</a>'
    figs = "".join(f"<div><b>{v}</b><span>{l}</span></div>" for v, l in h["figures"])
    return (
        hero(h["h1"], h["sub"], True, ctas)
        + f'<section><div class="wrap"><h2>{h["intro_h"]}</h2><div class="rule"></div><p class="lead">{h["intro"]}</p></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{h["cards_h"]}</h2><div class="rule"></div><div class="grid g3">{family_cards(lang, t, h["more"])}</div></div></section>'
        + f'<section><div class="wrap"><div class="facts">{figs}</div></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{h["app_h"]}</h2><div class="rule"></div><p class="lead">{h["app"]}</p></div></section>'
        + f'<section><div class="wrap"><h2>{h["cta_h"]}</h2><div class="rule"></div><p class="lead">{h["cta"]}</p><p><a class="btn btn-green" href="{href("contacts", lang)}">{h["cta2"]}</a></p></div></section>'
    )


def page_company(lang, t):
    c = t["company"]
    who = "".join(f'<p class="lead">{p}</p>' for p in c["who"])
    facts = "".join(f"<div><b>{val}</b><span>{label}</span></div>" for val, label in c["facts"])
    story = "".join(f"<p>{p}</p>" for p in c["story"])
    steps = "".join(f"<li><b>{n}</b><span>{d}</span></li>" for n, d in c["proc"])
    vals = "".join(f'<article class="card"><h3>{n}</h3><p>{d}</p></article>' for n, d in c["vals"])
    refs = "".join(f"<li>{r}</li>" for r in c["ref"])
    return (
        hero(c["h1"], c["sub"])
        + f'<section><div class="wrap"><h2>{c["who_h"]}</h2><div class="rule"></div>{who}</div></section>'
        + f'<section class="alt"><div class="wrap"><div class="facts">{facts}</div></div></section>'
        + f'<section><div class="wrap"><h2>{c["story_h"]}</h2><div class="rule"></div><div class="prose">{story}</div></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{c["val_h"]}</h2><div class="rule"></div><div class="grid g3">{vals}</div></div></section>'
        + f'<section><div class="wrap"><h2>{c["proc_h"]}</h2><div class="rule"></div><ol class="steps">{steps}</ol></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{c["ref_h"]}</h2><div class="rule"></div><ul class="ticks">{refs}</ul></div></section>'
    )


def page_services(lang, t):
    s_ = t["services"]
    cards = "".join(f'<article class="card"><h3>{n}</h3><p>{d}</p></article>' for n, d in s_["items"])
    return (
        hero(s_["h1"], s_["sub"])
        + f'<section><div class="wrap"><p class="lead">{s_["intro"]}</p><div class="grid g3">{cards}</div></div></section>'
        + f'<section class="alt"><div class="wrap"><h2>{s_["cta_h"]}</h2><div class="rule"></div><p class="lead">{s_["cta"]}</p>'
        + f'<p><a class="btn btn-green" href="{href("contacts", lang)}">{s_["btn"]}</a></p></div></section>'
    )


def page_news(lang, t):
    n = t["news"]
    items = "".join(
        f'<article class="news"><time datetime="{iso}">{label}</time><h3>{title}</h3><p>{text}</p></article>'
        for iso, label, title, text in n["items"]
    )
    return hero(n["h1"], n["sub"]) + f'<section><div class="wrap"><div class="news-list">{items}</div></div></section>'


def spec_tables(prod, lang):
    out = []
    for group, rows in prod["specs"]:
        trs = "".join(f"<tr><th scope=\"row\">{v(k, lang)}</th><td>{v(val, lang)}</td></tr>" for k, val in rows)
        out.append(f'<table class="spec-table"><caption>{v(group, lang)}</caption><tbody>{trs}</tbody></table>')
    if prod.get("note"):
        out.append(f'<p class="foot-note">{v(prod["note"], lang)}</p>')
    return "".join(out)


def v(x, lang):
    """Valore che puo' essere una stringa uguale nelle due lingue o un dizionario {it, en}."""
    if isinstance(x, dict):
        return x[lang]
    if lang == "en":                       # 0,5 bar -> 0.5 bar
        return re.sub(r"(\d),(\d)", r"\1.\2", x)
    return x


def page_products(lang, t):
    p = t["products"]
    sub = "".join(f'<li><a href="#{f["id"]}">{esc(f["name"])}</a></li>' for f in P.FAMILIES)
    blocks = []
    for f in P.FAMILIES:
        cards = []
        for pid in f["products"]:
            pr = P.PRODUCTS[pid]
            thumb = next((fn.replace("{lang}", lang) for fn in pr["thumbs"] if os.path.exists(os.path.join(SITE, "img", fn.replace("{lang}", lang)))), None)
            img = f'<img src="../img/{thumb}" alt="{esc(v(pr["subtitle"], lang))}" loading="lazy">' if thumb else ""
            keys = "".join(f"<li>{k}</li>" for k in pr["key"][lang])
            cards.append(
                f'<article class="card product-card">{img}<h3>{esc(pr["name"])}</h3><p>{esc(v(pr["subtitle"], lang))}</p>'
                f'<ul class="ticks">{keys}</ul><a class="btn btn-green" href="{pr["file"]}">{p["open"]}</a></article>'
            )
        blocks.append(
            f'<div class="family" id="{f["id"]}"><h2>{esc(f["name"])} · {esc(f["title"][lang])}</h2><div class="rule"></div>'
            f'<p class="lead">{esc(f["intro"][lang])}</p><div class="grid g3">{"".join(cards)}</div></div>'
        )
    return (
        hero(p["h1"], p["sub"])
        + f'<section><div class="wrap"><ul class="subnav">{sub}</ul>{"".join(blocks)}</div></section>'
    )


def page_product(pid, lang, t):
    p = t["products"]
    pr = P.PRODUCTS[pid]
    fam = next(f for f in P.FAMILIES if f["id"] == pr["family"])
    # testi: tre modelli diversi di scheda (comune ATLANTIS / paragrafi / sezioni)
    body = ""
    if "text" in pr:
        paras = [x.replace("{power}", v(pr["power"], lang)) for x in P.ATLANTIS_TEXT[lang]]
        body = "".join(f"<p>{x}</p>" for x in paras)
    elif "paragraphs" in pr:
        body = "".join(f"<p>{x}</p>" for x in pr["paragraphs"][lang])
    else:
        for i, (h, ps) in enumerate(pr["sections"][lang]):
            body += f"<h3>{h}</h3>" + "".join(f"<p>{x}</p>" for x in ps)
            if i == len(pr["sections"][lang]) - 1 and pr.get("construction"):
                body += "<ol>" + "".join(f"<li>{x}</li>" for x in pr["construction"][lang]) + "</ol>"
    keys = "".join(f"<li>{k}</li>" for k in pr["key"][lang])
    gallery = ""
    imgs = [(fn.replace("{lang}", lang), cap) for fn, cap in pr["images"]]
    imgs = [(fn, cap) for fn, cap in imgs if os.path.exists(os.path.join(SITE, "img", fn))]
    if imgs:
        figs = "".join(f'<figure><img src="../img/{fn}" alt="{esc(v(cap, lang))}" loading="lazy"><figcaption>{v(cap, lang)}</figcaption></figure>' for fn, cap in imgs)
        gallery = f'<section class="alt"><div class="wrap"><h2>{p["images_h"]}</h2><div class="rule"></div><div class="gallery">{figs}</div></div></section>'
    return (
        hero(esc(pr["name"]), esc(v(pr["subtitle"], lang)))
        + f'<section><div class="wrap"><p class="back"><a href="{href("products", lang, fam["id"])}">{p["back"]}</a></p>'
        + f'<div class="detail"><div class="text"><h2>{p["key_h"]}</h2><div class="rule"></div><ul class="ticks">{keys}</ul>{body}'
        + f'<p><a class="btn btn-red" href="{href("contacts", lang)}">{p["request"]}</a></p></div>'
        + f'<div class="specs"><h2>{p["spec_h"]}</h2><div class="rule"></div>{spec_tables(pr, lang)}</div></div></div></section>'
        + gallery
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


BUILDERS = {"home": page_home, "company": page_company, "products": page_products,
            "services": page_services, "news": page_news, "contacts": page_contacts}

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="#fff"/><rect x="11" y="4" width="7" height="31" fill="#008c45"/><rect x="20.5" y="4" width="7" height="31" fill="#fff" stroke="#b4bfb8" stroke-width="1"/><rect x="30" y="4" width="7" height="31" fill="#cd212a"/><path d="M6 3 V28 A18 18 0 0 0 42 28 V3" fill="none" stroke="#17211c" stroke-width="3.5" stroke-linecap="round"/></svg>"""

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


def write(lang, fn, html):
    with open(os.path.join(SITE, lang, fn), "w", encoding="utf-8") as fh:
        fh.write(html)


def main():
    for lang, t in T.items():
        os.makedirs(os.path.join(SITE, lang), exist_ok=True)
        for page in PAGES:
            html = (head(page, lang, t, t["title"][page], t["desc"][page]) + header(page, lang, t)
                    + BUILDERS[page](lang, t) + footer(page, lang, t))
            write(lang, PAGES[page][lang], html)
        for pid, pr in P.PRODUCTS.items():
            title = t["products"]["title"].format(name=pr["name"])
            desc = f'{pr["name"]} – {v(pr["subtitle"], lang)}. ' + "; ".join(pr["key"][lang]) + "."
            html = head(pid, lang, t, title, desc) + header(pid, lang, t) + page_product(pid, lang, t) + footer(pid, lang, t)
            write(lang, pr["file"], html)
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
