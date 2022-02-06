from random import choice
from time import sleep
from os import system
from string import ascii_lowercase
from intro import intro


intro()


def delay_print(text, delay=0.1, colour='\033[0m'):
    print(colour, end='')
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print('\033[0m',end='')


f = open('words.txt')
words = [x.lower() for x in f.read().split('\n')]
f.close()

word = choice(words)

delay_print('Welcome to Guess the Word!\n', colour='\033[4m')
delay_print('Press RETURN to continue. ')
input('')

guesses_remaining = 10
word_guessed = False
guessed_word = list(10 * '_')
already_guessed = []

while guesses_remaining > 0 and not word_guessed:
    
    system('clear')
    delay_print(f'You have {guesses_remaining} incorrect guesses remaining.\n\n')
    delay_print(' '.join(guessed_word) + '\n')
    delay_print(' '.join(sorted(already_guessed)) + '\n\n')

    loop = True
    while loop:
        delay_print('Guess a letter: ')
        letter = input('').lower()
        if len(letter) == 1 and letter in ascii_lowercase:
            if letter not in already_guessed and letter not in guessed_word:
                system('clear')
                delay_print('The letter is ')
                sleep(1)
                if letter in word:
                    delay_print('\033[1;32m in \033[0m the word.\n')
                    for i in range(len(word)):
                        if word[i] == letter:
                            guessed_word[i] = letter
                else:
                    delay_print('\033[1;31m not in \033[0m the word.\n')
                    guesses_remaining -= 1
                    already_guessed.append(letter)
                loop = False
            else:
                delay_print('You have already guessed this letter\n', colour='\033[1;31m')
        else:
            delay_print('This is not a letter\n', colour='\033[1;31m')

    if ''.join(guessed_word) == word:
        word_guessed = True

system('clear')
if word_guessed:
    delay_print(f'Well done, you won.\nThe word was \033[1;32m{word}\033[0m\n')
else:
    delay_print(f'You ran out of guesses.\nThe word was \033[1;31m{word}\033[0m\n')
