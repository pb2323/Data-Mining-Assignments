# Multimodal Data Tables with AutoGluon

This Colab notebook demonstrates how to train a multimodal ensemble using data that contains image, text, and tabular features with AutoGluon.

Google Colab Link - [https://colab.research.google.com/drive/1gzGS-oxX3qyH-LuFZ_0DKJ29ABYqzOtf?usp=sharing](https://colab.research.google.com/drive/1gzGS-oxX3qyH-LuFZ_0DKJ29ABYqzOtf?usp=sharing)

## Theory

**Multimodal learning** is a subfield of machine learning that aims to build models that can process and relate information from multiple modalities, such as images, text, and tabular data. This approach leverages the complementary information present in different modalities to improve the overall performance of the model.

**AutoGluon** is an open-source AutoML toolkit that automates the process of developing and deploying high-performance machine learning models. It supports various tasks, including tabular prediction, image classification, and object detection. In this notebook, we utilize AutoGluon's TabularPredictor to train a multimodal ensemble for the PetFinder dataset.

## Dataset

The **PetFinder dataset** provides information about shelter animals, including pictures, text descriptions, and tabular features like age, breed, and color. The goal is to predict the adoption rate of the animal, which is a multi-class classification problem.

## Approach

1. **Data Preparation:** Download and preprocess the PetFinder dataset, including handling image paths and text descriptions.
2. **Feature Metadata:** Construct a FeatureMetadata object to specify the types of features, including images and text.
3. **Hyperparameters:** Define the models to train using a predefined hyperparameter configuration for multimodal datasets.
4. **Training:** Fit a TabularPredictor using the prepared data, feature metadata, and hyperparameters.
5. **Evaluation:** Evaluate the performance of the trained model using a leaderboard.

## Usage

1. Open this notebook in Google Colab.
2. Run all the cells in the notebook to download the dataset, preprocess the data, train the model, and evaluate the results.

## Requirements

* Google Colab environment
* AutoGluon library
* GPU for training image and text models

## Note

* This notebook uses a sampled dataset for demonstration purposes. Training on the full dataset may require more computational resources.
* The performance of the model can be further improved by adjusting the hyperparameters and training for a longer time.