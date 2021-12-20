# By RN

# RRRRRRRRRRRRR  NNNN        NN
# RR         RR  NN NN       NN
# RR         RR  NN  NN      NN
# RR         RR  NN   NN     NN
# RRRRRRRRRRRRR  NN    NN    NN
# RR RRR         NN     NN   NN
# RR   RRR       NN      NN  NN
# RR     RRR     NN       NN NN
# RR       RRR   NN        NNNN

# Import libraries
from datetime import date as d
from random import randint as r
from os import remove as rm

print("")

# Welcome message
print("Welcome to the RN Random Password Generator.")
print("")

# Get personal info and store
print("We just need to ask you a few questions.")
print("")

# Name
nameExit = 0
while nameExit == 0:
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    print("")
    if str(firstName) != "" and str(lastName) != 0:
        nameExit = 1
    else:
        print("Sorry, we don't think this fullfills the criteria.")

# Age
ageExit = 0
while ageExit == 0:
    age = input("Please enter your age: ")
    print("")
    if str.isdigit(str(age)):
        ageExit = 1
    else:
        print("Sorry, we don't think this fullfills the criteria.")

# DoB
DoBExit = 0
while DoBExit == 0:
    DoBMonth = input("Please enter the month you were born in as a number (e.g. May = 5): ")
    DoBDay = input("Please enter the day you were born: ")
    print("")
    if str.isdigit(str(DoBMonth)) and str.isdigit(str(DoBDay)):
        if int(DoBMonth) >= 1 and int(DoBMonth) <= 12 and int(DoBDay) >= 1 and int(DoBDay) <= 31:
            DoBExit = 1
        else:
            print("Sorry, we don't think this fullfills the criteria.")
    else:
        print("Sorry, we don't think this fullfills the criteria.")

# Now store
fileName = "File_for_" + str(firstName) + "_" + str(lastName) + "_on_" + str(d.today().strftime("%b-%d-%Y")) + ".txt"
f = open(fileName, "a")

f.write("Made by RN \n \n")
f.write("First Name: " + firstName + "\n" + "Last Name: " + lastName + "\n" + "Age: " + age + "\n" + "DoB (MM/DD): " + str(DoBMonth).zfill(2) + "/" + str(DoBDay).zfill(2) + "\n \n")

# Keep the user updated
print("Your password is being generated and will be stored in the text file that is in the same folder as this.")
print("")

# Generate password 
password = ""

symbolNum = r(1,10)
if symbolNum == 1:
    symbol = "!"
elif symbolNum == 2:
    symbol = "@"
elif symbolNum == 3:
    symbol = "£"
elif symbolNum == 4:
    symbol = "$"
elif symbolNum == 5:
    symbol = "%"
elif symbolNum == 6:
    symbol = "^"
elif symbolNum == 7:
    symbol = "&"
elif symbolNum == 8:
    symbol = "*"
elif symbolNum == 9:
    symbol = "#"
elif symbolNum == 10:
    symbol = "?"

symbolNum2 = r(1,10)
if symbolNum2 == 1:
    symbol2 = "!"
elif symbolNum2 == 2:
    symbol2 = "@"
elif symbolNum2 == 3:
    symbol2 = "£"
elif symbolNum2 == 4:
    symbol2 = "$"
elif symbolNum2 == 5:
    symbol2 = "%"
elif symbolNum2 == 6:
    symbol2 = "^"
elif symbolNum2 == 7:
    symbol2 = "&"
elif symbolNum2 == 8:
    symbol2 = "*"
elif symbolNum2 == 9:
    symbol2 = "#"
elif symbolNum2 == 10:
    symbol2 = "?"

password += str(firstName)[0]
password += str(lastName)[0]
password += str(symbol)
password += str(DoBDay).zfill(2)
password += str(DoBMonth).zfill(2)
password += str(symbol2)

f.write("Suggested password: " + password + "\n" + "Strength: Very Strong" + "\n \n")
f.close()
print("Password generated.")
print("")

# Delete file
print("Powered by RN Delete File.")
print("")

deleteExit = 0
while deleteExit == 0:
    delete = input("Would you like RN Delete File to delete the file? (y/n) ")
    print("")
    if str.upper(str(delete)) == "Y":
        rm(fileName)
        print("File removed from system.")
        deleteExit = 1
    elif str.upper(str(delete)) == "N":
        print("File kept in system.")
        deleteExit = 1
    else:
        print("Sorry, we don't think this fullfills the criteria.")


print("")
print("Made by RN.")
print("")