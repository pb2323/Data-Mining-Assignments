# AutoMM for Named Entity Recognition

Google Colab Link - [https://colab.research.google.com/drive/11Pf7wcpNW_f8PNzMerJ-RgwFwUCQUrFL?usp=sharing](https://colab.research.google.com/drive/11Pf7wcpNW_f8PNzMerJ-RgwFwUCQUrFL?usp=sharing)

## Theory

Named Entity Recognition (NER) is a crucial task in Natural Language Processing (NLP) that involves identifying and classifying named entities in text into predefined categories like person names, organizations, locations, dates, etc. 

This Colab notebook demonstrates how to use AutoGluon's MultiModalPredictor for NER. AutoGluon automates the process of building high-performance deep learning models for various tasks, including NER. It leverages pre-trained models and advanced techniques like transfer learning to achieve excellent results.

## Usage

1. **Install necessary libraries:**

2. **Prepare your data:** Your data should be in a Pandas DataFrame with a text column and an annotation column containing entity information in JSON format.

3. **Train the model:**

4. **Evaluate and predict:**

## Example

The notebook provides a detailed example using the MIT movies corpus for training and evaluation. It also includes visualization using the `visualize_ner` function.