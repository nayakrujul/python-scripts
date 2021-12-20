import sys
import time
import numpy as np


# Function to validate board size (user input)
def validate_userinput(userinput):
    if(str.isdigit(str(userinput))):
        boardsize = int(userinput)
        if(boardsize > 10 or boardsize <= 2):
            print("Invalid board size. Must be between 3 and 10. DECLINED!")
            print("")
            sys.exit()
    else:
        print("Invalid input. Must be a positive integer. DECLINED!")
        print("")
        sys.exit()


# Function to initialise the boardlist
def initialise_boardlist(boardsize):
    boardlist = []
    # Populate all values with 0
    for m in range(boardsize):
        boardlist.insert(m, [])
        for n in range(boardsize):
            boardlist[m].append(0)
    # print(boardlist)
    return boardlist


# Function to print empty board
def print_empty_board(boardsize):
    print("")
    print("Here is the empty board:")
    print("")
    dash = " ---"
    slash = "|   "
    dash2 = dash * boardsize
    slash2 = slash * (boardsize + 1)

    while(boardsize > 0):
        print(dash2)
        print(slash2)
        boardsize = boardsize - 1
    print(dash2)
    print("")

# Function to check winner
def check_winner(boardlist):
    check_row_winner(boardlist)

    check_column_winner(boardlist)

    check_left_diagonal_winner(boardlist)

    check_right_diagonal_winner(boardlist)

    print("")

    check_board(boardlist)
    print("No winners yet. Please carry on.")


# Function to check if winner in any of the rows
def check_row_winner(boardlist):    
    for a in range(int(userinput)):
        row = boardlist[a]
        if(len(set(row)) == 1 and row[0] != 0):
            print("Player " + str(row[0]) + " has won.")
            sys.exit()
    # print("No row winners")


# Function to check if winner in any of the columns
def check_column_winner(boardlist):
    transposedBoardlist = np.array(boardlist).T
    for a in range(int(userinput)):
        row = transposedBoardlist[a]
        if(len(set(row)) == 1 and row[0] != 0):
            print("Player " + str(row[0]) + " has won.")
            sys.exit()
    # print("No column winners")


# Function to check if winner in the top-left to bottom-right diagonal
def check_left_diagonal_winner(boardlist):
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


# Function to check if winner in the top-right to bottom-left diagonal
def check_right_diagonal_winner(boardlist):
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


# Function to check if any coordinates available for further moves
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


# Function to print the current board
def print_board(boardlist):
    for a in range(len(boardlist)):
        for b in range(len(boardlist[a])):
            print(boardlist[a][b]),
        print("\n")



# -------------------------------------------------------------------
# Main Code
print("")
print("Welcome to RN Naughts and Crosses")
print("")
userinput = raw_input("How many squares do you want for each side? ")

validate_userinput(userinput)

boardsize = int(userinput)

boardlist = []
boardlist = initialise_boardlist(boardsize)

print_empty_board(boardsize)

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
        # print("Values accepted past first stage (Wrong number of values).")

        if(str.isdigit(rowColumnSplit[0]) and str.isdigit(rowColumnSplit[1])):
            # print("Values accepted past second stage (Not numeric values).")
            rowValue = int(rowColumnSplit[0])
            columnValue = int(rowColumnSplit[1])

            if(rowValue <= boardsize and rowValue >= 1 and columnValue <= boardsize and columnValue >= 1):
                # print("Values accepted past third stage (Coordinates not on board).")

                if(boardlist[(rowValue - 1)][(columnValue - 1)] == 0):
                    # print("Values accepted past fourth stage (Coordinates not available).")
                    print("")
                    # print("Inputting values...")
                    boardlist[(rowValue - 1)][(columnValue - 1)] = player
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
                    print("Values declined (Coordinates not available)")

            else:
                print("Values declined (Coordinates not on board)")

        else:
            print("Values declined (Not numeric values)")

    else:
        print("Values declined (Wrong number of values)")

print("")