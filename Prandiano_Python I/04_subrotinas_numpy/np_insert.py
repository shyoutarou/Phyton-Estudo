import numpy as np

matrix_x = [[1, 2, 1], [3, 4, 1], [1, 1, 1]]
matrix_x = np.array(matrix_x)
print(matrix_x)
print("")

matrix = np.insert(matrix_x, 2, 99)
print(matrix)
print("")

matrix_dois = np.insert(matrix_x, 2, 99, axis=1)
print(matrix_dois)
print("")

vector_y = [[3], [2], [1]]
vector_y = np.array(vector_y)

"""
Matematicamente o matrix e vector_y são vetores.
Python o matrix é um vetor e o vector_y é uma matriz. Isso é importante pois existem funções no Python que necessitam que seja EXATAMENTE um vetor ou uma matriz, mesmo que matematicamente faça sentido.
"""

matrix_tres = np.insert(matrix_x, [1], vector_y, axis=1)
print(matrix_tres)
print("")

vector_k = [[3, 2, 1]]
vector_k = np.array(vector_k)

matrix_quatro = np.insert(matrix_x, [1], vector_k, axis=1)
print(matrix_quatro)