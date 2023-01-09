class ArtefactosValiosos:
    def __init__(self, nombre, peso, precio, fecha_de_caducidad):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fecha_de_caducidad = fecha_de_caducidad
        print ("Artefacto creado con éxito")

    def __str__(self):
        return 'Artifacto: {}, Peso: {}, Precio: {}, Fecha de Caducidad: {}'.format(self.nombre, self.peso, self.precio, self.fecha_de_caducidad)