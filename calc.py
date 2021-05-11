#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def add(event):
    try:
        inte1 = e1.get()
        inte2 = e2.get()
        res = float(inte1) + float(inte2)
        l1['text'] = res
    except:
        l1['text'] = 'АШИПКА'


def sub(event):
    try:
        inte1 = e1.get()
        inte2 = e2.get()
        res = float(inte1) - float(inte2)
        l1['text'] = res
    except:
        l1['text'] = 'АШИПКА'


def mult(event):
    try:
        inte1 = e1.get()
        inte2 = e2.get()
        res = float(inte1) * float(inte2)
        l1['text'] = res
    except:
        l1['text'] = 'АШИПКА'


def div(event):
    try:
        inte1 = e1.get()
        inte2 = e2.get()
        res = float(inte1) / float(inte2)
        l1['text'] = res
    except:
        l1['text'] = 'АШИПКА'


root = Tk()

e1 = Entry(width=20)
e2 = Entry(width=20)
b1 = Button(width=5, height=2,
            bg="red", text="+")
b2 = Button(width=5, height=2,
            bg="green", text="-")
b3 = Button(width=5, height=2,
            bg="yellow", text="*")
b4 = Button(width=5, height=2,
            bg="blue", text="÷")
l1 = Label(width=20, height=2, text="")

b1.bind('<Button-1>', add)
b2.bind('<Button-1>', sub)
b3.bind('<Button-1>', mult)
b4.bind('<Button-1>', div)

e1.grid(row=0, column=0, columnspan=4)
e2.grid(row=1, column=0, columnspan=4)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=2, column=3)
l1.grid(row=3, column=0, columnspan=4)

root.mainloop()
