from random import randint
from math import ceil
from os import system
from threading import Thread
from time import sleep


def get_cards(n: int, l: int = 9, r: int = 1, s: int = 30) -> list[list[str]]:

    cards = []

    for x in range(n):

        cards.append([])

        while len(cards[-1]) < l:

            num = randint(r, s)

            if str(num).zfill(2) not in cards[-1]:
                cards[-1].append(str(num).zfill(2))

    return cards


def display(cards: list[list[str]], names: list[str]) -> None:

    print("\n\n")

    for x in range(ceil(len(cards[0]) / 3)):

        for y in cards:

            print(' '.join(y[x * 3: (x * 3) + 3]), end="\t")

        print("")

    for z in names:

        print(z + (8 - len(z)) * " ", end="\t")

    print("")


def random_number(c: list[list[str]], u: list[int], r: int = 1, s: int = 30) -> list[list[int], int]:

    num = randint(r, s)
    while num in u:
        num = randint(r, s)

    system('clear')

    print(f"The next number is {num}")

    _winner = []
    for x in range(len(c)):
        if str(num).zfill(2) in c[x]:
            c[x][c[x].index(str(num).zfill(2))] = "  "
            if c[x].count("  ") == len(c[x]):
                _winner.append(x)

    return [_winner, num]


players = input("How many players? ")
if not players.isdigit():
    players = 2
players = int(players)
if players < 2:
    players = 2

player_names = []
for times in range(players):
    player_names.append(input(f"Name of player {times + 1}: "))

winner = 0
winners = []
player_cards = get_cards(players)
used = []
counter = 0.0


def timer():

    global counter
    while not winner:
        counter += 0.1
        sleep(0.1)
    return False


my_thread = Thread(target=timer)
my_thread.start()

while not winner:

    winners, new_num = random_number(player_cards, used)
    used.append(new_num)
    winner = len(winners)
    display(player_cards, player_names)
    if not winner:
        input("")

if winner == 1:
    print("Winner:", player_names[winners[0]])
else:
    print("Winners:", ', '.join([player_names[i] for i in winners]))

print(f"\nThis game lasted {round(counter, 1)} sec")
