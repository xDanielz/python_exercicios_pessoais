from python_exercicios_pessoais.Chess_project.func import *

onboard = on_the_board()
while True:
    for c in [0, 1]:
        see_board(onboard)
        while True:
            while True:
                piece = str(input(f'{c} Peça: '))
                if len(piece) == 2:
                    piece = piece[0].lower()+piece[1].upper()
                if piece in onboard[c].keys():
                    break
            while True:
                pos = str(input('Posição da peça: '))
                if pos in onboard[c][piece]:
                    break
            while True:
                stop = False
                pos_mov = (piece_movement(c, piece, pos, onboard))
                if pos_mov == [[], [], []]:
                    break
                print(pos_mov)
                move = str(input('Para onde vai: '))
                for k in range(3):
                    if move in pos_mov[k]:
                        stop = True
                if stop:
                    break
            if c == 0:
                possible_enemy_piece = up_board(onboard)[board().index(move)]
                if possible_enemy_piece in onboard[1].keys():
                    onboard[1][possible_enemy_piece].pop(onboard[1][possible_enemy_piece].index(move))
            onboard[c][piece][onboard[c][piece].index(pos)] = move
            break
