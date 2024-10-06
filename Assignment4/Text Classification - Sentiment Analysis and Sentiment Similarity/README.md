# AutoMM for Text - Quick Start

This Colab demonstrates the use of AutoGluon's MultiModalPredictor for text-based tasks. It covers two common NLP problems: Sentiment Analysis and Sentence Similarity.

Google Colab Link - [https://colab.research.google.com/drive/1qNwednBn9Mb2n8EbrDh7LmAyDeUpyCPO?usp=sharing](https://colab.research.google.com/drive/1qNwednBn9Mb2n8EbrDh7LmAyDeUpyCPO?usp=sharing)

## Theory

**Sentiment Analysis:** This involves classifying text based on the sentiment it expresses (e.g., positive, negative, neutral).  It leverages Natural Language Processing (NLP) techniques to understand the meaning and emotional tone behind text data. Various approaches exist, including lexicon-based methods and deep learning models like recurrent neural networks (RNNs) and transformers.

**Sentence Similarity:**  This task focuses on quantifying the semantic similarity between two sentences. Techniques like cosine similarity between word embeddings or more advanced methods like Siamese networks and BERT-based models are used. The goal is to determine how closely two sentences relate in terms of meaning.

## Implementation

This Colab uses AutoGluon's `MultiModalPredictor`, which automatically selects and fine-tunes deep learning models for text prediction. It integrates with libraries like `timm`, `huggingface/transformers`, and `openai/clip`.

## Usage

1. **Install:** Install the necessary libraries using `!pip install autogluon.multimodal`.
2. **Load Data:** Load your text data as a Pandas DataFrame.
3. **Train:** Create a `MultiModalPredictor` instance and call `fit()` to train the model.
4. **Evaluate:** Use `evaluate()` to assess the model's performance on test data.
5. **Predict:** Utilize `predict()` to obtain predictions for new text inputs.

## Examples

The Colab provides detailed examples for Sentiment Analysis using the Stanford Sentiment Treebank (SST) dataset and Sentence Similarity using the Semantic Textual Similarity Benchmark (STS) dataset.
