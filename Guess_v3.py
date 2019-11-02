points = 0
ext = 0
while(ext != 1):
    print("")
    num1 = raw_input("Enter lowest number. ")
    num2 = raw_input("Enter highest number. ")
    if(str.isdigit(str(num1)) and str.isdigit(str(num2))):
        if(int(num2) > int(num1)):
            import random
            num = random.randint(int(num1),int(num2))
            total = int(num1) + int(num2)
            average = total / 2
            cap = int(num2) / (random.randint(2,7))
            factor = 3
            print("I am thinking of a number between " + str(num1) + " and " + str(num2) + ".")
            if(num % 2 == 0):
                print("It is even.")
            else:
                print("It is odd.")
            while(factor <= cap):
                if(num % factor == 0):
                    print("It is a multiple of " + str(factor) + ".")
                    factor = factor + 1
                else:
                    print("It is not a multiple of " + str(factor) + ".")
                    factor = factor + 1
            print("")
            if(num >= average):
                print("It is greater than or equal to " + str(average) + ".")
            else:
                print("It is less than " + str(average) + ".")
            exitCount = 0
            guesses = 1
            while(exitCount == 0):
                print("")
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
                        points = points + int((((float(num2) - float(num1))) / guesses))
                        print("You have " + str(points) + " points.")
                elif(str.lower(guess) == "exit"):
                    exitCount = 1
                elif(str.lower(guess) == "hint"):
                    guesses = guesses + 1
                    if(len(str(num)) == 1):
                        print("It is one-digit.")
                    elif(len(str(num)) >= 2):
                        print("It starts with " + str(num)[0] + ".")
                else:
                    print("Only accepts numbers.")
        else:
            print("Higher number has to be higher than lower number.")
    else:
        print("Only accepts numbers.")
    print("")
    playAgain = raw_input("Would you like to play again? ")
    print("")
    if(str.lower(playAgain) == "yes"):
        import random
        exitLoop = random.randint(5,10)
        while(exitLoop >= 0):
            print("Loading the game...")
            print("")
            import time
            import random
            time.sleep(random.randint(1,5))
            exitLoop = exitLoop - 1
        ext = 0
    else:
        print("We took that as a 'NO'. Thank you for playing.")
        ext = 1
print("")
