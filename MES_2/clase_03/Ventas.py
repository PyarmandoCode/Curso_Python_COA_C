
class Venta:
    def __init__(self,cliente):
        self.cliente=cliente
        self.productos=[]
    def agregar_producto(self,producto):
        self.productos.append(producto)
    def calcular_venta_total(self):
        total=0
        for producto in self.productos:
            total +=producto.calcular_total()
        return total    

    