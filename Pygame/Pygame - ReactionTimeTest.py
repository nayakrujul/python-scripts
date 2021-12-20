import pygame, time, os, random

pygame.init()

os.system('clear')

# Game clock
gameClock = pygame.time.Clock()

# Setup the game window
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Test your reaction time!")

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
  font = pygame.font.SysFont("dejavusansmono", 15)

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

showMessage("Test your reaction time!", BLUE, 3.0)
showMessage("When the screen goes green, press any key.", BLUE, 5.0)

# Game loop
gameRunning = True
colour = RED
frames = 0
start = random.randint(20,100)
timeElapsed = 0.0

while gameRunning:

  gameWindow.fill(colour)

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if colour == GREEN:
        gameRunning = False

      else:
        print("Screen hasn't gone green yet...")
        frames = 0

  if colour == GREEN:
    timeElapsed += 0.05

  frames += 1
  if frames == start:
    colour = GREEN

  # Update display
  pygame.display.update()

  gameClock.tick(20)

os.system("clear")
print(round(timeElapsed,2), "seconds")
showMessage(str((round(timeElapsed,2))) + " seconds", BLUE, 3.0)