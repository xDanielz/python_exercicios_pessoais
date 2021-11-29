from datetime import datetime


class SalaoPedro:

    def __init__(self, iterable: iter):

        self.final_value = 0
        self.price_dict = dict(iterable)
        self.done = dict()
        
    def menu(self):

        for op, name in enumerate(self.price_dict.keys(), 1):
            print(f"{name:<20} - {op:2}")

    def operation(self, option: str, amount: int, color=False):
        value = self.price_dict[option]
        if color:
            value += 0.50 * amount
            option += '/Cor'
        self.done.setdefault(option, (value, amount))
        self.final_value += value * amount

    def register(self):

        with open('registro da lan.txt', 'w') as file:
            file.write(f"{datetime.now()}\n")
            for name, (value, amount) in self.done.items():
                file.writelines(f"Nome: {name}\n Quantidade: {amount} Valor: {value}R$ \n\n")
                
    def result_of_operation(self):

        print('\n')
        dist = len(max(self.done.keys(), key=len))
        if dist < 12:
            dist = 12
        for name, (value, amount) in self.done.items():
            print(f"{name:{dist}} {'-'*30} {value:5} X Qtds {amount} = {value*amount}R$")
            
        print(f"{'Valor final':{dist}} {'-'*30} {self.final_value:5}R$ \n")
        
    def end_operation(self):

        self.result_of_operation()
        self.register()
        self.final_value = 0
        self.done.clear()


def condition_stopped(txt: str, expected=None):
    if expected is None:
        expected = {'S': True, 'N': False}
    chosen = None
    if isinstance(expected, dict):
        while chosen not in expected.keys():
            chosen = str(input(txt)).upper()
        return expected[chosen]
    while chosen not in expected:
        chosen = int(input(txt))
    return chosen
