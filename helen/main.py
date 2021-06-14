'''Makenson Noel 
   June 14, 2021'''

#Python Libraries 
import time
import os

#Local time 
localtime = time.asctime( time.localtime(time.time()) )

#from me to you tag
from_me = '''\n\nTo: Helen Arlette Corrales\nFrom: Makenson Ilteus Noel''' 

#Instructions function
def instructions():
    print("\nPlease follow the prompted instructions, follow every typed submission with the enter sign\n\n\n")

#Error Message
def error():
    print("E R R O R R 1804, That hasn't been programmed yet . . . . \n")

#Main   
def welcome():
    while True:
        date = input("Enter todays date MM/DD/YYYY: \n\n--->")

        if date == "06/14/2021":
            june_14_2021()

            #question input
            q = input("Enter \"Yes\" to submit another date | Enter \"No\" to QUIT: \n")

            #if yes, display this message
            if q == "Yes" or q=="yes":
                welcome()

            # If no, display this message     
            elif q =="No" or "no":
                print("S E E  Y O U  S O O N\n\n") 
                break

            #Ouputs when an invalid answer is submitted 
            else:
                print("I N V A L I D, please Enter \"Yes\" to submit another date | Enter \"No\" to QUIT: \n")
                welcome()

        else:
            error()

#Functions for dates     
def june_14_2021():
    
    #File placement
    filename = (r'c:\Users\maken\OneDrive\Documents\apps\python\helen\june_14_2021.txt')

    #Special message
    message = ('''\nHey Babygirl, Happy Monthaversary
    \nI just wanted you to know that I appreciate you and I'm thankful that I met you ! (>^_^)> <(^_^<)
    \nIm thankful that you're in my life <3 \n\n ''')

    print ("File Created ")
    print(message)

    #Creates and writes in a file 
    file = open(filename, "a+")
    with open(filename, "w+") as file:
        file.write(message + "\nTime:" + localtime + from_me)
        file.close()

#instructions 
instructions()

#Compiler delay 
time.sleep(8)

#Clear compiler screen 
os.system('cls')

#RUN Main
welcome()