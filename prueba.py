from tkinter import *
from tkinter import ttk
from datetime import *
from tkinter import messagebox
import time
import calendar
import threading
from threading import Timer
import os
import sys
from functools import partial

class prueba:

    def __init__(self):

        self.root = Tk()
        self.root.title("PRUEBAS")
        self.root.geometry('600x300+500+200')

        self.imprime = ttk.Label(self.root)
        self.imprime.grid(row=3, column=0)

        def añadir():

            self.pestaña = ttk.Frame(self.cliente)
            self.cliente.add(self.pestaña, text='CLIENTE')

            self.nombre = ttk.Entry(self.pestaña)
            self.entries.append(self.nombre)
            self.nombre.grid(row=1, column=0)

        def conseguido():
            self.imprime['text'] = ", ".join(
                entry.get() for entry in self.entries)

        self.cliente = ttk.Notebook(self.root)
        self.cliente.grid(row=0, column=0)

        self.pestaña = ttk.Frame(self.cliente)
        self.cliente.add(self.pestaña, text='CLIENTE')

        self.nombre = ttk.Entry(self.pestaña)
        self.entries = [self.nombre]
        self.nombre.grid(row=0, column=0)

        self.añade = ttk.Button(self.root, text='AÑADE', command=añadir)
        self.añade.grid(row=1, column=0)

        self.conseguir = ttk.Button(self.root, text='CONSIGE', command=conseguido)
        self.conseguir.grid(row=2, column=0)





        self.root.mainloop()

def main():
    my_app = prueba()

if __name__ == '__main__':
    main()
