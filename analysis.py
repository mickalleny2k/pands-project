import csv
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
from sklearn import datasets
import re
import fileinput
import random

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

sys.stdout = open('output.txt','wt')
summary = iris.describe()
summary = summary.transpose()
summary.head()
print("                                         SUMMARY OF DATA : ")
print(summary)
print()

# https://github.com/gabrielmulligan/fishersirisdataset/blob/master/fisher_scatterplot.py
# print a statistical summary by Species
# Firstly, define each species in the dataset i.e. how Python knows which of the three Iris varieties it is
setosa =iris[iris['species']=='setosa']
versicolor =iris[iris['species']=='versicolor']
virginica =iris[iris['species']=='virginica']

# print a statistical summary using the describe function
print ("")
print ("                            Summary Statistical Analysis - Iris Setosa")
print(setosa.describe())
print ("")
print ("                            Summary Statistical Analysis - Iris Versicolor")
print(versicolor.describe())
print ("")
print ("                            Summary Statistical Analysis - Iris Virginica")
print(virginica.describe())
print ("")

print("                                         THE FIRST 10 ROWS : ")
print(iris[iris_columns].head(11))
print()
print("                                         THE LAST 10 ROWS : ")
print(iris[iris_columns].tail(10))
print()
print("                                         RANDOM SAMPLE OF 10 ROWS : ")
print(iris.sample(10))
print()
mean = iris.groupby('species').mean()
print("                                         THE MEAN OF EACH SPECIES : ")
print(mean)
print()
std = iris.groupby('species').std()
print("                                         THE STANDARD DEVIATION OF EACH SPECIES : ")
print(std)
print()
median = iris.groupby('species').median()
print("                                         THE MEDIAN OF EACH SPECIES : ")
print(median)
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
sum = iris['sepal_length'].sum()
print("THE SUM TOTAL OF SEPAL LENGTH COLUMN : ")
print(sum)
sum = iris['sepal_width'].sum()
print("THE SUM TOTAL OF SEPAL WIDTH COLUMN : ")
print(sum)
sum = iris['petal_length'].sum()
print("THE SUM TOTAL OF PETAL LENGTH COLUMN : ")
print(sum)
sum = iris['petal_width'].sum()
print("THE SUM TOTAL OF PETAL WIDTH COLUMN  : ")
print(sum)
print()
print("                                         ROWS 140 - 150 : ") 
print(iris.iloc[146:151])
#print(iris.iloc[:-4])
print()
print("                                         ROWS 75 - 80 : ")
print(iris.loc[75:80])
#iris.replace(to_replace='setosa', value='asotes')
#iris.replace(to_replace='setosa', value='new', regex=True)
iris.replace({'species':'setosa'}, {'species': 'rose'}, inplace=True, regex=True)
print()
print(" REPLACE SETOSA WITH ROSE IN THE SPECIES COLUMN")
print(" CHANGE BACK TO SETOSA  : ")
print(iris["species"].head(5))
iris.replace({'species':'rose'}, {'species': 'setosa'}, inplace=True, regex=True)
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
    list = valuesWithDelims.tolist()
    print("                     SORTED LIST OF UNIQUE VALUES : ")
    print(list)
    random.shuffle(list)
    print("                     RANDOM SHUFFLED LIST OF UNIQUE VALUES : ")
    print(list)
#    print(iris[nameOfCol].dropna().unique())
print()
print()
print("                   SERIES OF UNIQUE SORTED VALUES FOR SEPAL LENGTH : ")
getUnique(iris, nameOfCol='sepal_length', delim = ',')
print()
print()
print("                   SERIES OF UNIQUE SORTED VALUES FOR SEPAL WIDTH : ")
getUnique(iris, nameOfCol='sepal_width', delim = ',')
print()
print()
print("                    SERIES OF UNIQUE SORTED VALUES FOR PETAL LENGTH : ")
getUnique(iris, nameOfCol='petal_length', delim = ',')
print()
print()
print("                    SERIES OF UNIQUE SORTED VALUES FOR PETAL WIDTH : ")
getUnique(iris, nameOfCol='petal_width', delim = ',')

def ColumnAddition(iris, newCol ,col1, col2, delim=', ', index=False):
    iris[newCol] = iris[col1] + iris[col2] 
    print(f"{iris[newCol].head(10)}")
    return iris[newCol]
print()
print("COLUMN ADDITION ")
print("SEPAL LENGTH + SEPAL WIDTH ")
ColumnAddition(iris, newCol='SL + SW', col1='sepal_length', col2='sepal_width', delim=', ', index=False)
print()
print("COLUMN ADDITION ")
print("PETAL LENGTH + PETAL WIDTH")
ColumnAddition(iris, newCol='PL + PW', col1='petal_length', col2='petal_width', delim=', ', index=False)

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


iris = sns.load_dataset("iris")
iris.head()
sns.pairplot(data = iris)
sns.pairplot(iris, hue="species", palette="rainbow")
plt.savefig('pairplot.png')
plt.show()
plt.close()

# YOUR CODE HERE


