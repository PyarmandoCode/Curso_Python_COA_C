import random
valor=random.random()
print(f"El Valor generado de manera aleatoria {valor}")

entre_valores=random.randrange(1,100)
print(f"El Numero generado entre 1 y 100 es {entre_valores}")

listas_personas=["JOSE","PEDRO","MARIA","NICOLE"]
persona_seleccionada=random.choice(listas_personas)
print(f"La Persona seleccioanada es {persona_seleccionada}")

"""
Hacer un programa que permita adivinar el lanzamiento 
de un Juego de datos si la persona acerto el numero que
aparecio en la primera plana
"""
def juego_del_dado():
    try:
        while True:
            lanza_azar=random.randrange(1,6)
            numero_adivinar=int(input("Ingrese el Numero a adivinar:"))
            if numero_adivinar==lanza_azar:
                print(f"Felicitaciones Acertates el numero fue {lanza_azar}")
                break
            else:
                print(f"El Numero no fue el correcto {lanza_azar}")    
    except Exception as err:
        print(f"A Ocurrido un error {err}")            
    else:
        print("No Ha ocurido ningun error")    

juego_del_dado()



                    