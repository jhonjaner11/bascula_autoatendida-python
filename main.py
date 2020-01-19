#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import os

class Application(ttk.Frame):

    def __init__(self, main_window):
        pestas_color="DarkGrey"
        pestas_color2="Blue"
        super().__init__(main_window)
        main_window.title("Panel Demo")

        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self)

        # Crear el contenido de cada una de las pestañas.

        # login:

        global verifica_usuario
        global verifica_clave

        verifica_usuario = ''
        verifica_clave = ''

        self.web_label = ttk.Label(self.notebook,
                               text="Introduzca nombre de usuario y contraseña")

        self.web_label = ttk.Label(self.notebook, text="Nombre usuario * ")
        self.web_label = ttk.Entry(self.notebook, textvariable=verifica_usuario)

        self.web_label = ttk.Label(self.notebook, text="")
        self.web_label = ttk.Label(self.notebook, text="Contraseña * ")
        self.web_label = ttk.Label(self.notebook, text="")
        self.web_label = ttk.Button(self.notebook, text="Acceder")
        self.web_label = ttk.Entry(self.notebook, textvariable=verifica_clave, show= '*')

        self.forum_label = ttk.Label(self.notebook,
                                          text="foro.recursospython.com")

        # Añadirlas al panel con su respectivo texto.
        self.notebook.add(self.web_label, text="Login", padding=20)
        self.notebook.add(self.forum_label, text="Foro", padding=20)

        self.notebook.pack(padx=10, pady=10)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
