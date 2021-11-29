from tkinter import *
import tkinter.font as tkfont


def calc4travel(fuelprice: float, averagecons: float, km: float) -> float:
    """
    Função para calcular o valor gasto para uma viagem de X Km (ida e volta).
    fuelprice: representa o preço do combustivel;
    averagecons: consumo médio do veiculo;
    km: distância em km.
    Retorna o valor em reais da quantia aproximada que será gasta
    em combustivel.
    """
    return (km/averagecons*fuelprice)*2


def fretevalor(km: float, val4km: float) -> float:
    """
    Função para calcular um preço sugerido para um frete.
    km: distância em km;
    val4km: preço cobrado por km rodado.
    Retorna o valor sugerido baseado na quantida cobrado por km.
    """
    return val4km*km*2


def comremcon4float(n: str) -> float:
    """"Substitui a virgula por ponto e converte em float"""
    return float(str(n).replace(',', '.'))


def aux_calc_frete():
    font_size = tkfont.Font(size=15)
    result = str()
    try:
        average_con = comremcon4float(tb_averageCon.get())
        distance = comremcon4float(tb_distance.get())
        fuel_price = comremcon4float(tb_conValue.get())
        con_value = comremcon4float(tb_distValue.get())
        valorfrete = fretevalor(distance, con_value) - calc4travel(fuel_price, average_con, distance)
        result = f"RESULTADO: {valorfrete:.2f}R$"
    except:
        result = "Dados incorretos e \nou Faltam dado/s"
    finally:
        tb_distance.delete(0, END)
        tb_averageCon.delete(0, END)
        tb_conValue.delete(0, END)
        tb_distValue.delete(0, END)
        Label(text=result, font=font_size, anchor=W).place(x=10, y=240, width=250, height=60)


app = Tk()

app.title("Auxiliador de calculo para fretes")
app.geometry("300x350")
Label(text="CONSUMO MÉDIO DO VEICULO").place(x=10, y=10, width=200, height=20)
tb_averageCon = Entry(app)
tb_averageCon.place(x=15, y=35, width=100, height=20)
Label(text="DISTÂNCIA A PERCORRER EM Km/h", anchor=W).place(x=10, y=55, width=250, height=20)
tb_distance = Entry(app)
tb_distance.place(x=15, y=75, width=100, height=20)
Label(text="PREÇO COBRADO POR Km", anchor=W).place(x=10, y=95, width=200, height=20)
tb_distValue = Entry(app)
tb_distValue.place(x=15, y=115, width=100, height=20)
Label(text="PREÇO DO COMBUSTIVEL", anchor=W).place(x=10, y=135, width=200, height=20)
tb_conValue = Entry(app)
tb_conValue.place(x=15, y=155, width=100, height=20)
Button(app, text="Calcular", command=aux_calc_frete).place(x=15, y=185, width=100, height=35)

app.mainloop()
