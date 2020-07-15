import functools
import operator

foldr = lambda func, acc, xs: functools.reduce(lambda x, y: func(y, x), xs[::-1], acc)
result = foldr(operator.sub, 0, [1, 2, 3])
print(result)  # 2
result = foldr(operator.add, 'R', ['1', '2', '3'])
print(result)  # 123R

def flip(func):
    @functools.wraps(func)
    def newfunc(x, y):
        return func(y, x)
    return newfunc

def foldr(func, acc, xs):
    return functools.reduce(flip(func), reversed(xs), acc)

print(foldr(operator.sub, 0, [1,2,3])) # 2
print(foldr(operator.add, 'R', ['1','2','3'])) # '123R'