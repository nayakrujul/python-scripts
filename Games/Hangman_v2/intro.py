from os import system
from time import sleep


def delay_type(text, delay=0.1, colour='\033[0m'):
    print(colour, end='')
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print('\033[0m',end='')



def intro():

    delay_type(
'''Program made by

\033[1;31mR R R R R R R R     \033[1;32mN N N                     N N       \033[1;33m0 0 0 0 0 0 0 0     \033[1;34m9 9 9 9 9 9 9 9
\033[1;31mR R R R R R R R     \033[1;32mN N N N                   N N       \033[1;33m0 0 0 0 0 0 0 0     \033[1;34m9 9 9 9 9 9 9 9
\033[1;31mR R         R R     \033[1;32mN N   N N                 N N       \033[1;33m0 0         0 0     \033[1;34m9 9         9 9
\033[1;31mR R         R R     \033[1;32mN N     N N               N N       \033[1;33m0 0         0 0     \033[1;34m9 9         9 9
\033[1;31mR R         R R     \033[1;32mN N       N N             N N       \033[1;33m0 0         0 0     \033[1;34m9 9         9 9
\033[1;31mR R R R R R R R     \033[1;32mN N         N N           N N       \033[1;33m0 0         0 0     \033[1;34m9 9 9 9 9 9 9 9
\033[1;31mR R R R R R R R     \033[1;32mN N           N N         N N       \033[1;33m0 0         0 0     \033[1;34m9 9 9 9 9 9 9 9
\033[1;31mR R R R             \033[1;32mN N             N N       N N       \033[1;33m0 0         0 0     \033[1;34m            9 9
\033[1;31mR R   R R           \033[1;32mN N               N N     N N       \033[1;33m0 0         0 0     \033[1;34m            9 9
\033[1;31mR R     R R         \033[1;32mN N                 N N   N N       \033[1;33m0 0         0 0     \033[1;34m            9 9
\033[1;31mR R       R R       \033[1;32mN N                   N N N N       \033[1;33m0 0 0 0 0 0 0 0     \033[1;34m9 9 9 9 9 9 9 9
\033[1;31mR R         R R     \033[1;32mN N                     N N N       \033[1;33m0 0 0 0 0 0 0 0     \033[1;34m9 9 9 9 9 9 9 9
\n''',
        0.01
    )

    sleep(3)

    system('clear')
