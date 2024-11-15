# Datasets Analysis and Model Building: Tabular and Time Series Data Analysis

This project involves extensive Exploratory Data Analysis (EDA), data preprocessing, visualization, and model building on two popular Kaggle datasets. The aim is to apply data cleaning, clustering, anomaly detection, data imputation, feature engineering, and model training using AutoML tools, including ensemble models with AutoVIML.

## Project Structure

The project is divided into two main parts, each focusing on a different dataset type:
1. **Tabular Data with Diverse Types** - Analyzes a dataset containing various data types, such as NYC Taxi data or Airbnb data.
2. **Time Series Data** - Focuses on processing and analyzing time-dependent data.

## Datasets

1. **Tabular Data**: This dataset includes diverse data types and requires comprehensive preprocessing steps.
2. **Time Series Data**: Involves analysis of sequential data over time with focus on handling temporal dependencies.

## Steps Involved

Each dataset goes through the following phases:

### 1. Exploratory Data Analysis (EDA) and Visualization
- Conducted detailed EDA and visualizations to understand data distributions, trends, and anomalies.
- Utilized automated EDA tools, including Auto EDA and Auto DS, combined with manual insights for a comprehensive data overview.

### 2. Data Preprocessing and Cleaning
- Handled missing values, performed data imputation, and removed outliers.
- Processed features and selected the most relevant ones for model training.

### 3. Clustering and Anomaly Detection
- Applied clustering techniques to identify natural groupings in data.
- Detected and eliminated anomalies to improve model accuracy and reliability.

### 4. Feature Engineering and Selection
- Engineered features to enhance model performance and conducted feature selection for optimal results.

### 5. Model Building using AutoML
- Leveraged AutoVIML for automated machine learning, including ensemble model creation.
- Experimented with multiple models and ensembles to identify the best-performing model for each dataset.

## Repository Structure

- [`tabular_diverse.ipynb`](https://colab.research.google.com/drive/1ig7BbBY174IZqQb_x_mYei3nuPxv10tk?usp=sharing) - Notebook with all steps for the tabular dataset, including EDA, preprocessing, clustering, and model building. Open in [Google Colab](https://colab.research.google.com/drive/1ig7BbBY174IZqQb_x_mYei3nuPxv10tk?usp=sharing).
- [`timeSeries.ipynb`](https://colab.research.google.com/drive/16Sn9P4j1CI0oqbunxwZvxKDsCsZqbX4B?usp=sharing) - Notebook with all steps for the time series dataset, covering EDA, preprocessing, clustering, and model building. Open in [Google Colab](https://colab.research.google.com/drive/16Sn9P4j1CI0oqbunxwZvxKDsCsZqbX4B?usp=sharing).
- `README.md` - Project documentation.
- Additional supporting files and outputs.

## Requirements

- Python libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, AutoVIML, Auto EDA, Auto DS, and any other necessary dependencies.
- Ensure that `AutoVIML` and relevant AutoML packages are installed.


## Results
The final results include:

- Clustered Data: Insights into data groupings and anomalies.
- Imputed Data: Filled missing values for complete data integrity.
- Selected Features: Optimal features identified for model performance.
- ML Models: Various models trained using AutoVIML, with the best-performing models saved for each dataset.

