print("")
print("C://users/itmn/Documents/RN/Timer.py running")
print("")
import time
hrs = raw_input("Please enter hours: ")
mins = raw_input("Please enter minutes: ")
secs = raw_input("Please enter seconds: ")
if(str.isdigit(str(hrs)) and str.isdigit(str(mins)) and str.isdigit(str(secs))):
    if(int(mins) < 60 and int(secs) < 60):
        import random
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        password = raw_input("Prove you're not a robot. What's " + str(num1) + " + " + str(num2) + "? ")
        if(str.isdigit(str(password))):
            if(int(password) == num1 + num2): 
                print("")
                intsecs = int(secs)
                intmins = int(mins)
                inthrs = int(hrs)
                print("Timer for " + str(int(hrs)).zfill(2) + ":" + str(int(mins)).zfill(2) + ":" + str(int(secs)).zfill(2) + " starting in 3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                exitCount = 0
                while(exitCount == 0):
                    print(str(inthrs).zfill(2) + ":" + str(intmins).zfill(2) + ":" + str(intsecs).zfill(2))
                    import time
                    time.sleep(1)
                    intsecs = intsecs - 1
                    if(intsecs < 0):
                        intsecs = intsecs + 60
                        intmins = intmins - 1
                    if(intmins < 0):
                        intmins = intmins + 60
                        inthrs = inthrs - 1
                    if(inthrs < 0):
                        print("Timer up!!")
                        quitcount = 0
                        while(quitcount == 0):
                            timerUp = raw_input("Timer up. Press enter to exit. ")
                            if(timerUp == "" or timerUp == "Exit"):
                                quitcount = 1
                            else:
                                print("Press enter to exit, you robot!")
                        exitCount = 1
            else:
                print("")
                print("You're a robot. " + str(num1) + " + " + str(num2) + " = " + str(int(num1) + int(num2)) + ", not " + str(password))
        else:
            print("")
            print("You're a robot. " + str(num1) + " + " + str(num2) + " = " + str(int(num1) + int(num2)) + ", not " + str(password))
    else:
        print("")
        print("Maximum for minutes is 59; maximum for seconds is 59.")
else:
    print("")
    print("Please use numbers instead.")
print("")