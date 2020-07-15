"""
Juntar uma sequência de arranjos ao longo de um novo eixo.
"""

import numpy as np

vector_x = [2, 4, 6, 8, 10, 12, 14]
vector_x = np.array(vector_x)
print(vector_x)
print("")

vector_y = [16, 18, 20, 22, 24, 26, 28]
vector_y = np.array(vector_y)
print(vector_y)
print("")

matrix_x = np.stack((vector_x, vector_y), axis=1)
print(matrix_x)
print("")

matrix_y = np.stack((vector_x, vector_y), axis=0)
print(matrix_y)
print("")

vector_w = [1, 2, 3, 4, 5, 6, 7, 8]
vector_w = np.array(vector_w)
print(vector_w)
print("")

#Exemplos abaixo não conseguem ser executados (proposital).
#matrix_k = np.stack((vector_x, vector_w), axis=1)
#print(matrix_k)
#print("")

#matrix_m = np.stack((vector_x, vector_w), axis=0)
#print(matrix_m)