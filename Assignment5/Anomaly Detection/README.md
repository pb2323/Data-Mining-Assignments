# Anomaly Detection with PyCaret

This notebook demonstrates how to perform anomaly detection using the PyCaret library.

Colab - [https://colab.research.google.com/drive/1W2m4ja_J-x5esOU3gCfmA5mIvKMJy6MP?usp=sharing](https://colab.research.google.com/drive/1W2m4ja_J-x5esOU3gCfmA5mIvKMJy6MP?usp=sharing)

Youtube link - [https://www.youtube.com/watch?v=Ice6Rlj8QcE](https://www.youtube.com/watch?v=Ice6Rlj8QcE)

Timestamps for this colab - (9:38 to 12:08)

## Steps

1. **Install PyCaret:**
This installs the PyCaret library with all its dependencies. PyCaret is an open-source, low-code machine learning library that helps automate machine learning workflows.

2. **Import Libraries:**
* `from pycaret.datasets import get_data`: Imports the `get_data` function, used to load datasets from PyCaret's repository.
* `from pycaret.anomaly import *`: Imports all modules and functions from the `anomaly` sub-package for anomaly detection tasks.
* `from pycaret.anomaly import AnomalyExperiment`: Imports the `AnomalyExperiment` class for creating an anomaly detection experiment.


3. **Load Dataset:**
Loads the 'anomaly' dataset from PyCaret's repository.

4. **Setup PyCaret Environment:**
* `session_id = 123`: Sets a seed for reproducibility, ensuring consistent results across different runs.
* `exp = AnomalyExperiment()`: Initializes an `AnomalyExperiment` object.
* `exp.setup(data, session_id = session_id)`: Prepares the environment for anomaly detection by setting up the experiment with the loaded dataset and session ID.

5. **Create Isolation Forest Model:**
Creates an Isolation Forest model. Isolation Forest is an unsupervised anomaly detection algorithm that isolates anomalies by randomly partitioning the data.

6. **Assign Model for Anomaly Detection:**
Assigns the created Isolation Forest model to the dataset, adding an 'Anomaly' column with labels (0 for normal data points and 1 for anomalies).

7. **Visualize Anomalies:**
Generates a t-SNE (t-distributed Stochastic Neighbor Embedding) plot to visualize the anomalies identified by the model.

8. **Evaluate Model:**
Displays an interactive dashboard with various plots to evaluate the performance of the Isolation Forest model.

9. **Make Predictions:**
Uses the trained Isolation Forest model to predict anomalies on the provided dataset, returning a dataframe with predictions.

10. **Save Model:** -
Saves the trained Isolation Forest model as a pipeline for future use, allowing you to load and reuse the model without retraining.