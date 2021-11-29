print('\033[1;34m=-' * 12, '\033[1;30mCALCULADORA', '\033[1;34m-=' * 12)
c, d, resultado = 0, 0, 0
operation = ['*', '+', '-', '/']
while c != 1:
    num = input('')
    num = num.replace(' ', '')
    for c in range(0, 4):
        if operation[c] in num:
            f = num.find(operation[c])
            r = num[f]
            n = int(num[:f])
            n1 = int(num[f + 1:])
            if operation[c] in num:
                if r == '+':
                    resultado = n + n1
                elif r == '*':
                    resultado = n * n1
                elif r == '-':
                    resultado = n - n1
                elif r == '/':
                    resultado = n / n1
        c = 1

while d != 1:
    print(resultado, end=' ')
    outron = input('')
    valor = int(outron[1:])
    sina = outron.find(outron[0])
    sinal = outron[sina]
    if sinal == '+':
        resultado += valor
    elif sinal == '*':
        resultado *= valor
    elif sinal == '-':
        resultado -= valor
    elif sinal == '/':
        resultado /= valor


