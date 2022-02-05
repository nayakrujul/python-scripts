from random import choice


print('\033[1;34mWelcome to Lingo.\033[0m\n\n'
      'Guess the 5-letter word to win.\n'
      'In each round you must guess a 5-letter word.\n'
      'It will then tell you if the letters are correct:\n\n'
      '\033[1;32mGreen\033[0m means it is in the word and in the correct position\n'
      '\033[1;33mOrange\033[0m means it is in the word but not in the right place\n'
      '\033[1;31mRed\033[0m means it is not in the word\n\n'
      'The first letter will be given to you.\n'
      'You have five guesses.\n')


f = open('words.txt')
words = f.read().split('\n')
f.close()


def check(real, guess):
    ret = [0 for x in range(len(real))]
    guessed = []
    for y in range(len(real)):
        if real[y] == guess[y]:
            ret[y] = 2
            guessed.append(real[y])
    for z in range(len(real)):
        if guess[z] in real and guess[z] not in guessed:
            ret[z] = 1
    return ret


def display(lst, guess, num):
    guess = guess.upper()
    for a in range(len(lst)):
        if lst[a] == 0:
            print('\033[1;31m_', end='')
        elif lst[a] == 1:
            print('\033[1;33m', guess[a], sep='', end='')
        else:
            print('\033[1;32m', guess[a], sep='', end='')
    print('\033[0m -', num, 'guesses left.')
    return lst == [2 for b in range(len(lst))]


word = choice(words)
guesses = 5
display(check(word, word[0] + '    '), word[0] + '    ', guesses)
while guesses > 0:
    guess_word = input('Guess a word: ').lower()
    guesses -= 1
    if guess_word not in words:
        print('Not a word. Game over. The word was:', word.upper())
        break
    if display(check(word, guess_word), guess_word, guesses):
        print('Well done, you won!')
        break
else:
    print('You ran out of guesses. The word was:', word.upper())
