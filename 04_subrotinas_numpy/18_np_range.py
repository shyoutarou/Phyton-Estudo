import   numpy   as   np

print ("++++++FIRST++++++++")
# Numeros Naturais N = (0, 10]
x = list (range(0, 10, 1))
print(x)
print (type (x))

print ("++++++SECOND++++++++")

# Numeros Naturais N* = (1, 10]
y = list (range(1, 10, 1))
print(y)
print (type (y))

print ("++++++THIRD++++++++")

# Numeros Inteiros Z = (-10, 10]
z = list (range(-10, 10, 1))
print(z)
print (type (z))
z = np.array (z)
print (type(z) )

print ("++++++FOURTH++++++++")

# Numeros Inteiros Z = (-10, 0]
inteiros_negativos = list (range(-9, 0, 1))
print(inteiros_negativos)
print (type (inteiros_negativos))

#Se comentar essa linha NÃO ira somar mas agragar elementos na soma inteiros_asterisco
inteiros_negativos = np.array (inteiros_negativos)

inteiros_positivos = list (range(1, 10, 1))
print(inteiros_positivos)
print (type (inteiros_positivos))

inteiros_asterisco = inteiros_negativos + inteiros_positivos
print(inteiros_asterisco)

print ("++++++FIFTH++++++++")

# Numeros Racionais Q = (-10, 10]
racionais = list (range(-10, 10, 0.05))
print (type (racionais))
z = np.array (racionais)
print (type(racionais) )

