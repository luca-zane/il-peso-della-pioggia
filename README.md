<img src="docs/copertina.jpg" alt="Copertina di «Il peso della pioggia»" width="220" align="right">

# Il peso della pioggia

*L'intelligenza artificiale dal neurone ai modelli che ragionano.*  
*Un dialogo tra un allievo e il suo Maestro.*

di Luca Zane · versione 2.0 · 17 novembre 2026 · gratuito · 316 pagine A4

**[Scarica il libro in PDF](https://github.com/luca-zane/il-peso-della-pioggia/releases/latest/download/il-peso-della-pioggia.pdf)**

Pagina del libro: [pioggia.lucazane.com](https://pioggia.lucazane.com) · Tutte le versioni: [Releases](../../releases) · DOI: [10.5281/zenodo.23697734](https://doi.org/10.5281/zenodo.23697734) · ORCID: [0009-0005-0960-9220](https://orcid.org/0009-0005-0960-9220)

<br clear="right">

> ***Quanto pesa la pioggia?***

Dipende. Per chi è in forma, quasi niente: esce e si allena. Per chi è stanco, abbastanza da restare a casa. Lo stesso fatto pesa in modo diverso a seconda di tutto il resto. È da qui che comincia l'intelligenza artificiale: un neurone che dà un peso a ogni cosa e impara a correggerlo sbagliando.

Un uomo si ferma sulla soglia di un dojo affacciato sul mare. Intorno a lui tutti parlano di intelligenza artificiale e hanno già un'opinione; lui prima vuole capire. Il Maestro lo accompagna una cintura alla volta, dal neurone più semplice ai modelli che ragionano, tra il dojo, la spiaggia e la barca.

Alla fine saprete prendere qualsiasi annuncio e chiedervi in quale lezione cade, quale problema risolve, a quale prezzo, e se è sostanza o rumore. E forse vi accorgerete che, strada facendo, il libro parlava anche di voi: di come prendete le decisioni, di quanto vi fidate di ciò che vedete, di quanto sapete tornare sui vostri passi, del peso che date alle cose che vi accadono.

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

## Domande frequenti

**È davvero gratuito?**  
Sì, e lo resterà. Il PDF si scarica senza registrazione e si può leggere, stampare e condividere liberamente, citando l'autore. Non si può vendere.

**C'è qualcosa da vendere dietro?**  
No. Dietro non c'è una società, né corsi, consulenze o altro da vendere. È nato come un quaderno personale, per una curiosità che non mi lascia stare e perché questa materia, prima di parlarne, va capita. Se può servire anche ad altri, tanto meglio.

**Serve saper programmare o essere bravi in matematica?**  
No. Il racconto si legge senza formule e senza codice. Per chi li vuole, ogni lezione ha una parte «Per chi vuole i conti» e un notebook Python che rifà i calcoli: si possono saltare senza perdere il filo.

**Quanto tempo ci vuole?**  
Dipende da come lo si legge. Solo il racconto: una decina di ore. Con i conti, i kata per casa e i notebook diventa un lavoro più impegnativo, da distribuire nel tempo: il ritmo giusto potrebbe essere una lezione alla settimana, quattordici settimane, più o meno un semestre.

**Posso usarlo in classe o in un corso?**  
Sì. La licenza (CC BY-NC-ND 4.0) permette di distribuirlo agli studenti e di usarlo come lettura, purché gratuitamente, citando l'autore e senza modificarlo. Per traduzioni o adattamenti serve il permesso dell'autore.

**Posso stamparlo?**  
Sì: è impaginato in A4 proprio per questo. Stampato fronte-retro si legge come un libro, e lascia spazio per gli appunti a margine.

**Ho trovato un errore: come lo segnalo?**  
Aprendo una [segnalazione nel repository su GitHub](../../issues), con la lezione, la seduta e una breve citazione del passaggio. Le correzioni finiscono nell'[errata](ERRATA.md) e nella versione successiva.

**Ci saranno altre versioni?**  
Probabilmente sì: dipende anche da quanto il libro servirà a chi lo legge. Se ti è stato utile, una stellina al [repository su GitHub](https://github.com/luca-zane/il-peso-della-pioggia) o una segnalazione aiutano a capirlo. Il pulsante «Scarica il PDF» porta sempre all'ultima versione, e il DOI che raccoglie tutte le versioni, [10.5281/zenodo.23697733](https://doi.org/10.5281/zenodo.23697733), punta sempre alla più recente.

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

ORCID dell'autore: [0009-0005-0960-9220](https://orcid.org/0009-0005-0960-9220).

Vedi anche [`CITATION.cff`](CITATION.cff).

© 2026 Luca Zane
