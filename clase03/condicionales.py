"""
Procesos Condicionales Simples
"""
#edad = int(input("Ingrese la edad del individuo:"))
#if edad>=18:
#    print("El Individuo es Mayor de Edad ")
#else:
#    print("El Individuo es Menor de Edad")    

"""
Procesos Condicionales Multiples
Desea Aplicar un bonificacion a un empleado de acuerdo
al Area en que Labora
[Sis]temas=0.02
[Con]tabilidad=0.03
[Mar]keting=0.05
No Tiene Bonificacion
"""
sueldo=float(input("Ingrese el Sueldo del Trabajador:"))
area = input("Ingrese el Area en que Laboras:")
if area =="Sis" or area=="RRHH":
    por_bon=0.02
elif area=="Cont":
    por_bon=0.03
elif area=="Mar":
    por_bon=0.05
else:
    por_bon=0
bon=sueldo*por_bon
neto=sueldo+bon
print(f"El Sueldo que recibira es {neto} con una bonificacion de {bon}")        
