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

pygame.display.set_caption("Flappy bird Game by Rujul.")

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

def showMessage(message,colour,duration):

  # Clear game window
  gameWindow.fill(WHITE)

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

# Bird

birdX = 100
birdY = 150
birdWidth = 10
birdHeight = 10

# Poles

pole1X = random.randint(50, 60) * 10
pole1Y = 0
pole1Width = 20
pole1Height = random.randint(5, 15) * 10

pole2X = pole1X
pole2Y = pole1Height + 100
pole2Width = 20
pole2Height = windowHeight - pole2Y

showMessage("3...", BLUE, 1.0)
showMessage("2...", BLUE, 1.0)
showMessage("1...", BLUE, 1.0)

# Game loop
gameRunning = True
down = False
score = 0

while gameRunning:

  # Fill game window with white
  gameWindow.fill(WHITE)

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_UP:
        down = True
    
    elif event.type == pygame.KEYUP:

      if event.key == pygame.K_UP:
        down = False
  if down:
    birdY -= 10
  else:
    birdY += 10

  pole1X -= 10
  pole2X -= 10

  pygame.draw.rect(gameWindow, RED, (birdX, birdY, birdWidth, birdHeight))
  pygame.draw.rect(gameWindow, GREEN, (pole1X, pole1Y, pole1Width, pole1Height))
  pygame.draw.rect(gameWindow, GREEN, (pole2X, pole2Y, pole2Width, pole2Height))

  if birdY < 0 or birdY >= windowHeight:
    gameRunning = False

  if birdX == pole1X:
    if birdY < pole1Height or birdY >= pole2Y:
      gameRunning = False
    else:
      gameSpeed += 1

  if pole1X < 0:
    pole1X = random.randint(50, 60) * 10
    pole1Y = 0
    pole1Width = 20
    pole1Height = random.randint(5, 15) * 10

    pole2X = pole1X
    pole2Y = pole1Height + 100
    pole2Width = 20
    pole2Height = windowHeight - pole2Y

  score += 1

  if score % 100 < gameSpeed:
    drawStatusBar(GREEN)
  else:
    drawStatusBar(BLUE)

  # Update display
  pygame.display.update()

  gameClock.tick(gameSpeed)