# Esta função retorna uma lista de tuplas,
# onde a i-ésima tupla contém o i-ésimo
# elemento de cada um dos argumentos.

x = [1, 2, 3]
y = [4, 5, 6]
for t in zip(x, y):
    print(t)
"""
(1, 4)
(2, 5)
(3, 6)
"""

# Lista com tamanhos diferentes serão emparelhadas
# e a diferença entre elas será desconsiderada.
lst_a = [6, 7, 8, 9]
lst_b = [1, 2, 3, 4, 5,10,11]

for x in zip(lst_a, lst_b):
    print(x)
"""
(6, 1)
(7, 2)
(8, 3)
(9, 4)
"""

x = [1, 2, 3]
y = [4, 5, 6]
print(zip(x, y))        # <zip object at 0x000001DFC92829C8>
print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]


# Gera uma lista da string de forma imperativa
string = 'Python'
lst = [] # estado inicial

for l in string:
    lst.append(l) # cada iteração gera um novo estado

print(lst) # ['P', 'y', 't', 'h', 'o', 'n']

# Gera uma lista da string de forma funcional
string = lambda x: x
lst = list(map(str, string('Python'))) # atribuição a um novo objeto

print(lst) # ['P', 'y', 't', 'h', 'o', 'n']

# Combinando zip e map
a = (1, 2)
b = (3, 4)
combinado = list(map(sum, zip(a, b)))
print(combinado) # [4, 6]

combinado = list(map(lambda x_y: sum(x_y), list(zip(a, b))))
print(combinado) # [4, 6] # [4, 6]

# unzipping
results = [
    ('January', 35423.85,),
    ('February', 31445.75,),
    ('March', 38525.22,),
]

months, revenue = zip(*results)

print(revenue) # (35423.85, 31445.75, 38525.22)
print(sum(revenue)) # 105394.82

#  iterables of different length
short_list = list(range(5))  # [0, 1, 2, 3, 4]
long_list = list(range(10,20))  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

result = list(zip(short_list, long_list))
print(result) # [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]

import itertools

result = list(itertools.zip_longest(short_list, long_list))
# [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14), (None, 15), (None, 16), (None, 17), (None, 18), (None, 19)]
print(result)