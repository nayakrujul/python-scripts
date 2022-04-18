from guizero import App, PushButton, Slider, Text, TextBox
from threading import Thread
from time import sleep
from matplotlib import pyplot
from numpy import array


f = open('countries.txt')
countries = [x.lower() for x in f.read().split('\n')]
f.close()


def timer():
    global counter
    while counter > 0:
        sleep(0.1)
        counter -= 0.1
        time_left.value = str(int(counter // 60)) + ':' + str(round(round(counter, 1) - ((counter // 60) * 60), 1)).zfill(4)
    time_left.value = '0:00.0'
    textbox.hide()
    score_text.value = 'You got ' + str(score) + ' countries in ' + str(duration.value) + 's'
    print('Ignore the warning message(s) below')
    fig, ax = pyplot.subplots()
    ax.plot(array(times), array(range(len(times))))
    ax.set(xlabel='Time (s)', ylabel='Correct #')
    pyplot.show()

def start_game():
    global counter
    counter = float(duration.value)
    title.value = 'Name as many countries as you can'
    time_left.show()
    duration.hide()
    start.hide()
    textbox.show()
    score_text.show()
    Thread(target=timer).start()

def check():
    global score
    if textbox.value.lower() in countries and counter > 0:
        countries.remove(textbox.value.lower())
        textbox.value = ''
        score += 1
        score_text.value = 'Score: ' + str(score)
        times.append(duration.value - counter)


app = App('Name the countries')

title = Text(app, 'Choose the duration in seconds', size=20)
time_left = Text(app, visible=False)

duration = Slider(app, 30, 600)
start = PushButton(app, text='Start', command=start_game)

textbox = TextBox(app, visible=False, command=check)
score_text = Text(app, 'Score: 0', visible=False)
score = 0

times = [0]

app.display()