import numpy   as   np

matrix_x = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
matrix_x = np.array(matrix_x)
matrix_y = np.delete(matrix_x, 1, 0)
print(matrix_y)

matrix_z = np.delete(matrix_x, [0, 2], 1)
print(matrix_z)

matrix_w = np.delete(matrix_x, [0, 2, 5], axis=None)
print(matrix_w)
