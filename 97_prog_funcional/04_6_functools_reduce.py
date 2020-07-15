from functools import reduce

values = [1, 2, 3, 4]

summed = reduce(lambda a, b: a + b, values)
print(summed) # 10

values = [1, 2, 3, 4, 5]

# By convention, we add `_` as a placeholder for an input
# we do not use.
first_value = reduce(lambda a, _: a, values)
print(first_value) # 1
