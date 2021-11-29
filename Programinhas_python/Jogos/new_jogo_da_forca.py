try:
    from daniel_personal.func_jogo_forca import tema, palavra
except ModuleNotFoundError:
    from func_jogo_forca import tema, palavra

print(f"{' Jogo da forca ':=^50}")
chances = 6
tema_esc = tema().upper()
palavra_esc = palavra().upper()
palavra_lista = list(palavra_esc)
palavra_escondida = list('_'*len(palavra_esc))
print(f"TEMA: {tema_esc}\nQuantidade de letras na palavra {len(palavra_esc)}")
while True:
    palpite = str(input(f"Te restam {chances} tentativas\nDe o seu \"chute\": ")).upper().strip()
    if palpite in palavra_esc and palpite not in palavra_escondida:
        if palpite == palavra_esc:
            print(f"\033[1;36mVocê acertou a palavra realmente era \033[1;34m{palpite.upper()}!")
            break
        for letra in palavra_lista:
            if letra == palpite:
                palavra_escondida[palavra_lista.index(letra)] = letra
                palavra_lista[palavra_lista.index(letra)] = '_'
        print(f"\033[1;36mVocê acertou, a palavra realmente continha a letra: "
              f"\033[1;34m{palpite}\033[1;30m\self{''.join(palavra_escondida)}")
    elif palpite not in palavra_esc:
        chances -= 1
        if chances == 0 or len(palpite) > 2:
            print(f"\nInfelizmente você perdeu :(\nA palavra era {palavra_esc}")
            break
        elif len(palpite) == 2:
            print(f"\033[1;31mApenas chute uma letra ou a palavra inteira\033[1;30m")
        elif len(palpite) == 1:
            print(f"\033[1;31mErrou, não contem a letra {palpite}\033[1;30m")
    else:
        print("\033[1;33mVocê já \"chutou\" essa letra\033[1;30m")