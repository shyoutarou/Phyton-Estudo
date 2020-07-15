import numpy as np

matrix = [[1, 2, 4, 8],
          [16, 32, 64, 128],
          [256, 512, 1024, 2048]]

# A estrutura de repetição abaixo trata-se apenas de um exemplo
# de como gerar a matrix acima
matrix_dois = np.zeros((3, 4))
k = 0
for i in range(0, 3, 1):
    for j in range(0, 4, 1):
        matrix_dois[i, j] = 2 ** k
        k = k + 1
print(matrix_dois)

# A nested List Comprehensions abaixo gera a matrix transposta
# de qualquer uma das matrixes acima, no caso, da matrix
matrix_transposta = [[linha[i] for linha in matrix]
                     for i in range(0, 4, 1)]

matrix_transposta = np.array(matrix_transposta)

print(matrix_transposta)

# O exemplo acima se equivale ao exemplo abaixo
matrix_transposta_dois = []
for i in range(4):
    matrix_transposta_dois.append([linha[i] for linha in matrix_dois])

print("")
print(matrix_transposta_dois)

# Ou então, ao exemplo abaixo
matrix_transposta_tres = []
for i in range(4):
    linha_transposta = []
    for linha in matrix:
        linha_transposta.append(linha[i])
    matrix_transposta_tres.append(linha_transposta)

print(matrix_transposta_tres)
