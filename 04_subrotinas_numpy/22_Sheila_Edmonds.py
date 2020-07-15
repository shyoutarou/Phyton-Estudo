import numpy as np
import math as mt

fim = input("Digitar o valor do último termo: ")
fim = int(fim)
inicio = 0     #É padrão
passo = 1     #É padrão

s = 0
r = 0

for n in range(inicio, fim + 1, passo):
    s = s + n
    r = r + (n ** 3)

print(r)

""" 
SE Digitar o valor do último termo: 92682
r = 18.447.221.737.294.547.409
AttributeError: 'int' object has no attribute 'sqrt'
Por isso tem que converter para float 
OU Utilizar o math.sqrt OU cmath.sqrt

Na verdade, 2 ** 64 é igual a 18.446.744.073.709.551.616 e, 
de acordo com o padrão dos tipos de dados C (versão C99), 
o tipo inteiro longo e sem sinal contém pelo menos o 
intervalo entre 0 e 18.446.744.073.705.515.615 incluído.

O AttributeError ocorre porque numpy, vendo um tipo que 
não sabe como manipular (após a conversão para o tipo de 
dados C), o padrão é chamar o método sqrt no objeto (mas 
isso não existe). Se usarmos floats em vez de números 
inteiros, tudo funcionará usando numpy:

"""
r = float(r)
r = np.sqrt(r)
# r = mt.sqrt(r)
print(r)

print("O valor do lado esquerdo da igualdade é : " + str(s))
print("O valor do lado direito da igualdade é : " + str(r))
