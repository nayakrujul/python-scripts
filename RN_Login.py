print("")
print("Welcome to RN.")
error = " cannot be blank."
filename = "RN_Login.txt"
check1 = 1
check2 = 2
RNaccount = raw_input("Do you have an RN account already? ")
if(RNaccount == "y" or RNaccount == "Y" or RNaccount == "yes" or RNaccount == "Yes"):
    userName = raw_input("Please enter username or email address. ")
    password = raw_input("Please enter your password. ")
    print("Welcome back " + userName)
    with open (filename, "a") as f:
        import datetime
        DateTimeNow = datetime.datetime.now()
        f.write("Username: " + userName + ". Password: " + password + ". Loggin in at " + str(DateTimeNow) + "\n")
        check1 = 0
        check2 = 0
elif(RNaccount == "n" or RNaccount == "N" or RNaccount == "no" or RNaccount == "No"):
    email = raw_input("Please enter email ID. ")
    phone = raw_input("Please enter your phone number. ")
    if(str.isdigit(str(phone))):
        username = raw_input("Please enter a username. ")
        password = raw_input("Please enter a password. ")
        if(username != "" and password != "" and len(username) >= 8 and len(password) >= 6):
            print("Stored as " + username + " with a email of " + email + " and a phone number of " + str(phone) + ". Password: ********.")
            print("-----")
            print("Personal Info")
            name = raw_input("What's your name? ")
            if(name != ""):
                address1 = raw_input("Hello " + name + ". What's your address (line 1)? ")
                if(address1 != ""):
                    address2 = raw_input("What's your address (line 2; optional)? ")
                    town = raw_input("Enter town/city. ")
                    if(town != ""):
                        county = raw_input("Enter county/state. ")
                        if(county != ""):
                            country = raw_input("Enter country. ")
                            if(country != ""):
                                postCode = raw_input("Enter post code. ")
                                if(postCode != ""):
                                    with open (filename, "a") as f:
                                        import datetime
                                        datetimeNow = datetime.datetime.now
                                        f.write(address1 + address2 + ", " + town + ", " + county + ", " + country + ". " + postCode + ". \n")
                                        check1 = 0
                                        check2 = 0
                                else:
                                    print("Post code" + error)
                            else:
                                print("Country" + error)
                        else:
                            print("County" + error)
                    else:
                        print("Town" + error)
                else:
                    print("Address line 1" + error)
            else:
                print("Name" + error)
        else:
            print("Username must be at least 8 characters and password must be at least 6 characters.")
    else:
        print("Phone number must be number.")
else:
    print("Options are y, Y, yes, Yes, n, N, no, No.")
print("")
if(check1 == 0 and check2 == 0):
    remove = raw_input("Would you like to remove the log? Press enter to remove. Type anything else to save. ")
    if(remove == ""):
        import random
        num01 = random.randint(1,100)
        num1 = float(num01) / 10.0
        num02 = random.randint(1,100)
        num2 = float(num02) / 10.0
        num = random.randint(1,9999999999)
        strnum = str(num).zfill(10)
        robot = raw_input("What's " + str(num1) + " + " + str(num2) + "? ")
        if(str((num1 + num2)) == robot):
            number = raw_input("Enter the number " + strnum + ": ")
            if(str(number) == strnum):
                sureRemove = raw_input("Are you sure you want to remove the log. Type anything to remove and press enter to save. ")
                if(sureRemove != ""):
                    with open(filename, "a") as f:
                        f.write("Deleting from disk. \n")
                        f.write("Deleted from disk.")
                    import time
                    time.sleep(0.100)
                    import os
                    os.remove(filename)
                    print("Log removed.")
                else:
                    print("Log saved.")
            else:
                print(str(number) + " is not " + strnum)
        else:
            print(str(num1) + " + " + str(num2) + " = " + str((num1 + num2)) + " not " + str(robot))
    else:
        print("Log saved.")
else:
    pass
print("")