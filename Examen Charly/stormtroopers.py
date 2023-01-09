#Creacion
class Stormtrooper:
  def __init__(self, nombre, rango):
    self.nombre = nombre
    self.rango = rango
    print("Stormtrooper {} de rango {} creado con éxito!".format(self.nombre, self.rango))
      
class clasificación(Stormtrooper):
  def init(self, nombre, rango, codigo_legion, identificador_cohorte, identificador_siglo, identificador_escuadra, numero_trooper):
    Stormtrooper.init(self, nombre, rango)
    self.codigo_legion = codigo_legion
    self.identificador_cohorte = identificador_cohorte
    self.identificador_siglo= identificador_siglo
    self.identificador_escuadra = identificador_escuadra
    self.numero_trooper = numero_trooper
      
#Experimentacion      
stormtroopers = []

for i in range(10):
  stormtrooper = Stormtrooper("Stormtrooper"+str(i), "Cabo")
  stormtroopers.append(stormtrooper)
  
for stormtrooper in stormtroopers:
  stormtrooper.calificacion()