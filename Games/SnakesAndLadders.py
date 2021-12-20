import sys, os, random, time, threading, math

def checkRobot(n): # Returns False for not a robot and True for robot

  from random import randint as r

  print("Welcome to the RN Robot Checking Service.")

  randnum = r(1,n)
  if randnum == 1:
    return False
  
  num = str(r(10000,99999))
  num1 = {
    "10": "Ten thousand",
    "11": "Eleven thousand",
    "12": "Twelve thousand",
    "13": "Thirteen thousand",
    "14": "Fourteen thousand",
    "15": "Fifteen thousand",
    "16": "Sixteen thousand",
    "17": "Seventeen thousand",
    "18": "Eighteen thousand",
    "19": "Nineteen thousand",
    "20": "Twenty thousand",
    "21": "Twenty-one thousand",
    "22": "Twenty-two thousand",
    "23": "Twenty-three thousand",
    "24": "Twenty-four thousand",
    "25": "Twenty-five thousand",
    "26": "Twenty-six thousand",
    "27": "Twenty-seven thousand",
    "28": "Twenty-eight thousand",
    "29": "Twenty-nine thousand",
    "30": "Thirty thousand",
    "31": "Thirty-one thousand",
    "32": "Thirty-two thousand",
    "33": "Thirty-three thousand",
    "34": "Thirty-four thousand",
    "35": "Thirty-five thousand",
    "36": "Thirty-six thousand",
    "37": "Thirty-seven thousand",
    "38": "Thirty-eight thousand",
    "39": "Thirty-nine thousand",
    "40": "Forty thousand",
    "41": "Forty-one thousand",
    "42": "Forty-two thousand",
    "43": "Forty-three thousand",
    "44": "Forty-four thousand",
    "45": "Forty-five thousand",
    "46": "Forty-six thousand",
    "47": "Forty-seven thousand",
    "48": "Forty-eight thousand",
    "49": "Forty-nine thousand",
    "50": "Fifty thousand",
    "51": "Fifty-one thousand",
    "52": "Fifty-two thousand",
    "53": "Fifty-three thousand",
    "54": "Fifty-four thousand",
    "55": "Fifty-five thousand",
    "56": "Fifty-six thousand",
    "57": "Fifty-seven thousand",
    "58": "Fifty-eight thousand",
    "59": "Fifty-nine thousand",
    "60": "Sixty thousand",
    "61": "Sixty-one thousand",
    "62": "Sixty-two thousand",
    "63": "Sixty-three thousand",
    "64": "Sixty-four thousand",
    "65": "Sixty-five thousand",
    "66": "Sixty-six thousand",
    "67": "Sixty-seven thousand",
    "68": "Sixty-eight thousand",
    "69": "Sixty-nine thousand",
    "70": "Seventy thousand",
    "71": "Seventy-one thousand",
    "72": "Seventy-two thousand",
    "73": "Seventy-three thousand",
    "74": "Seventy-four thousand",
    "75": "Seventy-five thousand",
    "76": "Seventy-six thousand",
    "77": "Seventy-seven thousand",
    "78": "Seventy-eight thousand",
    "79": "Seventy-nine thousand",
    "80": "Eighty thousand",
    "81": "Eighty-one thousand",
    "82": "Eighty-two thousand",
    "83": "Eighty-three thousand",
    "84": "Eighty-four thousand",
    "85": "Eighty-five thousand",
    "86": "Eighty-six thousand",
    "87": "Eighty-seven thousand",
    "88": "Eighty-eight thousand",
    "89": "Eighty-nine thousand",
    "90": "Ninety thousand",
    "91": "Ninety-one thousand",
    "92": "Ninety-two thousand",
    "93": "Ninety-three thousand",
    "94": "Ninety-four thousand",
    "95": "Ninety-five thousand",
    "96": "Ninety-six thousand",
    "97": "Ninety-seven thousand",
    "98": "Ninety-eight thousand",
    "99": "Ninety-nine thousand"
  }

  num2 = {
    "0": " and ",
    "1": ", one hundred and ",
    "2": ", two hundred and ",
    "3": ", three hundred and ",
    "4": ", four hundred and ",
    "5": ", five hundred and ",
    "6": ", six hundred and ",
    "7": ", seven hundred and ",
    "8": ", eight hundred and ",
    "9": ", nine hundred and ",
  }

  num3 = {
    "01": "One",
    "02": "Two",
    "03": "Three",
    "04": "Four",
    "05": "Five",
    "06": "Six",
    "07": "Seven",
    "08": "Eight",
    "09": "Nine",
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen",
    "20": "Twenty",
    "21": "Twenty-one",
    "22": "Twenty-two",
    "23": "Twenty-three",
    "24": "Twenty-four",
    "25": "Twenty-five",
    "26": "Twenty-six",
    "27": "Twenty-seven",
    "28": "Twenty-eight",
    "29": "Twenty-nine",
    "30": "Thirty",
    "31": "Thirty-one",
    "32": "Thirty-two",
    "33": "Thirty-three",
    "34": "Thirty-four",
    "35": "Thirty-five",
    "36": "Thirty-six",
    "37": "Thirty-seven",
    "38": "Thirty-eight",
    "39": "Thirty-nine",
    "40": "Forty",
    "41": "Forty-one",
    "42": "Forty-two",
    "43": "Forty-three",
    "44": "Forty-four",
    "45": "Forty-five",
    "46": "Forty-six",
    "47": "Forty-seven",
    "48": "Forty-eight",
    "49": "Forty-nine",
    "50": "Fifty",
    "51": "Fifty-one",
    "52": "Fifty-two",
    "53": "Fifty-three",
    "54": "Fifty-four",
    "55": "Fifty-five",
    "56": "Fifty-six",
    "57": "Fifty-seven",
    "58": "Fifty-eight",
    "59": "Fifty-nine",
    "60": "Sixty",
    "61": "Sixty-one",
    "62": "Sixty-two",
    "63": "Sixty-three",
    "64": "Sixty-four",
    "65": "Sixty-five",
    "66": "Sixty-six",
    "67": "Sixty-seven",
    "68": "Sixty-eight",
    "69": "Sixty-nine",
    "70": "Seventy",
    "71": "Seventy-one",
    "72": "Seventy-two",
    "73": "Seventy-three",
    "74": "Seventy-four",
    "75": "Seventy-five",
    "76": "Seventy-six",
    "77": "Seventy-seven",
    "78": "Seventy-eight",
    "79": "Seventy-nine",
    "80": "Eighty",
    "81": "Eighty-one",
    "82": "Eighty-two",
    "83": "Eighty-three",
    "84": "Eighty-four",
    "85": "Eighty-five",
    "86": "Eighty-six",
    "87": "Eighty-seven",
    "88": "Eighty-eight",
    "89": "Eighty-nine",
    "90": "Ninety",
    "91": "Ninety-one",
    "92": "Ninety-two",
    "93": "Ninety-three",
    "94": "Ninety-four",
    "95": "Ninety-five",
    "96": "Ninety-six",
    "97": "Ninety-seven",
    "98": "Ninety-eight",
    "99": "Ninety-nine"
  }

  fullinput = num1[(num[0] + num[1])] + num2[(num[2])] + num3[(num[3] + num[4])]
  answer = input("Enter " + str(fullinput) + " as a number: ")
  if str(answer) == num:
    return False
  else:
    return True

