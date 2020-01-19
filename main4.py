# import tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk


from bd_sqlite import *

from datetime import date
from datetime import datetime

import tkinter as tk

from PIL import Image, ImageTk
import os
import cv2

global labelA
global v_placa
global placa
global admin
global instancia
placa='x'

def abrir_admin():
        #se abre una ventana para gestionar
        admin = tk.Toplevel(master)
        global b2
        b2 = AdminP(admin)




class AdminP(ttk.Frame):

    def __init__(self,admin, *args, **kwargs):
        super().__init__(admin,*args, **kwargs)

        admin.title("Panel de pestañas en Tcl/Tk")

        self.notebook = ttk.Notebook(self,  width="600", height="450")

        self.Login_frame = LoginFrame(self.notebook)
        self.notebook.add(
            self.Login_frame, text="Login", padding=10)

        self.Admin_frame = AdminFrame(self.notebook)
        self.notebook.add(
            self.Admin_frame, text="Admin", padding=10)


        # self.Exit_frame = ExitFrame(self.notebook)
        # self.notebook.add(self.Exit_frame,text="Salir", padding=10)

        self.notebook.tab(self.Login_frame, state='normal')
        self.notebook.tab(self.Admin_frame, state='hidden')
        # self.notebook.tab(self.About_frame, state='hidden')
        # self.notebook.tab(self.Exit_frame, state='hidden')

        self.notebook.pack(padx=10, pady=10)
        self.pack( expand="True")


class LoginFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label1 = ttk.Label(self, text="Introduzca nombre de usuario y contraseña").pack()
        self.label2 = ttk.Label(self, text="").pack()

        self.label3 = ttk.Label(self, text="Nombre usuario * ").pack()
        self.usuario = ttk.Entry(self)
        self.usuario.pack()

        self.label4 = ttk.Label(self, text="").pack()

        self.labelpass = ttk.Label(self, text="Contraseña * ").pack()
        self.clave = ttk.Entry(self,  show= '*')
        self.clave.pack()
        self.label5 = ttk.Label(self, text="").pack()

        self.greet_button = ttk.Button(
            self, text="Ingresar", command=self.verifica_login)
        self.greet_button.pack()

        self.greet_label = ttk.Label(self)
        self.greet_label.pack()

    def verifica_login(self):

        usuario1 = self.usuario.get()
        clave1 = self.clave.get()
        arr = array([usuario1,clave1])
        con = sql_connection()
        values= verificar_usuario(con,arr)
        if (len(values)==1):
            b2.notebook.tab(b2.Admin_frame, state='normal')
            b2.notebook.tab(b2.Login_frame, state='disabled')
            b2.notebook.select(b2.Admin_frame)
        else:
            print("error con loggeo")


class AdminFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ###################################################
        con = sql_connection()
        productos= listar_productos(con)
        usuarios= listar_usuarios(con)
        eventos= listar_eventos_hoy(con)
        ####################################################
        t_productos = Label(self, text = "Productos: ", relief="groove")
        t_productos.grid(row = 0, column = 0)
        btn_nuevoP = Button(self, text = "Nuevo")
        btn_borrarP = Button(self, text = "Borrar")
        btn_editarP = Button(self, text = "Editar")

        btn_nuevoP.grid(row = 0, column = 1)
        btn_borrarP.grid(row = 0, column = 2)
        btn_editarP.grid(row = 0, column = 3)

        v_producto =tk.Listbox(self, height=len(productos),width=30)
        v_producto.insert(0, *productos)
        v_producto.grid(row = 2, column = 1, columnspan = 4,pady = 20)

        ##############################################
        t_usuarios = Label(self, text = "Usuarios: ", relief="groove")
        t_usuarios.grid(row = 4, column = 0)
        btn_nuevoU = Button(self, text = "Nuevo")
        btn_borrarU = Button(self, text = "Borrar")
        btn_editarU = Button(self, text = "Editar")

        btn_nuevoU.grid(row = 4, column = 1)
        btn_borrarU.grid(row = 4, column = 2)
        btn_editarU.grid(row = 4, column = 3)

        v_usuario =tk.Listbox(self, height=len(usuarios),width=30)
        v_usuario.insert(0, *usuarios)
        v_usuario.grid(row = 6, column = 1, columnspan = 4,pady = 20)

        ###############################################################


        t_eventos = Label(self, text = "Eventos: ", relief="groove")
        t_eventos.grid(row = 9, column = 0, sticky = W, pady = 2)
        btn_borrarE = Button(self, text = "Borrar")
        btn_editarE = Button(self, text = "Editar")

        btn_borrarU.grid(row = 9, column = 1, sticky = E)
        btn_editarU.grid(row = 9, column = 2, sticky = E)

        v_evento =tk.Listbox(self, height=len(eventos),width=30)
        v_evento.insert(0, *eventos)
        v_evento.grid(row = 11, column = 1, columnspan=4,pady = 20)


