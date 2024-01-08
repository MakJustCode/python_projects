"""
Makenson Noel 
June 8, 2021
A python program to illustrate Cryptography 
""" 
def welcome_message():
    print("\nWelcome to Cryptography \n\n")
    print("Cryptography is the practice and study of techniques for secure communication in the presence of third parties called adversaries.\n")
    print("The main classical cryptography methods are transposition ciphers\n")
    print("which rearrange the order of letters in a message and substitution ciphers,")
    print("\nwhich systematically replace letters or groups of letters with other letters or groups of letters.") 
    print("\nThe purpose of this app is to illustrate the Caesar Cipher Technique with text files\n\n")

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

    return result

def output_phase():

    # Input 
    a_str = str(input("\nEnter A to submit another file and to choose the option to encrypt or decrypt | Enter X to quit: "))

    # File Encrypt/Decrypt 
    if a_str == "A" or a_str=="a":
        run() 

    # Exit Function 
    elif a_str == "X" or a_str == "x":
        print("Q U I T T I N G . . .\n\n")
        exit() 

    # Error Message    
    else:
        print("E R R O R")
        output_phase()

def run():

    #text = str(input("\n(upper and lower case letters only, no spaces, punctuation symbols, or other characters) \n\nEnter phrase: "))

    option = (input("\n\nEnter Filename: "))

    if option == "encrypt_me.txt":

        tex = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\encrypt_me.txt", "a")
        tex.close()

        tex = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\encrypt_me.txt", "r" )
        text = tex.read().replace(" ", "")
        tex.close()

        print(text)

    elif option == "decrypt_me.txt":

        tex = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\decrypt_me.txt", "a")
        tex.close()

        tex = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\decrypt_me.txt", "r" )
        text = tex.read().replace(" ", "")
        tex.close()

        print(text)

    else:
        print("That File does not exist")
        run() 

    key = 3

    print ("\nText  : " + text)

    print ("Shift : " + str(key))

    answer_str = str(input("\nEnter E for Encrypt | Enter D for Decrypt: "))

    if answer_str == "E" or answer_str == "e":
        print ("Encrypted Cipher: " + encrypt(text,key))
        file = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\encrypt_me_enc.txt", "a")
        file.close()

        file = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\encrypt_me_enc.txt", "w")
        file.write("Encrypted Cipher: " + encrypt(text,key))
        file.close()

        option = option.replace(".txt", "_enc.txt")
        print("\n\n",option,"File successfully created")


    elif answer_str == "D" or answer_str == "d": 
        print ("Decrypted Cipher: " + decrypt(text,key))
        file = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\decrypt_me_dec.txt", "a")
        file.close()

        file = open(r"c:\Users\maken\OneDrive\Desktop\My Work\Python\.vscode\Python with oge\A3\decrypt_me_dec.txt", "w")
        file.write("Decrypted Cipher: " + decrypt(text, key))
        file.close()

        option = option.replace(".txt", "_dec.txt")
        print("\n\n",option,"File successfully created")
        

    else: 
        print("E R R O R .. Refreshing")
        run() 

    output_phase()

welcome_message()

run() 