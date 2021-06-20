# Import libraries
import pygame, os, random, time, string, statistics

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

pygame.display.set_caption("Typing test!")

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

# Define function to show message
def showMessage(message, size, colour):

  # Clear game window
  gameWindow.fill(WHITE)

  # Load font
  font = pygame.font.SysFont("dejavusansmono", size)

  # Render text
  renderedText = font.render(message, True, colour)

  # Determine where you have to put the pixels on the screen
  textArea = renderedText.get_rect()
  textArea.center = windowWidth // 2, windowHeight // 2

  # Draw the pixels on the screen
  gameWindow.blit(renderedText, textArea)

  # Update display
  pygame.display.update()
  
keys = {
  "A": pygame.K_a,
  "B": pygame.K_b,
  "C": pygame.K_c,
  "D": pygame.K_d,
  "E": pygame.K_e,
  "F": pygame.K_f,
  "G": pygame.K_g,
  "H": pygame.K_h,
  "I": pygame.K_i,
  "J": pygame.K_j,
  "K": pygame.K_k,
  "L": pygame.K_l,
  "M": pygame.K_m,
  "N": pygame.K_n,
  "O": pygame.K_o,
  "P": pygame.K_p,
  "Q": pygame.K_q,
  "R": pygame.K_r,
  "S": pygame.K_s,
  "T": pygame.K_t,
  "U": pygame.K_u,
  "V": pygame.K_v,
  "W": pygame.K_w,
  "X": pygame.K_x,
  "Y": pygame.K_y,
  "Z": pygame.K_z
}
letters = string.ascii_uppercase
times = []
frames = 0
currentKey = random.choice(letters)

showMessage("3...", 25, BLUE)
time.sleep(1)

showMessage("2...", 25, BLUE)
time.sleep(1)

showMessage("1...", 25, BLUE)
time.sleep(1)

colour = BLUE

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
      
      if event.key == keys[currentKey]:

        currentKey = random.choice(letters)
        times.append((frames/gameSpeed))
        frames = 0
        colour = BLUE

      else:

        colour = RED
    
  showMessage(currentKey, 50, colour)

  frames += 1

  if len(times) == 10:
    gameRunning = False

  # Update display
  pygame.display.update()

  # Tick game clock
  gameClock.tick(gameSpeed)

average = round(statistics.mean(times)*1000)
best = round(min(times)*1000)
worst = round(max(times)*1000)

print("Average: " + str(average) + " ms.\nBest: " + str(best) + " ms.\nWorst: " + str(worst) + " ms.\n")

showMessage("Average: " + str(average) + " ms.", 25, BLUE)
time.sleep(3)
showMessage("Best: " + str(best) + " ms.", 25, GREEN)
time.sleep(3)
showMessage("Worst: " + str(worst) + " ms.", 25, ORANGE)
time.sleep(3)

