import csv
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
from sklearn import datasets

filename = "iris.csv"

iris = pd.read_csv('iris.csv')
#print(iris)
iris_columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']
iris['sl*sw'] = iris['sepal_length'] * iris['sepal_width']
iris['pl*pw'] = iris['petal_length'] * iris['petal_width']
iris['sl+sw'] = iris['sepal_length'] + iris['sepal_width']
iris['pl+pw'] = iris['petal_length'] + iris['petal_width']
iris['sl/sw'] = iris['sepal_length'] / iris['sepal_width']
iris_columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species', 'sl*sw', 'pl*pw', 'sl+sw', 'pl+pw', 'sl/sw']
#print(iris)
#def addColumnAddition(iris, newCol ,col1, col2, delim=', '):
    # this could use the cat function or simple additions
#    iris[newCol] = iris[col1] + delim + iris[col2] 

#addColumnAddition(iris, newCol='newCol',petal_length','petal_width')
    
    # I don't need to return df as it should be changed
    # but i am to allow chaining
#    return df
#iris.loc['4.6', 'setosa']


sys.stdout = open('output.txt','wt')
summary = iris.describe()
summary = summary.transpose()
summary.head()
print(summary)
print()
print(iris[iris_columns].head(10))
print()
mean = iris.groupby('species').mean()
print(mean)
print()
sum = iris.groupby('species').sum()
print(sum)

iris.to_excel('output.xlsx')

'''
def add_cols(iris, iris_columns):
    filename = "iris.csv"
    iris = pd.read_csv('iris.csv')
    iris_columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species', 'sl*sw', 'pl*pw', 'sl+sw', 'pl+pw']
    iris['sl/sw'] = iris['sepal_length'] / iris['sepal_width']
    #iris['pl/pw'] = iris['petal_length'] / iris['petal_width']
    #iris['sl-sw'] = iris['sepal_length'] - iris['sepal_width']
    #iris['pl-pw'] = iris['petal_length'] - iris['petal_width']
    iris_columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species', 'sl*sw', 'pl*pw', 'sl+sw', 'pl+pw', 'sl/sw']
    sys.stdout = open('output.txt','wt')
    summary = iris.describe()
    summary = summary.transpose()
    summary.head()
    print(summary)
    print()
    print(iris[iris_columns].head(10))

add_cols(iris, iris_columns)
'''
#with open("sepal_length.txt", "wt") as f:
#    print(iris_columns['sepal_length'])

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

iris = sns.load_dataset("iris")

ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.savefig('scatterplot.png')
plt.show()
plt.close()