def Alfa(primeiro='A', ultimo='Z', passo=1):

    primeiro, ultimo = ord(primeiro.upper()), ord(ultimo.upper())

    if primeiro > ultimo:
        primeiro, ultimo = ultimo, primeiro

    for letra in range(primeiro, ultimo+1, passo):
        yield chr(letra)


for letter in Alfa():
    print(letter, end=' ')