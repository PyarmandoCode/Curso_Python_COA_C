"""
Realizar un programa en Python que simule un cajero automatico
1.-Retirar deinero
2.-Deposito dinero
3.-Consulta de Saldo
Debe ser en base a funciones y estructura de datos(Listas)
"""
saldo = 1000

def mostrar_menu():
    print("\nMenu de Opciones")
    print("1.-Consultar su saldo")
    print("2.-Retirar Dinero")
    print("3.-Depositar Dinero")
    print("4.-Salir")

def consultar_saldo():
    print(f"Tu Saldo actual es {saldo}")    

def retirar_dinero():
    global saldo
    cantidad= float(input("Ingrese la cantidad a retirar:$"))
    if cantidad > saldo:
        print("No Tiene Suficiente Saldo para retirar!!")
    else:
        saldo -= cantidad
        print(f"Retirastes: ${cantidad}\n Tu saldo actual es : ${saldo}")

def depositar_dinero():
    global saldo
    cantidad=float(input("Ingrese la cantidad a depositar; $ "))        
    saldo += cantidad
    print(f"Depositastes ${cantidad}\n Tu Saldo actual es: ${saldo}")


while True:
    try:
        mostrar_menu()    
        opcion=int(input("Seleccione una opcion:"))
        if opcion == 1:
            consultar_saldo()
        elif opcion ==2:
            retirar_dinero()
        elif opcion ==3:
            depositar_dinero()
        elif opcion ==4:
            break#False
        else:
            print("Opcion Invalida")            
    except ValueError:
        print("Debe Ingresar un valor Numerico a las opciones")        









