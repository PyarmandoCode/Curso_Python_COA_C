"""
Crear Programa que me permota calcular el pago
mensual de una planilla de trabajadores
"""
trabajadores = [
    {"codigo":"TRAB_01","ht":40},#0
    {"codigo":"TRAB_02","ht":42},#1
    {"codigo":"TRAB_03","ht":44},#2
]
#funcion para llenar mas trabajadores
def ingresar_trabajadores(codigoparm,htparm):
    try:
        nuevo_trabajador= {
            "codigo":codigoparm,
            "ht":htparm
        }
        trabajadores.append(nuevo_trabajador)
    except Exception as err:
        return f"Ocurrio un error {err}"    
    else:
        return f"Empleado Registrado Correctamente"    
#funcion para listar mas trabajadores  
      
def listar_trabajadores():
    total_acum=0
    pago_hora=20
    for index,trabajador in enumerate(trabajadores):
        total_trab = trabajadores[index]['ht']*pago_hora
        total_acum += total_trab
    print(f"La Planilla de este mes es {total_acum /len(trabajadores)}")

#programa principal
while True:
    codigo=input("Ingrese el codigo:")
    ht=int(input("Ingrese las Horas Trabajadas:"))
    ingresar_trabajadores(codigo,ht)
    resp=input("Desea Ingresar otro Trabajador:")
    if resp=="n":
        break
listar_trabajadores()    



