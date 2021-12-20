import curses, threading, time, random


index = 0
running = True
counter = 0.0
mistakes = -1

f = open('TypingTest_words.txt')
words_list = f.read().split('\n')
words = []
for x in words_list:
    words.append(x.split()[0])
    words.append(x.split()[1])

sentence = []
for times in range(random.randint(7, 10)):
    sentence.append(random.choice(words))
sentence = ' '.join(sentence).lower()


def timer():

    global counter
    while running:
        if index:
            time.sleep(0.1)
            counter += 0.1


def check(char, stdscr):

    global index, running, counter, mistakes

    if sentence[index].lower() == char.lower():
        index += 1
        if index == len(sentence):
            running = False
        ret = True
    else:
        mistakes += 1
        ret = False

    stdscr.move(2, 0)
    stdscr.addstr(f'{mistakes} mistake(s)')

    if index == 1:
        stdscr.addstr('\nTimer in progress.')

    return ret


def main(stdscr):

    global index
    stdscr.nodelay(1)

    stdscr.addstr(sentence)

    while running:

        c = stdscr.getch()
        if c != -1 and c != 127:
            if check(chr(c), stdscr):
                stdscr.move(0, 0)
                stdscr.addstr(index * " " + sentence[index:])
            stdscr.refresh()


my_thread = threading.Thread(target=timer)
my_thread.start()

curses.wrapper(main)
print('Time: ', round(counter, 1),
      ' seconds.\nMistakes: ', mistakes,
      '.\nTime per character: ', round(len(sentence) / round(counter, 1), 2),
      " char/sec.", sep="")
