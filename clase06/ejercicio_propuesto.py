from datetime import datetime
"""
Crear un Programa que me permita ingresar dos fechas y obtenga la diferencia
de dias entre esa fechas y tambien que imprima la  fecha actual formateada
usar funciones , excepciones y pasar los valores por parametros
"""
def diferencia_entre_fechas(fecha1,fecha2):
    try:
        delta = fecha2 - fecha1
        return delta.days
    except Exception as err:
        print(f"Ha Ocurrido un error {err}")
    else:
        print("Todo correcto")
    
