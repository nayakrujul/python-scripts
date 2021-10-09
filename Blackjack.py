from random import choice, randint

print("Blackjack!\n")

player_cards = []
dealer_cards = []

deck_nums = [
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10",
  "J",
  "Q",
  "K",
  "A"
]

deck_types = [
  "Diamonds",
  "Hearts",
  "Clubs",
  "Spades"
]

full_deck = []

def init_deck():
  for i in range(len(deck_types)):
    for j in range(len(deck_nums)):
      full_deck.append(deck_nums[j] + " of " + deck_types[i])

init_deck()

player_total = 0
dealer_total = 0

def deal_cards(player,dealer):
  returnList = [[],[]]
  for times in range(player):
    player_cards.append(choice(full_deck))
    full_deck.remove(player_cards[-1])
    returnList[0].append(player_cards[-1])
  for times in range(dealer):
    dealer_cards.append(choice(full_deck))
    full_deck.remove(dealer_cards[-1])
    returnList[1].append(dealer_cards[-1])
  return returnList

startCards = deal_cards(2,2)

def add_to_total(add_to, *cards):
  global player_total
  global dealer_total
  for card in cards:
    if str(card[0]).isdigit() and str(card[0]) != "1":
      if add_to == "P":
        player_total += int(card[0])
      elif add_to == "D":
        dealer_total += int(card[0])
      else:
        return -1
    elif str(card[0]) == "1":
      if str(card[0]) + str(card[1]) == "10":
        if add_to == "P":
          player_total += 10
        elif add_to == "D":
          dealer_total += 10
        else:
          return -1
      elif str(card[0]) + str(card[1]) == "1 ":
        if add_to == "P":
          player_total += 10
        elif add_to == "D":
          dealer_total += 10
        else:
          return -1
    elif str(card[0]) == "J" or str(card[0]) == "Q" or str(card[0]) == "K":
      if add_to == "P":
        player_total += 10
      elif add_to == "D":
        dealer_total += 10
      else:
        return -1
    elif str(card[0]) == "A":
      if add_to == "P":
        if player_total <= 10:
          player_total += 11
        else:
          player_total += 1
      elif add_to == "D":
        if dealer_total <= 10:
          dealer_total += 11
        else:
          dealer_total += 1
      else:
        return -1
    else:
      return -1

add_to_total("P", startCards[0][0], startCards[0][1])
add_to_total("D", startCards[1][0], startCards[1][1])

def print_cards():
  print("\nPlayer's cards:")
  for pcard in player_cards:
    print(pcard)
  print(f"Total: {player_total}")
  print("\nDealer's cards:")
  for dcard in dealer_cards:
    print(dcard)
  print(f"Total: {dealer_total}")

print_cards()

game = True

def check_win():

  global game

  if player_total > 21 or dealer_total == 21:
    print("\nDealer wins.")
    game = False

    f = open("log.txt", "rt")
    if f.read()[-1] == "D":
      streak = ""
    else:
      streak = " "
    f.close()

    f = open("log.txt", "at")
    f.write(streak + "D")
    f.close()

  elif player_total == 21 or dealer_total > 21:
    print("\nPlayer wins.")
    game = False

    f = open("log.txt", "rt")
    if f.read()[-1] == "P":
      streak = ""
    else:
      streak = " "
    f.close()

    f = open("log.txt", "at")
    f.write(streak + "P")
    f.close()

check_win()

player_leaves = 0
dealer_leaves = 0

while game:

  move = input("\nPlayer, draw (D) or leave (L)? ")

  if "D" in str(move).upper() or player_leaves >= 1:

    new_card = deal_cards(1,0)[0][0]

    print(f"\nYou got a {new_card}")

    add_to_total("P", new_card)

    print_cards()

    check_win()

    player_leaves = 0
  
  else:

    player_leaves += 1
  
  if game:

    if randint(1,21) > dealer_total or dealer_leaves >= 1:

      new_card = deal_cards(0,1)[1][0]

      print(f"\nDealer got a {new_card}")

      add_to_total("D", new_card)

      print_cards()

      check_win()

      dealer_leaves = 0
    
    else:

      print("\nDealer chose to leave.")

      dealer_leaves += 1

p = 0
d = 0
pstreak = 0
dstreak = 0
highp = 0
highd = 0
with open("log.txt", "rt") as f:
  for char in f.read():
    if char == "P":
      p += 1
      pstreak += 1
      dstreak = 0
      if pstreak > highp:
        highp = pstreak
    elif char == "D":
      d += 1
      dstreak += 1
      pstreak = 0
      if dstreak > highd:
        highd = dstreak
  f.close()

if d > p:
  winner = "Dealer leads"
  pcol = '\033[1;31;40m'
  dcol = '\033[1;32;40m'
elif p > d:
  winner = "Player leads"
  pcol = '\033[1;32;40m'
  dcol = '\033[1;31;40m'
else:
  winner = "scores tied at"
  pcol = '\033[1;32;40m'
  dcol = '\033[1;32;40m'

endc = '\033[0m'
orange = '\033[1;33;40m'
cyan = '\033[1;36;40m'

print(f"\n\n{orange}Statistics:{endc}\n\n{pcol}Player: " + str(round((p/(p+d))*100,2)).ljust(5,"0") + f"%{endc}\n{dcol}Dealer: " + str(round((d/(p+d))*100,2)).ljust(5,"0") + f"%{endc}\n\n{endc}{p+d} games in test data of which {winner} {d} - {p}{endc}")

print(f"\n{cyan}Highest streak: Player - {highp}{endc}")
print(f"{cyan}Highest streak: Dealer - {highd}{endc}")

if pstreak > dstreak:
  print(f"\n{cyan}Current streak: Player - {pstreak}{endc}")
elif pstreak < dstreak:
  print(f"\n{cyan}Current streak: Dealer - {dstreak}{endc}")