import tkinter as tk
from tkcalendar import Calendar

def obtener_fecha_hora():
    fecha=ca.get_date()
    hora=hora_spinbox.get()
    minuto=minuto_spinbox.get()
    am_pm=am_pm_spinbox.get()
    fecha_hora = f"{fecha} {hora}:{minuto} {am_pm}"
    print(f"Fecha y hora seleccionada {fecha_hora}")

#Crear la ventana
ventana=tk.Tk()
ventana.title("Campo Fecha")

#Crear el widget Calender
ca=Calendar(ventana,year=2024,mont=4,day=4,hour=12,minute=0)
ca.pack(padx=10,pady=10)

#Widgets para seleccionar la hora
tk.Label(ventana,text="Hora").pack()
hora_spinbox=tk.Spinbox(ventana,from_=1,to=12,width=2)
hora_spinbox.pack()

#Widgets para seleccionar la Minuto
tk.Label(ventana,text="Minuto").pack()
minuto_spinbox=tk.Spinbox(ventana,from_=0,to=59,width=2)
minuto_spinbox.pack()

tk.Label(ventana,text="AM/PM").pack()
am_pm_spinbox=tk.Spinbox(ventana,values=("AM","PM"),width=3)
am_pm_spinbox.pack()


#boton para obtener la fecha seleccionada
boton_obtener_fecha=tk.Button(ventana,text="Obtener Fecha y hora",command=obtener_fecha_hora)
boton_obtener_fecha.pack(padx=10,pady=10)

#Mostrar la ventana
ventana.mainloop()