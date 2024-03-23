"""
Crear un Programa Para Gestionar una Biblioteca
Representar Libros y bibliotecas

1.-Clase Libro
===========
Atributos
========
-Titulo
-Autor
-Año de Publicacion
-Genero

Metodos
=======
__init__:inicializar los atributos del libro
detalles:para mostrar los detalles del libro

2.-Clase Biblioteca
==================
Atributos:
==========
-Nombre de la biblioteca
-Lista de Libros(Lista Vacia)

Metodos
========
__init__:inicializar los atributos de la biblioteca
-Agregarlibro:Agregar un Libro a la lista de libros
-Mostrarlibros:Mostrar los detalles de todos los libros en la biblioteca

"""
class Libro:
    def __init__(self,titulo,autor,año,genero):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.genero=genero

    def detalles(self):
        return f"Titulo:{self.titulo},Autor:{self.autor},Año{self.año},Genero {self.genero}"
class Biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[]
    def agregar_libro(self,libro):
        self.libros.append(libro)    
        print(f"Libro '{libro}' Agregando a la biblioteca")
    def mostrar_libros(self):
        print(f"Libros disponibles en la {self.nombre}")
        for index,libro in enumerate(self.libros):
            print(f"{index+1} - {libro.titulo}")    

#Ejemplo de uso
if __name__=="__main__":   
    libro1=Libro("Cien años de soledad","Garcia Marques",1967,"Realismo")    
    libro2=Libro("Don Quijote de la Mancha","Miguel Cervantes",1956,"Realismo")         
    libro3=Libro("Aprende Python en 24 horas","Armando Ruiz",2024,"Programacion")
    libro4=Libro("Aprende POO","Armando Ruiz",2023,"Programacion")
    biblioteca=Biblioteca("Biblioteca Jesus Divino")#Creando una biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)
    biblioteca.mostrar_libros()




            
    

#print(libro1.autor)
#libro1.año
#libro1.genero
#print(libro1.__dict__)





