from guizero import App, Slider, PushButton, Text, TextBox
from random import choice

f = open('capitals.csv')
data = f.read().split('\n')
capitals = {}
for line in data:
    capitals[line.split(',')[0]] = line.split(',')[1].lower()

def new_capital():
    _country = choice(list(capitals.keys()))
    _capital = capitals[_country]
    capitals.pop(_country)
    return _country, _capital

def display_right_wrong():
    Text(app, 'Correct:', size=15)
    for _country, _capital in correct.items():
        Text(app, _country + ': ' + _capital)
    Text(app)
    Text(app, 'Incorrect:', size=15)
    for _country_, _capital_ in wrong.items():
        Text(app, _country_ + ': ' + _capital_)

def check():
    global country, capital, score, questions, game
    if answer.value.lower() == capital and game:
        answer.value = ''
        last_answer.value = ''
        correct[country] = ' '.join([item.capitalize() for item in capital.split()])
        country, capital = new_capital()
        score += 1
        questions -= 1
        title.value = 'What is the capital of ' + country
        score_text.value = 'Score: ' + str(score) + ' out of ' + str(questions_slider.value - questions)
    elif answer.value.lower() == 'pass' and game:
        questions -= 1
        answer.value = ''
        last_answer.value = 'The capital of ' + country + ' is ' + ' '.join([item.capitalize() for item in capital.split()])
        wrong[country] = ' '.join([item.capitalize() for item in capital.split()])
        country, capital = new_capital()
        title.value = 'What is the capital of ' + country
        score_text.value = 'Score: ' + str(score) + ' out of ' + str(questions_slider.value - questions)
    if questions == 0:
        title.value = 'You scored ' + str(score) + ' out of ' + str(questions_slider.value)
        answer.hide()
        last_answer.hide()
        pass_text.hide()
        score_text.hide()
        t1.hide()
        t2.hide()
        display_right_wrong()

def start():
    global questions
    title.value = 'What is the capital of ' + country
    questions = questions_slider.value
    questions_slider.hide()
    start_button.hide()
    answer.show()
    pass_text.show()
    score_text.show()

app = App('Country capitals')

country, capital = new_capital()

title = Text(app, 'Choose the number of questions', size=20)

t1 = Text(app, '\n\n')

questions_slider = Slider(app, 1, 197, width=500)

start_button = PushButton(app, text='Start', command=start)

answer = TextBox(app, command=check, visible=False)

pass_text = Text(app, 'Type "pass" to pass', visible=False)

t2 = Text(app, '\n\n')

score_text = Text(app, 'Score: 0 out of 0', visible=False)

Text(app, '\n\n')

last_answer = Text(app)

score = 0

game = True

correct = {}

wrong = {}

app.set_full_screen()

app.display()