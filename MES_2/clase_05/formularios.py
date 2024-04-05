import tkinter as tk

def enviar_formulario():
    nombre=entry_nombre.get()
    edad=entry_edad.get()
    print(f"Nombre {nombre} , Edad {edad}")

#crear la ventana
ventana=tk.Tk()
ventana.title("Formulario")

#Crear etiquetas y campos de entrada
etiqueta_nombre=tk.Label(ventana,text="Nombre:")
etiqueta_nombre.grid(row=0,column=0,padx=5,pady=5)
entry_nombre=tk.Entry(ventana)
entry_nombre.grid(row=0,column=1,padx=5,pady=5)

etiqueta_edad=tk.Label(ventana,text="Edad:")
etiqueta_edad.grid(row=1,column=0,padx=5,pady=5)
entry_edad=tk.Entry(ventana)
entry_edad.grid(row=1,column=1,padx=5,pady=5)

#Boton para enviar el formulario
boton_enviar=tk.Button(ventana,text="Enviar",command=enviar_formulario)
boton_enviar.grid(row=2,column=0,columnspan=2,padx=5,pady=5)


ventana.mainloop()