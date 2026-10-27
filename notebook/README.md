# Notebook

Gli esercizi del libro da far girare. Ogni notebook rifà in codice i conti che nel libro si fanno a mano, lezione per lezione, e risolve i kata per casa. Ogni numero calcolato viene confrontato con quello scritto nel libro: un segno ✓ vuol dire che coincidono.

| Notebook | Che cosa c'è dentro |
| --- | --- |
| `lezione-01-il-neurone` | il neurone della serata, i due kata |
| `lezione-02-la-piccola-rete` | la rete 3 → 2 → 1, la softmax e la temperatura |
| `lezione-03-come-impara-una-rete` | la backpropagation filo per filo, i conti del cantiere dei grandi |
| `lezione-04-generalizzare` | il quaderno sottile, il modello pigro, la serata assurda, la regola di controllo |
| `intermezzo-attrezzeria` | la rete in PyTorch con tre learning rate, il gradiente in JAX |
| `lezione-05-le-cnn` | la lente su una riga e su una piccola carta, pesi e conti, il max pooling |
| `lezione-06-rnn` | il barometro, il foglietto che sbiadisce |
| `lezione-07-embedding` | la mappa a due direzioni e la similarità coseno |
| `lezione-08-attention` | il giro al mercato, per una parola e in forma di matrici |
| `lezione-09-gli-llm` | il BPE in codice, la curva della vasca, Gopher contro Chinchilla |
| `lezione-10-post-training` | il giudice delle coppie, LoRA, la regola dell'esame |
| `lezione-11-inferenza` | il carrello, il quaderno, i quattro pesi quantizzati, il conto in euro |
| `lezione-12-ragionamento` | la regola dei dodicesimi, il voto delle cinque rotte |
| `intermezzo-cantiere-di-casa` | le quattro formule del cantiere di casa |
| `lezione-13-le-altre-scuole` | i vecchi al bar del porto, il bozzetto, il foglietto contro il quaderno |
| `lezione-14-agenti` | i passi dell'agente |

## Come usarli

Servono Python 3 e NumPy. L'attrezzeria usa anche PyTorch e JAX.

```
pip install numpy jupyter torch "jax[cpu]"
jupyter notebook
```

Si possono aprire anche direttamente su GitHub, con i risultati già calcolati, o su Google Colab. Ogni notebook finisce con un *Prova tu*: cambia i numeri e guarda che cosa succede.

Il codice è distribuito con licenza MIT (vedi `LICENSE-CODE`).
