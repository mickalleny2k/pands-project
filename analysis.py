import csv
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
from sklearn import datasets
import re
import fileinput

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
col1and2 = ['sepal_length', 'sepal_width']
#print(iris[['sepal_length', 'sepal_width']].head(6)) 
print(iris[col1and2].head(6))
print()
mean = iris.groupby('species').mean()
print(mean)
print()
sum = iris.groupby('species').sum()
print(sum)

number_of_letters = 0
number_of_chars = 0
number_of_numbers = 0
number_of_setosa = 0
number_of_versicolor = 0
number_of_virginica = 0
#output_file = 'output.txt'

#Research
#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
#Use a for loop to count the number of e's in each line of the text file

for line in fileinput.input():
    letters = len(re.findall('[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]', line))
    chars = len(re.findall('[?/:()%@#*<,]', line))
    numbers = len(re.findall('[0123456789]', line))
    setosa = len(re.findall('setosa', line))
    versicolor = len(re.findall('versicolor', line))
    virginica = len(re.findall('virginica', line))
    #find all of the e's and E's in each line
    number_of_letters = number_of_letters + letters
    number_of_chars = number_of_chars + chars
    number_of_numbers = number_of_numbers + numbers
    number_of_setosa = number_of_setosa + setosa
    number_of_versicolor = number_of_versicolor + versicolor
    number_of_virginica = number_of_virginica + virginica
    # Update the variable after each iteration of the loop

print()
print(f"The total number of letters contained in the iris.csv file is {number_of_letters}")
print(f"The total number of special characters contained in the iris.csv file is {number_of_chars}")
print(f"The total number of numbers contained in the iris.csv file is {number_of_numbers}")
print(f"The total number of setosa contained in the iris.csv file is {number_of_setosa}")
print(f"The total number of versicolor contained in the iris.csv file is {number_of_versicolor}")
print(f"The total number of virginica contained in the iris.csv file is {number_of_virginica}")

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