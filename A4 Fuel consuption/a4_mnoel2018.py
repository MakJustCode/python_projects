'''Makenson Noel 
   Fuel Consumption '''

import csv
import tuple
import matplotlib
import os

def error():
    print("E R R O R")

def mileage_info():
    print("Milage info ")

    mpg = input("\n\nEnter the MPG intevral that you're interested in: ")

    if mpg in range(1):
        print("Mak")


def trend_plot():
    print("Trend plot")

    options = input("At a minimum, offer 3 options: \n(H)ighway MPG \n(C)ity MPG \n(O)verall MPG")

    if options == "H":
        print("")

    elif options == "C":
        print("")

    elif options == "O": 
        print("")
    
    else:
        error()
    

    plot_produce = input("Enter the preferred way to produce the plot \n(D)isplay on screen \nsave to (F)ile")

    if plot_produce == "D":
        print("")

    elif plot_produce == "F":
        print("")

    else:
        error()

def main():

    option = int(input("Enter (1) for [Milage info] | Enter (2) to [Trend Plot] "))

    if option == 1:
        mileage_info()

    elif option == 2:
        trend_plot()

    else:
        main()

main() 

filename = (r'c:\Users\maken\OneDrive\Documents\apps\python\A4_Fuel_consumption\epadata2015.cvs')

#Macbook
#filename = (r') 



print(filename)