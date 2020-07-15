"""
15/fev/2020

James Gregory (1638 - 1675)

Circuli Quadratura (1667)

ArcTg(x) = x - (x ^ 3) / 3 + (x ^ 5) / 5 - (x ^ 7) / 7 + (x ^ 9) / 9 - (x ^ 11) / 11 + (x ^ 13) / 13 +  ...

Expansão em série de Taylor.
"""

import math as math

x = float(input("Digite o valor da Tangente: "))
n = int(input("Digite o valor para quantidade de termos da série de Taylor e Maclaurin: "))

inicio = 1
passo = 2

radianos = 0

# k = Variavel auxiliar para altenar o valor do sinal do coeficiente
k = 2

# 0 '2 * n' no parâmetro final é para dar possibilidade de calcular até o expoente 19, já que o passo é de 2.

for i in range(inicio, 2 * n, passo):
    coeficiente = ((-1) ** k) / i
    radianos = radianos + coeficiente * x ** i
    k = k + 1

print("O valor do Ângulo (rad) é de: " + str(radianos) + " rad")

graus = radianos * 180 / math.pi

print("O valor do Ângulo (graus) é de: " + str(graus))