if(checkRobot(3)):
  sys.exit()
else:
  os.system('clear')
  print("Welcome to Snakes and Ladders \n")

p1name = input("Player 1, enter your name: ")
p2name = input("Player 2, enter your name: ")

board = []
for i in range(1,101):
  board.append(str.zfill(str(i),2))

def printBoard():
  print(board[99], "|", board[98], "|", board[97], "|", board[96], "|", board[95], "|", board[94], "|", board[93], "|", board[92], "|", board[91], "|", board[90])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[80], "|", board[81], "|", board[82], "|", board[83], "|", board[84], "|", board[85], "|", board[86], "|", board[87], "|", board[88], "|", board[89])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[79], "|", board[78], "|", board[77], "|", board[76], "|", board[75], "|", board[74], "|", board[73], "|", board[72], "|", board[71], "|", board[70])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[60], "|", board[61], "|", board[62], "|", board[63], "|", board[64], "|", board[65], "|", board[66], "|", board[67], "|", board[68], "|", board[69])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[59], "|", board[58], "|", board[57], "|", board[56], "|", board[55], "|", board[54], "|", board[53], "|", board[52], "|", board[51], "|", board[50])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[40], "|", board[41], "|", board[42], "|", board[43], "|", board[44], "|", board[45], "|", board[46], "|", board[47], "|", board[48], "|", board[49])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[39], "|", board[38], "|", board[37], "|", board[36], "|", board[35], "|", board[34], "|", board[33], "|", board[32], "|", board[31], "|", board[30])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[20], "|", board[21], "|", board[22], "|", board[23], "|", board[24], "|", board[25], "|", board[26], "|", board[27], "|", board[28], "|", board[29])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[19], "|", board[18], "|", board[17], "|", board[16], "|", board[15], "|", board[14], "|", board[13], "|", board[12], "|", board[11], "|", board[10])
  print("----|----|----|----|----|----|----|----|----|----")
  print("", board[0], "|", board[1], "|", board[2], "|", board[3], "|", board[4], "|", board[5], "|", board[6], "|", board[7], "|", board[8], "|", board[9])

