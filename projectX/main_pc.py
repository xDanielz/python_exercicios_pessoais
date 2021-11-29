from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import Font
from trregistermanager import *

config = {"host": "127.0.0.1",
          "user": "hunter",
          "password": "gonxkillua",
          "database": "transporterodriguesdb"}
register_man = TrRegisterManager(**config)


def recorder():
    values = list()
    value_error = list()
    for name, val in reg_dict_values.items():
        val = str(val.get())
        if val == '' and name != "OBSERVAÇÕES":
            value_error.append(name)
            continue

        if name in ("KM", "PREÇO COMBS", "VALOR"):
            try:
                val = float(val)
            except ValueError:
                value_error.append(name)
                continue
        values.append(val)

    if not value_error:
        try:
            register_man.add_register(values)
        except Exception as exc:
            messagebox.showerror(title="DB ERROR", message=exc)
        else:
            #register_man.exit()
            for val in reg_dict_values:
                if val not in veic_driv.keys():
                    reg_dict_values[val].delete(0, END)
            messagebox.showinfo(title=":)", message="DADOS REGISTRADOS COM SUCESSO")
    else:
        messagebox.showerror(title=":(", message=f"SEGUINTE/S CAMPO/S ESTÃO INCORRETOS:\n {', '.join(value_error)}")


app = Tk()
app.title("Registro de fretes")
app.geometry('350x350')
initial_config = {'master': 'regtab', 'font': 'fnt', 'anchor': 'CENTER'}
fnt = Font(size=10, weight="bold")


nb = ttk.Notebook(app)
nb.place(x=0, y=0, width=1000, height=500)

# registry part interface
regtab = Frame(nb, background="white")
nb.add(regtab, text="REGISTRAR")

column_list = ("ID", "MOTORISTA", "VEICULO", "ORIGEM", "DESTINO", "KM",
               "PREÇO COMBS", "VALOR", "OBSERVAÇÕES")
veic_driv = {"MOTORISTA": ("LUCAS", "MATHEUS", "CLAUDIO"), "VEICULO": ("F350", "D10", "708E")}

reg_dict_values = {t: StringVar() if t in veic_driv.keys() else Entry(regtab) for t in column_list}
y = 10
for t in column_list:
    Label(regtab, text=t, font=fnt, anchor=CENTER, background="#ADD8E6").place(x=55, y=y, width=120, height=20)
    if t in veic_driv.keys():
        reg_dict_values[t].set(veic_driv[t][0])
        OptionMenu(regtab, reg_dict_values[t], *veic_driv[t]).place(x=180, y=y, width=120, height=23)
    else:
        reg_dict_values[t].place(x=180, y=y, width=120, height=20)
    y += 25
reg_buttom = Button(regtab, text="REGISTRAR", font=fnt, command=recorder)
reg_buttom.place(x=115, y=250, width=100, height=30)


# Interface of the part of viewing the records
def show_regs():
    global numbreg
    numbreg = len(register_man.get_records())
    form_values = register_man.get_records()
    chosen_reg = form_values[vop.get()]
    y = 40
    for reg in chosen_reg:
        if 'datetime' in repr(reg):
            reg = str(reg.time())
        Label(view_logs, text=reg, anchor=CENTER, background="#ADD8E6").place(x=180, y=y, width=80, height=20)
        y += 25


view_logs = Frame(nb, background="white")
nb.add(view_logs, text="VISUALIZAR")

data_labels_left = ["HORA", "Nº"] + list(column_list[:-3]) + ["COMBS", "VALOR", "OBS"]

# Show the names of columns
y = 40
for col in data_labels_left:
    Label(view_logs, text=col, font=fnt, anchor=CENTER, background="#ADD8E6").place(x=90, y=y, width=80, height=20)
    y += 25

# display as corresponding information as columns
dates = register_man.get_date()
vop = IntVar()
vop.set(0)
show_regs()
OptionMenu(view_logs, vop, *range(12)).place(x=90, y=15, width=45, height=20)
Button(view_logs, text="IR", command=show_regs).place(x=180, y=15, width=40, height=20)

app.mainloop()
