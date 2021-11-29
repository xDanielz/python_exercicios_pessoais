def temas_palavra() -> tuple:
    from random import choice
    Temas = dict(zoo=['leao', 'giraffa', 'macaco'],
                 pets=['cachorro', 'gato', 'passaro'],
                 qualidade=['humilde', 'gentil', 'carinhoso'],
                 familia=['daniel', 'claudio', 'longuinha',
                          'claudiane', 'luana', 'matheus',
                          'lucas', 'ravi', 'rodrigo',
                          'jessica', 'brenda'])
    tema = choice(list(Temas.keys()))
    return tema, choice(Temas[tema])


tema_palavra = temas_palavra()


def tema():
    return tema_palavra[0]


def palavra():
    return tema_palavra[1]


def process (p):    
    palavra_esc = palavra()
    palpite = p
    if len(palpite) > 1 and palpite != palavra_esc:
        answer = f'A palavra não é "{palpite}" Você perdeu'
    else:
        if palpite == palavra_esc:
            answer = f'A palavra era realmente {palpite}!'
        elif palpite in list(palavra_esc):
            answer = f'A letra "{palpite}" está na palavra'
        else:
            answer = f'A letra "{palpite}" não está na palavra'
    return answer
