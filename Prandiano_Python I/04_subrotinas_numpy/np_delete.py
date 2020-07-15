import numpy as np

matrix_x = [[1, 2, 1], [3, 4, 1], [1, 1, 1]]
matrix_x = np.array(matrix_x)
print(matrix_x)
print("")

matrix_y = np.delete(matrix_x, 1, 0)
print(matrix_y)
print("")

matrix_z = np.delete(matrix_x, [0, 2], 1)
print(matrix_z)
print("")

matrix_w = np.delete(matrix_x, [0, 2, 5], axis=None)
print(matrix_w)
print("")
