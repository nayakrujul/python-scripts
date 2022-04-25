import math
from guizero import App, Drawing, Slider, Text

def line_length(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

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
    a = sides.value
    b = mult.value
    for c in range(sides.value):
        x1, y1 = coords[(b * c) % a]
        x2, y2 = coords[c]
        colour = decide_colour(x1, y1, x2, y2)
        ids.append(shape.line(x1, y1, x2, y2, colour))
    return ids

def change_sides():
    global shape_id, coords, line_ids
    shape.delete(shape_id)
    coords = polygon_coords(sides.value, 200, 250, 200)
    shape_id = shape.polygon(coords, color='white')
    [shape.delete(id) for id in line_ids]
    line_ids = lines()

app = App('Mandelbrot Set - (a * b) MOD c')

Text(app, 'The Mandelbrot Set\n', size=20)

shape = Drawing(app, width=500, height=500)

coords = polygon_coords(10, 200, 250, 200)
shape_id = shape.polygon(coords, color='white')

Text(app, 'Number of sides:')
sides = Slider(app, 4, 100, width=200, command=change_sides)
sides.value = 10

Text(app, '\n')

Text(app, 'Multiple:')
mult = Slider(app, 2, 10, command=change_sides)

line_ids = lines()

app.set_full_screen()
app.display()