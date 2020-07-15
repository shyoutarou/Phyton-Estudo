pares = [numero for numero in range(20) if numero % 2 == 0]
#  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(pares)

multiplos = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
#  [0, 30, 60, 90]
print(multiplos)

resultado = ['1' if numero % 5 == 0 else '0' for numero in range(10)]
#  ['1', '0', '0', '0', '0', '1', '0', '0', '0', '0']
print(resultado)