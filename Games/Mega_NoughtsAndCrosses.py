import os


def display(lst, won_lst):

    colour = ['\033[0m', '\033[1;34m', '\033[1;31m']

    for a in range(0, 9, 3):
        
        print(colour[won_lst[a]], end='')
        print(' | '.join(lst[a][0]), end='\t')
        print(colour[won_lst[a + 1]], end='')
        print(' | '.join(lst[a + 1][0]), end='\t')
        print(colour[won_lst[a + 2]], end='')
        print(' | '.join(lst[a + 2][0]))

        print(colour[won_lst[a]] + '-- --- --', end='\t')
        print(colour[won_lst[a + 1]] + '-- --- --', end='\t')
        print(colour[won_lst[a + 2]] + '-- --- --')

        print(colour[won_lst[a]], end='')
        print(' | '.join(lst[a][1]), end='\t')
        print(colour[won_lst[a + 1]], end='')
        print(' | '.join(lst[a + 1][1]), end='\t')
        print(colour[won_lst[a + 2]], end='')
        print(' | '.join(lst[a + 2][1]))

        print(colour[won_lst[a]] + '-- --- --', end='\t')
        print(colour[won_lst[a + 1]] + '-- --- --', end='\t')
        print(colour[won_lst[a + 2]] + '-- --- --')

        print(colour[won_lst[a]], end='')
        print(' | '.join(lst[a][2]), end='\t')
        print(colour[won_lst[a + 1]], end='')
        print(' | '.join(lst[a + 1][2]), end='\t')
        print(colour[won_lst[a + 2]], end='')
        print(' | '.join(lst[a + 2][2]))

        print('\n')


def checkWin(board, player):

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    elif " " not in board[0] and " " not in board[1] and " " not in board[2] \
        and 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return "DRAW"

    return False


boards = []
for _ in range(9):
    boards.append([])
    for __ in range(3):
        boards[-1].append([])
        for ___ in range(3):
            boards[-1][-1].append(' ')

won = [0 for ____ in range(9)]
game = True
player = 'X'
play_board = 4


print(
    'The square system in this program works as follows:',
    '1 | 2 | 3',
    '-- --- --',
    '4 | 5 | 6',
    '-- --- --',
    '7 | 8 | 9',
    sep='\n'
)

input('\nPress RETURN to continue. ')


while game:

    os.system('clear')

    display(boards, won)

    print('\033[0mPlayer', player + ', play in board', play_board + 1)

    loop = True
    while loop:
        num = input('Square number ')

        if num.isdigit():
            num = int(num) - 1
            if 0 <= num <= 8:
                if boards[play_board][num // 3][num - ((num // 3) * 3)] == ' ':
                    boards[play_board][num // 3][num - ((num // 3) * 3)] = player
                    play_board = num
                    loop = False
                else:
                    print('Square not empty')
            else:
                print('Not a square')
        else:
            print('Not a square')
    
    for x in range(9):
        if won[x] == 0:
            if checkWin(boards[x], 'X') == True:
                won[x] = 1
            elif checkWin(boards[x], 'O') == True:
                won[x] = 2
    
    won_board = []
    for y in range(0, 9, 3):
        won_board.append(won[y:y+3])
    if checkWin(won_board, 1) == True:
        win = 'X wins'
        break
    elif checkWin(won_board, 2) == True:
        win = 'O wins'
        break
    elif checkWin(won_board, 3) == 'DRAW':
        win = 'Draw'
        break

    if player == 'X':
        player = 'O'
    else:
        player = 'X'

os.system('clear')
display(boards, won)
print(win)
