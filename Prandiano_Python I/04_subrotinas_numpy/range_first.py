"""
Range cria uma lista de números INTEIROS, sendo que o critério de parada é aberto.
N = [0, 10[
"""

import numpy as np

x = list(range(0, 10, 1))
print(x)
print(type(x))
print("")

y = list(range(1, 10, 1))
print(y)
print(type(y))
print("")

z = list(range(-10, 10, 1))
print(z)
print(type(z))
print("")

z = np.array(z)
print(type(z))