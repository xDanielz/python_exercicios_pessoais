while True:
    search = str(input('Informe a palavra que gostaria de procurar: '))
    try:
        with open(f'acounts.txt', 'r') as file:
            for lines in file.readlines():
                if search in lines:
                    print(lines)
                    break
            else:
                print('Não encontrado')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    stop = str(input('Gostaria de procurar outra palavra?[S/N]: '))[0].upper()
    if stop == 'N':
        break
