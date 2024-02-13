"""
Tipos de Datos Primitivos
Numericos
=========
*Enteros=Int
*Decimales=Float
Cadena
======
*String=Str
Booleano
========
*Logicos=True/False
"""
"""
Colecciones
==========
A>Listas
"""
productos=["TELEVISOR","CELULAR","MONITOR",80,12.70,True,["SMARTPHONE","PARLANTE"]]

#print(productos)
"""
print(productos[1])
print(productos[0])
print(productos[2])
print(productos[6])
"""
productos.append("TECLADO") #metodo append añade elementos al final de la lista
productos.insert(0,"LAPTOP") #metodo insert añade elemnento a la lista posicion indiques
productos.pop(0)#metodo permite eliminar un elemento de la lista por su posicion
productos.remove("MONITOR")
productos[3]=180.90
print(productos)