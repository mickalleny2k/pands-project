# Author : Michael Allen
# Analysis of Fisher's Iris Data Set
#The program:
#1.Outputs a summary of each variable to a single text file, 
#2. Saves a histogram of each variable to png files, and 
#3. Outputs a scatter plot of each pair of variables. 
#4. Performs any other analysis i think is appropriate

import csv
import numpy as np
import pandas as pd
import seaborn as sns
import sys

filename = "iris.csv"

iris_data = pd.read_csv('iris.csv')
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

'''with open(filename, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line)
'''
sys.stdout = open('output.txt','wt')
summary = iris_data.describe()
summary = summary.transpose()
summary.head()
print(summary)

#sys.stdout = open('output.txt','wt')

#pd.describe(csv_file)
#print(describe)

        