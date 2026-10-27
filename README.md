# Il peso della pioggia

*L'intelligenza artificiale dal neurone ai modelli che ragionano*  
*Un dialogo tra un allievo e il suo Maestro*

**[Scarica il libro in PDF](https://github.com/luca-zane/il-peso-della-pioggia/releases/latest/download/il-peso-della-pioggia.pdf)**: gratuito, in italiano, sempre all'ultima versione.

Pagina del libro: [pioggia.lucazane.com](https://pioggia.lucazane.com) · Tutte le versioni: [Releases](../../releases) · DOI: [10.5281/zenodo.23697734](https://doi.org/10.5281/zenodo.23697734)

Un uomo si ferma sulla soglia di un dojo di karate affacciato sul mare. Tutti intorno a lui parlano di intelligenza artificiale e tutti hanno già un'opinione; lui prima vuole capire. Il Maestro, un vecchio decimo dan che va per mare da cinquant'anni, lo accompagna una cintura alla volta: dal neurone più semplice ai modelli che ragionano, fino a costruirci sopra qualcosa di suo. Le lezioni si tengono nel dojo, sulla spiaggia, in barca, al mercato del porto, nel cantiere. E mentre impara, l'allievo vive: c'è la nebbia, c'è un vecchio pescatore che torna di lezione in lezione, c'è una notte in cui vorrebbe smettere e una mattina in cui riprende.

## Prefazione

### A chi è rivolto

A chi è curioso e ha poco tempo: a chi lavora, ha sentito tutte le parole e vuole finalmente capire che cosa c'è sotto. Non servono titoli di studio. Agli esperti di intelligenza artificiale il libro servirà a poco, e non pretende altro.

### Che cosa troverete

Soprattutto le idee che non cambiano ogni sei mesi: il neurone, l'allenamento, le reti che guardano e che leggono, gli embedding, i Transformer, i modelli di linguaggio e il modo in cui vengono educati e serviti. Le novità recenti stanno solo in brevi riquadri, le *Cronache del 2026*, datati di proposito. Niente guide agli strumenti del momento, niente euforie, niente critiche feroci. Alla fine si dovrebbe saper prendere qualsiasi annuncio e chiedersi in quale lezione cade, quale problema risolve, a quale prezzo, e se è sostanza o rumore.

### Perché il dojo e il mare

Perché nel dojo si impara ripetendo, sbagliando e correggendo, un gesto alla volta: è così che impara una rete. E in mare si naviga con strumenti imperfetti, il vento si legge ma non si comanda, e non ci si fida mai di un solo strumento: è così che si usa un modello. Le immagini si ricordano meglio delle definizioni. Per questo il libro è anche un racconto: un lettore che sente la storia avanzare legge volentieri anche le pagine più dense.

### Come leggere

Il percorso va per cinture, due lezioni ciascuna, dalla bianca alla nera, con alcuni intermezzi fuori dal dojo. Ogni lezione è divisa in sedute brevi, e ogni seduta si chiude con un *mokusō*: una sola domanda, senza risposta, su cui fermarsi. In fondo a ogni lezione ci sono una frase da portare con sé, *la lezione per il mondo*, e pochi esercizi, il *kata per casa*, risolti in fondo al libro. Le formule ci sono, perché sono il ponte verso i paper e il codice, ma si possono saltare.

### Come è stato scritto

In dialogo, come il libro: le domande, i dubbi, la rotta e le scelte sono dell'autore; molte risposte sono state costruite insieme a un modello di linguaggio, rilette, corrette e verificate una per una. I numeri del libro sono rifatti nei notebook di questo repository.

## Indice

- Prefazione
- Prologo · La soglia del dojo
- Lezione 1 · Il neurone e i pesi (verso la cintura bianca)
- Lezione 2 · La piccola rete (cintura bianca)
- Lezione 3 · Come impara una rete (verso la cintura gialla)
- Lezione 4 · Generalizzare e restare stabili (cintura gialla)
- Intermezzo · L'attrezzeria (cintura gialla)
- Lezione 5 · Le CNN, l'arte dello sguardo (verso la cintura arancione)
- Lezione 6 · RNN, LSTM, GRU: la memoria del tempo (cintura arancione)
- Intermezzo · Veglia in porto (cintura arancione)
- Lezione 7 · Embedding: il significato come geometria (verso la cintura verde)
- Lezione 8 · Attention e Transformer, la tecnica regina (cintura verde)
- Lezione 9 · Gli LLM: token, pretraining, scaling (verso la cintura blu)
- Lezione 10 · Il post-training: dal sapere al comportamento (cintura blu)
- Intermezzo · La prima guardia (cintura blu)
- Lezione 11 · L'economia del gesto: inferenza e ottimizzazioni (verso la cintura marrone)
- Lezione 12 · Pensare prima di colpire: ragionamento e test-time compute (cintura marrone)
- Intermezzo · Il cantiere di casa (cintura marrone)
- Lezione 13 · Le altre scuole (verso la cintura nera)
- Lezione 14 · Dal dojo al mare: costruire per chi naviga (cintura nera)
- Epilogo · Il rotolo del dojo
- Le storie del rotolo
- Appendice · Le soluzioni dei kata per casa

## Che cosa c'è qui

| Cartella | Contenuto |
| --- | --- |
| `testo/` | Il testo del libro: la sorgente da cui si costruisce il PDF (HTML) e una copia in Markdown, comoda da leggere e da confrontare tra versioni |
| `notebook/` | Un notebook per ogni lezione: i conti fatti a mano nel libro, rifatti con il codice e confrontati con quelli stampati |
| `costruzione/` | Tutto ciò che serve per costruire il PDF: lo script di conversione, il modello LaTeX, le figure, i caratteri e la copertina |
| `FONTI.md` | Gli studi, i numeri e le cronache citati nel libro, lezione per lezione |
| `ERRATA.md` | Gli errori trovati dopo la pubblicazione |
| `docs/` | La pagina web del libro |

## Costruire il PDF

Servono Python 3 con BeautifulSoup (e, se c'è, pikepdf) e una distribuzione TeX con LuaLaTeX.

```
cd costruzione
python3 build.py
```

Il risultato è `costruzione/il-peso-della-pioggia.pdf`, lo stesso file che si scarica dalle Releases.

## Segnalare un errore

Se trovi un errore di fatto, un conto che non torna o un refuso, apri una segnalazione nella sezione *Issues*, indicando la lezione, la seduta e una breve citazione del passaggio. Le correzioni entrano nelle versioni successive e vengono annotate in `ERRATA.md`.

## Licenze

- **Il testo, le figure e la copertina** sono distribuiti con licenza [Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0 Internazionale](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it) (CC BY-NC-ND 4.0). Puoi copiarli e diffonderli gratuitamente, con qualsiasi mezzo e in qualsiasi formato, citando l'autore. Non puoi venderli, né usarli a fini commerciali, né distribuirne versioni modificate. Traduzioni, adattamenti e altri usi sono possibili solo con il permesso scritto dell'autore.
- **Il codice degli esercizi** e gli script che costruiscono il PDF sono distribuiti con licenza MIT. Vedi `LICENSE-CODE`.
- **I caratteri** EB Garamond sono distribuiti con la SIL Open Font License.

## Citare il libro

Luca Zane, *Il peso della pioggia.*  
*L'intelligenza artificiale dal neurone ai modelli che ragionano*,  
versione 1.0, 2026. DOI: [10.5281/zenodo.23697734](https://doi.org/10.5281/zenodo.23697734).

Vedi anche `CITATION.cff`.

© 2026 Luca Zane
