import functools

def mult(x, y):
    print("x=", x, " y=", y)
    return x * y

fact = functools.reduce(mult, range(1, 4))
print('Factorial of 3: ', fact)
"""
x= 1  y= 2
x= 2  y= 3
Factorial of 3:  6
"""

from functools import reduce

def soma(x1, x2):
    return x1 + x2

# Saída: 10
print(reduce(soma, [1, 2, 3, 4]))


# Calcula o fatorial de n
def fat(n):
    return reduce(lambda x, y: x * y, range(1, n))

# Saída: 720
print(fat(7))
