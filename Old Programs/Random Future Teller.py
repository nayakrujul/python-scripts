print("")

testlist = [1, 2, 3]

def test():
  testlist.append(4)
  print(testlist)

test()

print("")

print("-------------------------------------")

print("")

quesion = input('Ask me a yes/no question and I will tell your future. ')

import random
for x in range(1):
  number = random.randint(1,8)

if number == 1:
  print("Yes. ")

elif number == 2:
  print("Maybe. ")

elif number == 3:
  print("No. ")

elif number == 4:
  print("The future is unclear. ")

elif number == 5:
  print("Of course")

elif number == 6:
  print("Do you really want to know the answer")

elif number == 7:
  print("Of course not")

elif number == 8:
  print("I don't know")

# Go to https://repl.it/repls/GrimyEvergreenLocatorprogram (Command + Click)
## Thank you