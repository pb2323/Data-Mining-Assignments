# Clustering Credit Data with PyCaret

This Colab notebook demonstrates how to perform clustering analysis on the "Credit" dataset using the PyCaret library.

Colab - [https://colab.research.google.com/drive/1CyrB0-8RN-uVLBqRdE41kLqYMJjsUtfM#scrollTo=6fBTpzIkAca1](https://colab.research.google.com/drive/1CyrB0-8RN-uVLBqRdE41kLqYMJjsUtfM#scrollTo=6fBTpzIkAca1)

Youtube link - [https://www.youtube.com/watch?v=Ice6Rlj8QcE](https://www.youtube.com/watch?v=Ice6Rlj8QcE)

Timestamps for this colab - (6:20 to 9:36)

## Steps

1. **Install PyCaret:** Installs the PyCaret library with all dependencies.

2. **Load the Dataset:** Imports the `get_data` function from PyCaret and loads the 'mice' dataset.

3. **Set up the Clustering Experiment:** Initializes the PyCaret clustering environment and performs data preprocessing.

4. **Create a K-Means Clustering Model:** Creates a K-Means clustering model with default parameters.

5. **Assign Clusters to Data Points:** Assigns cluster labels to each data point in the dataset based on the K-Means model.

6. **Visualize the Clusters:** Generates a scatter plot to visualize the clusters formed by the K-Means model.

7. **Evaluate the Model:** Creates visualizations like elbow plot and silhouette plot to assess the optimal number of clusters and the quality of clusters. It also displays the evaluation metrics.

8. **Predict Clusters for New Data:** Predicts cluster labels for new or unseen data using the trained K-Means model.

9. **Save the Trained Model:** Saves the trained K-Means model as a pipeline for future use.