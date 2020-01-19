
#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
import os

raiz = Tk()
#titulo
raiz.title("Ventana Demo")

# Si se puede expandir o no
raiz.resizable(1,1)

# Icono de la ventana
#raiz.iconbitmap("camara.ico")

# Dimensiones de la ventana
# raiz.geometry("650x350")

# Parametros de config en la ventana:
# raiz["bg"] = "#707070"
raiz.config( bg="#707070")



miFrame=Frame(raiz, width="650", height="350")
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="#707071",)
raiz.mainloop()
