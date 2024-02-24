from datetime import datetime,timedelta

#Obtener la fecha y la hora actual
fecha_actual=datetime.now()
#print(f"La fecha y hora del sistema es {fecha_actual}")

#Acceder a los componentes de la fecha

# print(f"El Año Actual {fecha_actual.year}")
# print(f"El Mes Actual {fecha_actual.month}")
# print(f"El Dia Actual {fecha_actual.day}")
# print(f"La Hora Actual {fecha_actual.hour}")
# print(f"Los Minutos {fecha_actual.minute}")
# print(f"Los Segundos {fecha_actual.second}")

#Operaciones entre fechas
nueva_fecha=fecha_actual+timedelta(days=7)
#print(f"la Nueva Fecha mas 7 dias es {nueva_fecha}")

#Conversion de fechas
cadena_fecha="2023-08-25"
formato_cadena = "%Y-%m-%d"
fecha_desde_cadena=datetime.strptime(cadena_fecha,formato_cadena)


fecha_formateada=fecha_desde_cadena.strftime(formato_cadena)
print(f"La Nueva Fecha es {fecha_formateada}")

#print(type(fecha_desde_cadena))

#Calcular la diferencia entre 2 fecha
fecha1=datetime(2022,5,10)
fecha2=datetime(2022,3,15)

diferencia_entre_fechas = fecha1 - fecha2
#print(f"Diferencia entre fechas {diferencia_entre_fechas.days}")

#Ejemplo con formato de fecha
fecha_objeto=datetime.now()
formato_deseado="%Y/%m/%d %H:%M:%S"

fecha_formateada=fecha_objeto.strftime(formato_deseado)
print(f"Fecha Formateada con el separador / {fecha_formateada}")