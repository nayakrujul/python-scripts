import sys
print("")
print("Welcome to RN Naughts and Crosses")
print("")
userinput = raw_input("How many squares do you want for each side? ")
if(str.isdigit(str(userinput))):
    repeat = int(userinput)
    if(repeat > 10 or repeat <= 0):
        print("Invalid board size. DECLINED!")
        print("")
        sys.exit()
else:
    print("Invalid input. DECLINED!")
    print("")
    sys.exit()
print("")
print("Here is the board:")
print("")
# A1 = " "
# A2 = " "
# A3 = " "
# B1 = " "
# B2 = " "
# B3 = " "
# C1 = " "
# C2 = " "
# C3 = " "
dash = " ---"
slash = "|   "
dash2 = dash * repeat
slash2 = slash * (repeat + 1)
while(repeat > 0):
    print(dash2)
    print(slash2)
    repeat = repeat - 1
print(dash2)
# value = 0
# while(value == 0):
#     row = raw_input("Enter row: ")
#     column = raw_input("Enter column: ")
#     if((str.upper(row) == "A" or str.upper(row) == "B" or str.upper(row) == "C") and (str(column) == "1" or str(column) == "2" or str(column) == "3")):
#         print("Values accepted.")
#     else:
#         print("Values declined.")
print("")