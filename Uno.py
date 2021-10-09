from os import system as command
from time import sleep as wait
from sys import exit
from random import choice

players = input("How many players? ")
if players.isdigit():
  players = int(players)
  if players > 1:
    command('clear')
    print("Starting in...")
    wait(1)
    command('clear')
    print("3...")
    wait(1)
    command('clear')
    print("2...")
    wait(1)
    command('clear')
    print("1...")
    wait(1)
    command('clear')
  else:
    exit("Connection to Replit servers was terminated due to invalid input.")
else:
  exit("Connection to Replit servers was terminated due to invalid input.")

cards = [
  "\033[1;31;40m 1 \033[1;37;0m",
  "\033[1;31;40m 2 \033[1;37;0m",
  "\033[1;31;40m 3 \033[1;37;0m",
  "\033[1;31;40m 4 \033[1;37;0m",
  "\033[1;31;40m 5 \033[1;37;0m",
  "\033[1;31;40m 6 \033[1;37;0m",
  "\033[1;31;40m 7 \033[1;37;0m",
  "\033[1;31;40m 8 \033[1;37;0m",
  "\033[1;31;40m 9 \033[1;37;0m",
  "\033[1;31;40m 0 \033[1;37;0m",
  "\033[1;31;40m TAKE 2 \033[1;37;0m",
  "\033[1;31;40m SKIP \033[1;37;0m",
  "\033[1;31;40m 1 \033[1;37;0m",
  "\033[1;31;40m 2 \033[1;37;0m",
  "\033[1;31;40m 3 \033[1;37;0m",
  "\033[1;31;40m 4 \033[1;37;0m",
  "\033[1;31;40m 5 \033[1;37;0m",
  "\033[1;31;40m 6 \033[1;37;0m",
  "\033[1;31;40m 7 \033[1;37;0m",
  "\033[1;31;40m 8 \033[1;37;0m",
  "\033[1;31;40m 9 \033[1;37;0m",
  "\033[1;31;40m 0 \033[1;37;0m",
  "\033[1;31;40m TAKE 2 \033[1;37;0m",
  "\033[1;31;40m SKIP \033[1;37;0m",

  "\033[1;32;40m 1 \033[1;37;0m",
  "\033[1;32;40m 2 \033[1;37;0m",
  "\033[1;32;40m 3 \033[1;37;0m",
  "\033[1;32;40m 4 \033[1;37;0m",
  "\033[1;32;40m 5 \033[1;37;0m",
  "\033[1;32;40m 6 \033[1;37;0m",
  "\033[1;32;40m 7 \033[1;37;0m",
  "\033[1;32;40m 8 \033[1;37;0m",
  "\033[1;32;40m 9 \033[1;37;0m",
  "\033[1;32;40m 0 \033[1;37;0m",
  "\033[1;32;40m TAKE 2 \033[1;37;0m",
  "\033[1;32;40m SKIP \033[1;37;0m",
  "\033[1;32;40m 1 \033[1;37;0m",
  "\033[1;32;40m 2 \033[1;37;0m",
  "\033[1;32;40m 3 \033[1;37;0m",
  "\033[1;32;40m 4 \033[1;37;0m",
  "\033[1;32;40m 5 \033[1;37;0m",
  "\033[1;32;40m 6 \033[1;37;0m",
  "\033[1;32;40m 7 \033[1;37;0m",
  "\033[1;32;40m 8 \033[1;37;0m",
  "\033[1;32;40m 9 \033[1;37;0m",
  "\033[1;32;40m 0 \033[1;37;0m",
  "\033[1;32;40m TAKE 2 \033[1;37;0m",
  "\033[1;32;40m SKIP \033[1;37;0m",

  "\033[1;33;40m 1 \033[1;37;0m",
  "\033[1;33;40m 2 \033[1;37;0m",
  "\033[1;33;40m 3 \033[1;37;0m",
  "\033[1;33;40m 4 \033[1;37;0m",
  "\033[1;33;40m 5 \033[1;37;0m",
  "\033[1;33;40m 6 \033[1;37;0m",
  "\033[1;33;40m 7 \033[1;37;0m",
  "\033[1;33;40m 8 \033[1;37;0m",
  "\033[1;33;40m 9 \033[1;37;0m",
  "\033[1;33;40m 0 \033[1;37;0m",
  "\033[1;33;40m TAKE 2 \033[1;37;0m",
  "\033[1;33;40m SKIP \033[1;37;0m",
  "\033[1;33;40m 1 \033[1;37;0m",
  "\033[1;33;40m 2 \033[1;37;0m",
  "\033[1;33;40m 3 \033[1;37;0m",
  "\033[1;33;40m 4 \033[1;37;0m",
  "\033[1;33;40m 5 \033[1;37;0m",
  "\033[1;33;40m 6 \033[1;37;0m",
  "\033[1;33;40m 7 \033[1;37;0m",
  "\033[1;33;40m 8 \033[1;37;0m",
  "\033[1;33;40m 9 \033[1;37;0m",
  "\033[1;33;40m 0 \033[1;37;0m",
  "\033[1;33;40m TAKE 2 \033[1;37;0m",
  "\033[1;33;40m SKIP \033[1;37;0m",

  "\033[1;34;40m 1 \033[1;37;0m",
  "\033[1;34;40m 2 \033[1;37;0m",
  "\033[1;34;40m 3 \033[1;37;0m",
  "\033[1;34;40m 4 \033[1;37;0m",
  "\033[1;34;40m 5 \033[1;37;0m",
  "\033[1;34;40m 6 \033[1;37;0m",
  "\033[1;34;40m 7 \033[1;37;0m",
  "\033[1;34;40m 8 \033[1;37;0m",
  "\033[1;34;40m 9 \033[1;37;0m",
  "\033[1;34;40m 0 \033[1;37;0m",
  "\033[1;34;40m TAKE 2 \033[1;37;0m",
  "\033[1;34;40m SKIP \033[1;37;0m",
  "\033[1;34;40m 1 \033[1;37;0m",
  "\033[1;34;40m 2 \033[1;37;0m",
  "\033[1;34;40m 3 \033[1;37;0m",
  "\033[1;34;40m 4 \033[1;37;0m",
  "\033[1;34;40m 5 \033[1;37;0m",
  "\033[1;34;40m 6 \033[1;37;0m",
  "\033[1;34;40m 7 \033[1;37;0m",
  "\033[1;34;40m 8 \033[1;37;0m",
  "\033[1;34;40m 9 \033[1;37;0m",
  "\033[1;34;40m 0 \033[1;37;0m",
  "\033[1;34;40m TAKE 2 \033[1;37;0m",
  "\033[1;34;40m SKIP \033[1;37;0m",

  "\033[1;31;40m TAKE 4 \033[1;37;0m",
  "\033[1;32;40m TAKE 4 \033[1;37;0m",
  "\033[1;33;40m TAKE 4 \033[1;37;0m",
  "\033[1;34;40m TAKE 4 \033[1;37;0m"
]

