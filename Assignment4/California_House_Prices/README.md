# California House Price Prediction with AutoGluon

This Colab notebook demonstrates how to use AutoGluon to predict house prices using the California House Prices dataset from Kaggle.

Google Colab Link - [https://colab.research.google.com/drive/1WdsvV0G4jYTqpbt2RsqoiVtnulyCeF4h](https://colab.research.google.com/drive/1WdsvV0G4jYTqpbt2RsqoiVtnulyCeF4h)

Youtube Video - [https://www.youtube.com/watch?v=_usbhcK18gI](https://www.youtube.com/watch?v=_usbhcK18gI)

## Setup

1. Install necessary libraries: `bash !pip3 install kaggle autogluon`

2.  Set up Kaggle API credentials:
   - Upload your `kaggle.json` file to the Colab environment.
   - Move the file to the Kaggle directory and set permissions:

3. Download and unzip the dataset:

## Usage

1. Run the provided Python script `example_kaggle_house.py` with different configurations:

   - Single MultiModalPredictor (MLP):

   - Single MultiModalPredictor (FT-Transformer):

   - MultiModalPredictor with Bagging:

   - MultiModalPredictor with Weighted Ensemble:

   - MultiModalPredictor with Stack Ensemble:

2. View the results and logs generated in the `logs` directory.

## Notes

- This notebook uses AutoGluon for automated machine learning.
- Different configurations are used to explore different modeling approaches.
- Results are logged to text files for analysis.