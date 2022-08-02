import math
from tkinter import *

# root widget, has to happen before anything else
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0, "Enter Your Name: ")

# FUNCTIONS
def button_click(number):
    e.insert(END, number)
    current = e.get()

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global math_type
    math_type = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global f_num
    global math_type
    math_type = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num
    global math_type
    math_type = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num
    global math_type
    math_type = "division"
    f_num = int(first_number)
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math_type == "addition":
        e.insert(0, f_num + int(second_number))
    if math_type == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math_type == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math_type == "division":
        e.insert(0, f_num / int(second_number))

    

# Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
button_plus = Button(root, text="+", padx=39, pady=20, command=add)
button_equal = Button(root, text="=", padx=99, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=88, pady=20, command=clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=42, pady=20, command=divide)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


# main loop
root.mainloop()

