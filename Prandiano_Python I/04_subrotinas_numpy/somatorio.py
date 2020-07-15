"""
Calcular o somatório dado pela Equação
S = x1 + x2 + x3 + ... + xn-2 + xn-1 + xn
"""

i = 1
n = 100
passo = 1
S = 0

for i in range(i, n + 1, passo):
    S = S + i
print(S)
