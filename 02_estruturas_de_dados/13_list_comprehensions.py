lista = []
for item in range(10):
    lista.append(item ** 2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(lista)

lista = [item ** 2 for item in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(lista)

texto = "teste"
maiusculas = []
for item in texto:
    maiusculas.append(str(item).upper())
# ['T', 'E', 'S', 'T', 'E']
print(maiusculas)

texto = "teste"
maiusculas = [str(item).upper() for item in texto]
# ['T', 'E', 'S', 'T', 'E']
print(maiusculas)