# Timegpt, tabula9 and relational deep learning

# TimeGPT and Tabular Project Colabs

This repository contains a series of Colab notebooks demonstrating various machine learning tasks using TimeGPT, Tabular, RDL, and RelBench. Each notebook has been tested, and all artifacts are checked into this repository. Additionally, a video presentation provides a walkthrough of each notebook’s purpose, code, and output. Below is a comprehensive explanation of each notebook to guide you through their functionalities and implementations.

## Table of Contents
1. [TimeGPT](#timegpt)
   - [TimeGPT Multivariate & Long Horizon Forecasting](https://colab.research.google.com/drive/182RoYBLd4BXIr4Z1PcmVqJjcUAuwi65E?usp=sharing)
   - [Fine-tune TimeGPT with Custom Data](https://colab.research.google.com/drive/182RoYBLd4BXIr4Z1PcmVqJjcUAuwi65E?usp=sharing)
   - [Anomaly Detection with TimeGPT](https://colab.research.google.com/drive/1FmoMB8MA8lhysqDzzk_05T7lT-PlNJoY?usp=sharing)
   - [Energy Forecasting with TimeGPT](https://colab.research.google.com/drive/1WVzOPRIyMsQNXOLv3dRxQ90ye8oRBKPr?usp=sharing)
   - [Bitcoin Price Prediction with TimeGPT](https://colab.research.google.com/drive/1DRluSFlycF7p4uIdkJdQCuDOwe3WO6_j?usp=sharing)
2. [Tabular](#tabular)
   - [Synthetic Data Generation for a Real Dataset](https://colab.research.google.com/drive/182RoYBLd4BXIr4Z1PcmVqJjcUAuwi65E?usp=sharing)
   - [Zero-shot Inference on Tabula Model](https://colab.research.google.com/drive/14FORPh5pcITRvnh-FjTCKUFdz-p6K7Xn?usp=sharing)
3. [RDL and RelBench](#rdl-and-relbench)
   - [Training a GNN-based Model for Tabular Prediction](https://colab.research.google.com/drive/1mkrDN7Gy71jWOdndiGF9728P3D55sbUH?usp=sharing)

---

## TimeGPT

### a) TimeGPT Multivariate & Long Horizon Forecasting
**Notebook:** `Multivariate_long_horizon.ipynb`

In this notebook, we use TimeGPT to forecast multiple time series over long horizons. Multivariate forecasting is essential for understanding relationships across several time-dependent variables. The notebook is structured as follows:
- **Data Preparation**: Import and preprocess a sample multivariate time series dataset.
- **Model Setup**: Configure TimeGPT for handling multivariate time series data.
- **Long Horizon Forecasting**: Set the forecasting range, enabling the model to predict further into the future.
- **Results Visualization**: Generate visualizations to analyze the forecasted results.

### b) Fine-tune TimeGPT with Custom Data
**Notebook:** `finetune.ipynb`

This notebook walks you through fine-tuning TimeGPT with your dataset, tailoring the model to perform optimally on a specific time series task. Fine-tuning improves prediction accuracy by training the model on data more similar to your application’s needs.
- **Loading Custom Data**: Upload and preprocess your data, ensuring compatibility with TimeGPT's input requirements.
- **Fine-tuning Process**: Run the fine-tuning process, where the model parameters adjust based on your data.
- **Evaluation**: Compare model predictions with actual values from your dataset to evaluate fine-tuning effectiveness.

### c) Anomaly Detection with TimeGPT
**Notebook:** `Anomaly_detection.ipynb`

In this notebook, we utilize TimeGPT to detect anomalies in time series data, identifying patterns or data points that deviate significantly from expected values.
- **Dataset Preparation**: Import and preprocess time series data.
- **Anomaly Detection Setup**: Configure TimeGPT’s anomaly detection settings to identify irregular patterns.
- **Visualization and Interpretation**: Visualize anomalies to understand when and why they occurred, aiding in root cause analysis for time series anomalies.

### d) Energy Forecasting with TimeGPT
**Notebook:** `Energy_forecasting.ipynb`

This notebook applies TimeGPT to predict energy demand, demonstrating its utility in forecasting applications where managing resources and demand is essential.
- **Energy Data Import**: Load a dataset containing energy usage over time.
- **Forecasting Model Configuration**: Set up TimeGPT for energy forecasting, configuring time intervals and data parameters.
- **Prediction Analysis**: Analyze the predictions, comparing them against historical data to evaluate forecast accuracy and potential energy-saving insights.

### e) Bitcoin Price Prediction with TimeGPT
**Notebook:** `Bitcoin_forecasting.ipynb`

Using TimeGPT, this notebook focuses on forecasting the price of Bitcoin. Due to the high volatility of cryptocurrencies, this application shows TimeGPT’s ability to handle complex, unpredictable data.
- **Data Import**: Load historical Bitcoin price data.
- **Model Training and Forecasting**: Set up TimeGPT to predict Bitcoin prices, adjusting model parameters for optimal performance in high-variance data.
- **Results Visualization**: Visualize forecast results, providing insights into potential price movements and market trends.

---

## Tabular

### a) Synthetic Data Generation for a Real Dataset
**Notebook:** `synthetic_data_for_a_real_data_set.ipynb`

This notebook demonstrates how to use Tabula to create synthetic data that resembles a real dataset. Synthetic data is beneficial for training models when original data is limited or sensitive.
- **Data Loading and Transformation**: Import a sample dataset and preprocess it.
- **Synthetic Data Generation**: Use Tabula’s functions to generate a new dataset with similar characteristics.
- **Comparison and Evaluation**: Compare the synthetic dataset to the original to ensure it retains relevant features without compromising sensitive information.

### b) Zero-shot Inference on Tabula Model
**Notebook:** `zero_shot_inference.ipynb`

This notebook performs zero-shot inference on a Tabula model, demonstrating the model’s predictive capabilities without specific training on the dataset. Zero-shot inference is valuable for rapid model deployment in new scenarios.
- **Model Setup**: Configure Tabula for zero-shot inference.
- **Data Input and Inference**: Input a dataset and observe predictions generated by the model.
- **Analysis**: Review model performance and determine how accurately it generalizes across unseen data.

---

## RDL and RelBench

### a) Training a GNN-based Model for Tabular Prediction
**Notebook:** `train_model.ipynb`

In this notebook, we use RelBench to train a Graph Neural Network (GNN)-based model for predicting outcomes in tabular data. GNNs are effective for data with relational structures, such as social networks or molecular structures.
- **Dataset Preparation**: Import and preprocess a tabular dataset for GNN-based prediction.
- **Model Training**: Train a GNN model using RelBench’s tools, adjusting hyperparameters to improve model performance.
- **Metric Evaluation**: Evaluate the model with various metrics, such as accuracy and F1-score, to assess its suitability for the prediction task.

---

## Instructions

1. **Setup and Run**: Each notebook is ready to be opened and executed in Google Colab. Begin by running setup cells to install any dependencies required.
2. **Artifacts and Demonstrations**: All artifacts, including outputs, are available in this repository for review. Each notebook includes cell outputs showcasing the results after execution.
3. **Video Presentation**: A video presentation accompanies this README, explaining the purpose and results of each notebook, with a detailed breakdown of the code, input data, and resulting output.

---
## Conclusion

This project showcases the versatility of TimeGPT, Tabular, and RelBench tools for handling time series and tabular data in various prediction and forecasting tasks.


