carrito_compra =[]

def agregar_producto():
    nombre=input("Ingrese el Nombre del producto:")
    cantidad=int(input("Ingrese la cantidad:")
    precio_unitario=float(input("Ingrese el precio por unidad:"))

    producto = {
        'nombre':nombre,
        'cantidad':cantidad,
        'precio_unitario':precio_unitario
    }

    carrito_compra.append(producto)
    print(f"{nombre} Ha sido agregado al carrito")

def mostrar_carrito():
    if not carrito_compra:
        print("El Carrito de compras esta vacio")    
    else:
        print("Producto en el carrito")
        total_compra=0
        for producto in carrito_compra:
            total_producto=producto['cantidad'] * producto['precio_unitario']
            total_compra += total_producto
            print(f"{producto['nombre']} - Cantidad {producto['cantidad']} - Precio Unitario ${producto['precio_unitario']} -Total ${total_producto}")
        print(f"Total de la Compra: ${total_compra}")    

agregar_producto()
                  
