def board():
    return ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']


def on_the_board():
    return [{'wP': ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
             'wT': ['a1', 'h1'], 'wC': ['b1', 'g1'], 'wB': ['c1', 'f1'], 'wD': ['d1'], 'wR': ['e1']},

            {'bP': ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
             'bT': ['a8', 'h8'], 'bC': ['b8', 'g8'], 'bB': ['c8', 'f8'], 'bD': ['d8'], 'bR': ['e8']}]


def up_board(pospiece):
    new_board = board()
    for dictt in pospiece:
        for key in dictt:
            for pos in dictt[key]:
                new_board[new_board.index(pos)] = key
    return new_board


def see_board(pospiece):
    for i, p in enumerate(up_board(pospiece), 1):
        print(f"\033[1;30m{p}", end=' ')
        if i % 8 == 0:
            print('')


def horizontal(real_value) -> list:
    edges = [0, 7, 8, 15, 16, 23, 24, 31, 32, 39, 40, 47, 48, 55, 56, 63]
    for n in range(len(edges)):
        if real_value % 8 == 0:
            real_value += 1
        if edges[n] <= real_value <= edges[n+1]:
            left_edge = edges[n]
            right_edge = edges[n+1]
            return list(range(left_edge, right_edge+1, 1))


def vertical(real_value) -> list:
    if real_value != 0:
        begin = list(range(real_value, -1, -8))[-1]
    else:
        begin = 0
    result = []
    for c in range(8):
        result.append(begin)
        begin += 8
    return result


def sides(real_value, vert=False, hori=False, diag=False):
    results = dict()
    if vert is True:
        verti = vertical(real_value)
        top = verti[:verti.index(real_value)]
        bot = verti[verti.index(real_value)+1:]
        results['Vertical'] = dict(TOP=top,
                                   BOT=bot)
    if hori is True:
        hori = horizontal(real_value)
        left = hori[:hori.index(real_value)]
        right = hori[hori.index(real_value) + 1:]
        results['Horizontal'] = dict(LEFT=left,
                                     RIGHT=right)
    if diag is True:
        diago = diagonal(real_value)
        result = [[], [], [], []]
        c = 0
        for d in diago:
            if d != '|':
                result[c].append(d)
            else:
                c += 1
        results['Diagonal'] = dict(TOP_LEFT=result[0],
                                   TOP_RIGHT=result[1],
                                   BOT_LEFT=result[2],
                                   BOT_RIGHT=result[3])
    return results


def diagonal(real_value) -> list:
    side = sides(real_value, hori=True, vert=True)
    leftside = sorted(side['Horizontal']['LEFT'], reverse=True)
    rightside = side['Horizontal']['RIGHT']
    topside = sorted(side['Vertical']['TOP'], reverse=True)
    botside = sorted(side['Vertical']['BOT'], reverse=False)
    limit = max([len(leftside), len(rightside), len(topside), len(botside)])
    result = []
    for pos in [topside, botside]:
        for pos1 in [leftside, rightside]:
            for k in range(limit):
                try:
                    result.append(pos[k] + pos1[k] - real_value)
                except IndexError:
                    break
            result.append('|')
    return result


def piece_movement(color, piece, pos, pospiece) -> list:
    pos_index = board().index(pos)
    my_pieces = pospiece[color]
    verti = sides(pos_index, vert=True)['Vertical']
    if color == 0:
        vert = sorted(verti['TOP'], reverse=True)
        foe_pieces = pospiece[1]
    else:
        vert = verti['BOT']
        foe_pieces = pospiece[0]
    horiz = sides(pos_index, hori=True)['Horizontal']
    diag = sides(pos_index, diag=True)['Diagonal']
    possible_moves = [[], [], []]
    moving_house = []
    if piece[1] == 'T':
        moving_house.extend([verti, horiz])
    elif piece[1] == 'B':
        moving_house.append(diag)
    elif piece[1] == 'D':
        moving_house.extend([verti, horiz, diag])
    elif piece[1] == 'C':
        for v, h in verti.items(), horiz.items():
            jump = []
            ex = 0
            ind = [-2, 1, -1, 0]
            for first_v in v, h:
                for i, c in enumerate(sorted(first_v[1], reverse=True)[:2]) if 'TOP' in first_v or 'LEFT' in first_v \
                        else enumerate(first_v[1][:2]):
                    for dict_value in sides(c, hori=True).values() if 'TOP' in first_v or 'BOT' in first_v \
                            else sides(c, vert=True).values():
                        for list_value in dict_value.values():
                            try:
                                if list_value:
                                    jump.append(list_value[ind[ex]])
                            except IndexError:
                                break
                            ex += 1
                            if ex == 4:
                                ex = 0
        moving_house.append({'JUMP': sorted(jump)})
    elif piece[1] == 'P':
        if pos_index in horizontal(8) and color == 1:
            c = 2
        elif pos_index in horizontal(48) and color == 0:
            c = 2
        else:
            c = 1
        moving_house.append({'TOP': [x for x in vert[0:c]]})
        for c in range(1):
            for k in ['TOP_LEFT', 'TOP_RIGHT']:
                try:
                    if up_board(pospiece)[diag[k][c]] in foe_pieces.keys():
                        moving_house.append({'TOP': board()[diag[c]]})
                except IndexError:
                    break
    elif piece[1] == 'R':
        pass
    for i, houses_pos in enumerate(moving_house):
        for k, dv in houses_pos.items():
            if k in ['TOP', 'LEFT']:
                dv = reversed(dv)
            for first_v in dv:
                if up_board(pospiece)[first_v] in my_pieces.keys():
                    break
                elif up_board(pospiece)[first_v] in foe_pieces.keys():
                    possible_moves[i].append(board()[first_v])
                    break
                possible_moves[i].append(board()[first_v])
    return possible_moves
