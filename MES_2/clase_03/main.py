from Clientes import Cliente
from Ventas import Venta
from Productos import Producto
cliente1 = Cliente("Juan","Calle 123")
venta1= Venta(cliente1)
producto1 = Producto("Camisa",20,2)
producto2=Producto("Pantalon",30,1)
venta1.agregar_producto(producto1)
venta1.agregar_producto(producto2)
total_venta1=venta1.calcular_venta_total()
print(f"Cliente {venta1.cliente.nombre}")
print("Productos")
for producto in venta1.productos:
    print(f"-{producto.nombre}:{producto.precio}*{producto.cantidad}={producto.calcular_total()}")
print(f"Total de la venta {total_venta1} ")
