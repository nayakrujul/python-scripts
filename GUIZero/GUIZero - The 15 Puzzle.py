from guizero import App, Box, PushButton, Text
from random import shuffle

difficulty = input(
    'Select difficulty: \n' \
    '[1] Easy (3 x 3) \n' \
    '[2] Medium (4 x 4) - default \n' \
    '[3] Hard (5 x 5) \n' \
    ' > '
)

if difficulty == '1':
    BOARD_SIZE = 3
elif difficulty == '3':
    BOARD_SIZE = 5
else:
    BOARD_SIZE = 4

def clear_board():
    lst = list(range(1, BOARD_SIZE ** 2))
    shuffle(lst)
    lst.append('')
    new_board = [[None for a in range(BOARD_SIZE)] for b in range(BOARD_SIZE)]
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            button = PushButton(
                board, text=str(lst[(x*BOARD_SIZE)+y]), grid=[x, y], width=3, command=swap, args=[x, y]
            )
            new_board[x][y] = button
    return new_board

def get_empty_square():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board_squares[x][y].text == '':
                return x, y

def swap(x, y):
    global move_counter
    if game:
        a, b = get_empty_square()
        if (
            (x not in [a - 1, a, a + 1]) or
            (y not in [b - 1, b, b + 1]) or
            ((x, y) in [(a, b), (a - 1, b - 1), (a - 1, b + 1), (a + 1, b - 1), (a + 1, b + 1)])
        ):
            return -1
        board_squares[a][b].text, board_squares[x][y].text = board_squares[x][y].text, board_squares[a][b].text
        move_counter += 1
        message.value = 'Moves: ' + str(move_counter)
        check_win()

def check_win():
    global game
    flattened = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            flattened.append(board_squares[y][x].text)
    game = not (flattened == [str(z) for z in list(range(1, BOARD_SIZE ** 2))] + [''])
    if game == False:
        message.value = 'You won in ' + str(move_counter) + ' moves!'
        parity.value = ''
        for a in board_squares:
            for b in a:
                b.bg = 'green'
                b.text_color = 'white'

def inversions():
    flattened = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            flattened.append(board_squares[y][x].text)
    want = [str(z) for z in list(range(1, BOARD_SIZE ** 2))] + ['']
    inv = 0
    for a in range(len(flattened)):
        for b in range(a):
            if want.index(flattened[a]) > want.index(flattened[b]):
                inv += 1
    return inv

def solvable():
    global game
    if inversions() % 2 == 0:
        return 'solvable'
    game = None
    return 'unsolvable'

def reset():
    global board_squares, move_counter, game
    board_squares = clear_board()
    move_counter = 0
    game = True
    check_win()
    message.value = 'Moves: 0'
    parity.value = 'This puzzle is ' + solvable()

app = App("The 15 Puzzle - RN09")
board = Box(app, layout="grid")
board_squares = clear_board()

move_counter = 0
game = True
check_win()

Text(app, '')
message = Text(app, 'Moves: 0')
parity = Text(app, 'This puzzle is ' + solvable())
Text(app, '')

PushButton(app, text='New puzzle', command=reset)

app.display()