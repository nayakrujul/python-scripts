import sys, time, random

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  BLACK = '\033[1;30;40m'
  RED = '\033[1;31;40m'
  GREEN = '\033[1;32;40m'
  YELLOW = '\033[1;33;40m'
  BLUE = '\033[1;34;40m'
  PURPLE = '\033[1;35;40m'
  CYAN = '\033[1;36;40m'
  WHITE = '\033[1;37;40m'

print(f"{bcolors.HEADER}Learn Vocab{bcolors.ENDC}\n")
print(f"{bcolors.WARNING}BEFORE YOU START: Make sure the text file is in this format{bcolors.ENDC}\n")
print(f"{bcolors.BOLD}Word : Definition\nWord : Definition{bcolors.ENDC}\n")
input(f"{bcolors.WARNING}Continue? {bcolors.ENDC}")

with open("vocab.txt", "rt") as f:
  vocab = f.read()

vocabDict = {}

running = True
words = 0

while running:
  if " : " in vocab:
    partition1 = str.partition(vocab, " : ")
    partition2 = str.partition(str(partition1[2]), "\n")
    vocabDict.update({partition1[0]: partition2[0]})
    vocab = partition2[2]
    words += 1
  else:
    running = False

if words == 0:
  print(f"{bcolors.FAIL}Words in incorrect format.")
  sys.exit()

print("\nYou have", words, "words.\n")

wordsRemaining = input(f"{bcolors.BOLD}Type in the number of words you want to revise: ")

if str.isdigit(str(wordsRemaining)):
  print("\nStarting in...")
  time.sleep(1)
  print("3...")
  time.sleep(1)
  print("2...")
  time.sleep(1)
  print("1...")
  time.sleep(1)

else:
  print(f"{bcolors.FAIL}Not a number.")
  sys.exit()

wordsRemaining = int(wordsRemaining)

if wordsRemaining == 0:
  print(f"{bcolors.FAIL}Cannot be 0.")
  sys.exit()

if wordsRemaining > words:
  print(f"{bcolors.FAIL}Cannot be more than total words.")
  sys.exit()

print(f"{bcolors.ENDC}")
score = 0
wrong = 0

while wordsRemaining > 0:

  vocabDictkeys = []
  for key in vocabDict:
    vocabDictkeys.append(key)

  word = random.choice(vocabDictkeys)
  answer = str(input(str(word) + ": "))

  if answer == vocabDict[word]:
    print(f"{bcolors.OKGREEN}Correct.\n{bcolors.ENDC}")
    score += 1
  else:
    print(f"{bcolors.FAIL}Wrong.{bcolors.ENDC} {vocabDict[word]}\n")
    wrong += 1

  vocabDict.pop(word)
  wordsRemaining -= 1

print("You got", score, "out of", score+wrong)