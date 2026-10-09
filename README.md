# Sito Immobiliare 4S Srl

Rifacimento completo di www.immobiliare4s.it. Sito statico: una sola pagina HTML
+ una cartella di immagini. Nessun WordPress, nessun database, nessun plugin.

## Cartelle

| Cartella  | Cosa contiene |
|-----------|---------------|
| `src/`    | **I file da modificare**: `page.html` (testi e stile) e `_scene3d.part.html` (la sezione 3D del tetto). |
| `docs/`   | Il sito pronto da mettere online. Generato, non si modifica a mano. |
| `assets/` | Materiale di partenza: logo in alta risoluzione, foto originali, ritagli. |

## Come modificare il sito

1. Apri `src/page.html` e cambia quello che serve.
2. Dal terminale, dentro questa cartella:

   ```
   python build.py
   ```

3. Il risultato aggiornato è in `docs/`.

`build.py` aggiunge al file la testata HTML (titolo, descrizione per Google,
anteprima per WhatsApp/Facebook, dati dell'azienda per i motori di ricerca) e
rigenera favicon e immagine social a partire dal logo.

## Come vedere il sito prima di pubblicarlo

Doppio clic su `docs/index.html`: si apre nel browser.

## Dov'e' online adesso

Anteprima pubblica su **https://sagardelledonne.github.io/immobiliare4s/**
(repo `sagardelledonne/immobiliare4s`, GitHub Pages dal ramo `main`, cartella `docs/`).
La pagina ha il `noindex`: Google non la indicizza, cosi' non fa concorrenza al
sito vero che e' ancora su WordPress.

Per aggiornarla: `python build.py` e poi `git add -A && git commit && git push`.

## Come metterlo sul dominio vero

In testa a `build.py` ci sono due righe da cambiare (`BASE` e `ANTEPRIMA`),
poi si rilancia `python build.py`.
Va caricato tutto il contenuto della cartella `docs/` (compresa `img/`) nella
cartella pubblica dell'hosting, al posto di WordPress. Funziona su qualsiasi
hosting, anche il più economico, perché sono solo file statici.

## Dati usati nel sito

- Immobiliare 4S Srl — Via Daniele Manin 48, 20092 Cinisello Balsamo (MI)
- P.IVA 12749360967
- Tel. ufficio 02 67177263 — email immobiliare4soci@gmail.com
- WhatsApp e modulo contatti: +39 328 783 4263 (Massimo)
- Soci: Massimo, Vincenzo Milano, Emanuele Mangione, Carmelo Lanzafame
- Video: https://youtu.be/KJu2mDW_ChU

## Da confermare con il cliente

Queste frasi sono state scritte in modo ragionevole ma vanno verificate:

- sopralluogo e preventivo gratuiti e senza impegno;
- zone servite (Cinisello Balsamo, Sesto San Giovanni, Monza, Milano e limitrofi);
- preventivo consegnato in pochi giorni dal sopralluogo;
- un socio segue ogni cantiere dall'inizio alla consegna;
- 260+ cantieri completati (numero preso dal vecchio sito);
- numero WhatsApp da usare nel modulo contatti.

## Il modulo contatti

Non invia email da solo (servirebbe un servizio a pagamento). Prepara il testo
della richiesta e lo apre in WhatsApp o nel programma di posta del visitatore,
che decide se inviarlo. Se in futuro serve la ricezione automatica, si può
collegare a un servizio tipo Formspree senza toccare il resto del sito.

## Il modello 3D del tetto

La sezione "Cosa c'è sotto le tegole" è un modello 3D fatto con Three.js:
casa con gli strati del tetto che si aprono, confronto prima/dopo e due gru
che girano. Scelte fatte per tenerlo leggero:

- la libreria (circa 150 KB compressi) viene scaricata **solo quando si arriva
  a quella sezione**, non all'apertura del sito;
- geometrie semplici, niente ombre calcolate, risoluzione limitata;
- l'animazione si ferma quando la sezione esce dallo schermo o si cambia scheda;
- chi ha attivato "riduci animazioni" nel sistema vede il modello fermo;
- se il dispositivo non supporta il 3D compare un testo al posto del modello,
  e l'elenco degli strati resta comunque leggibile.

Il sorgente è in `src/_scene3d.part.html` (stile + HTML + script insieme).

## Formato delle immagini

Le foto sono in **WebP** (37% più leggere dei JPEG originali: 920 KB -> 584 KB).
Gli originali restano in `assets/`. Se l'hosting non riconoscesse il formato,
va aggiunta la riga `AddType image/webp .webp` nel file `.htaccess`.
