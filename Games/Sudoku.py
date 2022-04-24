from random import sample, randint
from os import system


class board:
    
    def __init__(self, base):
        self.base = base
        side = base ** 2
        pattern = lambda r,c: (base * (r % base)+ r // base + c) % side
        shuffle = lambda s: sample(s, len(s))
        
        rBase = list(range(base))
        rows  = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)] 
        cols  = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums  = shuffle(range(1,base*base+1))

        self.board = [[nums[pattern(r,c)] for c in cols] for r in rows]
        self.solution = tuple([tuple(x) for x in self.board])
        
        for times in range(randint(7, 15)):
            a, b = randint(0, 8), randint(0, 8)
            while self.board[a][b] == ' ':
                a, b = randint(0, 8), randint(0, 8)
            self.board[a][b] = ' '
            self.board[8 - a][8 - b] = ' '

        self.start_board = tuple([tuple(x) for x in self.board])

    def display(self):
        print('  |\033[1;32m 1 2 3 \033[0m|\033[1;32m 4 5 6 \033[0m|\033[1;32m 7 8 9 \033[0m|')
        for row in range(len(self.board)):
            if row % self.base == 0:
                print('- ' * (len(self.board) + self.base + 2))
            print('\033[1;32m' + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'][row] + '\033[0m', end=' ')
            for col in range(len(self.board)):
                if col % self.base == 0:
                    print('| ', end='')
                if self.board[row][col] == self.start_board[row][col]:
                    print(self.board[row][col], end=' ')
                else:
                    print('\033[1;31m', self.board[row][col], '\033[0m', end=' ', sep='')
            print('|')
        print('- ' * (len(self.board) + self.base + 1))
        

game_board = board(3)
game = True

while game:
    
    system('clear')
    print('\033[3m\033[4mSudoku\033[0m\n')
    game_board.display()
    
    loop = True
    while loop:
        print('')
        grid = input('Square (e.g. A1): ')
        if len(grid) == 2:
            row_num, col_num = list(grid)
            if row_num in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] and col_num.isdigit():
                row_num = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'].index(row_num)
                col_num = int(col_num) - 1
                if 0 <= col_num <= 8:
                    if game_board.start_board[row_num][col_num] == ' ':
                        loop = False
                    else:
                        print('Square not empty.')
                else:
                    print('Out of range.')
            else:
                print('Wrong format.')
        else:
            print('Wrong length.')

    loop2 = True
    while loop2:
        print('')
        num = input('Number (1-9): ')
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 9:
                game_board.board[row_num][col_num] = num
                loop2 = False

    if tuple([tuple(x) for x in game_board.board]) == game_board.solution:
        game = False

system('clear')
game_board.display()
print('\nYou win!')
