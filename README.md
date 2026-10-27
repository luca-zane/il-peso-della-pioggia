# Il peso della pioggia

*L'intelligenza artificiale dal neurone ai modelli che ragionano. Un dialogo tra un allievo e il suo Maestro.*

**[Scarica il PDF](https://github.com/luca-zane/il-peso-della-pioggia/releases/latest/download/il-peso-della-pioggia.pdf)**

> Il libro è un dialogo tra un allievo e un Maestro, in un dojo di karate affacciato sul mare. […]
> Soprattutto teorie consolidate: il neurone, l'allenamento, le reti che guardano e che leggono, gli embedding, i Transformer, i modelli di linguaggio e il modo in cui vengono educati e serviti. Sono le idee che non cambiano ogni sei mesi, e sono quelle che servono per capire le nuove.
>
> Il dojo è aperto a tutti: etichette e titoli di studio restano fuori, come le scarpe sulla soglia.
>
> — dalla *Prefazione*

## Leggerlo

**[Scarica il libro in PDF](https://github.com/luca-zane/il-peso-della-pioggia/releases/latest/download/il-peso-della-pioggia.pdf)**, gratuito, sempre all'ultima versione.

Pagina del libro: [pioggia.lucazane.com](https://pioggia.lucazane.com) · Tutte le versioni: [Releases](../../releases)

## Che cosa c'è qui

| Cartella | Contenuto |
| --- | --- |
| `testo/` | Il testo del libro: la sorgente da cui si costruisce il PDF (HTML) e una copia in Markdown, comoda da leggere e da confrontare tra versioni |
| `costruzione/` | Tutto ciò che serve per costruire il PDF: lo script di conversione, il modello LaTeX, le figure, i caratteri e la copertina |
| `notebook/` | Gli esercizi del libro da far girare: i conti fatti a mano nelle lezioni, ripetuti con il codice |
| `FONTI.md` | Le fonti degli studi, dei numeri e delle cronache citati nel libro |
| `ERRATA.md` | Gli errori trovati dopo la pubblicazione |
| `docs/` | La pagina web del libro |

## Costruire il PDF

Servono Python 3 con BeautifulSoup e una distribuzione TeX con LuaLaTeX.

```
cd costruzione
python3 build.py
```

Il risultato è `costruzione/libro.pdf`. Con `--bozza` si ottiene la versione con la filigrana per i lettori di prova.

## Segnalare un errore

Se trovi un errore di fatto, un conto che non torna o un refuso, apri una segnalazione nella sezione *Issues*, indicando la lezione, la seduta e una breve citazione del passaggio. Le correzioni entrano nelle versioni successive e vengono annotate in `ERRATA.md`.

## Licenze

- **Il testo, le figure e la copertina** sono distribuiti con licenza [Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0 Internazionale](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it) (CC BY-NC-ND 4.0). Puoi copiarla e diffonderla gratuitamente, con qualsiasi mezzo e in qualsiasi formato, citando l'autore. Non puoi venderla, né usarla a fini commerciali, né distribuirne versioni modificate. Traduzioni, adattamenti e altri usi sono possibili solo con il permesso scritto dell'autore.
- **Il codice degli esercizi**, e gli script che costruiscono il PDF, sono distribuiti con licenza MIT. Vedi `LICENSE-CODE`.
- **I caratteri** EB Garamond sono distribuiti con la SIL Open Font License.

## Citare il libro

Vedi `CITATION.cff`, oppure il DOI riportato nella pagina della versione su Zenodo.

© 2026 Luca Zane
