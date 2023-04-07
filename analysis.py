# Author : Michael Allen
# Analysis of Fisher's Iris Data Set
#The program:
#1.Outputs a summary of each variable to a single text file, 
#2. Saves a histogram of each variable to png files, and 
#3. Outputs a scatter plot of each pair of variables. 
#4. Performs any other analysis i think is appropriate

import csv

filename = "fishers_iris_dataset.csv"

with open(filename, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line)

        