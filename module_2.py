#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


class Block:
    def __init__(self, master):
        self.ent = Entry(master, width=20)
        self.but = Button(
            master,
            text="Преобразовать"
        )
        self.lab = Label(
            master,
            width=20,
            bg='black',
            fg='white'
        )
        self.but['command'] = self.str_to_sort
        self.ent.pack()
        self.but.pack()
        self.lab.pack()

    def str_to_sort(self):
        s = self.ent.get()
        s = s.split()
        s.sort()
        self.lab['text'] = ' '.join(s)


root = Tk()

first_block = Block(root)

root.mainloop()
