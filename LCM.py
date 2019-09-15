print("")
print("Welcome to RN Lowest Common Multiple Calculator")
import random
num = random.randint(0,9999)
robot = raw_input("Prove you're not a robot. Type the number " + str(num) + ": ")
if(str.isdigit(str(robot))):
    if(int(robot) == int(num)):
        multiply = 1
        num1 = raw_input("Please enter first number: ")
        num2 = raw_input("Please enter second number: ")
        if(str.isdigit(str(num1)) and str.isdigit(str(num2))):
            if(int(num1) > 0 and int(num2) > 0):
                if(num1 > num2):
                    while((int(num1) * multiply) % int(num2) != 0):
                        multiply = multiply + 1
                    print("LCM is " + str(int(num1) * multiply))
                elif(num2 > num1):
                    while((int(num2) * multiply) % int(num1) != 0):
                        multiply = multiply + 1
                    print("LCM is " + str(int(num2) * multiply))
                else:
                    print("LCM is " + str(num1))
            else:
                print("Cannot do LCM of 0")
        else:
            print("Please enter numbers instead")
    else:
        print("ROBOT!!")
else:
    print("ROBOT!!")
print("")
raw_input("Press enter to exit. (10 mbs at 1 mb/sec). ")
seconds = 10
while(seconds >= 0):
    mbs = (10.0 - seconds)
    print(str(round(seconds, 1)) + " secs left to exit (" + str(mbs) + " mbs downloaded).")
    seconds = float(seconds) - 0.1    
    import time
    time.sleep(0.1)
print("")