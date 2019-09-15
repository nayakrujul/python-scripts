print("")
numList = []
quitCheck = 0
numCount = 0
print("Welcome to RN Average Calculator")
while(quitCheck == 0):
    number = raw_input("Enter your number. Enter a blank number to exit. You have entered " + str(numCount) + " numbers: ")
    if(str.isdigit(number)):
        if(len(str(int(number))) > 10):
            print("Please enter a number under or equal to 10 digits. ")
        else:
            numList2 = [str(int(number))]
            numList = numList + numList2
            numCount = numCount + 1
    elif(number == ""):
        quitCheck = 1
    
    else:
        print("Please enter a number with no spaces, letters or non-alphanumeric characters. Decimals not allowed.")
if(numCount != 0):
    print("You entered " + str(numList) + " and " + str(numCount) + " numbers. ")
    total = 0
    for i in numList:
        total = total + float(i)
    ans = float(total) / float(numCount)
    ans2 = round(ans, 2)
    ans3 = int(round(ans2, 0))
    print("Your answer is " + str(ans2) + " to 2 decimal places, " + str(ans) + " in full and " + str(ans3) + " as a whole number.")
else:
    print("Your answer is 0")
print("Goodbye!!")
print("")