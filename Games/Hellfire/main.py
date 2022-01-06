from curses import wrapper
from time import sleep
from random import randint
from os import system


class Game:

    def __init__(self):
        self.board = [[' ' for a in range(20)] for b in range(5)]
        self.level = 2
        self.speed = 3
        self.rnd_count = 3
        self.score = 0
        self.board[self.level][0] = 'X'

    def __str__(self):
        return '\n'.join([' '.join(c + ["^"]) for c in self.board])

    def random_block(self):
        self.board[randint(0, 4)][-1] = '|'
        self.rnd_count = 0

    def update(self):
        for x in self.board:
            x.pop(0)
            x.append(' ')
        self.rnd_count += 1
        if self.rnd_count >= 3:
            self.random_block()
        self.score += 1
        if self.score % 10 == 0:
            self.speed += 0.5

    def over(self):
        if self.board[self.level][0] == '|':
            return False
        self.board[self.level][0] = 'X'
        return True


running = True
win = False
game = Game()


def main(stdscr):

    global running, win, game

    stdscr.nodelay(1)

    while running:

        c = stdscr.getch()
        if c == 258 and game.level < 4:
            game.level += 1
        if c == 259 and game.level > 0:
            game.level -= 1

        game.update()
        running = game.over()

        if game.score >= 200:
            running = False
            win = True

        stdscr.move(0, 0)
        stdscr.addstr('Score: ' + str(game.score) + '\n')
        stdscr.addstr(str(game))

        sleep(1 / game.speed)


input("""HELLFIRE by nayakrujul
Instructions:
Avoid the oncoming missiles using the up and down arrow keys.
Get to a score of 200 to complete the first level.
Press return to continue.
""")

system('clear')

wrapper(main)

if win:
    print("Well done, you beat the level.")
else:
    print("You got ", game.score, ". Try again to see if you can do better.", sep="")
