from time import sleep as s
from os import system as sys
from threading import Thread as t
from math import floor as f

board = []


def printBoard():
	print(" 1  2  3  4  5  6  7")
	print("----------------------")
	print("|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|" +
	      board[0][3] + "|" + board[0][4] + "|" + board[0][5] + "|" +
	      board[0][6] + "|")
	print("|--|--|--|--|--|--|--|")
	print("|" + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" +
	      board[1][3] + "|" + board[1][4] + "|" + board[1][5] + "|" +
	      board[1][6] + "|")
	print("|--|--|--|--|--|--|--|")
	print("|" + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|" +
	      board[2][3] + "|" + board[2][4] + "|" + board[2][5] + "|" +
	      board[2][6] + "|")
	print("|--|--|--|--|--|--|--|")
	print("|" + board[3][0] + "|" + board[3][1] + "|" + board[3][2] + "|" +
	      board[3][3] + "|" + board[3][4] + "|" + board[3][5] + "|" +
	      board[3][6] + "|")
	print("|--|--|--|--|--|--|--|")
	print("|" + board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "|" +
	      board[4][3] + "|" + board[4][4] + "|" + board[4][5] + "|" +
	      board[4][6] + "|")
	print("|--|--|--|--|--|--|--|")
	print("|" + board[5][0] + "|" + board[5][1] + "|" + board[5][2] + "|" +
	      board[5][3] + "|" + board[5][4] + "|" + board[5][5] + "|" +
	      board[5][6] + "|")
	print("----------------------")


def initBoard():
	for i in range(6):
		board.append([])
		for j in range(7):
			board[i].append("  ")


