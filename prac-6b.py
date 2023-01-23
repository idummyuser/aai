from operator import methodcaller
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
print("Name - Pritesh Tayade - Roll No 15")
print("Un-supervised Learning Model")

customer_data = pd.read_csv(r"C:\Workspace\un-org\MScIT\Part-II-2022-23\Sem-3\Applied-Artificial-Intelligence\pracs\Pritesh\AIPracsProject\Mall_Customers.csv")
customer_data.shape
customer_data.head()
data = customer_data.iloc[:, 3:5].values

plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")

dend = shc.dendrogram(shc.linkage(data, method='ward'))

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)

plt.figure(figsize=(10, 7))
plt.scatter(data[:, 0], data[:,1], c = cluster.labels_, cmap = 'rainbow')
plt.show()
