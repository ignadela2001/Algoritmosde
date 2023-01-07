
from io import open 

fichero = open("personas.txt", "r")
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n", "").split(";")
    persona = {"id":campos[0], "nombre":campos[1], "apellidos":campos[2], "nacimiento":campos[3]}
    personas.appemd(persona)
    
for p in personas:
    print("(id={}) {} {} => {}".format(p["id"], p["nombre"], p["apellido"], p["nacimiento"]))