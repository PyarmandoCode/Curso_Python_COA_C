productos=list()

while True:
    valor=input("Ingrese un Producto para la lista:")
    productos.append(valor)
    opc=input("¿Desea Seguir Añadiendo productos a la Lista:")
    if opc != "S":
        break

for items in productos:
    print(items)