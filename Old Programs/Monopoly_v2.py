play_again = "Y"

while(play_again == "Yes" or play_again == "yes" or play_again == "Y" or play_again == "y"):
    exit = 0
    cash = 2500
    properties = 0
    print("")
    print("Welcome to Monopoly. ")
    while(exit == 0 and (cash + (properties * 200)) >= 1):
        print("")
        print("Rolling the dices...")
        import random
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        property_value = random.randint(5,50)
        property_value2 = property_value * 10
        property_owner = random.randint(1,3)
        rent = random.randint(1,50)
        print("The values are " + str(roll1) + " and " + str(roll2))
        if(roll1 == roll2):
            cash = cash + int(((roll1) * 100))
            print("You got a double " + str(roll1) + ". You got " + str(((roll1) * 100))  + " bonus cash. You have " + (str(int(cash) + (int(properties) * 200))) + " cash remaining.")
        print("")
        if(property_owner == 1):
            print("The property that you are on belongs to someone else. Please pay " + str(rent) + " cash. You have " + 
            (str(int(cash) + (int(properties) * 200))) + " cash remaining.")
            cash = cash - rent
            print("You have " + (str(int(cash) + (int(properties) * 200))) + " cash remaining.")
        elif(property_owner == 2):
            print("The property that you are on belongs to yourself. Please carry on.")
            import random
            rent2 = random.randint(1,50)
            print("You got " + str(rent2) + " rent.")
            cash = cash + rent2
            print("You have " + (str(int(cash) + (int(properties) * 200))) + " cash remaining.")
        elif(property_owner == 3):
            buy = raw_input("The property that you are on belongs to the bank. Would you like to buy it for " + str(property_value2) + " cash. You have " + (str(int(cash) + (int(properties) * 200))) + " cash remaining. ")
            if(buy == "Yes" or buy == "yes" or buy == "Y" or buy == "y"):
                cash = cash - property_value2
                properties = properties + 1
                import random
                rent2 = random.randint(1,50)
                print("You got " + str(rent2) + " rent.")
                cash = cash + rent2
                print("You have " + (str(int(cash) + (int(properties) * 200))) + " cash remaining.")

        check = raw_input("Do you want to count cash now? ")
        if(check == "Yes" or check == "yes" or check == "Y" or check == "y"):
            exit = 1
        elif(check == "Pw. Win"):
            password = raw_input("Password. ")
            if(password == "RN Pw."):
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("Well done Rujul. You win.")
                exit = 1
                cash = cash * 10
            else:
                print("You hacker!")
                cash = cash / 10
    print("")
    print("Your cash is " + str(cash) + " and " + str(properties) + " properties at 200 cash per property, totalling " + str(int(cash) + (int(properties) * 200)) + " cash, giving you a profit of " + (str(int(cash) + (int(properties) * 200) - 2500)) + ". Thank you for playing.")
    play_again = raw_input("Would you like to play again? ")
    
print("")
print("-----------------------------------------------------")
print("")