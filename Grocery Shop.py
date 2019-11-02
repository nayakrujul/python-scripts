print("")
print("RN Grocery Shop in Python 2.6.9")
import random
finishLoad = random.randint(10,15)
num1 = random.randint(1,5)
num2 = random.randint(1,5)
num3 = random.randint(1,5)
op1 = random.randint(1,3)
if(op1 == 1):
    op = " + "
    ans = num1 + num2 + num3
elif(op1 == 2):
    op = " - "
    ans = num1 - num2 - num3
elif(op1 == 3):
    op = " x "
    ans = num1 * num2 * num3
else:
    op = " THIS IS A NETWORK ERROR. PLEASE DO NOT CONTINUE. "
while(finishLoad >= 0):
    import time
    print("Loading.")
    finishLoad = finishLoad - 1
    time.sleep(1)
    print("Loading..")
    finishLoad = finishLoad - 1
    time.sleep(1)
    print("Loading...")
    finishLoad = finishLoad - 1
    time.sleep(1)
print("")
robot = raw_input("Please prove that you're not a robot. What is " + str(num1) + op + str(num2) + op + str(num3) + "? ")
if(str(robot) == str(ans)):
    items = 'crisps @ 1.00, peanuts @ 2.00, butter @ 1.25, cheese @ 2.00, milk @ 1.50, yoghurt @ 2.00, eggs @ 1.50, bread @ 1.50, coffee @ 1.00.'
    print("")
    receipt = ""
    money = 20
    ext = 0
    while(ext == 0):
        ask = raw_input("Would you like to buy or exit? You have " + str(money) + " left. ")
        if(str.lower(ask) == "buy"):
            print("You can buy " + str(items))
            item = raw_input("Which item would you like to buy? ")
            if(str.lower(item) == "crisps" and money >= 1):
                money = money - 1
                print("Crisps bought")
            elif(str.lower(item) == "peanuts" and money >= 2):
                money = money - 2
                print("Peanuts bought")
            elif(str.lower(item) == "butter" and float(money) >= 1.25):
                money = float(money) - 1.25
                print("Butter bought")
            elif(str.lower(item) == "cheese" and money >= 2):
                money = money - 2
                print("Cheese bought")
            elif(str.lower(item) == "milk" and float(money) >= 1.5):
                money = float(money) - 1.5
                print("Milk bought")
            elif(str.lower(item) == "yoghurt" and money >= 2):
                money = money - 2
                print("Yoghurt bought")
            elif(str.lower(item) == "eggs" and float(money) >= 1.5):
                money = float(money) - 1.5
                print("Eggs bought")
            elif(str.lower(item) == "bread" and float(money) >= 1.5):
                money = float(money) - 1.5
                print("Bread bought")
            elif(str.lower(item) == "Coffee" and money >= 1):
                money = money - 1
                print("Coffee bought")
            else:
                print("Please choose an option that you have enough money for.")
            receipt = receipt + item + "\n"
        elif(str.lower(ask) == "exit"):
            ext = 1
        else:
            print("We didn't get your option. Please try again.")
        print("")
    receiptAsk = raw_input("Thank you for shopping at RN. Would you like a receipt? ")
    if(str.lower(receiptAsk) == "yes"):
        print(str(receipt) + "\n" + "Total price " + str((20.0 - float(money))))
    else:
        print("We took that as a no.")
else:
    print(str(num1) + op + str(num2) + op + str(num3) + " = " + str(ans) + " not " + str(robot))
print("")
