def get_card(card):

  card = card.upper()

  if len(card) not in (2, 3):
    return False
  
  if card[-1] not in ("H", "D", "C", "S"):
    return False
  
  cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

  if card[:-1] not in cards:
    return False

  return cards.index(card[:-1]), card[-1]

def all_same_suit(hand):

  suit = hand[0][1]
  for x, y in hand:
    if y != suit:
      return False
  return True

def straight(hand):

  lst = []
  lst.append([x for x,y in hand])
  new_lst = [int(i) for i in lst[0]]
  lowest = min(new_lst)
  for m in range(len(hand)):
    if lowest+m not in new_lst:
      return 0
  if lowest == 8:
    return 2
  return 1

def same_rank(hand):

  lst = [x for x, y in hand]
  new_lst = []
  for i in lst:
    new_lst.append(lst.count(i))
  return new_lst

def get_hand(hand):

  lst = []
  lst.append([get_card(i) for i in hand])
  lst = lst[0]

  used = []
  for x in lst:
    if x in used:
      return False
    used.append(x)
  
  # Royal flush
  if all_same_suit(lst) and straight(lst) == 2:
    return (0, "RF")
  
  # Straight flush
  if all_same_suit(lst) and straight(lst) == 1:
    return (1, "SF")

  # Four of a kind
  if 4 in same_rank(lst):
    return (2, "FK")
  
  # Full house
  if 3 in same_rank(lst) and 2 in same_rank(lst):
    return (3, "FH")

  # Flush
  if all_same_suit(lst):
    return (4, "FL")
  
  # Straight
  if straight(lst) >= 1:
    return (5, "ST")
  
  # Three of a kind
  if 3 in same_rank(lst):
    return (6, "TK")
  
  # Two Pair
  if same_rank(lst).count(2) == 4:
    return (7, "TP")
  
  # Pair
  if 2 in same_rank(lst):
    return (8, "PA")
  
  # High Card
  else:
    return (9, "HC")

print(get_hand(["10H", "JH", "KH", "QH", "AH"]))
print(get_hand(["2H", "3H", "4H", "5H", "6H"]))
print(get_hand(["2H", "2D", "2C", "2S", "6H"]))
print(get_hand(["2H", "2D", "2C", "6S", "6H"]))
print(get_hand(["2H", "3H", "4H", "5H", "7H"]))
print(get_hand(["2H", "3H", "4H", "5H", "6S"]))
print(get_hand(["2H", "2D", "2C", "4S", "6H"]))
print(get_hand(["2H", "2D", "4C", "6S", "6H"]))
print(get_hand(["2H", "2D", "3C", "4S", "6H"]))
print(get_hand(["2H", "7D", "KC", "AS", "6H"]))