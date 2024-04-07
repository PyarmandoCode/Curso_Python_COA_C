import tkinter as tk
import sqlite3
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mostrar los cursos Referentes a Python")
        #Crear la conexion a la bd
        self.conn=sqlite3.connect('cursos.db')
        self.cursor=self.conn.cursor()
        #Crear la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tblcursos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT,
                            duracion TEXT,
                            precio INTEGER)''')
        self.conn.commit()
        self.create_widgets()
        self.load_data()
    def create_widgets(self):
        #crear el formulario
        self.form_frame=ttk.LabelFrame(self,text="Datos del Curso")    
        self.form_frame.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.nombre_label=ttk.Label(self.form_frame,text="Nombre")
        self.nombre_label.grid(row=0,column=0,padx=5,pady=5,sticky="e")
        self.nombre_value=tk.StringVar()
        self.nombre_entry=ttk.Entry(self.form_frame,textvariable=self.nombre_value,state='readonly')
        self.nombre_entry.grid(row=0,column=1,padx=5,pady=5)

        self.duracion_label=ttk.Label(self.form_frame,text="Duracion")
        self.duracion_label.grid(row=1,column=0,padx=5,pady=5,sticky="e")
        self.duracion_value=tk.StringVar()
        self.duracion_entry=ttk.Entry(self.form_frame,textvariable=self.duracion_value,state='readonly')
        self.duracion_entry.grid(row=1,column=1,padx=5,pady=5)

        self.precio_label=ttk.Label(self.form_frame,text="Precio")
        self.precio_label.grid(row=2,column=0,padx=5,pady=5,sticky="e")
        self.precio_value=tk.StringVar()
        self.precio_entry=ttk.Entry(self.form_frame,textvariable=self.precio_value,state='readonly')
        self.precio_entry.grid(row=2,column=1,padx=5,pady=5)

        #Crear la tabla para mostrar los datos
        self.data_tree=ttk.Treeview(self,column=("Id","Nombre","Duracion","Costo"))
        self.data_tree.grid(row=1,column=0,padx=10,pady=5,sticky="w")

        #Configurar las columnas de la tabla
        self.data_tree.heading("#0",text="Id")
        self.data_tree.heading("#1",text="Nombre")
        self.data_tree.heading("#2",text="Duracion")
        self.data_tree.heading("#3",text="Costo")

        self.data_tree.bind("<<TreeviewSelect>>",self.on_select)

    def load_data(self):    
        for record in self.data_tree.get_children():
            self.data_tree.delete(record)

        self.cursor.execute("select * from tblcursos")    
        records=self.cursor.fetchall()

        for row in records:
            self.data_tree.insert("","end",text=row[0],values=(row[1],row[2],row[3]))

    def on_select(self,event):
        seleted_item=self.data_tree.selection()[0]        
        values=self.data_tree.item(seleted_item,'values')
        self.nombre_value.set(values[0])
        self.duracion_value.set(values[1])
        self.precio_value.set(values[2])


if __name__=="__main__":
    app = Application()

    app.mainloop()        