# Version 1 (unused) - goes through every single possibility of a win (over 160 lines of code)
def checkWin():

	win = ""

	# Vertical (21)
	if board[0][0] == board[1][0] == board[2][0] == board[3][0] != "  ":
		win = board[0][0]
	if board[1][0] == board[2][0] == board[3][0] == board[4][0] != "  ":
		win = board[1][0]
	if board[2][0] == board[3][0] == board[4][0] == board[5][0] != "  ":
		win = board[2][0]
	if board[0][1] == board[1][1] == board[2][1] == board[3][1] != "  ":
		win = board[0][1]
	if board[1][1] == board[2][1] == board[3][1] == board[4][1] != "  ":
		win = board[1][1]
	if board[2][1] == board[3][1] == board[4][1] == board[5][1] != "  ":
		win = board[2][1]
	if board[0][2] == board[1][2] == board[2][2] == board[3][2] != "  ":
		win = board[0][2]
	if board[1][2] == board[2][2] == board[3][2] == board[4][2] != "  ":
		win = board[1][2]
	if board[2][2] == board[3][2] == board[4][2] == board[5][2] != "  ":
		win = board[2][2]
	if board[0][3] == board[1][3] == board[2][3] == board[3][3] != "  ":
		win = board[0][3]
	if board[1][3] == board[2][3] == board[3][3] == board[4][3] != "  ":
		win = board[1][3]
	if board[2][3] == board[3][3] == board[4][3] == board[5][3] != "  ":
		win = board[2][3]
	if board[0][4] == board[1][4] == board[2][4] == board[3][4] != "  ":
		win = board[0][4]
	if board[1][4] == board[2][4] == board[3][4] == board[4][4] != "  ":
		win = board[1][4]
	if board[2][4] == board[3][4] == board[4][4] == board[5][4] != "  ":
		win = board[2][4]
	if board[0][5] == board[1][5] == board[2][5] == board[3][5] != "  ":
		win = board[0][5]
	if board[1][5] == board[2][5] == board[3][5] == board[4][5] != "  ":
		win = board[1][5]
	if board[2][5] == board[3][5] == board[4][5] == board[5][5] != "  ":
		win = board[2][5]
	if board[0][6] == board[1][6] == board[2][6] == board[3][6] != "  ":
		win = board[0][6]
	if board[1][6] == board[2][6] == board[3][6] == board[4][6] != "  ":
		win = board[1][6]
	if board[2][6] == board[3][6] == board[4][6] == board[5][6] != "  ":
		win = board[2][6]

	# Horizontal (24)

	if board[0][0] == board[0][1] == board[0][2] == board[0][3] != "  ":
		win = board[0][0]
	if board[1][0] == board[1][1] == board[1][2] == board[1][3] != "  ":
		win = board[1][0]
	if board[2][0] == board[2][1] == board[2][2] == board[2][3] != "  ":
		win = board[2][0]
	if board[3][0] == board[3][1] == board[3][2] == board[3][3] != "  ":
		win = board[3][0]
	if board[4][0] == board[4][1] == board[4][2] == board[4][3] != "  ":
		win = board[4][0]
	if board[5][0] == board[5][1] == board[5][2] == board[5][3] != "  ":
		win = board[5][0]
	if board[0][1] == board[0][2] == board[0][3] == board[0][4] != "  ":
		win = board[0][1]
	if board[1][1] == board[1][2] == board[1][3] == board[1][4] != "  ":
		win = board[1][1]
	if board[2][1] == board[2][2] == board[2][3] == board[2][4] != "  ":
		win = board[2][1]
	if board[3][1] == board[3][2] == board[3][3] == board[3][4] != "  ":
		win = board[3][1]
	if board[4][1] == board[4][2] == board[4][3] == board[4][4] != "  ":
		win = board[4][1]
	if board[5][1] == board[5][2] == board[5][3] == board[5][4] != "  ":
		win = board[5][1]
	if board[0][2] == board[0][3] == board[0][4] == board[0][5] != "  ":
		win = board[0][2]
	if board[1][2] == board[1][3] == board[1][4] == board[1][5] != "  ":
		win = board[1][2]
	if board[2][2] == board[2][3] == board[2][4] == board[2][5] != "  ":
		win = board[2][2]
	if board[3][2] == board[3][3] == board[3][4] == board[3][5] != "  ":
		win = board[3][2]
	if board[4][2] == board[4][3] == board[4][4] == board[4][5] != "  ":
		win = board[4][2]
	if board[5][2] == board[5][3] == board[5][4] == board[5][5] != "  ":
		win = board[5][2]
	if board[0][3] == board[0][4] == board[0][5] == board[0][6] != "  ":
		win = board[0][3]
	if board[1][3] == board[1][4] == board[1][5] == board[1][6] != "  ":
		win = board[1][3]
	if board[2][3] == board[2][4] == board[2][5] == board[2][6] != "  ":
		win = board[2][3]
	if board[3][3] == board[3][4] == board[3][5] == board[3][6] != "  ":
		win = board[3][3]
	if board[4][3] == board[4][4] == board[4][5] == board[4][6] != "  ":
		win = board[4][3]
	if board[5][3] == board[5][4] == board[5][5] == board[5][6] != "  ":
		win = board[5][3]

	# Diagonal 1 (12)

	if board[0][0] == board[1][1] == board[2][2] == board[3][3] != "  ":
		win = board[0][0]
	if board[0][1] == board[1][2] == board[2][3] == board[3][4] != "  ":
		win = board[0][1]
	if board[0][2] == board[1][3] == board[2][4] == board[3][5] != "  ":
		win = board[0][2]
	if board[0][3] == board[1][4] == board[2][5] == board[3][6] != "  ":
		win = board[0][3]
	if board[1][0] == board[2][1] == board[3][2] == board[4][3] != "  ":
		win = board[1][0]
	if board[1][1] == board[2][2] == board[3][3] == board[4][4] != "  ":
		win = board[1][1]
	if board[1][2] == board[2][3] == board[3][4] == board[4][5] != "  ":
		win = board[1][2]
	if board[1][3] == board[2][4] == board[3][5] == board[4][6] != "  ":
		win = board[1][3]
	if board[2][0] == board[3][1] == board[4][2] == board[5][3] != "  ":
		win = board[2][0]
	if board[2][1] == board[3][2] == board[4][3] == board[5][4] != "  ":
		win = board[2][1]
	if board[2][2] == board[3][3] == board[4][4] == board[5][5] != "  ":
		win = board[2][2]
	if board[2][3] == board[3][4] == board[4][5] == board[5][6] != "  ":
		win = board[2][3]

	# Diagonal 2 (12)

	if board[0][3] == board[1][2] == board[2][1] == board[3][0] != "  ":
		win = board[0][3]
	if board[1][3] == board[2][2] == board[3][1] == board[4][0] != "  ":
		win = board[1][3]
	if board[2][3] == board[3][2] == board[4][1] == board[5][0] != "  ":
		win = board[1][3]
	if board[0][4] == board[1][3] == board[2][2] == board[3][1] != "  ":
		win = board[0][4]
	if board[1][4] == board[2][3] == board[3][2] == board[4][1] != "  ":
		win = board[1][4]
	if board[2][4] == board[3][3] == board[4][2] == board[5][1] != "  ":
		win = board[2][4]
	if board[0][5] == board[1][4] == board[2][3] == board[3][2] != "  ":
		win = board[0][5]
	if board[1][5] == board[2][4] == board[3][3] == board[4][2] != "  ":
		win = board[1][5]
	if board[2][5] == board[3][4] == board[4][3] == board[5][2] != "  ":
		win = board[2][5]
	if board[0][6] == board[1][5] == board[2][4] == board[3][3] != "  ":
		win = board[0][6]
	if board[1][6] == board[2][5] == board[3][4] == board[4][3] != "  ":
		win = board[1][6]
	if board[2][6] == board[3][5] == board[4][4] == board[5][3] != "  ":
		win = board[2][6]

	# Board filled (Draw)
	allFilled = True
	for m in range(6):
		for n in range(7):
			if board[m][n] == "  ":
				allFilled = False
	if allFilled:
		win = "DRAW!"

	return win


