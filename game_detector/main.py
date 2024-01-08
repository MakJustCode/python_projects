'''
Makenson Noel 
DevelopWithMak
Detect a opp

its a game XD

'''



def instructions():
    print("\n(P) Punch \n(W) Weave \n(K) Kick\n")

def player():
    def player1():
        playerhealth = 100

    def A1():
        playerhealth = 100

    def A2():
        playerhealth = 100

    def A3():
        playerhealth = 100

def enemies():

    def fn1():
        enemyhealth = 100

    def fn2():
        enemyhealth = 100 

    def fn3():
        enemyhealth = 100 

    def fn4():
        enemyhealth = 100 

    

def game():
    

    player = ["Player 1", "A1", "A2", "A3"]

    enemies = ["FN1", "FN2", "FN3", "FN4"]

    playerhealth = 100

    opphealth = 100 

    punchweight = 25

    kickweight = 50


    

    print("\n\n\n\n\nPerson 1: Yooo wtf you stepped on my shoes G\n\n") 
    print("                                                     Dialogue : Yo what you gon do about it, you gon let him try you like that ?\n\n")
    print("Me: Nah f*ck that let's fade \n\n")

    print("Now fighting ", enemies[0], " don't get whupped \n\n")

    #Transition Screen 

    print("Alright ", enemies[0], " wassup\n\n")

    for i in range (opphealth):

        instructions()

        fight_option = input(" ")

        i = 0



        if fight_option == "P" or fight_option == "p":
            punch = 25 
            opphealth = opphealth - punch
            if opphealth >= 0:
                print("You punched",enemies[0], " health is now  Health:", opphealth)

            elif opphealth <= 0: 
                print("Damn you whupped that mf")

            fight_option = input(" ")



            #animation

            
        elif fight_option == "k" or fight_option =="K":
            kick = 50
            opphealth = opphealth - kick 
            if opphealth >= 0:
                print("You kicked",enemies[0], " health is now  Health:", opphealth)

            instructions()
            fight_option = input(" ")

            if opphealth <=0: 
                print("Damn you whupped that mf")

            #animation


def start_screen():

    print("WELCOME TO OPP\n\n\n")
    print("[START]\n\n\n")
    print("[QUIT]")

    start_option = input("Enter S to Start | Enter Q to QUIT")

    if start_option == "s" or start_option == "S":
        game() 

    elif start_option == "q" or start_option == "Q":
        print("E X I T T I N G . . . . . . . ")

start_screen()
