import pygame
import os, time

pygame.init()
os.system('clear')

gameClock = pygame.time.Clock()
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Checkbox Race - RN09")

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

def showMessage(message, colour=BLACK, size=25, x=250, y=150, fill=True, update=True):
    if fill:
        gameWindow.fill(WHITE)
    font = pygame.font.SysFont("dejavusansmono", size)
    renderedText = font.render(message, True, colour)
    textArea = renderedText.get_rect()
    textArea.center = x, y
    gameWindow.blit(renderedText, textArea)
    if update:
        pygame.display.update()

gameWindow.fill(WHITE)
for _ in range(50):
    pygame.draw.rect(gameWindow, BLUE, (_ * 10 + 2, 147, 6, 6), 1)

showMessage('3...', y=100, fill=False)
time.sleep(1)
pygame.draw.rect(gameWindow, WHITE, (200, 75, 100, 50))
showMessage('2...', y=100, fill=False)
time.sleep(1)
pygame.draw.rect(gameWindow, WHITE, (200, 75, 100, 50))
showMessage('1...', y=100, fill=False)
time.sleep(1)
pygame.event.get()

start = time.time()
full_round = lambda x, n: str(round(x, n)).split('.')[0] + '.' + str(round(x, n)).split('.')[1] + ((n - len(str(round(x, n)).split('.')[1])) * '0')

times = []

checked = 0
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (145 <= y <= 155) and ((checked * 10) <= x <= (checked * 10 + 8)):
                checked += 1
                times.append(time.time() - start)
            else:
                if checked > 0:
                    checked -= 1
    showMessage('GO', y=100, update=False)
    for i in range(checked):
        pygame.draw.rect(gameWindow, BLUE, (i * 10 + 2, 147, 6, 6))
    for j in range(checked, 50):
        pygame.draw.rect(gameWindow, BLUE, (j * 10 + 2, 147, 6, 6), 1)
    showMessage(full_round(time.time() - start, 2), y=200, fill=False)
    if checked >= 50:
        break
    gameClock.tick(60)

stats = 1
while game and stats:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats = 0
    if stats == 1:
        final_time = full_round(time.time() - start, 2)
        print('Your time:', final_time + 's')
        showMessage('Completed in ' + final_time + 's', y=50, update=False)
        for n, t in enumerate(times):
            pygame.draw.circle(gameWindow, BLACK, (n*10 + 5, 300 - (t / float(final_time))*200), 2)
        pygame.draw.line(gameWindow, RED, (0, 100), (0, 300), 5)
        pygame.draw.line(gameWindow, RED, (0, 300), (500, 300), 5)
        showMessage('Time', x=20, y=110, size=15, fill=False, update=False)
        showMessage('Checked boxes', x=440, y=290, size=15, fill=False, update=False)
        pygame.display.update()
        stats = 2

pygame.quit()