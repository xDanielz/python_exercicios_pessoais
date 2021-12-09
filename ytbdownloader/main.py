from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog
from ytbdownloader import *
from threading import Thread


def choise_path():
    global savelocal
    savelocal = str(filedialog.askdirectory())
    label_saveWhere.config(text=savelocal[savelocal.rfind('/')+1:], anchor=CENTER)


def download():
    url = tb_url.get()
    op = option.get()

    try:
        yt = YtbDownloader()
        if chkvalue.get():
            yt.download_playlist(url=url, savelocal=savelocal, tomp3=op)
        else:
            if op:
                yt.download_and_convertmp3(url=url, savelocal=savelocal)
            else:
                yt.download_video(url=url, savelocal=savelocal)

    except Exception as exc:
        print(exc)
        messagebox.showerror(title=":(", message="HOUVE UM PROBLEMA, VERIFIQUE A URL DO VIDEO")
    else:
        messagebox.showinfo(title=":)", message="BAIXADO COM SUCESSO")
    tb_url.delete(0, END)


app = Tk()
savelocal = None
option = BooleanVar()
app.geometry("400x300")
app.configure(background='orange')
font = Font(size=10, weight='bold')

Label(app, text="YOUTUBER DOWNLOADER", font=font).place(x=100, y=5, height=25, width=200)

Label(app, text="URL DO VIDEO: ", font=font).place(x=140, y=35, height=25, width=120)
tb_url = Entry(app)
tb_url.place(x=75, y=65, height=25, width=250)

Label(app, text="PLAYLIST", font=font).place(x=140, y=95, width=90, height=25)
chkvalue = BooleanVar()
chkvalue.set(False)
chkbuttom = Checkbutton(app, var=chkvalue)
chkbuttom.place(x=235, y=95, width=30, height=25)

Button(app, text="DIRETORIO:", command=choise_path, font=font).place(x=75, y=125, height=25, width=120)
label_saveWhere = Label(app, text='', font=font, anchor=W)
label_saveWhere.place(x=200, y=125, height=25, width=125)

Rb1 = Radiobutton(app, text="MÚSICA(MP3)", background='white', font=font, variable=option, value=True)
Rb1.place(x=50, y=170, height=25, width=120)

Rb2 = Radiobutton(app, text="VÍDEO(MP4)", font=font, background='white', variable=option, value=False)
Rb2.place(x=230, y=170, height=25, width=120)

#task = Thread(target=download)
Button(app, text="BAIXAR", font=font, command=download).place(x=140, y=220, height=25, width=120)

app.mainloop()
