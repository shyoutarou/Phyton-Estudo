import numpy as np

"""
np.zeros(# de vezes, # de linhas, # de colunas)
"""

num_de_variaveis = 3
K = 2

print("")
print("Um")
soma_medioides = np.zeros((1, K, num_de_variaveis), dtype=float)
print(soma_medioides)

print("")
print("Dois")
soma_medioides = np.zeros((1, num_de_variaveis, K), dtype=float)
print(soma_medioides)

print("")
print("Três")
soma_medioides = np.zeros((K, 1, num_de_variaveis), dtype=float)
print(soma_medioides)

print("")
print("Três-Dois")
soma_medioides[0, 0, 2] = 9
print(soma_medioides)

print("")
print("Quatro")
soma_medioides = np.zeros((K, num_de_variaveis, 1), dtype=float)
print(soma_medioides)

print("")
print("Cinco")
soma_medioides = np.zeros((num_de_variaveis, 1, K), dtype=float)
print(soma_medioides)

print("")
print("Seis")
soma_medioides = np.zeros((num_de_variaveis, K, 1), dtype=float)
print(soma_medioides)
