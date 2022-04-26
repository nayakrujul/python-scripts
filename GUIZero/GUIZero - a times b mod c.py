import math
from guizero import App, Drawing, Slider, Text

def line_length(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

def text(n, r, x, y):
    ids = []
    for i in range(n):
        ids.append(shape.text((r * math.cos(2 * math.pi * i / n)) * (1 + (n / 200)) + x, (r * math.sin(2 * math.pi * i / n)) * (1 + (n / 200)) + y, str(i)))
    return ids

def polygon_coords(n, r, x, y):
    new_coords = []
    for i in range(n):
        new_coords.append([round(z, 2) for z in [(r * math.cos(2 * math.pi * i / n)) + x, (r * math.sin(2 * math.pi * i / n)) + y]])
    return new_coords

def decide_colour(x1, y1, x2, y2):
    length = line_length(x1, y1, x2, y2)
    if length < 75:
        return 'purple'
    elif length < 150:
        return 'blue'
    elif length < 225:
        return 'green'
    elif length < 300:
        return 'yellow'
    elif length < 375:
        return 'orange'
    else:
        return 'red'

def lines():
    ids = []
    c = sides.value
    b = mult.value
    for a in range(sides.value):
        x1, y1 = coords[(a * b) % c]
        x2, y2 = coords[a]
        colour = decide_colour(x1, y1, x2, y2)
        ids.append(shape.line(x1, y1, x2, y2, colour))
    return ids

def change_sides():
    global shape_id, coords, line_ids, text_ids
    shape.delete(shape_id)
    coords = polygon_coords(sides.value, 200, 325, 325)
    shape_id = shape.polygon(coords, color='white')
    [shape.delete(id) for id in line_ids + text_ids]
    line_ids = lines()
    text_ids = text(sides.value, 200, 325, 325)

app = App('a * b MOD c')

shape = Drawing(app, width=650, height=650)

coords = polygon_coords(10, 200, 325, 325)
shape_id = shape.polygon(coords, color='white')
text_ids = text(10, 200, 325, 325)

Text(app, 'Number of sides:')
sides = Slider(app, 4, 100, width=200, command=change_sides)
sides.value = 10

Text(app, 'Multiple:')
mult = Slider(app, 2, 10, command=change_sides)

line_ids = lines()

app.set_full_screen()
app.display()