import csv
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
from sklearn import datasets
import re
import fileinput
#import dataManipulation

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

print(iris["sl/sw"].head(5))

'''
def addColumnAddition(iris, newCol, col1, col2, delim=', '):
    # this could use the cat function or simple additions
    iris[newCol] = iris[col1] + delim + iris[col2] 
    return iris

addColumnAddition(iris,"newCol",'petal_length','petal_width', delim=',')
print(iris.head(5))

addColumnAddition(iris, newCol='newCol',petal_length','petal_width')
    
    # I don't need to return df as it should be changed
    # but i am to allow chaining
    return iris
#iris.loc['4.6', 'setosa']
'''

sys.stdout = open('output.txt','wt')
summary = iris.describe()
summary = summary.transpose()
summary.head()
print("                                         SUMMARY OF DATA : ")
print(summary)
print()
print("                                         THE FIRST 10 ROWS : ")
print(iris[iris_columns].head(11))
print()
mean = iris.groupby('species').mean()
print("                                         THE MEAN OF EACH SPECIES : ")
print(mean)
print()
max = iris.groupby('species').max()
print("                                         THE MAX OF EACH SPECIES : ")
print(max)
print()
min = iris.groupby('species').min()
print("                                         THE MIN OF EACH SPECIES : ")
print(min)
print()
sum = iris.groupby('species').sum()
print("                                         THE SUM OF EACH SPECIES : ")
print(sum)
print()
print("                                         ROWS 146 - 151 : ") 
print(iris.iloc[146:151])
#print(iris.iloc[:-4])
print()
print("                                         ROWS 75 - 80 : ")
print(iris.loc[75:80])
#iris.replace(to_replace='setosa', value='asotes')
#iris.replace(to_replace='setosa', value='new', regex=True)
iris.replace({'species':'setosa'}, {'species': 'new'}, inplace=True, regex=True)
print()
print(" THE SPECIES COLUMN : ")
print(iris["species"].head(5))
iris.replace({'species':'new'}, {'species': 'setosa'}, inplace=True, regex=True)
print(iris["species"].head(5))
print()
print(" THE DATAFRAME SIZE : ")
print(f"The dataframe size is {iris.size}")
print()
print(" CROSS TABULATION : ")
print(pd.crosstab('species', ['sepal_length', 'petal_length']))
print()
col1and2 = ['sepal_length', 'sepal_width']
#print(iris[['sepal_length', 'sepal_width']].head(6)) 
print(" COLUMN 1 & 2 : ")
print(iris[col1and2].head(6))

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
print("                     TOTAL NUMBER OF .......")
print(f"The total number of letters contained in the iris.csv file is {number_of_letters}")
print(f"The total number of special characters contained in the iris.csv file is {number_of_chars}")
print(f"The total number of numbers contained in the iris.csv file is {number_of_numbers}")
print(f"The total number of setosa contained in the iris.csv file is {number_of_setosa}")
print(f"The total number of versicolor contained in the iris.csv file is {number_of_versicolor}")
print(f"The total number of virginica contained in the iris.csv file is {number_of_virginica}")

excel_file = "output.xlsx"
iris.to_excel('output.xlsx')
with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a") as writer:
    iris['petal_length'].to_excel(writer, sheet_name="petal_length", index=False)
with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a") as writer:
    iris['petal_width'].to_excel(writer, sheet_name="petal_width", index=False)
with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a") as writer:
    iris['pl+pw'].to_excel(writer, sheet_name="pl+pw", index=False)

def getUnique(iris, nameOfCol, delim = ','):
    # drop na gets rid of the values in the series that have no value
    # this actually returns a numpy.ndarray
    valuesWithDelims = iris[nameOfCol].dropna().unique() 
    valuesWithDelims.sort()
    print(valuesWithDelims)
#    print(iris[nameOfCol].dropna().unique())
print()
print("                   UNIQUE SORTED VALUES FOR SEPAL LENGTH : ")
getUnique(iris, nameOfCol='sepal_length', delim = ',')
print()
print("                   UNIQUE SORTED VALUES FOR SEPAL WIDTH : ")
getUnique(iris, nameOfCol='sepal_width', delim = ',')
print()
print("                    UNIQUE SORTED VALUES FOR PETAL LENGTH : ")
getUnique(iris, nameOfCol='petal_length', delim = ',')
print()
print("                    UNIQUE SORTED VALUES FOR PETAL WIDTH : ")
getUnique(iris, nameOfCol='petal_width', delim = ',')

def ColumnAddition(iris, newCol ,col1, col2, delim=', '):
    # this could use the cat function or simple additions
    iris[newCol] = iris[col1] + iris[col2] 
    
    # I don't need to return df as it should be changed
    # but i am to allow chaining
    print(f"{iris[newCol].head(10)}")
    return iris[newCol]
print()
print("SEPAL LENGTH + SEPAL WIDTH")
ColumnAddition(iris, newCol='SL + SW', col1='sepal_length', col2='sepal_width', delim=', ')
print()
print("PETAL LENGTH + PETAL WIDTH")
ColumnAddition(iris, newCol='PL + PW', col1='petal_length', col2='petal_width', delim=', ')
'''
def getSeriesOfUnique(iris, nameOfCol, delim = ','):
    # drop na gets rid of the values in the series that have no value
    # this actually returns a numpy.ndarray
    valuesWithDelims = iris[nameOfCol].dropna().unique()
    print(iris[nameOfCol].dropna().unique())

getSeriesOfUnique(iris, nameOfCol='sepal_length', delim = ',')
getSeriesOfUnique(iris, nameOfCol='sepal_width', delim = ',')
getSeriesOfUnique(iris, nameOfCol='petal_length', delim = ',')
getSeriesOfUnique(iris, nameOfCol='petal_width', delim = ',')
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