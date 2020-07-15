import numpy as np

vector_x = [1, 2, 5]
vector_y = [2, 4, 8]
vector = np.append(vector_x, vector_y)
print(vector)
vector_z = [-6, 0, 1]
vector = np.append(vector_x, [vector_y, vector_z])
print(vector)
"""                                                                   
Ao especificar o parametro 'axis', o parametro 'values' deve possuir
as mesmas dimensoes do parametro 'axis'. """
matrix_x = [vector_x, vector_y]
print(matrix_x)
matrix_x = np.array(matrix_x)
print(matrix_x.shape)
vector_z = np.array(vector_z)
print(vector_z.shape)
matrix = np.append(matrix_x, vector_z, axis=0)  # Proposital print(matrix)
