#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def sel():
    s = str(var.get())
    l1.config(text=s)


root = Tk()

var = IntVar()
rb1 = Radiobutton(text='Вася', indicatoron=0, width=15, height=3, state=ACTIVE, variable=var,
                 value='89097525555', command=sel)
rb2 = Radiobutton(text='Петя', indicatoron=0, width=15, height=3, state=ACTIVE, variable=var,
                 value='87512456635', command=sel)
rb3 = Radiobutton(text='Маша', indicatoron=0, width=15, height=3, state=ACTIVE, variable=var,
                 value='84652487598', command=sel)
l1 = Label(width=30, bg="blue", height=11)

rb1.grid(row=0, column=0)
rb2.grid(row=1, column=0)
rb3.grid(row=2, column=0)
l1.grid(row=0, column=1, rowspan=3)

root.mainloop()
