from random import shuffle
from os import system
from time import sleep


def get_cards():

    nums = [str(x) for x in range(2, 11)] + ["J", "Q", "K", "A"]
    suits = ["H", "D", "S", "C"]
    cards = [y + z for y in nums for z in suits]
    shuffle(cards)
    return cards[:21]


def display(lst, rows=7):

    print("Col 1   Col 2   Col 3")
    if rows > 0:
        print(lst[0], lst[1], lst[2], sep="\t")
    if rows > 1:
        print(lst[3], lst[4], lst[5], sep="\t")
    if rows > 2:
        print(lst[6], lst[7], lst[8], sep="\t")
    if rows > 3:
        print(lst[9], lst[10], lst[11], sep="\t")
    if rows > 4:
        print(lst[12], lst[13], lst[14], sep="\t")
    if rows > 5:
        print(lst[15], lst[16], lst[17], sep="\t")
    if rows > 6:
        print(lst[18], lst[19], lst[20], sep="\t")


def animation(lst, rev=0):

    if rev:
        for rows in reversed(range(8)):
            system('clear')
            print("Is your card in:")
            display(lst, rows)
            sleep(.2)
    else:
        for rows in range(8):
            system('clear')
            print("Is your card in:")
            display(lst, rows)
            sleep(.2)


def animation2(lst):

    lst2 = lst[::]

    for item in range(10):

        system('clear')
        print("Is your card in:")
        shuffle(lst2)
        display(lst2)
        sleep(.25)


system('clear')
cards_list = get_cards()

print("Choose a card from the below list and keep it in mind.\n")
for x in range(3):
    for y in range(7):
        card = cards_list[(x * 7) + y]
        print(card + (5 - len(card)) * " ", end="")
    print("")

input("\nPress return when you're done.")

shuffle(cards_list)

for times in range(3):

    system('clear')
    print("Is your card in:")
    display(cards_list)

    while True:
        col = input("1, 2, or 3? ")
        if col in ["1", "2", "3"]:
            break
        print("Try again.")

    if times == 0:
        animation(cards_list, 1)
    elif times == 1:
        animation2(cards_list)

    col = int(col) - 1
    first = list(reversed(cards_list[::3]))
    second = list(reversed(cards_list[1::3]))
    third = list(reversed(cards_list[2::3]))
    order = [
        second + first + third,
        first + second + third,
        first + third + second
    ]
    cards_list = order[col]

    if times == 0:
        animation(cards_list)

system('clear')
print(f"Your card is {cards_list[10]}")
