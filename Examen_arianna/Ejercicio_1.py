#Ejercicio 1

from math import pi
import pickle 


#0.5 puntos

class Figura:
    '''Clase base
    '''

    def __init__(self, color, area) -> None:
        self.color = color
        self.area = area

    def __str__(self) -> str:
        return '{} {}'.format(self.color, self.area)

    #Sobreescribimos estos operadores necesarios para la funcion comparar_areas_v2() 
    
    def __eq__(self, __o: object) -> bool:
        return self.area  == __o.area

    def __gt__(self, __o: object) -> bool:
        return self.area  > __o.area

    def __lt__(self, __o: object) -> bool:
        return self.area  < __o.area

class Triangulo(Figura):
    '''Clase triangulo que extiende la clase base Figura'''

    def __init__(self, color, base, altura) -> None:
        super().__init__(color, base*altura*0.5)
        self.base = base
        self.altura = altura


class Cuadrado(Figura):
    '''Clase cuadrado que extiende la clase base Figura'''

    def __init__(self, color, lado) -> None:
        super().__init__(color, lado*lado)
        self.lado = lado


class Circulo(Figura):
    '''Clase cuadrado que extiende la clase base Figura'''

    def __init__(self, color, radio) -> None:
        super().__init__(color, pi*radio*radio)
        self.radio = radio

lista_figuras = []

lista_figuras.append(Triangulo("rojo", 2.0, 1.0))
lista_figuras.append(Cuadrado("azul",2.0))
lista_figuras.append(Circulo("verde", 3.0))


#0.5 puntos

def catalogar(list_fig):
    '''Funcion catalogar que muestra el nombre de cada clase y sus atributos haciendo uso 
    del metodo __str__ implementado en la clase base
    '''
    for fig in list_fig:
        print("clase {} con atributos {}".format(type(fig).__name__, fig))


catalogar(lista_figuras)

print()

#0.5 puntos

def mostrar_areas(list_fig):
    '''funcion que muestra las areas de las figuras
    '''
    for fig in list_fig:
        print("La figura {} tiene un area de {} m2".format(type(fig).__name__, fig.area))

mostrar_areas(lista_figuras)

print()

#0.5 puntos

def comparar_areas(list_fig):
    '''funcion que compara las areas de las figuras
    '''
    for fig1 in list_fig:
            for fig2 in list_fig:
                if fig1 is not fig2:

                    if fig1.area == fig2.area:
                        print("Las figuras {} y {} tienen el area {} m2".format(type(fig1).__name__, type(fig2).__name__, fig1.area))
                    elif fig1.area > fig2.area:
                        print("Las figura {} tiene un area mayor que la {}: {} > {}".format(type(fig1).__name__, type(fig2).__name__, fig1.area, fig2.area))
                    else: 
                        print("Las figura {} tiene un area menor que la {}: {} < {}".format(type(fig1).__name__, type(fig2).__name__, fig1.area, fig2.area))


comparar_areas(lista_figuras)

print()


#0.5 puntos

def comparar_areas2(list_fig):
    '''
    '''
    for fig1 in list_fig:
            for fig2 in list_fig:
                if fig1 is not fig2:

                    if fig1 == fig2:
                        print("Las figuras {} y {} tienen el area {} m2".format(type(fig1).__name__, type(fig2).__name__, fig1.area))
                    elif fig1 > fig2:
                        print("Las figura {} tiene un area mayor que la {}: {} > {}".format(type(fig1).__name__, type(fig2).__name__, fig1.area, fig2.area))
                    else: 
                        print("Las figura {} tiene un area menor que la {}: {} < {}".format(type(fig1).__name__, type(fig2).__name__, fig1.area, fig2.area))


comparar_areas2(lista_figuras)

print()


#0.25 puntos

def guardar_figuras(list_fig, filename):
    '''
    '''
    filehandler = open(filename, 'wb') 
    pickle.dump(list_fig, filehandler)
    filehandler.close


guardar_figuras(lista_figuras, "figuras.obj")

print()


#0.25 puntos

def leer_figuras(filename):
    '''
    '''
    file_pi = open(filename, 'rb') 
    object_pi = pickle.load(file_pi)
    file_pi.close
    return object_pi


lista_figuras = leer_figuras("figuras.obj")

for i in lista_figuras:
    print(i)

print()
