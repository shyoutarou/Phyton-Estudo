import math as mt

x = float(input("Digitar o valor da tangente: "))
n = int(input("Digitar o valor para a quantidade de termos da séria Taylor-MacLaurin: "))

inicio = 1
passo = 2
radianos = 0
k = 2  #variável auxiliar para alternar o valor do sinal do coeficiente

"""
O parâmetro final 2 * n é para dar a posssibilidade 
de calcular até o expoente 19, já que o passo é de 2
"""
for i in range(inicio, 2 * n, passo):
    coeficiente = ((-1) ** k)
    radianos = radianos + coeficiente * x ** i
    k = k + i

print("O valor do ângulo(rad) é de: " + str(radianos) + " rad")

graus = radianos * 180 / mt.pi
print("O valor do ângulo(graus) é de: " + str(graus) + " graus")