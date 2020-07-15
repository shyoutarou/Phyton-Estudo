import numpy as np

x = np.zeros((2, 2))
print(x)
print(type(x))
x = [[2, 3], [4, 7]]
print(x)
print(type(x))
print("")

y = np.zeros((2, 3))
print(y)
print(type(y))
y = [[-2, 8, 6], [8, -4, 1]]
print(y)
print(type(y))
print("")

# Perceber o ponto após os números
z = np.zeros((3, 4), dtype = int)
print(z)
print(type(z))
z = [[1, 3, 12.2, -4], [5, 7, -2.3, 11], [-7, 2, 2.5, 7.1]]
print(z)
print(type(z))