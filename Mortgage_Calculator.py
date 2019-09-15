print("")
print("Welcome to RN Mortgage Calculator.")
amount = input("Please enter amount without interest (Do not include currency symbol). ")
if(str.isdigit(str(amount))):
    years = input("Please enter years. ")
    amount = float(amount) + (float(amount) * 0.03)
    amount = round(amount, 2)
    if(str.isdigit(str(years))):
        yearsComplete = input("Please enter years that have been completed. ")
        months = int(years) * 12
        if(str.isdigit(str(yearsComplete)) and int(yearsComplete) < int(years)):
            amountComplete = input("Please enter the amount that you have paid already (Do not include currency symbol). ")
            monthsComplete = int(yearsComplete) * 12
            if(str.isdigit(str(amountComplete)) and int(amountComplete) < int(amount)):
                amountLeft = float(amount) - int(amountComplete)
                amountLeft = round(amountLeft, 2)
                monthsLeft = months - monthsComplete
                averageLeft = amountLeft / monthsLeft
                print("You have to pay " + str(amountLeft) + " in " + str(monthsLeft) + " months at " + str(averageLeft) + " per month.")
                average = float(amount) / months
                average = round(average, 2)
                if(average < averageLeft):
                    aboveBelow = "below"
                    end = "You've got to pay up quickly!"
                elif(average > averageLeft):
                    aboveBelow = "above"
                    end = "You can sit back and relax!"
                else:
                    aboveBelow = "on"
                    end = "You're right on the mark!"
                print("You are " + aboveBelow + " average. The average for the full mortgage is " + str(average) + " per month and your average left is " + str(averageLeft) + " per month. " + end)
            
            elif(amountComplete >= amount):
                print("Amount complete must be less than amount")
            
            else:
                print("Please enter a number instead.")

        elif(yearsComplete >= years):
            print("Years complete must be less than years")
        
        else:
            print("Please enter a number instead.")

    else:
        print("Please enter a number instead (currency symbols not allowed).")

else:
    print("Please enter a number instead (currency symbols not allowed).")

print("")