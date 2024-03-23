"""
Persistencia de datos
SQLITE .- Base de datos Local que esta formado
por tablas que en su contenido tienes campos y filas
esto nos permitira que nuestra informacion que genera nuestra
aplicacion que persistente y posteriormente lo podemos administrar
"""
"""
Realizar una aplicacion para gestionar peliculas
y luego poder administrarlas
CRUD:CREATE-READ-UPDATE-DELETE
-Insertar (Insert)
-Eliminar (Delete)
-Actualizar (Update)
-Consulta (Select)
"""
import sqlite3
class Pelicula:
    def __init__(self,titulo,director,duracion):
        self.titulo=titulo
        self.director=director
        self.duracion=duracion
    def __str__(self):
         return f"{self.titulo} -Dirigida por {self.director}" 

class Videoteca:
    def __init__(self,db_file):
        self.db_file=db_file
        self.conexion=sqlite3.connect(db_file)       
        self.cursor=self.conexion.cursor()
        self.crear_tabla()
    
    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas (
                             id INTEGER PRIMARY KEY,
                             titulo TEXT,
                             director TEXT,
                             duracion INTEGER) 
                            ''')
        self.conexion.commit() 

    def agregar_pelicula(self,pelicula):
        self.cursor.execute('''INSERT INTO peliculas(titulo,director,duracion) VALUES (?,?,?)''',(pelicula.titulo,pelicula.director,pelicula.duracion))    
        self.conexion.commit()
        print(f"Pelicula '{pelicula.titulo}' Agregada a la videoteca")

    def mostrar_peliculas(self):
        self.cursor.execute('''SELECT titulo,director FROM peliculas''')    
        peliculas=self.cursor.fetchall()
        print("Peliculas disponibles en la Videoteca")
        for pelicula in peliculas:
            print(f"{pelicula[0]} - Dirigida por {pelicula[1]}")
#Ejemplo de uso
if __name__=="__main__":
    videoteca=Videoteca("videoteca.db")
    pelicula1=Pelicula("El Padrino","Francis Ford Coppola",175)   
    pelicula2=Pelicula("La Lista de Schinder","Steven Spielber",195)  
    pelicula3=Pelicula("Pulp Fiction","Quentin Tarantino",154) 
    pelicula4=Pelicula("El Exorcista","Quentin Tarantino",124)
    videoteca.agregar_pelicula(pelicula1)
    videoteca.agregar_pelicula(pelicula2)
    videoteca.agregar_pelicula(pelicula3)
    videoteca.mostrar_peliculas()






















