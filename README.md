# Il peso della pioggia

**L'intelligenza artificiale dal neurone ai modelli che ragionano**

*Un dialogo tra un allievo e il suo Maestro, tra un dojo di karate e un piccolo porto.*

**[Scarica il PDF](https://github.com/luca-zane/il-peso-della-pioggia/releases/latest/download/il-peso-della-pioggia.pdf)**

Un allievo bussa alla porta di un dojo affacciato sul mare. In quattordici lezioni, tra il tatami, la barca e le banchine, il Maestro lo accompagna dal singolo neurone fino ai modelli che ragionano: come impara una rete, perché sbaglia con sicurezza, come nasce e si educa un grande modello di linguaggio, quanto costa farlo lavorare, e come si costruisce qualcosa di utile per chi lo userà.

Il libro è pensato per chi ha una base tecnica o scientifica e vuole capire davvero come funzionano questi sistemi, senza perdersi. I conti più impegnativi stanno in riquadri che si possono saltare.

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

- **Il testo, le figure e la copertina** sono distribuiti con licenza [Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0 Internazionale](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it) (CC BY-NC-ND 4.0). Puoi leggerlo, stamparlo e condividerlo liberamente, citando l'autore, senza usi commerciali e senza modificarlo.
- **Il codice** (gli script di costruzione e i notebook) è distribuito con licenza MIT: puoi copiarlo, modificarlo e usarlo nei tuoi progetti. Vedi `LICENSE-CODE`.
- **I caratteri** EB Garamond sono distribuiti con la SIL Open Font License.

## Citare il libro

Vedi `CITATION.cff`, oppure il DOI riportato nella pagina della versione su Zenodo.

© 2026 Luca Zane
