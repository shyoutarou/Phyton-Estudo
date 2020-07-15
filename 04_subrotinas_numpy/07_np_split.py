import numpy as np

vector_x = [2, 4, 6, 8, 10, 12, 14,
            16, 18, 20, 22, 24, 26,
            28, 30, 32, 34, 36]
vector_x = np.array(vector_x)
matrix_x = np.split(vector_x, 3)
print(matrix_x)

matrix_x = [[1, 2, 1],
            [3, 4, 1],
            [1, 1, 1]]
matrix_x = np.array(matrix_x)
matrix = np.split(matrix_x, 3)
print(matrix)

matrix_dois = np.split(vector_x, [2, 4])
print(matrix_dois)

matrix_tres = np.split(matrix_x, [2, 4, 5])
print(matrix_tres)

matrix_quatro = np.split(matrix_x, [2, 4, 5], axis=1)
print(matrix_quatro)
