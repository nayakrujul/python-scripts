import pygame, os, random, time, datetime

# Initialise pygame
pygame.init()

# Clear console
os.system('clear')

# Game clock
gameClock = pygame.time.Clock()
gameSpeed = 100

# Setup the game window
windowWidth = 300
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight), pygame.DOUBLEBUF, 32)

name = input("Name: ")

f = open("scores.txt", "a")

dt = datetime.datetime.now()

dateNow = str.zfill(str(dt.day),2) + "/" + str.zfill(str(dt.month),2) + "/" + str.zfill(str(dt.year),4)

if name == "devcode09":

  os.system('clear')

  password = input("Developer Code 009 - Please enter your password: ")

  confidential = open("confidential.txt", "r")

  c = confidential.read()

  os.system('clear')

  if password == str.partition(str(c), "\n")[0]:

    text = input("Please enter the text you would like to write: ")

    os.system('clear')

    f.write(dateNow + " DEVELOPER NOTICE:\n\n" + str(text) + "\n\n-------------------------\n\n")

  name = "DEVELOPER"

  confidential.close()

f.write(dateNow + " - SESSION STARTED - " + str(name) + "\n\n")

pygame.display.set_caption("Archery")

# Colours in (r,g,b) format
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
GREY = (128,128,128)

def display(x,y,s):

  # Board

  pygame.draw.ellipse(gameWindow, BLACK, (20,20,260,260))
  pygame.draw.ellipse(gameWindow, WHITE, (25,25,250,250))
  pygame.draw.ellipse(gameWindow, BLACK, (50,50,200,200))
  pygame.draw.ellipse(gameWindow, BLUE, (75,75,150,150))
  pygame.draw.ellipse(gameWindow, RED, (100,100,100,100))
  pygame.draw.ellipse(gameWindow, YELLOW, (125,125,50,50))

  # Crosshairs

  if s:
    pygame.draw.ellipse(gameWindow, BLACK, (x,y,30,30), 5)
    pygame.draw.line(gameWindow, BLACK, (x+15,y+2), (x+15,y+28),5)
    pygame.draw.line(gameWindow, BLACK, (x+2,y+15), (x+28,y+15),5)

  pygame.display.update()

def release(xPos,yPos):
  
  global total
  global fired

  if xPos >= 125 and xPos <= 175 and yPos >= 125 and yPos <= 175:
    result = "YELLOW!"
    total += 5

  elif xPos >= 100 and xPos <= 200 and yPos >= 100 and yPos <= 200:
    result = "RED!"
    total += 4

  elif xPos >= 75 and xPos <= 225 and yPos >= 75 and yPos <= 225:
    result = "BLUE!"
    total += 3
  
  elif xPos >= 50 and xPos <= 250 and yPos >= 50 and yPos <= 250:
    result = "BLACK!"
    total += 2
  
  elif xPos >= 25 and xPos <= 275 and yPos >= 25 and yPos <= 275:
    result = "WHITE!"
    total += 1

  else:
    result = "Off the board!"

  fired += 1

  print(result)
  return result


# Game loop
gameRunning = True

total = 0
fired = 0

up = False
down = False
left = False
right = False
shift = False

x = random.randint(0,300)
y = random.randint(0,300)

time_left = 100

while gameRunning:

  gameWindow.fill(WHITE)

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
      
      if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
        shift = True

      if shift:
        if event.key == pygame.K_UP:
          up = True
        elif event.key == pygame.K_DOWN:
          down = True
        elif event.key == pygame.K_LEFT:
          left = True
        elif event.key == pygame.K_RIGHT:
          right = True

      if event.key == pygame.K_x or event.key == pygame.K_BACKSPACE:
        gameRunning = False

    if event.type == pygame.KEYUP:
      
      if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and (shift):
        shift = False
        up = False
        down = False
        left = False
        right = False
        result = release(x+15,y+15)
        dt = datetime.datetime.now()
        full = str(name) + ": " + str.zfill(str(dt.day),2) + "/" + str.zfill(str(dt.month),2) + "/" + str.zfill(str(dt.year),4) + " " + str.zfill(str(dt.hour),2) + ":" + str.zfill(str(dt.minute),2) + ":" + str.zfill(str(dt.second),2) + " - " + str(result) + "\n"
        f.write(full)
        x = random.randint(0,300)
        y = random.randint(0,300)

      if event.key == pygame.K_UP:
        up = False
      elif event.key == pygame.K_DOWN:
        down = False
      elif event.key == pygame.K_LEFT:
        left = False
      elif event.key == pygame.K_RIGHT:
        right = False

  if up:
    y -= 5
  if down:
    y += 5
  if left:
    x -= 5
  if right:
    x += 5
  if shift:
    time_left -= 1
  else:
    time_left = 100
  if time_left == 0:
    result = release(x+15,y+15)
    dt = datetime.datetime.now()
    full = str(name) + ": " + str.zfill(str(dt.day),2) + "/" + str.zfill(str(dt.month),2) + "/" + str.zfill(str(dt.year),4) + " " + str.zfill(str(dt.hour),2) + ":" + str.zfill(str(dt.minute),2) + ":" + str.zfill(str(dt.second),2) + " - " + str(result) + "\n"
    f.write(full)
    shift = False
    up = False
    down = False
    left = False
    right = False
    x = random.randint(0,300)
    y = random.randint(0,300)

  display(x,y,shift)

  gameClock.tick(gameSpeed)

  pygame.display.update()

if fired > 0:

  average = total / fired

  dt = datetime.datetime.now()

  thisDict = {
    0: "OFF THE BOARD",
    1: "WHITE",
    2: "BLACK",
    3: "BLUE",
    4: "RED",
    5: "YELLOW"
  }

  dateNow = str.zfill(str(dt.day),2) + "/" + str.zfill(str(dt.month),2) + "/" + str.zfill(str(dt.year),4)

  f.write("\n" + dateNow + " - SESSION AVERAGE FOR " + str.upper(str(name)) + ": " + thisDict[int(average)] + "\n\n-------------------------\n\n")

else:

  f.write("\n" + dateNow + " - SESSION AVERAGE FOR " + str.upper(str(name)) + ": OFF THE BOARD \n\n-------------------------\n\n")

f.close()