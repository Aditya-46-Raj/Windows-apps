from tkinter import *

# Function to update expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    win = Tk()
    win.configure(background="black")
    win.title("Adi's Calculator")
    win.geometry("345x410")
    win.minsize(345, 410)
    win.maxsize(345, 410)

    expression = ""
    equation = StringVar()

    expression_field = Entry(win, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=110, ipady=24)

    button1 = Button(win, text=' 1 ', fg='white', bg='#333333',font=8, command=lambda: press(1), height=3, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(win, text=' 2 ', fg='white', bg='#333333',font=8, command=lambda: press(2), height=3, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(win, text=' 3 ', fg='white', bg='#333333',font=8, command=lambda: press(3), height=3, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(win, text=' 4 ', fg='white', bg='#333333',font=8, command=lambda: press(4), height=3, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(win, text=' 5 ', fg='white', bg='#333333',font=8, command=lambda: press(5), height=3, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(win, text=' 6 ', fg='white', bg='#333333',font=8, command=lambda: press(6), height=3, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(win, text=' 7 ', fg='white', bg='#333333',font=8, command=lambda: press(7), height=3, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(win, text=' 8 ', fg='white', bg='#333333',font=8, command=lambda: press(8), height=3, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(win, text=' 9 ', fg='white', bg='#333333',font=8, command=lambda: press(9), height=3, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(win, text=' 0 ', fg='white', bg='#333333',font=8, command=lambda: press(0), height=3, width=7)
    button0.grid(row=5, column=0)

    plus = Button(win, text=' + ', fg='white', bg='#333333',font=8, command=lambda: press("+"), height=3, width=7)
    plus.grid(row=2, column=3)

    minus = Button(win, text=' - ', fg='white', bg='#333333',font=8, command=lambda: press("-"), height=3, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(win, text=' x ', fg='white', bg='#333333',font=8, command=lambda: press("*"), height=3, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(win, text=' / ', fg='white', bg='#333333',font=8, command=lambda: press("/"), height=3, width=7)
    divide.grid(row=5, column=3)

    equal = Button(win, text=' = ', fg='white', bg='#333333',font=8, command=equalpress, height=3, width=7)
    equal.grid(row=5, column=2)

    clear = Button(win, text='Clear', fg='white', bg='#333333',font=8, command=clear, height=3, width=7)
    clear.grid(row=5, column='1')

    win.mainloop()
