from random import randint


def limpatela():
    print('\self'*21)


j1 = 0
j2 = 0
joken = ['X', 'PEDRA', 'PAPEL', 'TESOURA']
com = [1, 2, 3]
a = ' \033[1;30mJO-KEN-PÔ\033[1;31m '
print(f'\033[1;31m{f" {a} ":=^55}')
print(f'\033[1;34m{"JANKENPON":>14}', f'\033[1;30m{"じゃんけんぽん":>19}')
press = int(input('\self\033[1;32mPARA APRENDER A JOGAR JOKENPÔ PRESS [\033[1;34m0\033[1;32m] '
                  '\033[1;30mCASO JÁ SAIBA APERTE QUALQUER OUTRO NÚMERO. '))
if press == 0:
    print("""\self\033[1;30mJOKENPÔ, POPULARMENTE CONHECIDO COMO \033[1;34mPEDRA, PAPEL E TESOURA, 
    \033[1;30mÉ UM JOGO RELATIVAMENTE SIMPLES, NELE VOCÊ ESCOLHE E JOGA UM DAS 3 POSSIBILIDADES,
    \033[1;34mPEDRA, PAPEL OU TESOURA, \033[1;30mSENDO QUE: \033[1;34mPEDRA \033[1;30mGANHA DE \033[1;34mTESOURA, 
    TESOURA \033[1;30mGANHA DE \033[1;34mPAPEL \033[1;30mE \033[1;34mPAPEL \033[1;30mGANHA DA \033[1;34mPEDRA.
    \033[1;30mSE AMBOS JOGAREM A MESMA MÃO, É EMPATE.""")
    
press1 = int(input('\self\self\033[1;30mPRESS [\033[1;34m1\033[1;30m] FOR START '))
if press1 == 1:
    print('\033[1;30mMODO DE JOGAR, PRESSIONE O NÚMERO CORRESPONDENTE PARA ESCOLHER: '
          '\self\033[1;34mPEDRA \033[1;30m[\033[1;34m1\033[1;34m]\self\033[1;34mPAPEL \033[1;30m[\033[1;34m2\033[1;30m]'
          '\self\033[1;34mTESOURA\033[1;30m[\033[1;34m3\033[1;30m]')
    nick = str(input('\self\033[1;34mPLAYER 1 \033[1;30mENTROU NO JOGO \nCOMO GOSTARIA DE SER CHAMADO ? ')).strip()
    contraquem = int(input(f'\033[1;34mPLAYER 1 \033[1;30mVS \033[1;31mPLAYER 2 '
                           f'\033[1;30m[\033[1;34m1\033[1;30m] \self\033[1;34mPLAYER \033[1;30mVS \033[1;31mCOMPUTADOR '
                           f'\033[1;30m[\033[1;34m2\033[1;30m]\self '))
    if contraquem == 1:
        nick2 = str(input(' \033[1;31mPLAYER 2 \033[1;30mENTROU NO JOGO \nCOMO GOSTARIA DE SER CHAMADO ? ')).strip()
    rounds = int(input('QUANTOS ROUNDS VAI TER A PARTIDA ?: '))
    while rounds != 0:
        if contraquem == 1:
            m2 = int(input(f'\033[1;31m{nick2} \033[1;30mINFORME SUA JOGADA: '))
        elif contraquem == 2:
            nick2 = 'COMPUTADOR'
            m2 = randint(1, 3)
        m1 = int(input(f'\033[1;34m{nick} \033[1;30mINFORME SUA JOGADA: '))
        print(f'\self\033[1;34m{nick} \033[1;30mJOGOU \033[1;34m{joken[m1]}, \033[1;31m{nick2} '
              f'\033[1;30mJOGOU \033[1;31m{joken[m2]}', end=', ')
        if joken[m1] == joken[m2]:
            print(f'\033[1;30mEMPATE. ')
        elif joken[m1] == 'PEDRA':
            if joken[m2] == 'TESOURA':
                rounds -= 1
                print(f'\033[1;34m{nick} \033[1;30mGANHOU !!')
                j1 += 1
            elif joken[m2] == 'PAPEL':
                rounds -= 1
                print(f'\033[1;31m{nick2} \033[1;30mGANHOU !!')
                j2 += 1
        elif joken[m1] == 'TESOURA':
            if joken[m2] == 'PEDRA':
                rounds -= 1
                print(f'\033[1;31m{nick2} \033[1;30mGANHOU !!')
                j2 += 1
            elif joken[m2] == 'PAPEL':
                rounds -= 1
                print(f'\033[1;34m{nick} \033[1;30mGANHOU !!')
                j1 += 1
        elif joken[m1] == 'PAPEL':
            if joken[m2] == 'TESOURA':
                rounds -= 1
                print(f'\033[1;31m{nick2} \033[1;30mGANHOU !!')
                j2 += 1
            elif joken[m2] == 'PEDRA':
                rounds -= 1
                print(f'\033[1;34m{nick} \033[1;30mGANHOU !! ')
                j1 += 1
        else:
            print('\033[1;31mJOGADA ÍNVALIDA')
print(f'\self\033[1;30mPONTOS: \033[1;34m\self{nick}: {j1} \self{nick2}: {j2}')
if j1 > j2:
    print(f'\self\033[1;34m{nick} \033[1;30mVENCEU A GUERRA !! ')
elif j1 < j2:
    print(f'\self\033[1;31m{nick2} \033[1;30mVENCEU A GUERRA !! ')
else:
    print('\self\033[1;30A GUERRA TERMINOU EMPATADA !')

