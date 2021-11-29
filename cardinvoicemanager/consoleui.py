from mytools.tools import *


class ConsoleUi:
    def __init__(self, name, options):
        self.name = name
        self.options = tuple(options)

    def __call__(self):
        os.system('cls')
        print(self.name.upper().center(60))
        while True:
            for i, op in enumerate(self.options, 1):
                print(f'{i}.{op}')
            op = input(": ")
            os.system('cls')
            if op.isnumeric() and int(op) <= len(self.options):
                return int(op)
            print_pause("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
            os.system('cls')
