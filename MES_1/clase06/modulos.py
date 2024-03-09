"""
Modulo Matematico
Algunas FUNCIONES
"""
import math #Modulo Matematico
#print(f"El Valor de PI {math.pi}")
#print(f"La Raiz Cuadrada de 20 {math.sqrt(20)}")
#print(f"Coseno de PI {math.cos(math.pi/4)}")

"""
Modulo Estadistico
"""
import statistics
datos=[2.90,10.5,14.7,23.7,10.5]
media_aritmetica=statistics.mean(datos)
print(f"La Media aritmetica o promedio de la lista de datos es {round(media_aritmetica,2)}")
valor_medio=statistics.median(datos)
print(f"El Valor medio de la lista de datos es {valor_medio}")
valor_moda=statistics.mode(datos)
print(f"La Moda de la lista de datos es {valor_moda}")



      
