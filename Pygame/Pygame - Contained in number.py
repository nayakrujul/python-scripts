import pygame, os, time

#  CHANGEABLE  #
width = 1000   # width of screen
height = 1000  # height of screen
quick = True   # quick/slow version
# ------------ #

pygame.init()
os.system('clear')

gameClock = pygame.time.Clock()
gameWindow = pygame.display.set_mode((width, height))

pygame.display.set_caption("RN09")

WHITE = (255, 255, 255)
GREY = (200, 200, 200)

num = input('Enter a digit (0-9): ')
if num not in list('0123456789'):
    num = '7'

gameWindow.fill(WHITE)

last_time = None
start_time = time.time()

def secs_to_min_secs(s):
    min, sec = divmod(s, 60)
    return f'{int(min)}:{str(int(sec)).zfill(2)}'

for i in range(1, width*height + 1):
    y, x = divmod(i, width)
    if x == 0:
        os.system('clear')
        percent = round(y*100 / height, 1)
        print(f'{percent}% complete.')
        if last_time is not None:
            diff = time.time() - last_time
            time_for_all = diff * 1000
            to_complete = 1 - (percent / 100)
            remaining = int(round(to_complete*time_for_all))
            print(f'Time remaining:', secs_to_min_secs(remaining))
        print(f'Time so far:', secs_to_min_secs(time.time() - start_time))
        last_time = time.time()
    if num in str(i):
        pygame.draw.circle(gameWindow, GREY, (x, y), 1)
        if not quick:
            pygame.display.update()

pygame.display.update()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False

pygame.quit()