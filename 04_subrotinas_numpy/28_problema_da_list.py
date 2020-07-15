import numpy as np

bd = [[1, 4], [5, 2], [6, 1],
      [2, 5], [2, 3], [3, 4]]

sementes = np.array(bd)
print("x " + str(sementes.shape))

# n = Número de elementos, ou seja, neste caso, este
# valor também é o número de sementes

n = sementes.shape[0]

# K = número total de grupos para a clusterização
K = sementes.shape[1]

soma_sementes_lista = K * [[]]
print("z" + str(soma_sementes_lista))
"""problema que armazena a lista inteira na memoria"""
for k in range(0, K, 1):
    for i in range(0, n, 1):
        if i == 0:
            k_min = 0
        elif i == 1:
            k_min = 0
        elif i == 2:
            k_min = 0
        elif i == 3:
            k_min = 1
        elif i == 4:
            k_min = 1
        elif i == 5:
            k_min = 0

        soma_sementes_lista[k_min].append(sementes[i])
        print(soma_sementes_lista)
        print("")