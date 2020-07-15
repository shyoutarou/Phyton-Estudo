"""
15/fev/2020

Sheila May Edmonds (1916 - 2002)

Sums of powers of the natural numbers (1957)

1 + 2 + 3 + ... + n = (1 ^ 3 + 2 ^ 3 + 3 ^ 3 + ... + n ^ 3) ^ (1 / 2)

"""

import numpy as np

fim = int(input("Digitar o valor do último termo: "))

inicio = 0
passo = 1

S = 0
R = 0

for n in range(inicio, fim + 1, passo):
    S = S + n
    R = R + n ** 3

R = R ** (1 / 2)
# R = np.sqrt(R) Dá overflow quando coloca um valor muito alto

print("O valor do lado esquerdo da igualdade é: " + str(S))
print("O valor do lado direito da igualdade é: " + str(R))