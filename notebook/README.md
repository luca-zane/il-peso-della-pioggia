# Notebook

Gli esercizi del libro da far girare. Ogni notebook rifà in codice i conti che nel libro si fanno a mano, lezione per lezione, e risolve i kata per casa. Ogni numero calcolato viene confrontato con quello scritto nel libro: un segno ✓ vuol dire che coincidono.

| Notebook | Che cosa c'è dentro |
| --- | --- |
| `lezione-01-il-neurone` | il neurone della serata, le tre attivazioni, la softmax, il prodotto scalare e il coseno, la linea nella sabbia, la cross-entropy, la correzione del diario, i due kata |
| `lezione-02-la-piccola-rete` | i tre cerchi e le quattro serate, l'interazione, i pesi iniziali, la piega, la temperatura, la soglia, precision e recall, la calibrazione, gli alberi, il modello decisionale, i due kata |
| `lezione-03-come-impara-una-rete` | la discesa del gradiente, il cesto a fine giornata, la backpropagation filo per filo, lo scandaglio a mano, i neuroni morti, i conti del cantiere dei grandi, gli ottimizzatori |
| `lezione-04-generalizzare` | i tre mucchi, i neuroni A e B del quaderno sottile, le notti rare, la deviazione, le bussole dell'ensemble, la serata assurda, la cima tra i bozzelli, la regola di controllo |
| `intermezzo-attrezzeria` | la rete in PyTorch con tre learning rate, il gradiente in JAX |
| `lezione-05-le-cnn` | la lente su una riga e su una piccola carta, pesi e conti di uno strato, il campo recettivo, la vedetta leggera, gli esempi avversari, i due kata |
| `lezione-06-rnn` | il barometro, il ricordo che sbiadisce, il quaderno della LSTM, il GRU, l'attenzione del 2014 |
| `lezione-07-embedding` | la mappa a due direzioni e la similarità coseno, il passo del trattore, imparare per contrasto, i conti del bibliotecario e le matrioske, lo schedario di bordo |
| `lezione-08-attention` | il giro al mercato, per una parola e in forma di matrici, il conto del quadrato, la maschera, la bussola che gira, i pesi del blocco |
| `lezione-09-gli-llm` | il BPE in codice, la curva della vasca, il duello delle due navi, oltre la regola, il gradino della misura |
| `lezione-10-post-training` | il giudice in formula, la soglia dell'esame, la media dei fratelli, le vele staccabili di LoRA |
| `lezione-11-inferenza` | il viaggio e la busta in numeri, i quattro pesi scritti con pochi bit, il sapere oscuro, il conto in euro |
| `lezione-12-ragionamento` | la regola dei dodicesimi, il prezzo del pensiero, il muro del caos, il voto dei cinque skipper, il giudice |
| `intermezzo-piccolo-cabotaggio` | i pesi e la busta, il viaggio, il venditore: i conti del piccolo cabotaggio |
| `lezione-13-le-altre-scuole` | la restauratrice e il bozzetto, le cartoline, la busta e il foglietto, i vecchi al bar del porto, le linee tra le barche |
| `lezione-14-agenti` | i passi dell'agente, i sei guardiani |

## Come usarli

Servono Python 3 e NumPy. L'attrezzeria usa anche PyTorch e JAX.

```
pip install numpy jupyter torch "jax[cpu]"
jupyter notebook
```

Si possono aprire anche direttamente su GitHub, con i risultati già calcolati, o su Google Colab. Alcuni notebook finiscono con un *Prova tu*: cambia i numeri e guarda che cosa succede.

Il codice è distribuito con licenza MIT (vedi `LICENSE-CODE`).
