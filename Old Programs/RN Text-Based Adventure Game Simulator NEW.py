print()
print("Welcome to the RN Adventure game simulator (v1.4)! ")
print()
print("Here are the rules:")
print("To move forwards press 'F' and then 'Enter'.")
print("To move backwards press 'B' and then 'Enter'.")
print("To move left press 'L' and then 'Enter'.")
print("To move right press 'R' and then 'Enter'.")
print("To exit press 'E' and then 'Enter'.")
print("To upgrade, press 'U' and then 'Enter'.")
print("For more info about the game, press 'I' and then 'Enter'.")

posX = 4
posY = 4
Quit = 0

import random
for x in range(1):
  EX = random.randint(1,7)
import random
for x in range(1):
  EY = random.randint(1,7)
import random
for x in range(1):
  SecCodeNum = random.randint(100,999)

print("You have a 7 by 7 grid. You are currently at (4, 4). Your enemy can be anywhere, so beware.")

print("Start in 3, 2, 1, Go!")

while(posY != 8 and posX != 8 and posY != 0 and posX != 0 and posY != EY and posX != EX and Quit == 0):
  print("You are at (" + str(posX) + ", " + str(posY) + ").")
  start = input("Enter your step. ")
  if(start == "F" or start == "f"):
    posY = posY + 1
  elif(start == "B" or start == "b"):
    posY = posY - 1
  elif(start == "L" or start == "l"):
    posX = posX - 1
  elif(start == "R" or start == "r"):
    posX = posX + 1
  elif(start == "E" or start == "e"):
    print("You have quit the game.")
    Quit = Quit + 1
  elif(start == "U" or start == "u"):
    card = input("Please enter your card number. Press 'Enter' to return to game. ")
    if(len(card) == 16):
      secCode = input("Please enter the three digit security code on the back of your card. Press 'Enter' to return to game. ")
      if(int(secCode) == int(SecCodeNum)):
        print("Upgrade pending. Returning to game. ")
      elif(secCode == ""):
        print("Returning to game. ")
      else:
        print("Wrong Security Code. Returning to game. ")
        print("Security code for card " + str(card) + " is " + str(SecCodeNum) + ".")
    elif(card == ""):
      print("Returning to game. ")
    else:
      print("Wrong card number. Returning to game. ")
  elif(start == "I" or start == "i"):
    print("Sorry, this feature is not availiable in this version. Upgrade for more!!")
  else:
    print("Incorrect step, options are F, B, L, R, E, U and I. ")

print("You have been defeated. Enemy was at (" + str(EX) + ", " + str(EY) + "). You are at (" + str(posX) + ", " + str(posY) + ").")

if(posX == EX):
  print("Enemy in x line (shooting vertically)")
elif(posY == EY):
  print("Enemy in y line (shooting horizontally)")
elif(posX == 8):
  print("Off the grid on the East (Right) side")
elif(posX == 0):
  print("Off the grid on the West (Left) side")
elif(posY == 8):
  print("Off the grid on the North (Furthest) side")
elif(posY == 0):
  print("Off the grid on the South (Closest) side")

# Go to https://repl.it/repls/VoluminousLiquidFiber (Command + Click)
## Thank you