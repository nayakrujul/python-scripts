from guizero import App, Text, Drawing, Box, PushButton
from random import choice, sample, shuffle
from os import listdir
from PIL import Image

def options():
    options = [country] + sample(countries, 3)
    shuffle(options)
    for x in range(4):
        choices[x].text = options[x]

def new_flag():
    global country, countries, imgid
    flag.delete(imgid)
    country = choice(countries)
    countries.remove(country)
    image = Image.open('flags4/' + country + '.png')
    flag.resize(image.size[0], image.size[1])
    imgid = flag.image(0, 0, 'flags4/' + country + '.png')
    if countries == []:
        countries = [file[:-4] for file in listdir('flags4')]
    options()
    score_text.value = f'\nScore: {score}/{questions}'

def change_colour(x, colour, y=-1):
    if choices[x].bg == colour:
        choices[x].bg = None
        if y != -1:
            choices[y].bg = None
        app.cancel(change_colour)
        new_flag()
    else:
        if y != -1:
            choices[y].bg = 'green'
        choices[x].bg = colour

def correct_answer():
    for x in range(4):
        if choices[x].text == country:
            return x

def check(x):
    global score, questions
    questions += 1
    if choices[x].text == country:
        score += 1
        app.repeat(1000, change_colour, [x, 'green'])
    else:
        app.repeat(1000, change_colour, [x, 'red', correct_answer()])

def clear_board():
    new_board = [None, None, None, None]
    for x in range(4):
        button = PushButton(
            app,
            text='',
            command=check,
            args=[x]
        )
        new_board[x] = button
    return new_board

countries = [file[:-4] for file in listdir('flags4')]

app = App('Flags')

Text(app, 'Name this flag\n', size=20)

flag = Drawing(app, width=500, height=500)
country = choice(countries)
countries.remove(country)
image = Image.open('flags4/' + country + '.png')
flag.resize(image.size[0], image.size[1])
imgid = flag.image(0, 0, 'flags4/' + country + '.png')

Text(app, '\n\n')

choices = clear_board()

Text(app, '\n\n')

score_text = Text(app, '\nScore: 0/0')

options()

score = 0
questions = 0

app.set_full_screen()
app.display()