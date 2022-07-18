def in_check(board, p):
    other_p = str((p % 2) + 1)
    check = False
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'P' + other_p:
                if p == 1:
                    if y < 7:
                        if board[x+1][y+1] == 'K1':
                            check = True
                            
                    if y > 0:
                        if board[x+1][y-1] == 'K1':
                            check = True
                            
                else:
                    if y < 7:
                        if board[x-1][y+1] == 'K2':
                            check = True
                            
                    if y > 0:
                        if board[x-1][y-1] == 'K2':
                            check = True
                            
            elif board[x][y] == 'R' + other_p:
                _x = x + 1
                _y = y
                while _x < 8:
                    if board[_x][_y] == '  ':
                        _x += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x - 1
                _y = y
                while _x >= 0:
                    if board[_x][_y] == '  ':
                        _x -= 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x
                _y = y + 1
                while _y < 8:
                    if board[_x][_y] == '  ':
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x
                _y = y - 1
                while _y >= 0:
                    if board[_x][_y] == '  ':
                        _y -= 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
            elif board[x][y] == 'B' + other_p:
                _x = x + 1
                _y = y + 1
                while _x < 8 and _y < 8:
                    if board[_x][_y] == '  ':
                        _x += 1
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x + 1
                _y = y - 1
                while _x < 8 and _y >= 0:
                    if board[_x][_y] == '  ':
                        _x += 1
                        _y -= 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x - 1
                _y = y + 1
                while _x >= 0 and _y < 8:
                    if board[_x][_y] == '  ':
                        _x -= 1
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x - 1
                _y = y - 1
                while _x >= 0 and _y >= 0:
                    if board[_x][_y] == '  ':
                        _x += 1
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
            elif board[x][y] == 'Q' + other_p:
                _x = x + 1
                _y = y
                while _x < 8:
                    if board[_x][_y] == '  ':
                        _x += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x - 1
                _y = y
                while _x >= 0:
                    if board[_x][_y] == '  ':
                        _x -= 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x
                _y = y + 1
                while _y < 8:
                    if board[_x][_y] == '  ':
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x
                _y = y - 1
                while _y >= 0:
                    if board[_x][_y] == '  ':
                        _y -= 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x + 1
                _y = y + 1
                while _x < 8 and _y < 8:
                    if board[_x][_y] == '  ':
                        _x += 1
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x + 1
                _y = y - 1
                while _x < 8 and _y >= 0:
                    if board[_x][_y] == '  ':
                        _x += 1
                        _y -= 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x - 1
                _y = y + 1
                while _x >= 0 and _y < 8:
                    if board[_x][_y] == '  ':
                        _x -= 1
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
                _x = x - 1
                _y = y - 1
                while _x >= 0 and _y >= 0:
                    if board[_x][_y] == '  ':
                        _x += 1
                        _y += 1
                    else:
                        if board[_x][_y] == 'K' + str(p):
                            check = True
                            
                        break
            elif board[x][y] == 'H' + other_p:
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
                for a, b in allowed:
                    if (0 <= a+x < 8) and (0 <= b+y < 8):
                        if board[a+x][b+y] == 'K' + str(p):
                            check = True
                            
            elif board[x][y] == 'K' + other_p:
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
                for a, b in allowed:
                    if (0 <= a+x < 8) and (0 <= b+y < 8):
                        if board[a+x][b+y] == 'K' + str(p):
                            check = True
                            
    return check

def checkmate(board, player):
    for sqx in range(8):
        for sqy in range(8):
            moves = []
            if board[sqx][sqy][1] == str(player):
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
                for move in moves:
                    temp = tuple([tuple(row) for row in board])
                    new_board = [[square for square in row] for row in temp]
                    new_board[sqx][sqy] = new_board[move[0]][move[1]]
                    new_board[move[0]][move[1]] = '  '
                    if not in_check(new_board, player):
                        return False
    return True