class Application(ttk.Frame):

        def tomar_foto(self):
                print("Proceso Iniciado")
                # print(self.peso)
                #######################################################
                cap = cv2.VideoCapture(0)
                leido, frame = cap.read()
                if leido == True:
                	cv2.imwrite("foto.png", frame)
                	print("Foto tomada correctamente")
                else:
                	print("Error al acceder a la cámara")
                """
                	Finalmente liberamos o soltamos la cámara
                """
                cap.release()

                img = Image.open("foto.png")
                image = img.resize((600,450), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                labelA = Label(master, image=photo)
                labelA.image = photo
                labelA.grid(row=0, column=4,  columnspan = 2, rowspan = 5, padx = 3, pady = 4)
                #######################################################
                fecha_in=datetime.now()
                peso_neto=self.peso
                producto=int(self.v_producto.get())
                placa = 'msd666'
                miPack = array([placa, fecha_in, peso_neto, producto])
                con = sql_connection()
                res= insert_evento(con,miPack)

                # values=["Arroz","Platano","Yuca","Papa","Mazorca"]
                self.v_placa.config(text=placa)

                # v_placa = Label(master, text = placa)
                # v_placa.grid(row = 2, column = 1, sticky = W, pady = 2)

        def __init__(self, master):
                super().__init__(master)
                master.title("panel")

                fecha = date.today()
                #Fecha actual
                now = datetime.now()
                #formato hora
                hora = now.strftime('%H:%M:%S')
                #print('Date is:'+ format)
                self.peso = 12
                # con = sql_connection()
                # values= listar_productos(con)
                # values=["Arroz","Platano","Yuca","Papa","Mazorca"]

                # this will create a label widget
                t_fecha = Label(master, text = "Fecha: ",borderwidth=2, relief="groove")
                t_hora = Label(master, text = "Hora: ",borderwidth=2, relief="groove")
                t_placa = Label(master, text = "Placa: ",borderwidth=2, relief="groove")
                t_peso = Label(master, text = "Peso: ",borderwidth=2, relief="groove")
                t_producto = Label(master, text = "Producto: ",borderwidth=2, relief="groove")

                # grid method to arrange labels in respective
                # rows and columns as specified
                t_fecha.grid(row = 0, column = 0, sticky = W, padx = 5)
                t_hora.grid(row = 1, column = 0, sticky = W, padx = 5)
                t_placa.grid(row = 2, column = 0, sticky = W, padx = 5)
                t_peso.grid(row = 3, column = 0, sticky = W, padx = 5)
                t_producto.grid(row = 4, column = 0, sticky = W, padx = 5)

                # this will create a label widget
                self.v_fecha = Label(master, text = fecha)
                self.v_hora = Label(master, text = hora)
                self.v_peso = Label(master, text = self.peso)
                self.v_placa = Label(master, text = placa)


                self.v_producto = Entry(master)

                # v_producto =tk.Listbox(master, height=len(values))
                # v_producto.insert(0, *values)

                # grid method to arrange labels in respective
                # rows and columns as specified

                self.v_fecha.grid(row = 0, column = 1, sticky = W, pady = 2)
                self.v_hora.grid(row = 1, column = 1, sticky = W, pady = 2)
                self.v_placa.grid(row = 2, column = 1, sticky = W, pady = 2)
                self.v_peso.grid(row = 3, column = 1, sticky = W, pady = 2)
                self.v_producto.grid(row = 4, column = 1,sticky = W, pady = 2)

                # adding image (remember image should be PNG and not JPG)
                # image = PhotoImage(file = "camion.png")
                # img1 = img.subsample(2, 2)


                img = Image.open("foto.png")
                image = img.resize((600,450), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)

                labelA = Label(master, image=photo)
                labelA.config(image=photo)
                labelA.image = photo # this line need to prevent gc
                labelA.grid(row=0, column=4,  columnspan = 2, rowspan = 5, padx = 3, pady = 4)

                # setting image with the help of label
                # Label(master, image = img).grid(row = 0, column = 3)

                # button widget
                b2 = Button(master, text = "Administración",command=abrir_admin)

                # arranging button widgets
                b2.grid(row = 6, column = 5, sticky = E)

                # button widget

                btnFoto = Button(master, text = "foto",command=self.tomar_foto)

                # arranging button widgets
                btnFoto.grid(row = 6, column = 0, columnspan = 2,  padx = 100, ipadx = 10,  pady = 1, sticky = E)


master = tk.Tk()
app=Application(master)
# infinite loop which can be terminated
# by keyboard or mouse interrupt
app.mainloop()
