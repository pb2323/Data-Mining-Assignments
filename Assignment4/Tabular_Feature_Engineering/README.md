# Automatic Feature Engineering with AutoGluon

This Colab notebook demonstrates how to use AutoGluon's automatic feature engineering capabilities for tabular data.

Google Colab Link - [https://colab.research.google.com/drive/14t6k7Gy_eNGHynLCygpuYprJ45dk-kD0?usp=sharing](https://colab.research.google.com/drive/14t6k7Gy_eNGHynLCygpuYprJ45dk-kD0?usp=sharing)

## Theory

**Feature engineering** is the process of transforming raw data into features that are more suitable for machine learning models. It can involve tasks such as:

* **Handling missing values:** Replacing missing values with a suitable value, such as the mean or median.
* **Encoding categorical features:** Converting categorical features into numerical representations that can be used by machine learning models.
* **Creating new features:** Deriving new features from existing ones, such as interactions between features or aggregations of features.

**AutoGluon** automates many of these feature engineering tasks, making it easier to build high-performing machine learning models.

## Code Overview

The notebook uses the `autogluon.tabular` module to perform automatic feature engineering.

1. **Data Preparation:**
   - We first create a sample dataset using `make_regression` from `sklearn.datasets`.
   - We then add different types of features (integer, datetime, categorical, and string) to the dataset.

2. **Automatic Feature Generation:**
   - We use `AutoMLPipelineFeatureGenerator` to automatically generate features from the dataset.
   - This generator applies a series of transformations to the data, such as encoding categorical features and handling missing values.

3. **Model Training:**
   - We use `TabularPredictor` to train a machine learning model on the engineered features.
   - We specify the label column and the hyperparameters for the model.

4. **Customization:**
   - We show how to customize the feature engineering process by using a custom `PipelineFeatureGenerator`.
   - This allows you to control the specific transformations that are applied to the data.

## Usage

To use this notebook, simply run the code cells in order. You can modify the code to experiment with different datasets and feature engineering options.