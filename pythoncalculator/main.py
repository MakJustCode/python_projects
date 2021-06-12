#Problem 1 simple calculator

#Python Library
import math
import numpy as np
# End of Library 

print("C A L C U L A T O R") # displayed at the top od the calculator 

e=2.718 #Exponential

# Beginning of Functions
def add(a, b): # this is addition function
  return a + b

def subtract(a, b): # this is my subtraction function
  return a - b

def multiplication(a, b): # this is my multiplication function
  return a * b

def division(a, b): # this is my division function 
  return a / b

def summation(a, b): #this is my summation function 
  return (a + b) / 2

def mod(a, b): # this is my modular function
  return a % b

def power(a, b): # this is my power function
  return math.pow(a, b) 

def exp(e,a):
  return math.exp(e,a) # this is my exponentail function

def naturalLog(a): # this is my natural log funtion
  return np.log(a) 

def absolute(a):
  return abs(a)
# Ending of functions 

# Beginning of the while 
while True:

  #Beginning of the prompted questions 
  num1 = int(input("\nEnter first number: "))
  operation = input("\nList of operations: \n+ (addition) \n- (subtraction) \n* (multiplication) \n/ (division) \n% (module) \ns (summation) \np (power) \ne (exponent), \nl (natural log) \na (absolute value) \n\nEnter operation : ")
  num2 = int(input("\n(This is required) \nEnter second number:"))
  #Ending of the prompted questions 

  # if, else if and else statments for the calculator 
  if operation == "+":
    print("\n", num1, "+", num2, "=", add(num1, num2)) # Add

  elif operation == "-":
    print("\n", num1, "-", num2, "=", subtract(num1, num2)) # Subtract

  elif operation == "*":
    print("\n", num1, "*", num2, "=", multiplication(num1, num2)) # Multiply

  elif operation == "/":
    print("\n", num1, "/", num2, "=", division(num1, num2)) # Divide

  elif operation == "%":
    print("\n", num1, "%", num2, "=", mod(num1, num2)) # Modular

  elif operation == "s":
    print("\n", num1, "summation", num2, "=", summation(num1, num2)) # Summation

  elif operation == "p":
    print("\n", num1, "pow", num2, "=", power(num1, num2)) # Power

  elif operation == "e":
    print("\n", num1, "exp", num2, "=", exp(num1, num2)) # Exponential

  elif operation == "l":
    print("\n", num1, "log", num2, "=", naturalLog(num1, num2)) # Log

  elif operation == "a":
    print("\n", num1, "absolute", num2, "=", absolute(num1, num2)) #Absolute

  else:
    print("ERROR, Please follow instructions") #invalid response 

  
  choice = input("\n\nEnter x to exit") #Break statment to exit the calculator 
  if choice == "X" or choice == "x":
    break 
# Ending of the while loop 


print("Session Ended") # Exit message 