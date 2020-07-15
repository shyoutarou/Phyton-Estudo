"""
Problema: em um sorteio de 2 números aleatórios, qual a média dos pontos?
"""

from random import *
from numpy import *

num_de_pontos = int(input("Digitar o número de pares de pontos aleatórios que deverão ser gerados: "))
print("n / " + "x(1) | " + "y(1) | " + "x(2) | " + "y(2) | " + "Distância")
n = 0
distancia = zeros(num_de_pontos)
while n <= num_de_pontos - 1:
    x1 = random.random()
    y1 = random.random()
    x2 = random.random()
    y2 = random.random()
    distancia[n] = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
