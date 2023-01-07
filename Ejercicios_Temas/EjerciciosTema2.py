import numpy as np
#Ejercicio 1



#a)
A = []
x = input("Introduce la coordenada x del punto A")
if x == " ":
    x = 0
A.append(x)
y = input("Introduce la coordenada y del punto A")
if y == " ":
    y = 0
A.append(y)
cuadrante = 0
if x > 0:
    if y > 0:
        cuadrante = 1
    elif y < 0:
        cuadrante = 4
elif x < 0:
    if y > 0:
        cuadrante = 2
    elif y < 0:
        cuadrante = 3
elif x == 0:
    if y == 0:
        cuadrante = "Punto de origen."
print(A + "Es el punto A que se encuentra en el "+ cuadrante + "º cuadrante.")





#b)
B = []
x2 = input("Introduce la coordenada x del punto A")
if x2 == " ":
    x2 = 0
B.append(x2)
y2 = input("Introduce la coordenada y del punto A")
if y2 == " ":
    y2 = 0
B.append(y2)
cuadrante2 = 0
if x2 > 0:
    if y2 > 0:
        cuadrante2 = 1
    elif y2 < 0:
        cuadrante2 = 4
elif x2 < 0:
    if y2 > 0:
        cuadrante2 = 2
    elif y2 < 0:
        cuadrante2 = 3
elif x2 == 0:
    if y2 == 0:
        cuadrante2 = "Punto de origen."
print(B + "Es el punto A que se encuentra en el "+ cuadrante2 + "º cuadrante.")






#c)
vector = []
xv = x - x2
yv = y - y2
vector.append(xv)
vector.append(yv)
print("El vector formado por los puntos A y b es:" + vector)
#d)
d = np.sqrt(((x2-x)^2)+((y2-y)^2))
print("La distancia entre los puntos A y B es: " + d)

#Ejercicio 2
class Vehiculo():
  def _init_(self, color, ruedas):
    self.color = color
    self.ruedas = ruedas
  def _str_(self):
    return "color {}, {} ruedas".format( self.color, self.ruedas )
class Coche(Vehiculo):
  def _init_(self, color, ruedas, velocidad, cilindrada):
    Vehiculo._init_(self, color, ruedas)
    self.velocidad = velocidad
    self.cilindrada = cilindrada
  def _str_(self):
    return Vehiculo._str_(self) + f'velocidad {self.velocidad}, cilindrada {self.cilindrada}'
class Camioneta(Coche):
  def _init_(self, color, ruedas, velocidad, cilindrada, carga):
    Coche._init_(self, color, ruedas, velocidad, cilindrada)
    self.carga = carga
  def _str_(self):
    return Coche._str_(self) + f' carga{self.carga}'
class Bicicleta(Vehiculo):
  def _init_(self, color, ruedas, tipo):
    Vehiculo._init_(self, color, ruedas)
    self.tipo = tipo
  def _str_(self):
    return Vehiculo._str_(self) + f' tipo {self.tipo},'
class Motocicleta(Bicicleta):
    def _init_(self, color, ruedas, tipo, velocidad, cilindrada):
      Bicicleta._init_(self, color, ruedas, tipo)
      self.velocidad = velocidad
      self.cilindrada = cilindrada
    def _str_(self):  
      return Bicicleta._str_(self) + f'velocidad {self.velocidad}, cilindrada {self.cilindrada}'
def Catalogar(vehiculos,rueda):
  for i in vehiculos:
    if i.ruedas == rueda:
      print(type(i)._name_, i)
vehiculos = [Coche("verde", 4, 150, 1200), Camioneta("blanca", 4, 150, 1200,6000), Bicicleta("negra", 2, 'calle'), Motocicleta("verde", 2, 'urbana', 150, 1200)]     
Catalogar(vehiculos,4)