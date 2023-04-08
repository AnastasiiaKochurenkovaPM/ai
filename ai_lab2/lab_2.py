import numpy as np
import scipy.integrate as integrate
from integration import integral
from graphic import graphic
from errors import err

a = 1
b = 2
  
def f_main(x):
    return np.exp(x**2)

def f_test(x):
    return x**2

print("Функція x^2")
integr2 = integral(a, b, f_test)
err(integr2, 14.895)

print("Функція e^x^2")
integr1 = integral(a, b, f_main)
err(integr1, )

# graphic(1, 2, f_main)
# graphic(1, 2, f_test)