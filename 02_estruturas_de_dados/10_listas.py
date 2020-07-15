L = [3, 'abacate', 9.7, [5, 6, 3], "Python", (3, 'j')]
# Seleciona os elementos das posições 1,2,3
print(L[1:4])  # ['abacate', 9.7, [5, 6, 3]]
# Seleciona os elementos a partir da posição 2
print(L[2:])  # [9.7, [5, 6, 3], 'Python', (3, 'j')]
# Seleciona os elementos até a posição 3
print(L[:4])  # [3, 'abacate', 9.7, [5, 6, 3]]

L[3] = 'morango'
print(L)        # [3, 'abacate', 9.7, 'morango', 'Python', (3, 'j')]

L[7] = 'banana'