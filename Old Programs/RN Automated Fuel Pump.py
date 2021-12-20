print("Welcome to RN Fuel")

fuel = input("Which fuel would you like? ")

import random
for x in range(1):
  cost = random.randint(100,130)

print(fuel + " fuel costs " + str(cost) + " pence per litre.")

litres = input("How many litres would you like? ")

ans = float(litres) * (float(cost) / 100)

ansans = round(ans, 2)

print("Please pay £" + str(ansans))

card = input("Enter your card number. ")

while not (int(card) > 999999999999999 and int(card) < 10000000000000000):
  card = input("This card number is invalid. Enter a valid card number. ")

code = input("Enter the three digit security code on the back of your card. ")

while not (int(code) > 99 and int(code) < 1000):
  code = input("This code is invalid. Enter a valid three digit security code. ")

expiry = input("Enter the expiry year. ")

while not (int(expiry) > 2019):
  expiry = input("This expiry year is invalid. Enter a valid expiry year. ")

print("Thank you for coming to RN fuel. We hope you drive away happy!")
  
# Go to https://repl.it/repls/MuddyFormalSoftwareagent (Command + Click)
## Thank you