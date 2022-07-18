import pygame
import os, time

pygame.init()
os.system('clear')

gameClock = pygame.time.Clock()
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("CPS Test 2 - RN09")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
GREY = (200,200,200)

'''
The position argument of the showMessage function must be one of:

['TL', 'TC', 'TR',
 'CL', 'CC', 'CR',
 'BL', 'BC', 'BR']
(case insensitive)

This shows the position of the x and y coordinates given relative to the text
('TL' = top-left corner of text, 'BC' = bottom-centre of text, etc.)

It defaults to 'CC' (centre)
'''

def showMessage(message, colour=BLACK, size=25, x=250, y=150, position='CC', fill=False, update=False):
    if fill:
        gameWindow.fill(WHITE)
    font = pygame.font.SysFont("dejavusansmono", size)
    renderedText = font.render(message, True, colour)
    textArea = renderedText.get_rect()
    if len(position) != 2:
        position = 'CC'
    posy, posx = position.upper()
    if posx == 'L':
        x += textArea.width // 2
    elif posx == 'R':
        x -= textArea.width // 2
    if posy == 'T':
        y += textArea.height // 2
    elif posy == 'B':
        y -= textArea.height // 2
    textArea.center = x, y
    gameWindow.blit(renderedText, textArea)
    if update:
        pygame.display.update()

clicks = []
game = True
high_1 = 0
high_5 = 0
high_10 = 0
while game:
    time_now = round(time.time(), 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks.insert(0, time_now)
    num_1 = 0
    num_5 = 0
    num_10 = 0
    for t in clicks:
        if (time_now - t) > 10:
            break
        num_10 += 1
        if (time_now - t) <= 5:
            num_5 += 1
            if (time_now - t) <= 1:
                num_1 += 1
    if num_1 > high_1:
        high_1 = num_1
    if num_5 > high_5:
        high_5 = num_5
    if num_10 > high_10:
        high_10 = num_10
    gameWindow.fill(WHITE)
    pygame.draw.rect(gameWindow, BLACK, (40, 15, 120, 60), 5)
    showMessage(str(num_1), size=30, x=100, y=50, position='BC')
    showMessage('clicks in 1s', size=15, x=100, y=50, position='TC')
    pygame.draw.rect(gameWindow, BLACK, (340, 15, 120, 60), 5)
    showMessage(str(high_1), size=30, x=400, y=50, position='BC')
    showMessage('highest 1s', size=15, x=400, y=50, position='TC')
    showMessage(str(num_5) + ' clicks in 5s', size=20, x=100, y=125)
    showMessage(str(high_5) + ' highest 5s', size=20, x=400, y=125)
    showMessage(str(num_10) + ' clicks in 10s', size=20, x=100, y=160)
    showMessage(str(high_10) + ' highest 10s', size=20, x=400, y=160)
    if high_1 >= 10:
        pygame.draw.rect(gameWindow, GREEN, (0, 200, 125, 100))
    else:
        pygame.draw.rect(gameWindow, GREEN, (0, 200, 12.5*num_1, 100))
    if high_5 >= 35:
        pygame.draw.rect(gameWindow, GREEN, (125, 200, 125, 100))
    else:
        pygame.draw.rect(gameWindow, GREEN, (125, 200, (25/7)*num_5, 100))
    if high_10 >= 60:
        pygame.draw.rect(gameWindow, GREEN, (250, 200, 125, 100))
    else:
        pygame.draw.rect(gameWindow, GREEN, (250, 200, (25/12)*num_10, 100))
    if len(clicks) >= 250:
        pygame.draw.rect(gameWindow, GREEN, (375, 200, 125, 100))
    else:
        pygame.draw.rect(gameWindow, GREEN, (375, 200, 0.5*len(clicks), 100))
    pygame.draw.line(gameWindow, BLACK, (0, 200), (500, 200), 5)
    for i in range(1, 4):
        pygame.draw.line(gameWindow, BLACK, (i*125, 200), (i*125, 300), 5)
    showMessage('10 clicks in 1s', size=12, x=62.5, y=250)
    showMessage('35 clicks in 5s', size=12, x=187.5, y=250)
    showMessage('60 clicks in 10s', size=12, x=312.5, y=250)
    showMessage('Total 250 clicks', size=12, x=437.5, y=250)
    pygame.display.update()
    gameClock.tick(30)