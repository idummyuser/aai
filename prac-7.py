#Write an application to implement Clusteringalgorithm.

from numpy import where
from sklearn.datasets import make_classification
from matplotlib import pyplot

# Define Dataset
x, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1,
                           random_state=4)

# Create scatter plot for samples from each class
for class_value in range(2):
    # Get row indexes for samples from each class
    row_ix = where(y == class_value)

    # Create scatter of these samples
    pyplot.scatter(x[row_ix, 0], x[row_ix, 1])

# Show the plot
pyplot.show()
