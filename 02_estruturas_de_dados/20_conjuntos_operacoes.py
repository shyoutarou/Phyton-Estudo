conjuntol = {'a', 'b', 4, 7, 8, 9, 'c', 'd'}
print(conjuntol)  # {4, 'c', 7, 8, 9, 'd', 'b', 'a'}

# Contem / Contido
conjunto2 = set(['a', 'b', 'c'])
print(conjunto2)  # {'c', 'b', 'a'}

print(conjuntol.issubset(conjunto2))  # False
print(conjunto2.issubset(set('abcdefg')))  # True

print(conjunto2 <= set('abcdefg'))  # True
print(set('abcdefg') >= conjunto2)  # True

# União

conjuntol = {'a', 'b', 4, 7, 8, 9}
# {4, 7, 8, 'a', 9, 'b'}
print(conjuntol)

conjunto2 = {'a', 'b', 'c'}
# {'c', 'b', 'a'}
print(conjunto2)

# OU conj_union = conjuntol.union(conjunto2)
conj_union = conjuntol | conjunto2
# {4, 7, 8, 9, 'a', 'c', 'b'}
print(conj_union)

# Interseção

# OU conj_intesect = conjuntol.intersection(conjunto2)
conj_intesect = conjuntol & conjunto2
# {'b', 'a'}
print(conj_intesect)

lista1 = [1, 2, 3]
lista2 = [2, 4, 3]
# {2, 3}
print(set(lista1).intersection(lista2))

lista3 = list(set(lista1).intersection(lista2))
print(lista3)  # [2, 3]

conjuntol = {'a', 'b', 4, 7, 8, 9, 'c', 'd'}
# {4, 7, 8, 9, 'c', 'd', 'b', 'a'}
print(conjuntol)

conjunto2 = {'nada, tudo'}
# {'nada, tudo'}
print(conjunto2)

conjunto3 = set('nada, tudo')
# {'o', 't', ' ', 'u', 'a', 'n', ',', 'd'}
print(conjunto3)

conjuntol.intersection_update(conjunto3)
# {'a', 'd'}
print(conjuntol)

conjuntol.intersection_update(conjunto2)
# set()
print(conjuntol)

conjuntol.intersection_update(conjunto3)
# set()
print(conjuntol)

# Diferença

conjuntol = set('1234')
# {'2', '4', '3', '1'}
print(conjuntol)

conjunto2 = {'123, 1', 1, '2', 2, 3}
# {'2', 1, 2, 3, '123, 1'}
print(conjunto2)

# OU conjuntol - conjunto2
conj_diferenca = conjuntol.difference(conjunto2)
# {'3', '1', '4'}
print(conj_diferenca)

conj_diferenca = conjunto2.difference(conjuntol)
# {1, 2, 3, '123, 1'}
print(conj_diferenca)

# Diferença simétrica
conj_diferenca = conjuntol.symmetric_difference(conjunto2)
# {1, 2, '123, 1', 3, '3', '4', '1'}
print(conj_diferenca)
