"""
Diferente da função Range original, a função Arange do Numpy aceita decimal e já transforma o resultado em array.
"""

import numpy as np

x = np.arange(1, 10, 1)
print(x)
print(type(x))
print("")

y = np.arange(-3, 5, 0.1)
print(y)
print(type(y))
print("")

z = np.arange(0, 37, 0.005)
print(z)
print(type(z))
print("")

w = np.arange(0.5, 22.7, 2)
print(w)
print(type(w))
print("")

k = np.arange(1.7, 12.8, 0.127)
print(k)
print(type(k))
print("")

j = np.arange(-89.4, 54.2, 0.02)
print(j)
print(type(j))
print("")
