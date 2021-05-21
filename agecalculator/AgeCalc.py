""" Makenson I. Noel 
    April 4, 2021
    Happy Easter
    Happy Resurrection Day
    Develope With Mak """

"""This is an age calculator, will calculate and tell the user there age for 100 years"""

import math

#Function
def ageCalculator():
    #Age span
    SPAN = 100
    #Age at birth
    age = 0
    #Birth year input
    birthYear = int(input("Enter Birth Year: "))
   
    #while loop, while age is less than the year born, increment age and year until the target span 
    for age in range(SPAN):
        #age increment
        age += 1
        #year increment
        birthYear += 1
        print ("Your age is", age, "in the year ", birthYear)

print (ageCalculator())