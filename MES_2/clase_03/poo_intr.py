"""
Definicion de una clase y la creacion de objetos
"""

class Persona:
    def __init__(self,nombre,edad,sueldo,ts=None):
        self.nombre=nombre
        self.edad=edad
        self.sueldo=sueldo
        self.ts=ts
    def mensaje(self):    
        return f"Hola {self.nombre} Ya usas POO?" 
    def calcular_bon(self):
        if self.ts>5:
            return f"Ud tiene una bonificacion del 2% de su sueldo"
        else:
            return f"Ud AUN NO CUENTA CON UNA BONIFICACION"
#Esto es un objeto QUE SE INSTANCIA de la clase
empleado1=Persona("Jorge",29,1600,10)
print(empleado1.__dict__)
print(f"Este es el nombre:{empleado1.nombre}")
print(f"Esta es la edad :{empleado1.edad}")
print(empleado1.mensaje())
print(empleado1.calcular_bon())



