import numpy as np

vector_x = [True, True, True]
vector_x = np.array(vector_x)

vector_y = [True, True, False]
vector_y = np.array(vector_y)

vector = np.all([vector_x, vector_y])
print(vector)

vector_dois = np.all([vector_x, vector_x])
print(vector_dois)

matrix_x = [[True, True], [True, True]]
matrix_x = np.array(matrix_x)

matrix_y = [[True, False], [True, True]]
matrix_y = np.array(matrix_y)

matrix = np.all([matrix_x, matrix_y])
print(vector)

matrix_dois = np.all([matrix_x, matrix_x])
print(matrix_dois)

matrix_tres = np.all(matrix_y, axis=0)
print(matrix_tres)

matrix_quatro = np.all(matrix_y, axis=1)
print(matrix_quatro)
