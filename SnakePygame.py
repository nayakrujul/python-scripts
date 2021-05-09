# Snake game by RN09 (repl.it/@RN09) | nayakrujul (github.com/nayakrujul)

# Created with Python 3.8
# March 2021

# Import libraries
import pygame, os, random, time, datetime #, threading

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

pygame.display.set_caption("Snake! by Rujul.")

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

# Size and positions

# Snake
snakeBlockSize = 10
snakeHeadX = windowWidth // 2
snakeHeadY = windowHeight // 2
snakeChangeX = snakeBlockSize
snakeChangeY = 0

# Define the list for each of the snake's rectangle body parts' positions
snakeList = []
snakeLength = 1

# Fruit
appleX = (random.randint(10, windowWidth - (2*snakeBlockSize)) // snakeBlockSize) * snakeBlockSize
appleY = (random.randint(30, windowHeight - (2*snakeBlockSize)) // snakeBlockSize) * snakeBlockSize

# Set score
score = 0

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

def drawSnake():

  for snakeBodySegment in snakeList:
    snakeBodySegmentX, snakeBodySegmentY = snakeBodySegment

    pygame.draw.rect(gameWindow, GREEN, (snakeBodySegmentX, snakeBodySegmentY, snakeBlockSize, snakeBlockSize))

def drawStatusBar():

  # Generate text
  statusMessage = "SCORE: " + str(score) + "     "
  statusMessage += "APPLES EATEN: " + str((snakeLength - 1)) + "     "
  statusMessage += "SPEED: " + str((round(gameSpeed,1)))

  # os.system('clear')
  # print(statusMessage)

  # Load font
  font = pygame.font.SysFont("dejavusansmono", 15)

  # Render text
  renderedText = font.render(statusMessage, True, BLUE)

  # Determine where you have to put the pixels on the screen
  textArea = renderedText.get_rect()
  textArea.center = windowWidth // 2, 20

  # Draw background
  pygame.draw.rect(gameWindow, YELLOW, ((windowWidth-textArea.width)/2, 8, textArea.width, textArea.height + 5))

  # Draw the pixels on the screen
  gameWindow.blit(renderedText, textArea)

  # Update display
  pygame.display.update()

# def threadClear():
  # time.sleep(3)
  # os.system('clear')
  # myThread.terminate()
# myThread = threading.Thread(target=threadClear)

# Fill game window with white
gameWindow.fill(WHITE)

showMessage("Snake! by Rujul.", GREEN, 2.0)
showMessage("3...", BLUE, 1.0)
showMessage("2...", BLUE, 1.0)
showMessage("1...", BLUE, 1.0)

# Update game info
os.system('clear')
# print("Game speed (refresh rate):", gameSpeed, "times per second. \nScore:", score, "\nSnake length:", (score+1), "blocks.")

# Set caption
pygame.display.set_caption("Score: " + str(score))

# Game loop
gameRunning = True
while gameRunning:

  for event in pygame.event.get():

    # Handle quit event
    if event.type == pygame.QUIT:
      gameRunning = False
      deathMsg = 'ended game.'

    # Detect keypresses and respond
    elif event.type == pygame.KEYDOWN:

      if event.key == pygame.K_UP:
        snakeChangeX = 0
        snakeChangeY = -snakeBlockSize

      elif event.key == pygame.K_DOWN:
        snakeChangeX = 0
        snakeChangeY = snakeBlockSize

      elif event.key == pygame.K_LEFT:
        snakeChangeX = -snakeBlockSize
        snakeChangeY = 0

      elif event.key == pygame.K_RIGHT:
        snakeChangeX = snakeBlockSize
        snakeChangeY = 0

      # elif event.key == pygame.K_o:
        # if gameSpeed > 3:
          # gameSpeed -= 1

      # elif event.key == pygame.K_p:
        # gameSpeed += 1
        
      # elif event.key == pygame.K_r:
        # gameSpeed = 5

      elif event.key == pygame.K_SPACE:
        # os.system('clear')
        input("Press enter to restart.")
        os.system('clear')
        showMessage("3...", BLUE, 1.0)
        showMessage("2...", BLUE, 1.0)
        showMessage("1...", BLUE, 1.0)

  # Update Snake Position
  snakeHeadX += snakeChangeX
  snakeHeadY += snakeChangeY

  # Detect if the snake touches the left or right edge
  if snakeHeadX <= 0 or snakeHeadX >= windowWidth - snakeBlockSize:
    gameRunning = False
    deathMsg = 'hit the edge!'

  # Detect if the snake touches the top or bottom edge
  elif snakeHeadY <= 0 or snakeHeadY >= windowHeight - snakeBlockSize:
    gameRunning = False
    deathMsg = 'hit the edge!'

  # Detect if snake touches own body
  alreadyInSnakeList = []
  for snakeBodySegment in snakeList:
    if snakeBodySegment in alreadyInSnakeList:
      gameRunning = False
      deathMsg = 'hit yourself!'
    alreadyInSnakeList.append(snakeBodySegment)

  # Update snakeList
  if len(snakeList) > snakeLength:
    del snakeList[0]

  # Detect if snake touches fruit
  if snakeHeadX == appleX and snakeHeadY == appleY:

    snakeLength += 1

    appleX = (random.randint(10, windowWidth - (2*snakeBlockSize)) // snakeBlockSize) * snakeBlockSize
    appleY = (random.randint(30, windowHeight - (2*snakeBlockSize)) // snakeBlockSize) * snakeBlockSize

    score += (random.randint(10,100)*5)

    # os.system('clear')
    # print("Apple collected. Score:", score)
    # myThread.start()

    gameSpeed += round(((random.randint(5,15))/10),1)

    # Set caption
    pygame.display.set_caption("Score: " + str(score))

    # Update game info
    # os.system('clear')
    # print("Game speed (refresh rate):", round(gameSpeed, 1), "times per second. \nScore:", score, "\nSnake length:", (snakeLength), "blocks.")

  # Add new snake position to snakeList
  snakeList.append((snakeHeadX, snakeHeadY))

  # Maintain the length of snakeList to match the snakeLength
  if len(snakeList) > snakeLength:
    del snakeList[0]

  # Fill window
  gameWindow.fill(WHITE)

  # Draw new snake/fruit
  # pygame.draw.rect(gameWindow, GREEN, (snakeHeadX, snakeHeadY, snakeBlockSize, snakeBlockSize))
  drawSnake()
  pygame.draw.rect(gameWindow, RED, (appleX, appleY, snakeBlockSize, snakeBlockSize))

  # Draw status bar
  drawStatusBar()

  # Update display
  pygame.display.update()

  # Tick game clock
  gameClock.tick(gameSpeed)

showMessage("You " + deathMsg + " Game over.", RED, 2.0)

with open("scores.txt", "a") as f:
  x = datetime.datetime.now()
  full = str.zfill(str(x.day),2) + "/" + str.zfill(str(x.month),2) + "/" + str.zfill(str(x.year),4) + " " + str.zfill(str(x.hour),2) + ":" + str.zfill(str(x.minute),2) + ":" + str.zfill(str(x.second),2) + " - " + str.zfill(str(score),6) + "\n"
  f.write(full)

print("Your score was", str(score) + "!")
if score <= 1000:
  showMessage("Your score was " + str(score) + ".", RED, 2.0)
elif score <= 2000:
  showMessage("Your score was " + str(score) + ".", ORANGE, 2.0)
else:
  showMessage("Your score was " + str(score) + ".", GREEN, 2.0)
showMessage("Thanks for playing.", BLUE, 3.0)