"""
Makenson Noel 
May 26, 2021



"""

import csv
#A python program to illustrate Caesar Cipher Technique

alphabet = "abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Encryption algorithm 
def encrypt(text, key):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    #
    return result

# Decryption algorithm 
def decrypt(text, key):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - key - 65) % 26 + 65)
 
        # Decrypt lowercase characters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)

    #
    return result

def output_phase():


    # Input 
    a_str = str(input("Enter A to submit another phase, key, and to choose the option to encrypt or decrypt | Enter X to quit: "))

    # Phase, Key, Encrypt/Decrypt 
    if a_str == "A" or a_str=="a":
        run() 

    # Exit Function 
    elif a_str == "X" or a_str == "x":
        print("Q U I T T I N G . . .")
        exit() 

    # Error Message    
    else:
        print("E R R O R")
        output_phase()

def run():

    # 
    text = str(input("Enter phrase (upper and lower case letters only, no spaces, punctuation symbols, or other characters): "))

    #Insert character check 
    for text in range(alphabet):
        key = int(input("Enter Key: "))
        print ("Text  : " + text)
        print ("Shift : " + str(key))

        answer_str = str(input("Enter E for Encrypt or D for Decrypt: "))

        if answer_str == "E" or answer_str == "e":
            print ("Cipher: " + encrypt(text,key))

        elif answer_str == "D" or answer_str == "d": 
            print ("Cipher: " + decrypt(text,key))

        else: 
            print("E R R O R .. Refreshing")
            run() 

    output_phase()


"""def brute_force():
    A = []
    length = len(A)
    i = 0
    j = length - 1
    A.sort() 

    for i in range(length):
        for j in range(length):
            i = i + 1 
            j = j - 1"""

run() 
