import numpy as np
import random
import math
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


# генеруємо послідовність з пар дійсних чисел
def generate_data(n):
    data = []
    for i in range(n):
        x = random.random()
        y = random.random()
        data.append((x, y))
    return np.array(data) 


def plot_kmeans(X, y_kmeans, centers):
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='summer')
    plt.scatter(centers[:, 0], centers[:, 1], c='blue', s=100, alpha=0.9)
    plt.show()


# алгоритм кластеризації за методом К-середні
def k_means(data, k, max_iter):
    n = len(data)
    
    labels = np.random.randint(k, size=n)
    
    for i in range(max_iter):
        centers = np.array([np.mean(data[labels == j], axis=0) for j in range(k)])
        new_labels = np.argmin(np.linalg.norm(data - centers[:, np.newaxis], axis=2), axis=0)
        if np.array_equal(labels, new_labels):
            break
        
        labels = new_labels
    
    return labels, centers


#метод по-шарової кластеризації
def spherical_clustering(data, R): 
    n = len(data)
    labels = np.zeros(n, dtype=int)
    num_clusters = 0
    used_indices = set()
    
    # Оберемо випадкову точку як центр першого кластеру
    idx = random.randint(0, n-1)
    center = data[idx]
    labels[idx] = num_clusters
    used_indices.add(idx)
    num_clusters += 1
    
    while len(used_indices) < n:
        # Знайдемо всі точки, які знаходяться в радіусі R від центру кластеру
        indices = np.array(list(set(range(n)) - used_indices))
        distances = cdist(np.array([center]), data[indices])[0]
        neighbor_indices = indices[distances < R]
        
        if len(neighbor_indices) == 0:
            idx = random.choice(list(set(range(n)) - used_indices))
            center = data[idx]
            labels[idx] = num_clusters
            used_indices.add(idx)
            num_clusters += 1
        else:
            center = np.mean(data[neighbor_indices], axis=0)
        for i in neighbor_indices:
            labels[i] = num_clusters
            used_indices.add(i)
        num_clusters += 1
        
    centers = [np.mean(data[labels == j], axis=0) for j in range(num_clusters)]
    return labels, centers    


k = 15 #кількість кластерів
max_iterations = 100
data = generate_data(1000)
sum1 = 0
sum2 = 0
count = 0
kmeans_clusters, centers = k_means(data, k, max_iterations)
spherical_clusters, cent = spherical_clustering(data, 0.8)

# Порівняння результатів
print("Метод K-середніх:")
print("Кількість кластерів:", len(np.unique(kmeans_clusters)))
for i in range(len(np.unique(kmeans_clusters))):
    cluster_size = np.sum(kmeans_clusters == i)
    sum1 += cluster_size
    cluster_center = np.mean(data[kmeans_clusters == i], axis=0)
    print("Кластер", i, "розмірність:", cluster_size, "центр:", cluster_center)

avg1 = sum1 / 5
plot_kmeans(data, kmeans_clusters, centers)

print("\nМетод по-шарової кластеризації:")
print("Кількість кластерів:", len(np.unique(spherical_clusters)))
for i in range(len(np.unique(spherical_clusters))):
    cluster_size = np.sum(spherical_clusters == i)
    sum2 += cluster_size
    count = count + 1
    cluster_center = np.mean(data[spherical_clusters == i], axis=0)
    print("Кластер", i, "розмірність:", cluster_size, "центр:", cluster_center)

avg2 = sum2 / count
plot_kmeans(data, spherical_clusters, np.array(cent))

print("Середньо-зважене розмірів утворених кластерів:\nМетод К-середніх: ", avg1, "\nМетод по-шарової кластеризації: ", avg2)