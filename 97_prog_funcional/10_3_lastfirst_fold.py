import functools

def foldl(func, acc, xs):
    return functools.reduce(func, xs, acc)

def flip(func):
    @functools.wraps(func)
    def newfunc(x, y):
        return func(y, x)

    return newfunc

def foldr(func, acc, xs):
    return functools.reduce(flip(func), reversed(xs), acc)

def first(func, acc, xs):
    return foldr(lambda x, y: x if func(x) else y, acc, xs)

def last(func, acc, xs):
    return foldl(lambda x, y: y if func(y) else x, acc, xs)

print(last(lambda x: x < 8, 99, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # => 7
print(first(lambda x: x > 3, 99, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # => 4
print(first(lambda x: x > 20, 99, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # => 99