player_decks = []

for times in range(players):
  player_decks.append([])

def choose_a_card():
  card = choice(cards)
  cards.remove(card)
  return card

def init_decks():
  for i in range(players):
    for j in range(7):
      player_decks[i].append(choose_a_card())

def print_deck(player):
  print("Player", player, "- your cards:")
  for every_index in range(len(player_decks[player-1])):
    print("["+ str(every_index + 1) + "] -", player_decks[player-1][every_index])

init_decks()

last_card = choose_a_card()
print("The starting card is:\n" + last_card)
wait(3)

current_player = 1
game = True
last_draw = False

while game:

  last_draw = False

  command('clear')

  input("Player " + str(current_player) + ", press ENTER to start. ")

  command('clear')

  for every_player_deck_index in range(len(player_decks)):

    if len(player_decks[every_player_deck_index]) == 1:
      if every_player_deck_index + 1 != current_player:
        print("Player", every_player_deck_index + 1, "is on an Uno.\n")
      else:
        print("You are on an Uno!\n")

  print("The last card was\n" + last_card, "\n")

  print_deck(current_player)

  loop = True

  while loop:

    card_input = input("\nUse D to draw a card\n\nWhich card do you want to use? ")

    if card_input.isdigit():
      card_input = int(card_input)
      if int(card_input) <= len(player_decks[current_player-1]) and int(card_input) >= 1:
        if (str(player_decks[current_player-1][card_input-1])[5] == str(last_card)[5] or str(player_decks[current_player-1][card_input-1])[11] == str(last_card)[11] or "TAKE 4" in player_decks[current_player-1][card_input-1]):
          last_card = player_decks[current_player-1][card_input-1]
          player_decks[current_player-1].remove(last_card)
          loop = False
    elif "D" in str.upper(str(card_input)):
      new_card = choose_a_card()
      player_decks[current_player-1].append(new_card)
      print("\nYou received\n" + new_card, "\n")
      card_input = input("Do you want to use it (Y/N)? ")
      loop = False
      if "Y" in str(card_input).upper():
        if (
          player_decks[current_player-1][-1][5] == str(last_card)[5]
          or player_decks[current_player-1][-1][11] == str(last_card)[11]
          or "TAKE 4" in new_card
        ):
          last_card = new_card
          player_decks[current_player-1].remove(last_card)
        else:
          last_draw = True
      else:
        last_draw = True
    
  if "TAKE 4" in last_card and last_draw == False:
    current_player += 1
    if current_player > players:
      current_player -= players
    player_decks[current_player-1].append(choose_a_card())
    player_decks[current_player-1].append(choose_a_card())
    player_decks[current_player-1].append(choose_a_card())
    player_decks[current_player-1].append(choose_a_card())
    command('clear')
    input("Player " + str(current_player) + ", your turn was skipped due to a TAKE 4. ")
  
  if "TAKE 2" in last_card and last_draw == False:
    current_player += 1
    if current_player > players:
      current_player -= players
    player_decks[current_player-1].append(choose_a_card())
    player_decks[current_player-1].append(choose_a_card())
    command('clear')
    input("Player " + str(current_player) + ", your turn was skipped due to a TAKE 2. ")
  
  if "SKIP" in last_card and last_draw == False:
    current_player += 1
    if current_player > players:
      current_player -= players
    command('clear')
    input("Player " + str(current_player) + ", your turn was skipped due to a SKIP. ")

  current_player += 1
  if current_player > players:
    current_player -= players

  for deck_index in range(len(player_decks)):
    if player_decks[deck_index] == []:
      game = False
      winner = deck_index + 1

command('clear')
print("Player", winner, "wins!")
