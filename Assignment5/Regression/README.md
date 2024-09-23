# Regression - Gold Price Prediction using PyCaret

This Colab notebook demonstrates how to use the PyCaret library to predict Gold prices.

Colab - [https://colab.research.google.com/drive/1hBMCHIlIOEpD4ldeEa7YRDcu_sR4oX6f?usp=sharing](https://colab.research.google.com/drive/1hBMCHIlIOEpD4ldeEa7YRDcu_sR4oX6f?usp=sharing)

Youtube link - [https://www.youtube.com/watch?v=Ice6Rlj8QcE](https://www.youtube.com/watch?v=Ice6Rlj8QcE)

Timestamps for this colab - (2:57 to 6:18)


## Installing PyCaret

`bash !pip install pycaret` 

`!pip install pycaret[full]`

* Installs the PyCaret library.
* Installs the full version of PyCaret with all dependencies.

## Loading the Dataset

`python from pycaret.datasets` 

`import get_data data = get_data('gold')`

* Imports the regression module from PyCaret.
* Initializes the PyCaret environment for regression.
* Sets 'Gold\_T+22' as the target variable for prediction.
* Sets a random seed for reproducibility.

## Comparing Models

`python best = compare_models()`

* Compares various regression models to evaluate performance.
* Selects the best-performing model based on metrics.

## Creating and Analyzing the Model

* Creates a LightGBM regression model.
* Visualizes the residuals of the model.
* Plots the error distribution of the model.
* Displays the feature importance plot.
* Opens an interactive window for detailed model evaluation.

## Making Predictions

* Predicts on the held-out test set.
* Creates a copy of the original data and removes the target variable.
* Predicts on the new dataset without the target variable.

## Saving and Loading the Model

* Saves the trained model pipeline for future use.
* Loads the saved model pipeline.