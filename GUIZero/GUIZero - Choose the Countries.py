from guizero import App, Box, PushButton, Text
from random import randint, sample, shuffle

f = open('countries.csv')
data = f.read().split('\n')
countries, capitals = [], []
for line in data:
    countries.append(line.split(',')[0])
    if line.split(',')[0] != line.split(',')[1]:
        capitals.append(line.split(',')[1])

def get_list():
    num = randint(30, 70)
    lst = sample(countries, num) + sample(capitals, 100 - num)
    shuffle(lst)
    return lst

def colour(x, y):
    global selected
    if 'Select' in title.value:
        if squares[x][y].bg == 'lightblue':
            squares[x][y].bg = None
            selected -= 1
        else:
            squares[x][y].bg = 'lightblue'
            selected += 1
        title.value = f'Select all the countries ({selected} selected)'

def check():
    correct = 0
    total = 0
    for x in range(10):
        for y in range(10):
            if squares[x][y].text in countries:
                total += 1
                if squares[x][y].bg == 'lightblue':
                    squares[x][y].bg = 'lightgreen'
                    correct += 1
                else:
                    squares[x][y].bg = 'yellow'
            elif squares[x][y].bg == 'lightblue':
                squares[x][y].bg = 'orange'
    title.value = f'You got {correct} out of {total}'
    key.show()
    
def clear_board():
    new_board = [[None for a in range(10)] for b in range(10)]
    for x in range(10):
        for y in range(10):
            button = PushButton(
                box,
                text=countries_list[x*10 + y],
                grid=[x, y],
                command=colour,
                args=[x, y]
            )
            new_board[x][y] = button
    return new_board

app = App('Choose the countries')

title = Text(app, 'Select all the countries (0 selected)', size=20)

Text(app, '\n\n')

box = Box(app, layout='grid')

countries_list = get_list()

squares = clear_board()

Text(app, '\n\n')

submit = PushButton(app, text='Submit', command=check)

Text(app, '\n\n')

key = Text(app, 'Green = correctly selected (was a country) \nOrange = incorrectly selected (wasn\'t a country) \nYellow = incorrectly not selected (was a country)', visible=False)

selected = 0

app.display()