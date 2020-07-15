import numpy   as   np

matrix_x = [[1, 2, 1],
            [3, 4, 1],
            [1, 1, 1]]
matrix_x = np.array(matrix_x)
vector_y = [[5, 6, 1]]
vector_y = np.array(vector_y)
vector = np.concatenate((matrix_x, vector_y), axis=0)
print(vector)
vector_z = [[-6, 0, 1]]
vector_z = np.array(vector_z)
print(vector_z)

vector = np.concatenate((matrix_x, vector_z.T), axis=1)
print(vector)

vector = np.concatenate((matrix_x, vector_y), axis=None)
print(vector)
