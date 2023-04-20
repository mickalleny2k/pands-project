import csv
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
from sklearn import datasets

filename = "iris.csv"

iris = pd.read_csv('iris.csv')
iris.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

sys.stdout = open('output.txt','wt')
summary = iris.describe()
summary = summary.transpose()
summary.head()
print(summary)

iris= datasets.load_iris()

fig, axes = plt.subplots(nrows= 2, ncols=2)
colors= ['blue', 'red', 'green']

for i, ax in enumerate(axes.flat):
    for label, color in zip(range(len(iris.target_names)), colors):
        ax.hist(iris.data[iris.target==label, i], label=             
                            iris.target_names[label], color=color)
        ax.set_xlabel(iris.feature_names[i])  
        ax.legend(loc='upper right')
        plt.savefig('Histogram.png')

plt.show()
plt.close()