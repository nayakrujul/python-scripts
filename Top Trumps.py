from random import choice
from os import system

# Values as "Name": [Friendship (/50), Courage (/30), Humour (/10), Fame (/40), Speed (/100)]
cards = {
  "Mama Topolino": [45,22,8,18,32],
  "Tomber": [21,23,7,28,49],
  "David Hobbscap": [33,24,7,37,56],
  "Nigel Gearsley": [44,21,9,39,88],
  "Holley Shiftwell": [39,29,6,34,71],
  "Rip Clutchgoneski": [30,24,6,20,83],
  "Grem": [5,10,4,18,27],
  "Fillmore": [47,23,6,22,30],
  "Ramone": [39,20,6,22,45],
  "Jeff Gorvette": [29,18,8,38,88],
  "Mater": [50,27,10,23,43], # MAX FRIENDSHIP AND HUMOUR
  "Lightning McQueen": [46,24,8,40,100], # MAX FAME AND SPEED
  "Acer": [4,11,5,17,26],
  "Lewis Hamilton": [37,25,7,39,89],
  "Siddeley": [30,27,6,31,69],
  "Shu Todoroki": [23,18,5,34,82],
  "Raoul Caroule": [27,19,6,36,85],
  'Rod "Torque" Redline': [34,30,7,38,68], # MAX COURAGE
  "Uncle Topolino": [46,21,8,17,56],
  "Francesco Bernoulli": [31,22,9,40,100], # MAX FAME AND SPEED
  "Sarge": [35,26,4,20,37],
  "Luigi": [45,26,8,19,39],
  "Sally": [48,25,7,21,56],
  "Carla Veloso": [35,22,8,29,84],
  "Sir Miles Axlerod": [10,8,5,37,46],
  "Guido": [43,24,5,20,41],
  "Professor Z": [12,5,6,30,29],
  "Finn McMissile": [32,30,7,37,74], # MAX COURAGE
  "Sheriff": [32,24,5,27,53],
  "Flo": [41,21,7,21,47],
}

def choose_cards(num=1):
  returnList = []
  for times in range(num):
    appendCard = choice(list(cards.keys()))
    returnList.append(appendCard)
  return returnList

# print("Welcome to Cars Top Trumps!\n")

# card = choose_cards()[0]
# print(
#   card,
#   "\nFriendship:",
#   cards[card][0],
#   "\nCourage:",
#   cards[card][1],
#   "\nHumour:",
#   cards[card][2],
#   "\nFame:",
#   cards[card][3],
#   "\nSpeed:",
#   cards[card][4]
# )

p1cards = choose_cards(15)
p2cards = choose_cards(15)

firstPlayer = 1

game = True
while game:

  system('clear')

  print(f"Player 1 - {len(p1cards)}\nPlayer 2 - {len(p2cards)}\n")

  if firstPlayer == 1:

    card = p1cards[0]
    print(
      "Player 1:\n\n" +
      card,
      "\n[1] Friendship:",
      cards[card][0],
      "/ 50\n[2] Courage:",
      cards[card][1],
      "/ 30\n[3] Humour:",
      cards[card][2],
      "/ 10\n[4] Fame:",
      cards[card][3],
      "/ 40\n[5] Speed:",
      cards[card][4],
      "/ 100"
    )

    loop = True
    while loop:
      selected = str(input("\nSelect an option: "))
      if selected.isdigit():
        selected = int(selected)
        if selected >= 1 and selected <= 5:
          loop = False
    
    p1score = cards[card][selected-1]

    card2 = p2cards[0]
    print(
      "\nPlayer 2:\n\n" +
      card2,
      "\n[1] Friendship:",
      cards[card2][0],
      "/ 50\n[2] Courage:",
      cards[card2][1],
      "/ 30\n[3] Humour:",
      cards[card2][2],
      "/ 10\n[4] Fame:",
      cards[card2][3],
      "/ 40\n[5] Speed:",
      cards[card2][4],
      "/ 100"
    )

    p2score = cards[card2][selected-1]

    if p1score > p2score:
      input("\nPlayer 1 wins.")
      p1cards.remove(card)
      p1cards.append(card)
      p2cards.remove(card2)
      p1cards.append(card2)
      firstPlayer = 1
    elif p1score < p2score:
      input("\nPlayer 2 wins.")
      p1cards.remove(card)
      p2cards.append(card)
      p2cards.remove(card2)
      p2cards.append(card2)
      firstPlayer = 2
    else:
      input("\nDraw!")
      p1cards.remove(card)
      p1cards.append(card)
      p2cards.remove(card2)
      p2cards.append(card2)
  
  elif firstPlayer == 2:

    card = p2cards[0]
    print(
      "Player 2:\n\n" +
      card,
      "\n[1] Friendship:",
      cards[card][0],
      "/ 50\n[2] Courage:",
      cards[card][1],
      "/ 30\n[3] Humour:",
      cards[card][2],
      "/ 10\n[4] Fame:",
      cards[card][3],
      "/ 40\n[5] Speed:",
      cards[card][4],
      "/ 100"
    )

    loop = True
    while loop:
      selected = str(input("\nSelect an option: "))
      if selected.isdigit():
        selected = int(selected)
        if selected >= 1 and selected <= 5:
          loop = False
    
    p2score = cards[card][selected-1]

    card2 = p1cards[0]
    print(
      "\nPlayer 1:\n\n" +
      card2,
      "\n[1] Friendship:",
      cards[card2][0],
      "/ 50\n[2] Courage:",
      cards[card2][1],
      "/ 30\n[3] Humour:",
      cards[card2][2],
      "/ 10\n[4] Fame:",
      cards[card2][3],
      "/ 40\n[5] Speed:",
      cards[card2][4],
      "/ 100"
    )

    p1score = cards[card2][selected-1]

    if p1score > p2score:
      input("\nPlayer 1 wins.")
      p1cards.remove(card2)
      p1cards.append(card2)
      p2cards.remove(card)
      p1cards.append(card)
      firstPlayer = 1
    elif p1score < p2score:
      input("\nPlayer 2 wins.")
      p1cards.remove(card2)
      p2cards.append(card2)
      p2cards.remove(card)
      p2cards.append(card)
      firstPlayer = 2
    else:
      input("\nDraw!")
      p1cards.remove(card2)
      p1cards.append(card2)
      p2cards.remove(card)
      p2cards.append(card)
  
  if p1cards == []:
    game = False
    system('clear')
    print("Player 2 wins!")
  if p2cards == []:
    game = False
    system('clear')
    print("Player 1 wins!")

print("\nThe deck:\n")

full_deck = (p1cards + p2cards)
full_deck.sort()
for card in full_deck:
  print(" -->", card)