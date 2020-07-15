from random import *

print("TESTE")

from numpy import *

print("TESTE")

num_de_pontos = input("Digitar o número de pares de pontos aleatórios que deverão ser gerados: ")

num_de_pontos = int(num_de_pontos)
print("n | " + "x(1) | " + "x(2) | ")

n = 0
distancia = zeros(num_de_pontos)

while n <= num_de_pontos - 1:
    x1 = random.random()
    y1 = random.random()
    x2 = random.random()
    y2 = random.random()
    # Pitagoras
    distancia[n] = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

    print(n, "|" + (format(round(x1, 3), "4f")) +
          "|" + (format(round(x1, 3), "4f")) +
          "|" + (format(round(x1, 3), "4f")) +
          "|" + (format(round(x1, 3), "4f")))

    n = n + 1

media = sum(distancia), (n - 1)
print("\n A média das distâncias dos números aleatórios gerado é de " + str(format(round(media, 4), "4f")))
