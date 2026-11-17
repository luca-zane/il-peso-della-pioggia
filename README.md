<img src="docs/copertina.jpg" alt="Copertina di «Il peso della pioggia»" width="220" align="right">

# Il peso della pioggia

*L'intelligenza artificiale dal neurone ai modelli che ragionano.*  
*Un dialogo tra un allievo e il suo Maestro.*

di Luca Zane · versione 2.0 · 17 novembre 2026 · gratuito · 316 pagine A4

**[Scarica il libro in PDF](https://github.com/luca-zane/il-peso-della-pioggia/releases/latest/download/il-peso-della-pioggia.pdf)**

Pagina del libro: [pioggia.lucazane.com](https://pioggia.lucazane.com) · Tutte le versioni: [Releases](../../releases) · DOI: [10.5281/zenodo.23697734](https://doi.org/10.5281/zenodo.23697734)

<br clear="right">

## Il libro

Il libro è un dialogo tra un allievo e un Maestro, in un dojo di karate affacciato sul mare. Nel dojo si impara ripetendo, sbagliando e correggendo, un gesto alla volta: è così che impara una rete. In mare si naviga con strumenti precisi dentro un mondo che non lo è: il vento si legge ma non si comanda, il tempo si prevede solo per qualche giorno, e non ci si fida mai di un solo strumento: è così che si usa un modello.

Soprattutto teorie consolidate: il neurone, l'allenamento, le reti che guardano e che leggono, gli embedding, i Transformer, i modelli di linguaggio e il modo in cui vengono educati e serviti. Sono le idee che non cambiano ogni sei mesi, e sono quelle che servono per capire le nuove. La promessa è questa: alla fine saprete prendere qualsiasi annuncio e chiedervi in quale lezione cade, quale problema risolve, a quale prezzo, e se è sostanza o rumore.

## A chi è rivolto

> *Il dojo è aperto a tutti: etichette e titoli di studio restano fuori, come le scarpe sulla soglia.*

Penso che servirà soprattutto a chi usa l'intelligenza artificiale ogni giorno, per lavoro o per curiosità, sente di averne in testa solo slogan confusi e non vuole fermarsi alla superficie: sviluppatori, ingegneri, analisti, chi guida progetti tecnici, studenti, curiosi con il gusto della logica. Con un po' di pazienza si capiscono tante cose anche da principianti.

## Il percorso

Si va per cinture, due lezioni ciascuna, dalla bianca alla nera. Dopo alcune cinture c'è un intermezzo: un'uscita dal dojo per mettere alla prova ciò che si sa.

| | Cintura | Che cosa si impara |
| :-: | --- | --- |
| ⚪ | Bianca · lezioni 1–2 | il neurone, i pesi, le reti a strati |
| 🟡 | Gialla · lezioni 3–4 | come una rete impara e come generalizza |
| ◌ | *Intermezzo* | *l'attrezzeria: PyTorch, JAX, TensorFlow* |
| 🟠 | Arancione · lezioni 5–6 | le architetture storiche: CNN e RNN |
| ◌ | *Intermezzo* | *la veglia in porto: contesto, allucinazioni, consiglio di modelli* |
| 🟢 | Verde · lezioni 7–8 | embedding, attention e Transformer |
| 🔵 | Blu · lezioni 9–10 | gli LLM: pretraining e post-training |
| ◌ | *Intermezzo* | *la prima guardia: scrivere la pagina, provarla, risparmiare dove conta* |
| 🟤 | Marrone · lezioni 11–12 | inferenza efficiente e ragionamento |
| ◌ | *Intermezzo* | *piccolo cabotaggio: un modello sul proprio computer* |
| ⚫ | Nera · lezioni 13–14 | le altre famiglie di modelli e la costruzione di prodotti |

In fondo al libro: l'epilogo con il rotolo del dojo e i glossari, le storie del rotolo, le soluzioni dei kata per casa e i riferimenti, lezione per lezione.

## Com'è fatta una lezione

- **Le sedute**: il racconto, in pezzi brevi. Ognuna si chiude con un *mokusō*: una sola domanda, senza risposta, su cui fermarsi.
- **Il kata di oggi**: cinque punti da ripetere prima di andare.
- **Le dicerie di banchina**: tre cose che si sentono dire in giro, e come stanno davvero.
- **La lezione per il mondo**: una frase da portare con sé fuori dal dojo.
- **Per chi vuole i conti**: le formule e i numeri, legati al punto del racconto che traducono. Sono il ponte verso i paper e il codice; chi non li ama li salta senza perdere il filo.
- **Il kata per casa**: uno o due esercizi, risolti in fondo al libro.

## Quanto tempo serve

Non è un libro da leggere in fretta: le lezioni sembrano brevi, ma sono dense. Meglio leggere una seduta alla volta, lasciarla decantare e solo dopo andare avanti. Il racconto da solo si legge in una decina di ore. Con i conti, i kata e i notebook diventa un lavoro di qualche mese: il ritmo giusto potrebbe essere una lezione alla settimana, quattordici settimane, più o meno un semestre. E non serve capire tutto: il racconto si regge da sé.

## Come è nato

> «Con l'intelligenza artificiale un libro così si scrive in un minuto.» In un minuto si ottiene un testo ordinato, scorrevole, e uguale a mille altri. Questo è nato in un altro modo: da un lungo dialogo tra l'autore e Claude, un modello di intelligenza artificiale di Anthropic. […] La rotta, le scelte e la revisione finale sono dell'autore; la stesura è cresciuta in due, una pagina alla volta. Come in una regata in doppio: il timone lo tiene uno alla volta, ma la barca la portano in due.

## Che cosa c'è qui

| Cartella | Contenuto |
| --- | --- |
| `notebook/` | Un notebook per ogni lezione: i conti fatti a mano nel libro, rifatti con il codice e confrontati con quelli stampati |
| `testo/` | Il testo del libro: la sorgente da cui si costruisce il PDF (HTML) e una copia in Markdown, comoda da leggere e da confrontare tra versioni |
| `costruzione/` | Tutto ciò che serve per costruire il PDF: lo script di conversione, il modello LaTeX, le figure, i caratteri e la copertina |
| `FONTI.md` | Gli studi, i numeri e le cronache citati nel libro, lezione per lezione |
| `ERRATA.md` | Gli errori trovati dopo la pubblicazione |
| `CHANGELOG.md` | Che cosa è cambiato da una versione all'altra |
| `docs/` | La pagina web del libro |

## Costruire il PDF

Servono Python 3 con BeautifulSoup e pikepdf, e una distribuzione TeX con LuaLaTeX e la sillabazione italiana.

```
cd costruzione
python3 build.py
```

Il risultato è `costruzione/il-peso-della-pioggia.pdf`, lo stesso file che si scarica dalle Releases.

## Errata e segnalazioni

Errori e segnalazioni sono benvenuti. Se trovi un errore di fatto, un conto che non torna o un refuso, apri una segnalazione nella sezione [Issues](../../issues), indicando la lezione, la seduta e una breve citazione del passaggio. Le correzioni entrano nelle versioni successive e vengono annotate in [`ERRATA.md`](ERRATA.md).

## Licenze

- **Il testo, le figure e la copertina** sono distribuiti con licenza [Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0 Internazionale](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it) (CC BY-NC-ND 4.0). Puoi copiarli e diffonderli gratuitamente, con qualsiasi mezzo e in qualsiasi formato, citando l'autore. Non puoi venderli, né usarli a fini commerciali, né distribuirne versioni modificate. Traduzioni, adattamenti e altri usi sono possibili solo con il permesso scritto dell'autore.
- **Il codice degli esercizi** e gli script che costruiscono il PDF sono distribuiti con licenza MIT. Vedi [`LICENSE-CODE`](LICENSE-CODE).
- **I caratteri** EB Garamond sono distribuiti con la SIL Open Font License.

## Citare il libro

Luca Zane, *Il peso della pioggia. L'intelligenza artificiale dal neurone ai modelli che ragionano*, versione 2.0, 2026. DOI: [10.5281/zenodo.23697734](https://doi.org/10.5281/zenodo.23697734).

Vedi anche [`CITATION.cff`](CITATION.cff).

© 2026 Luca Zane
