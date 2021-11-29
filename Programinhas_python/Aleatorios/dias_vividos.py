import datetime
print(f'\033[1;30mVou lhe dizer quantos dias você viveu')
IDADE = int(input('\nInforme sua idade: '))
MESES = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO',
         'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
DIASM = {'JANEIRO': 31, 'FEVEREIRO': 29, 'MARÇO': 31, 'ABRIL': 30, 'MAIO': 31, 'JUNHO': 31, 'JULHO': 31,
         'AGOSTO': 31, 'SETEMBRO': 30, 'OUTUBRO': 31, 'NOVEMBRO': 30, 'DEZEMBRO': 31}

DIAT = datetime.date.today().day  # DIA ATUAL
MAT = datetime.date.today().month  # MES ATUAL
diasav = 0  # Aqui vai ser somado os dias que já viveu do ano atual.

for d in range(0, MAT - 1):
    diasav += DIASM[MESES[d]]
diasav += DIAT - 1
ANO_ATUAL = datetime.date.today().year  # ANO ATUAL
ANO_DE_NASCIMENTO = ANO_ATUAL - IDADE  # ANO DE NASCIMENTO
# HORAT = datetime.time().hour  HORA ATUAL
# Verificar quais anos a partir do ano do nascimento, até o atual para saber quais são bissextos.
ap, c = ANO_DE_NASCIMENTO, 0
while ap != ANO_ATUAL:
    if ap % 4 == 0:
        if ap % 100 != 0:
            c += 1
    else:
        if ap % 400 == 0:
            c += 1
    ap += 1
DJV = (IDADE * 365) + c + diasav
print(f'\nVOCÊ JÁ VIVEU: {DJV} DIAS {round(DJV/12)} MESES\nAPROXIMADAMENTE {DJV/12*24} HORAS.')
