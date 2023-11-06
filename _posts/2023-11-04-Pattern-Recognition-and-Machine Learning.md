---
title: "Review of 'Pattern Recognition and Machine Learning'"
date: 2023-11-04T23:23:23+01:00
toc: false
categories:
  - review
tags:
  - "machine learning"
  - book
  - theory
---

<style>
.styled-table-am {overflow: auto; width: 100%;}
.styled-table-am table {
    border: 3px solid #F21368;
    border-collapse: collapse;
    border-spacing: 2px;
    text-align: left;
    width: 100%;
}
.styled-table-am th, .styled-table-am td {
    border: 3px solid #F21368;
    background-color: #000000;
    color: #FFFFFF;
    padding: 5px;
}
.styled-table-am th:first-child, .styled-table-am td:first-child {
    width: 200px;  /* Fixed width for the first column */
}
.styled-table-am th:nth-child(2), .styled-table-am td:nth-child(2) {
    width: 100%;  /* Set a large width for the second column */
}
</style>
<div class="styled-table-am" role="region" tabindex="0">
	<table>
		<thead>
		<tr>
			<th>Title</th>
			<th>Pattern Recognition and Machine Learning</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Author</td>
			<td>Bishop, Christopher M.</td>
		</tr>
		<tr>
			<td>Language</td>
			<td>English</td>
		</tr>
		<tr>
			<td>Subjects</td>
			<td>Algorithms / Machine learning / Statistics</td>
		</tr>
		<tr>
			<td>Media info</td>
			<td>Year: 2006 / Type: Book / Format: PDF</td>
		</tr>
		<tr>
			<td>Audience</td>
			<td>Undergraduates / Practictioners</td>
		</tr>
		<tr>
			<td>Description</td>
			<td>Book with exercises</td>
		</tr>
		<tr>
			<td>URLs<br></td>
			<td><a href="https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf" target="_blank">PDF</a><br><a href="https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/" target="_blank">Site</a></td>
		</tr>
		<tr>
			<td>Related URLs</td>
			<td></td>
		</tr>
		<tr>
			<td>License</td>
			<td></td>
		</tr>
		<tr>
			<td>Last checked</td>
			<td>02/11/2023</td>
		</tr>
		</tbody>
	</table>
</div>


From the book site:
>This leading textbook provides a comprehensive introduction to the fields of pattern recognition and machine learning. It is aimed at advanced undergraduates or first-year PhD students, as well as researchers and practitioners. No previous knowledge of pattern recognition or machine learning concepts is assumed. This is the first machine learning textbook to include a comprehensive coverage of recent developments such as probabilistic graphical models and deterministic inference methods, and to emphasize a modern Bayesian perspective. It is suitable for courses on machine learning, statistics, computer science, signal processing, computer vision, data mining, and bioinformatics. This hard cover book has 738 pages in full colour, and there are 431 graded exercises (with solutions available below). Extensive support is provided for course instructors.

The book covers a variety of algorithms and key concepts in the field of machine learning. Some of the algorithms and techniques discussed in the book include:

1. Linear and logistic regression
2. Neural networks
3. Support vector machines
4. Gaussian processes
5. Probabilistic graphical models
6. Variational inference
7. Hidden Markov models.

Additionally, the book presents a Bayesian perspective, which has become popular in the field of machine learning in recent years. The book also explains approximate inference algorithms that allow for quick responses in situations where exact ones are not feasible. Exercises are graded according to difficulty ranging from (★), which denotes a simple exercise taking a few minutes to complete, through to (★★★), which denotes a significantly more complex exercise.

It's also important to highlight what's missing and, principally, it concerns everything that falls under the umbrella of deep learning, which uses neural networks with multiple layers of processing to extract higher-level features from raw data. Some of the most important algorithms and architectures in this field include:

- Convolutional neural networks (CNNs):
  - Mainly used for computer vision tasks, such as image and video recognition.
  - Examples: LeNet, AlexNet, VGGNet, ResNet, GoogleNet/inception, MobileNets.
- Recurrent neural networks (RNNs):
  - Designed to work with sequences of data, such as time series or natural language.
  - Examples: LSTM (long short-term memory), GRU (gated recurrent units).
- Autoencoder:
  - Used for unsupervised learning of efficient encodings, dimensionality reduction, and feature learning.
  - Examples: Sparse autoencoder, denoising autoencoder, variational autoencoder (VAE).
- Generative adversarial networks (GANs):
  - Composed of two neural networks, the generator and the discriminator, which are trained simultaneously through an adversarial game. Used to generate data that resembles real data, such as images, videos, and music.
- Capsule neural networks (CapsNet):
  - An attempt to improve CNNs using "capsules" that preserve spatial information and improve the network's ability to recognize objects from different angles and positions.
