x = 12
y = 3.14
V = [1, 2, 5]
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(V)
# [1, 2, 5]
print(M)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a = 2 + 3j
print(a)
# b = 5 - 6i
# SyntaxError: invalid syntax

s = "Ada Byron"
print(type(x))
# <class 'int'>
print(type(y))
# <class 'float'>
print(type(V))
# <class 'list'>
print(type(M))
# <class 'list'>
print(type(s))
# <class 'str'>
"""
size(V)
Traceback (most recent call last):
  File "C:1.12.1.atribuicao_dados.py", line 28, in <module>
    size(V)
NameError: name 'size' is not defined
"""
# print(len(x))
# Não a len para tipo integer, interrompe e não executa o restante do código
print(len(V)) # 3
print(len(M)) # 3
print(len(s)) # 9
