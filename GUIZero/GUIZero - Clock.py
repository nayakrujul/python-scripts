from guizero import App, Drawing, Slider
import math, datetime

def polygon_coords(n, r, x, y):
    new_coords = []
    for i in range(n):
        new_coords.append([round(z, 2) for z in [(r * math.cos(2 * math.pi * i / n)) + x, (r * math.sin(2 * math.pi * i / n)) + y]])
    return new_coords

def lines(delete):
    global line_id1, line_id2, line_id3
    hour, minute, second = datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second
    if delete:
        shape.delete(line_id1)
        shape.delete(line_id2)
        shape.delete(line_id3)
    line_id1 = shape.line(250, 250, inner[int((hour + (minute / 60) * 5))][0], inner[int((hour + (minute / 60) * 5))][1], width=5)
    line_id2 = shape.line(250, 250, outer[minute - 15][0], outer[minute - 15][1], width=5)
    line_id3 = shape.line(250, 250, outer[second - 15][0], outer[second - 15][1], width=3)

def labels():
    for i in range(len(outer)):
        j = (i - 15) % 60
        if j == 0:
            j = 60
        if j % 5 == 0:
            x, y = outer[i]
            z = j // 5
            shape.text(245 + (1.1 * (250 - x)), 245 + (1.1 * (250 - y)), str(z))

app = App('Clock')

shape = Drawing(app, width=500, height=500)
outer = polygon_coords(60, 200, 250, 250)
inner = polygon_coords(60, 100, 250, 250)
shape_id = shape.polygon(outer, color='white')

lines(False)
labels()

app.repeat(1000, lines, args=[True])
app.display()