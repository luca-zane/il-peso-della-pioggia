# Fonti

Gli studi, i numeri e le cronache citati nel libro, lezione per lezione. Per ogni voce: autori, anno, titolo, e dove compare nel libro.

Per gli studi classici bastano autori, anno e titolo per ritrovarli. Per le Cronache del 2026 e per i fatti di cronaca c'è il collegamento alla fonte consultata. Se trovi un errore, lo raccogliamo in [ERRATA.md](ERRATA.md).

## Lezione 1 · Il neurone e i pesi
- F. Rosenblatt (1958), *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*. Il percettrone.

## Lezione 2 · La piccola rete
- W. Yin, J. Hay, D. Roth (2019), *Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach*. Un modello di linguaggio che sceglie tra etichette scritte a parole, senza allenarlo su quelle.
- Cronaca del 2026 · I modelli decisionali. Tra settembre e ottobre: [Liquid AI d1](https://www.marktechpost.com/2026/09/29/liquid-ai-releases-d1-a-decision-model-that-returns-calibrated-probabilities-with-zero-output-tokens/), probabilità calibrate senza token in uscita; Jev di TypeSafe AI, servizio chiuso, e Microsoft-Decision-1 ([panoramica](https://www.layer3labs.io/guides/system-one-decision-models)); una ricetta aperta in [*Releasing the Inner Jev: A Simple Recipe for Open Decision Models*](https://arxiv.org/abs/2610.17205). L'uso per togliere dal contesto le parti che non servono più: [Context Compaction](https://jevmodel.org/use-cases/context-compaction/).

## Lezione 3 · Come impara una rete
- D. E. Rumelhart, G. E. Hinton, R. J. Williams (1986), *Learning representations by back-propagating errors*. La backpropagation.
- D. P. Kingma, J. Ba (2014), *Adam: A Method for Stochastic Optimization*.
- I. Loshchilov, F. Hutter (2017), *Decoupled Weight Decay Regularization*. AdamW.

## Lezione 4 · Generalizzare e restare stabili
- M. T. Ribeiro, S. Singh, C. Guestrin (2016), *"Why Should I Trust You?": Explaining the Predictions of Any Classifier*. Lupi, husky e neve.
- M. Belkin, D. Hsu, S. Ma, S. Mandal (2019), *Reconciling modern machine learning practice and the bias-variance trade-off*. Double descent.
- K. He, X. Zhang, S. Ren, J. Sun (2015), *Deep Residual Learning for Image Recognition*. Connessioni residue.
- S. Ioffe, C. Szegedy (2015), *Batch Normalization*.

## Lezione 5 · Le CNN
- Y. LeCun, L. Bottou, Y. Bengio, P. Haffner (1998), *Gradient-Based Learning Applied to Document Recognition*. LeNet-5.
- A. Krizhevsky, I. Sutskever, G. E. Hinton (2012), *ImageNet Classification with Deep Convolutional Neural Networks*. AlexNet.
- P. Viola, M. Jones (2001), *Rapid Object Detection using a Boosted Cascade of Simple Features*. Il rivelatore di volti.
- J. Redmon, S. Divvala, R. Girshick, A. Farhadi (2015), *You Only Look Once*. YOLO.
- A. G. Howard et al. (2017), *MobileNets*.
- G. Hinton, O. Vinyals, J. Dean (2015), *Distilling the Knowledge in a Neural Network*. Distillazione e "sapere oscuro".
- I. J. Goodfellow, J. Shlens, C. Szegedy (2014), *Explaining and Harnessing Adversarial Examples*. Il panda e il gibbone.
- K. Eykholt et al. (2018), *Robust Physical-World Attacks on Deep Learning Visual Classification*. Gli adesivi sul cartello di stop.

## Lezione 6 · RNN, LSTM, GRU
- S. Hochreiter, J. Schmidhuber (1997), *Long Short-Term Memory*.
- K. Cho et al. (2014), *Learning Phrase Representations using RNN Encoder-Decoder*. GRU.
- D. Bahdanau, K. Cho, Y. Bengio (2014), *Neural Machine Translation by Jointly Learning to Align and Translate*. La nascita dell'attention.

## Intermezzo · Veglia in porto
- N. F. Liu et al. (2023), *Lost in the Middle: How Language Models Use Long Contexts*.
- M. Sharma et al. (2023), *Towards Understanding Sycophancy in Language Models*.

## Lezione 7 · Embedding
- T. Mikolov et al. (2013), *Efficient Estimation of Word Representations in Vector Space*. word2vec.
- T. Bolukbasi et al. (2016), *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*.
- A. Radford et al. (2021), *Learning Transferable Visual Models From Natural Language Supervision*. CLIP.
- A. Kusupati et al. (2022), *Matryoshka Representation Learning*.
- P. Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. RAG.
- E. J. Hu et al. (2021), *LoRA: Low-Rank Adaptation of Large Language Models*.
- X. Cheng et al., Università di Pechino e DeepSeek-AI (gennaio 2026), [*Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models*](https://arxiv.org/abs/2601.07372). Engram, le schede degli n-grammi.
- H. Cai et al. (ottobre 2026), [*EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory*](https://arxiv.org/abs/2610.10533). Correggere i fatti nelle schede, con il resto del modello fermo.

## Lezione 8 · Attention e Transformer
- A. Vaswani et al. (2017), *Attention Is All You Need*.
- J. Su et al. (2021), *RoFormer: Enhanced Transformer with Rotary Position Embedding*. RoPE.
- J. Devlin et al. (2018), *BERT*.
- C. Raffel et al. (2019), *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*. T5.
- C. Olsson et al. (2022), *In-context Learning and Induction Heads*.
- J. Ainslie et al. (2023), *GQA: Training Generalized Multi-Query Transformer Models*.

## Lezione 9 · Gli LLM
- R. Sennrich, B. Haddow, A. Birch (2016), *Neural Machine Translation of Rare Words with Subword Units*. BPE per il linguaggio; l'algoritmo di compressione è di P. Gage (1994).
- J. Hoffmann et al. (2022), *Training Compute-Optimal Large Language Models*. Chinchilla, e la formula della vasca.
- P. Villalobos et al., Epoch AI (2024), *Will we run out of data?* Il fondo dell'archivio.
- I. Shumailov et al. (2024), *AI models collapse when trained on recursively generated data*. Model collapse.
- R. Schaeffer, B. Miranda, S. Koyejo (2023), *Are Emergent Abilities of Large Language Models a Mirage?*

## Lezione 10 · Il post-training
- Z. Gekhman et al. (2024), *Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?* I fatti nuovi nel fine-tuning.
- A. Wald (1943), il lavoro sugli aerei che rientravano; ricostruito in M. Mangel, F. J. Samaniego (1984), *Abraham Wald's Work on Aircraft Survivability*.
- P. Christiano et al. (2017), *Deep Reinforcement Learning from Human Preferences*. La capriola.
- L. Ouyang et al. (2022), *Training language models to follow instructions with human feedback*.
- R. Rafailov et al. (2023), *Direct Preference Optimization*.
- Y. Bai et al. (2022), *Constitutional AI*.
- A. T. Kalai et al. (2025), *Why Language Models Hallucinate*. L'esame che premia chi tira a indovinare.
- DeepSeek-AI (2025), *DeepSeek-R1*. Ricompense verificabili, GRPO.
- T. Dettmers et al. (2023), *QLoRA*. Il modello da 65 miliardi su una sola scheda.
- Vendée Globe 2024-25: Charlie Dalin vince in 64 giorni e 19 ore, record della regata, il 14 gennaio 2025; Jean Le Cam, su una barca nuova senza foil, arriva ventesimo in 85 giorni e 15 ore ([Figaro Nautisme](https://figaronautisme.meteoconsult.fr/actus-nautisme-flash/2025-02-04/75290-jean-le-cam-20e-du-vendee-globe-2024)). La classifica ufficiale è su [vendeeglobe.org](https://www.vendeeglobe.org).
- La scomparsa di Charlie Dalin, l'11 giugno 2026, a 42 anni, per una malattia scoperta prima della regata ([Yacht](https://www.yacht.de/it/regata/vendee-globe/vendee-globe-addio-a-un-gigante-charlie-dalin-e-morto/)).

## Intermezzo · La prima guardia
- Cronaca del 2026 · Il risparmio dei token. K. Guzik (aprile 2026), [*I Benchmarked the Viral "Caveman" Prompt to Save LLM Tokens. Then My 6-Line Version Beat It*](https://dev.to/jakguzik/i-benchmarked-the-viral-caveman-prompt-to-save-llm-tokens-then-my-6-line-version-beat-it-2o81): tra il 9 e il 21% di token d'uscita in meno, senza perdita di precisione.
- Z. Yin et al. (2024), [*Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance*](https://arxiv.org/abs/2402.14531): le richieste scortesi rendono peggio.
- O. Dobariya, A. Kumar (2025), [*Mind Your Tone: Investigating How Prompt Politeness Affects LLM Accuracy*](https://arxiv.org/abs/2510.04950): le richieste scortesi rendono di poco meglio.

## Lezione 11 · L'economia del gesto
- T. Dao et al. (2022), *FlashAttention*.
- Y. Leviathan, M. Kalman, Y. Matias (2022), *Fast Inference from Transformers via Speculative Decoding*.
- DeepSeek-AI (2024), *DeepSeek-V2*, MLA; *DeepSeek-V3*, 671 miliardi di parametri, 37 attivi.
- C. Elsworth et al., Google (agosto 2025), [*Measuring the environmental impact of delivering AI at Google Scale*](https://arxiv.org/abs/2508.15734). Circa 0,24 wattora per la richiesta di testo mediana: meno di nove secondi di televisione.

## Lezione 12 · Pensare prima di colpire
- J. Wei et al. (2022), *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- T. Kojima et al. (2022), *Large Language Models are Zero-Shot Reasoners*. "Ragioniamo passo per passo".
- X. Wang et al. (2022), *Self-Consistency Improves Chain of Thought Reasoning*.
- C. Snell et al. (2024), *Scaling LLM Test-Time Compute Optimally*.
- L. Lamport, R. Shostak, M. Pease (1982), *The Byzantine Generals Problem*.
- Anthropic (2025), *Reasoning Models Don't Always Say What They Think*. Il biglietto sul tavolo.
- Anthropic (2025), *On the Biology of a Large Language Model*. 36 più 59, le rime.
- B. Baker et al., OpenAI (2025), *Monitoring Reasoning Models for Misbehavior*. "Facciamo passare il test".
- T. Korbak et al. (2025), *Chain of Thought Monitorability*.

## Lezione 13 · Le altre scuole
- J. Ho, A. Jain, P. Abbeel (2020), *Denoising Diffusion Probabilistic Models*.
- Y. Lipman et al. (2022), *Flow Matching for Generative Modeling*.
- I. Goodfellow et al. (2014), *Generative Adversarial Networks*.
- A. Dosovitskiy et al. (2020), *An Image is Worth 16x16 Words*. ViT.
- A. Gu, T. Dao (2023), *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*.
- Cronaca del 2026 · Le parole restaurate. Google DeepMind (giugno 2026), DiffusionGemma: blocchi di 256 token, fino a quattro volte più veloce del gemello Gemma, oltre mille token al secondo su una H100 ([Decrypt](https://decrypt.co/370706/google-new-open-model-generates-text-diffusiongemma)).
- Cronaca del 2026 · Lo scafo delle serie. Mistral AI (15 ottobre 2026), [Timestral](https://mistral.ai/news/timestral/): quattro modelli da 5 a 209 milioni di parametri, 32.768 passi di storia, previsioni in quantili. La licenza esclude le aziende con più di 20 milioni di dollari di ricavi al mese ([analisi della licenza](https://medium.com/@andy.a.g/mistrals-timestral-forecasting-models-run-on-a-cpu-no-gpu-needed-649c75075558)).

## Lezione 14 · Dal dojo al mare
- J. Reason (1990), *Human Error*. Il modello del formaggio svizzero.
- S. Willison (2025), *The lethal trifecta for AI agents*. Le tre cose da non dare insieme a un agente.
- Cronaca del 2026 · Il modulo sul sito. Capsule Security (aprile 2026), ShareLeak in Microsoft Copilot Studio (CVE-2026-21520) e PipeLeak in Salesforce Agentforce ([CSO Online](https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html)).
- Cronaca del 2026 · Due facce della stessa capacità. Anthropic (giugno-luglio 2026): Claude Fable 5 per tutti e Mythos 5 per i partner della difesa informatica; la sospensione del 12 giugno per i controlli sulle esportazioni, revocati il 30 giugno; la nuova vedetta e il ritorno il 1° luglio ([Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5)). Le falle in PHP, annunciate il 20 ottobre 2026 e presenti dalla versione 5.4 del 2012 ([PHP2Shell](https://en.wikipedia.org/wiki/PHP2Shell)).
- Le navi spostate dai falsi segnali di posizione: nel giugno 2017, nel Mar Nero, una ventina di navi si sono viste sulle carte all'aeroporto di Gelendžik, a oltre 30 km nell'entroterra ([The War Zone](https://www.twz.com/13549/russia-may-be-testing-its-gps-spoofing-capabilities-around-the-black-sea), da un rapporto della US Maritime Administration).
