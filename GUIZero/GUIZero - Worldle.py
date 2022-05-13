from guizero import App, Box, Drawing, PushButton, Text, TextBox
from os import listdir
from random import choice
from math import radians, cos, sin, asin, sqrt


f = open('positions.csv')
data = f.read().split('\n')
codes = {}
positions = {}
for line in data:
    code, country, lat, lng = eval('[' + line + ']')
    codes[code.lower()] = country
    positions[country.lower()] = (lat, lng)

def clear_board():
    new_board = [[None for a in range(6)] for b in range(5)]
    for x in range(5):
        for y in range(5):
            text = Text(
                box,
                '  ',
                grid=[y,x]
            )
            new_board[y][x] = text
        text = Text(
            box,
            '    ',
            grid=[5,x]
        )
        new_board[x][5] = text
    return new_board

def distance(latlon1, latlon2):

    lat1, lon1 = latlon1
    lat2, lon2 = latlon2
    
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
      
    return c * 6371

def choose_country():
    chosen = choice(listdir('icons'))[:2]
    return chosen, codes[chosen]

def submit_answer():
    global row
    if answer.value.lower() in positions.keys():
        dist = distance(positions[country.lower()], positions[answer.value.lower()])
        for x in range(5):
            if dist <= (10000 - (x * 2500)):
                squares[x][row].bg = 'green'
            else:
                squares[x][row].bg = 'yellow'
        squares[row][5].value = str(int(dist)) + 'km'
        answer.value = ''
        row += 1
        if dist == 0 or row == 5:
            answer.disable()
            submit.disable()
            Text(app, 'Correct answer was ' + country)

app = App("Country outlines")

Text(app, 'Which country is this?', size=20)

code, country = choose_country()
drawing = Drawing(app, width=250, height=250)
imgid = drawing.image(0, 0, f'icons/{code}.png')

Text(app, '\n\n')

box = Box(app, layout='grid')
squares = clear_board()
row = 0

Text(app, '\n\n')

answer = TextBox(app)
submit = PushButton(app, text='Submit', command=submit_answer)

Text(app, '\n\n')

app.set_full_screen()

app.display()