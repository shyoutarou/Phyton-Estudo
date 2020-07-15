import numpy as np

vector_x = [1, 2, 5]
vector_y = [2, 4, 8]

vector = np.append(vector_x, vector_y)
print(vector)

vector_z = [-6, 0, 1]
vector = np.append(vector_x, [vector_y, vector_z])
print(vector)

"""
Ao especificar o parâmetro 'axis', o parâmetro 'values' deve possuir as mesmas dimensões do parâmetro 'axis'
"""

matrix_x = [vector_x, vector_y]
print(matrix_x)

matrix_x = np.array(matrix_x)
print(matrix_x.shape)
# Lista não tem shape, tem lenght


vector_z = np.array(vector_z)
print(vector_z.shape)
# Reparar que não gera uma matriz. Uma das dimensões 'some'

# matrix = np.append(matrix_x, vector_z, axis = 0)
# print(matrix)