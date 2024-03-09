# try:
#     division = 20 / 0
# except Exception as err:
#     print(err)    
"""
Crear un programa que almacene notas de alumnos en un
diccionario con sus respectivos nombres  y me indique 
el nombre del alumno con notas masl alta y mas baja
alumnos ={
    "nombre":"jose","nota":20,
    "nombre":"pedro","nota":12
}
"""
estudiantes = {}
while True:
    #Solicitar nombre y la nota del estudiante
    nombre=input("Ingrese el nombre del estudiante (o 'no' para terminar) ")
    #Salir del bucle si se ingresa "no"
    if nombre.lower() == "no":
        break
    try:
        nota=float(input(f"Ingrese la nota de {nombre}:"))
        #validar que la nota este en el rango de 0 a 20
        if 0<= nota <=20:
            estudiantes[nombre]=nota
        else:
            print("Error la nota debe estar en el rango de [0..20]")    
    except ValueError:
        print("Error Ingrese un Valor valido para la nota")    

#Verificar si hay estudiantes registrados
if estudiantes:
    #Encontrar el nombre del estudiante con la nota mas alta y baja
    estudiante_max_nota=max(estudiantes,key=estudiantes.get) 
    estudiante_min_nota=min(estudiantes,key=estudiantes.get)   

    print(f"\nEstudiante con la nota mas alta {estudiante_max_nota} - Nota: {estudiantes[estudiante_max_nota]}")
    print(f"\nEstudiante con la nota mas baja {estudiante_min_nota} - Nota: {estudiantes[estudiante_min_nota]}")
else:
    print("No Se han Ingresado estudiantes")    











