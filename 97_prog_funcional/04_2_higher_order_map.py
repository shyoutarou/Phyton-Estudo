def square(x): return x * x


num = 10
d = 0
sqrList = map(square, range(num))
while d < num:
    # 0 1 4 9 16 25 36 49 64 81
    print(next(sqrList), end=' ')
    d = d + 1

# Gerar uma lista da string # Imperativo
string = 'Python'
lista = []  # estado inicial

for l in string:
    lista.append(l)  # cada iteração gera um novo estado

print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']

# Gerar uma lista da string # Funcional
string = lambda x: x
lista = list(map(str, string('Python')))  # atribuição a um novo objeto

print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']

# Map com expressão Lambda
num = 10
d = 0
sqrList2 = map(lambda x: x * x, range(num))
while d < num:
    # 0 1 4 9 16 25 36 49 64 81
    print(next(sqrList2), end=' ')
    d = d + 1

# Map com função incorporada
bases = [10, 20, 30, 40, 50]
index = [1, 2, 3, 4, 5]
powers = list(map(pow, bases, index))
# [10, 400, 27000, 2560000, 312500000]
print("")
print(powers)

# Programação Imperativa
lista = (0.1, 0.3, 2.5, 0.8, 1.1, 0.1)
menores_que_1 = []
for x in lista:
    x = x ** 2
    if x < 1:
        menores_que_1.append(x)
# [0.010000000000000002, 0.09, 0.6400000000000001, 0.010000000000000002]
print(menores_que_1)

# Programação Funcional
menores_que_1 = list(map(lambda x: x ** 2, filter(lambda x: x < 1, lista)))
# [0.010000000000000002, 0.09, 0.6400000000000001, 0.010000000000000002]
print(menores_que_1)
