a = [0, 1, 2]
b = [3, 4, 5]
c = a + b
print(c)  # [0, 1, 2, 3, 4, 5]
L = [1, 2]
R = L * 4
print(R)  # [1, 2, 1, 2, 1, 2, 1, 2]

del R[3]
print(R)

L = [1, 2, 3, 4]
print(L.count(3))
print(L.index(3))

print(sum(L))
print(len(L))
print(min(L))
print(max(L))

L.remove(3)
print(L)
L.insert(2, 3)
print(L)
L.pop(3)
print(L)

L = [3, 'abacate', 9.7, [5, 6, 3], "Python", (3, 'j')]
# Seleciona os elementos das posições 1,2,3
print(L[1:4])  # ['abacate', 9.7, [5, 6, 3]]
# Seleciona os elementos a partir da posição 2
print(L[2:])  # [9.7, [5, 6, 3], 'Python', (3, 'j')]
# Seleciona os elementos até a posição 3
print(L[:4])  # [3, 'abacate', 9.7, [5, 6, 3]]
