def mensaje_bienvenida(user,passw,nom):
    if user=="Admin" and passw=="123":
        return f"Bienvenido {nom} al Sistema"
    else:
        return f"Usuario {nom} Invalido"
#print(mensaje_bienvenida("Admin","12","Armando"))
        
def calcular_promedio(numeros):
    total = sum(numeros)
    cantidad=len(numeros)
    promedio=total/cantidad
    return promedio

#Llamada a la Funcion
# lista_numeros=[10,20,30,40,50]
# promedio_resultado=calcular_promedio(lista_numeros)
# print(f"El promedio es {promedio_resultado}")
    

# frase="Python es Un lENGUAJE DE PROGRAMACION facil de aprender en el 2024"
# #print(len(frase))
# for char in frase:
#     if char.isdigit():
#         print("Si hay un digito")
#         break
#     else:
#         print("No Hay digito")    
    

def validar_contraseña(contraseña):
    #Verificar si la contraseña tiene al menos 8 caracteres y contiene al menos un numeros
    if len(contraseña)>=8 and any(char.isdigit() for char in contraseña):
        return True
    else:
        return False
    
#Llamada a la Funcion

# contraseña_usuario="MiContraseña123"    
# if validar_contraseña(contraseña_usuario):
#     print("Contraseña Valida")
# else:
#     print("Contraseña Invalida")    

    




