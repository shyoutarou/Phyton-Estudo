
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposta = []
for i in range(len(matrix[0])):
    linha_transposta = []
    for linha in matrix:
        linha_transposta.append(linha[i])
    transposta.append(linha_transposta)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(transposta)

transposta =  [[linha[i]  for  linha in matrix]  for  i in  range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(transposta)