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
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
iris = pd.read_csv('iris.csv')
sys.stdout = open('output.txt','wt')
print("             PROGRAMMING AND SCRIPTING PROJECT : OUTPUT TEXT FILE")
print()
print("5 COLUMNS")
print(iris.columns)
iris_columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']
iris['sl*sw'] = iris['sepal_length'] * iris['sepal_width']
iris['pl/pw'] = iris['petal_length'] / iris['petal_width']
iris['sl+sw'] = iris['sepal_length'] + iris['sepal_width']
iris['pl-pw'] = iris['petal_length'] - iris['petal_width']
#iris['sl/sw'] = iris[int('sepal_length')] ^ iris[int('sepal_width')]
iris_columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species', 'sl*sw', 'pl/pw', 'sl+sw', 'pl-pw']
print()
print("9 COLUMNS")
print(iris.columns)
#https://www.geeksforgeeks.org/python-pandas-dataframe-columns/
print()
print("PETAL LENGTH DIVIDED BY PETAL WIDTH")
print(iris["pl/pw"].head(5))
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
print()
print("Data Shape : Numbers of rows and columns")
print(iris.shape)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html
print()
print("ROWS 65 to 70")
print(iris[65:71])
#I only printed rows 65 to 70. All other rows were ignored. https://realpython.com/python-print/
print()
print("ROWS 100 to 105")
sliced_data=iris[100:106]
print(sliced_data)
# Print ROWS 100 to 105 All other rows were ignored.
print()
summary = iris.describe()
summary = summary.transpose()
summary.head()
#The following statistical data is calculated: count, mean, std, min, 25%, 50%, 75% and max Count : Number of rows Mean: Average Std: Standard Deviation 25% : Twenty Five percent 50% : Fifty percent 75% : Seventy five percent Min: Minimum Max : Maximum
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html?highlight=summary
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
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html?highlight=head#pandas.DataFrame.head
#I printed the head of the dataset to the ouput file. All other rows were ignored.
print()
print("                                         THE LAST 10 ROWS : ")
print(iris[iris_columns].tail(10))
#I printed the tail of the dataset to the ouput file. All other rows were ignored.
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail
print()
print("                                         RANDOM SAMPLE OF 10 ROWS : ")
print(iris.sample(10))
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html?highlight=sample#pandas.DataFrame.sample
#I printed a random sample of 10 rows. I called the pandas function sample()
print()
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html?highlight=groupby#pandas.DataFrame.groupby
mean = iris.groupby('species').mean()
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.mean.html?highlight=mean#pandas.core.groupby.DataFrameGroupBy.mean
print("                                         THE MEAN OF EACH SPECIES : ")
#I grouped the dataset by species and calculated the mean of each group.
print(mean)
print()
#I grouped the dataset by species and calculated the standard deviation of each group.
std = iris.groupby('species').std()
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.std.html?highlight=std#pandas.core.groupby.DataFrameGroupBy.std
print("                                         THE STANDARD DEVIATION OF EACH SPECIES : ")
print(std)
print()
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.median.html?highlight=median#pandas.core.groupby.DataFrameGroupBy.median
median = iris.groupby('species').median()
#I grouped the dataset by species and calculated the median of each group.
print("                                         THE MEDIAN OF EACH SPECIES : ")
print(median)
print()
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.max.html?highlight=max#pandas.core.groupby.DataFrameGroupBy.max
max = iris.groupby('species').max()
print("                                         THE MAX OF EACH SPECIES : ")
print(max)
#I grouped the dataset by species and calculated the maximum of each group.
print()
min = iris.groupby('species').min()
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.min.html?highlight=min#pandas.core.groupby.DataFrameGroupBy.min
print("                                         THE MIN OF EACH SPECIES : ")
print(min)
#I grouped the dataset by species and calculated the maximum of each group.
print()
sum = iris.groupby('species').sum()
#I grouped the dataset by species and calculated the sum of each group.
print("                                         THE SUM OF EACH SPECIES : ")
print(sum)
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.sum.html?highlight=sum#pandas.core.groupby.DataFrameGroupBy.sum
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
#https://stackoverflow.com/questions/43772362/how-to-print-a-specific-row-of-a-pandas-dataframe
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
#Use a for loop to count the total number of letters, characters, numbers in each line of the text file
# remove fileinput
with open("iris.csv") as f:
    for line in f:
        letters = len(re.findall('[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]', line))
        chars = len(re.findall('[?/:()%@#*<,]', line))
        numbers = len(re.findall('[0123456789]', line))
        #find all of the letters, characters, numbers in each line
        setosa = len(re.findall('setosa', line))
        versicolor = len(re.findall('versicolor', line))
        virginica = len(re.findall('virginica', line))
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
    iris['pl-pw'].to_excel(writer, sheet_name="pl-pw", index=False)

