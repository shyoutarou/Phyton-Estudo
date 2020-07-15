import functools
import operator

foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)
result = foldl(operator.sub, 0, [1, 2, 3])
print(result) # -6
result = foldl(operator.add, 'L', ['1', '2', '3'])
print(result) # L123

# FOLDL Function
def foldl(func, acc, xs):
  return functools.reduce(func, xs, acc)

print(foldl(operator.sub, 0, [1,2,3])) # -6
print(foldl(operator.add, 'L', ['1','2','3'])) # 'L123'