# Version 2 - goes through every square on the board to check if it is part of a winning line (~35 lines of code)
def checkWin2():

	allFilled = True

	for a in range(6):
		for b in range(7):

			# Vertical
			if a < 3:
				if board[a][b] == board[a + 1][b] == board[a + 2][b] == board[
				    a + 3][b] != "  ":
					return board[a][b]

			# Horizontal
			if b < 4:
				if board[a][b] == board[a][b + 1] == board[a][
				    b + 2] == board[a][b + 3] != "  ":
					return board[a][b]

			# Diagonal 1
			if a < 3 and b < 4:
				if board[a][b] == board[a + 1][b + 1] == board[a + 2][
				    b + 2] == board[a + 3][b + 3] != "  ":
					return board[a][b]

			# Diagonal 2
			if a < 3 and b >= 3:
				if board[a][b] == board[a + 1][b - 1] == board[a + 2][
				    b - 2] == board[a + 3][b - 3] != "  ":
					return board[a][b]

			if board[a][b] == "  ":
				allFilled = False

	if allFilled:
		return "DRAW!"

	return ""


# Version 3 (unused) - checks the squares around the last placed piece (almost 120 lines of code)
def checkWin3(column):
	if board[0][column] == "  ":
		if board[1][column] == "  ":
			if board[2][column] == "  ":
				if board[3][column] == "  ":
					if board[4][column] == "  ":
						row = 5
					else:
						row = 4
				else:
					row = 3
			else:
				row = 2
		else:
			row = 1
	else:
		row = 0

	left = 1
	right = 0
	up = 1
	down = 0
	diag_1_1 = 1
	diag_1_2 = 0
	diag_2_1 = 1
	diag_2_2 = 0

	new_col = column - 1
	while new_col >= 0:
		if board[row][column] == board[row][new_col]:
			left += 1
			new_col -= 1
		else:
			new_col = -1

	new_col = column + 1
	while new_col <= 6:
		if board[row][column] == board[row][new_col]:
			right += 1
			new_col += 1
		else:
			new_col = 7

	new_row = row - 1
	while new_row >= 0:
		if board[row][column] == board[new_row][column]:
			up += 1
			new_row -= 1
		else:
			new_row = -1

	new_row = row + 1
	while new_row <= 5:
		if board[row][column] == board[new_row][column]:
			down += 1
			new_row += 1
		else:
			new_row = 6

	new_row = row + 1
	new_col = column + 1
	while new_row <= 5 and new_col <= 6:
		if board[row][column] == board[new_row][column]:
			diag_1_1 += 1
			new_row += 1
			new_col += 1
		else:
			new_row = 6
			new_col = 7

	new_row = row - 1
	new_col = column - 1
	while new_row >= 0 and new_col >= 0:
		if board[row][column] == board[new_row][column]:
			diag_1_2 += 1
			new_row -= 1
			new_col -= 1
		else:
			new_row = -1
			new_col = -1

	new_row = row + 1
	new_col = column - 1
	while new_row <= 5 and new_col >= 0:
		if board[row][column] == board[new_row][column]:
			diag_2_1 += 1
			new_row += 1
			new_col -= 1
		else:
			new_row = 6
			new_col = -1

	new_row = row - 1
	new_col = column + 1
	while new_row >= 0 and new_col <= 6:
		if board[row][column] == board[new_row][column]:
			diag_2_2 += 1
			new_row -= 1
			new_col += 1
		else:
			new_row = -1
			new_col = 7

	if left + right >= 4 or up + down >= 4 or diag_1_1 + diag_1_2 >= 4 or diag_2_1 + diag_2_2 >= 4:
		return board[row][column]

	allFilled = True
	for v in range(6):
		for w in range(7):
			if board[v][w] == "  ":
				allFilled = False
	if allFilled:
		return "DRAW!"

	return ""


