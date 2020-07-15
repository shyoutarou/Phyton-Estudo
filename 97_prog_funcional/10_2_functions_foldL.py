import functools
import operator

lmax = lambda xs: functools.reduce(lambda x, y: x if x > y else y, xs)
print(lmax([1, 2, 3, 4, 5]))  # 5

lmin = lambda xs: functools.reduce(lambda x, y: x if x < y else y, xs)
print(lmin([1, 2, 3, 4, 5]))  # 1

lsum = lambda xs: functools.reduce(operator.add, xs)
print(lsum([1, 2, 3, 4, 5]))  # 15

product = lambda xs: functools.reduce(operator.mul, xs)
print(product([1, 2, 3, 4, 5]))  # 120

lany = lambda pred, xs: functools.reduce(lambda x, y: x or pred(y), xs, False)
result = lany(lambda x: x > 3, [1, 2])
print(result)  # False

result = lany(lambda x: x > 3, [1, 2, 3, 4, 5, 6])
print(result)  # True

lall = lambda pred, xs: functools.reduce(lambda x, y: x and pred(y), xs, True)
result = lall(lambda x: x > 3, [4, 5, 6, 7])
print(result)  # True

result = lall(lambda x: x > 3, [1, 2])
print(result)  # False

lmap = lambda func, xs: functools.reduce(lambda x, y: x + [func(y)], xs, [])
result = lmap(lambda x: x + 2, [1, 2, 3, 4, 5])
print(result)  # [3, 4, 5, 6, 7]

lfilter = lambda func, xs: functools.reduce(lambda x, y: x + [y] if func(y) else x, xs, [])
result = lfilter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)  # [2, 4, 6, 8]
