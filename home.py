import tkinter as tk
from tkinter import ttk

from datetime import date
from datetime import datetime

from tkinter import *
from tkinter.ttk import *

#Día actual
fecha = date.today()

#Fecha actual
now = datetime.now()

#formato hora
hora = now.strftime('%H:%M:%S')

#print('Date is:'+ format)

placa = 'MAZ123'
producto = 'Arroz'

class HomeFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label_text_fecha = ttk.Label(self, text='Fecha: ')
        self.label_fecha = ttk.Label(self, text=fecha)

        self.label_text_fecha.grid(row = 0, column = 0, sticky = W, pady = 2)
        self.label_fecha.grid(row = 1, column = 0, sticky = W, pady = 2)

        # self.label_text_hora = ttk.Label(self, text='Hora: ').pack()
        # self.label_hora = ttk.Label(self, text=hora).pack()
        #
        # self.label_text_placa = ttk.Label(self, text='Placa: ').pack()
        # self.label_placa = ttk.Label(self, text=placa).pack()
        #
        # self.label_text_producto = ttk.Label(self, text='Producto: ').pack()
        # self.label_producto = ttk.Label(self, text=producto).pack()

        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()
