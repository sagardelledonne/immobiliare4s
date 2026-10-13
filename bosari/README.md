# Sito Bosari Thermal Management (bozza)

Sito vetrina bilingue (italiano / inglese), statico, senza animazioni.
Cartella indipendente dal sito Immobiliare 4S presente nel resto del repository.

## Struttura

| Pagina | Italiano | Inglese |
|---|---|---|
| Home | `it/index.html` | `en/index.html` |
| Profilo aziendale | `it/azienda.html` | `en/company.html` |
| Prodotti (elenco per linea) | `it/prodotti.html` | `en/products.html` |
| Scheda ATLANTIS BAE6 / BAE9 | `atlantis-bae6.html`, `atlantis-bae9.html` | idem in `en/` |
| Scheda COLUMBUS 1000 | `columbus-1000.html` | idem in `en/` |
| Scheda U-COOL 1200/50 | `u-cool-1200-50.html` | idem in `en/` |
| Contatti + mappa + come raggiungerci | `it/contatti.html` | `en/contacts.html` |

`site/index.html` sceglie la lingua in base al browser. Il pulsante **IT / EN** in alto
porta alla stessa pagina nell'altra lingua.

## Come si modifica

- `config.py`: indirizzo, telefono, email, partita IVA, dominio.
- `products.py`: **i prodotti** (testi IT/EN, tabelle tecniche, immagini). Per aggiungere un prodotto: nuova voce in `PRODUCTS` e nella sua famiglia in `FAMILIES`.
- `build.py`: gli altri testi (dizionari `T["it"]` e `T["en"]`).
- `site/css/style.css`: colori (verde `#008c45`, bianco, rosso `#cd212a`) e impaginazione.

Dopo ogni modifica: `python3 build.py`. Le pagine finite sono in `site/`.
Per vederle basta aprire `site/index.html` nel browser.

## Contenuti INVENTATI (segnaposto) – da sostituire prima di pubblicare

Su richiesta del cliente, tutto ciò che mancava e' stato inventato per avere una bozza completa.
Finché `PREVIEW = True` in `config.py`, ogni pagina mostra in alto un banner rosso "BOZZA" e ha il
`noindex`: con `PREVIEW = False` il banner sparisce e il sito entra su Google, quindi **prima**
di farlo va sostituito tutto quanto segue.

| Cosa | Dove | Note |
|---|---|---|
| Telefono `+39 02 1234 5678`, partita IVA `IT01234567890`, orari | `config.py` | segnaposto |
| Email `info@bosari.it` | `config.py` | riceve le richieste del modulo contatti: verificare che esista |
| Indirizzo Via Montale 14 | `config.py` | gli elenchi riportano anche Via Grazia Deledda 10/M |
| Anno di fondazione 1996 | `config.py` | da registro imprese, da verificare |
| Storia, "Come lavoriamo", approccio, settori | `build.py` (`T[..]["company"]`) | testi scritti da zero |
| Pagina Servizi (5 servizi) | `build.py` (`T[..]["services"]`) | inventata |
| Pagina Novità (3 notizie con date) | `build.py` (`T[..]["news"]`) | inventata, date comprese |
| Logo (tubo a U + tre alette tricolore) | `build.py` (`LOGO_SVG`, `FAVICON`) | disegnato per la bozza |
| Foto di copertina (cartiglio sfuocato) | `site/img/hero.jpg`, `make_hero.py` | immagine generata |
| Illustrazioni dei prodotti (4 SVG: ATLANTIS BAE6/BAE9, COLUMBUS, U-COOL) | `site/img/art-*.svg`, `make_art.py` | disegnate al posto delle foto troppo piccole; le foto vere restano nella galleria |
| Informativa privacy (testo tipo) | `build.py` (`T[..]["privacy"]`) | **va fatta verificare da un professionista** prima di pubblicare |
| Parcheggio visitatori, indicazioni stradali | `build.py` (`T[..]["contacts"]["how_p"]`) | inventati |
| Schema del U-COOL (accanto alla foto vera) | `site/img/ucool-it.svg`, `ucool-en.svg`, `make_ucool.py` | disegno illustrativo, non in scala |

## Cosa e' stato aggiunto oltre ai contenuti

- **Mappa con consenso**: Google Maps si carica solo cliccando "Carica la mappa" (niente cookie di terzi prima).
- **Modulo contatti**: scelta del prodotto (preselezionato dal pulsante "Richiedi informazioni" nella scheda) e casella di consenso privacy obbligatoria.
- **Confronto BAE6 / BAE9** nella pagina Prodotti (dati delle schede tecniche).
- `sitemap.xml`, `robots.txt` (blocca tutto finché `PREVIEW = True`), pagina `404.html`, immagine per le anteprime social (`social.jpg`).
- Controllato in browser: nessun errore JavaScript, nessun file mancante, nessun scorrimento orizzontale a 390 px.

## Schede tecniche e catalogo in PDF

`python3 make_datasheets.py` genera in `site/download/` una scheda tecnica per ogni prodotto
(`bosari-<prodotto>-it|en.pdf`) e il catalogo completo (`bosari-catalogo-it.pdf`, `bosari-catalogue-en.pdf`),
a partire dagli stessi dati del sito (`products.py`), poi rigenera il sito: i pulsanti di download
compaiono nelle schede e nella pagina Prodotti. Va rilanciato ogni volta che si cambiano i dati dei prodotti.
Serve Chromium (nel percorso indicato in cima allo script). I PDF riportano "BOZZA" finché `PREVIEW = True`.

## Preso dal sito attuale (screenshot del cliente)

Testi inglesi e dati tecnici dei 4 prodotti (ATLANTIS BAE6/BAE9, COLUMBUS 1000, U-COOL 1200/50),
con foto e disegni ritagliati (bassa risoluzione). Le versioni italiane sono traduzioni da far rivedere.
Il vecchio menu era Home, Company Profile, Products, Services, News: qui e' lo stesso, piu' Contatti.

## Foto

La foto del U-COOL 1200/50 (`site/img/ucool-foto.jpg`) e' quella fornita dal cliente, ma e' piccola
(316 x 388 px): conviene l'originale. Per cambiare una foto basta sovrascrivere il file e rilanciare
`python3 build.py`. Lo stesso vale per la copertina (`site/img/hero.jpg`, segnaposto generato).

## Note tecniche

- Nessuna animazione ne' transizione (il CSS le disattiva esplicitamente).
- Unico JavaScript: scelta lingua nella pagina radice e preparazione dell'email nel modulo.
- Il modulo non invia da solo: apre il programma di posta del visitatore con il testo pronto.
- La mappa e' un incorporamento Google Maps caricato solo su richiesta; in alternativa c'e' il link a OpenStreetMap. Non e' stato possibile vederla caricarsi in questo ambiente (Google bloccato): provarla da un browser normale.
- Adatto a telefono, con tema scuro automatico se il dispositivo lo usa.
