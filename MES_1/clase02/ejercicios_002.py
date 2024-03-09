"""
002-1.-Pedir 2 números al usuario y sumarlos, restarlos, multiplicarlos y dividirlos.
num1=int(input("Ingrese el Numero 1:"))
num2=int(input("Ingrese el Numero 2:"))
sum = num1 + num2
res = num1 - num2
mul = num1 * num2
div = num1 // num2 #Division Entera
print(f"La Suma es {sum} Resta {res} la Multiplicacion {mul} la division {div}")
"""
"""
002-2.-. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuánto deberá pagar finalmente por su compra. 
precio=float(input("Ingrese el precio del producto:"))
des=precio*0.15
total=precio-des
print(f"El Total a pagar por el producto es {total} ha tenido un descuento de {des} porque su precio normal es {precio}")
"""
"""
002-3.-. Un alumno desea saber cuál será su calificación final en la materia de 
Algoritmos. Dicha calificación se compone de los siguientes porcentajes: 
• 55% del promedio de sus tres calificaciones parciales. 
• 30% de la calificación del examen final.  
• 15% de la calificación de un trabajo final.     
"""
parcial_1=float(input("Ingrese el parcial 1:"))
parcial_2=float(input("Ingrese el parcial 2:"))
parcial_3=float(input("Ingrese el parcial 3:"))
promedio=(parcial_1+parcial_2+parcial_3)/3
peso_promedio=promedio*0.55
e_final=float(input("Ingrese el Examen Final:"))
peso_efinal=e_final*0.30
trab_final=float(input("Ingrese el Trabajo final:"))
peso_trabfinal=trab_final*0.15
calificacion=peso_promedio+peso_efinal+peso_trabfinal
print(f"EL Promedio Final obtenido en el curso fue de {calificacion}")












