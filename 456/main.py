'''
Developed By: Mak

'''
# 4 5 6 Dice Game 
import random 

def game():

  #First dice, picks a random number from 1 to 6
  dice_one = random.randint(1, 6)

  #Second dice, picks a random number from 1 to 6
  dice_two = random.randint(1, 6)

  #Third dice, picks a random number from 1 to 6  
  dice_three = random.randint(1, 6)

  #Title of game
  print("------------------\n\nDice Game\n\n\n", dice_one, dice_two, dice_three)

  ''' if and else statements, one the user gets one of the combinations they Win the dice game

  456 
  465

  546
  564

  654
  645

  '''

  if dice_one == 4 and dice_two == 5 and dice_three == 6:
    print("You won\n\n------------------")


  elif dice_one == 4 and dice_two == 6 and dice_three == 5:
    print("You won\n\n------------------")

  elif dice_one == 5 and dice_two == 4 and dice_three == 6:
    print("You won\n\n------------------")

  elif dice_one == 5 and dice_two == 6 and dice_three == 4:
    print("You won\n\n------------------")

  elif dice_one == 6 and dice_two == 5 and dice_three == 4:
    print("You won\n\n------------------")

  elif dice_one == 6 and dice_two == 4 and dice_three == 5:
    print("You won\n\n------------------")

  else: 
    print("You Lost\n\n------------------")

# User recieves a ticket after each game, if the user win they can present there ticket for a prize, count keeps track of the tickets      
count = 0

#while, marking the start of the game
while True:
  start = input("\n\n-------------------\nTo start Enter S: ")
  print("-------------------")

  #if user enters s then the game starts
  if start == "S" or start == "s":
    count = count + 1
    print("\n\n------------------\nTicket", count)
    game()
  
  #else error code
  else:
    print("ERROR 898: Invalid Input")
