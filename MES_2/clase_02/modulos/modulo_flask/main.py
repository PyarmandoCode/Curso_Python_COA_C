from flask import Flask

#Crear una instancia de la aplicacion Flask
app =Flask(__name__)

#Definir una ruta y la funcion que se ejecutara cuando se acceda a la ruta

@app.route('/')
def hola_mundo():
    return "Hola Mundo desde Python en la Web Usando Flask"

if __name__=="__main__":
    app.run(debug=True)




