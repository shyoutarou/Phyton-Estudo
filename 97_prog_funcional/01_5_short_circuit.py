# x OR y
# Se x é falso, then y else x
# Avalia o segundo argumento (y) apenas se o primeiro
# for false. Ou seja, quando o primeiro argumento aval
# ia a true, o valor total deve ser true.
# x AND y	Se x é falso, then x else y
# Avalia o segundo argumento (y) apenas se o primeiro (x)
# for True. Ou seja, quando o primeiro argumento avalia a
# false, o valor total deve ser false
# NOT x
# Se x for falso, then True, caso contrário False
# NOT tem uma prioridade mais baixa que os operadores
# não booleanos. Portanto, NOT a == b é interpretado como
# NOT (a == b) e a == NOT b é um erro de sintaxe.


print('x' == ('x' or 'y')) # True
print('y' == ('x' or 'y')) # False
print('x' == ('x' and 'y')) # False
print('y' == ('x' and 'y')) # True


def check(x, y, z):
    if(z == "OR"):
        return x > 6 or y < 20
    elif(z == "AND"):
        return x > 6 and y < 20

x = 5
y = 10
if check(x, y, "OR"): print('OR')  # OR
if check(x, y, "AND"): print('AND')
x = 7
y = 10
if check(x, y, "OR"): print('OR')  # OR
if check(x, y, "AND"): print('AND') # AND

"""
n = 0
m = 2
if m < 9/n:
    print('m < 1/n') # ZeroDivisionError: division by zero
"""

n = 0
m = 2
if n and m < 9/n:
    print('m < 1/n')

a = 0
b = 2
c = 3
x = c or a
print(x) # 3


x = a or b
print(x)  # 2
x = b or c
print(x)  # 2
x = 0 or a
print(x)  # 0 (the result is false because 0 and a are both false)
x = a or b+c or b+a
print(x)  # 5 (b+c, the first true value)


username=''
username = username or input('Enter username')



# python code to demonstrate short circuiting
# using all() and any()

# helper function
def check(i):
	print ("geeks")
	return i

# using all()
# stops execution when false occurs tells the compiler that even if one is
# false, all cannot be true, hence stop execution further.  prints 3 "geeks"
print (all(check(i) for i in [1, 1, 0, 0, 3]))
"""
geeks
geeks
geeks
False
"""

print("\r")

# using any()
# stops execution when true occurs  tells the compiler that even if one is
# true, expression is true, hence stop  execution further. r prints 4 "geeks"
print (any(check(i) for i in [0, 0, 0, 1, 3]))
"""
geeks
geeks
geeks
geeks
True
"""




