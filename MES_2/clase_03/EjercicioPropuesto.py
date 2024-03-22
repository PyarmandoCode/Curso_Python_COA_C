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
    
libro1=Libro("Cien años de soledad","Garcia Marques",1967,"Realismo")    
print(libro1.autor)
libro1.año
libro1.genero
print(libro1.__dict__)





