import random
import numpy as np
import matplotlib.pyplot as plt
  
def graphic(a, b, func):
    N = 1000
    max = 0.0
    plt_values = []
  
    for i in range(N):
        array = np.zeros(N)
  
        for i in range (len(array)):
            array[i] = random.uniform(a,b)
  
            integral = 0.0
  
        for i in array:
            integral += func(i)
  
        answer = (b-a)*integral/float(N)
    
        plt_values.append(answer)

    print ("Значення інтегралу: {:.6f}.".format(answer))    

    plt.title("Обчислені розподіли площ")
    plt.hist (plt_values, bins=30, ec="black") 
    plt.xlabel("Площі")
    plt.show()

    return answer