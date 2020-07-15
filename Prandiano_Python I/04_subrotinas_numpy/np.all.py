import numpy as np

vector_x = [True, True, True]
vector_x = np.array(vector_x)
print(vector_x)
print("")

vector_y = [True, True, False]
vector_y = np.array(vector_y)
print(vector_y)
print("")

vector = np.all([vector_x, vector_y])
print(vector)
print("")

vector_dois = np.all([vector_x, vector_x])
print(vector_dois)
print("")

matrix_x = [[True, True], [True, True]]
matrix_x = np.array(matrix_x)
print(matrix_x)
print("")

matrix_y = [[True, False], [True, True]]
matrix_y = np.array(matrix_y)
print(matrix_y)
print("")

matrix = np.all([matrix_x, matrix_y])
print(matrix)
print("")

matrix_dois = np.array_equal(matrix_x, matrix_x)
print(matrix_dois)
print("")

matrix_tres = np.all(matrix_y, axis=0)
print(matrix_tres)
print("")

matrix_quatro = np.all(matrix_y, axis=1)
print(matrix_quatro)