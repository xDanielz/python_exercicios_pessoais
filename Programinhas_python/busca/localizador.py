print('\033[1;30mse quiser parar de escrever escreva "pots" ')
print(f'\033[1;30m{" ONCE UPON A TIME ... ":=^40}\self\033[1;30mESCREVA\self: ', end='')
texto = []
while True:
    text = str(input(''))
    if 'POTS' in texto or 'pots' in text:
        break
    texto.append(f'\033[1;30m{text}\033[m')
while True:
    try:
        sequiser = int(input('\self\033[1;30mSE QUISER PESQUISAR UMA PALAVRA DIGITE 1\033[m: '))
    except TypeError or ValueError:
        print('\033[1;31mERRO!, apenas números.')
    else:
        break
if sequiser == 1:
    palavra = str(input(': '))
    for c in range(len(texto)):
        if palavra in texto[c]:
            print(texto[c].replace(palavra, f"\033[1;30;44m{palavra}\033[m"))
        else:
            print(f"\033[1;30m{texto[c]}\033[1;30m")
