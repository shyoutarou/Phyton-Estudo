"""
Calcular o produtório dado pela Equação:

P = c x (c + 1) x (c + 2 ) x ... x (c + (n - 2)) x (c + (n - 1)) x n

"""

i = input("Digite o valor inicial (i): ")
i = int(i)

n = input("Digite o valor final (n): ")
n = int(n)

passo = 1
P = 1

for i in range(i, n + 1, passo):
    P = P * i
print(P)