from os import system
from statistics import mean
from random import randint

values = [0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 250, 500, 750, 1000, 3000, 5000, 10000, 15000, 20000, 35000, 50000, 75000, 100000, 250000]

def calc():
  amt = mean(values)
  if len(values) > 6:
    amt /= (len(values) / randint(3,6))
  return "£" + str(round(amt))

loop = True
while loop:

  system('clear')

  for i in range(len(values)):
    if values[i] != 0.1 and values[i] != 0.5:
      print(f"[{i+1}] - £{values[i]}")
    else:
      print(f"[{i+1}] - £{values[i]}0")

  loop2 = True
  while loop2:
    remove = str(input("\nRemove value "))
    if remove.isdigit():
      remove = int(remove)
      if remove <= len(values) and remove >= 1:
        loop2 = False
        if values[remove-1] != 0.1 and values[remove-1] != 0.5:
          print(f"Removed £{values[remove-1]}")
        else:
          print(f"Removed £{values[remove-1]}0")
        values.pop(remove-1)
    elif remove.lower() == "exit":
      loop = False
      loop2 = False

  input(f"\nThe banker's offer will be somewhere around {calc()}")

  if len(values) == 1:
    loop = False