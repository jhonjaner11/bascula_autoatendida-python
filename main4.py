# import tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk


from bd_sqlite import *
from tabla import *
from reconocimiento import *

from datetime import date
from datetime import datetime

import tkinter as tk

from PIL import Image, ImageTk
import os
import cv2
import csv


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

# def reconocer_placa(foto):
#     aux = "La foto analizada es: "+foto
#     print(aux)
#     placa = "PGL420"
#     return placa

class AdminP(ttk.Frame):

    def __init__(self,admin, *args, **kwargs):
        super().__init__(admin,*args, **kwargs)

        admin.title("Panel de pestañas en Tcl/Tk")


        self.notebook = ttk.Notebook(self,  width="800", height="600")

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
        eventos2= listar_eventos_hoy(con)
        eventos.insert(0, ['placa','fecha_in','fecha_out','peso_in','peso_out','peso_neto','producto','id'])
        ####################################################
        t_productos = Label(self, text = "Productos: ", relief="groove")
        t_productos.grid(row = 0, column = 0)
        btn_nuevoP = Button(self, text = "Nuevo", command=self.abrir_producto)
        btn_borrarP = Button(self, text = "Borrar", command=self.borrar_producto)
        btn_editarP = Button(self, text = "Editar", command=self.editar_producto)

        btn_nuevoP.grid(row = 0, column = 1)
        btn_borrarP.grid(row = 0, column = 2)
        # btn_editarP.grid(row = 0, column = 3)

        self.v_producto =tk.Listbox(self, height=len(productos),width=30)
        self.v_producto.insert(0, *productos)
        self.v_producto.grid(row = 2, column = 1, columnspan = 4,pady = 20)



        ##############################################
        t_usuarios = Label(self, text = "Usuarios: ", relief="groove")
        t_usuarios.grid(row = 4, column = 0)
        btn_nuevoU = Button(self, text = "Nuevo", command=self.abrir_usuario)
        btn_borrarU = Button(self, text = "Borrar", command=self.borrar_usuario)
        btn_editarU = Button(self, text = "Editar")

        btn_nuevoU.grid(row = 4, column = 1)
        btn_borrarU.grid(row = 4, column = 2)
        # btn_editarU.grid(row = 4, column = 3)

        self.v_usuario =tk.Listbox(self, height=len(usuarios),width=30)
        self.v_usuario.insert(0, *usuarios)
        self.v_usuario.grid(row = 6, column = 1, columnspan = 4,pady = 20)

        ###############################################################


        t_eventos = Label(self, text = "Eventos: ", relief="groove")
        t_eventos.grid(row = 9, column = 0, sticky = W, pady = 2)
        btn_borrarE = Button(self, text = "Borrar", command=self.borrar_evento)
        btn_borrarE.grid(row = 9, column = 1, sticky = E)

        btn_exportarE = Button(self, text = "Exportar csv", command=self.exportar_evento)
        btn_exportarE.grid(row = 9, column = 2, sticky = E)

        self.v_evento =tk.Listbox(self, height=len(eventos),width=60)
        self.v_evento.insert(0, *eventos)
        self.v_evento.grid(row = 11, column = 1, columnspan=4,pady = 20)


        # proyectos_headers =['placa','fecha_in','fecha_out','peso_in','peso_out','peso_neto','producto','id']
        #
        # self.proyectos_tab = Table(self, title="Proyectos Registrados", headers=proyectos_headers)
        # self.proyectos_tab.grid(row=10, column=0, columnspan=4)
        #
        # #cursor.execute("SELECT Proyectos.Proyecto,Marca,Paquete FROM Proyectos")
        # # cursor =
        #
        # for row in eventos2:
        #    self.proyectos_tab.add_row(row)



    def abrir_producto(self):
        self.p_ventana = tk.Toplevel()
        texto = Label(self.p_ventana, text = "Producto nuevo: ", relief="groove")
        texto.grid(row = 0, column = 0)

        texto2 = Label(self.p_ventana, text = "Nombre Producto: ")
        texto2.grid(row = 1, column = 0)
        self.producto_nombre = Entry(self.p_ventana)
        self.producto_nombre.grid(row = 1, column = 1)

        texto3 = Label(self.p_ventana, text = "Codigo Producto: ")
        texto3.grid(row = 2, column = 0)
        self.producto_codigo = Entry(self.p_ventana)
        self.producto_codigo.grid(row = 2, column = 1)

        btn_nuevoP2 = Button(self.p_ventana, text = "Crear", command=self.nuevo_producto)
        btn_nuevoP2.grid(row = 3, column = 1, sticky = E)


    def editar_producto(self):
        self.p_ventana = tk.Toplevel()
        texto = Label(self.p_ventana, text = "Editar Producto: ", relief="groove")
        texto.grid(row = 0, column = 0)

        texto2 = Label(self.p_ventana, text = "Nombre Producto: ")
        texto2.grid(row = 1, column = 0)
        self.producto_nombre = Entry(self.p_ventana)
        self.producto_nombre.grid(row = 1, column = 1)

        texto3 = Label(self.p_ventana, text = "Codigo Producto: ")
        texto3.grid(row = 2, column = 0)
        self.producto_id = Entry(self.p_ventana)
        self.producto_id.grid(row = 2, column = 1)



        miPack=self.v_producto.get(ANCHOR)
        id=miPack[0]
        nombre=miPack[1]
        self.producto_id.insert(0,id)
        self.producto_nombre.insert(0,nombre)


        btn_nuevoP2 = Button(self.p_ventana, text = "Modificar", command=self.modificar_producto)
        btn_nuevoP2.grid(row = 3, column = 1, sticky = E)
    def abrir_usuario(self):
        self.u_ventana = tk.Toplevel()
        texto = Label(self.u_ventana, text = "Usuario nuevo: ", relief="groove")
        texto.grid(row = 0, column = 0)
        texto2 = Label(self.u_ventana, text = "Nombre Usuario: ")
        texto2.grid(row = 1, column = 0)
        self.user_usuario = Entry(self.u_ventana)
        self.user_usuario.grid(row = 1, column = 1)

        texto3 = Label(self.u_ventana, text = "Contraseña Usuario: ")
        texto3.grid(row = 2, column = 0)
        self.pw_usuario = Entry(self.u_ventana)
        self.pw_usuario.grid(row = 2, column = 1)
        btn_nuevoP2 = Button(self.u_ventana, text = "Crear", command=self.nuevo_usuario)
        btn_nuevoP2.grid(row = 3, column = 1)

    def nuevo_producto(self):

        con = sql_connection()
        nombre=self.producto_nombre.get()
        codigo=self.producto_codigo.get()
        miPack=array([codigo,nombre])
        res= crear_producto(con,miPack)
        # self.v_producto.insert(END,miPack)
        self.v_producto.delete(0, END)
        productos= listar_productos(con)
        self.v_producto.insert(0, *productos)
        self.p_ventana.destroy()

    def modificar_producto(self):

        con = sql_connection()
        # miPack = self.v_producto.get(ANCHOR)

        nombre=self.producto_nombre.get()
        codigo=self.producto_id.get()
        miPack=array([codigo,nombre])
        res= update_producto(con,miPack)
        # self.v_producto.insert(END,miPack)
        self.v_producto.delete(0, END)
        productos= listar_productos(con)
        self.v_producto.insert(0, *productos)
        self.p_ventana.destroy()

    def borrar_producto(self):
        con = sql_connection()
        miPack= self.v_producto.get(ANCHOR)
        print(miPack)
        res = eliminar_producto(con,miPack)
        self.v_producto.delete(0, END)
        productos= listar_productos(con)
        self.v_producto.insert(0, *productos)
        print(res)

    def nuevo_usuario(self):

        con = sql_connection()
        user=self.user_usuario.get()
        pw=self.pw_usuario.get()
        miPack = array([user, pw])
        res= crear_usuario(con,miPack)
        # self.v_producto.insert(END,miPack)
        self.v_usuario.delete(0, END)
        usuarios= listar_usuarios(con)
        self.v_usuario.insert(0, *usuarios)
        self.u_ventana.destroy()

    def borrar_usuario(self):
        con = sql_connection()
        miPack= self.v_usuario.get(ANCHOR)
        user= miPack[0]
        res = eliminar_usuario(con,miPack)
        self.v_usuario.delete(0, END)
        usuarios= listar_usuarios(con)
        self.v_usuario.insert(0, *usuarios)
        print(res)

    def borrar_evento(self):
        con = sql_connection()
        miPack= self.v_evento.get(ANCHOR)
        id= miPack[7]
        res = eliminar_evento(con,id)
        self.v_evento.delete(0, END)
        eventos= listar_eventos(con)
        self.v_evento.insert(0, *eventos)
        print(res)

    def exportar_evento(self):

        # myData = [["first_name", "second_name", "Grade"],
        #           ['Alex', 'Brian', 'A'],
        #           ['Tom', 'Smith', 'B']]
        con = sql_connection()
        eventos= listar_eventos_exportar(con)
        print(eventos)
        eventos.insert(0, ['placa','fecha_in','fecha_out','peso_in','producto'])

        #
        myFile = open('eventosDATA.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(eventos)


        print("Writing complete")
        print("Te amo mi vida hermosa! No espere llegar amarte tanto tanto!!!!!")


class Application(ttk.Frame):

        def tomar_foto_entrada(self):
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

                placa=reconocer_placa("camion.png")
                fecha_in=datetime.now()
                peso_neto=self.peso
                producto=int(self.v_producto.get())
                # placa = 'msd666'
                miPack = array([placa, fecha_in, peso_neto, producto])
                con = sql_connection()
                res= insert_evento(con,miPack)

                # values=["Arroz","Platano","Yuca","Papa","Mazorca"]
                self.v_placa.config(text=placa)

                # v_placa = Label(master, text = placa)
                # v_placa.grid(row = 2, column = 1, sticky = W, pady = 2)

        def tomar_foto_salida(self):
                print("Proceso Salida Iniciado")
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
                placa = reconocer_placa("foto.png")
                miPack = array([placa])

                con = sql_connection()
                res= buscar_evento(con,miPack)
                id = res[0]
                peso_neto = res[1]
                peso_out = self.peso
                peso_carga = peso_neto - peso_out  ## SI EL PESO CARGA ES POSITIVO(DEJO CARGA), NEGATIVO(SACÓ CARGA)

                # peso_in=
                # peso_out=self.peso
                # producto=int(self.v_producto.get())
                miPack = array([id, peso_carga, peso_out])
                con = sql_connection()
                res= insert_evento_salida(con,miPack)
                print(res)

                self.v_placa.config(text=placa)

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

                btnIngreso = Button(master, text = "Ingreso",command=self.tomar_foto_entrada)
                btnSalida = Button(master, text = "Salida",command=self.tomar_foto_salida)

                # arranging button widgets
                btnIngreso.grid(row = 6, column = 0, columnspan = 1, padx =5,   pady = 1, sticky = E)
                btnSalida.grid(row = 6, column = 1, columnspan = 1,  ipadx =5,   pady = 1, sticky = E)



master = tk.Tk()
app=Application(master)
# infinite loop which can be terminated
# by keyboard or mouse interrupt
app.mainloop()
