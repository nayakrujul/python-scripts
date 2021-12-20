print("")
print("Welcome to RN Feedback.")
import random
num = random.randint(100000,999999)
robot = input("Enter " + str(num) + ": ")
if(str(num) == str(robot)):
    user = input("Please enter username: ")
    import math
    if(str.isdigit(str(user)) and str(user) != ""):
        print("Please use at least 1 non-numeric character")
    else:
        exitCheck = 0
        count = 1
        filename = "Feedback.txt"
        while(exitCheck == 0):
            feedback = input("Please enter feedback. Enter a blank to exit: ")
            if(feedback != ""):
                stars = input("How many stars would you give us? ")
                if(str.isdigit(str(stars))):
                    if(int(stars) <= 5 and int(stars) >= 1):
                        with open (filename, "a") as f:
                            import datetime
                            DateTimeNow = datetime.datetime.now()
                            f.write ("Date and Time: " + str(DateTimeNow) + "; Feedback " + str(count) + ": " + str(feedback) + "; User: " + str(user) + "; Stars: " + str(stars) + "." + "\n")
                        count = count + 1
                        print("Thank you for your feedback.")
                    else:
                        print("Only 1 to 5 allowed")
                else:
                    print("Please enter a number instead")
            else:
                exitCheck = 1
                with open (filename, "a") as f:
                    import datetime
                    DateTimeNow = datetime.datetime.now()
                    f.write ("Closing at " + str(DateTimeNow) + "... " + "\n")
        if(count != 1):
            clear = input("Press enter to clear. Type anything else to save. ")
            if(clear == ""):
                with open (filename, "a") as f:
                    f.write ("Deleting... " + "\n")
                    f.write ("Deleted")
                import time
                time.sleep(0.1)
                import os
                os.remove(filename)
                print("File removed.")
            else:
                print("File saved.")
                with open (filename, "a") as f:
                    f.write ("Re-opening... " + "\n")
else:
    print("ROBOT!")
print("")