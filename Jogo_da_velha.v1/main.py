from jogo_da_velha import JogoDaVelha
import os

result = ''
game = JogoDaVelha()
for _ in range(9):
    os.system('cls')
    game.hashtag()
    while True:
        move = str(input(f"Jogador {game.player+1} informe a posição: "))
        if move in game.available_positions:
            game.move(move)
            break
        print('\nErro, posição indisponível ou inexistente.\n')
    if game.victory():
        r = f"O jogador {game.player+1} ganhou !!"
        break
    game.change_turn()
else:
    r = "Deu Velha :("
os.system('cls')
print(r)
game.hashtag()
input('Pressione algo para sair')
