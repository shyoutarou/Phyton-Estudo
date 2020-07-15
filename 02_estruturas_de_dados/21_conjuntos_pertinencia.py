# Contem / Contido

conjuntol = {'a', 'b', 4, 7, 8, 9, 'c', 'd'}
print('a' in conjuntol)  # True
print('7' in conjuntol)  # False
print(5 in conjuntol)    # False

conjunto2 = set(['a', 'b', 'c'])
print(conjunto2.issubset(conjuntol))  # True

print(conjuntol.issubset(conjunto2))  # False
print(conjuntol.issuperset(conjunto2))  # True

conjuntol = {'a', 'b', 'c', 'd'}
conjunto2 = set(['a', 'b', 'c'])
conjunto3 = set(['x', 'z'])

print(conjuntol.isdisjoint(conjunto2))  # False
print(conjunto2.isdisjoint(conjunto3))  # True

lista1 = [1, 1, 1, 1, 2, 2, 3]
conjuntol = set(lista1)
# {1, 2, 3}
print(conjuntol)
# OU voltar como lista [1, 2, 3]
print(list(conjuntol))