- Memory-augmented neural networks (MANNs):
  - Combine RNNs with an external memory that the network can read and write, allowing the network to perform tasks that require understanding and reasoning.
  - Examples: NTM (neural Turing machines), DNC (differentiable neural computers).
- Transformers:
  - A type of architecture that uses attention mechanisms to improve the handling of data sequences, particularly influential in the field of natural language processing.
  - Examples: BERT, GPT (generative pre-trained transformer), T5, XLNet.

# Recensione di 'Pattern Recognition and Machine Learning'
Dal sito di pubblicazione del libro:
>Questo testo guida offre una introduzione completa ai campi del riconoscimento dei modelli e dell'apprendimento automatico. È rivolto a studenti universitari avanzati o a studenti di dottorato al primo anno, così come a ricercatori e professionisti. Non viene presupposta alcuna conoscenza precedente dei concetti di riconoscimento dei modelli o di apprendimento automatico. Questo è il primo libro di testo sull'apprendimento automatico che include una copertura completa di sviluppi recenti come i modelli grafici probabilistici e i metodi di inferenza deterministica, e che enfatizza una moderna prospettiva bayesiana. È adatto per corsi di apprendimento automatico, statistica, informatica, elaborazione dei segnali, visione artificiale, data mining e bioinformatica. Questo libro rilegato ha 738 pagine a colori, e ci sono 431 esercizi graduati (con soluzioni disponibili sotto). È fornito un ampio supporto per gli istruttori del corso.

Il libro copre una varietà di algoritmi e concetti chiave nel campo dell'apprendimento automatico. Alcuni degli algoritmi e delle tecniche discussi nel libro includono:

1. Regressione lineare e logistica
2. Reti neurali
3. Macchine a vettori di supporto
4. Processi gaussiani
5. Modelli grafici probabilistici
6. Inferenza variazionale
7. Modelli di Markov nascosti.

Inoltre, il libro presenta una prospettiva bayesiana, che è diventata popolare nel campo dell'apprendimento automatico negli ultimi anni. Il libro spiega anche algoritmi di inferenza approssimata che permettono risposte rapide in situazioni in cui quelle esatte non sono fattibili. Gli esercizi sono classificati secondo la difficoltà partendo da (★), che denota un esercizio semplice che richiede pochi minuti per essere completato, fino a (★★★), che indica un esercizio significativamente più complesso.

È importante sottolineare anche cosa manca e, principalmente, si tratta di tutto ciò che rientra nel novero dell'apprendimento profondo, che utilizza reti neurali con molteplici livelli di elaborazione per estrarre caratteristiche di livello superiore dai dati grezzi. Alcuni degli algoritmi e delle architetture più importanti in questo campo includono:

- Reti neurali convoluzionali (_convolutional neural networks_, CNNs):
	- Utilizzate principalmente per compiti di visione artificiale, come il riconoscimento di immagini e video.
	- Esempi: LeNet, AlexNet, VGGNet, ResNet, GoogleNet/inception, MobileNets.
- Reti neurali ricorrenti (_recurrent neural networks_, RNNs):
	- Progettate per lavorare con sequenze di dati, come serie temporali o linguaggio naturale.
	- Esempi: LSTM (_long short-term memory_), GRU (_gated recurrent units_).
- Codificatore automatico (_autoencoder_):
	- Utilizzati per l'apprendimento non supervisionato di codifiche efficienti, riduzione della dimensionalità e apprendimento di rappresentazioni.
	- Esempi: Autoencoder sparsi, Denoising Autoencoder, Variational Autoencoder (VAE).
- Reti neurali generative avversarie (_generative adversarial networks_, GANs):
	- Composte da due reti neurali, il generatore e il discriminatore, che vengono addestrate simultaneamente attraverso un gioco avversario. Utilizzate per generare dati che assomigliano a dati veri, come immagini, video, e musica.
- Reti neurali di capsule (_capsule neural network_, CapsNet):
	- Un tentativo di migliorare le CNN utilizzando "capsule" che conservano le informazioni spaziali e migliorano la capacità della rete di riconoscere oggetti da diverse angolazioni e posizioni.
- Reti neurali con memoria esterna (_memory-augmented neural networks_, MANNs):
	- Combinano RNN con una memoria esterna che la rete può leggere e scrivere, permettendo alla rete di compiere compiti che richiedono comprensione e ragionamento.
	- Esempi: NTM (_neural Turing machines_), DNC (_differentiable neural computers_).
- Trasformatori (_transformer_):
	- Un tipo di architettura che utilizza meccanismi di attenzione per migliorare il trattamento delle sequenze di dati, particolarmente influente nel campo del processamento del linguaggio naturale.
	- Esempi: BERT, GPT (_Generative Pre-trained Transformer_), T5, XLNet.