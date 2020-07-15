"""
Fatorial
Calcular o fatorial de um número dado pela Equação
n! = 1 x 2 x 3 x ... x (n - 2) x (n - 1) x n
"""

n = input("Digitar o número para ser calculado seu fatorial: ")
n = int(n)

if n < 1:
    quit()

f = 1

for i in range(1, n + 1, 1):
    f = f * i
print("O fatorial do número digitado n = " + str(n) + " é " + str(f) + ".")
