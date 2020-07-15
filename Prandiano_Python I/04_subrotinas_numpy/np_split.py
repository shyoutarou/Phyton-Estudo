"""
Dividir um arranjo em sub-arranjos
"""

import numpy as np

vector_x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
print(vector_x)
print("")
vector_x = np.array(vector_x)
print(vector_x)
print("")

matrix_x = np.split(vector_x, 3)
print(matrix_x)
print("")

matrix_x = [[1, 2, 1], [3, 4, 1], [1, 1, 1]]
print(matrix_x)
print("")
matrix_x = np.array(matrix_x)
print(matrix_x)
print("")

matrix = np.split(matrix_x, 3)
print(matrix)
print("")

matrix_dois = np.split(vector_x, [2, 4])
print(matrix_dois)
print("")

matrix_tres = np.split(matrix_x, [2, 4, 5])
print(matrix_tres)
print("")
""" 
Notar que ele corta nas posições 2, 4 e 5, no sentido da linha.
Na posição 2, ele cortará na posição 2, tendo as linhas [1, 2, 1] e [3, 4, 1].
Na posição 4, ele cortará na posição 4, tendo as linhas [1, 1, 1] e uma linha vazia [] com shape=(0, 3).
Na posição 5, ele cortará na posição 5, tendo uma linha vazia [] com shape=(0, 3).
"""

matrix_quatro = np.split(matrix_x, [2, 4, 5], axis=1)
print(matrix_quatro)
"""
Notar que ele corta nas posições 2, 4 e 5, no sentido da coluna.
Na posição 2, sobra as colunas [1, 2], [3, 4] e [1, 1].
Assim como no exemplo da matrix_tres, ele tentará cortar nas posições 4 e 5, mas conterão colunas vazias.
"""
