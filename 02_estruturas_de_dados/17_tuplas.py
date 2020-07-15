# TUPLAS

T = (1, 2, 3, 4, 5)
print(T)
print(T[3])
# T[3] = 8

T = (10, 20, 30, 40, 50)
a, b, c, d, e = T
print("a=", a, "b=", b)  # a= 10 b= 20
print("d+e=", d + e)     # d+e= 90

*a, b = [1, 2, 3, 4, 5]
print(a)  # [1, 2, 3, 4]
print(b)  # 5

a, *b = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4, 5]

# SyntaxError: two starred expressions in assignment
#*a, *b = [1, 2, 3, 4, 5]