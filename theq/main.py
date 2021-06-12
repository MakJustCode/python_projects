"""
Makenson Noel 
June 11, 2021
A python program to illustrate a Queue system 
""" 

import time 
import os

def welcome():
    print("Welcome to the Queue \n\n")
    print("File Created\n\n")

def queue():
    name = input("\nEnter name: ")

    localtime = time.asctime( time.localtime(time.time()) )

    print("Name:", name, "\nTime:", localtime)

    filename = (r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\theq\testpage.txt")


    print ("Added to the Queue ")

    file = open(filename, "a+")

    with open(filename, "w+") as file:
        file.write("Name:"+ name + "\nTime:" + localtime)
        file.close()

    f = [5]
    


    answer = input("\nPress X to enter name: ")
    os.system('cls')

    while answer == 'x' or answer == 'X':
        queue()

welcome()

while True:
    queue() 
