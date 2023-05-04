import numpy as np
import random
from ant import Ant

class AntColony:
    def __init__(self, num_ants, num_iterations, alpha, beta, evaporation_rate, distance_matrix):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.distance_matrix = distance_matrix
        self.pheromone_matrix = np.ones_like(distance_matrix) / distance_matrix.shape[0]
        self.best_path = None
        self.best_distance = float('inf')

    # оновлює матрицю феромонів після того, як усі мураxи завершать свій шлях
    def update_pheromone_matrix(self, paths, distances):
        for i in range(self.distance_matrix.shape[0]):
            for j in range(self.distance_matrix.shape[1]):
                self.pheromone_matrix[i][j] *= (1 - self.evaporation_rate)
        for path, distance in zip(paths, distances):
            pheromone_deposit = 1 / distance
            for i in range(len(path) - 1):
                self.pheromone_matrix[path[i]][path[i+1]] += pheromone_deposit / len(path)

    def solve(self):
        # список мурашок, які рухаються по випадковим містам
        for i in range(self.num_iterations):
            ants = [Ant(random.randint(0, self.distance_matrix.shape[0] - 1),
                       self.distance_matrix.shape[0],
                       self.distance_matrix) for j in range(self.num_ants)]
            paths = []
            distances = []

            # визначаємо наступне місто, доки всі міста не будуть відвідані
            for ant in ants:
                while ant.visited_cities != set(range(self.distance_matrix.shape[0])):
                      next_city = ant.choose_next_city(self.pheromone_matrix, self.alpha, self.beta)
                      if next_city is None:
                          break
                paths.append(list(ant.visited_cities))
                distance = 0
                path = list(ant.visited_cities)
                path.append(path[0])  # додати першу точку у кінець списку
                for i in range(len(path) - 1):
                    distance += self.distance_matrix[path[i]][path[i+1]]
                distances.append(distance)
                # Якщо довжина поточного шляху коротша за найкращий знайдений 
                # шлях, то найкращий шлях і довжина оновлюються
                if distances[-1] < self.best_distance:
                   self.best_distance = distances[-1]
                   self.best_path = paths[-1]
            # оновлення матриці феромонів на основі знайдених шляхів
            self.update_pheromone_matrix(paths, distances)
            path.append(path[0])