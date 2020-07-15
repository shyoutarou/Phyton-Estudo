"""
Dividir um arranjo em sub-arranjos ao longo de um eixo tridimensional. Perceber que a função np.split e equivalente a np.split, ou seja, com o parâmetro axis = 2 por padrão

"""

import numpy as np

matrix_x = [[[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24], [26, 28, 30, 32]]]
matrix_x = np.array(matrix_x)
print(matrix_x)
print("")

matrix_x = np.dsplit(matrix_x, 2)
print(matrix_x)
print("")

matrix_x = [[[1, 2, 1], [3, 4, 1], [1, 1, 1]]]
matrix_x = np.array(matrix_x)
print("")

matrix = np.dsplit(matrix_x, [1, 2])
print(matrix)
print("")

matrix_dois = np.dsplit(matrix_x, [2, 4])
print(matrix_dois)
print("")

matrix_tres = np.dsplit(matrix_x, [2, 4, 5])
print(matrix_tres)
print("")

matrix_quatro = np.dsplit(matrix_x, [2, 4, 5])
print(matrix_quatro)