def timer():
  global counter
  counter = 0
  while gameRunning:
    time.sleep(1)
    counter += 1

p1pos = 0
p2pos = 0
ladders = {
  1: 38,
  4: 14,
  8: 30,
  21: 42,
  28: 76,
  50: 67,
  71: 92,
  80: 99
}
snakes = {
  32: 10,
  # 36: 6,
  48: 26,
  # 62: 18,
  88: 24,
  # 95: 56,
  97: 78
}

gameRunning = True
myThread = threading.Thread(target=timer)
myThread.start()
while gameRunning:
  os.system('clear')
  printBoard()

  print("\n" + str(p1name))
  input("Press enter to roll dice.")
  dice = random.randint(1,6)
  print("You rolled a", dice)
  time.sleep(2)

  p1pos += dice
  if p1pos in ladders:
    p1pos = ladders[p1pos]
    print("Ladder! Up to", p1pos)
    time.sleep(2)
  elif p1pos in snakes:
    p1pos = snakes[p1pos]
    print("Snake! Down to", p1pos)
    time.sleep(2)
  
  if p1pos >= 100:
    print("Winner!")
    p1pos = 100
    i = 0
    while i < 100:
      board[i] = str.zfill(str((i+1)),2)
      i += 1
    board[99] = "\033[1;31;40m P1\033[1;37;0m"
    board[(p2pos-1)] = "\033[1;31;40mP2\033[1;37;0m"
    break

  i = 0
  while i < 100:
    board[i] = str.zfill(str((i+1)),2)
    i += 1

  board[(p1pos-1)] = "\033[1;31;40mP1\033[1;37;0m"
  if p2pos != 0:  
    board[(p2pos-1)] = "\033[1;31;40mP2\033[1;37;0m"

  os.system('clear')
  printBoard()

  print("\n" + str(p2name))
  input("Press enter to roll dice.")
  dice = random.randint(1,6)
  print("You rolled a", dice)
  time.sleep(2)

  p2pos += dice
  if p2pos in ladders:
    p2pos = ladders[p2pos]
    print("Ladder! Up to", p2pos)
    time.sleep(2)
  elif p2pos in snakes:
    p2pos = snakes[p2pos]
    print("Snake! Down to", p2pos)
    time.sleep(2)
  
  if p2pos >= 100:
    print("Winner!")
    p2pos = 100
    i = 0
    while i < 100:
      board[i] = str.zfill(str((i+1)),2)
      i += 1
    board[(p1pos-1)] = "\033[1;31;40mP1\033[1;37;0m"
    board[99] = "\033[1;31;40m P2\033[1;37;0m"
    break

  i = 0
  while i < 100:
    board[i] = str.zfill(str((i+1)),2)
    i += 1

  board[(p1pos-1)] = "\033[1;31;40mP1\033[1;37;0m"
  board[(p2pos-1)] = "\033[1;31;40mP2\033[1;37;0m"
gameRunning = False
os.system('clear')
printBoard()

print("\nThanks for playing!")
mins = math.floor(counter/60)
secs = counter - (mins*60)
print("This game lasted", str(mins) + ":" + str(secs))