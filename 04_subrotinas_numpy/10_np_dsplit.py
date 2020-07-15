import numpy as np

matrix_x = [[[2, 4, 6, 8],
             [10, 12, 14, 16],
             [18, 20, 22, 24],
             [26, 28, 30, 32]]]
matrix_x = np.array(matrix_x)

matrix_x = np.dsplit(matrix_x, 2)
print(matrix_x)

matrix_x = [[[1, 2, 1],
            [3, 4, 1],
            [1, 1, 1]]]
matrix_x = np.array(matrix_x)
matrix = np.dsplit(matrix_x, [1, 2])
print(matrix)

matrix_dois = np.dsplit(matrix_x, [2, 4])
print(matrix_dois)

matrix_tres = np.dsplit(matrix_x, [2, 4, 5])
print(matrix_tres)

matrix_quatro = np.dsplit(matrix_x, [2, 4, 5])
print(matrix_quatro)
