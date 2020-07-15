from functools import partial

# defining a function that sums 2 numbers
plus = lambda a, b: a + b
plus(3, 5) # result 8

# curring calling partial function by supplying
# the first parameters with value 1
plus_one = partial(plus, 1)

# functools.partial(<function <lambda> at 0x000001A0CE093798>, 1)
print(plus_one)

# I can use the new function as normal
plus_five = plus_one(5)
print(plus_five) # result 6