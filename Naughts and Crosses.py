import sys
import time
import numpy as np

print("")
print("Welcome to RN Naughts and Crosses")
print("")
userinput = raw_input("How many squares do you want for each side? ")

boardlist = []

def initialise_boardlist(userinput):
    # boardlist = [[0,0,0],[0,0,0],[0,0,0]]
    # boardlist1 = [0] * int(userinput)
    # boardlist = boardlist1 * int(userinput)
    for m in range(int(userinput)):
        boardlist.insert(m, [])
        for n in range(int(userinput)):
            boardlist[m].append(0)
    # print(boardlist)
    return boardlist

boardlist = initialise_boardlist(userinput)

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
print("Here is the empty board:")
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
    # print("")
    check_column_winner(boardlist)
    # print("")
    check_left_diagonal_winner(boardlist)
    # print("")
    check_right_diagonal_winner(boardlist)
    print("")
    check_board(boardlist)
    print("No winners yet. Please carry on.")


def check_row_winner(boardlist):    
    # print("Checking board for each row...")   
    # check rows
    for a in range(int(userinput)):
        row = boardlist[a]
        if(len(set(row)) == 1 and row[0] != 0):
            print("Player " + str(row[1]) + " has won.")
            sys.exit()
    # print("No row winners")


def check_column_winner(boardlist):
    # check columns
    # print("Checking board for each column...")
    transposedBoardlist = np.array(boardlist).T
    for a in range(int(userinput)):
        row = transposedBoardlist[a]
        if(len(set(row)) == 1 and row[0] != 0):
            print("Player " + str(row[1]) + " has won.")
            sys.exit()
    # print("No column winners")


def check_left_diagonal_winner(boardlist):
    # check left diagonal
    # print("Checking board for the left diagonal...")
    for x in range(int(userinput)):
        if(x == 0):
            firstValue = boardlist[x][x]
            if(firstValue == 0):
                # print("No left diagonal winners")
                return 0
            else:
                continue
        nextValue = boardlist[x][x]
        if(nextValue != firstValue):
            # print("No left diagonal winners")
            return 0
    print("Player " + str(firstValue) + " has won")
    sys.exit()
    
def check_right_diagonal_winner(boardlist):
    # check right diagonal
    # print("Checking board for the right diagonal...")
    for x in range(int(userinput)):
        if(x == 0):
            firstValue = boardlist[x][(int(userinput) - x - 1)]
            if(firstValue == 0):
                # print("No right diagonal winners")
                return 0
            else:
                continue
        nextValue = boardlist[x][(int(userinput) - x - 1)]
        if(nextValue != firstValue):
            # print("No right diagonal winners")
            return 0
    print("Player " + str(firstValue) + " has won")
    sys.exit()


def check_board(boardlist):
    validFlag = 0
    for a in range(len(boardlist)):
        for b in range(len(boardlist[a])):
            if(boardlist[a][b] == 0):
                validFlag = 1
                break
    if(validFlag == 0):
        print("No more possible moves. Draw")
        sys.exit()


def print_board(boardlist):
    for a in range(len(boardlist)):
        for b in range(len(boardlist[a])):
            print(boardlist[a][b]),
        print("\n")

def initialise_boardlist(userinput, boardlist):
    boardlist = [[0,0,0],[0,0,0],[0,0,0]]

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

player = 1

while(0 == 0):

    print("")

    print("Player " + str(player))

    print("")

    print("The top-left corner of the board is 1, 1")
    rowColumn = raw_input("Please enter your coordinates in the form row, column (no brackets needed): ")
    rowColumnSplit = rowColumn.split(", ")

    print("")
    

    if(len(rowColumnSplit) == 2):
        # print("Values accepted past first stage.")

        if(str.isdigit(rowColumnSplit[0]) and str.isdigit(rowColumnSplit[1])):
            # print("Values accepted past second stage.")
            split1 = rowColumnSplit[0]
            split2 = rowColumnSplit[1]

            if(int(split1) <= 3 and int(split1) >= 1 and int(split2) <= 3 and int(split2) >= 1):
                # print("Values accepted past third stage.")

                if(boardlist[(int(split1) - 1)][(int(split2) - 1)] == 0):
                    # print("Values accepted past fourth stage.")
                    print("")
                    # print("Inputting values...")
                    boardlist[(int(split1) - 1)][(int(split2) - 1)] = player
                    # print("Values inputted")
                    print("")

                    if(player == 1):
                        player = 2
                    elif(player == 2):
                        player = 1
                    else:
                        errorExit = raw_input("An error has occured. We are trying to fix it as soon as we can. To exit, press enter.")
                        sys.exit()
                    print_board(boardlist)
                    check_winner(boardlist)
                    print("Continuing...")
                    continue

                else:
                    print("Values declined (fourth stage)")

            else:
                print("Values declined (third stage)")

        else:
            print("Values declined (second stage)")

    else:
        print("Values declined (first stage)")

print("")