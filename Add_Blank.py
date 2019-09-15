print("")
import random
num1 = random.randint(1,5)
num2 = random.randint(1,5)
op = random.randint(1,2)
if(op == 1):
    op1 = " + "
elif(op == 2):
    op1 = " x "
else:
    op1 = " _ Network connection issue. Please try again later. _ "
lines = input("How many blank lines would you like? ")
robot = input("Prove you're not a robot. What's " + str(num1) + op1 + str(num2) + "? ")
if(str.isdigit(str(lines)) and int(lines) > 0 and str.isdigit(str(robot))):
    if(op == 1):
        if(num1 + num2 == int(robot)):
            intlines = int(lines)
            print(str(lines) + " blank lines added.")
            while(intlines != 0):
                print("")
                intlines = intlines - 1
        else:
            print("Robot! " + str(num1) + op1 + str(num2) + " = " + str(int(num1) + int(num2)))
            name = input("It's the FBI. What's your name? ")
            address = input("What's your address? ")
            filename = "Data_log.txt"
            with open (filename, "w") as f:
                f.write ("Name: " + name + "; Address: " + address)
            print("Logged as " + name + " with an address of " + address)
    elif(op == 2):
        if(num1 * num2 == int(robot)):
            intlines = int(lines)
            print(str(lines) + " blank lines added.")
            while(intlines != 0):
                print("")
                intlines = intlines - 1           
        else:
            print("Robot! " + str(num1) + op1 + str(num2) + " = " + str(int(num1) * int(num2)))
            name = input("It's the FBI. What's your name? ")
            address = input("What's your address? ")
            filename = "Data_log.txt"
            with open (filename, "w") as f:
                f.write ("Name: " + name + "; Address: " + address)
            print("Logged as " + name + " with an address of " + address)
            clear = input("Press enter to clear: ")
            count = 0.1
            if(clear == ""):
                print("Removing Data Log...")
                while(count < 10):
                    import random
                    time = random.randint(1,10)
                    time1 = float(time) / 10
                    import time
                    time.sleep(time1)
                    print(str(int(float(count) * 10)) + " percent complete.")
                    import random
                    addcount = random.randint(5,20)
                    ac = float(addcount) / 10
                    count = count + ac
                print("100 percent complete.")
                import os
                os.remove("Data_log.txt")
                print("Data Log removed with RN Add_Blank clearing (Based on Text_Send)")
            else:
                print("Data log saved")
                print("")
    else:
        print("Network connection issue. Please try again later. ")
elif(lines < 1):
    print("Minimum number of lines: 1")
else:
    print("Please enter a number")
print("")