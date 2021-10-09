# Import libraries
import pygame, os, random, time, datetime, threading, sys

# Initialise pygame
pygame.init()

# Clear console
os.system('clear')

# Game clock
gameClock = pygame.time.Clock()
gamespeed = 5

# Setup the game window
windowWidth = 1000
windowHeight = 300
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

pygame.display.set_caption("Drag Race!")

# Define function to show message
def showMessage(message,colour,duration,y=windowHeight//2):

  # Load font
  font = pygame.font.SysFont("dejavusansmono", 25)

  # Render text
  renderedText = font.render(message, True, colour)

  # Determine where you have to put the pixels on the screen
  textArea = renderedText.get_rect()
  textArea.center = windowWidth // 2, y

  # Draw the pixels on the screen
  gameWindow.blit(renderedText, textArea)

  # Update display
  pygame.display.update()

  time.sleep(duration)

p1x = 0
p2x = 0
p1speed = 5
p2speed = 5
p1gear = 1
p2gear = 1
p1score = 0
p2score = 0

wins = []

def draw_cars(p1=True,p2=True,speed=True):

  if p1:
    pygame.draw.rect(gameWindow, BLUE, (p1x, 100, 50, 20))
    pygame.draw.circle(gameWindow, BLACK, (p1x+10,120), 5)
    pygame.draw.circle(gameWindow, BLACK, (p1x+40,120), 5)

  if p2:
    pygame.draw.rect(gameWindow, RED, (p2x, 200, 50, 20))
    pygame.draw.circle(gameWindow, BLACK, (p2x+10,220), 5)
    pygame.draw.circle(gameWindow, BLACK, (p2x+40,220), 5)

  if speed:
    showMessage(str(p1speed)+" mph. Gear "+str(p1gear),BLUE,0.0,50)
    showMessage(str(p2speed)+" mph. Gear "+str(p2gear),RED,0.0,250)

  for i in range(len(wins)):
    pygame.draw.circle(gameWindow, wins[i], (50*i+25,25), 20)

gameWindow.fill(WHITE)
draw_cars(True,False,False)
showMessage("Player 1 - use LEFT SHIFT to gear up", BLUE, 3.0)

gameWindow.fill(WHITE)
draw_cars(False,True,False)
showMessage("Player 2 - use RIGHT SHIFT to gear up", RED, 3.0)

gameWindow.fill(WHITE)
draw_cars(True,True,False)
showMessage("Time your gear up to go faster and win the race.", ORANGE, 4.0)

gameWindow.fill(WHITE)
draw_cars(True,True,False)
showMessage("Best of 3 wins.", ORANGE, 3.0)

gameWindow.fill(WHITE)
draw_cars(True,True,False)
showMessage("3...", ORANGE, 1.0)

gameWindow.fill(WHITE)
draw_cars(True,True,False)
showMessage("2...", ORANGE, 1.0)

gameWindow.fill(WHITE)
draw_cars(True,True,False)
showMessage("1...", ORANGE, 1.0)

gameWindow.fill(WHITE)

gameRunning = True
while gameRunning:

  gameWindow.fill(WHITE)

  draw_cars()

  p1x += p1speed
  p2x += p2speed

  if p1speed < p1gear * 10:
    p1speed += 1
  if p2speed < p2gear * 10:
    p2speed += 1

  for event in pygame.event.get():
    # Handle quit event
    if event.type == pygame.QUIT:
      gameRunning = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LSHIFT:
        if p1speed < (p1gear * 10 - 5):
          p1speed = (p1gear - 1) * 10
        elif p1gear < 8:
          p1gear += 1
      if event.key == pygame.K_RSHIFT:
        if p2speed < (p2gear * 10 - 5):
          p2speed = (p2gear - 1) * 10
        elif p2gear < 8:
          p2gear += 1
  
  if p1x > 950 and p1x > p2x:
    wins.append(BLUE)
    p1score += 1
    p1x = 0
    p2x = 0
    p1speed = 5
    p2speed = 5
    p1gear = 1
    p2gear = 1
    gameWindow.fill(WHITE)
    showMessage("Player 1 wins!",BLUE,3.0)
    if p1score < 2:
      gameWindow.fill(WHITE)
      draw_cars(True,True,False)
      showMessage("3...", ORANGE, 1.0)
      gameWindow.fill(WHITE)
      draw_cars(True,True,False)
      showMessage("2...", ORANGE, 1.0)
      gameWindow.fill(WHITE)
      draw_cars(True,True,False)
      showMessage("1...", ORANGE, 1.0)
  elif p2x > 950 and p2x > p1x:
    wins.append(RED)
    p2score += 1
    p1x = 0
    p2x = 0
    p1speed = 5
    p2speed = 5
    p1gear = 1
    p2gear = 1
    gameWindow.fill(WHITE)
    showMessage("Player 2 wins!",RED,3.0)
    if p2score < 2:
      gameWindow.fill(WHITE)
      draw_cars(True,True,False)
      showMessage("3...", ORANGE, 1.0)
      gameWindow.fill(WHITE)
      draw_cars(True,True,False)
      showMessage("2...", ORANGE, 1.0)
      gameWindow.fill(WHITE)
      draw_cars(True,True,False)
      showMessage("1...", ORANGE, 1.0)
  elif p1x > 950 and p2x > 950 and p1x == p2x:
    p1x = 0
    p2x = 0
    p1speed = 5
    p2speed = 5
    p1gear = 1
    p2gear = 1
    gameWindow.fill(WHITE)
    showMessage("DRAW!",ORANGE,3.0)
    gameWindow.fill(WHITE)
    draw_cars(True,True,False)
    showMessage("3...", ORANGE, 1.0)
    gameWindow.fill(WHITE)
    draw_cars(True,True,False)
    showMessage("2...", ORANGE, 1.0)
    gameWindow.fill(WHITE)
    draw_cars(True,True,False)
    showMessage("1...", ORANGE, 1.0)

  if p1score == 2 or p2score == 2:
    gameRunning = False

  pygame.display.update()

  # Tick game clock
  gameClock.tick(gamespeed)

draw_cars(False,False,False)
pygame.display.update()
time.sleep(5)