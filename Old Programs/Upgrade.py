print("")
print("Upgrade to the newest version of RN.")
print("Current rate - 4 mbs/second")
print("")
choose = input("Choose your data in mbs (min. 15, max. 150). ")
if(str.isdigit(str(choose))):
    if(int(choose) >= 15 and int(choose) <= 150):
        time3 = 0
        data = 0
        print("Estimated time: " + str(round((int(choose) / 4), 2)) + " seconds.")
        print("")
        while(data < ((int(choose) * 1000) + 500)):
            print("Downloading data...")
            import random
            increase = random.randint(500,1000)
            time1 = random.randint(1,5)
            time2 = time1 / 10
            import time
            time.sleep(time2)
            time3 = float(time3) + time2
            print(str(data) + " kbs (" + str(round((int(data) / 1000), 1)) + " mbs) dowloaded in " + str(round(time3, 1)) + " seconds.")
            print("")
            data = data + increase
        print("100 percent complete (" + str(choose) + " mbs; "  + str(round(time3, 1)) + " seconds). Estimated time: " + str(round((int(choose) / 4), 2)) + " seconds.")
    else:
        print("Minimum: 5; Maximum: 100.")
else:
    print("Please use numbers")
print("")