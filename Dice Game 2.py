from time import sleep as s
from random import randint as r
print("")

print("Hello and welcome the the RN Two Player Game of Five Dice!")
print("")

s(3)

print("Rules:")
print("Each player rolls 5 virtual dice. Highest score gets a point. First to three wins.")
print("")

s(5)

player = 1
score1 = 0
score2 = 0

gameExit = 0
while (gameExit == 0):

    print("Player 1's turn")
    print("")

    raw_input("Press enter to roll")

    print("Rolling dice...")
    print("")
    s(1)

    total1 = 0
    for x in range(5):
        dice = r(1,6)
        print(dice)
        total1 = total1 + dice
        s(1)
    print("Player 1 Total: " + str(total1))
    print("")

    ######################################

    print("Player 2's turn")
    print("")

    raw_input("Press enter to roll")

    print("Rolling dice...")
    print("")
    s(1)

    total2 = 0
    for x in range(5):
        dice = r(1,6)
        print(dice)
        total2 = total2 + dice
        s(1)
    print("Player 2 Total: " + str(total2))
    print("")

    ######################################

    if (total1 > total2):
        print("Player 1 gets a point!")
        print("")
        score1 += 1
    elif (total2 > total1):
        print("Player 2 gets a point!")
        print("")
        score2 += 1
    else:
        print("Tie! No points.")
        print("")

    s(1)
    
    print("Scores:")
    print("Player 1 has " + str(score1) + " points")
    print("Player 2 has " + str(score2) + " points")
    print("")

    s(1)

    if (score1 == 3 or score2 == 3):
        print("We have a winner...")
        gameExit = 1

if (score1 == 3):
    print("It's Player 1!")
else:
    print("It's Player 2!")