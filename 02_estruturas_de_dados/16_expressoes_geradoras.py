# EXPRESSÕES GERADORAS
# Parentes inves de Conchetes(List Conpreensions)

squares = [i ** 2 for i in range(10)]
#  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

print("==========")

# squares = <generator object <genexpr> at 0x000001E5BA502A48>
squares = (i ** 2 for i in range(10))
for item in squares:
    print(item, end=' ')  # 0 1 4 9 16 25 36 49 64 81

print("")
print("==========")

# pares = <generator object <genexpr> at 0x000001C7B1E74B48>
pares = (i for i in range(20) if not i % 2)
for item in pares:
    print(item, end=' ')  # 0 2 4 6 8 10 12 14 16 18

print("")
print("==========")

gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)

lista = list(gen_exp)
print(lista)

print("==========")

anonima = lambda x: 3 * x + 1
par = lambda x: x % 2 == 0
d = 0

mapeado = map(anonima, lista)
filtrado = filter(par, lista)

while d < 5:
    print(next(mapeado), end=' ')
    print("filtrado: " + str(next(filtrado)))
    d = d + 1

print("")
print("==========")


def preguicosa(pre):
    for i in range(pre):
        yield anonima(pre)


result = preguicosa(10)
print(result)
for n in result:
    print(n, end=' ')
