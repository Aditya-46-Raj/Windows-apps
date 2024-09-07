from tkinter import *
from tkinter import filedialog

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)


win=Tk()
win.geometry("600x600")
win.title("Adi's Notepad")
win.config(bg='lightblue')
win.resizable(False,False)

b1=Button(win,width='20',height='2',text='save file',bg='lightgreen',command=save_file).place(x=100,y=5)
b2=Button(win,width='20',height='2',text='open file',bg='lightgreen',command=open_file).place(x=300,y=5)

entry=Text(win,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)


win.mainloop()