import pygame, os, sys, math, cmath, random


pygame.init()
os.system('clear')

gameClock = pygame.time.Clock()
windowWidth = 500
windowHeight = 500
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Equation Grapher - RN09")

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


colour = RED


def sin(x):
  return cmath.sin(math.radians(x)).real
def cos(x):
  return cmath.cos(math.radians(x)).real
def tan(x):
  return cmath.tan(math.radians(x)).real
def arcsin(x):
  return math.degrees(cmath.asin(x).real)
def arccos(x):
  return math.degrees(cmath.acos(x).real)
def arctan(x):
  return math.degrees(cmath.atan(x).real)


def showMessage(message, colour=BLACK, size=15, x=250, y=250, fill=True):

    if fill:
        gameWindow.fill(WHITE)
    
    font = pygame.font.SysFont("dejavusansmono", size)
    rendecolourText = font.render(message, True, colour)
    
    textArea = rendecolourText.get_rect()
    textArea.center = x, y
    gameWindow.blit(rendecolourText, textArea)


def get_coords(eq, lst):
    # To protect against something like '__import__("shutil").rmtree("/")'
    if 'import' in eq:
        sys.exit("Don't even try.")
    ret = []
    for xval in lst:
        try:
            ret.append(round(eval(
                eq.replace('^', '**'),
                {
                    'x': xval,
                    'sin': sin, 'cos': cos, 'tan': tan,
                    'arcsin': arcsin, 'arccos': arccos, 'arctan': arctan,
                    'sqrt': math.sqrt, 'ceil': math.ceil, 'floor': math.floor
                }
            ), 2))
        except Exception as e:
            sys.exit("Couldn't understand this: " + str(e))
    return ret


def get_scale(lst):
    _min, _max = math.floor(min(lst)), math.ceil(max(lst))
    if _min == _max:
        _min -= 1
        _max += 1
    diff = _max - _min
    return (500 / diff, _min, _max)


def get_pos(xval, xscale, minx, yval, yscale, miny):
    xpos = (xval - minx) * xscale
    ypos = 500 - ((yval - miny) * yscale)
    return (xpos, ypos)


showMessage('Enter the equation below', size=30)
pygame.display.update()


print('Enter an equation, e.g. y = 2*x^2 + 5*x + 1')
print('                                           ')
print('You can use any of the following functions:')
print('sin, cos, tan, arcsin, arccos, arctan, abs,')
print('round, ceil, floor, sqrt                   ')
print('                                           ')

equation = input('y = ')

x = [i / 10 for i in range(-100, 101)]
y = get_coords(equation, x)

sx, mx, _mx = get_scale(x)
sy, my, _my = get_scale(y)

print('                                 ')
print('Keyboard shortcuts:              ')
print('Hold [s] to make the scale square')
print('Hold [d] for disco mode          ')
print('Press [l] to toggle line labels  ')
print('Press [k] to show/hide lines     ')


loop = 1
disco = False
labels = True
lines = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                sy = sx
                loop = 1
            if event.key == pygame.K_d:
                disco = True
            if event.key == pygame.K_l:
                labels = not labels
                loop = 1
            if event.key == pygame.K_k:
                lines = not lines
                loop = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                sy = get_scale(y)[0]
                loop = 1
            if event.key == pygame.K_d:
                disco = False
                colour = RED
                loop = 1
    if loop == 1:
        gameWindow.fill(WHITE)
        pygame.draw.line(
            gameWindow, BLACK,
            (0, get_pos(0, sx, mx, 0, sy, my)[1]),
            (500, get_pos(0, sx, mx, 0, sy, my)[1]),
            10
        )
        pygame.draw.line(
            gameWindow, BLACK,
            (get_pos(0, sx, mx, 0, sy, my)[0], 0),
            (get_pos(0, sx, mx, 0, sy, my)[0], 500),
            10
        )
        for xline in range(-10, 11):
            if lines:
                pygame.draw.line(
                    gameWindow, BLACK,
                    (get_pos(xline, sx, mx, 0, sy, my)[0], 0),
                    (get_pos(xline, sx, mx, 0, sy, my)[0], 500),
                    2
                )
            if labels:
                showMessage(
                    str(xline),
                    x=get_pos(xline, sx, mx, 0, sy, my)[0],
                    y=get_pos(0, sx, mx, 0, sy, my)[1] + 20,
                    fill=False
                )
        try:
            for yline in range(my, _my + 1, (_my - my) // 20):
                if lines:
                    pygame.draw.line(
                        gameWindow, BLACK,
                        (0, get_pos(0, sx, mx, yline, sy, my)[1]),
                        (500, get_pos(0, sx, mx, yline, sy, my)[1]),
                        2
                    )
                if labels:
                    showMessage(
                        str(yline),
                        x=270,
                        y=get_pos(0, sx, mx, yline, sy, my)[1],
                        fill=False
                    )
        except: pass
        for X, Y in zip(x, y):
            pygame.draw.circle(gameWindow, colour, get_pos(X, sx, mx, Y, sy, my), 5)
        pygame.display.update()
        loop = 2

    elif disco:
        colour = random.sample(list(range(256)), 3)
        for X, Y in zip(x, y):
            pygame.draw.circle(gameWindow, colour, get_pos(X, sx, mx, Y, sy, my), 5)
        pygame.display.update()

    gameClock.tick(10)

pygame.quit()
