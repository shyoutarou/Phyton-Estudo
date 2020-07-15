a = 1
print(type(a))  # <class 'int'>
b = 2
print(isinstance(type(a), type(a))) # False
print(isinstance(type(a), type(b))) # False
print(isinstance(type(a), int)) # False
print(isinstance(5, int)) # True
print(isinstance(a, int)) # True
print(isinstance(b, int)) # True

a = 'abacaxi'
print(type(a))  # <class 'str'>
a = 1.0
print(type(a))  # <class 'float'>
a = 3.1 + 2j
print(type(a))  # <class 'complex'>

