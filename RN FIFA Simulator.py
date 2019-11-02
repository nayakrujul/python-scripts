print("")
print("Welcome to RN FIFA Simulator.")
teamScore = 0
oppScore = 0
team = input("Please select your team. ")
opponent = input("Please select your opponent's team. ")
if(len(team) >= 3 and len(opponent) >= 3 and team != opponent):
    teamShort = team[0] + team[1] + team[2]
    oppShort = opponent[0] + opponent[1] + opponent[2]
    print("")
    print(str.upper(teamShort) + " (" + team + ") " + str(teamScore) + " - " + str(oppScore) + " " + str.upper(oppShort) + " (" + opponent + ")")
    mins = 0
    print("")
    while(mins <= 90):
        import random
        wait = random.randint(1,7)
        number = random.randint(1,50)
        letter1 = random.randint(2,4)
        letters = letter1 * 2
        scoreMiss = random.randint(1,4)
        mins = mins + wait
        name = ""
        while(letters > 0):
            if(letters % 2 == 0):
                import random
                letter = random.randint(1,18)
                if(letter == 1):
                    name = name + "B"
                elif(letter == 2):
                    name = name + "C"
                elif(letter == 3):
                    name = name + "D"
                elif(letter == 4):
                    name = name + "F"
                elif(letter == 5):
                    name = name + "G"
                elif(letter == 6):
                    name = name + "H"
                elif(letter == 7):
                    name = name + "J"
                elif(letter == 8):
                    name = name + "K"
                elif(letter == 9):
                    name = name + "L"
                elif(letter == 10):
                    name = name + "M"
                elif(letter == 11):
                    name = name + "N"
                elif(letter == 12):
                    name = name + "P"
                elif(letter == 13):
                    name = name + "R"
                elif(letter == 14):
                    name = name + "S"
                elif(letter == 15):
                    name = name + "T"
                elif(letter == 16):
                    name = name + "V"
                elif(letter == 17):
                    name = name + "W"
                elif(letter == 18):
                    name = name + "Z"
            else:
                import random
                letter = random.randint(1,5)
                if(letter == 1):
                    name = name + "A"
                elif(letter == 2):
                    name = name + "E"
                elif(letter == 2):
                    name = name + "I"
                elif(letter == 2):
                    name = name + "O"
                elif(letter == 2):
                    name = name + "U"
            letters = letters - 1
        import time
        time.sleep(wait)
        if(scoreMiss == 1):
            print(team + " player " + name + " (number " + str(number) + ") scored! " + str(mins) + " mins.")
            teamScore = teamScore + 1
        elif(scoreMiss == 2):
            print(opponent + " player " + name + " (number " + str(number) + ") scored! " + str(mins) + " mins.")
            oppScore = oppScore + 1
        elif(scoreMiss == 3):
            print(team + " player " + name + " (number " + str(number) + ") missed! " + str(mins) + " mins.")
        elif(scoreMiss == 4):
            print(opponent + " player " + name + " (number " + str(number) + ") missed! " + str(mins) + " mins.")
        print(str.upper(teamShort) + " (" + team + ") " + str(teamScore) + " - " + str(oppScore) + " " + str.upper(oppShort) + " (" + opponent + ")")
        print("")
    print("Time up!")
    if(teamScore > oppScore):
        print("You won!")
    elif(teamScore < oppScore):
        print("You lost!")
    else:
        ext = 0
        while(ext == 0):
            print("Draw! Penalties!")
            import random
            yourScore = random.randint(0,5)
            otherScore = random.randint(0,5)
            import time
            time.sleep(random.randint(1,5))
            print("You scored " + str(yourScore) + " and your opponent scored " + str(otherScore))
            print("")
            if(yourScore > otherScore):
                print("You won!")
                ext = 1
            elif(yourScore < otherScore):
                print("You lost!")
                ext = 1
else:
    print("Must be at least 3 characters and teams cannot be same.")
print("")
penalties = inputinput("Would you like to practise your penalties? ")
if(str.lower(penalties) == "yes" or str.lower(penalties) == "y"):
    ext = 0
    while(ext == 0):
        print("Penalties!")
        import random
        yourScore = random.randint(0,5)
        otherScore = random.randint(0,5)
        import time
        time.sleep(random.randint(1,5))
        print("You scored " + str(yourScore) + " and your opponent scored " + str(otherScore))
        print("")
        if(yourScore > otherScore):
            print("You won!")
            ext = 1
        elif(yourScore < otherScore):
            print("You lost!")
            ext = 1
    print("")
