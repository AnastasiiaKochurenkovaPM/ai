import numpy as np
from integration import integral
from graphic import graphic
from errors import err
  
def f_main(x):
    return np.exp(x**2)

def f_test(x):
    return x**2

print("Функція e^x^2")
integr1 = integral(1, 2, f_main)
err(integr1, 14.989976)

print("Функція x^2")
integr2 = integral(0, 1, f_test)
err(integr2, 1/3)

graphic(1, 2, f_main)
graphic(0, 1, f_test)