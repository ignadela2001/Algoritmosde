texto = "Un dia que el viento soplaba#Mira como se mueve aquella bandolera - dijo un monje#lo que se mueve es el viento -respondio otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas = texto.split("#")

for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else: 
        lineas[i] = "- " + lineas [i] + "."
        
for linea in lineas:
    print (linea)