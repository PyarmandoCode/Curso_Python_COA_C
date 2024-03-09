"""
Colecciones=Estructura de datos
Listas = []
Tuplas =()
Diccionarios ={}
Set = {}
"""

mi_diccionario=dict()

mi_diccionario = {
    "nombre":"juan","edad":30,"ciudad":"new york"
}

#print(mi_diccionario["nombre"])
#Agregar un nuevo elemento al Diccionario
# mi_diccionario['profesion']="Developer Python pro"
# #print(mi_diccionario)
# for k,v in mi_diccionario.items():
#     print(f'La Clave {k} y su Valor {v}')



lista_empleado =[
    {"codigo":100,"nombre":"juan","edad":30,"ciudad":"new york"},
    {"codigo":200,"nombre":"pedro","edad":20,"ciudad":"miami"},
    {"codigo":300,"nombre":"maria","edad":17,"ciudad":"la florida"},
    {"codigo":400,"nombre":"rosa","edad":43,"ciudad":"las vegas"}
]

def buscar_empleado(lista,cod):
    for empleado in lista:
        if empleado['codigo']==cod:
            dato=f"{empleado['nombre']} - {empleado['edad']} - {empleado['ciudad']}"
            return f"{dato}"
    return f"No Se encontro el empleado"    
        
print(buscar_empleado(lista_empleado,800))
    

