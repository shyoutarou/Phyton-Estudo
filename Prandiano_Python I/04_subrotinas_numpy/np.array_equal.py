"""
Verificar se dois arranjos possuem a mesma dimensão e os mesmos elementos
"""

import numpy as np

vector_x = [1, 2, 3]
vector_x = np.array(vector_x)
print(vector_x)
print("")

vector_y = [2, 4, 6]
vector_y = np.array(vector_y)
print(vector_y)
print("")

vector = np.array_equal(vector_x, vector_y)
print(vector)
print("")

vector_dois = np.array_equal(vector_x, vector_x)
print(vector_dois)
print("")

matrix_x = [[1, 2], [3, 4]]
matrix_x = np.array(matrix_x)
print(matrix_x)
print("")

matrix_y = [[2, 4], [6, 8]]
matrix_y = np.array(matrix_y)
print(matrix_y)
print("")

matrix = np.array_equal(matrix_x, matrix_y)
print(matrix)
print("")

matrix_dois = np.array_equal(matrix_x, matrix_x)
print(matrix_dois)
print("")