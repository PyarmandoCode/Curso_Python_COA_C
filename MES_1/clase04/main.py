from funciones import calcular_promedio,validar_contraseña

#Llamada a la Funcion
# lista_numeros=[10,20,30,40,50]
# promedio_resultado=calcular_promedio(lista_numeros)
# print(f"El promedio es {promedio_resultado}")

contraseña_usuario="MiContraseña123"    
if validar_contraseña(contraseña_usuario):
    print("Contraseña Valida")
else:
    print("Contraseña Invalida")   