from guizero import App, Picture, PushButton, Text, TextBox
from os import listdir, remove, system
from random import choice
from cv2 import imread, imwrite
from numpy import array

def path(c):
    return f'flags4/{c}.png'

def check():
    global game_running
    if game_running:
        for y in countries:
            if user_input.value.lower() == y.lower():
                img1 = imread(path(y))
                img2 = imread(path(correct_answer))
                new_flag = []
                for a, p in zip(img1, img2):
                    new_flag.append([])
                    for b, q in zip(a, p):
                        b1, g1, r1 = b
                        b2, g2, r2 = q
                        b3 = abs(b1 - b2) // 3
                        g3 = abs(g1 - g2) // 3
                        r3 = abs(r1 - r2) // 3
                        new_flag[-1].append([255 - (r3 + g3 + b3)] * 3)
                system('clear')
                imwrite('temp.png', array(new_flag))
                flag.image = 'temp.png'
                remove('temp.png')
                user_input.value = ''
                if y in correct_answer:
                    title.value = 'You win!\n\n'
                    flag.image = path(correct_answer)
                    game_running = False
                    user_input.disable()
                return None

def reveal():
    global game_running
    title.value = 'The answer was ' + correct_answer + '\n\n'
    flag.image = path(correct_answer)
    game_running = False
    user_input.disable()

countries = []
for x in listdir('flags4'):
    countries.append(x[:-4])

game_running = True

app = App('Flagle')

title = Text(app, 'Flagle\n\n', size=20)

correct_answer = choice(countries)

flag = Picture(app, height=100)

Text(app, '\n\nEnter a country:')
user_input = TextBox(app, width=20)
submit = PushButton(app, check, text='Check')

Text(app, '')

give_up = PushButton(app, reveal, text='Give up')

Text(app, '\n\nHow this works:\n\nGuess the country/territory.\nWhen you enter a country, the two flags are compared.\nThe more similar areas are lighter.\nThe less similar areas are darker.')

app.set_full_screen()
app.display()
