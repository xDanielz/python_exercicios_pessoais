from mytools.tools import *
from mytools.register import *
from CardInvoiceManager.cardinvoicemanager import *

cin = CardInvoiceManager()

user_funcreg = Register()


@user_funcreg(1)
def addcarduser():
    name = input('NOME: ')
    if name not in cin.viewpeoples():
        cin.addpeople(name)
        return
    print_pause('Usuário existente.')


@user_funcreg(2)
def subcarduser():
    name = input('NOME: ')
    if name in cin.viewpeoples():
        cin.subpeople(name)
        return
    print_pause('Usuário inexistente.')


@user_funcreg(3)
def changecarduser():
    name = input('NOME: ')
    if name in cin.viewpeoples():
        newname = input('NOVO NOME: ')
        cin.changepeople(name, newname)
        return
    print_pause('Usuário inexistente.')


@user_funcreg(4)
def viewusers():
    for n in cin.viewpeoples():
        print(n)
    os.system('pause')
