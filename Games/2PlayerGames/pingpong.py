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

pygame.display.set_caption("2-player Games")

# Define function to show message
def showMessage(message,colour,duration,y=windowHeight//2,fill=True,size=25,font="dejavusansmono"):

    if fill:
        gameWindow.fill(WHITE)

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

p1y = 125
p2y = 125

p1change = 0
p2change = 0

ballX = 250
ballY = 150

ballDirX = random.choice([-2,-1,1,2]) * 2
ballDirY = random.choice([-2,-1,0,1,2]) * 2

if ballDirX < 0:
    colour = BLUE
else:
    colour = RED

class game:

    running = True
    elapsed = 0.0

    class draw:

        def fill():

            gameWindow.fill(colour)

        def rect():

            if colour == BLUE:
                pygame.draw.rect(gameWindow,WHITE,(20,p1y,10,50))
                pygame.draw.rect(gameWindow,RED,(470,p2y,10,50))
            else:
                pygame.draw.rect(gameWindow,BLUE,(20,p1y,10,50))
                pygame.draw.rect(gameWindow,WHITE,(470,p2y,10,50))

        def ball():

            pygame.draw.circle(gameWindow,WHITE,(ballX,ballY),5)

        def display():

            pygame.display.update()
    
    def respond():

        global p1change
        global p2change

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    game.running = False
                    game.winner = ['Select a game', BLACK, 0]

                if event.key == pygame.K_UP:

                    p2change = -3
                
                elif event.key == pygame.K_DOWN:

                    p2change = 3
                
                elif event.key == pygame.K_w:

                    p1change = -3
                
                elif event.key == pygame.K_s:

                    p1change = 3
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:

                    p2change = 0
                
                elif event.key == pygame.K_w or event.key == pygame.K_s:

                    p1change = 0

    def update():

        global p1y
        global p2y
        global ballX
        global ballY

        p1y += p1change
        p2y += p2change

        ballX += ballDirX
        ballY += ballDirY

    def touch():

        global ballDirX
        global ballDirY
        global colour
        global gameSpeed

        if ballX <= 35 and ballX >= 30:

            if ballY > p1y and ballY < p1y + 50:

                ballDirX = random.choice([1,2]) * 2
                ballDirY = random.choice([-2,-1,0,1,2]) * 2

                colour = RED

                gameSpeed += 3

        elif ballX >= 465 and ballX <= 470:

            if ballY > p2y and ballY < p2y + 50:

                ballDirX = random.choice([-1,-2]) * 2
                ballDirY = random.choice([-2,-1,0,1,2]) * 2

                colour = BLUE

                gameSpeed += 3

    def bounce():

        global ballDirY

        if ballY <= 5:

            ballDirY = random.choice([1,2])

        if ballY >= 295:

            ballDirY = random.choice([-1,-2])

    def restrain():

        global p1y
        global p2y

        if p1y > 250:

            p1y = 250
        
        elif p1y < 0:

            p1y = 0
        
        if p2y > 250:

            p2y = 250
        
        elif p2y < 0:

            p2y = 0
    
    def over():

        if ballX <= 5:

            game.running = False

            game.winner = ["Player 2 wins!", RED, 5]
        
        elif ballX >= 495:

            game.running = False

            game.winner = ["Player 1 wins!", BLUE, 5]

    def showTime():

        game.elapsed += 1 / gameSpeed
        secs = float(round(game.elapsed, 1))

        mins = 0

        while secs >= 60:
            secs -= 60.0
            mins += 1

        secs = float(round(secs,1))
        mins = round(mins)

        showMessage(str(mins).zfill(2) + ":" + str(secs).zfill(4), WHITE, 0.0, 50, False)

    def start():

        global p1y, p2y, p1change, p2change, ballX, ballY, ballDirX, ballDirY

        showMessage("Player 1 - use WASD", BLUE, 3)
        showMessage("Player 2 - use Arrows", RED, 3)
        showMessage("3...", ORANGE, 1)
        showMessage("2...", ORANGE, 1)
        showMessage("1...", ORANGE, 1)

        p1y = 125
        p2y = 125
        
        p1change = 0
        p2change = 0
        
        ballX = 250
        ballY = 150
        
        ballDirX = random.choice([-2,-1,1,2]) * 2
        ballDirY = random.choice([-2,-1,0,1,2]) * 2

    def tick():

        gameClock.tick(gameSpeed)

def play():

    game.start()
    
    while game.running:
    
        game.respond()
    
        game.draw.fill()
    
        game.showTime()
    
        game.touch()
    
        game.restrain()
    
        game.update()
    
        game.bounce()
    
        game.draw.rect()
    
        game.draw.ball()
    
        game.draw.display()
    
        game.over()
    
        game.tick()
    
    showMessage(game.winner[0], game.winner[1], game.winner[2])

#   T T T T T T T T T T T T T T    T T T T T T T T T T T T T T    N N                       N N
#   T T T T T T T T T T T T T T    T T T T T T T T T T T T T T    N N N                     N N 
#             T T T                           T T T               N N N N                   N N
#             T T T                           T T T               N N   N N                 N N
#             T T T                           T T T               N N     N N               N N
#             T T T                           T T T               N N       N N             N N
#             T T T                           T T T               N N         N N           N N
#             T T T                           T T T               N N           N N         N N
#             T T T                           T T T               N N             N N       N N
#             T T T                           T T T               N N               N N     N N
#             T T T                           T T T               N N                 N N   N N
#             T T T                           T T T               N N                   N N N N
#             T T T                           T T T               N N                     N N N
#             T T T                           T T T               N N                       N N

# The Thonnu Games (expand the code window if you can't see the whole logo)

# Created September 2021. https://replit.com/@RN09

