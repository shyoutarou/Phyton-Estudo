gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(gen_exp)  # <generator object <genexpr> at 0x0000021099F12C48>
print(list(gen_exp))  # [0, 4, 16, 36, 64]


def numbers():
    number = 0
    while True:
        yield number
        number += 1

def condition(generator, func=lambda x: True):
    while True:
        value = next(generator)
        if func(value):
            yield value

def take(n, generator):
    for index in range(n):
        yield next(generator)

def sum_values(generator):
    s = 0
    for value in generator:
        s += value
    return s

result = sum_values(take(10, condition(numbers(), lambda x: x ** 2 % 5 == 0)))

print("Soma de 10 números natural, em que o quadrado é dividido por 5:", result)  # 275
