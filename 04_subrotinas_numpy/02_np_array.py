# Função np.array
print("=======ONE========")
import numpy   as   np
x = np.array([[1, 2], [3, 4]])

print(x)
print(type(x))
y = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
print(y)
print(type(y))

#   Perceber   o  ponto   apos   os   numeros
z = np.array([[1, 3], [5, 7]], dtype=float)
print(z)
print(type(z))

print("\n=======TWO========")
x = np.zeros((2, 2))
print(x)
print(type(x))

x = [[2, 3], [4, 7]]
print(x)
print(type(x))

y = np.zeros((2, 3))
print(y)
print(type(y))

y = [[-2, 8, 6], [8, -4, 1]]
print(y)
print(type(y))

# Perceber o ponto apos os numeros
z = np.zeros((3, 4))  # , dtype = float)
print(z)
print(type(z))

z = [[1, 3, 12.2, -4], [5, 7, -2.3, 11], [-7, 2, 2.5, 7.1]]
print(z)
print(type(z))

print("\n=======THREE========")
x = np.ones((2, 2))
print(x)
print(type(x))

x = [[2, 3], [4, 7]]
print(x)
print(type(x))

y = np.ones((2, 3))
print(y)
print(type(y))

y = [[-2, 8, 6], [8, -4, 1]]
print(y)
print(type(y))

# Perceber o ponto apos os numeros
z = np.ones((3, 4))  # , dtype = float)
print(z)
print(type(z))

z = [[1, 3, 12.2, -4], [5, 7, -2.3, 11], [-7, 2, 2.5, 7.1]]
print(z)
print(type(z))
