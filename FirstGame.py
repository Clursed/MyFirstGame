#\!/\!/\!/\!/\!/\!/\!/\!/COMPLETE GAME\!/\!/\!/\!/\!/\!/\!/\!/
#Login 
#runlog
def runlog():
    name = input("what is your name?   ")
    age = input("How old are you?  ")
    print("Welcome", name, "you are", age, "years old")
    print("Thats it thank you for logging in have fun!")
    print("Enter Game Def")
#Login system
def login():
    log = input("Hello would you like to log in? (yes/no)   ")
    if log == "yes":
        runlog()
    elif log == "no":
        print ("Ok enjoy playing!")
login()
#--------------------------Path's------------------------------------
#-----------------------deathsLeft------------------------------

def death1():
    print("The orange glizzy gobbler gotch ya ass better luck next time")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    
def death2():
    print("you were killed by bigfoot try again loser")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    
#Wins
def win1():
    print("Yo u won... good job ig")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")

def win2():
    print("You have found the magical path where will will find endless piles of riches")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")

#------------------------------Left----------------------------
def q4():
    ans = input("You find anthoner split path this time there colored (Orange/Green)  ")
    if ans == "orange":
        death1()
    elif ans == "green":
        win1()

def q3():
    ans = input("You have reached a forest do yo go into the forest or find a new path?(Path/Forrest)   ")
    if ans == "path":
        win2()
    elif ans == "forrest":
        death2()
    
def q2():
    ans = input("you have come across a lake do you (swim/go around) the lake")
    if ans == "swim":
        q3()
    elif ans == "go around":
        q4()

def run_game():
     ans = input("You start on a split path (left or right)  ")
     if ans == "left":
         q2()
     elif ans == "right":
         q5()
#-----------------------parhRight------------------------------
#-----------------------deathsRight-------------------------
def death3():
    print("You open the door an find a ladder leading down you decide to go down it an find a bunker as you explore you get killed by a deamon nun sucks to suck")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    
def death4():
    print("As you grab the door knob you feel somthing grab you as you get pulled back into the house an the door slams you get thrown into the wall you look up an see a deamon nun rush to you and kill you Gg you tryed")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")

def death5():
    print("You walk up to the man in a black coat and he ask you if you want to trade he offer a gold watch, a sword and a dagger you kindly decline his offers as you are a broke bitch an dont even know where you are as you walk away the man charges at you with the dagger and stabs you in the chest you dead gg")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    
    
def death6():
    print ("As you go back down the path you hear a growl as you look back you see a cave spider jump at you it takes you to the grould and as you fight it bites you filling you with poison as it slowly kills you as you watch the spider wrap you in a wep gg's")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    

def death7():
    print("As you continue into the cave a pack of moutain lions come out of the darkness and eat you ")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    


def death8():
    print("As you go to leave the earth starts to shake and a pile of rocks fall covering the exit now its dark an you hear a growl as you get pounsed and eatten alive")
    play_again  = input("play again?")
    if play_again == "yes":
        print("--------------------------")
        run_game()
    else:
        print("Later")
    
#----------------------pathRight-----------------------------
def q9():
    ans = input("As you walk threw the cave you see that the walls and cellings are covered in crystal(Continue/Exit)")
    if ans == "continue":
        death7()
    elif ans == "exit":
        death8()

def q8():
    ans = input("As your going down the path you find a Cave do ener it?(Enter/Pass)")
    if ans == "enter":
        q9()
    elif ans == "pass":
        death6()

def q7():
    ans = input("As your going down the path you find a trader but he lowkey skechy(Trade/Continue)  ")
    if ans == "trade":
        death5()
    elif ans == "continue":
        q8()
        

def q6():
    print("You enter the house and see its empty but there's one door in the corner of the house")
    ans = input("Do you explore the door or leave(explore/leave)  ")
    if ans == "explore":
        death3()
    elif ans == "leave":
            death4()

def q5():
    ans = input("You stumble across a house do you enter or continue the path(Enter/Pass)  ")
    if ans == "enter":
        q6()
    elif ans == "pass":
        q7()
#/__________________________________________/





#\_/\_/\_/\_/\_/\_/\_/\_/Run\_/Game_/\_/\_/\_/\_/\_/\_/\_/\_


run_game()






#/________________________________________\
