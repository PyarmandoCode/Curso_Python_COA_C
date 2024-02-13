"""
PRIMER CLASE DE PYTHON EN COA
USO DE VARIABLES Y TIPO DE DATOS
"""

#print("Hola Mundo desde Python desde COA") # Esta funcion print visualiza mensajes por consola

#Uso de Variables - Tipo de Datos Primitivos
#Numericas
edad = 18
gastos = 190.57
#Cadena = STR
nombre = "Juan"
apellido= 'Perez'
#Booleana
estado = True # False

#print(type(edad))
#print(type(gastos))
#print(type(nombre))
#print(type(estado))


#Operaciones Aritmeticas
suma = 12 + 4
resta = 12 - 4
divdec = 12 / 4
divent = 12 // 4
mult= 12 * 4

# print(suma)
# print(resta)
# print(divent)
# print(divdec)

#Concatenar Variables y Frases
edad = 18
gastos = 190.57
#Cadena = STR
nombre = "Juan"
apellido= 'Perez'
#Booleana
estado = True # False

#print(nombre+apellido+str(edad))
#print(nombre,apellido,edad)
#print(f"\t\t El Nombre de la Persona es {nombre} \n\n su apellido es {apellido} y su  edad {edad}")

#input

# nombre = input("ingrese su Nombre:")
# apellido = input("ingrese la apellido:")
# año_nac = int(input("ingrese el año de nacimiento:")) #Convertir o Castear
# edad = 2024 - año_nac
# print(f"hola {nombre} que bueno verte por aca tu edad es {edad}")


# pago_hora=10
# nombre_trab=input("Ingrese el nombre del trabajador:")
# horas_trab=int(input("Ingrese las horas trabajadas diarias:"))
# jornal=horas_trab*pago_hora
# print(f"{nombre_trab} tu pago de hoy sera {jornal}")


producto=input("Ingrese el nombre del producto:")
precio=float(input("Ingrese el precio del producto: "))
cant=int(input("Ingrese la cantidad del producto a comprar:"))
sub_total = precio * cant
impuesto = sub_total * 0.08
total = sub_total + impuesto
print(f"El Total a pagar sera {total} y el impuesto aplicado es {impuesto}")
