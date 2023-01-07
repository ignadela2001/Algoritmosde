#Ejericio 1
#En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una
#plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban
#apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo. A
#los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera,
#con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse encima de otro más pequeño. 
#Se dijo a los sacerdotes que, cuando hubieran terminado de mover
#los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.

from lib2to3.pytree import Node
from symbol import term
from tempfile import tempdir


def TorreHanoi(n, i, f, aux):   
    if n > 0:
        TorreHanoi(n-1, i, aux, f)
        print ("\nSe mueve el anillo desde torre " + str(i) + " Hasta torre " + str(f))
        TorreHanoi(n-1, aux, f, i)

n = int(input("Introduce el numero de anillos: "))
TorreHanoi(n, 1, 2, 3)

#Ejercicio 2
#Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus
#de forma recursiva y de forma iterativa

matriz = [[5, 6, 9],
          [4, 2, 0],
          [7, 5, 4]]

def determinante(matriz):
    solucion_sarrus = ((matriz[0][0] * matriz[1][1] * matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])+(matriz[2][0]*matriz[0][1]*matriz[1][2]))-((matriz[0][2] * matriz[1][1] * matriz[2][0])+(matriz[1][2] * matriz[2][1] * matriz[0][0])+(matriz[2][2] * matriz[0][1] * matriz[1][0]))
    return solucion_sarrus

determinante(matriz)


#Ejercicio 3
#Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de
#las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los
#algoritmos necesarios para resolver las actividades detalladas a continuación:
#realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las
#mismas de manera descendente;
#   • mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
#   • determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
#   • indicar cuál es la nave que requiere mayor cantidad de tripulación;
#   • mostrar todas las naves que comienzan con AT;
#   • listar todas las naves que pueden llevar seis o más pasajeros;
#   • mostrar toda la información de la nave más pequeña y la más grande.

vehiculos = [("Halcon milenario", 34, 4, 8),("AT-ST", 9, 2, 2),("Estrella de la muerte", 120000, 1381669, 368685),("AT-AT", 44, 3, 40),("X-wing", 13, 2, 0),("Tie Fighter", 6, 1, 0)]
naves = {}
metros = []
tripulacion = []
pasajeros = []
for i in range(vehiculos):
    for j in range(3):
        naves[i] = j

#Ejercicio 4
#Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
#   • restar dos polinomios;
#   • dividir el polinomio por un numero;
#   • eliminar un término;
#   • determinar si un término existe en un polinomio.

class datoPolinomio(object):

    """Clase dato polinomio. """

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y termino"""
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    """Clase Polinomio"""
    def __init__(self):
        """Crea un polinomio de grado 0"""
        self.termino_mayor = None
        self.grado = 1
    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino al polinomio"""
        aux = Node()
        dato = datoPolinomio
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux 
    def modificar_termino(polinomio, termino, valor):
        """Modifica un termino del polinomio."""
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig 
        aux.info.valor = valor
    def obtener_valor(polinomio, termino):
        """Devuelve el valor de un termino del polinomio. """
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig 
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomios y devuelve el resultado. """
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor + pol2.info.valor
                if (obtener_valor(paux, termino) != 0):
                    valor >= obtener_valor(paux, termino)
                    modificar_termino(paux, termino, valor)
                else:
                    agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux