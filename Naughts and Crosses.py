import sys
import time
import numpy as np

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
def check_winner(boardlist):
    check_row_winner(boardlist)
    print("")
    check_column_winner(boardlist)
    print("")
    check_left_diagonal_winner(boardlist)
    print("")
    check_right_diagonal_winner(boardlist)
    print("")
    print("No winners. Please carry on.")

def check_row_winner(boardlist):    
    print("Checking board for each row...")   
    # check rows
    for a in range(int(userinput)):
        row = boardlist[a]
        if(len(set(row)) == 1 and row[0] != 0):
            print("Player " + str(row[1]) + " has won.")
            sys.exit()
    print("No row winners")

def check_column_winner(boardlist):
    # check columns
    print("Checking board for each column...")
    transposedBoardlist = np.array(boardlist).T
    for a in range(int(userinput)):
        row = transposedBoardlist[a]
        if(len(set(row)) == 1 and row[0] != 0):
            print("Player " + str(row[1]) + " has won.")
            sys.exit()
    print("No column winners")

def check_left_diagonal_winner(boardlist):
    # check left diagonal
    print("Checking board for the left diagonal...")
    for x in range(int(userinput)):
        if(x == 0):
            firstValue = boardlist[x][x]
            if(firstValue == 0):
                print("No left diagonal winners")
                return 0
            else:
                continue
        nextValue = boardlist[x][x]
        if(nextValue != firstValue):
            print("No left diagonal winners")
            return 0
    print("Player " + str(firstValue) + " has won")
    sys.exit()
    
def check_right_diagonal_winner(boardlist):
    # check right diagonal
    print("Checking board for the right diagonal...")
    for x in range(int(userinput)):
        if(x == 0):
            firstValue = boardlist[x][(int(userinput) - x - 1)]
            if(firstValue == 0):
                print("No right diagonal winners")
                return 0
            else:
                continue
        nextValue = boardlist[x][(int(userinput) - x - 1)]
        if(nextValue != firstValue):
            print("No right diagonal winners")
            return 0
    print("Player " + str(firstValue) + " has won")
    sys.exit()

# boardlist = []
# boardlistline = []
# for x in range(0, int(userinput)):
#   for y in range(0, int(userinput)):
#     boardlistline.append(0)
#   boardlist.append(boardlistline)
#   boardlistline = []
# print("Printing current board...")
# time.sleep(1)
# for z in range(0, int(userinput)):
#   print(boardlist[z])
# print("")

boardlist = [[0,1,1],[0,1,0],[1,2,1]]
check_winner(boardlist)
print("")