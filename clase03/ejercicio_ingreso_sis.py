usuario_valido="admin"
contraseña_valida="123"
intentos=3


while intentos > 0:
    usuario=input("Ingrese el Usuario:")
    contraseña=input("Ingrese Contraseña:")
    if usuario==usuario_valido and contraseña==contraseña_valida:
        print("Bienvenido al Sistema")
        break #Terminar el Proceso
    else:
        intentos -= 1
        print(f"Usuario Invalido,Intentos Restantes {intentos}")
if intentos ==0:
    print("Tu Cuenta se Bloqueara por 24 Horas")        
