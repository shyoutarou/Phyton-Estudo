# Python code to demonstrate lambda

# funções normais
def double(x):
   return x * 2

print(double(5)) # 10

# funções lambda
dobro = lambda x: x * 2
print(dobro(5)) # 10


cube = lambda x: x * x * x
print(cube(7)) # 343

L = [1, 3, 2, 4, 5, 6]
is_even = [x for x in L if x % 2 == 0]

print(is_even)  # [2, 4, 6]

unsorted = [('b', 6), ('a', 10), ('d', 0), ('c', 4)]

# Sort on the second tuple value (the integer).
print(sorted(unsorted, key=lambda x: x[1]))
#[('d', 0), ('c', 4), ('b', 6), ('a', 10)]



