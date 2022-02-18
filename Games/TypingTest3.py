from getkey import getkey
from random import choice
from string import ascii_uppercase
from time import sleep
from os import system
from threading import Thread


counter = 0.0
timing = False
left = 20
correct = 0
counts = []


def timer():
    global counter
    while left > 0:
        if timing:
            sleep(0.1)
            counter += 0.1


input('Press the key which appears on the screen.\nPress RETURN to continue. ')
system('clear')
timer_thread = Thread(target=timer)
timer_thread.start()


while left > 0:
    system('clear')
    ans = choice(ascii_uppercase)
    print(ans)
    timing = True
    key = getkey()
    timing = False
    counts.append(counter)
    counter = 0.0
    if key.upper() == ans:
        correct += 1
    left -= 1

system('clear')
print('You got ', correct, ' out of 20 (', correct * 5, '%).', sep='')
print('Average time:', round(sum(counts) / 20, 2), 'seconds.')
print('Slowest time:', round(max(counts), 1), 'seconds.')
print('Fastest time:', round(min(counts), 1), 'seconds.')
print('Score: ', round((1.7 - sum(counts) / 20) * correct * 5, 1), '%', sep='')
