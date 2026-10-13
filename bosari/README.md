# Sito Bosari Thermal Management (bozza)

Sito vetrina bilingue (italiano / inglese), statico, senza animazioni.
Cartella indipendente dal sito Immobiliare 4S presente nel resto del repository.

## Struttura

| Pagina | Italiano | Inglese |
|---|---|---|
| Home | `it/index.html` | `en/index.html` |
| Profilo aziendale | `it/azienda.html` | `en/company.html` |
| Prodotti (3 linee) | `it/prodotti.html` | `en/products.html` |
| Contatti + mappa + come raggiungerci | `it/contatti.html` | `en/contacts.html` |

`site/index.html` sceglie la lingua in base al browser. Il pulsante **IT / EN** in alto
porta alla stessa pagina nell'altra lingua.

## Come si modifica

- `config.py`: indirizzo, telefono, email, partita IVA, dominio.
- `build.py`: tutti i testi (dizionari `T["it"]` e `T["en"]`).
- `site/css/style.css`: colori (verde `#008c45`, bianco, rosso `#cd212a`) e impaginazione.

Dopo ogni modifica: `python3 build.py`. Le pagine finite sono in `site/`.
Per vederle basta aprire `site/index.html` nel browser.

## Da sostituire / confermare (importante)

www.bosari.it non era raggiungibile durante la preparazione: i contenuti NON sono stati
copiati dal sito attuale. Sono basati solo su informazioni pubbliche trovate online
(sede a Opera (MI); scambiatori e raffreddatori a heat pipe; isolamento elettrico fino a
12 kV; applicazioni metropolitane e tram).

1. **Immagine di copertina**: `site/img/hero.jpg` e' un segnaposto generato
   (`make_hero.py`). Va sostituita con la foto vera, leggermente sfuocata, di un cartiglio
   di un progetto reale con righello e strumenti appoggiati (1920x900 circa, sotto 300 KB).
2. **Logo**: in testata c'e' un marchio provvisorio tricolore + scritta. Va messo il logo vero.
3. **Indirizzo**: gli elenchi riportano sia Via Eugenio Montale 14 sia Via Grazia Deledda 10/M
   a Opera. La mappa usa `MAP_QUERY` in `config.py`.
4. **Telefono, email, partita IVA**: telefono e partita IVA mancanti; l'email
   `info@bosari.it` e' provvisoria ed e' quella che riceve le richieste del modulo contatti.
5. **Testi**: profilo aziendale, valori, settori, terza linea prodotti ("su specifica") e anno
   di fondazione (1996, da registro imprese) vanno verificati. Nessun dato tecnico e' stato
   inventato: schede tecniche e codici prodotto vanno aggiunti.
6. **Pubblicazione**: in `config.py` mettere `PREVIEW = False` e il dominio definitivo,
   poi `python3 build.py`. Caricare il contenuto di `site/` sull'hosting.

## Note tecniche

- Nessuna animazione ne' transizione (il CSS le disattiva esplicitamente).
- Unico JavaScript: scelta lingua nella pagina radice e preparazione dell'email nel modulo.
- Il modulo non invia da solo: apre il programma di posta del visitatore con il testo pronto.
- La mappa e' un incorporamento Google Maps; in alternativa c'e' il link a OpenStreetMap.
- Adatto a telefono, con tema scuro automatico se il dispositivo lo usa.
