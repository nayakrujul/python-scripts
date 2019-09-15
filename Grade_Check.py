print("")
print("Welcome to RN Grade Check")
print("F: > 20; E: 20 - 34.99; D: 35 - 49.99; C: 50 - 64.99; B: 65 - 79.99; A: 80 - 89.99; A+: 90 or above.")
exitCount = 0
numCount = 0
list2 = []
while(exitCount == 0):
    percent = raw_input("Enter percentage. Press enter to exit. ")
    if(str.isdigit(str(percent))):
        list1 = [str(percent)]
        list2 = list1 + list2
        numCount = numCount + 1
    elif(str(percent) == ""):
        exitCount = 1
    else:
        print("Please enter a number.")
if(numCount > 0):
    print("")
    total = 0
    for i in list2:
        total = total + int(i)
    ans = float(total) / float(numCount)
    fl_ans = float(ans)
    if(fl_ans < 20):
        print("Your grade is F. You got an average of " + str(round(fl_ans, 2)) + " percent. Work a lot harder.")
    elif(fl_ans >= 20 and fl_ans < 35):
        print("Your grade is E. You got an average of " + str(round(fl_ans, 2)) + " percent. Work harder.")
    elif(fl_ans >= 35 and fl_ans < 50):
        print("Your grade is D. You got an average of " + str(round(fl_ans, 2)) + " percent. Nearly satisfactory.")
    elif(fl_ans >= 50 and fl_ans < 65):
        print("Your grade is C. You got an average of " + str(round(fl_ans, 2)) + " percent. Satisfactory.")
    elif(fl_ans >= 65 and fl_ans < 80):
        print("Your grade is B. You got an average of " + str(round(fl_ans, 2)) + " percent. Good.")
    elif(fl_ans >= 80 and fl_ans < 90):
        print("Your grade is A. You got an average of " + str(round(fl_ans, 2)) + " percent. Great!")
    elif(fl_ans >= 90):
        print("Your grade is A+. You got an average of " + str(round(fl_ans, 2)) + " percent. Super! Well done!")
    else:
        print("Network connection error.")
else:
    print("Please enter at least 1 grade")
print("")
raw_input("Press enter to continue. ")
data = 0
time0 = 0.0
while(data < 10700):
    print("Downloading data...")
    import random
    increase = random.randint(500,1000)
    time1 = random.randint(1,5)
    time2 = float(time1) / 10
    import time
    time.sleep(time2)
    time0 = time0 + time2
    print(str(data) + " kbs (" + str(round((float(data) / 1000), 1)) + " mbs) dowloaded in " + str(round(time0, 1)) + " seconds. Estimated time: " + str(round((5.0 - float(time0)), 1)) + " seconds left.")
    print("")
    data = data + increase
print("100 percent complete (10MB)")
print("")