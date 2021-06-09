import pygame, os, random, time

# Initialise pygame
pygame.init()

# Clear console
os.system('clear')

# Game clock
gameClock = pygame.time.Clock()
gameSpeed = 5

# Setup the game window
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Chrome Dino Game by Rujul.")

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

# Dinosaur

dinoX = 100
dinoY = 200
dinoYChange = 0
dinoWidth = 10
dinoHeight = 20

# Cacti

cactusX = (random.randint((windowWidth/10),((windowWidth+30)/10)))*10
cactusY = (random.randint(20,21))*10
cactusHeight = 220 - cactusY
cactusWidth = 10

cactus2X = cactusX + (random.randint(15,35)*10)
cactus2Y = (random.randint(20,21))*10
cactus2Height = 220 - cactus2Y
cactus2Width = 10

def draw():
  # Cacti
  pygame.draw.rect(gameWindow, GREEN, (cactusX, cactusY, cactusWidth, cactusHeight))
  pygame.draw.rect(gameWindow, GREEN, (cactus2X, cactus2Y, cactus2Width, cactus2Height))
  # Dino
  pygame.draw.rect(gameWindow, GREY, (dinoX, dinoY, dinoWidth, dinoHeight))
  # Ground
  pygame.draw.rect(gameWindow, BLACK, (0, 220, windowWidth, 80))

def showMessage(message,colour,duration):

  # Clear game window
  gameWindow.fill(WHITE)

  # Set Caption
  pygame.display.set_caption(message)

  # Load font
  font = pygame.font.SysFont("dejavusansmono", 25)

  # Render text
  renderedText = font.render(message, True, colour)

  # Determine where you have to put the pixels on the screen
  textArea = renderedText.get_rect()
  textArea.center = windowWidth // 2, windowHeight // 2

  # Draw the pixels on the screen
  gameWindow.blit(renderedText, textArea)

  # Update display
  pygame.display.update()

  # Pause game for duration
  time.sleep(duration)

def drawStatusBar(colour):

  # Generate text
  statusMessage = "SCORE: " + str(score) + "     "

  # os.system('clear')
  # print(statusMessage)

  # Load font
  font = pygame.font.SysFont("dejavusansmono", 15)

  # Render text
  renderedText = font.render(statusMessage, True, colour)

  # Determine where you have to put the pixels on the screen
  textArea = renderedText.get_rect()
  textArea.center = windowWidth // 2, 20

  # Draw the pixels on the screen
  gameWindow.blit(renderedText, textArea)

  # Update display
  pygame.display.update()

showMessage("3...", BLUE, 1.0)
showMessage("2...", BLUE, 1.0)
showMessage("1...", BLUE, 1.0)

# Fill game window with white
gameWindow.fill(WHITE)

score = 0
big_jumps_left = 3

pygame.display.set_caption("Chrome Dino Game")

print("Up arrow to jump. Space for big jump.")

# Game loop
gameRunning = True
while gameRunning:

  # Fill game window with white
  gameWindow.fill(WHITE)

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_UP:
        if dinoY == 200:
          dinoYChange = -10
      
      elif event.key == pygame.K_SPACE:
        if big_jumps_left > 0:
          dinoY = 150
          big_jumps_left -= 1
          os.system('clear')
          print(big_jumps_left, "free big jumps left.")
        else:
          dinoY = 150
          score -= 100
          os.system('clear')
          print("-100 points")

  dinoY += dinoYChange

  if dinoY <= 170:
    dinoYChange = 10
  elif dinoY == 200:
    dinoYChange = 0

  cactusX -= 10
  cactus2X -= 10

  if cactusX <= 0:
    cactusX = (random.randint((windowWidth/10),((windowWidth+30)/10)))*10
    cactusY = (random.randint(20,21))*10
    cactusHeight = 220 - cactusY
    gameSpeed += 1

  if cactus2X <= 0:
    cactus2X = (random.randint((windowWidth/10),((windowWidth+30)/10)))*10
    cactus2Y = (random.randint(20,21))*10
    cactus2Height = 220 - cactus2Y
    gameSpeed += 1

  draw()

  if((dinoY == cactusY or dinoY-10 == cactusY or dinoY+10 == cactusY) and (dinoX == cactusX)):
    gameRunning = False
  elif((dinoY == cactus2Y or dinoY-10 == cactus2Y or dinoY+10 == cactus2Y) and (dinoX == cactus2X)):
    gameRunning = False

  score += random.randint(1,10)

  if score % 100 < 10:
    drawStatusBar(GREEN)
  else:
    drawStatusBar(BLUE)

  # Update display
  pygame.display.update()

  gameClock.tick(gameSpeed)

showMessage("Score: " + str(score), RED, 3.0)