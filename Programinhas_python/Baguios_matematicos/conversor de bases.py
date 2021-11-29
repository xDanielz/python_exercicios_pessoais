num = int(input(f'\033[1;30m{"Conversor de bases númericas":^40} \nDigite o número: '))
base = 1
base = int(input("""\nEscolha a base:
    [ 1 ]HEXADECIMAL
    [ 2 ]BINÁRIO
    [ 3 ]OCTAL
    """))
h = ['10', '11', '12', '13', '14', '15']
hexa = ['a', 'b', 'c', 'd', 'e', 'f']
r1 = []
c, c1 = 0, 0
n = num
r = ''
para, acaba = True, True
while para:
    if base == 1:
        nb = 'HEXADECIMAL'
        b = 16
        para = False
    elif base == 2:
        nb = 'BINÁRIO'
        b = 2
        para = False
    elif base == 3:
        nb = 'OCTAL'
        b = 8
        para = False
    else:
        print('\033[1;31mNÚMERO INVALIDO')
        base = int(input('\nTente novamente: '))
while n != 0:
    r += str(n % b)
    r1.append(str(n % b))
    n //= b
while c1 != len(r1) and c != len(h):
    if h[c] in r1[c1]:
        r1[c1] = r1[c1].replace(r1[c1], hexa[c])
    c1 += 1
    if c1 == len(r1):
        c1 = 0
        c += 1
if base == 1:
    r = ''.join(r1)
r = r[::-1]
print(f'O Número \033[1;34m{num} \033[1;30mConvertido para \033[1;34m{nb} \033[1;30mé: \033[1;34m{r}')