def timer():
	global counter
	counter = 0.00
	while game:
		s(0.01)
		counter += 0.01


initBoard()

player = 1
game = True

t(target=timer).start()

while game:
	printBoard()
	col = input("\nPlayer " + str(player) + ": ")
	if str.isdigit(col):
		if int(col) >= 1 and int(col) <= 7:
			if board[0][int(col) - 1] == "  ":
				if board[1][int(col) - 1] == "  ":
					if board[2][int(col) - 1] == "  ":
						if board[3][int(col) - 1] == "  ":
							if board[4][int(col) - 1] == "  ":
								if board[5][int(col) - 1] == "  ":
									board[5][int(col) - 1] = "P" + str(player)
								else:
									board[4][int(col) - 1] = "P" + str(player)
							else:
								board[3][int(col) - 1] = "P" + str(player)
						else:
							board[2][int(col) - 1] = "P" + str(player)
					else:
						board[1][int(col) - 1] = "P" + str(player)
				else:
					board[0][int(col) - 1] = "P" + str(player)
			else:
				print("Invalid.")
				s(1)
				player -= 1
		else:
			print("Invalid.")
			s(1)
			player -= 1
	else:
		print("Invalid.")
		s(1)
		player -= 1

	for x in range(6):
		for y in range(7):
			if board[x][y] == "P1":
				board[x][y] = "\033[1;31;40mP1\033[1;37;0m"
			if board[x][y] == "P2":
				board[x][y] = "\033[1;32;40mP2\033[1;37;0m"

	player += 1
	if player == 3:
		player = 1

	if checkWin2() != "":
		game = False

	sys('clear')

printBoard()

if checkWin() != "DRAW!":
	print("\n" + checkWin2(), "wins!")
else:
	print("\n" + checkWin2())

print("\nThanks for playing!")
mins = f(counter / 60)
secs = f(counter - (mins * 60))
hunds = round((counter - mins * 60 - secs) * 100, 0)
print(
    "This game lasted",
    str.zfill(str(mins), 2) + ":" + str.zfill(str(secs), 2) + "." +
    str.zfill(str(int(hunds)), 2))
