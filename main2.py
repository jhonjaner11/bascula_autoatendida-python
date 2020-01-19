#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from home import HomeFrame

class ExitFrame(ttk.Frame):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.greet_button = ttk.Button(
        self, text="Salir", command=self.cerrar_sesion)
        self.greet_button.pack()
    def cerrar_sesion(self):
        app.notebook.tab(app.Login_frame, state='normal')
        app.notebook.tab(app.Home_frame, state='hidden')
        app.notebook.tab(app.About_frame, state='hidden')
        app.notebook.tab(app.Exit_frame, state='hidden')




class LoginFrame(ttk.Frame):
    global verifica_usuario
    global verifica_clave

    global entrada_login_usuario
    global entrada_login_clave

    verifica_usuario = ''
    verifica_clave = ''

    entrada_login_usuario = ''
    entrada_login_clave = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label1 = ttk.Label(self, text="Introduzca nombre de usuario y contraseña").pack()
        self.label2 = ttk.Label(self, text="").pack()

        self.label3 = ttk.Label(self, text="Nombre usuario * ").pack()
        self.usuario = ttk.Entry(self, textvariable=verifica_usuario)
        self.usuario.pack()

        self.label4 = ttk.Label(self, text="").pack()

        self.labelpass = ttk.Label(self, text="Contraseña * ").pack()
        self.clave = ttk.Entry(self, textvariable=verifica_clave, show= '*').pack()
        self.label5 = ttk.Label(self, text="").pack()

        self.greet_button = ttk.Button(
            self, text="Ingresar", command=self.verifica_login)
        self.greet_button.pack()

        self.greet_label = ttk.Label(self)
        self.greet_label.pack()

    def verifica_login(self):
        self.greet_label["text"] = \
            "¡Hola, {}!".format(self.usuario.get())
        app.notebook.tab(app.Login_frame, state='disabled')
        app.notebook.tab(app.Home_frame, state='normal')
        app.notebook.tab(app.About_frame, state='normal')
        app.notebook.tab(app.Exit_frame, state='normal')

        app.notebook.select(app.Home_frame)

class AboutFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Visitanos en recursospython.com y "
                              "foro.recursospython.com.")
        self.label.pack()

        self.web_button = ttk.Button(self, text="Visitar web")
        self.web_button.pack(pady=10)

        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()

# class HomeFrame(ttk.Frame):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.label = ttk.Label(self)
#         self.label["text"] = ("Visitanos en recursospython.com y "
#                               "foro.recursospython.com.")
#         self.label.pack()
#
#         self.web_button = ttk.Button(self, text="Cerrar Sesion", command=self.cerrar_sesion)
#         self.web_button.pack(pady=10)
#
#         self.forum_button = ttk.Button(self, text="Visitar foro")
#         self.forum_button.pack()
#
#     def cerrar_sesion(self):
#         app.notebook.tab(app.Login_frame, state='normal')
#         app.notebook.tab(app.Home_frame, state='hidden')
#         app.notebook.tab(app.About_frame, state='hidden')
#

class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Panel de pestañas en Tcl/Tk")

        self.notebook = ttk.Notebook(self,  width="1200", height="600")

        self.Login_frame = LoginFrame(self.notebook)
        self.notebook.add(
            self.Login_frame, text="Login", padding=10)

        self.Home_frame = HomeFrame(self.notebook)
        self.notebook.add(
            self.Home_frame, text="Home", padding=10)

        self.About_frame = AboutFrame(self.notebook)
        self.notebook.add(self.About_frame,text="Acerca de", padding=10)

        self.Exit_frame = ExitFrame(self.notebook)
        self.notebook.add(self.Exit_frame,text="Salir", padding=10)

        self.notebook.tab(self.Login_frame, state='normal')
        self.notebook.tab(self.Home_frame, state='hidden')
        self.notebook.tab(self.About_frame, state='hidden')
        self.notebook.tab(self.Exit_frame, state='hidden')

        self.notebook.pack(padx=10, pady=10)
        self.pack( expand="True")



main_window = tk.Tk()
main_window.geometry("650x350")

global app
app = Application(main_window)
app.mainloop()
