# Anexar dados
num_naturais = [0, 1, 2, 3, 4, 5]
print(type(num_naturais))
print(num_naturais)

num_naturais.append(6)
print(num_naturais)

num_naturais.append(7)
print(num_naturais)

num_naturais.append(39)
print(num_naturais)

# Alterar dados

num_naturais[2] = 16
# lembrar que Python sempre começa do elemento zero. Ou seja,
# o elemento 2 é a 3a posição
print(num_naturais)

num_naturais[4] = -7
print(num_naturais)

num_naturais[0]
print(num_naturais)

num_naturais[8] = 134
print(num_naturais)

# num_naturais[10] = 99 # vai dar erro porque está fora do range

num_naturais[-3] = 45
print(num_naturais)
# quando o range é negativo, o Python reconhece como "do final
# da lista para o começo da lista", começando com -1 ao
# invés de zero. Ou seja, o último elemento é o -1, o penúltimo é -2, etc.

# num_naturais[-11] = 33 # nesse caso vai dar erro também
# porque está fora do range
