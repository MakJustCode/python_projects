"""Makenson I. Noel
    Monday, April 5th, 2021
    Develope With Mak"""


"""Created a program to display welcome and display the current date and time, also flip a coin"""

import datetime

time = datetime.datetime.now()

#Welcome Function
def welcome():

    name = input("Enter name: ")
    print ("Welcome,", name)
    print("Date: ", time.strftime("%A"), time) 

#Coin Flip Function 
def flipCoin():
    HEADS = 0
    TAILS = 1

    for i in range (0,1):
        if i == HEADS:
            print ("Coin flip result is: Heads")
        elif i == TAILS:
            print ("Coin flip result is: Tails")



#Output 
print(welcome()) 

print("\n\n\n", flipCoin())