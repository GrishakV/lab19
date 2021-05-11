#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def color(event):
    if event.widget['bg'] == "#ff0000":
        e1.delete(0, END)
        l1['text'] = "Красный"
        e1.insert(0, "#ff0000")
    elif event.widget['bg'] == "#ff9900":
        e1.delete(0, END)
        l1['text'] = "Оранжевый"
        e1.insert(0, "#ff9900")
    elif event.widget['bg'] == "#ffff00":
        e1.delete(0, END)
        l1['text'] = "Желтый"
        e1.insert(0, "#ffff00")
    elif event.widget['bg'] == "#33cc33":
        e1.delete(0, END)
        l1['text'] = "Зеленый"
        e1.insert(0, "#33cc33")
    elif event.widget['bg'] == "#6699ff":
        e1.delete(0, END)
        l1['text'] = "Голубой"
        e1.insert(0, "#6699ff")
    elif event.widget['bg'] == "#0000ff":
        e1.delete(0, END)
        l1['text'] = "Синий"
        e1.insert(0, "#0000ff")
    elif event.widget['bg'] == "#cc00cc":
        e1.delete(0, END)
        l1['text'] = "Филетовый"
        e1.insert(0, "#cc00cc")


root = Tk()

l1 = Label(width=20)
e1 = Entry(width=20)
b1 = Button(width=20, bg="#ff0000")
b2 = Button(width=20, bg="#ff9900")
b3 = Button(width=20, bg="#ffff00")
b4 = Button(width=20, bg="#33cc33")
b5 = Button(width=20, bg="#6699ff")
b6 = Button(width=20, bg="#0000ff")
b7 = Button(width=20, bg="#cc00cc")

b1.bind('<Button-1>', color)
b2.bind('<Button-1>', color)
b3.bind('<Button-1>', color)
b4.bind('<Button-1>', color)
b5.bind('<Button-1>', color)
b6.bind('<Button-1>', color)
b7.bind('<Button-1>', color)

l1.pack()
e1.pack()
b1.pack(padx=1, pady=1)
b2.pack(padx=1, pady=1)
b3.pack(padx=1, pady=1)
b4.pack(padx=1, pady=1)
b5.pack(padx=1, pady=1)
b6.pack(padx=1, pady=1)
b7.pack(padx=1, pady=1)
root.mainloop()
