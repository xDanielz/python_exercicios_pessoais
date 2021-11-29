import os

from prettytable import PrettyTable
from AccountManager import id_check, AccountManager
from tools import *

_current_directory = os.getcwd()
_save_local = _current_directory + '\\save'
try:
    os.mkdir(_save_local)
except FileExistsError:
    os.chdir(_save_local)
except Exception as e:
    print_pause(e)
finally:
    os.chdir(_save_local)

accman = AccountManager('Accounts_v2.db')
idcheck = id_check('Accounts_v2.db', 'accounts_v2')
functions = {}


def register(op: int):
    assert isinstance(op, int)

    def deco(fun):
        functions[op] = fun

    return deco


def regischeck(fun):
    """
    Verifica se existe algum registro.
    """
    def deco():
        return fun() if bool(accman.show_all()) else print_pause('Nenhuma conta registrada')

    return deco


@register(1)
def save():
    reg = {'account': input('CONTA: '),
           'email': input('E-MAIL: '),
           'password': input('SENHA: '),
           'user': input('USUARIO: ')
           }
    accman.save(**reg)
    print_pause('Dados registrados com sucesso')


@register(4)
@regischeck
def change():
    _id = correct_op('ID: ', str.isnumeric, 'Valor ínvalido')
    if not idcheck(_id):
        print_pause(f'ID: {_id}, não encontrado')
        return
    print('Deixem em branco o que não é para ser alterado')
    before = accman.show(_id)
    reg = {'account': input(f'CONTA, {before[1]} ->: '),
           'email': input(f'E-MAIL, {before[2]} ->: '),
           'password': input(f'SENHA, {before[3]} ->: '),
           'user': input(f'USUARIO, {before[4]} ->: ')
           }
    ys = correct_op('Tem certeza ?\n[S,N]: ', lambda x: x.upper() in ('S', 'N'), 'Respota ínvalida')
    if ys in 'Ss':
        reg = {k: v for k, v in reg.items() if v != ''}
        accman.change(_id, **reg)
        print_pause(f'Conta de ID: {_id}, alterada com sucesso')


@register(3)
@regischeck
def delete():
    op = correct_op('1 TODOS\n2 SÓ UM\n: ', str.isnumeric, 'Deve ser um número')
    ys = correct_op('Tem certeza ?\n[S,N]: ', lambda x: x.upper() in ('S', 'N'), 'Respota ínvalida')
    if ys in 'Ss':
        if op == '1':
            accman.delete_all()
            print_pause('Todos os registros apagados com sucesso!')
        elif op == '2':
            _id = correct_op('ID: ', str.isnumeric, 'Deve ser um número')
            if not idcheck(_id):
                print_pause(f'ID: {_id}, não encontrado')
                return
            accman.delete(_id)
            print_pause(f'Registro: {_id}, apagado com sucesso')


@register(2)
@regischeck
def show():
    op = correct_op('1 TODOS\n2 ENCONTRAR\n: ', lambda x: str.isnumeric(x) and x in ('1', '2'), 'Valor ínvalido')
    pt = PrettyTable('ID CONTA E-MAIL SENHA USUÁRIO'.split())
    os.system('cls')
    if op == '1':
        pt.add_rows(accman.show_all())
    elif op == '2':
        match = set()
        search = input('PESQUISAR: ')
        for row in accman.show_all():
            for column in row:
                if search in str(column):
                    match.add(row)
        if match:
            pt.add_rows(match)
        else:
            print_pause('Nenhuma informação correspondente')
            return
    print_pause(pt)


def menu(menu_name: str, list_op: iter):
    menu_name = str(menu_name)
    list_op = list(list_op)

    def func():
        nonlocal list_op, menu_name
        print(menu_name.center(50))
        _menu = ''
        for i, o in enumerate(list_op, 1):
            _menu += f'{i} {o}\n'
        _menu += ':'
        op = correct_op(_menu, lambda x: str.isnumeric(x) and 0 < int(x) <= len(list_op), 'Valor ínvalido')
        return int(op)
    return func


def main():
    os.system('cls')
    mn = ['ADICIONAR', 'EXIBIR', 'APAGAR', 'MUDAR', 'ENCERRAR']
    showmenu = menu('GERENCIADOR DE CONTAS', mn)
    while True:
        op = showmenu()
        if op == len(mn):
            break
        func = functions[op]
        func()
        os.system('cls')


if __name__ == '__main__':
    main()
