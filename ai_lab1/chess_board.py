import numpy as np
from matplotlib import pyplot as plt
from chess_board import simulated_annealing
N_QUEENS = 8

def board (answer):
    image = np.ones(N_QUEENS*N_QUEENS)
    image = image.reshape((N_QUEENS, N_QUEENS))
    line = []
    # line = simulated_annealing(answer)
    index = 0
    for i in answer.pop().solution:
        line = []
        for j in range(1, N_QUEENS+1):
            if i == j:
                line.append(0)
            else:
                line.append(1)
        image[index] = line
        index += 1
    row_labels = range(1, N_QUEENS+1)
    col_labels = range(1, N_QUEENS+1)
    plt.matshow(image)
    plt.xticks(range(N_QUEENS), col_labels)
    plt.yticks(range(N_QUEENS), row_labels)
    plt.show()