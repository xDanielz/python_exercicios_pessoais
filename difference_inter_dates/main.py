from datetime import datetime
from simpledate import SimpleDate
from tkinter import messagebox
from tkinter import *
from tkinter.font import Font


def difference():
    date1 = entry_from.get()
    date2 = entry_to.get()
    try:
        date1 = datetime.strptime(date1, '%d/%m/%Y')
        date2 = datetime.strptime(date2, '%d/%m/%Y')
    except ValueError:
        messagebox.showerror('Error', 'Formato de data errado')
        return
    date1 = SimpleDate.fromdatetime(date1)
    date2 = SimpleDate.fromdatetime(date2)
    info = {'years': 'ANOS', 'months': 'MESÊS', 'weeks': 'SEMANAS', 'days': 'DIAS', 'total_days': 'DIAS TOTAIS'}
    y = 255
    for k, v in date1.difference_inter_dates(date2).items():
        if v != 0:
            Label(text=f'{info[k]}: {v}', font=Font(size=15, weight='bold')).place(x=100, y=y, width=200, height=30)
            y += 25


app = Tk()
app.geometry('400x400')


lb_title = Label(app, text='CALCULADORA DE DATA', font=Font(size=20, weight='bold'))
lb_title.place(x=20, y=25, width=350, height=30)

lb_from = Label(app, text='DE', font=Font(size=15, weight='bold'))
entry_from = Entry(app)
lb_from.place(x=150, y=70, width=80, height=30)
entry_from.place(x=135, y=100, width=120, height=30)

lb_to = Label(app, text='ATÉ', font=Font(size=15, weight='bold'))
entry_to = Entry(app)
lb_to.place(x=150, y=140, width=80, height=30)
entry_to.place(x=135, y=170, width=120, height=30)

lb_difference = Button(app, text='DIFERENÇA', font=Font(size=15, weight='bold'), command=difference)
lb_difference.place(x=135, y=220, width=120, height=30)


app.mainloop()
