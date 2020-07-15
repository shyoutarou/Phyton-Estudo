import numpy as np

inteiros_negativos = list(range(-10, 0, 1))
print(inteiros_negativos)
print(type(inteiros_negativos))
print("")


inteiros_positivos = list(range(1, 11, 1))
print(inteiros_positivos)
print(type(inteiros_positivos))
print("")

inteiros_asterisco = inteiros_negativos + inteiros_positivos
print(inteiros_asterisco)
print(type(inteiros_asterisco))
print("")

inteiros_negativos = np.array(inteiros_negativos)
inteiros_positivos = np.array(inteiros_positivos)
inteiros_asterisco = inteiros_negativos + inteiros_positivos
print(inteiros_asterisco)
print(type(inteiros_asterisco))