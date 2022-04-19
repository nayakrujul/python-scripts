from guizero import App, Drawing, Text, PushButton
from random import choice
from time import sleep
from format_num import format_num


f = open('areas.txt')
data = f.read().split('\n')
f.close()
areas = {}
for line in data:
    areas[line.split(': ')[0]] = int(line.split(': ')[1].replace(',', ''))


def button_pressed(arg):
    global size
    size = 0
    app.repeat(20, slow_reveal, [arg])

def change_colour(colour):
    if app.bg == colour:
        app.bg = None
        app.cancel(change_colour)
    else:
        app.bg = colour

def slow_reveal(arg):
    global size
    if size < areas[country2.value] and areas[country2.value] >= 50:
        c2size.value = format_num(size) + ' sq km'
        size += areas[country2.value] // 50
    else:
        c2size.value = format_num(areas[country2.value]) + ' sq km'
        app.cancel(slow_reveal)
        check(arg)

def check(arg):
    global game, score, imgid, imgid2
    if game:
        if arg == 'B':
            if areas[country1.value] <= areas[country2.value]:
                app.repeat(500, change_colour, ['green'])
                country1.value = country2.value
                c1size.value = format_num(areas[country1.value]) + ' sq km'
                while country2.value == country1.value:
                    country2.value = choice(list(areas.keys()))
                c2size.value = ''
                score += 1
                score_text.value = 'Score: ' + str(score)
                c1flag.delete(imgid)
                try: imgid = c1flag.image(0, 0, 'flags2/' + country1.value + '.png')
                except: imgid = c1flag.image(0, 0, 'flags2/NotFound.png')
                c2flag.delete(imgid2)
                try: imgid2 = c2flag.image(0, 0, 'flags2/' + country2.value + '.png')
                except: imgid2 = c2flag.image(0, 0, 'flags2/NotFound.png')
            else:
                app.repeat(500, change_colour, ['red'])
                game = False
                bigger.hide()
                smaller.hide()
        else:
            if areas[country1.value] >= areas[country2.value]:
                app.repeat(500, change_colour, ['green'])
                country1.value = country2.value
                c1size.value = format_num(areas[country1.value]) + ' sq km'
                while country2.value == country1.value:
                    country2.value = choice(list(areas.keys()))
                c2size.value = ''
                score += 1
                score_text.value = 'Score: ' + str(score)
                c1flag.delete(imgid)
                try: imgid = c1flag.image(0, 0, 'flags2/' + country1.value + '.png')
                except: imgid = c1flag.image(0, 0, 'flags2/NotFound.png')
                c2flag.delete(imgid2)
                try: imgid2 = c2flag.image(0, 0, 'flags2/' + country2.value + '.png')
                except: imgid2 = c2flag.image(0, 0, 'flags2/NotFound.png')
            else:
                app.repeat(500, change_colour, ['red'])
                game = False
                bigger.hide()
                smaller.hide()
    if not game:
        play_again.show()

def new_game():
    global game, score, imgid, imgid2
    country1.value = choice(list(areas.keys()))
    c1size.value = format_num(areas[country1.value]) + ' sq km'
    country2.value = choice(list(areas.keys()))
    c2size.value = ""
    c1flag.delete(imgid)
    c2flag.delete(imgid2)
    try: imgid = c1flag.image(0, 0, 'flags2/' + country1.value + '.png')
    except: imgid = c1flag.image(0, 0, 'flags2/NotFound.png')
    try: imgid2 = c2flag.image(0, 0, 'flags2/' + country2.value + '.png')
    except: imgid2 = c2flag.image(0, 0, 'flags2/NotFound.png')
    bigger.show()
    smaller.show()
    play_again.hide()
    score_text.value = "Score: 0"
    game = True
    score = 0
    

app = App("Bigger or smaller?")

country1 = Text(app, choice(list(areas.keys())), size=20)
c1size = Text(app, format_num(areas[country1.value]) + ' sq km')
c1flag = Drawing(app, width=100, height=120)
try: imgid = c1flag.image(0, 0, 'flags2/' + country1.value + '.png')
except: imgid = c1flag.image(0, 0, 'flags2/NotFound.png')

Text(app, "vs\n\n")

country2 = Text(app, choice(list(areas.keys())), size=20)
while country2.value == country1.value:
    country2.value = choice(list(areas.keys()))
c2size = Text(app, "")
c2flag = Drawing(app, width=100, height=120)
try: imgid2 = c2flag.image(0, 0, 'flags2/' + country2.value + '.png')
except: imgid2 = c2flag.image(0, 0, 'flags2/NotFound.png')

bigger = PushButton(app, text="Bigger", command=button_pressed, args=['B'])
smaller = PushButton(app, text="Smaller", command=button_pressed, args=['S'])

Text(app, "\n\n\n")

score_text = Text(app, "Score: 0")

Text(app, "")

play_again = PushButton(app, text="Play again", command=new_game, visible=False)

game = True
score = 0

app.set_full_screen()
app.display()
