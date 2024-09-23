# PyCaret Classification Tutorial

This Colab notebook demonstrates how to use PyCaret for classification. 

Colab - [https://colab.research.google.com/drive/1Pu8eiM--kXQqpu_iGUl_QvzMT7Pcmf4s?usp=sharing](https://colab.research.google.com/drive/1Pu8eiM--kXQqpu_iGUl_QvzMT7Pcmf4s?usp=sharing)

Youtube link - [https://www.youtube.com/watch?v=Ice6Rlj8QcE](https://www.youtube.com/watch?v=Ice6Rlj8QcE)

Timestamps for this colab - (0:00 to 2:55)

It covers the following steps:

**1. Installation:**

- Install PyCaret with the `mlops` extra: `bash !pip install pycaret[mlops]`

**2. Data Loading:**

- Load the `wine` dataset from PyCaret's dataset module: `python from pycaret.datasets import get_data data = get_data('wine')`

**3. Setup:**

- Initialize the setup using `pycaret.classification.setup`: `python from pycaret.classification import * s = setup(data, target = 'type', session_id = 123)`

**4. Compare Models:**

- Compare baseline models using `compare_models`: `python best = compare_models()`

**5. Analyze Model:**

- Analyze the best model using various plots like confusion matrix, AUC, and feature importance using `plot_model`:`python plot_model(best, plot = 'confusion_matrix') plot_model(best, plot = 'auc') plot_model(best, plot = 'feature')`

**6. Prediction:**

- Predict on the test set using `predict_model`:`python holdout_pred = predict_model(best)`

**7. Save Model:**

- Save the trained model pipeline using `save_model`:`python save_model(best, 'wine_type_prediction_model')`

**8. Load Model:**

- Load the saved model pipeline using `load_model`:`python loaded_best_pipeline = load_model('wine_type_prediction_model')`

This notebook provides a comprehensive overview of using PyCaret for multiclass classification tasks. You can explore the detailed function-by-function overview in the notebook for a deeper understanding of each step.