#Ejercicios del tema 1. 

#1.1 Escribe una función cuya firma sea multiple(n, m), y que tome dos enteros y devuelva True is n es un múltiplo de m,
# es decir n = m*i, para una algún entero i, o False en cualquier otro caso.
def multiple(n, m):
    resultado = 0
    if n % m == 0:
        return True
    else:
        return False 
multiple(4, 2)

#1.2  Escribe una función cuya firma sea even(k), y que tome un valor entero y devuelva True is k es par o False en otro caso.
def even(k):
    resultado = 0
    if k % 2 == 0:
        return True
    else:
        return False
even(2)

#1.3 Escribe una función cuya firma sea minmax(data), y que tome una secuencia de uno o mas números, y que devuelva el máximo y mínimo de la secuencia
# No se puede usar las funciones min o max para implementar la solución.
def minmax(data):
    return ("El maximo es:" + str(max(data)) + "  El minimo es: " + str(min(data)))
data = (1,2,3,4,5,6,7,8)
minmax(data)

#BUSCAR ALTERNATIVA A MIN Y A MAX
#def minmax(data):
#    lista = list(data)
#    lista.sort(reverse = True)
#    return lista(0),lista(#rango maximo de la lista)
#data = (1,2,3,4,5,6,7,8)
#minmax(data)

# 1.4 Escribe una función  que come una numero entero positivo n y devuelva la suma de los cuadrados  de los cuadrados de todos los enteros positivos 
# menores a n. 
# Ejemplo: n = 5, solución 4**2 + 3**2 + 2**2 + 1**1
def entero_positivo(n):
    primos = []
    primos_cuadrados = []
    suma_primos_cuadrados = 0
    solucion = "la solucion es: "+ str(suma_primos_cuadrados)
    for i in range(n-1):
        if n-1 % i == 0:
            primos.append(i)
    for i in primos:
        primos_cuadrados.append(i**2)
    for i in primos_cuadrados:
        suma_primos_cuadrados = suma_primos_cuadrados + i
    return solucion
entero_positivo(10)
    
#1.5 Escribe una función que tome un entero positivo y devuelva la suma de los cuadrados de todos los números impares menores
# a n.
# Ejemplo: n = 7, solución 5**2 + 3**2 + 1**1
def entero_impares(n):
    impares = []
    impares_al_cuadrado = []
    suma_impares_cuadrado = 0
    solucion = "La suma de los impares menores al numero entero positivo dado al cuadrado es: " + str(suma_impares_cuadrado)
    for i in range(n-1):
        if i % 2 != 0:
            impares.append(i)
    for i in impares:
        impares_al_cuadrado.append(i**2)
    for i in impares_al_cuadrado:
        suma_impares_cuadrado = suma_impares_cuadrado + i
    return solucion
        
#1.6 Python permite utilizar números negativos como indices en un secuencia, tal como un string. Si el string tiene una longitud n, y la expresión
#  s[k] se usa para los indices −n ≤ k < 0, cual es el el indice equivalente  j ≥ 0 tal que s[j] hace referencia a los mismos elementos?
#---------------------------




#---------------------------
#1.7 Cuales son los parámetros que se deben usar en el constructor de la función range para producir los valores, s 50, 60, 70, 80?
for i in range(50, 90, 10):
    print("s "+ str(i))
    
#1.8 Cuales son los parámetros que se deben usar en el constructor de la función range para producir los valores, 8, 6, 4, 2, 0, −2, −4, −6, −8?
for i in range(8, -10, 2):
    print("s "+ str(i))

#1.9 Escribe una funcion que tome una secuencia de números y determine si todos los números en la secuencia son diferentes.
def num_dif(numeros):
    for numero in numeros:
        for j in numeros:
            if numero == j:
                print("Hay un numero igual a otro")
            else:
                print("Todos los numeros son diferentes")
numeros = [1, 2, 3, 4]
num_dif(numeros)
#1.10 Escribe una función que tome dos listas a y b de longitud n de números enteros, y devuelva el producto escalar de a y b.
# Es decir, devuelva una vector c de longitud n tal que  c[i] = a[i] · b[i], para i = 0,...,n− 1.
def prod_esc(lista1, lista2):
    resultado = []
    for i in lista1:
        for j in lista2:
            resultado[i] = lista1[i]*lista2[j]
        #resultado[i] = lista1[i]*lista2[i]
    return resultado
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]

# 1.11 Escribe una función que cuente el numero de vocales en una un cadena de caracteres dada.
frase = str(input("Introduce una cadena de caracteres para contar sus vocales: "))
frase_lista = []
frase_lista.append(frase)
num_vocales = 0
for letra in frase:
    if letra == ("a", "e", "i", "o", "u"): 
        num_vocales = num_vocales + 1
print("El numero total de vocales es: " + str(num_vocales))

# 1.12 Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
"Hola Mundo"     #string
[1, 10, 100]      #list
-25              #int
1.167             #float
["Hola", "Mundo"] #list

# 1.13 Realiza un programa que siga las siguientes instrucciones:
#    • Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#    • Crea un conjunto llamado administradores con los administradores Juan y Marta.
#    • Borra al administrador Juan del conjunto de administradores.
#    • Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#    • Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
def administracion():
    usuarios = ["Marta", "David", "Elvira", "Juan", "Marcos"]
    administradores = ["Juan", "Marta"]
    print("Los usuarios son: ")
    print(usuarios)
    print("Los administradores son: ")
    print(administradores)
    administradores.remove("Juan")
    administradores.append("Marcos")
    print("Despues de todos los cambios: ")
    print("Los usuarios son: ")
    print(usuarios)
    print("Los administradores son:")
    print(administradores)
    return 

# 1.14 Crea un script llamado tabla.py que realice las siguientes tareas:
#    • Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
#    • El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
#    • En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
#    • El script contendrá un bucle for que itere el número de veces del primer argumento.
#    • Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
#    • Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.
#    • Ejecuta el código y observa el resultado.
#    • Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.
filas = input("Introduce el numero de filas siendo este un numero entero positivo. ")
columnas = input("Introduce el numero de columnas siendo este un numero entero positivo. ")

def tabla(filas, columnas):
    for i in filas:
        print(" * ")
        for j in columnas:
            print(" * ", end='')
tabla(filas, columnas)
# 1.15 Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
#resultado = 10/0
resultado = 10/0
