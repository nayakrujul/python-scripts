from guizero import App, Text, Combo
from datetime import datetime

app = App("Time")

def set_time():

  x = datetime.now()

  time_dict = {
    "GMT-11": -11, "GMT-10": -10, "GMT-9": -9, "GMT-8": -8, "GMT-7": -7, "GMT-6": -6, "GMT-5": -5, "GMT-4": -4, "GMT-3": -3, "GMT-2": -2, "GMT-1": -1, "GMT": 0, "GMT+1": 1, "GMT+2": 2, "GMT+3": 3, "GMT+4": 4, "GMT+5": 5, "GMT+6": 6, "GMT+7": 7, "GMT+8": 8, "GMT+9": 9, "GMT+10": 10, "GMT+11": 11, "GMT+12": 12, "GMT+13": 13, "GMT+14": 14
  }

  hour = int(x.hour)

  hour += time_dict[time_zone.value]

  if hour >= 24:
    hour -= 24
  if hour < 0:
    hour += 24

  time_now.value = str.zfill(str(hour),2) + ":" + str.zfill(str(x.minute),2) + ":" + str.zfill(str(x.second),2)
  time_now.text_color = "black"

  app.display()

def please_wait():

  time_now.value = "PLEASE WAIT..."
  time_now.text_color = "orange"

Text(app, "Time now:\n\n", size=20)
time_now = Text(app, "SYNCHRONISING...", size=50, color="orange")

Text(app, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

time_zone = Combo(app, options=["GMT-11", "GMT-10", "GMT-9", "GMT-8", "GMT-7", "GMT-6", "GMT-5", "GMT-4", "GMT-3", "GMT-2", "GMT-1", "GMT", "GMT+1", "GMT+2", "GMT+3", "GMT+4", "GMT+5", "GMT+6", "GMT+7", "GMT+8", "GMT+9", "GMT+10", "GMT+11", "GMT+12", "GMT+13", "GMT+14"], selected="GMT", command=please_wait)

app.set_full_screen()

app.repeat(500, set_time)

app.display()