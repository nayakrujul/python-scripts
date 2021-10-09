from guizero import *
from datetime import datetime as dt

alarm = False
alarmCounter = 0
calc = True

def set_time():
  global alarm
  global alarmCounter

  x = dt.now()
  timeNow = str(x.hour).zfill(2) + ":" + str(x.minute).zfill(2) + ":" + str(x.second).zfill(2)
  timeText.value = timeNow

  if x.hour == hour and x.minute == minute and x.second == 0:
    alarm = True

  if alarm:
    alarmCounter += 1
    if alarmCounter % 2 == 1:
      timeText.text_color = (255,0,0)
    else:
      timeText.text_color = (0,0,0)
    left.value = ""
  else:
    timeText.text_color = (0,0,0)
    if calc:
      calc_time_left()

def key_pressed():
  global alarm
  global loop
  global calc
  alarm = False
  loop = True
  calc = False
  while loop:
    global hour
    global minute
    hour = str(input("Hour (24hr format): "))
    minute = str(input("Minute: "))
    if hour.isdigit() and minute.isdigit():
      hour = int(hour)
      minute = int(minute)
      if hour < 24 and minute < 60:
        loop = False
  alarmText.value = "Alarm set for " + str(hour) + ":" + str(minute) + "."
  calc = True

def calc_time_left():
  x = dt.now()
  hours = hour - x.hour
  if hours < 0:
    hours += 24
  mins = minute - x.minute
  if mins < 0:
    hours -= 1
    mins += 60
  secs = 60 - x.second
  if secs < 0:
    mins -= 1
    secs += 60
  if secs != 0:
    mins -= 1
  left.value = "Time left: " + str(hours).zfill(2) + ":" + str(mins).zfill(2) + ":" + str(secs).zfill(2) + "."
  

app = App()

app.set_full_screen()

timeText = Text(app, "INITIALISING...", size=50)

loop = True
while loop:
  hour = str(input("Hour (24hr format): "))
  minute = str(input("Minute: "))
  if hour.isdigit() and minute.isdigit():
    hour = int(hour)
    minute = int(minute)
    if hour < 24 and minute < 60:
      loop = False

Text(app, "\n\n\n\n\n\n\n")
alarmText = Text(app, "Alarm set for " + str(hour) + ":" + str(minute) + ".", size=30)
Text(app, "")
left = Text(app, "Time left: ", size=20)

app.repeat(1000, set_time)

app.when_key_pressed = key_pressed

app.display()