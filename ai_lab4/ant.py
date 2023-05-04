import numpy as np

class Ant:
    def __init__(self, start_city, num_cities, distance_matrix):
        self.visited_cities = set([start_city])
        self.current_city = start_city
        self.distance_matrix = distance_matrix
        self.num_cities = num_cities
        self.total_distance = 0

    # визначає наступну вершину, яку мураха повинна відвідати
    def choose_next_city(self, pheromone_matrix, alpha, beta):
        # набір міст, які ще не були відвідані мурахою
        unvisited_cities = set(range(self.num_cities)) - self.visited_cities
        probabilities = []
        total_prob = 0
        for city in unvisited_cities:
            pheromone = pheromone_matrix[self.current_city][city]
            distance = self.distance_matrix[self.current_city][city]
            probability = pheromone ** alpha * ((1 / distance) ** beta)
            total_prob += probability
            probabilities.append((city, probability))
        if not probabilities:
            return None
        probabilities = [(city, probability / total_prob) for city, probability in probabilities]
        # вибір наступної вершини з найбільшою ймовірністю
        next_city = max(probabilities, key=lambda x: x[1])[0]
        self.visited_cities.add(next_city)
        self.total_distance += self.distance_matrix[self.current_city][next_city]
        self.current_city = next_city
        return next_city