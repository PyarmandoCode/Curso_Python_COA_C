import tkinter as tk

#Metodo para manejar las opciones seleccionadas
def seleccionar_opcion():
    seleccion=opcion_variable.get()
    print(f"Opcion seleccionada {seleccion}")

ventana=tk.Tk()    
ventana.title("Menu Desplegable")

#Variable para almacenar la opcion seleccionda
opcion_variable=tk.StringVar(ventana)
opciones =["Opcion1","Opcion2","Opcion3"]
#Establecer la opcion predeterminada
opcion_variable.set(opciones[0])
#Crear el menu desplegable
menu_desplegable=tk.OptionMenu(ventana,opcion_variable,*opciones)
menu_desplegable.pack()

#Boton para seleccionar la opcion
boton=tk.Button(ventana,text="Seleccionar",command=seleccionar_opcion)
boton.pack()

#Mostrar la ventana
ventana.mainloop()
