# AutoGluon Tabular Quick Start

This notebook provides a quick introduction to using AutoGluon's `TabularPredictor` for predicting values in tabular datasets.

Google Colab Link - [https://colab.research.google.com/drive/1k6u8i89YVumy0_0MWk7IZt5ZK7ov3xne?usp=sharing](https://colab.research.google.com/drive/1k6u8i89YVumy0_0MWk7IZt5ZK7ov3xne?usp=sharing)

Youtube Video - [https://www.youtube.com/watch?v=_usbhcK18gI](https://www.youtube.com/watch?v=_usbhcK18gI)

## Theory

**AutoGluon** is an open-source AutoML (Automated Machine Learning) library that aims to automate the process of developing high-performing machine learning models for various tasks, including tabular data prediction. 

**Tabular Data:** Data organized in rows and columns, similar to a spreadsheet or database table.

**Prediction Task:** Given a set of input features (columns in the table), the goal is to predict the value of a target column (also called the label).

**AutoML:** AutoML automates the process of selecting the best machine learning model, hyperparameter tuning, and feature engineering.

**How it works:**
1. **Data Loading:** AutoGluon uses `TabularDataset` to load and preprocess the data.
2. **Model Selection:** It automatically chooses from a variety of models like Random Forests, Gradient Boosting Machines, Neural Networks, etc.
3. **Hyperparameter Tuning:** AutoGluon tunes the hyperparameters of the selected models to optimize performance.
4. **Ensembling:** It combines the predictions from multiple models to improve accuracy and robustness.

## Usage

1. **Installation:**

2. **Data Preparation:** Load your data into a `TabularDataset`.
3. **Training:** Create a `TabularPredictor` and call `fit()` to train models.
4. **Prediction:** Use `predict()` to make predictions on new data.
5. **Evaluation:** Use `evaluate()` to assess the performance of the predictor.
