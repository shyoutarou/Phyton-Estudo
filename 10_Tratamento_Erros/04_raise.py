from custom_exception import Excep


def verifica_numero_primo(numero):
    if numero < 0:
        raise ValueError('O valor deve ser maior ou igual a zero!')


# verifica_numero_primo(-1)

"""
SyntaxError
for e in [1,2,3] # SyntaxError: invalid syntax(sem dois pontos:)
    print(e)
"""
"""
SyntaxError
# Sem fechamento de string "
a = "5
"""
"""
# IndentationError: unindent does not match any outer indentation level
x = 8
while x < 16:
   print(x)
 x = x + 1
"""
"""
# KeyError: 'seguro'
mensalidades = {"carro": 586, "casa": 1506}
print(mensalidades["seguro"])
"""
"""
# NameError: name 'x' is not defined
while x < 0:
    print(x)
    x = x + 1
"""
"""
# ValueError: invalid literal for int() with base 10: 'abc'
int("abc")

# ValueError: substring not found
s = "Alo Mundo"
s.index("rei")
"""
"""
# TypeError: float expected at most 1 arguments, got 2
# float(35, 4)

# TypeError: list indices must be integers or slices, not tuple
s= []
s["amarelo", "vermelho", " verde"]
s["marrom"]
"""
"""
# IndexError: string index out of range
s = "ABCDE"
s[19]
"""

try:
    # IndexError: string index out of range
    s = "ABCDE"
    s[19]
except KeyError:
    Excep.lancador() # Uma exceção do tipo NovaException foi lançada