"""
Hacer un programa que rellene una Lista con los 10 primeros números enteros 
y los muestre en pantalla en orden ascendente. 

numeros_pares = list() #Inicializando Lista vacia
numeros_impares = list() #Inicializando Lista vacia

for numero in range(1,11):
    if numero % 2 == 0:
        numeros_pares.append(numero)#2,4,6,8,10
    else:
        numeros_impares.append(numero)#1,3,5,7,9
print(f"Los Numeros Pares son {numeros_pares}")    
print(f"Los Numeros Impares son {numeros_impares}")    


"""

"""
En Una Lista Almacenar notas de un salon de clase del curso de python
el ingreso debe terminar cuando se escriba la palabra "fin". luego se debe imprimir lo sgte;
1.-La  Nota mas Alta
2.-La Nota Mas Baja
3.-El Promedio General de la Clase
"""
def nota_max_min_prom():
    notas_curso_python = list()
    con=0
    while True:
        nota=float(input("Ingrese la Nota:"))
        if 0 <= nota <=20:
            notas_curso_python.append(nota)
            rpta = input("¿Desea Ingresar Otra Nota:")
            con +=1
            if rpta == "fin":
                break
        else:
            print(f"La Nota ingresada {nota} no esta en el rango [0..20]")    
    nota_alta=max(notas_curso_python)
    nota_min=min(notas_curso_python)
    suma_nota=sum(notas_curso_python)
    promedio_nota=suma_nota/con
    return f"La Nota Mas Alta es {round(nota_alta,2)} \n La Nota Minima es {round(nota_min,2)} \n El promedio de la clase es {round(promedio_nota,2)}"

print(nota_max_min_prom())