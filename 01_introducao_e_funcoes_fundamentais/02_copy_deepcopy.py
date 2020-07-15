c = 'copia de texto'

# c2 NÃO é cópia, é referência de c
c2 = c

# ´Cópias do texto
c2 = list(c)
c2 = c[:]
import copy

c2 = copy.copy(c)

lista_a = [1, 2, [3, 4]]
lista_b = lista_a[:]
copylista_b = copy.copy(lista_a)
deepcopylista_b = copy.deepcopy(lista_a)

# Subtituiu o 3 pelo 10
lista_a[2][0] = 10

print(lista_a)  # [1, 2, [10, 4]]
print(lista_b)  # [1, 2, [10, 4]]
print(copylista_b)  # [1, 2, [10, 4]]
print(deepcopylista_b)  # [1, 2, [3, 4]]
