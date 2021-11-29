from CardInvoiceManager.cardinvoicemanager import *
from mytools.tools import *
from mytools.register import *
from prettytable import PrettyTable
from datetime import datetime

idcheck = id_check('invoice_man.db')
cin = CardInvoiceManager()

record_funcreg = Register()


@record_funcreg(1)
def addreguser():
    name = input('Para quem você deseja adicionar um registro ?: ')
    if name in cin.viewpeoples():
        date = []
        while True:
            for t in 'DIA MÊS ANO'.split():
                d = correct_op(t + ': ', lambda x: x.isnumeric, 'Deve ser um número')
                date.append(d)
            date = '/'.join(date)
            try:
                date = datetime.strptime(date, '%d/%m/%Y').date()
            except ValueError:
                print_pause('DATA ÍNVALIDA')
            else:
                break
        installments = correct_op('Quantas prestações ?: ', lambda x: x.isnumeric,
                                  'Deve ser um número')
        paid = correct_op('Quantas já foram pagas ?: ', lambda x: x.isnumeric,
                          'Deve ser um número')
        installments += '/' + paid
        value = correct_op('Qual o valor das prestações: ', lambda x: x.isnumeric,
                           'Deve ser um número')
        cin.addreg(name, date.strftime('%d/%m/%Y'), installments, value)
        return
    print_pause('Usúario inexistente')


@record_funcreg(2)
def delreguser():
    name = input('NOME: ')
    if name in cin.viewpeoples():
        while True:
            _id = correct_op('ID: ', lambda x: x.isnumeric, 'Deve ser númerico')
            if idcheck(name, _id):
                break
        cin.delreg(name, _id)
        return
    print_pause('Usúario inexistente')


@record_funcreg(6)
def delallreg():
    name = input('NOME: ')
    if name in cin.viewpeoples():
        cin.delallreg(name)
        return
    print_pause('Usúario inexistente')


@record_funcreg(3)
def changereguser():
    name = input('NOME: ')
    if name in cin.viewpeoples():
        pass
    print_pause('Usúario inexistente')


@record_funcreg(4)
def viewreguser():
    pt = PrettyTable('ID DATA PARCELAS VALOR'.split())
    name = input('NOME: ')
    if name in cin.viewpeoples():
        records = cin.viewinvoice(name)
        amount = sum(float(v[-1]) for v in records)
        pt.add_rows(records)
        print(name, pt, sep='\n')
        print_pause(f'VALOR TOTAL: {amount:.2f}')
        return
    print_pause('Usúario inexistente')
