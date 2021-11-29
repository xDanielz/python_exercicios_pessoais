import os
from time import sleep

print(f"DESLIGAMENTO AUTOMATIZADO".center(60))

hour = int(input('HORA: '))
minute = int(input('MINUTO: '))
second = int(input('SEGUNDO: '))

t = hour*60*60 + minute*60 + second

for c in range(t, -1, -1):
    print('\t\t\t\tDeslingando em ', c, 'Segundos')
    sleep(1)
    if not c:
        os.system('shutdown -s -f -t 0')
    os.system('cls')
