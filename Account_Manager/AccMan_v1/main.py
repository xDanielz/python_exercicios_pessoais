from prettytable import PrettyTable
import sqlite3
from AccountManager import *
from tools import *


accounts = []
with UseSqlite3db('Accounts.db') as cursor:
    try:
        regs = cursor.execute('SELECT * FROM accounts')
    except sqlite3.OperationalError:
        pass
    else:
        for i, reg in enumerate(regs.fetchall()):
            acc = dict(zip('account email password login'.split(), reg[1:]))
            accounts.append(AccountManager(**acc))
            accounts[i].set_alldatas(_id=reg[0])

menu = ('1 Adicionar', '2 Visualizar', '3 Mudar', '4 Deletar', '5 Sair')
while True:
    os.system('cls')
    op = correct_op('\n'.join(menu)+'\n: ', lambda n: n in map(str, range(1, 6)), 'Opção invalida')
    op = int(op)
    if op == len(menu):
        break

    elif op == 1:
        acc = {'account': input('Nome da conta: '),
               'email': input('E-mail: '),
               'password': input('Senha: '),
               'login': input('Login/Nome de usuario: ')}
        accounts.append(AccountManager(**acc))
        accounts[-1].save()
        print_pause('Conta salva com sucesso !')
        continue

    elif len(accounts) >= 1:
        if op == 2:
            pt = PrettyTable('ID CONTA E-MAIL SENHA USUARIO'.split())
            op = int(correct_op('1 Todos\n2 Pesquisar\n: ', lambda n: n in ('1', '2'), 'Opção invalida'))
            if op == 1:
                pt.add_rows(ac.show() for ac in accounts)
            elif op == 2:
                find = input('Encontrar: ')
                os.system('cls')
                for ac in accounts:
                    for data in ac.show():
                        if find.casefold() in str(data).casefold():
                            pt.add_row(ac.show())
                            break

            print_pause(pt.get_string(sortby='ID') if any(pt) else 'Nenhum registro foi encontrado')

        elif op == 3:
            idf = int(correct_op('ID: ', str.isnumeric, 'Opção invalida'))
            os.system('cls')
            try:
                i = findacc(idf, accounts)
            except ValueError:
                print_pause('ID Não encontrado')
            else:
                possibilities = [('account', 'CONTA'), ('email', 'E-MAIL'), ('password', 'SENHA'), ('login', 'USUARIO')]
                print('Escolhas os campos que deseja mudar')
                choices = input('1 Conta\n2 E-MAIL\n3 SENHA\n4 USUARIO\n: ').replace(' ', '')
                os.system('cls')
                choices = [int(n) for n in choices if n.isnumeric()]
                choices = [n for n in choices if 0 <= n <= 4]
                if any(choices) and len(choices) <= 4:
                    accounts[i].change(**{possibilities[k-1][0]: input(possibilities[k-1][1]+': ') for k in choices})
                    print_pause('Informações atualizadas com sucesso!')
                    continue
                print_pause('Opção invalída')

        elif op == 4:
            op = int(correct_op('1 Todos\n2 Só um\n: ', lambda n: n in ('1', '2'), 'Opção invalida'))
            if op == 1:
                with UseSqlite3db('Accounts.db') as cursor:
                    cursor.execute('DELETE FROM accounts')
                accounts.clear()
                AccountManager._instance_count = 0
                print_pause('Todas as contas foram apagadas com sucesso !')

            elif op == 2:
                idf = int(correct_op('ID: ', str.isnumeric, 'ID deve ser um número'))
                try:
                    i = findacc(idf, accounts)
                except ValueError:
                    print_pause('ID Não encontrado')
                else:
                    accounts[i].delete()
                    del accounts[i]
                    print_pause(f'Conta de ID {i} apagada com sucesso!')
        continue
    print_pause('Não existem contas salvas :(')
