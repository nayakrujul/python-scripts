import os,time

def that_completely_unnecessary_loading_screen():

  for i in range(101):
    print(i*"_" + (100-i)*"-" + "\n")
    print(i*" " + "LOADING...")
    time.sleep(0.05)
    os.system('clear')

that_completely_unnecessary_loading_screen()

print("Check ISBN Number\n\nType 'help' to find out how it works")


def check(s):

  if type(s) != type("abc"):

    return "Wrong format."

  s = s.replace("-","")

  if not s.isdigit():

    return "Has other non-numeric characters."
  
  if len(s) != 13:

    return "Wrong number of digits."
  
  total = 0

  for c in range(len(s)):

    if c % 2 == 0:

      total += int(s[c])
    
    else:

      total += int(s[c]) * 3

  return total % 10 == 0

loop = True

while loop:

  isbn = str(input("\nISBN "))

  if isbn != "":
    if 'help' in isbn.lower():
      print(
        """
-----------------------------------------------------
|               How this program works:             |
|  We are checking the ISBN-13 Number by the Check  |
|                Digit (the last one).              |
|                                                   |
|  If you go through the whole number, adding three |
|    times the digit for every odd-numbered digit   |
|    (e.g. if the 5th digit is 6, add 18) and one   |
|   times the digit for every even-numbered digit   |
|     (e.g. if the 8th digit is 9, add 9), if the   |
|    value adds to a multiple of 10 (e.g. 120), it  |
|       is a correct ISBN. Otherwise, it is not.    |
|                                                   |
|  You can add dashes, '-', wherever you want. The  |
|            program will ignore them.              |
|                                                   |
|       You are running v3.0 - September 2021.      |
-----------------------------------------------------
        """
        )
    else: 
      print(check(isbn))
  else:
    loop = False