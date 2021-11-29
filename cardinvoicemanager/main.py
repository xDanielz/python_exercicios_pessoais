from record import *
from user import *
from consoleui import *

appname = 'GERENCIADOR DA FATURA'
options = 'USÚARIOS REGISTROS ENCERRAR'.split()
user_and_regs = [user_funcreg, record_funcreg]
main_menu = ConsoleUi(appname, options)

if __name__ == '__main__':
    while True:
        op = main_menu()
        submenu_options = 'ADICIONAR REMOVER ALTERAR VISUALIZAR VOLTAR'.split()

        if op == 1:
            submenu_name = 'USÚARIOS'

        elif op == 2:
            submenu_name = 'REGISTROS'
            submenu_options.extend(('REMOVER TODOS DE UM USUARIO',))

        elif op == 3:
            break

        else:
            print('Valor ínvalido')

        sub_menu = ConsoleUi(submenu_name, submenu_options)
        sub_op = sub_menu()
        if sub_op == 5:
            continue
        list_func = user_and_regs[op-1]
        list_func[sub_op]()
        os.system('cls')
