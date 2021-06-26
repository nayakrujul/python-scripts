from guizero import App, Picture

def ball(event):
  x, y = event.display_x, event.display_y
  picture.show()
  picture.resize(x,y)

app = App("Ball!", layout="grid", bg="black")

picture = Picture(app, image="ball.png", visible=True, width=50, height=50, grid=[0,0])

app.when_clicked = ball