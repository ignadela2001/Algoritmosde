import itertools

class City:
    def __init__(self, name):
        self.name = name

# Nombres de las ciudades
names = ['Concepción del Uruguay', 'Rodas', 'Tulum', 'Phuket', 'Tokio', 'Atenas',
         'Orlando', 'Santiago', 'Moscú', 'Bombinhas', 'Londres', 'Paris', 'Sídney', 'Berlín']
# Matrices de distancias y costos
distances = [[]]
costs = [[]]


def create_cities(names, distances, costs):
    cities = []
    for i in range(len(names)):
        city = City(names[i], distances[i], costs[i])
        cities.append(city)
    return cities

class TouristSolver:
    def __init__(self, cities, distances, costs):
        self.cities = cities
        self.distances = distances
        self.costs = costs
    
    def solve(self):
        # Inicializamos las variables que almacenarán la mejor solución encontrada
        best_distance = float('inf')
        best_cost = float('inf')
        best_permutation = None
        
        # Generamos todas las permutaciones de ciudades
        for permutation in itertools.permutations(self.cities[1:]):
            # Añadimos la ciudad de salida al principio y al final de la permutación
            permutation = [self.cities[0]] + list(permutation) + [self.cities[0]]
            # Calculamos la distancia y el costo de la permutación actual
            distance = 0
            cost = 0
            for i in range(len(permutation) - 1):
                city1 = permutation[i]
                city2 = permutation[i + 1]
                city1_index = self.cities.index(city1)
                city2_index = self.cities.index(city2)
                distance += self.distances[city1_index][city2_index]
                cost += self.costs[city1_index][city2_index]
            # Si la permutación actual tiene una distancia menor que la mejor distancia encontrada hasta el momento,
            # o una distancia igual pero un costo menor, actualizamos la mejor solución
            if distance < best_distance or (distance == best_distance and cost < best_cost):
                best_distance = distance
                best_cost = cost
                best_permutation = permutation

                print('Mejor permutación:', [city.name for city in best_permutation])
                print('Distancia total:', best_distance, 'km')
                print('Costo total:', best_cost, 'dólares')

def create_cities(names, distances, costs):
    cities = []
    for i in range(len(names)):
        city = City(names[i], distances[i], costs[i])
        cities.append(city)
    return cities



