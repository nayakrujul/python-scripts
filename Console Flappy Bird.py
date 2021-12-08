from curses import wrapper
from time import sleep
from random import randint, random


running = True
poles_x = 19
bird_y = 4
gap = randint(0, 9)
score = 0
speed = 5
hacker = False


def display(stdscr):

    for y in range(10):
        stdscr.move(y, 0)
        for x in range(20):
            if x == poles_x and y != gap:
                stdscr.addstr("|")
            elif y == bird_y and x == 2:
                stdscr.addstr("B")
            else:
                stdscr.addstr(" ")
        stdscr.move(y, 20)
        stdscr.addstr(str(y)[-1])
        if y == 0:
            stdscr.addstr("  Score: " + str(score))


def move(direction):

    global bird_y, hacker

    if direction == 258 and bird_y < 9:
        bird_y += 1
        return True

    if direction == 259 and bird_y > 0:
        bird_y -= 1
        return True

    if 48 <= direction <= 57:
        bird_y = direction - 48
        return True

    if direction == ord('H'):
        hacker = not hacker

    return False


def main(stdscr):

    global poles_x, running, gap, score, speed, bird_y

    stdscr.nodelay(1)

    display(stdscr)

    while running:

        display(stdscr)
        c = stdscr.getch()
        move(c)

        poles_x -= 1
        if poles_x < 0:
            poles_x = 19
            gap = randint(0, 9)
        if poles_x == 2:
            if bird_y != gap:
                break
            else:
                score += 1
                speed += 0.5

        if hacker and int(round(random()) + 0.25):
            bird_y = gap

        sleep(1 / speed)


wrapper(main)

print("Score:", score)
