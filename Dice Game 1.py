#RRRRRRRRRRRRR
#RRRRRRRRRRRRR
#RR        RRR
#RR        RRR
#RRRRRRRRRRRRR
#RRRRRRRRRRRRR
#RRRRR
#RR RRRR
#RR   RRRR
#RR     RRRR
#RR       RRRR

# Big R for Rujul

######################################################

# Import libraries
from random import randint as r
from time import sleep as s
print("")

# Welcome message
print("Welcome to the RN 1-player Dice Game.")
print("")

# Rules
print("Game rules:")
print("You guess a number from 1 to 20, then the computer guesses one.")
print("A virtual 1-20 dice is then rolled. Closest gets a point.")
print("")

# 'First to' input and validation
winExt = 0
while (winExt == 0):

    winPts = input("How many points do you want this game to be up to (1 - 15)? ")
    print("")

    # Is it a number?
    if(str.isdigit(str(winPts))):
        intWinPts = int(winPts)

        # Is it between 1 and 15?
        if(intWinPts >= 1 and intWinPts <= 15):
            print("Playing up to " + str(winPts) + "points...")
            winExt = 1

        # Error message
        else:
            print("Try again.")

    # Error message
    else:
        print("Try again.")
print("")

turns = 0
playerPts = 0
cpuPts = 0

# Completely pointless waste of time
print("Processing...")
s(2)
print("")
print("Connecting to server...")
s(1)
print("")
print("Downloading data from server...")
s(4)
print("")
print("Almost done.")
s(1)
print("")

# Game
while(playerPts < intWinPts and cpuPts < intWinPts):
    print("Your turn.")

    # Input and validation
    guess = input("Guess a number: ")
    if(str.isdigit(str(guess))):
        print("Guess accepted.")
    else:
        print("Not a number: Guess registered as 0.")
        guess = 0
    print("")

    # Computer's 'guess'
    cpuGuess = r(1,20)
    print("Computer's guess: " + str(cpuGuess))
    print("")
    s(1)

    # Roll the 'dice'
    print("Rolling dice...")
    s(2)
    dice = r(1,20)
    print(dice)
    print("")
    s(1)

    # Find out who is closer

    # Player
    if(int(guess) > dice):
        playerDiff = int(guess) - dice
        print("You were over by " + str(playerDiff))
    elif(int(guess) < dice):
        playerDiff = dice - int(guess)
        print("You were under by " + str(playerDiff))
    else:
        playerDiff = 0
        print("Exact! Well done!")
    print("")
    
    s(1)

    # Computer
    if(int(cpuGuess) > dice):
        cpuDiff = int(cpuGuess) - dice
        print("The computer was over by " + str(cpuDiff))
    elif(int(cpuGuess) < dice):
        cpuDiff = dice - int(cpuGuess)
        print("The computer was under by " + str(cpuDiff))
    else:
        cpuDiff = 0
        print("The computer was exact")
    print("")
    
    s(1)

    if(playerDiff < cpuDiff):
        print("Well done! You won the point!")
        playerPts += 1
    elif(cpuDiff < playerDiff):
        print("Tough luck. The Computer gets a point.")
        cpuPts += 1
    else:
        print("Tie! No points awarded.")

    s(1)

    # Score
    print("The scores stand at: Player " + str(playerPts) + " - " + str(cpuPts) + " Computer")
    print("")

s(2)

# Winner
if(playerPts == intWinPts):
    print("Well done. You have reached " + str(winPts))
elif(cpuPts == intWinPts):
    print("The Computer has reached " + str(winPts))
else:
    print("Error.")
print("")

print("Thank you for playing.")
print("")