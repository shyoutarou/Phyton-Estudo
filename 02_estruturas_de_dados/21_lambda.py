def square_func(x): return (x * x)


square = lambda x: x * x
print(square(5))  # 25

soma = lambda x, y, z: x + y + z
print(soma(5, 10, 15))  # 30

disp = lambda str: print('Saída:' + str.upper())
disp("Olá, mundo!") # Saída:OLÁ, MUNDO!
