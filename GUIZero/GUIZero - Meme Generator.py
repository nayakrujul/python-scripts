from guizero import App, TextBox, Drawing, Combo, Text, Slider
import os

def draw_meme():
  os.system('clear')
  meme.clear()
  meme.image(0, 0, "woodpecker.jfif", width=300, height=300)
  meme.text(
  20, 20, top_text.value,
  color=top_color.value,
  size=int(top_size.value),
  font="courier")
  meme.text(
  20, 250, bottom_text.value,
  color=bottom_color.value,
  size=int(bottom_size.value),
  font="times new roman",
  )

app = App("Meme Generator")

top_text = TextBox(app, "Top text", command=draw_meme)
top_color = Combo(app,
  options=["black", "white", "red", "green", "blue", "orange"],
  command=draw_meme,
  selected="orange")
top_size = Slider(app, start=20, end=40, command=draw_meme)

Text(app, text="")

bottom_text = TextBox(app, "Bottom text", command=draw_meme)
bottom_color = Combo(app,
  options=["black", "white", "red", "green", "blue", "orange"],
  command=draw_meme,
  selected="blue")
bottom_size = Slider(app, start=20, end=40, command=draw_meme)

Text(app, text="")

meme = Drawing(app, width="fill", height="fill")
draw_meme()
app.display()

