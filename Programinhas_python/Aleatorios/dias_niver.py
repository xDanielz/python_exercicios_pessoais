from datetime import date
MES_ATUAL = date.today().month  # mes atual
met = MES_ATUAL
DIA_ATUAL = date.today().day  # dia atual
dat = DIA_ATUAL
MESES_DO_ANO = ['x', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
                'outubro', 'novembro', 'dezembro']
DIAS_DO_ANO = {'x': 0, 'janeiro': 31, 'fevereiro': 29, 'março': 31, 'abril': 30, 'maio': 31, 'junho': 30, 'julho': 31,
               'agosto': 31, 'setembro': 30, 'outubro': 31, 'novembro': 30, 'dezembro': 31}
dia_niver = int(input('\033[1;30mInforme a data do seu aniversário \n\nDIA: '))
mes_niver = int(input('MÊS: '))
parar = True
dpn = 0  # Dias para O aniversário
mpn = 0  # MESES para o aniversário
d = 0
while parar:
    if dat != DIAS_DO_ANO[MESES_DO_ANO[met]]:
        dat += 1
    else:
        dat = 1
        met += 1
    if dat == 1 and met != mes_niver:
        mpn += 1
    if met == MES_ATUAL or met == mes_niver and dat != DIA_ATUAL:
        dpn += 1
    if met == 13:
        met = 1
    if dat == dia_niver and met == mes_niver:
        parar = False
if dpn > 30:
    mpn += 1
    dpn -= 30
if dia_niver == DIA_ATUAL and mes_niver == MES_ATUAL:
    print('HOJE É SEU ANIVERSÁRIO PARABENS !!!')
print(f'FALTAM {mpn} MESES E {dpn} DIAS.')
