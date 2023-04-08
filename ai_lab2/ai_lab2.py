import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.integrate as integrate

a = 1
b = 2
  
def f_main(x):
    return np.exp(x**2)

def f_test(x):
    return x**2

#обчислення значення інтегралу
def integrate_function(a,b,func):
    integrate_value, error = integrate.quad(func, a,b)
    return integrate_value


#обчислення абсолютної та відносної похибки
def err(integral_value, exact_value):
    abs_error = abs(integral_value - exact_value)
    rel_error = abs_error / abs(exact_value)

    print("Абсолютна похибка: {:.6f}".format(abs_error))
    print("Відносна похибка: {:.6f}\n".format(rel_error))


#метод Монте-Карло
def integral_monte_carlo (a,b, func, mode, c, d):
    N = 1000
    array_x = np.zeros(N)
    array_y = np.zeros(N)
  
   # масив випадкових чисел
    for i in range (N):
        array_x[i] = random.uniform(a,b)
        array_y[i] = random.uniform(1, 10)
  
    integral = 0.0 #початкове значення оцінки інтеграла

    for i in array_x:
        integral += func(i)
  
    answer = (b-a)*integral/float(N)
    print ("Значення інтегралу обчисленого методом Монте-Карло: {:.6f}.".format(answer))

    fig, ax = plt.subplots(1,1,figsize=(10,10))
    plt.grid(True)
    plt.ylim(c, d)
    x = np.linspace(a, b, N)
    plt.plot(x, func(x), color="black", linewidth=4)
    for i in range(N):
        plt.plot( array_x[i],  array_y[i], 'ro-' if( array_y[i] > func( array_x[i])) else 'go-', alpha=0.3)

    plt.show()    

    return answer


#виклик функцій
print("Функція x^2")
integr2 = integral_monte_carlo(a, b, f_test, "test", 1, 10)
exact1 = integrate_function(a, b, f_test)
print("Значення інтегралу: {:.6f}.".format(exact1))
err(integr2, exact1)

print("Функція e^x^2")
integr1 = integral_monte_carlo(a, b, f_main, "main", 1, 10)
exact2 = integrate_function(a, b, f_main)
print("Значення інтегралу: {:.6f}.".format(exact2))
err(integr1, exact2)