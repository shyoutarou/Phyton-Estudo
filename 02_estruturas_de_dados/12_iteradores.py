class Fib:
    def __init__(self, max):
        super(Fib, self).__init__()
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

    def next(self):
        return self.__next__()


# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
for n in Fib(1000):
    print(n, end=' ')

print("")


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
for n in fib(1000):
    print(n, end=' ')


class CustomRange:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb

    def next(self):
        return self.__next__()


print("")
# 0 1 2 3 4 5 6 7 8 9
for n in CustomRange(10):
    print(n, end=' ')

print("")

texto = 'um elemento por vez'

# u/m/ /e/l/e/m/e/n/t/o/ /p/o/r/ /v/e/z/
for i in texto:
    print(i + '/', end='')

print("")

def numbers_up_to(max_number):
    output = []
    for number in range(max_number + 1):
        output.append(number)
    return output

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
for i in numbers_up_to(15):
    print(i, end=' ')

def numbers_up_to(max_number):
    for number in range(max_number + 1):
        yield number

print("")

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 .... n
for i in numbers_up_to(10):
    print(i, end=' ')

my_first_generator = numbers_up_to(42)
print(next(my_first_generator))  # 0
print(next(my_first_generator))  # 1
print(next(my_first_generator))  # 2
print(next(my_first_generator))  # 3
print(next(my_first_generator))  # 4

ran_1 = list(range(5))
print(ran_1)     # [0, 1, 2, 3, 4]

ran_1 = list(range(3, 8))
print(ran_1)    # [3, 4, 5, 6, 7]

ran_3 = list(range(2, 11, 3))
print(ran_3)    # [2, 5, 8]