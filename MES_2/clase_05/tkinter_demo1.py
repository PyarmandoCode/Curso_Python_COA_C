import tkinter as tk
from misfunciones import *

def imprimir_texto():
    texto=entrada.get()
    print(f"Texto ingresado {texto}")

#Crear Ventana
ventana=tk.Tk()
ventana.title("Mi Ventana")

#Crear una Etiqueta
#etiqueta=tk.Label(ventana,text="Hola Mundo desde Tkinter!!")
#etiqueta.pack()

#Campo de entrada de texto
entrada=tk.Entry(ventana)
entrada.pack()

#Boton para imprimir el texto ingresado
boton = tk.Button(ventana,text="Imprimir Texto",command=imprimir_mensaje)
boton.pack()

#Mostrar Ventana
ventana.mainloop()
