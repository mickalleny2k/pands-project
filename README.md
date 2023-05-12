# pands-project

# Project for Programming and Scripting course
Analyse the Fisher's Iris data set

# Introduction : 
Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in 1936, as an example of linear discriminant analysis i.e. a method used in statistics to find a linear combination of features that characterizes or separates two or more classes of objects or events. In this study, Fisher wished to investigate if the species of an Iris flower could be identified by examining its petal and sepal length and width.

# Purpose of Task
Analyse the Iris Fisher Data Set
Write a program called analysis.py that:
1. Outputs a summary of each variable to a single text file,
2. Saves a histogram of each variable to png files, and
3. Outputs a scatter plot of each pair of variables.
4. Performs any other analysis you think is appropriate

# Installation
Run the python program analysis.py in Visual Studio Code
![Screenshot](installation.PNG)

# PROGRAMMING AND SCRIPTING PROJECT : OUTPUT TEXT FILE
## 5 COLUMNS
There are 5 columns in the original iris.csv file: 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'

## 9 COLUMNS
I added 4 more columns : 'sl*sw', 'pl/pw', 'sl+sw', 'pl-pw'
'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species', 'sl*sw', 'pl/pw', 'sl+sw', 'pl-pw'
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html

## PETAL LENGTH DIVIDED BY PETAL WIDTH
I printed the first 5 rowns in the column
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html

## "Data Shape : Numbers of rows and columns
There are 150 columns and 9 rows.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html

## ROWS 65 to 70
I only printed rows 65 to 70.
All other rows were ignored.
https://realpython.com/python-print/

# Histograms

Saves a histogram of each variable to png files

![Screenshot](Histograms.png)

# Scatterplot

Saves a scatterplot of each variable to png files

![Screenshot](scatterplot.png)


# Research
- https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
- https://github.com/gabrielmulligan/fishersirisdataset/blob/master/fisher_scatterplot.py
- https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
- https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
- https://www.geeksforgeeks.org/python-pandas-dataframe-columns/
- https://realpython.com/python-print/
- https://stackoverflow.com/questions/43772362/how-to-print-a-specific-row-of-a-pandas-dataframe
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html

