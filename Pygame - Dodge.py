# Created with Python 3.8
# 2021

# Import libraries
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
windowHeight = 250
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

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

# Positions

gap = random.randint(0,9)
blockX = 500
x = 100
y = 100
size = 25


# Define function to show message
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

showMessage("3...", BLUE, 1.0)
showMessage("2...", BLUE, 1.0)
showMessage("1...", BLUE, 1.0)

pygame.display.set_caption("DODGE!")

# Game loop
gameRunning = True
while gameRunning:

  gameWindow.fill(WHITE)

  for event in pygame.event.get():

    # Handle quit event
    if event.type == pygame.QUIT:
      gameRunning = False

    # Detect keypresses and respond
    elif event.type == pygame.KEYDOWN:

      if event.key == pygame.K_UP:

        if y > 0:

          y -= 25
      
      elif event.key == pygame.K_DOWN:

        if y < (windowHeight-size):

          y += 25

  i = 0
  
  for i in range(10):

    if i != gap:

      pygame.draw.rect(gameWindow, RED, (blockX, i*25, 25, 25))

  blockX -= 25

  if blockX <= 0:

    blockX = 500
    gap = random.randint(0,9)
    gameSpeed += 2
  
  elif blockX == 100:

    i = 0

    for i in range(10):

      if i != gap:

        if y == i*25:

          gameRunning = False
  
  pygame.draw.rect(gameWindow, BLUE, (x,y,size,size))

  pygame.display.update()

  gameClock.tick(gameSpeed)

showMessage("Score: " + str(int(((gameSpeed-1)/2)-2)), ORANGE, 5.0)