import os,time

def that_completely_unnecessary_loading_screen():

  for i in range(101):
    print(i*"_" + (100-i)*"-" + "\n")
    print(i*" " + "LOADING...")
    time.sleep(0.05)
    os.system('clear')

that_completely_unnecessary_loading_screen()

cardType = input(
"""Validate Card

Select a card type:
[1] American Express (15 digits)
[2] Visa (13 or 16 digits)
[3] MasterCard (16 digits)

 > """)

def mod10(cardNum):
  total = 0
  for i in range(len(cardNum)):
    if i % 2 == 0:
      doubled = int(cardNum[i]) * 2
      if doubled < 10:
        total += doubled
      else:
        doubled = str(doubled)
        new = 0
        for c in doubled:
          new += int(c)
        total += new
    else:
      total += int(cardNum[i])
  return total % 10 == 0

def amex():

  num = input("Enter your card number.\nYou can use a SPACE to separate numbers.\n")
  num = num.replace(" ","")
  if len(num) != 15:
    return f"Wrong number of digits ({len(num)} instead of 15)"
  if num[0] != '3' or (num[1] != '4' and num[1] != '7'):
    return f"Not a valid AMEX card - must start in 34 or 37"
  return mod10(num)

def visa():

  num = input("Enter your card number.\nYou can use a SPACE to separate numbers.\n")
  num = num.replace(" ","")
  if len(num) != 16 and len(num) != 13:
    return f"Wrong number of digits ({len(num)} instead of 13 or 16)"
  if num[0] != '4':
    return f"Not a valid VISA card - must start in 4"
  return mod10(num)

def mastercard():

  num = input("Enter your card number.\nYou can use a SPACE to separate numbers.\n")
  num = num.replace(" ","")
  if len(num) != 16:
    return f"Wrong number of digits ({len(num)} instead of 16)"
  if num[0] != '5' or (num[1] != '1' and num[1] != '5'):
    return f"Not a valid MASTERCARD card - must start in 51 or 55"
  return mod10(num)

os.system('clear')

if '1' in cardType:
  print(amex())
elif '2' in cardType:
  print(visa())
elif '3' in cardType:
  print(mastercard())