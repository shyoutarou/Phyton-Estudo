def isPrime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
        else:
            return True


fltrObj = filter(isPrime, range(10))
# Nº Primos de 1-10: [3, 5, 7, 9]
print('Nº Primos de 1-10:', list(fltrObj))

# Programa para filtrar apenas os itens pares de uma lista
lst = [1, 5, 4, 6, 8, 11, 3, 12]
new_lst = list(filter(lambda x: (x % 2 == 0), lst))

# Saída: [4, 6, 8, 12]
print(new_lst)

pares = filter(lambda x: x % 2 == 0, range(10))
# [0, 2, 4, 6, 8]
print(list(pares))

def soma(x, y): return x + y

#<class 'function'>
print(type(soma))

s = soma
print(s(1, 2)) # 3
print(soma(1, 2)) # 3

