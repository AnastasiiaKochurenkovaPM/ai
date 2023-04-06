import random
import numpy as np
import matplotlib.pyplot as plt
  
def integral (a,b, func):
    N = 1000
    array = np.zeros(N)
  
   # масив випадкових чисел
    for i in range (len(array)):
        array[i] = random.uniform(a,b)
  
    integral = 0.0 #початкове значення оцінки інтеграла

    for i in array:
        integral += func(i)
  
    answer = (b-a)*integral/float(N)
    print ("Значення інтегралу: {:.6f}.".format(answer))

    return answer