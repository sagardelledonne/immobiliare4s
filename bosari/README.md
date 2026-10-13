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

## Da sostituire / confermare (importante)

Prodotti (testi inglesi e dati tecnici) ricavati dagli screenshot del sito attuale forniti dal
cliente. Il sito originale e' solo in inglese: **le versioni italiane sono traduzioni da far
rivedere**. Per tutto il resto www.bosari.it non era raggiungibile.

1. **Immagine di copertina**: `site/img/hero.jpg` e' un segnaposto generato
   (`make_hero.py`). Va sostituita con la foto vera, leggermente sfuocata, di un cartiglio
   di un progetto reale con righello e strumenti appoggiati (1920x900 circa, sotto 300 KB).
2. **Foto e disegni dei prodotti**: ritagliati dagli screenshot, quindi a bassa risoluzione.
   Servono i file originali (`site/img/`). Manca la foto del U-COOL 1200/50.
3. **Logo**: in testata c'e' un marchio provvisorio tricolore + scritta. Va messo il logo vero.
4. **Profilo aziendale, Home, Services, News**: non visti. I testi del profilo sono ricavati
   dalle pagine prodotto; il vecchio sito aveva anche le voci "Services" e "News": da decidere se tenerle.
5. **Indirizzo**: gli elenchi riportano sia Via Eugenio Montale 14 sia Via Grazia Deledda 10/M
   a Opera. La mappa usa `MAP_QUERY` in `config.py`.
6. **Telefono, email, partita IVA**: telefono e partita IVA mancanti; l'email
   `info@bosari.it` e' provvisoria ed e' quella che riceve le richieste del modulo contatti.
7. **Anno di fondazione** (1996, da registro imprese) da verificare.
8. **Pubblicazione**: in `config.py` mettere `PREVIEW = False` e il dominio definitivo,
   poi `python3 build.py`. Caricare il contenuto di `site/` sull'hosting.

## Note tecniche

- Nessuna animazione ne' transizione (il CSS le disattiva esplicitamente).
- Unico JavaScript: scelta lingua nella pagina radice e preparazione dell'email nel modulo.
- Il modulo non invia da solo: apre il programma di posta del visitatore con il testo pronto.
- La mappa e' un incorporamento Google Maps; in alternativa c'e' il link a OpenStreetMap.
- Adatto a telefono, con tema scuro automatico se il dispositivo lo usa.
