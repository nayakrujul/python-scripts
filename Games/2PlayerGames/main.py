import pygame, os, time, random, math, pingpong, chess_tools

pygame.init()

windowWidth = 500
windowHeight = 300
gameWindow = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("2-player Games")

gameClock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

def showMessage(
    message, colour, duration, 
    x=windowWidth//2, y=windowHeight//2, 
    fill=True, size=25, font="dejavusansmono",
    update=True
):
    if fill:
        gameWindow.fill(WHITE)
    font = pygame.font.SysFont(font, size)
    renderedText = font.render(message, True, colour)
    textArea = renderedText.get_rect()
    textArea.center = x, y
    gameWindow.blit(renderedText, textArea)
    if update:
        pygame.display.update()
    time.sleep(duration)

def paint_fight():

    showMessage('Player 1 - use WASD to move', BLUE, 3.0)
    showMessage('Player 2 - use arrows to move', RED, 3.0)
    showMessage('Fill the board with your colour', BLACK, 3.0)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)

    p1_x = 0
    p1_y = 120
    p1_xchange = 10
    p1_ychange = 0

    p2_x = windowWidth - 50
    p2_y = 120
    p2_xchange = -10
    p2_ychange = 0

    board = [[0 for i in range(windowWidth // 10)] for j in range(windowHeight // 10)]
    end_time = time.time() + 30

    game_running = True
    ended = False
    while game_running and not ended:

        gameWindow.fill(WHITE)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                ended = True
                game_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    ended = True
                    game_running = False

                if event.key == pygame.K_w:
                    p1_xchange = 0
                    p1_ychange = -10

                elif event.key == pygame.K_s:
                    p1_xchange = 0
                    p1_ychange = 10

                elif event.key == pygame.K_a:
                    p1_xchange = -10
                    p1_ychange = 0

                elif event.key == pygame.K_d:
                    p1_xchange = 10
                    p1_ychange = 0

                elif event.key == pygame.K_UP:
                    p2_xchange = 0
                    p2_ychange = -10

                elif event.key == pygame.K_DOWN:
                    p2_xchange = 0
                    p2_ychange = 10

                elif event.key == pygame.K_LEFT:
                    p2_xchange = -10
                    p2_ychange = 0

                elif event.key == pygame.K_RIGHT:
                    p2_xchange = 10
                    p2_ychange = 0

        p1_x += p1_xchange
        p1_y += p1_ychange
        
        if p1_x < 0:
            p1_x = 0
        elif p1_x > windowWidth - 50:
            p1_x = windowWidth - 50
        if p1_y < 0:
            p1_y = 0
        elif p1_y > windowHeight - 50:
            p1_y = windowHeight - 50
            
        p2_x += p2_xchange
        p2_y += p2_ychange

        if p2_x < 0:
            p2_x = 0
        elif p2_x > windowWidth - 50:
            p2_x = windowWidth - 50
        if p2_y < 0:
            p2_y = 0
        elif p2_y > windowHeight - 50:
            p2_y = windowHeight - 50

        for a in range(5):
            for b in range(5):
                board[(p1_y // 10) + a][(p1_x // 10) + b] = 1
                board[(p2_y // 10) + a][(p2_x // 10) + b] = 2

        for c in range(windowHeight // 10):
            for d in range(windowWidth // 10):
                if board[c][d] == 1:
                    pygame.draw.rect(gameWindow, BLUE, (d * 10, c * 10, 10, 10))
                elif board[c][d] == 2:
                    pygame.draw.rect(gameWindow, RED, (d * 10, c * 10, 10, 10))
        pygame.draw.rect(gameWindow, BLUE, (p1_x, p1_y, 50, 50))
        pygame.draw.rect(gameWindow, BLACK, (p1_x, p1_y, 50, 50), 5)
        pygame.draw.rect(gameWindow, RED, (p2_x, p2_y, 50, 50))
        pygame.draw.rect(gameWindow, BLACK, (p2_x, p2_y, 50, 50), 5)

        showMessage(str(round(end_time - time.time(), 1)), BLACK, 0, y=20, fill=False)

        counts = [0, 0, 0]
        for x in board:
            for y in x:
                counts[y] += 1

        showMessage('Player 1 ' + str(int(round(counts[1] / 15))) + '% - ' + str(int(round(counts[2] / 15))) + '% Player 2', BLACK, 0, y=50, fill=False)
        
        gameClock.tick(10)

        if time.time() > end_time:
            game_running = False

    if not ended:
        counts = [0, 0, 0]
        for x in board:
            for y in x:
                counts[y] += 1
        if counts[1] > counts[2]:
            showMessage('Player 1 wins!', BLUE, 5.0)
        elif counts[2] > counts[1]:
            showMessage('Player 2 wins!', RED, 5.0)
        else:
            showMessage('DRAW', BLACK, 5.0)

def gem_grab():
    
    showMessage('P1 - use any of WASD to grab', BLUE, 3.0)

    showMessage('P2 - use any arrow key to grab', RED, 3.0)

    showMessage('Grab the gem first', BLACK, 3.0)

    showMessage('First to 3 wins', BLACK, 3.0)

    showMessage('3...', BLACK, 1.0)
    
    showMessage('2...', BLACK, 1.0)
    
    showMessage('1...', BLACK, 1.0)

    p1_length = 50
    p1_change = 0
    p1_score = 0

    p2_length = 50
    p2_change = 0
    p2_score = 0

    diamond_taken = 0
    diamond_show = time.time() + (random.random() * 5)

    game_running = True
    while p1_score < 3 and p2_score < 3 and game_running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_running = False

                if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                    if p1_change == 0:
                        p1_change = 5

                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    if p2_change == 0:
                        p2_change = 5

        p1_length += p1_change
        p2_length += p2_change

        if p1_length >= 240 and p1_change == 5:
            p1_change = -5
        if p2_length >= 240 and p2_change == 5:
            p2_change = -5

        gameWindow.fill(WHITE)

        pygame.draw.rect(gameWindow, BLUE, (0, 125, p1_length, 50))
        pygame.draw.rect(gameWindow, RED, (windowWidth-p2_length, 125, p2_length, 50))
        
        if time.time() >= diamond_show:
            if diamond_taken == 0 and p1_length >= 240:
                diamond_taken = 1
            elif diamond_taken == 0 and p2_length >= 240:
                diamond_taken = 2
            if diamond_taken == 0:
                pygame.draw.circle(gameWindow, GREEN, (240, 140), 10)
            elif diamond_taken == 1:
                pygame.draw.circle(gameWindow, GREEN, (p1_length-10, 140), 10)
            else:
                pygame.draw.circle(gameWindow, GREEN, (windowWidth-p2_length+10, 140), 10)

        if diamond_taken == 1 and p1_length <= 0:
            p1_score += 1
            p1_length = 50
            p1_change = 0
            p2_length = 50
            p2_change = 0
            diamond_taken = 0
            diamond_show = time.time() + (random.random() * 5)
        elif diamond_taken == 2 and p2_length <= 0:
            p2_score += 1
            p1_length = 50
            p1_change = 0
            p2_length = 50
            p2_change = 0
            diamond_taken = 0
            diamond_show = time.time() + (random.random() * 5)
        elif p1_change == -5 and p2_change == -5 and p1_length <= 0 and p2_length <= 0:
            p1_length = 50
            p1_change = 0
            p2_length = 50
            p2_change = 0
            diamond_taken = 0
            diamond_show = time.time() + (random.random() * 5)

        for a in range(p1_score):
            pygame.draw.circle(gameWindow, BLUE, (a*50 + 20, 20), 20)
        for b in range(p1_score, 3):
            pygame.draw.circle(gameWindow, BLUE, (b*50 + 20, 20), 20, 5)
        for x in range(p2_score):
            pygame.draw.circle(gameWindow, RED, (windowWidth - (x*50 + 20), 20), 20)
        for y in range(p2_score, 3):
            pygame.draw.circle(gameWindow, RED, (windowWidth - (y*50 + 20), 20), 20, 5)

        pygame.display.update()
        gameClock.tick(60)

    if game_running:
        if p1_score == 3:
            showMessage('Player 1 wins!', BLUE, 5.0)
        else:
            showMessage('Player 2 wins!', RED, 5.0)

def football():

    showMessage('Player 1 - use WASD to move', BLUE, 3.0)

    showMessage('Player 2 - use arrow keys to move', RED, 3.0)

    showMessage('Further controls are in the', BLACK, 0.0, y=140)
    showMessage('bottom corners of the screen', BLACK, 3.0, y=160, fill=False)

    showMessage('First to 3 wins', BLACK, 3.0)

    showMessage('3...', BLACK, 1.0)
    
    showMessage('2...', BLACK, 1.0)
    
    showMessage('1...', BLACK, 1.0)

    p1_x1 = 200
    p1_x2 = 50
    p2_x1 = 300
    p2_x2 = 450
    ball_x = 250
    p1_y1 = p1_y2 = p2_y1 = p2_y2 = ball_y = 150
    p1_xchange1 = p1_xchange2 = p1_ychange1 = p1_ychange2 = p2_xchange1 = p2_xchange2 = p2_ychange1 = p2_ychange2 = ball_xchange = ball_ychange = 0
    ball = 0
    ball_left = 0
    p1_player = p2_player = 1
    p1_score = p2_score = 0

    winner = 0
    while winner == 0:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                winner = -1
    
            elif event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_ESCAPE:
                    winner = -1

                if event.key == pygame.K_w:
                    if p1_player == 1:
                        p1_ychange1 = -5
                    else:
                        p1_ychange2 = -5
                        
                if event.key == pygame.K_s:
                    if p1_player == 1:
                        p1_ychange1 = 5
                    else:
                        p1_ychange2 = 5

                if event.key == pygame.K_a:
                    if p1_player == 1:
                        p1_xchange1 = -5
                    else:
                        p1_xchange2 = -5
                        
                if event.key == pygame.K_d:
                    if p1_player == 1:
                        p1_xchange1 = 5
                    else:
                        p1_xchange2 = 5

                if event.key == pygame.K_UP:
                    if p2_player == 1:
                        p2_ychange1 = -5
                    else:
                        p2_ychange2 = -5
                        
                if event.key == pygame.K_DOWN:
                    if p2_player == 1:
                        p2_ychange1 = 5
                    else:
                        p2_ychange2 = 5

                if event.key == pygame.K_LEFT:
                    if p2_player == 1:
                        p2_xchange1 = -5
                    else:
                        p2_xchange2 = -5
                        
                if event.key == pygame.K_RIGHT:
                    if p2_player == 1:
                        p2_xchange1 = 5
                    else:
                        p2_xchange2 = 5

                if event.key == pygame.K_z:
                    if ball != 1:
                        if p1_player == 1:
                            p1_player = 2
                            p1_xchange1 = 0
                            p1_ychange1 = 0
                        else:
                            p1_player = 1
                            p1_xchange2 = 0
                            p1_ychange2 = 0

                if event.key == pygame.K_RSHIFT:
                    if ball != 2:
                        if p2_player == 1:
                            p2_player = 2
                            p2_xchange1 = 0
                            p2_ychange1 = 0
                        else:
                            p2_player = 1
                            p2_xchange2 = 0
                            p2_ychange2 = 0

                if event.key == pygame.K_x:
                    if ball == 1:
                        if p1_player == 1:
                            if p1_xchange1 != 0:
                                ball = 0
                                ball_left = 15
                                ball_xchange += (p1_xchange1 // abs(p1_xchange1))
                            if p1_ychange1 != 0:
                                ball = 0
                                ball_left = 15
                                ball_ychange += (p1_ychange1 // abs(p1_ychange1))
                        else:
                            if p1_xchange2 != 0:
                                ball = 0
                                ball_left = 15
                                ball_xchange += (p1_xchange2 // abs(p1_xchange2))
                            if p1_ychange2 != 0:
                                ball = 0
                                ball_left = 15
                                ball_ychange += (p1_ychange2 // abs(p1_ychange2))
                    elif ball == 2:
                        if p1_player == 1:
                            if abs(p1_x1 - ball_x) < 50 and abs(p1_y1 - ball_y) < 50:
                                ball = 1
                        else:
                            if abs(p1_x2 - ball_x) < 50 and abs(p1_y2 - ball_y) < 50:
                                ball = 1

                if event.key == pygame.K_SLASH or event.key == pygame.K_QUESTION:
                    if ball == 2:
                        if p2_player == 1:
                            if p2_xchange1 != 0:
                                ball = 0
                                ball_left = 15
                                ball_xchange += (p2_xchange1 // abs(p2_xchange1))
                            if p2_ychange1 != 0:
                                ball = 0
                                ball_left = 15
                                ball_ychange += (p2_ychange1 // abs(p2_ychange1))
                        else:
                            if p2_xchange2 != 0:
                                ball = 0
                                ball_left = 15
                                ball_xchange += (p2_xchange2 // abs(p2_xchange2))
                            if p2_ychange2 != 0:
                                ball = 0
                                ball_left = 15
                                ball_ychange += (p2_ychange2 // abs(p2_ychange2))
                    elif ball == 1:
                        if p2_player == 1:
                            if abs(p2_x1 - ball_x) < 50 and abs(p2_y1 - ball_y) < 50:
                                ball = 2
                        else:
                            if abs(p2_x2 - ball_x) < 50 and abs(p2_y2 - ball_y) < 50:
                                ball = 2

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    
                    if p1_player == 1:
                        if p1_ychange1 == -5:
                            p1_ychange1 = 0
                    else:
                        if p1_ychange2 == -5:
                            p1_ychange2 = 0
                        
                if event.key == pygame.K_s:
                    if p1_player == 1:
                        if p1_ychange1 == 5:
                            p1_ychange1 = 0
                    else:
                        if p1_ychange2 == 5:
                            p1_ychange2 = 0

                if event.key == pygame.K_a:
                    if p1_player == 1:
                        if p1_xchange1 == -5:
                            p1_xchange1 = 0
                    else:
                        if p1_xchange2 == -5:
                            p1_xchange2 = 0
                        
                if event.key == pygame.K_d:
                    if p1_player == 1:
                        if p1_xchange1 == 5:
                            p1_xchange1 = 0
                    else:
                        if p1_xchange2 == 5:
                            p1_xchange2 = 0

                if event.key == pygame.K_UP:
                    if p2_player == 1:
                        if p2_ychange1 == -5:
                            p2_ychange1 = 0
                    else:
                        if p2_ychange2 == -5:
                            p2_ychange2 = 0
                        
                if event.key == pygame.K_DOWN:
                    if p2_player == 1:
                        if p2_ychange1 == 5:
                            p2_ychange1 = 0
                    else:
                        if p2_ychange2 == 5:
                            p2_ychange2 = 0

                if event.key == pygame.K_LEFT:
                    if p2_player == 1:
                        if p2_xchange1 == -5:
                            p2_xchange1 = 0
                    else:
                        if p2_xchange2 == -5:
                            p2_xchange2 = 0
                        
                if event.key == pygame.K_RIGHT:
                    if p2_player == 1:
                        if p2_xchange1 == 5:
                            p2_xchange1 = 0
                    else:
                        if p2_xchange2 == 5:
                            p2_xchange2 = 0

        if p1_player == 1:
            if p1_x2 != 50:
                p1_xchange2 = (-(p1_x2 - 50) // abs(p1_x2 - 50)) * 2
            else:
                p1_xchange2 = 0
            if p1_y2 != 150:
                p1_ychange2 = (-(p1_y2 - 150) // abs(p1_y2 - 150)) * 2
            else:
                p1_ychange2 = 0
        else:
            if p1_x1 != ball_x:
                p1_xchange1 = (-(p1_x1 - ball_x) // abs(p1_x1 - ball_x)) * 2
            else:
                p1_xchange1 = 0
            if p1_y1 != ball_y:
                p1_ychange1 = (-(p1_y1 - ball_y) // abs(p1_y1 - ball_y)) * 2
            else:
                p1_ychange1 = 0

        if p2_player == 1:
            if p2_x2 != 450:
                p2_xchange2 = (-(p2_x2 - 450) // abs(p2_x2 - 450)) * 2
            else:
                p2_xchange2 = 0
            if p2_y2 != 150:
                p2_ychange2 = (-(p2_y2 - 150) // abs(p2_y2 - 150)) * 2
            else:
                p2_ychange2 = 0
        else:
            if p2_x1 != ball_x:
                p2_xchange1 = (-(p2_x1 - ball_x) // abs(p2_x1 - ball_x)) * 2
            else:
                p2_xchange1 = 0
            if p2_y1 != ball_y:
                p2_ychange1 = (-(p2_y1 - ball_y) // abs(p2_y1 - ball_y)) * 2
            else:
                p2_ychange1 = 0
        
        p1_x1 += p1_xchange1
        if p1_x1 < 0:
            p1_x1 = 0
        if p1_x1 > 500:
            p1_x1 = 500
        p1_x2 += p1_xchange2
        if p1_x2 < 0:
            p1_x2 = 0
        if p1_x2 > 500:
            p1_x2 = 500
        p1_y1 += p1_ychange1
        if p1_y1 < 0:
            p1_y1 = 0
        if p1_y1 > 300:
            p1_y1 = 300
        p1_y2 += p1_ychange2
        if p1_y2 < 0:
            p1_y2 = 0
        if p1_y2 > 300:
            p1_y2 = 300
        p2_x1 += p2_xchange1
        if p2_x1 < 0:
            p2_x1 = 0
        if p2_x1 > 500:
            p2_x1 = 500
        p2_x2 += p2_xchange2
        if p2_x2 < 0:
            p2_x2 = 0
        if p2_x2 > 500:
            p2_x2 = 500
        p2_y1 += p2_ychange1
        if p2_y1 < 0:
            p2_y1 = 0
        if p2_y1 > 300:
            p2_y1 = 300
        p2_y2 += p2_ychange2
        if p2_y2 < 0:
            p2_y2 = 0
        if p2_y2 > 300:
            p2_y2 = 300

        if ball_left > 0:
            ball_x += ball_xchange * ball_left
            ball_y += ball_ychange * ball_left
            ball_left -= 1

        if ball == 0 and abs(p1_x1 - ball_x) < 20 and abs(p1_y1 - ball_y) < 20:
            ball = 1
            p1_player = 1
            p1_xchange2 = 0
            p1_ychange2 = 0
        elif ball == 0 and abs(p1_x2 - ball_x) < 20 and abs(p1_y2 - ball_y) < 20:
            ball = 1
            p1_player = 2
            p1_xchange1 = 0
            p1_ychange1 = 0
        if ball == 0 and abs(p2_x1 - ball_x) < 20 and abs(p2_y1 - ball_y) < 20:
            ball = 2
            p2_player = 1
            p2_xchange2 = 0
            p2_ychange2 = 0
        elif ball == 0 and abs(p2_x2 - ball_x) < 20 and abs(p2_y2 - ball_y) < 20:
            ball = 2
            p2_player = 2
            p2_xchange1 = 0
            p2_ychange1 = 0

        if ball == 1:
            if p1_player == 1:
                ball_x, ball_y = p1_x1 + 20, p1_y1
            else:
                ball_x, ball_y = p1_x2 + 20, p1_y2
        elif ball == 2:
            if p2_player == 1:
                ball_x, ball_y = p2_x1 - 20, p2_y1
            else:
                ball_x, ball_y = p2_x2 - 20, p2_y2

        if ball_x < 0:
            ball_x = 0
        if ball_x > 500:
            ball_x = 500
        if ball_y < 0:
            ball_y = 0
        if ball_y > 300:
            ball_y = 300

        if ball_x > 490 and (100 < ball_y < 200):
            p1_score += 1
            p1_x1 = 200
            p1_x2 = 50
            p2_x1 = 300
            p2_x2 = 450
            ball_x = 250
            p1_y1 = p1_y2 = p2_y1 = p2_y2 = ball_y = 150
            p1_xchange1 = p1_xchange2 = p1_ychange1 = p1_ychange2 = p2_xchange1 = p2_xchange2 = p2_ychange1 = p2_ychange2 = ball_xchange = ball_ychange = 0
            ball = 0
            ball_left = 0
            p1_player = p2_player = 1
        elif ball_x < 10 and (100 < ball_y < 200):
            p2_score += 1
            p1_x1 = 200
            p1_x2 = 50
            p2_x1 = 300
            p2_x2 = 450
            ball_x = 250
            p1_y1 = p1_y2 = p2_y1 = p2_y2 = ball_y = 150
            p1_xchange1 = p1_xchange2 = p1_ychange1 = p1_ychange2 = p2_xchange1 = p2_xchange2 = p2_ychange1 = p2_ychange2 = ball_xchange = ball_ychange = 0
            ball = 0
            ball_left = 0
            p1_player = p2_player = 1

        gameWindow.fill(WHITE)

        pygame.draw.line(gameWindow, BLACK, (250, 0), (250, 300), 5)
        pygame.draw.rect(gameWindow, BLACK, (0, 50, 100, 200), 5)
        pygame.draw.circle(gameWindow, BLACK, (100, 150), 50, 5)
        pygame.draw.rect(gameWindow, WHITE, (0, 55, 95, 190))
        pygame.draw.rect(gameWindow, BLACK, (400, 50, 100, 200), 5)
        pygame.draw.circle(gameWindow, BLACK, (400, 150), 50, 5)
        pygame.draw.rect(gameWindow, WHITE, (405, 55, 95, 190))
        pygame.draw.circle(gameWindow, BLACK, (250, 150), 50, 5)
        
        pygame.draw.line(gameWindow, BLUE, (0, 100), (0, 200), 10)
        pygame.draw.line(gameWindow, RED, (500, 100), (500, 200), 10)

        pygame.draw.circle(gameWindow, WHITE, (ball_x, ball_y), 10)
        pygame.draw.circle(gameWindow, BLACK, (ball_x, ball_y), 10, 5)
        
        pygame.draw.circle(gameWindow, BLUE, (p1_x1, p1_y1), 20)
        showMessage('A', WHITE, 0.0, p1_x1, p1_y1, False, 20)
        pygame.draw.circle(gameWindow, BLUE, (p1_x2, p1_y2), 20)
        showMessage('B', WHITE, 0.0, p1_x2, p1_y2, False, 20)
        
        pygame.draw.circle(gameWindow, RED, (p2_x1, p2_y1), 20)
        showMessage('A', WHITE, 0.0, p2_x1, p2_y1, False, 20)
        pygame.draw.circle(gameWindow, RED, (p2_x2, p2_y2), 20)
        showMessage('B', WHITE, 0.0, p2_x2, p2_y2, False, 20)

        if p1_player == 1:
            pygame.draw.polygon(gameWindow, BLUE, [
                (p1_x1-20, p1_y1-50), (p1_x1+20, p1_y1-50), (p1_x1, p1_y1-25)
            ], 5)
        else:
            pygame.draw.polygon(gameWindow, BLUE, [
                (p1_x2-20, p1_y2-50), (p1_x2+20, p1_y2-50), (p1_x2, p1_y2-25)
            ], 5)

        if p2_player == 1:
            pygame.draw.polygon(gameWindow, RED, [
                (p2_x1-20, p2_y1-50), (p2_x1+20, p2_y1-50), (p2_x1, p2_y1-25)
            ], 5)
        else:
            pygame.draw.polygon(gameWindow, RED, [
                (p2_x2-20, p2_y2-50), (p2_x2+20, p2_y2-50), (p2_x2, p2_y2-25)
            ], 5)

        pygame.draw.rect(gameWindow, WHITE, (200, 10, 100, 20))
        pygame.draw.rect(gameWindow, BLACK, (190, 5, 120, 30), 5)
        showMessage(f'{p1_score} - {p2_score}', BLACK, 0.0, y=20, fill=False)

        if ball != 1:
            showMessage('Z - change player', BLUE, 0.0, 80, 260, False, 15)
        if ball == 2:
            if p1_player == 1:
                if abs(p1_x1 - ball_x) < 50 and abs(p1_y1 - ball_y) < 50:
                    showMessage('X - tackle', BLUE, 0.0, 50, 280, False, 15)
            else:
                if abs(p1_x2 - ball_x) < 50 and abs(p1_y2 - ball_y) < 50:
                    showMessage('X - tackle', BLUE, 0.0, 50, 280, False, 15)
        elif ball == 1:
            showMessage('X - kick ball', BLUE, 0.0, 60, 280, False, 15)

        if ball != 2:
            showMessage('SHIFT - change player', RED, 0.0, 400, 260, False, 15)
        if ball == 1:
            if p2_player == 1:
                if abs(p2_x1 - ball_x) < 50 and abs(p2_y1 - ball_y) < 50:
                    showMessage('/ - tackle', RED, 0.0, 450, 280, False, 15)
            else:
                if abs(p2_x2 - ball_x) < 50 and abs(p2_y2 - ball_y) < 50:
                    showMessage('/ - tackle', RED, 0.0, 450, 280, False, 15)
        elif ball == 2:
            showMessage('/ - kick ball', RED, 0.0, 440, 280, False, 15)

        if p1_score == 3:
            winner = 1
        elif p2_score == 3:
            winner = 2

        gameClock.tick(10)

    if winner != -1:
        if winner == 1:
            showMessage('Player 1 wins!', BLUE, 5.0)
        else:
            showMessage('Player 2 wins!', RED, 5.0)

def arrow_game():
    showMessage('Player 1 - use WASD', BLUE, 3.0)
    showMessage('Player 2 - use arrows', RED, 3.0)
    showMessage('Press the keys in the correct order', BLACK, 3.0, size=20)
    showMessage('First to 5 wins', BLACK, 3.0)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)
    
    up = '↑'
    down = '↓'
    left = '←'
    right = '→'

    length = 4
    new_list = lambda: [random.choice([up, down, left, right]) for times in range(length)]
    lst = new_list()

    p1 = []
    p2 = []
    p1_score = p2_score = 0
    pause = 0

    game_running = True
    while ((p1_score < 5 and p2_score < 5) or p1_score == p2_score) and game_running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_running = False

                if event.key == pygame.K_w:
                    p1.append(up)

                elif event.key == pygame.K_s:
                    p1.append(down)

                elif event.key == pygame.K_a:
                    p1.append(left)

                elif event.key == pygame.K_d:
                    p1.append(right)

                elif event.key == pygame.K_UP:
                    p2.append(up)

                elif event.key == pygame.K_DOWN:
                    p2.append(down)

                elif event.key == pygame.K_LEFT:
                    p2.append(left)

                elif event.key == pygame.K_RIGHT:
                    p2.append(right)

                if len(p1) > length:
                    p1 = p1[:length]
                if len(p2) > length:
                    p2 = p2[:length]

        if pause <= 0:
            if length <= 8:
                showMessage(' '.join(lst), BLACK, 0.0, y=50, size=50)
            else:
                showMessage(' '.join(lst), BLACK, 0.0, y=50, size=400 // length)
                
            for x in range(len(p1)):
                if p1[x] == lst[x]:
                    showMessage(p1[x], GREEN, 0.0, ((x % 4) * 50) + 50, ((x // 4) * 50) + 100, size=40, fill=False)
                else:
                    showMessage(p1[x], RED, 0.0, ((x % 4) * 50) + 50, ((x // 4) * 50) + 100, size=40, fill=False)
            for y in range(len(p2)):
                if p2[y] == lst[y]:
                    showMessage(p2[y], GREEN, 0.0, 500 - (((y % 4) + 1) * 50), ((y // 4) * 50) + 100, size=40, fill=False)
                else:
                    showMessage(p2[y], RED, 0.0, 500 - ((y % 4) * 50), ((y // 4) * 50) + 100, size=40, fill=False)
            showMessage(f'{p1_score} - {p2_score}', BLACK, 0.0, y=250, fill=False)
    
            if len(p1) == length or len(p2) == length:
                p1_correct = p2_correct = 0
                for i in range(len(p1)):
                    if p1[i] == lst[i]:
                        p1_correct += 1
                for j in range(len(p2)):
                    if p2[j] == lst[j]:
                        p2_correct += 1
                if p1_correct > p2_correct:
                    p1_score += p1_correct - p2_correct
                if p2_correct > p1_correct:
                    p2_score += p2_correct - p1_correct
                length += 1
                lst = new_list()
                pause = 1
        else:
            pause -= 0.1
            p1 = []
            p2 = []

        gameClock.tick(10)

    if game_running:
        if p1_score > p2_score:
            showMessage('Player 1 wins!', BLUE, 5.0)
        else:
            showMessage('Player 2 wins!', RED, 5.0)

def race():

    showMessage('Player 1 - use W', BLUE, 3.0)
    showMessage('Player 2 - use up arrow', RED, 3.0)
    showMessage('Keep tapping your key', BLACK, 3.0)
    showMessage('Don\'t false start', BLACK, 3.0)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)
    
    p1_x = p2_x = 0
    p1_false = p2_false = 0
    start = time.time() + (random.random() * 3)
    full_round = lambda x, n: str(round(x, n)).split('.')[0] + '.' + str(round(x, n)).split('.')[1] + ((n - len(str(round(x, n)).split('.')[1])) * '0')
    
    game_running = True
    while p1_x < 500 and p2_x < 500 and game_running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_running = False
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                    
                if event.key == pygame.K_w:
                    if time.time() > start:
                        p1_x += 5
                    else:
                        p1_false += 1
                        start = time.time() + (random.random() * 3)
                        
                if event.key == pygame.K_UP:
                    if time.time() > start:
                        p2_x += 5
                    else:
                        p2_false += 1
                        start = time.time() + (random.random() * 3)
                        
        if p1_false >= 3:
            p2_x = 500
        if p2_false >= 3:
            p1_x = 500
            
        if time.time() < start:
            
            showMessage('On your marks', BLACK, 0.0)
            
            pygame.draw.circle(gameWindow, BLUE, (50, 50), 20, 5)
            pygame.draw.circle(gameWindow, BLUE, (100, 50), 20, 5)
            pygame.draw.circle(gameWindow, BLUE, (150, 50), 20, 5)
            
            for i in range(1, p1_false+1):
                pygame.draw.line(gameWindow, BLUE, ((i * 50) - math.sqrt(200), 50 - math.sqrt(200)), ((i * 50) + math.sqrt(200), 50 + math.sqrt(200)), 5)
                pygame.draw.line(gameWindow, BLUE, ((i * 50) + math.sqrt(200), 50 - math.sqrt(200)), ((i * 50) - math.sqrt(200), 50 + math.sqrt(200)), 5)
                
            pygame.draw.circle(gameWindow, RED, (50, 250), 20, 5)
            pygame.draw.circle(gameWindow, RED, (100, 250), 20, 5)
            pygame.draw.circle(gameWindow, RED, (150, 250), 20, 5)
            
            for j in range(1, p2_false+1):
                pygame.draw.line(gameWindow, RED, ((j * 50) - math.sqrt(200), 250 - math.sqrt(200)), ((j * 50) + math.sqrt(200), 250 + math.sqrt(200)), 5)
                pygame.draw.line(gameWindow, RED, ((j * 50) + math.sqrt(200), 250 - math.sqrt(200)), ((j * 50) - math.sqrt(200), 250 + math.sqrt(200)), 5)
                
            pygame.display.update()
            
        else:
            showMessage(str(full_round(time.time() - start, 2)), BLACK, 0.0, y=50)
            if time.time() < (start + 1):
                showMessage('Go', BLACK, 0.0, fill=False)
            pygame.draw.circle(gameWindow, BLUE, (p1_x, 100), 10)
            showMessage(str((500 - p1_x) // 5), BLUE, 0.0, p1_x, 80, size=15, fill=False)
            pygame.draw.circle(gameWindow, RED, (p2_x, 200), 10)
            showMessage(str((500 - p2_x) // 5), RED, 0.0, p2_x, 180, size=15, fill=False)

        gameClock.tick(20)

    if game_running:
        if p1_false < 3 and p2_false < 3:
            showMessage(str(full_round(time.time() - start, 2)), BLACK, 0.0, y=50)
        else:
            gameWindow.fill(WHITE)
        if p1_x >= 500:
            showMessage('Player 1 wins!', BLUE, 5.0, fill=False)
        else:
            showMessage('Player 2 wins!', RED, 5.0, fill=False)

def shooting_aliens():
    showMessage('P1 - use A/D to move, W to shoot', BLUE, 3.0)
    showMessage('P1 - use Left/Right to move, Up to shoot', RED, 3.0, size=20)
    showMessage('Dodge the aliens\' bullets', BLACK, 3.0)
    showMessage('Shoot the aliens', BLACK, 3.0)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)
    aliens = [[1 for a in range(20)] for b in range(5)]
    aliens_x = 20
    aliens_y = 20
    aliens_change = 2
    p1_x = 0
    p2_x = 450
    p1_change = p2_change = 0
    p1_bullet = p2_bullet = aliens_bullet = False
    p1_bullet_x = p1_bullet_y = p2_bullet_x = p2_bullet_y = aliens_bullet_x = aliens_bullet_y = 0
    p1_score = p2_score = 0
    game_running = True
    aliens_alive = True
    while game_running and aliens_alive:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_running = False
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    game_running = False

                elif event.key == pygame.K_a:
                    p1_change = -5

                elif event.key == pygame.K_d:
                    p1_change = 5

                elif event.key == pygame.K_w:
                    if not p1_bullet:
                        p1_bullet = True
                        p1_bullet_x = p1_x + 25
                        p1_bullet_y = 250

                elif event.key == pygame.K_LEFT:
                    p2_change = -5

                elif event.key == pygame.K_RIGHT:
                    p2_change = 5

                elif event.key == pygame.K_UP:
                    if not p2_bullet:
                        p2_bullet = True
                        p2_bullet_x = p2_x + 25
                        p2_bullet_y = 250

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_a:
                    if p1_change == -5:
                        p1_change = 0

                elif event.key == pygame.K_d:
                    if p1_change == 5:
                        p1_change = 0

                elif event.key == pygame.K_LEFT:
                    if p2_change == -5:
                        p2_change = 0

                elif event.key == pygame.K_RIGHT:
                    if p2_change == 5:
                        p2_change = 0

        gameWindow.fill(WHITE)
        
        p1_x += p1_change
        p2_x += p2_change
        
        if p1_x < 0:
            p1_x = 0
        elif p1_x > 200:
            p1_x = 200
            pygame.draw.line(gameWindow, BLACK, (250, 220), (250, 300), 5)
            
        if p2_x < 250:
            p2_x = 250
            pygame.draw.line(gameWindow, BLACK, (250, 220), (250, 300), 5)
        elif p2_x > 450:
            p2_x = 450
            
        pygame.draw.rect(gameWindow, BLUE, (p1_x, 250, 50, 20))
        pygame.draw.rect(gameWindow, RED, (p2_x, 250, 50, 20))

        if p1_bullet:
            p1_bullet_y -= 10
            if p1_bullet_y < 0:
                p1_bullet = False
            pygame.draw.circle(gameWindow, BLACK, (p1_bullet_x, p1_bullet_y), 2)
        if p2_bullet:
            p2_bullet_y -= 10
            if p2_bullet_y < 0:
                p2_bullet = False
            pygame.draw.circle(gameWindow, BLACK, (p2_bullet_x, p2_bullet_y), 2)

        if not aliens_bullet:
            aliens_bullet = True
            aliens_bullet_x = aliens_x + (random.randint(0, 19) * 20)
            aliens_bullet_y = aliens_y + (random.randint(0, 4) * 20)

        if aliens_bullet:
            aliens_bullet_y += 10
            if aliens_bullet_y >= 250:
                aliens_bullet = False
                if p1_x <= aliens_bullet_x <= p1_x + 50:
                    p1_score -= 50
                elif p2_x <= aliens_bullet_x <= p2_x + 50:
                    p2_score -= 50
            pygame.draw.circle(gameWindow, BLACK, (aliens_bullet_x, aliens_bullet_y), 2)

        aliens_x += aliens_change
        if aliens_x > 80 and aliens_change > 0:
            aliens_change = -aliens_change
            if aliens_y < 150:
                aliens_y += 10
        elif aliens_x < 20 and aliens_change < 0:
            aliens_change = -aliens_change
            if aliens_y < 150:
                aliens_y += 10

        aliens_alive = False
        for x in range(5):
            for y in range(20):
                i = aliens_x + (y * 20)
                j = aliens_y + (x * 20)
                if p1_bullet and abs(p1_bullet_x - i) < 10 and abs(p1_bullet_y - j) < 10 and aliens[x][y] == 1:
                    aliens[x][y] = 0
                    p1_bullet = False
                    p1_score += 10
                if p2_bullet and abs(p2_bullet_x - i) < 10 and abs(p2_bullet_y - j) < 10 and aliens[x][y] == 1:
                    aliens[x][y] = 0
                    p2_bullet = False
                    p2_score += 10
                elif aliens[x][y] == 1:
                    aliens_alive = True
                    pygame.draw.circle(gameWindow, GREEN, (i, j), 8)
        
        showMessage(str(p1_score), BLUE, 0.0, 50, 280, False)
        showMessage(str(p2_score), RED, 0.0, 450, 280, False)
        gameClock.tick(10)

    if game_running:
        if p1_score > p2_score:
            showMessage('Player 1 wins!', BLUE, 5.0)
        else:
            showMessage('Player 2 wins!', RED, 5.0)

def play_1v1():

    showMessage('P1 - Move: WASD, Shoot: Q', BLUE, 3.0)
    showMessage('P2 - Move: Arrows, Shoot: Shift', RED, 3.0)
    showMessage('Shoot the other person five times to win', BLACK, 3.0, size=20)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)
    
    p1_x = 50
    p2_x = 450
    p1_y = p2_y = 150
    p1_xchange = p1_ychange = p2_xchange = p2_ychange = 0
    p1_health = p2_health = 5
    p1_ammo = p2_ammo = 3.0
    p1_bullets = []
    p2_bullets = []
    game_running = True
    
    while game_running and p1_health > 0 and p2_health > 0:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_running = False
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    game_running = False

                if event.key == pygame.K_w:
                    p1_ychange = -5

                elif event.key == pygame.K_s:
                    p1_ychange = 5

                elif event.key == pygame.K_a:
                    p1_xchange = -5

                elif event.key == pygame.K_d:
                    p1_xchange = 5

                elif event.key == pygame.K_q:
                    if p1_ammo >= 1:
                        p1_ammo -= 1
                        if not (p1_xchange == 0 and p1_ychange == 0):
                            p1_bullets.append([p1_x, p1_y, p1_xchange * 2, p1_ychange * 2])

                elif event.key == pygame.K_UP:
                    p2_ychange = -5

                elif event.key == pygame.K_DOWN:
                    p2_ychange = 5

                elif event.key == pygame.K_LEFT:
                    p2_xchange = -5

                elif event.key == pygame.K_RIGHT:
                    p2_xchange = 5

                elif event.key == pygame.K_RSHIFT:
                    if p2_ammo >= 1:
                        p2_ammo -= 1
                        if not (p2_xchange == 0 and p2_ychange == 0):
                            p2_bullets.append([p2_x, p2_y, p2_xchange * 2, p2_ychange * 2])
                    
            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    if p1_ychange == -5:
                        p1_ychange = 0
                        
                if event.key == pygame.K_s:
                    if p1_ychange == 5:
                        p1_ychange = 0

                if event.key == pygame.K_a:
                    if p1_xchange == -5:
                        p1_xchange = 0
                        
                if event.key == pygame.K_d:
                    if p1_xchange == 5:
                        p1_xchange = 0

                if event.key == pygame.K_UP:
                    if p2_ychange == -5:
                        p2_ychange = 0
                        
                if event.key == pygame.K_DOWN:
                    if p2_ychange == 5:
                        p2_ychange = 0

                if event.key == pygame.K_LEFT:
                    if p2_xchange == -5:
                        p2_xchange = 0
                        
                if event.key == pygame.K_RIGHT:
                    if p2_xchange == 5:
                        p2_xchange = 0

        p1_x += p1_xchange
        p1_y += p1_ychange
        
        if p1_x < 0:
            p1_x = 0
        elif p1_x > windowWidth:
            p1_x = windowWidth
        if p1_y < 0:
            p1_y = 0
        elif p1_y > windowHeight:
            p1_y = windowHeight
            
        p2_x += p2_xchange
        p2_y += p2_ychange

        if p2_x < 0:
            p2_x = 0
        elif p2_x > windowWidth:
            p2_x = windowWidth
        if p2_y < 0:
            p2_y = 0
        elif p2_y > windowHeight:
            p2_y = windowHeight

        if p1_ammo < 3.0:
            p1_ammo += 0.1
        if p2_ammo < 3.0:
            p2_ammo += 0.1

        gameWindow.fill(WHITE)
        pygame.draw.circle(gameWindow, BLUE, (p1_x, p1_y), 20)
        pygame.draw.line(gameWindow, BLUE, (p1_x, p1_y), (p1_x + 5*p1_xchange, p1_y + 5*p1_ychange), 5)
        pygame.draw.circle(gameWindow, RED, (p2_x, p2_y), 20)
        pygame.draw.line(gameWindow, RED, (p2_x, p2_y), (p2_x + 5*p2_xchange, p2_y + 5*p2_ychange), 5)

        for i in range(int(p1_ammo)):
            pygame.draw.rect(gameWindow, BLUE, (p1_x + (i - 1.5) * 10, p1_y + 35, 10, 10))
        for j in range(int(p1_ammo), 3):
            pygame.draw.rect(gameWindow, BLUE, (p1_x + (j - 1.5) * 10, p1_y + 35, 10, 10), 1)

        for k in range(int(p2_ammo)):
            pygame.draw.rect(gameWindow, RED, (p2_x + (k - 1.5) * 10, p2_y + 35, 10, 10))
        for l in range(int(p2_ammo), 3):
            pygame.draw.rect(gameWindow, RED, (p2_x + (l - 1.5) * 10, p2_y + 35, 10, 10), 1)

        pygame.draw.rect(gameWindow, BLUE, (p1_x - 25, p1_y - 35, p1_health * 10, 10))
        pygame.draw.rect(gameWindow, RED, (p2_x - 25, p2_y - 35, p2_health * 10, 10))

        index = 0
        while index < len(p1_bullets):
            x, y, xchng, ychng = p1_bullets[index]
            x += xchng
            y += ychng
            p1_bullets[index] = [x, y, xchng, ychng]
            pygame.draw.circle(gameWindow, BLUE, (x, y), 5)
            if x < 0 or x > 500 or y < 0 or y > 300:
                p1_bullets.pop(index)
            if math.sqrt((p2_x - x) ** 2 + (p2_y - y) ** 2) < 20:
                p2_health -= 1
                p1_bullets.pop(index)
            index += 1

        index2 = 0
        while index2 < len(p2_bullets):
            x, y, xchng, ychng = p2_bullets[index2]
            x += xchng
            y += ychng
            p2_bullets[index2] = [x, y, xchng, ychng]
            pygame.draw.circle(gameWindow, RED, (x, y), 5)
            if x < 0 or x > 500 or y < 0 or y > 300:
                p2_bullets.pop(index2)
            if math.sqrt((p1_x - x) ** 2 + (p1_y - y) ** 2) < 20:
                p1_health -= 1
                p2_bullets.pop(index2)
            index2 += 1
        
        pygame.display.update()
        gameClock.tick(10)

    if game_running:
        if p1_health > 0:
            showMessage('Player 1 wins!', BLUE, 5.0)
        else:
            showMessage('Player 2 wins!', RED, 5.0)

def chess():
    showMessage('Both players - use the mouse', BLACK, 3.0)
    showMessage('Click a piece then click a new position', BLACK, 3.0, size=20)
    showMessage('Checkmate your opponent to win', BLACK, 3.0)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)
    
    board = [
        ['R1', 'H1', 'B1', 'Q1', 'K1', 'B1', 'H1', 'R1'],
        ['P1' for a in range(8)]
    ] + [['  ' for b in range(8)] for c in range(4)] + [
        ['P2' for d in range(8)],
        ['R2', 'H2', 'B2', 'Q2', 'K2', 'B2', 'H2', 'R2']
    ]
    game_running = True
    new_display = True
    player = 1
    selected = (-1, -1)
    moves = []
    get_square = lambda xpos, ypos: ((xpos - 10) // 60, (ypos - 10) // 35)
    winner = 0
    while game_running and winner == 0:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_running = False
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    game_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (10 <= mousex < 490) and (10 <= mousey < 290):
                    sqx, sqy = get_square(mousex, mousey)
                    if board[sqx][sqy][1] == str(player):
                        selected = sqx, sqy
                        new_display = True
                        moves = []
                        if board[sqx][sqy][0] == 'P':
                            if player == 1:
                                if sqx < 7:
                                    if board[sqx+1][sqy] == '  ':
                                        moves.append((sqx + 1, sqy))
                                if sqx == 1:
                                    if board[3][sqy] == '  ':
                                        moves.append((3, sqy))
                                if sqy < 7:
                                    if board[sqx+1][sqy+1][1] == '2':
                                        moves.append((sqx + 1, sqy + 1))
                                if sqy > 0:
                                    if board[sqx+1][sqy-1][1] == '2':
                                        moves.append((sqx + 1, sqy - 1))
                            else:
                                if sqx > 0:
                                    if board[sqx-1][sqy] == '  ':
                                        moves.append((sqx - 1, sqy))
                                if sqx == 6:
                                    if board[4][sqy] == '  ':
                                        moves.append((4, sqy))
                                if sqy < 7:
                                    if board[sqx-1][sqy+1][1] == '1':
                                        moves.append((sqx - 1, sqy + 1))
                                if sqy > 0:
                                    if board[sqx-1][sqy-1][1] == '1':
                                        moves.append((sqx - 1, sqy - 1))
                        elif board[sqx][sqy][0] == 'R':
                            x = sqx + 1
                            y = sqy
                            while x < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx - 1
                            y = sqy
                            while x >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx
                            y = sqy + 1
                            while y < 8:
                                print(x, y)
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    y += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx
                            y = sqy - 1
                            while y >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    y -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                        elif board[sqx][sqy][0] == 'B':
                            x = sqx + 1
                            y = sqy + 1
                            while x < 8 and y < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x += 1
                                    y += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx + 1
                            y = sqy - 1
                            while x < 8 and y >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x += 1
                                    y -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx - 1
                            y = sqy + 1
                            while x >= 0 and y < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x -= 1
                                    y += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx - 1
                            y = sqy - 1
                            while x >= 0 and y >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x -= 1
                                    y -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                        elif board[sqx][sqy][0] == 'Q':
                            x = sqx + 1
                            y = sqy
                            while x < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx - 1
                            y = sqy
                            while x >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx
                            y = sqy + 1
                            while y < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    y += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx
                            y = sqy - 1
                            while y >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    y -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx + 1
                            y = sqy + 1
                            while x < 8 and y < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x += 1
                                    y += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx + 1
                            y = sqy - 1
                            while x < 8 and y >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x += 1
                                    y -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx - 1
                            y = sqy + 1
                            while x >= 0 and y < 8:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x -= 1
                                    y += 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                            x = sqx - 1
                            y = sqy - 1
                            while x >= 0 and y >= 0:
                                if board[x][y] == '  ':
                                    moves.append((x, y))
                                    x -= 1
                                    y -= 1
                                else:
                                    if board[x][y][1] != str(player):
                                        moves.append((x, y))
                                    break
                        elif board[sqx][sqy][0] == 'H':
                            allowed = [
                                (-2, -1),
                                (-2, 1),
                                (-1, -2),
                                (-1, 2),
                                (1, -2),
                                (1, 2),
                                (2, -1),
                                (2, 1)
                            ]
                            for x, y in allowed:
                                if (0 <= sqx+x < 8) and (0 <= sqy+y < 8):
                                    if board[sqx+x][sqy+y][1] != str(player):
                                        moves.append((sqx + x, sqy + y))
                        elif board[sqx][sqy][0] == 'K':
                            allowed = [
                                (-1, -1),
                                (-1, 0),
                                (-1, 1),
                                (0, -1),
                                (0, 1),
                                (1, -1),
                                (1, 0),
                                (1, 1)
                            ]
                            for x, y in allowed:
                                if (0 <= sqx+x < 8) and (0 <= sqy+y < 8):
                                    if board[sqx+x][sqy+y][1] != str(player):
                                        moves.append((sqx + x, sqy + y))
                    elif selected != (-1, -1):
                        if (sqx, sqy) in moves:
                            prev_board = tuple([tuple(row) for row in board])
                            board[sqx][sqy] = board[selected[0]][selected[1]]
                            board[selected[0]][selected[1]] = '  '
                            if chess_tools.in_check(board, player):
                                board = [[square for square in row] for row in prev_board]
                            else:
                                selected = (-1, -1)
                                moves = []
                                player = (player % 2) + 1
                                new_display = True

        if chess_tools.checkmate(board, 1):
            winner = 2
        elif chess_tools.checkmate(board, 2):
            winner = 1

        if new_display:

            new_display = False
            
            gameWindow.fill(WHITE)
            
            colour = [BLUE, RED][player - 1]
            
            for x in range(10, 500, 60):
                pygame.draw.line(gameWindow, colour, (x, 10), (x, 290), 5)
            for y in range(10, 300, 35):
                pygame.draw.line(gameWindow, colour, (10, y), (490, y), 5)

            if selected != (-1, -1):
                for x, y in moves:
                    pygame.draw.circle(gameWindow, colour, (x*60 + 40, y*35 + 27.5), 10)
                        
            for row in range(8):
                for square in range(8):
                    if board[row][square][1] == '1':
                        showMessage(board[row][square][0], BLUE, 0.0, row*60 + 40, square*35 + 27.5, False, update=False)
                    elif board[row][square][1] == '2':
                        showMessage(board[row][square][0], RED, 0.0, row*60 + 40, square*35 + 27.5, False, update=False)
            
            pygame.display.update()
        gameClock.tick(10)

    if game_running:
        if winner == 1:
            showMessage('Player 1 wins!', BLUE, 5.0)
        else:
            showMessage('Player 2 wins!', RED, 5.0)

def stop_watchers():
    showMessage('P1 - Use any of WASD', BLUE, 3.0)
    showMessage('P2 - Use any arrow key', RED, 3.0)
    showMessage('Stop at the specified time to win', BLACK, 3.0)
    showMessage('3...', BLACK, 1.0)
    showMessage('2...', BLACK, 1.0)
    showMessage('1...', BLACK, 1.0)
    
    stop_at = random.randint(5, 10)
    p1_stop = p2_stop = 0
    elapsed = 0.0
    game_running = True
    while (p1_stop < 2 or p2_stop < 2) and game_running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_running = False

                if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                    if p1_stop < 2:
                        p1_stop = elapsed

                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    if p2_stop < 2:
                        p2_stop = elapsed

        showMessage(f'Stop at {stop_at} seconds', BLACK, 0.0, y=50, update=False)
        pygame.draw.rect(gameWindow, BLUE, (100, 125, 100, 50), 5)
        pygame.draw.rect(gameWindow, RED, (300, 125, 100, 50), 5)
        if elapsed < 2:
            pygame.draw.rect(gameWindow, BLUE, (100, 125, 100, elapsed * 25))
            showMessage(str(round(elapsed, 1)), BLUE, 0.0, 150, fill=False, update=False)
            pygame.draw.rect(gameWindow, RED, (300, 125, 100, elapsed * 25))
            showMessage(str(round(elapsed, 1)), RED, 0.0, 350, fill=False)
        else:
            pygame.draw.rect(gameWindow, BLUE, (100, 125, 100, 50))
            pygame.draw.rect(gameWindow, RED, (300, 125, 100, 50))
            if (elapsed - p1_stop <= 1) and (p1_stop >= 2):
                pygame.draw.rect(gameWindow, GREEN, (100, 125, 100, 50), 5)
            if (elapsed - p2_stop <= 1) and (p2_stop >= 2):
                pygame.draw.rect(gameWindow, GREEN, (300, 125, 100, 50), 5)
            pygame.display.update()
        elapsed += 0.1
        gameClock.tick(10)

    if game_running:
        p1 = abs(p1_stop - stop_at)
        p2 = abs(p2_stop - stop_at)
        gameWindow.fill(WHITE)
        pygame.draw.rect(gameWindow, BLUE, (100, 125, 100, 50), 5)
        pygame.draw.rect(gameWindow, RED, (300, 125, 100, 50), 5)
        showMessage(str(round(p1_stop, 1)), BLUE, 0.0, 150, fill=False, update=False)
        showMessage(str(round(p2_stop, 1)), RED, 0.0, 350, fill=False, update=False)
        if p1 < p2:
            showMessage('Player 1 wins!', BLUE, 5.0, y=50, fill=False)
        elif p2 < p1:
            showMessage('Player 2 wins!', RED, 5.0, y=50, fill=False)
        else:
            showMessage('Draw!', BLACK, 5.0, y=50, fill=False)
            

message = True
running = True
while running:

    if message:
        showMessage('Select a game', BLACK, 0.0, y=25, update=False)
        showMessage('[ESC] Exit', BLACK, 0.0, y=60, fill=False, size=15, update=False)
        showMessage('[1] Paint fight', BLACK, 0.0, y=100, fill=False, size=15, update=False)
        showMessage('[2] Gem grab', BLACK, 0.0, y=120, fill=False, size=15, update=False)
        showMessage('[3] Ping pong', BLACK, 0.0, y=140, fill=False, size=15, update=False)
        showMessage('[4] Football', BLACK, 0.0, y=160, fill=False, size=15, update=False)
        showMessage('[5] Arrow game', BLACK, 0.0, y=180, fill=False, size=15, update=False)
        showMessage('[6] Race', BLACK, 0.0, y=200, fill=False, size=15, update=False)
        showMessage('[7] Shooting aliens', BLACK, 0.0, y=220, fill=False, size=15, update=False)
        showMessage('[8] 1v1', BLACK, 0.0, y=240, fill=False, size=15, update=False)
        showMessage('[9] Chess', BLACK, 0.0, y=260, fill=False, size=15, update=False)
        showMessage('[0] Stop watchers', BLACK, 0.0, y=280, fill=False, size=15, update=False)
        pygame.display.update()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
                break

            elif event.key == pygame.K_1:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                paint_fight()
                message = True
                break

            elif event.key == pygame.K_2:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                gem_grab()
                message = True
                break

            elif event.key == pygame.K_3:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                pingpong.play()
                message = True
                break

            elif event.key == pygame.K_4:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                football()
                message = True
                break

            elif event.key == pygame.K_5:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                arrow_game()
                message = True
                break

            elif event.key == pygame.K_6:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                race()
                message = True
                break
                
            elif event.key == pygame.K_7:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                shooting_aliens()
                message = True
                break

            elif event.key == pygame.K_8:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                play_1v1()
                message = True
                break

            elif event.key == pygame.K_9:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                chess()
                message = True
                break

            elif event.key == pygame.K_0:
                showMessage('Press ESCAPE to return to menu', BLACK, 3.0)
                stop_watchers()
                message = True
                break

    gameClock.tick(10)
    
pygame.quit()
