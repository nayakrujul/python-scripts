import curses, random, time, threading, math

running = False
index = 0
starting = random.randint(10, 20)
counter = starting
tot_words = -1


def timer():

    global counter
    while True:
        if running:
            time.sleep(0.1)
            counter -= 0.1
        if counter <= 0:
            break


def new_word():

    global tot_words
    f = open("TypingTest_words.txt")
    words = f.read().split("\n")
    words_lst = []
    for x in words:
        [words_lst.append(y) for y in x.split()]
    tot_words += 1
    return random.choice(words_lst).lower()


word = new_word()


def main(stdscr):

    global index, word, running

    stdscr.nodelay(1)

    stdscr.addstr("Press any key")

    while True:

        c = stdscr.getch()
        if c != -1 and c != 410:
            running = True
            break

    while running:

        c = stdscr.getch()
        if c != -1 and c != 127:
            if chr(c) == word[index]:
                index += 1
                if index == len(word):
                    word = new_word()
                    index = 0
        stdscr.move(0, 0)
        stdscr.addstr(index * " " + word[index:] + (10 - len(word)) * " " + str(math.ceil(counter)) + " ")
        stdscr.refresh()

        if counter <= 0:
            break


my_thread = threading.Thread(target=timer)
my_thread.start()

curses.wrapper(main)

print(f"Words typed: {tot_words}.\nWords per minute: {round((60 / starting) * tot_words, 2)} wpm")
