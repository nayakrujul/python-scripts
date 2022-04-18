from guizero import App, Box, PushButton, Text
from time import time
from random import choice, shuffle
from threading import Thread


difficulty = input(
    'Select difficulty: \n' \
    '[0] Practice (5 x 5) \n' \
    '[1] Easy (10 x 10) \n' \
    '[2] Medium (15 x 15) - default \n' \
    '[3] Hard (20 x 20) \n' \
    ' > '
)

if difficulty == '0':
    BOARD_SIZE = 5
elif difficulty == '1':
    BOARD_SIZE = 10
elif difficulty == '3':
    BOARD_SIZE = 20
else:
    BOARD_SIZE = 15

first_move = True
checked_already = []
game = True
win = False

def clear_board():
    new_board = [[None for a in range(BOARD_SIZE)] for b in range(BOARD_SIZE)]
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            button = PushButton(
                board, text="", grid=[x, y], width=3, command=press_square, args=[x,y]
            )
            button.when_right_button_pressed = flag
            button.bg = 'white'
            new_board[x][y] = button
    return new_board

def create_board():
    new_board = [[None for a in range(BOARD_SIZE + 1)] for b in range(BOARD_SIZE + 1)]
    for x in range(BOARD_SIZE + 1):
        for y in range(BOARD_SIZE + 1):
            if x < BOARD_SIZE and y < BOARD_SIZE:
                new_board[x][y] = choice([True, False, False, False, False])
            else:
                new_board[x][y] = False
    return new_board

def number_on_square(x, y):
    if actual_board[x][y]:
        return -1
    return [
        actual_board[x + 1][y],
        actual_board[x - 1][y],
        actual_board[x][y + 1],
        actual_board[x][y - 1],
        actual_board[x + 1][y + 1],
        actual_board[x + 1][y - 1],
        actual_board[x - 1][y + 1],
        actual_board[x - 1][y - 1]
    ].count(True)

def first_turn_move(x, y):
    global checked_already, first_move
    checked_already.append((x, y))
    first_move = False
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return None
    if len(checked_already) > (BOARD_SIZE ** 2) // 5:
        return -1
    num = number_on_square(x, y)
    if len(checked_already) == 1:
        actual_board[x][y] = False
        num = number_on_square(x, y)
    if num != -1:
        board_squares[x][y].text = str(num)
        board_squares[x][y].bg = 'green'
        check = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1)
        ]
        shuffle(check)
        for a, b in check:
            if (a, b) not in checked_already:
                if first_turn_move(a, b) == -1:
                    return -1

def press_square(x, y):
    global game, message, win, start_time
    if game and (not win):
        if first_move:
            start_time = time()
            timer_thread.start()
            first_turn_move(x, y)
        else:
            num = number_on_square(x, y)
            if num == -1:
                game = False
                message.value = '\nYou lose'
                board_squares[x][y].text = 'BOOM'
                board_squares[x][y].bg = 'red'
                board_squares[x][y].text_color = 'white'
                for a in range(BOARD_SIZE):
                    for b in range(BOARD_SIZE):
                        if actual_board[a][b]:
                            board_squares[a][b].text = 'BOOM'
                            if board_squares[a][b].bg != 'yellow':
                                board_squares[a][b].bg = 'red'
                                board_squares[a][b].text_color = 'white'
                        elif board_squares[a][b].bg == 'yellow':
                            board_squares[a][b].text = 'X'
                            board_squares[a][b].bg = 'orange'
                            board_squares[a][b].text_color = 'white'
            else:
                board_squares[x][y].text = str(num)
                board_squares[x][y].bg = 'green'
    elif not game:
        message.value = '\nYou lose\nPressing squares isn\'t going to change that'
    if check_win():
        message.value = 'You win!'
        win = True

def flag(data):
    if data.widget.text == '':
        data.widget.text = '⚠️'
        data.widget.bg = 'yellow'
    elif data.widget.text == '⚠️':
        data.widget.text = ''
        data.widget.bg = 'white'
    
def check_win():
    if not game:
        return False
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if not (board_squares[x][y].text != '' or actual_board[x][y]):
                return False
    return True

def timer():
    while game and (not win):
        if not first_move:
            time_msg.value = 'Time: ' + str(int(time() - start_time)).zfill(3)


app = App("Minesweeper - RN09")
board = Box(app, layout="grid")
board_squares = clear_board()
actual_board = create_board()

Text(app, '')
message = Text(app, 'Press the squares to play')
time_msg = Text(app, 'Time: 000')

timer_thread = Thread(target=timer)

app.display()
