import random
import numpy as np
import matplotlib.pyplot as plt
  
def graphic(a, b, func):

    inside = 0
    n = 1000

    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(a, b)
        if y <= func(x):
            inside += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)


    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.scatter(x_inside, y_inside, color='g', marker='s')
    ax.scatter(x_outside, y_outside, color='r', marker='s')
    fig.show()
    # s = 0
    # n=1000
    # x_vals = []
    # y_vals = []
    # for i in range(n):
    #     x = random.uniform(a, b)
    #     y = random.uniform(a, b)
    #     f = func(x)
    #     s += y
    #     x_vals.append(x)
    #     y_vals.append(y)
    # result = s * (b - a) / n
    # # plt.hist(x_vals, bins=20, density=True, alpha=0.6, color='blue')
    # x = np.linspace(a, b, 100)
    # plt.plot(x, f, color='red', lw=2)

    # plt.scatter(x_vals, y_vals, color='blue', s=.1)
    
    # plt.show()
    # return result
    # N = 1000
    # max = 0.0
    # plt_values = []
  
    # for i in range(N):
    #     array = np.zeros(N)
  
    #     for i in range (len(array)):
    #         array[i] = random.uniform(a,b)
  
    #         integral = 0.0
  
    #     for i in array:
    #         integral += func(i)
  
    #     answer = (b-a)*integral/float(N)
    
    #     plt_values.append(answer)

    # plt.title("Обчислені розподіли площ")
    # plt.hist (plt_values, bins=30, ec="black") 
    # plt.xlabel("Площі")
    # plt.show()