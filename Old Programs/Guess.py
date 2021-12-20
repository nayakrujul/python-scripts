print("")
import random
num = random.randint(1,99)
factor = 3
print("I am thinking of a number between 1 and 99.")
if(num % 2 == 0):
    print("It is even.")
else:
    print("It is odd.")
while(factor <= 12):
    if(num % factor == 0):
        print("It is a multiple of " + str(factor) + ".")
        factor = factor + 1
    else:
        print("It is not a multiple of " + str(factor) + ".")
        factor = factor + 1
if(num >= 50):
    print("It is greater than or equal to 50.")
else:
    print("It is less than 50.")
exitCount = 0
guesses = 1
while(exitCount == 0):
    guess = raw_input("Guess the number: ")
    if(str.isdigit(str(guess))):
        if(int(guess) > num):
            print("Lower.")
            guesses = guesses + 1
        elif(int(guess) < num):
            print("Higher.")
            guesses = guesses + 1
        else:
            print("Guessed it in " + str(guesses) + " guesses!")
            exitCount = 1
print("")