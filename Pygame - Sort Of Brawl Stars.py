# You are currently running Version 2 of "Sort Of Brawl Stars"
# Last updated 2nd September 2021
# New in this update:
# You can now shoot while standing still

# Import libraries
import pygame, os, random, time, datetime, threading, sys

# Initialise pygame
pygame.init()

# Clear console
os.system('clear')

# Game clock
gameClock = pygame.time.Clock()
gameSpeed = 30

# Setup the game window
windowWidth = 500
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

pygame.display.set_caption("Brawl Stars!")

# Define function to show message
def showMessage(message,colour,duration,y=windowHeight//2,size=25,font="dejavusansmono"):

  # Load font
  font = pygame.font.SysFont(font, size)

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

p1x = 400
p1y = 150
p1xchange = 0
p1ychange = 0
p1ammo = 0
p1bullet = [-10,-10,-1,0]
p1noAmmo = False

p2x = 100
p2y = 150
p2xchange = 0
p2ychange = 0
p2ammo = 0
p2bullet = [-10,-10,1,0]
p2noAmmo = False

def update():
  
  pygame.draw.circle(gameWindow, BLUE, (p1x,p1y), 10)
  pygame.draw.circle(gameWindow, RED, (p2x,p2y), 10)
  pygame.draw.circle(gameWindow, BLUE, (p1bullet[0],p1bullet[1]), 5)
  pygame.draw.circle(gameWindow, RED, (p2bullet[0],p2bullet[1]), 5)

gameWindow.fill(BLACK)

showMessage("THE",WHITE,0.0,windowHeight//2-60,70,"comicsansms")
showMessage("THO",WHITE,0.0,windowHeight//2,70,"comicsansms")
showMessage("NNU",WHITE,3.0,windowHeight//2+60,70,"comicsansms")
gameWindow.fill(WHITE)

image = pygame.image.load('cake.jpg')
imgArea = image.get_rect()
imgArea.center = windowWidth // 2, windowHeight // 2
gameWindow.blit(image, imgArea)
showMessage("5",WHITE,3.0,windowHeight//2+50,70)
gameWindow.fill(WHITE)

showMessage("In association with",BLACK,0.0,windowHeight//2-50,15)
showMessage("RN09 Studios",BLUE,3.0,windowHeight//2,40)
gameWindow.fill(WHITE)

showMessage("And",BLACK,0.0,windowHeight//2-50,15)
showMessage("Not A Rip Off Games",RED,3.0)
gameWindow.fill(WHITE)

showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.5,windowHeight//2,40)
pygame.draw.rect(gameWindow,RED,(200,280,20,10),5)
showMessage("20%",BLACK,0.5,windowHeight-50,20)
gameWindow.fill(WHITE)

pygame.draw.rect(gameWindow,RED,(200,280,20,10),5)
showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.0,windowHeight//2,40)
showMessage("Connecting to server...",BLACK,1.5,windowHeight-50,20)
gameWindow.fill(WHITE)

pygame.draw.rect(gameWindow,RED,(200,280,50,10),5)
showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.0,windowHeight//2,40)
showMessage("50%",BLACK,1.0,windowHeight-50,20)
gameWindow.fill(WHITE)

pygame.draw.rect(gameWindow,RED,(200,280,50,10),5)
showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.0,windowHeight//2,40)
showMessage("Downloading content...",BLACK,2.5,windowHeight-50,20)
gameWindow.fill(WHITE)

pygame.draw.rect(gameWindow,RED,(200,280,84,10),5)
showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.0,windowHeight//2,40)
showMessage("84%",BLACK,0.5,windowHeight-50,20)
gameWindow.fill(WHITE)

pygame.draw.rect(gameWindow,RED,(200,280,92,10),5)
showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.0,windowHeight//2,40)
showMessage("92%",BLACK,1.5,windowHeight-50,20)
gameWindow.fill(WHITE)

pygame.draw.rect(gameWindow,RED,(200,280,100,10),5)
showMessage("BRAWL",RED,0.0,windowHeight//2-30)
showMessage("STARS",BLUE,0.0,windowHeight//2,40)
showMessage("100%",BLACK,0.2,windowHeight-50,20)
gameWindow.fill(WHITE)

showMessage("Instructions:",ORANGE,2.0)
gameWindow.fill(WHITE)

showMessage("Player 1 - use arrow keys to move",BLUE,3.0)
gameWindow.fill(WHITE)

showMessage("Player 2 - use WASD keys to move",RED,3.0)
gameWindow.fill(WHITE)

showMessage("Player 1",BLUE,0.0,windowHeight//2-50)
showMessage("use SHIFT or CTRL to shoot",BLUE,3.0,windowHeight//2+50)
gameWindow.fill(WHITE)

showMessage("Player 2",RED,0.0,windowHeight//2-50)
showMessage("use Z or X to shoot",RED,3.0,windowHeight//2+50)
gameWindow.fill(WHITE)

showMessage("Shoot your opponent to win.",ORANGE,3.0)
gameWindow.fill(WHITE)

showMessage("3...", BLUE, 1.0)
gameWindow.fill(WHITE)

showMessage("2...", BLUE, 1.0)
gameWindow.fill(WHITE)

showMessage("1...", BLUE, 1.0)
gameWindow.fill(WHITE)

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
        p1xchange = 0
        p1ychange = -1
        if p1bullet[0] <= -10 or p1bullet[1] <= -10:
          p1bullet[2] = 0
          p1bullet[3] = -1

      elif event.key == pygame.K_DOWN:
        p1xchange = 0
        p1ychange = 1
        if p1bullet[0] <= -10 or p1bullet[1] <= -10:
          p1bullet[2] = 0
          p1bullet[3] = 1

      elif event.key == pygame.K_LEFT:
        p1xchange = -1
        p1ychange = 0
        if p1bullet[0] <= -10 or p1bullet[1] <= -10:
          p1bullet[2] = -1
          p1bullet[3] = 0

      elif event.key == pygame.K_RIGHT:
        p1xchange = 1
        p1ychange = 0
        if p1bullet[0] <= -10 or p1bullet[1] <= -10:
          p1bullet[2] = 1
          p1bullet[3] = 0
      
      elif event.key == pygame.K_w:
        p2xchange = 0
        p2ychange = -1
        if p2bullet[0] <= -10 or p2bullet[1] <= -10:
          p2bullet[2] = 0
          p2bullet[3] = -1

      elif event.key == pygame.K_s:
        p2xchange = 0
        p2ychange = 1
        if p2bullet[0] <= -10 or p2bullet[1] <= -10:
          p2bullet[2] = 0
          p2bullet[3] = 1

      elif event.key == pygame.K_a:
        p2xchange = -1
        p2ychange = 0
        if p2bullet[0] <= -10 or p2bullet[1] <= -10:
          p2bullet[2] = -1
          p2bullet[3] = 0

      elif event.key == pygame.K_d:
        p2xchange = 1
        p2ychange = 0
        if p2bullet[0] <= -10 or p2bullet[1] <= -10:
          p2bullet[2] = 1
          p2bullet[3] = 0
      
      elif event.key == pygame.K_RCTRL or event.key == pygame.K_RSHIFT:
        if p1ammo == 0:
          p1ammo = 50
          p1bullet[0] = p1x
          p1bullet[1] = p1y
        else:
          p1noAmmo = True
      
      elif event.key == pygame.K_z or event.key == pygame.K_x:
        if p2ammo == 0:
          p2ammo = 50
          p2bullet[0] = p2x
          p2bullet[1] = p2y
        else:
          p2noAmmo = True
    
    elif event.type == pygame.KEYUP:

      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        p1ychange = 0

      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        p1xchange = 0
      
      elif event.key == pygame.K_w or event.key == pygame.K_s:
        p2ychange = 0
      
      elif event.key == pygame.K_a or event.key == pygame.K_d:
        p2xchange = 0
  
  if p1noAmmo:
    showMessage("No Ammo!", BLUE, 0.0, 50)
  if p1ammo == 0:
    p1noAmmo = False
  if p2noAmmo:
    showMessage("No Ammo!", RED, 0.0, 250)
  if p2ammo == 0:
    p2noAmmo = False

  p1x += p1xchange
  p1y += p1ychange
  p2x += p2xchange
  p2y += p2ychange

  if p1x > 490:
    p1x = 490
  if p1x < 10:
    p1x = 10
  if p1y > 290:
    p1y = 290
  if p1y < 10:
    p1y = 10
  
  if p2x > 490:
    p2x = 490
  if p2x < 10:
    p2x = 10
  if p2y > 290:
    p2y = 290
  if p2y < 10:
    p2y = 10

  if p1ammo > 0:
    p1ammo -= 1
  if p2ammo > 0:
    p2ammo -= 1
  
  if p1bullet[0] > -10:
    p1bullet[0] += (p1bullet[2]*5)
    p1bullet[1] += (p1bullet[3]*5)
  if p2bullet[0] > -10:
    p2bullet[0] += (p2bullet[2]*5)
    p2bullet[1] += (p2bullet[3]*5)

  update()

  if p1bullet[0] - p2x < 10 and p1bullet[0] - p2x > -10 and p1bullet[1] - p2y < 10 and p1bullet[1] - p2y > -10:
    gameRunning = False
    showMessage("PLAYER 1 WINS!!!", BLUE, 5.0)
  elif p2bullet[0] - p1x < 10 and p2bullet[0] - p1x > -10 and p2bullet[1] - p1y < 10 and p2bullet[1] - p1y > -10:
    gameRunning = False
    showMessage("PLAYER 2 WINS!!!", RED, 5.0)

  pygame.display.update()

  gameClock.tick(gameSpeed)

gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 11 - 176 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 11 - 177 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 11 - 178 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 11 - 179 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("LEVEL UP - RANK 12", BLUE,  0.5)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 180 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 181 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 182 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 183 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 184 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 185 trophies", BLUE,  0.2)
gameWindow.fill(WHITE)

showMessage("RANK 1!", GREEN, 0.0, 50, 30)
showMessage("+10",GREEN, 0.0, 75, 15)
showMessage("RANK 12 - 186 trophies", BLUE,  2)
gameWindow.fill(WHITE)