r = range(10)
print(r)  # Python 3 range(0, 10) Lazy evaluation
# Python 2.x [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r[3])  # 3

"""
# Python 2.x
r = xrange(10)
print(r) # xrange(10)
lst = [x for x in r]
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

numbers = range(10)
iterator = iter(numbers)
print(numbers) # range(0, 10)
print(list(numbers))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(iterator)  # <range_iterator object at 0x0000018AE309E770>
print(next(iterator)) # 0
print(next(iterator)) # 1
new_iter = iter(numbers)
print(new_iter) # <range_iterator object at 0x0000018AE303C4D0>
print(next(new_iter))  # 0
print(next(new_iter))  # 1
print(next(new_iter))  # 2


