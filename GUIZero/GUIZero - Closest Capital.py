from guizero import App, Text, TextBox
from math import radians, cos, sin, asin, sqrt
from random import choice


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
     
f = open('positions.csv')
data = f.read().split('\n')
positions = {}
capitals = {}
for line in data:
    country, capital, lat, ns, lon, ew = line.split(', ')
    capitals[country] = capital
    lat = float(lat)
    lon = float(lon)
    if ns == 'S':
        lat = -lat
    if ew == 'W':
        lon = -lon
    positions[country] = (lat, lon)

closest_capital = {}
for country1 in positions.keys():
    closest = [None, None]
    for country2 in positions.keys():
        if country1 != country2:
            dist = distance(positions[country1], positions[country2])
            if closest == [None, None]:
                closest = [dist, country2]
            elif dist < closest[0]:
                closest = [dist, country2]
    closest_capital[country1] = closest[1]


def new_country():
    chosen = choice(list(positions.keys()))
    title.value = 'What is the closest capital to ' + capitals[chosen] + ' (capital of ' + chosen + ')?'
    return chosen, closest_capital[chosen]

def check():
    global score, prompt, correct
    if answer.value.lower() in [x.lower() for x in capitals.values()] or answer.value.lower() in [y.lower() for y in capitals.keys()]:
        if answer.value.lower() == correct.lower() or answer.value.lower() == capitals[correct].lower():
            answer.value = ''
            score += 1
            prompt, correct = new_country()
            score_text.value = 'Score: ' + str(score)
        else:
            answer.value = ''
            answer.disable()
            instructions.hide()
            title.value = 'Wrong. The correct answer was ' + capitals[correct] + ' (capital of ' + correct + ').'

app = App('Closest capital')

title = Text(app, size=20)
instructions = Text(app, 'Name the city or the country that it is capital of.')
Text(app, '\n\n')
answer = TextBox(app, command=check)
score_text = Text(app, 'Score: 0')

prompt, correct = new_country()
score = 0

app.set_full_screen()
app.display()