import numpy as np

matrix_x = [[1, 2, 1],
            [3, 4, 1],
            [1, 1, 1]]
matrix_x = np.array(matrix_x)

matrix = np.insert(matrix_x, 2, 99)
print(matrix)

matrix_dois = np.insert(matrix_x, 2, 99, axis=1)
print(matrix_dois)

vector_y = [[3], [2], [1]]
vector_y = np.array(vector_y)

matrix_tres = np.insert(matrix_x, [1], vector_y, axis=1)
print(matrix_tres)
vector_k = [[3, 2, 1]]
vector_k = np.array(vector_k)

matrix_quatro = np.insert(matrix_x, [1], vector_k, axis=1)
print(matrix_quatro)
