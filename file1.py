#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def openfile():
    filename = e1.get()
    with open(filename, 'r') as s:
        t1.insert(0.0, s.read())


def save():
    date = t1.get(0.0, 'end')
    print(date)
    filename = e1.get()
    with open(filename, 'w') as f:
        f.write(date)


root = Tk()

e1 = Entry(width=20)
t1 = Text()
b1 = Button(width=20, text="OPEN")
b2 = Button(width=20, text="SAVE")

b1.config(command=openfile)
b2.config(command=save)

e1.grid(row=0, column=0, sticky=W+E, padx=3)
b1.grid(row=0, column=1, sticky=E)
b2.grid(row=0, column=2, sticky=W)
t1.grid(row=1, column=0, columnspan=3)

root.mainloop()
