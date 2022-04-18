import pygame, os, time, statistics

pygame.init()
os.system('clear')

gameClock = pygame.time.Clock()
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Tempo tapper - RN09")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
GREY = (200, 200, 200)

def showMessage(message, colour, size=25, y=150, fill=True):

    if fill:
        gameWindow.fill(WHITE)
    
    font = pygame.font.SysFont("dejavusansmono", size)
    renderedText = font.render(message, True, colour)
    
    textArea = renderedText.get_rect()
    textArea.center = windowWidth // 2, y
    gameWindow.blit(renderedText, textArea)
    
    pygame.display.update()

def showBar(width):
    pygame.draw.rect(gameWindow, BLACK, (50, 25, 400, 20), 1)
    if width > 200:
        width = 200
    pygame.draw.rect(gameWindow, BLACK, (50, 25, width * 2, 20))

loop = True
counts = []
first = True

while loop:
    if counts == []:
        showMessage('Press any key to tap the tempo', BLUE)
    else:
        bpm = round(statistics.mean(counts), 1)
        showMessage(str(bpm) + ' BPM', BLUE)
        showBar(bpm)
    showMessage('Press ESCAPE to exit', RED, 15, 250, False)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
            elif first:
                last = time.time()
                first = False
            else:
                counts.append(60 / (time.time() - last))
                last = time.time()
    gameClock.tick(5)