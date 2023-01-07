import itertools

class City:
    def __init__(self, name, distances, costs):
        self.name = name
        self.distances = distances
        self.costs = costs

class TouristSolver:
    def __init__(self, cities):
        self.cities = cities
    
    def solve(self):
        # Inicializamos las variables que almacenarán la mejor solución encontrada
        best_distance = float('inf')
        best_cost = float('inf')
        best_permutation = None
        
        # Generamos todas las permutaciones de ciudades
        for permutation in itertools.permutations(self.cities):
            # Añadimos la ciudad de salida al principio y al final de la permutación
            permutation = [self.cities[0]] + list(permutation) + [self.cities[0]]
            # Calculamos la distancia y el costo de la permutación actual
            distance = 0
            cost = 0
            for i in range(len(permutation) - 1):
                city1 = permutation[i]
                city2 = permutation[i + 1]
                distance += city1.distances[city2]
                cost += city1.costs[city2]
            # Si la permutación actual tiene una distancia menor que la mejor distancia encontrada hasta el momento,
            # o una distancia igual pero un costo menor, actualizamos la mejor solución
            if distance < best_distance or (distance == best_distance and cost < best_cost):
                best_distance = distance
                best_cost = cost
                best_permutation = permutation
        
        # Mostramos la mejor solución encontrada
        print('Mejor permutación:', [city.name for city in best_permutation])
        print('Distancia total:', best_distance, 'km')
        print('Costo total:', best_cost, 'dólares')

# Creamos los objetos City
cities = [City('Concepción del Uruguay', [0, 5678, 7012, 5623, 9834, 2945], [0, 100, 150, 120, 300, 80]),
          City('Rodas', [5678, 0, 7890, 3456, 1234, 5678], [100, 0, 200, 80, 50, 100]),
          City('Tulum', [7012, 7890, 0, 6789, 2345, 1234], [150, 200, 0, 180, 250, 140]),
          City('Phuket', [5623, 3456, 6789,
