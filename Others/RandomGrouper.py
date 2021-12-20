from random import shuffle, randint, choice
from os import system
from time import sleep
from math import ceil



f = open("names.txt")
names = f.read().split("\n")
f.close()



max_group = input('Max in each group: ')

if not max_group.isdigit():
  max_group = len(names)
max_group = int(max_group)
if max_group > len(names):
  max_group = len(names)

display = input("Display setting (1-5): ")
if display not in ("1","2","3","4","5"):
  display = "1"

total_groups = ceil(len(names) / max_group)



groups = []
[groups.append([]) for times in range(total_groups)]


def display1():

  shuffle(names)

  for group in range(1, total_groups + 1):

    print(f"\033[1;{30+group}mGroup", group)

    if group < total_groups:

      for name_index in range((group - 1) * max_group, group * max_group):

        print(names[name_index])
    
    else:

      for name_index in range((group - 1) * max_group, len(names)):

        print(names[name_index])
    
    print("\n")


def display2():

  global groups

  groups = []
  [groups.append([]) for times in range(total_groups)]

  for name in names:

    group = randint(1, total_groups)
    while len(groups[group - 1]) >= max_group:
      group = randint(1, total_groups)

    print(f"\033[1;{30+group}m{name} - {group}")
    groups[group - 1].append(0)


def display3():

  global groups

  for group in range(len(groups)):
    print(f"\033[1;{31+group}mGroup ", group + 1, '\n', '\n'.join(groups[group]), '\033[1;0m\n', sep='')
  
  print("\n")
  print("\n".join(names))

  try:

    name = choice(names)
    names.remove(name)

    group = randint(0, total_groups - 1)
    while len(groups[group]) >= max_group:
      group = randint(0, total_groups - 1)
    
    groups[group].append(name)
  
  except:
    pass


def display4():

  global groups

  print('\n'.join(names))
  input("\nPress RETURN to colour. ")

  system('clear')

  for name in names:

    group = randint(0, total_groups - 1)
    while len(groups[group]) >= max_group:
      group = randint(0, total_groups - 1)

    groups[group].append(0)
    print(f"\033[1;{31 + group}m{name} - {group + 1}")

  print("\033[1;0m\nPress RETURN to colour. ")


def display5():

  for times in range(randint(5, 20)):

    system('clear')

    shuffle(names)
      
    print("\n".join(names))

    sleep(0.2)

  system('clear')

  group = 0

  for index in range(len(names)):

    if index % max_group == 0:

      group += 1
      print(f"\033[1;{30+group}m",end="")

    print(names[index])



if display in ("1","2"):

  for times in range(randint(5, 20)):

    try:
      system('clear')
    except:
      system('cls')

    if display == "1":

      display1()
    
    else:

      display2()

    sleep(0.2)


elif display == "3":

  for times in range(len(names) + 1):

    try:
      system('clear')
    except:
      system('cls')

    display3()

    sleep(0.2)


elif display == "4":

  system('clear')
  display4()


elif display == "5":

  display5()



print('\033[1;0m')