def soma(x, y):
    total = x + y
    print("Total soma = ", total)  # Total soma =  8


# Programa principal
total = 10
soma(3, 5)
print("Total principal = ", total)  # Total principal =  10


def soma_global(x, y):
    global total
    total = x + y
    print("Total soma = ", total)  # Total soma =  8


# Programa principal
total = 10
soma_global(3, 5)
print("Total principal = ", total)  # Total principal =  8


def soma_retorno(x, y):
    return x + y


s = soma_retorno(3, 5)
print("Total soma = ", s)  # Total soma =  8


def calcula_juros(valor, taxa=10):
    juros = valor * taxa / 100
    return juros

s = calcula_juros(300)
print("Taxa juros = ", s)  # Taxa juros =  30.0
