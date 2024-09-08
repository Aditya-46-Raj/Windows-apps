from tkinter import *
from textblob import TextBlob

win=Tk()
win.title('Spelling Checker')
win.geometry("700x400")
win.config(bg="#dae6f6")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(win,text="Correct text is :",font=("poppins",20),bg="#dae6f6", fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading=Label(win,text="Spelling Checker",font=("Helvetica",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

enter_text=Entry(win,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(win,text="Check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()

spell=Label(win,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)


win.mainloop()