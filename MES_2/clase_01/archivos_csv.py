"""
Leer Archivos CSV
"""

import csv
def leer_csv():
    try:
        con=0
        with open('./MES_2/clase_01/archivos/dinamica.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                if con>0 and int(row[2])>800:
                    print(f"{con } {row[0]} {row[1]} {row[2]}")
                con +=1
    except Exception as err:
        print(f"Ocurrio un error {err}")            
    else:
        print("No Ocurrio Errores")    
    finally:
        file.close()    

"""
Generar un Archivo CSV
"""        
def generar_archivo():
    try:
        data=[
               ['CODIGO','PRODUCTO','STOCK'],
               ['A100','XYZ','200'],
               ['A200','MNO','400'],
               ['A300','lNO','400'],
              ]
        with open('./MES_2/clase_01/archivos/nuevos_datos.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(data)
    except Exception as err:
        print(f"El Archivo no se genero {err}")        
    else:
        print("Se genero correctamente")    
    finally:
        file.close()    
generar_archivo()        



