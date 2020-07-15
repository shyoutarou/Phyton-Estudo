# CONJUNTOS


# cities = frozenset(["Frankfurt", "3asel", "Freiburg"])
# cities.add("Strasbourg")

# cities = set((("Python", "Perl"), ("Paris", "3erlin", "London")))
# cities = set((["Python", "Perl"], ["Paris", "Berlin", "London"]))

cities = set(["Frankfurt", "3asel", "Freiburg"])
cities.add("Strasbourg")
#  {'Freiburg', 'Frankfurt', '3asel', 'Strasbourg'}
print(cities)

conjunto = set('234') | frozenset("45")
print(conjunto) # {'5', '3', '4', '2'}
print(set('45') | frozenset("234")) # {'5', '3', '4', '2'}
# frozenset({'5', '3', '4', '2'})
print(frozenset('45') | set('234'))
# frozenset({'5', '3', '4', '2'})
print(frozenset('234') | set('45'))

# {'4', '2', '5', '6', '3'}
print(set('234').union("56"))
# print(set('234') | [5, 6])

conjuntol = {'a', 'b', 4, 7, 8, 9, 'c', 'd'}
# {4, 7, 8, 9, 'c', 'd', 'b', 'a'}
print(conjuntol)

conjunto2 = {'nada, tudo'}
# {'nada, tudo'}
print(conjunto2)

conjunto3 = {'nada', 'tudo'}
# {'tudo', 'nada'}
print(conjunto3)

conjunto4 = set('nada, tudo')
# {'o', 't', ' ', 'u', 'a', 'n', ',', 'd'}
print(conjunto4)

conjuntol.update(conjunto2)
# {'nada, tudo', 4, 7, 8, 9, 'c', 'a', 'b', 'd'}
print(conjuntol)

conjuntol.update(conjunto3)
# {'tudo', 'nada, tudo', 'nada', 4, 7, 8, 9, 'c', 'a', 'b', 'd'}
print(conjuntol)

conjuntol.update(conjunto4)
# {'b', 'tudo', 4, ',', 7, 8, 9,  'nada, tudo', 'c',
# 'nada', ' ',  'a', 'u', 'o', 'd', 't', 'n'}
print(conjuntol)
