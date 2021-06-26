import pygame, os, random, time

# Initialise pygame
pygame.init()

# Clear console
os.system('clear')

# Game clock
gameClock = pygame.time.Clock()
gameSpeed = 100

# Setup the game window
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Press the keys.")

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

def drawStatusBar():

  # Generate text
  statusMessage = "PLAYER 1: " + str(p1score) + "     |     PLAYER 2: " + str(p2score)

  # os.system('clear')
  # print(statusMessage)

  # Load font
  font = pygame.font.SysFont("dejavusansmono", 15)

  # Render text
  renderedText = font.render(statusMessage, True, BLUE)

  # Determine where you have to put the pixels on the screen
  textArea = renderedText.get_rect()
  textArea.center = windowWidth // 2, 20

  # Draw the pixels on the screen
  gameWindow.blit(renderedText, textArea)

  # Update display
  pygame.display.update()

required = random.randint(20,50)

showMessage("PLAYER 1: Press RETURN.", ORANGE, 3.0)
showMessage("PLAYER 2: Press SPACE.", ORANGE, 3.0)

showMessage("Press your key " + str(required) + " times.", ORANGE, 3.0)

start = False

showMessage("3...", BLUE, 1.0)
showMessage("2...", BLUE, 1.0)
showMessage("1...", BLUE, 1.0)

# Game loop
gameRunning = True
p1score = 0
p2score = 0

while gameRunning:

  # Fill game window with white
  gameWindow.fill(WHITE)

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_RETURN:

        if start:

          p1score += 1
        
        else:

          gameRunning = False
          winner, reason = 2, "pressed before start."

      elif event.key == pygame.K_SPACE:
        
        if start:
          
          p2score += 1

        else:

          gameRunning = False
          winner, reason = 1, "pressed before start."

      if p1score >= required:

        gameRunning = False
        winner, reason = 1, ""

      elif p2score >= required:

        gameRunning = False
        winner, reason = 2, ""

  if start == False:
    start = True
  
  drawStatusBar()

  # Update display
  pygame.display.update()

  gameClock.tick(gameSpeed)

if reason != "":
  this_dict = {1:2, 2:1}

  print("Player", this_dict[winner], reason)

showMessage("Player " + str(winner) + " wins!", GREEN, 5.0)