print("")
print("Welcome to RN Calculator")
print("")
enterError = "Please enter a number instead."
import random
robot = random.randint(100,999)
checkrobot = raw_input("Enter the number " + str(robot) + ": ")
if(str(robot) == str(checkrobot)):
    num1 = raw_input("Enter first number: ")
    if(str.isdigit(str(num1)) or str.isdecimal(str(num1))):
        op = raw_input("Enter operator: ")
        if(op == "+" or op == "-" or op == "x" or op == "*" or op == "/"):
            num2 = raw_input("Enter second number: ")
            if(str.isdigit(str(num2)) or str.isdecimal(str(num2))):
                if(op == "+"):
                    ans = int(num1) + int(num2)
                elif(op == "-"):
                    ans = int(num1) - int(num2)
                elif(op == "x" or op == "*"):
                    ans = int(num1) * int(num2)
                elif(op == "/"):
                    ans = int(num1) / int(num2)
                else:
                    ans = "Sorry, there was a problem in the network. Please try again later."
                print("Your answer to " + str(num1) + " " + str(op) + " " + str(num2) + " is " + str(ans))
            else:
                print(enterError)
        else:
            print("Please enter an operator (+, -, x or *, /) instead.")
    else:
        print(enterError)
else:
    print("You robot!!")
print("")
raw_input("Press enter to exit. ")
data = 0
print("Exiting Calculator")
print("Sorry, having trouble connecting to RN")
print("")
time0 = 0.0
while(data < 10500):
    print("Downloading data...")
    percent = float(data) / 100
    if(percent > 100.00):
        percent = 100
    import random
    increase = random.randint(200,1000)
    time1 = random.randint(1,5)
    time2 = float(time1) / 10
    time0 = time0 + float(time2)
    import time
    time.sleep(time2)
    print(str(data) + " kbs (" + str(round((float(data) / 1000), 1)) + " mbs) dowloaded in " + str(time0) + " secs. " + str(percent) + " percent complete.")
    print("")
    data = data + increase
print("100 percent complete (10MB) at " + str(round((10 / (time0)), 2)) + " mbs/sec")
print("")