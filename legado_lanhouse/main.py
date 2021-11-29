from Sistema_Aux import *

services = [('XEROX', 0.50),
            ('IMPRESSÃO', 1.00),
            ('BOLETO/SEGUNDA-VIA', 2.00),
            ('CURRICULO', 3.00),
            ('COPIA', 0.50),
            ('EXTRA', 1.00)]

color = False
amount = 1
barber_salon = SalaoPedro(services)
while True:
    while True:
        print('\n')
        barber_salon.menu()
        option = condition_stopped(': ', range(1, 7))-1
        if option != 6:
            amount = condition_stopped('Quantos: ', range(1, 21))
            color = condition_stopped('Colorido? [S/N]: ')
        barber_salon.operation(services[option][0], amount, color)
        stop = condition_stopped('Deseja finalizar ? [S/N]: ')
        if stop:
            barber_salon.end_operation()
            break
    kill = condition_stopped('Deseja encerrar o programa ?[S/N]: ')
    if kill:
        break
