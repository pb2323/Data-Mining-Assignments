# AutoMM for Text - Multilingual Problems

This Colab notebook demonstrates how to use AutoGluon's MultiModalPredictor for multilingual text classification tasks. 

Google Colab Link - [https://colab.research.google.com/drive/1nMU6gpSSPqfBwH2Tj9pLQsknpoZYJip2?usp=sharing](https://colab.research.google.com/drive/1nMU6gpSSPqfBwH2Tj9pLQsknpoZYJip2?usp=sharing)

## Theory

**Multilingual Natural Language Processing (NLP)** deals with enabling computers to understand and process information in multiple languages.  Traditional approaches involved training separate models for each language. However, recent advancements in **cross-lingual transfer learning** have made it possible to train models that can generalize across languages.

**AutoGluon** simplifies this process by providing the `MultiModalPredictor` which automatically leverages state-of-the-art techniques like:

* **Large-scale multilingual pretraining:** Models like XLM-R and DeBERTa-V3 are trained on massive multilingual datasets, allowing them to learn universal language representations.
* **Parameter-efficient finetuning:** This technique allows for adapting a pretrained model to a specific task with minimal changes to the model's parameters, making it more efficient for multilingual tasks.
* **Zero-shot transfer:** By training on a resource-rich language like English, these models can often be applied directly to other languages without any further training.

## Usage

This notebook demonstrates two key approaches:

1. **Finetuning a language-specific BERT model:** A German BERT model is fine-tuned for sentiment classification on German Amazon reviews.
2. **Cross-lingual transfer:** A model trained on English Amazon reviews is used to predict sentiment on German and Japanese reviews, demonstrating zero-shot transfer capabilities.

## Dataset

The [Cross-Lingual Amazon Product Review Sentiment](https://webis.de/data/webis-cls-10.html) dataset is used for this demonstration. It contains product reviews in English, German, French, and Japanese.

## Results

The notebook presents the accuracy scores achieved by the different approaches on the respective test sets.

## Conclusion

AutoGluon's MultiModalPredictor enables easy and effective multilingual text classification. By leveraging cross-lingual transfer learning, it's possible to build models that perform well across languages.