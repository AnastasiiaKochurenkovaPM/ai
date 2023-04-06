import numpy as np

def err(integral_value, exact_value):
    abs_error = abs(integral_value - exact_value)
    rel_error = abs_error / abs(exact_value)

    print("Абсолютна похибка: {:.6f}".format(abs_error))
    print("Відносна похибка: {:.6f}\n".format(rel_error))