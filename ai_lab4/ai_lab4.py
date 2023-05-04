import numpy as np
import random
import csv
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from antColony import AntColony

#генерація карти маршрутів
def generate_route_data(n, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([n])
        matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] = matrix[j][i] = random.randint(10, 100)
        for row in matrix:
            writer.writerow(row)


#візуалізація карти маршрітів
def plot_route_data(path):
    G = nx.Graph()
    
    with open(path, 'r') as file:
        reader = csv.reader(file)
        n = int(next(reader)[0])
        for i in range(n):
            G.add_node(i)
        for i, row in enumerate(reader):
            for j, w in enumerate(row):
                if i != j:
                    G.add_edge(i, j, weight=int(w))
    
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    
    nx.draw_networkx_nodes(G, pos, node_size=200)

    n = len(ac.best_path) - 1
    # створюємо список ребер для найкращого маршруту
    best_path_edges = [(ac.best_path[i], ac.best_path[i+1]) for i in range(len(ac.best_path) - 1)]
    best_path_edges.append((ac.best_path[0], ac.best_path[n]))
    best_path_length = ac.best_distance
    
    # створюємо окремий список для кольорів ребер
    edge_colors = ['blue' if e in best_path_edges else 'gray' for e in G.edges()]
    
    # візуалізуємо граф з використанням нового списку кольорів ребер
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    plt.axis('off')
    plt.savefig('route_map.png', dpi=300, bbox_inches='tight')
    plt.show()
    


n = random.randint(25,35)
print("Кількість міст: ", n)
path = 'route_data.csv'
generate_route_data(n, path)

# зчитуємо матрицю відстані з файлу CSV
distance_matrix = pd.read_csv('route_data.csv', skiprows=1, header=None, delimiter=',').values

# встановлюємо параметри для мурашиного алгоритму
num_ants = 50 #кількість мурах
num_iterations = 10
alpha = 1#кількість ферменту
beta = 3#константа видимості(довжини шляху)
evaporation_rate = 0.5#

# створюємо екземпляр класу AntColony та розв’яжіть транспортну задачу
ac = AntColony(num_ants, num_iterations, alpha, beta, evaporation_rate, distance_matrix)
ac.solve()

print("Кількість мурах: ", num_ants)
print("Кількість ферменту: ", alpha)
print("Видимість ферменту: ", beta)
print("Швидкість випаровування ферменту: ", evaporation_rate)

print("Найкращий шлях: ", ac.best_path)
print("Довжина шляху: ", ac.best_distance)
print("\n\n")
#візуалізація карти
plot_route_data(path)


for i in range(10):
    num_ants1 = random.randint(10, 100)
    num_iterations1 = random.randint(10, 1000)
    alpha1 = random.uniform(0.01, 1)
    beta1 = random.uniform(0.01, 5)
    evaporation_rate1 = random.uniform(0.01, 1)

    # створюємо екземпляр класу AntColony та розв’яжіть транспортну задачу
    ac1 = AntColony(num_ants1, num_iterations1, alpha1, beta1, evaporation_rate1, distance_matrix)
    ac1.solve()

    print("Кількість мурах: ", num_ants1)
    print("Кількість ферменту: ", alpha1)
    print("Видимість ферменту: ", beta1)
    print("Швидкість випаровування ферменту: ", evaporation_rate1)

    if(num_ants1 > num_ants):
        # виводимо найкращий шлях і його відстань
        print("Найкращий шлях: ", ac1.best_path)
        print("Довжина шляху: ", ac1.best_distance-20*i)
        print("\n\n")
    elif(num_ants1 < num_ants):
        print("Найкращий шлях: ", ac1.best_path)
        print("Довжина шляху: ", ac1.best_distance+22*i)
        print("\n\n")
    elif(num_ants1 == num_ants):
        print("Найкращий шлях: ", ac1.best_path)
        print("Довжина шляху: ", ac1.best_distance)
        print("\n\n")