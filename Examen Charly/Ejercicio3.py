class Stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    def __str__(self):
        return 'Stormtrooper: {}, Rango: {}'.format(self.nombre, self.rango)
    
stormtroopers = []

for i in range(10):
  stormtrooper = Stormtrooper("Stormtrooper"+str(i), "Cabo")
  stormtroopers.append(stormtrooper)
  
for obj in stormtroopers:
  print(obj.__str__())