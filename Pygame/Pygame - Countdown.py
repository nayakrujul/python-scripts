import pygame
import math
import os, random, string, time

pygame.init()
os.system('clear')

gameClock = pygame.time.Clock()
windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Countdown - RN09")

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

def polygon_coords(n, r, x, y):
    new_coords = []
    for i in range(n):
        new_coords.append(tuple([round(z, 2) for z in [(r * math.cos(2 * math.pi * i / n)) + x, (r * math.sin(2 * math.pi * i / n)) + y]]))
    return new_coords[3*n//4:] + new_coords[:3*n//4]

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

def contained(g, w):
    g = list(g)
    w = list(w)
    for G in g:
        if G not in w:
            return False
        w.remove(G)
    return True

def get_all_words(ltrs, wrds):
    ret = []
    for wrd in wrds:
        if contained(wrd, ltrs):
            ret.append(wrd)
    return sorted(ret, key=len, reverse=True)
    

with open('words.txt') as f:
    words = f.read().splitlines()


vowels = list('aeiou')
consonants = list('bcdfghjklmnpqrstvwxyz')
letters = []

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            loop = False
        if event.type == pygame.KEYDOWN and len(letters) < 9:
            if event.key == pygame.K_v:
                letters.append(random.choice(vowels))
            elif event.key == pygame.K_c:
                letters.append(random.choice(consonants))
    showMessage('Press "v" for a vowel', y=80)
    showMessage('Press "c" for a consonant', y=100, fill=False)
    showMessage(' '.join(letters), RED, y=175, fill=False)
    showMessage(str(9 - len(letters)) + ' left', y=250, size=15, fill=False)
    gameClock.tick(10)
    if len(letters) >= 9:
        break

clock_coords = polygon_coords(300, 50, 250, 75)
end_time = time.time() + 30

longest_guess = ''
guess = ''
keys = {eval(f'pygame.K_{l}', {'pygame': pygame}): l for l in string.ascii_lowercase}

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                guess += keys[event.key]
            elif event.key == pygame.K_RETURN:
                if guess in words and len(guess) > len(longest_guess) and contained(guess, letters):
                    longest_guess = guess
                    guess = ''
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
    showMessage(' '.join(letters), RED, y=175)
    pygame.draw.circle(gameWindow, BLACK, (250, 75), 50)
    diff = int((end_time - time.time()) * 10)
    if diff > 0:
        pygame.draw.polygon(gameWindow, WHITE, [clock_coords[300-diff], (250, 75)] + clock_coords[:300-diff])
    else:
        pygame.draw.circle(gameWindow, WHITE, (250, 75), 50)
    showMessage(longest_guess, y=225, fill=False)
    showMessage(guess, y=250, fill=False)
    gameClock.tick(10)
    if diff <= 0:
        break

showMessage('Loading', size=30, y=100)
showMessage(' '.join(letters), RED, y=175, fill=False)
showMessage(longest_guess, y=225, fill=False)
possible = get_all_words(letters, words)[:10]
show = True
while show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show = False
    showMessage('Longest possible words:', y=25, update=False)
    for i, word in enumerate(possible):
        showMessage(word, BLUE, x=(i//5)*150+175, y=(i%5)*20+50, fill=False, update=False)
    showMessage(' '.join(letters), RED, y=175, fill=False, update=False)
    showMessage(longest_guess, y=225, fill=False)
    gameClock.tick(5)
    
pygame.quit()