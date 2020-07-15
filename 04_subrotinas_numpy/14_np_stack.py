import numpy   as   np

vector_x = [2, 4, 6, 8, 10, 12, 14]
vector_x = np.array(vector_x)

vector_y = [16, 18, 20, 22, 24, 26, 28]
vector_y = np.array(vector_y)

matrix_x = np.stack((vector_x, vector_y))
print(matrix_x)

matrix_y = np.stack((vector_y, vector_x))
print(matrix_y)

vector_w = [1, 2, 3, 4, 5, 6, 7, 8]
vector_w = np.array(vector_w)
matrix_k = np.stack((vector_x, vector_w), axis=1)  # Proposital print(matrix_k)
print(matrix_k)

matrix_m = np.stack((vector_x, vector_w), axis=0)  # Proposital print(matrix_m)
print(matrix_m)
