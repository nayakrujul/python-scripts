from guizero import App, Drawing, PushButton, Text, TextBox
from os import listdir
from random import choice


f = open('codes.txt')
data = f.read().split('\n')
codes = {}
for line in data:
    codes[line.split(': ')[1].lower()] = line.split(': ')[0]


def choose_country():
    chosen = choice(listdir('icons'))[:2]
    return chosen, codes[chosen]

def submit_answer():
    global score, questions, code, country, imgid
    if answer.value.lower() == country.lower():
        score += 1
        correct.value = 'Correct!'
    else:
        correct.value = 'Incorrect - ' + country
    questions += 1
    answer.value = ''
    drawing.delete(imgid)
    code, country = choose_country()
    imgid = drawing.image(0, 0, f'icons/{code}.png')
    score_text.value = str(score) + '/' + str(questions) 

app = App("Country outlines")

Text(app, 'Which country is this?', size=20)

code, country = choose_country()
drawing = Drawing(app, width=250, height=250)
imgid = drawing.image(0, 0, f'icons/{code}.png')

score = 0
questions = 0

Text(app, '\n\n')

answer = TextBox(app)
submit = PushButton(app, text='Check', command=submit_answer)

Text(app, '\n\n')

correct = Text(app)
score_text = Text(app, '0/0')

app.set_full_screen()

app.display()