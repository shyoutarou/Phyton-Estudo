import numpy as np

# na forma tradicional
triangulo_de_pascal = []
# Perceber que, a regra de elevar 11 a n funciona para n <= 5
for i in range(0, 6, 1):
    triangulo_de_pascal.append(11 ** i)
print(triangulo_de_pascal)

# Na forma de List Comprehensions
triangulo_de_pascal_dois = [11 ** i for i in range(0, 6, 1)]
print(triangulo_de_pascal_dois)

# Na forma trasicional
multiplos_de_tres = []
for i in range(3, 101, 3):
    multiplos_de_tres.append(i)
print(multiplos_de_tres)

# Na forma de List Comprehensions
multiplos_de_tres_lc = [i for i in range(3, 101, 3)]
print(multiplos_de_tres_lc)

# Na forma trasicional
multiplos_de_sete = []
for i in range(0, 51, 1):
    multiplos_de_sete.append(i % 7 == 0)
print(multiplos_de_sete)

# Na forma de List Comprehensions
multiplos_de_sete_lc = [i % 7 == 0 for i in range(0, 51, 1)]
print(multiplos_de_sete_lc)

# Tem que ser tudo TRUE
vector_dois = np.all([multiplos_de_sete, multiplos_de_sete_lc])
print(vector_dois)

vector_dois = np.array_equal(multiplos_de_sete, multiplos_de_sete_lc)
print(vector_dois)

modelos = ["Atrium", "Attentus", "Bhaskara", "BigproddatA",
           "Corpus", "Fibonacci", "Fluxo de Caixa", "Formica",
           "Horobox", "Horoférias", "Horótimo", "Hurst",
           "Installation", "Moneta", "Mulcta", "Palete Caixa",
           "Productio", "Tecellarius", "Thermo", "Transdia"]

# Outro exemplo
h_modelos_maiusculo = []
for i in range(0, len(modelos), 1):
    h_modelos_maiusculo.append(modelos[i].upper())
print(h_modelos_maiusculo)

# Na forma de List Comprehensions
h_modelos_maiusculo_lc = [modelos[i].upper() for i in range(0, len(modelos), 1)]
print(h_modelos_maiusculo_lc)