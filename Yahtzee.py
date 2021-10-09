from random import randint as die # The singular of dice, not death
from time import sleep as wait
from os import system as command

def dice():
  command('clear')
  print("Rolling...")
  wait(1)
  command('clear')

  d1 = die(1,6)
  d2 = die(1,6)
  d3 = die(1,6)
  d4 = die(1,6)
  d5 = die(1,6)
  return [d1, d2, d3, d4, d5]

def print_dice(diceList):
  if len(diceList) != 5:
    return -1
  print("----- ----- ----- ----- -----")
  print(f"| {diceList[0]} | | {diceList[1]} | | {diceList[2]} | | {diceList[3]} | | {diceList[4]} | ")
  print("----- ----- ----- ----- -----")

game = True
p1Used = []
p2Used = []

p1TotalScore = 0
p2TotalScore = 0

while game:

  # Player 1

  command('clear')

  print("Player 1 -", p1TotalScore, "\nPlayer 2 -", p2TotalScore, "\nTurns remaining -", 13-len(p1Used), "\n")

  input("Player 1, press enter to roll the dice: ")

  diceList = dice()
  print_dice(diceList)

  rollsLeft = 2
  while rollsLeft > 0:
    again = input("Roll again (Y/N)? ")

    if "Y" in str.upper(str(again)):
      rollsLeft -= 1 
      diceList = dice()
      print_dice(diceList)
    else:
      rollsLeft = 0
  
  p1Allowed = []

  if (
    diceList[0] == diceList[1] == diceList[2]
    or diceList[0] == diceList[2] == diceList[3]
    or diceList[0] == diceList[3] == diceList[4]
    or diceList[0] == diceList[1] == diceList[3]
    or diceList[0] == diceList[1] == diceList[4]
    or diceList[0] == diceList[2] == diceList[4] 
    or diceList[1] == diceList[2] == diceList[3] 
    or diceList[1] == diceList[2] == diceList[4] 
    or diceList[1] == diceList[3] == diceList[4] 
    or diceList[2] == diceList[3] == diceList[4]
  ): 
    p1Allowed.append("Three Of A Kind")
  
  if (
    diceList[0] == diceList[1] == diceList[2] == diceList[3]
    or diceList[0] == diceList[2] == diceList[3] == diceList[4]
    or diceList[0] == diceList[1] == diceList[3] == diceList[4]
    or diceList[0] == diceList[1] == diceList[2] == diceList[4]
    or diceList[1] == diceList[2] == diceList[3] == diceList[4]
  ):
    p1Allowed.append("Four Of A Kind")
  
  if (
    (
      (diceList[0] == diceList[1] == diceList[2] and diceList[3] == diceList[4])
      or (diceList[0] == diceList[2] == diceList[3] and diceList[1] == diceList[4])
      or (diceList[0] == diceList[3] == diceList[4] and diceList[1] == diceList[2])
      or (diceList[0] == diceList[1] == diceList[3] and diceList[2] == diceList[4])
      or (diceList[0] == diceList[1] == diceList[4] and diceList[2] == diceList[3])
      or (diceList[0] == diceList[2] == diceList[4] and diceList[1] == diceList[3])
      or (diceList[1] == diceList[2] == diceList[3] and diceList[0] == diceList[4])
      or (diceList[1] == diceList[2] == diceList[4] and diceList[0] == diceList[3])
      or (diceList[1] == diceList[3] == diceList[4] and diceList[0] == diceList[2])
      or (diceList[2] == diceList[3] == diceList[4] and diceList[0] == diceList[1])
    )
  ):
    p1Allowed.append("Full House")

  #smallStraight = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
  smallStraight1 = [1,2,3,4]
  smallStraight2 = [2,3,4,5]
  smallStraight3 = [3,4,5,6]

  if (
    set([diceList[0], diceList[1], diceList[2], diceList[3]]) == set(smallStraight1)
    or set([diceList[0], diceList[2], diceList[3], diceList[4]]) == set(smallStraight1)
    or set([diceList[0], diceList[1], diceList[3], diceList[4]]) == set(smallStraight1)
    or set([diceList[0], diceList[1], diceList[2], diceList[4]]) == set(smallStraight1)
    or set([diceList[1], diceList[2], diceList[3], diceList[4]]) == set(smallStraight1)
    or set([diceList[0], diceList[1], diceList[2], diceList[3]]) == set(smallStraight2)
    or set([diceList[0], diceList[2], diceList[3], diceList[4]]) == set(smallStraight2)
    or set([diceList[0], diceList[1], diceList[3], diceList[4]]) == set(smallStraight2)
    or set([diceList[0], diceList[1], diceList[2], diceList[4]]) == set(smallStraight2)
    or set([diceList[1], diceList[2], diceList[3], diceList[4]]) == set(smallStraight2)
    or set([diceList[0], diceList[1], diceList[2], diceList[3]]) == set(smallStraight3)
    or set([diceList[0], diceList[2], diceList[3], diceList[4]]) == set(smallStraight3)
    or set([diceList[0], diceList[1], diceList[3], diceList[4]]) == set(smallStraight3)
    or set([diceList[0], diceList[1], diceList[2], diceList[4]]) == set(smallStraight3)
    or set([diceList[1], diceList[2], diceList[3], diceList[4]]) == set(smallStraight3)
  ):
    p1Allowed.append("Small Straight")

  largeStraight1 = [1,2,3,4,5]
  largeStraight2 = [2,3,4,5,6]

  if (
    set([diceList[0], diceList[1], diceList[2], diceList[3], diceList[4]]) == set(largeStraight1)
    or set([diceList[0], diceList[1], diceList[2], diceList[3], diceList[4]]) == set(largeStraight2)
  ):
    p1Allowed.append("Large Straight")
  
  if (
    diceList[0] == diceList[1] == diceList[2] == diceList[3] == diceList[4]
  ):
    p1Allowed.append("Yahtzee")
  
  p1Scores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  scoreNames = ["1", "2", "3", "4", "5", "6", "Three Of A Kind", "Four Of A Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]
  total = 0

  for i in range(len(diceList)):
    if str(diceList[i]) not in p1Used:
      p1Scores[diceList[i]-1] += diceList[i]
    total += diceList[i]
  
  if "Three Of A Kind" in p1Allowed and "Three Of A Kind" not in p1Used:
    p1Scores[6] = total
  if "Four Of A Kind" in p1Allowed and "Four Of A Kind" not in p1Used:
    p1Scores[7] = total
  if "Full House" in p1Allowed and "Full House" not in p1Used:
    p1Scores[8] = 25
  if "Small Straight" in p1Allowed and "Small Straight" not in p1Used:
    p1Scores[9] = 30
  if "Large Straight" in p1Allowed and "Large Straight" not in p1Used:
    p1Scores[10] = 40
  if "Yahtzee" in p1Allowed and "Yahtzee" not in p1Used:
    p1Scores[11] = 50
  if "Chance" not in p1Used:
    p1Scores[12] = total

  print("")
  for j in range(len(p1Scores)):
    print("[" + str.zfill(str(j+1),2) + "]", scoreNames[j], "-", p1Scores[j])
  unused = []
  for k in range(len(scoreNames)):
    if scoreNames[k] not in p1Used:
      unused.append(scoreNames[k])
  print("\nYou have not used:", unused)

  loop = True

  while loop:

    choice = input("\nEnter the number: ")

    if choice.isdigit():
      if int(choice) <=13 and int(choice) >= 1:
        if scoreNames[int(choice)-1] not in p1Used:
          p1TotalScore += p1Scores[int(choice)-1]
          p1Used.append(scoreNames[int(choice)-1])
          loop = False
  
  # Player 2

  command('clear')

  print("Player 1 -", p1TotalScore, "\nPlayer 2 -", p2TotalScore, "\nTurns remaining -", 13-len(p2Used), "\n")

  input("Player 2, press enter to roll the dice: ")

  diceList = dice()
  print_dice(diceList)

  rollsLeft = 2
  while rollsLeft > 0:
    again = input("Roll again (Y/N)? ")

    if "Y" in str.upper(str(again)):
      rollsLeft -= 1 
      diceList = dice()
      print_dice(diceList)
    else:
      rollsLeft = 0
  
  p2Allowed = []

  if (
    diceList[0] == diceList[1] == diceList[2]
    or diceList[0] == diceList[2] == diceList[3]
    or diceList[0] == diceList[3] == diceList[4]
    or diceList[0] == diceList[1] == diceList[3]
    or diceList[0] == diceList[1] == diceList[4]
    or diceList[0] == diceList[2] == diceList[4] 
    or diceList[1] == diceList[2] == diceList[3] 
    or diceList[1] == diceList[2] == diceList[4] 
    or diceList[1] == diceList[3] == diceList[4] 
    or diceList[2] == diceList[3] == diceList[4]
  ): 
    p2Allowed.append("Three Of A Kind")
  
  if (
    diceList[0] == diceList[1] == diceList[2] == diceList[3]
    or diceList[0] == diceList[2] == diceList[3] == diceList[4]
    or diceList[0] == diceList[1] == diceList[3] == diceList[4]
    or diceList[0] == diceList[1] == diceList[2] == diceList[4]
    or diceList[1] == diceList[2] == diceList[3] == diceList[4]
  ):
    p2Allowed.append("Four Of A Kind")
  
  if (
    (
      (diceList[0] == diceList[1] == diceList[2] and diceList[3] == diceList[4])
      or (diceList[0] == diceList[2] == diceList[3] and diceList[1] == diceList[4])
      or (diceList[0] == diceList[3] == diceList[4] and diceList[1] == diceList[2])
      or (diceList[0] == diceList[1] == diceList[3] and diceList[2] == diceList[4])
      or (diceList[0] == diceList[1] == diceList[4] and diceList[2] == diceList[3])
      or (diceList[0] == diceList[2] == diceList[4] and diceList[1] == diceList[3])
      or (diceList[1] == diceList[2] == diceList[3] and diceList[0] == diceList[4])
      or (diceList[1] == diceList[2] == diceList[4] and diceList[0] == diceList[3])
      or (diceList[1] == diceList[3] == diceList[4] and diceList[0] == diceList[2])
      or (diceList[2] == diceList[3] == diceList[4] and diceList[0] == diceList[1])
    )
  ):
    p2Allowed.append("Full House")

  #smallStraight = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
  smallStraight1 = [1,2,3,4]
  smallStraight2 = [2,3,4,5]
  smallStraight3 = [3,4,5,6]

  if (
    set([diceList[0], diceList[1], diceList[2], diceList[3]]) == set(smallStraight1)
    or set([diceList[0], diceList[2], diceList[3], diceList[4]]) == set(smallStraight1)
    or set([diceList[0], diceList[1], diceList[3], diceList[4]]) == set(smallStraight1)
    or set([diceList[0], diceList[1], diceList[2], diceList[4]]) == set(smallStraight1)
    or set([diceList[1], diceList[2], diceList[3], diceList[4]]) == set(smallStraight1)
    or set([diceList[0], diceList[1], diceList[2], diceList[3]]) == set(smallStraight2)
    or set([diceList[0], diceList[2], diceList[3], diceList[4]]) == set(smallStraight2)
    or set([diceList[0], diceList[1], diceList[3], diceList[4]]) == set(smallStraight2)
    or set([diceList[0], diceList[1], diceList[2], diceList[4]]) == set(smallStraight2)
    or set([diceList[1], diceList[2], diceList[3], diceList[4]]) == set(smallStraight2)
    or set([diceList[0], diceList[1], diceList[2], diceList[3]]) == set(smallStraight3)
    or set([diceList[0], diceList[2], diceList[3], diceList[4]]) == set(smallStraight3)
    or set([diceList[0], diceList[1], diceList[3], diceList[4]]) == set(smallStraight3)
    or set([diceList[0], diceList[1], diceList[2], diceList[4]]) == set(smallStraight3)
    or set([diceList[1], diceList[2], diceList[3], diceList[4]]) == set(smallStraight3)
  ):
    p2Allowed.append("Small Straight")

  largeStraight1 = [1,2,3,4,5]
  largeStraight2 = [2,3,4,5,6]

  if (
    set([diceList[0], diceList[1], diceList[2], diceList[3], diceList[4]]) == set(largeStraight1)
    or set([diceList[0], diceList[1], diceList[2], diceList[3], diceList[4]]) == set(largeStraight2)
  ):
    p2Allowed.append("Large Straight")
  
  if (
    diceList[0] == diceList[1] == diceList[2] == diceList[3] == diceList[4]
  ):
    p2Allowed.append("Yahtzee")
  
  p2Scores = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  scoreNames = ["1", "2", "3", "4", "5", "6", "Three Of A Kind", "Four Of A Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]
  total = 0

  for i in range(len(diceList)):
    if str(diceList[i]) not in p2Used:
      p2Scores[diceList[i]-1] += diceList[i]
    total += diceList[i]
  
  if "Three Of A Kind" in p2Allowed and "Three Of A Kind" not in p2Used:
    p2Scores[6] = total
  if "Four Of A Kind" in p2Allowed and "Four Of A Kind" not in p2Used:
    p2Scores[7] = total
  if "Full House" in p2Allowed and "Full House" not in p2Used:
    p2Scores[8] = 25
  if "Small Straight" in p2Allowed and "Small Straight" not in p2Used:
    p2Scores[9] = 30
  if "Large Straight" in p2Allowed and "Large Straight" not in p2Used:
    p2Scores[10] = 40
  if "Yahtzee" in p2Allowed and "Yahtzee" not in p2Used:
    p2Scores[11] = 50
  if "Chance" not in p2Used:
    p2Scores[12] = total

  print("")
  for j in range(len(p2Scores)):
    print("[" + str.zfill(str(j+1),2) + "]", scoreNames[j], "-", p2Scores[j])
  unused = []
  for k in range(len(scoreNames)):
    if scoreNames[k] not in p2Used:
      unused.append(scoreNames[k])
  print("\nYou have not used:", unused)

  loop = True

  while loop:

    choice = input("\nEnter the number: ")

    if choice.isdigit():
      if int(choice) <=13 and int(choice) >= 1:
        if scoreNames[int(choice)-1] not in p2Used:
          p2TotalScore += p2Scores[int(choice)-1]
          p2Used.append(scoreNames[int(choice)-1])
          loop = False
  
  # End of game

  if len(p1Used) == 13 and len(p2Used) == 13:
    command('clear')
    print("Game Over.\n")
    game = False

if p1TotalScore > p2TotalScore:
  print("Player 1 wins by", p1TotalScore, "-", p2TotalScore)
elif p2TotalScore > p1TotalScore:
  print("Player 2 wins by", p1TotalScore, "-", p2TotalScore)
else:
  print("DRAW!", p1TotalScore, "-", p2TotalScore)