'''Makenson Noel 
   Iris Dataset and dictionaries 
'''

def welcome():
    print("\nCreating a simple program for using dictionaries to store and process the contents of a very popular dataset, the Iris flower dataset.\n")

    print("The Iris flower dataset is one of the most popular datasets in human history. \nThe dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant: setosa, virginica, or versicolor. \nFor each sample, 4 attributes are stored: petal length, petal width, sepal length, and sepal width.\n\n")

import os
import csv
import pprint
#import numpy as np
filename = (r"c:\Users\maken\OneDrive\Documents\apps\python\A5\iris.csv")

def calculate_average(data_lines):
    # declare sum values for each species
    # first is petal length
    # second is petah width
    # third is sepal length
    # fourth is sepal width
    sum_attributes = {
        "setosa": [0, 0, 0, 0],
        "versicolor": [0, 0, 0, 0],
        "virginica": [0, 0, 0, 0]
    }

    counts = {
        "setosa": 0,
        "versicolor": 0,
        "virginica": 0
    }

    # read lines from data_lines
    for row in data_lines:
        species = row[-1] # get the species
        # add the columns
        sum_attributes[species][0] += float(row[2])
        sum_attributes[species][1] += float(row[3])
        sum_attributes[species][2] += float(row[0])
        sum_attributes[species][3] += float(row[1])
        # increase count
        counts[species] += 1
  
    # calculate and return a dict of averages
    averages = {
        species: [x / counts[species] for x in sum_attributes[species]] for species in sum_attributes
    }

    # return averages
    return averages

def pretty_print(averages):
    # pretty print function
    welcome()
    print('---------------------------------------------------------------------------------')
    print(f'{"Species":<20} {"Setosa":>10} {"Versicolor":>20} {"Virginica":>20}')
    print('---------------------------------------------------------------------------------')
    print("Attributes (cm):")
    print(f'{" Avg petal length:":<20} {averages["setosa"][0]:>10.2f} {averages["versicolor"][0]:>20.2f} {averages["virginica"][0]:>20.2f}')
    print(f'{" Avg petal width:":<20} {averages["setosa"][1]:>10.2f} {averages["versicolor"][1]:>20.2f} {averages["virginica"][1]:>20.2f}')
    print(f'{" Avg sepal length:":<20} {averages["setosa"][2]:>10.2f} {averages["versicolor"][2]:>20.2f} {averages["virginica"][2]:>20.2f}')
    print(f'{" Avg sepal width:":<20} {averages["setosa"][3]:>10.2f} {averages["versicolor"][3]:>20.2f} {averages["virginica"][3]:>20.2f}')
    print("\n\n")

# main script
# open file for reading
with open(filename, newline='') as dataFile:
    reader = csv.reader(dataFile)
    # skip the header line
    next(reader)
    data = []
    # add all data
    for row in reader:
        data.append(row)

# calculate averages
averages = calculate_average(data)
pretty_print(averages)