def getUnique(iris, nameOfCol, delim = ','):
    # drop na gets rid of the values in the series that have no value
    # this actually returns a numpy.ndarray
    valuesWithDelims = iris[nameOfCol].dropna().unique()
    print(valuesWithDelims)
    print("                     SERIES OF UNIQUE SORTED VALUES : ")
    valuesWithDelims.sort()
    print(valuesWithDelims)
    list = valuesWithDelims.tolist()
    print("                     SORTED LIST OF UNIQUE VALUES : ")
    print(list)
    random.shuffle(list)
    print("                     RANDOM SHUFFLED LIST OF UNIQUE VALUES : ")
    print(list) 

print()
print()
#print([iris['petal_length']])
print("                   SERIES OF UNIQUE UNSORTED VALUES FOR SEPAL LENGTH : ")
getUnique(iris, nameOfCol='sepal_length', delim = ',')
print()
print()
print("                   SERIES OF UNIQUE UNSORTED VALUES FOR SEPAL WIDTH : ")
getUnique(iris, nameOfCol='sepal_width', delim = ',')
print()
print()
print("                    SERIES OF UNIQUE UNSORTED VALUES FOR PETAL LENGTH : ")
getUnique(iris, nameOfCol='petal_length', delim = ',')
print()
print()
print("                    SERIES OF UNIQUE UNSORTED VALUES FOR PETAL WIDTH : ")
getUnique(iris, nameOfCol='petal_width', delim = ',')
#sortSeries(valuesWithDelims)

def ColumnAddition(iris, newCol ,col1, col2, delim=', ', index=False):
    iris[newCol] = iris[col1] + iris[col2] 
    print(f"{iris[newCol].head(10)}")
    return iris[newCol]
print()
def ColumnSubtraction(iris, newCol ,col1, col2, delim=', ', index=False):
    iris[newCol] = iris[col1] - iris[col2] 
    print(f"{iris[newCol].tail(10)}")
    return iris[newCol]
print("COLUMN ADDITION ")
print("SEPAL LENGTH + SEPAL WIDTH ")
ColumnAddition(iris, newCol='SL PLUS SW', col1='sepal_length', col2='sepal_width', delim=', ', index=False)
print()
print("COLUMN SUBTRACTION ")
print("PETAL LENGTH MINUS PETAL WIDTH")
ColumnSubtraction(iris, newCol='PL MINUS PW', col1='petal_length', col2='petal_width', delim=', ', index=False)

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

print()
print("Print all 150 original rows and 5 columns in the Iris Fisher dataset using a for loop")
#Print all 150 original rows and 5 columns in the Iris Fisher dataset using a for loop
with open("iris.csv") as f: #Opens Iris data set csv file in data folder
    for line in f:# loops through each line
        line = line.replace(',', '  ') #replaces comma with space, code from Mohamed Noor
        line = line.rstrip() #Removes nextline code on end, code from Mohamed Noor
        print(line.split(',')[:]) #Splits and Prints 
        #each line as a list, colon separates each item in
        # columns
    for column in f:
        print (f.read())


