from nome import Nome

A = Nome("Nilo")
print(A)  # Nilo
"""
B = Nome("    ")
Traceback (most recent call last):
  File "teste_nome.py", line 5, in <module>
    B = Nome("    ")
  File "nome.py", line 4, in __init__
    raise ValueError("Nome não pode ser nulo nem em branco")
ValueError: Nome não pode ser nulo nem em branco
"""
"""
C = Nome(None)
Traceback (most recent call last):
  File "teste_nome.py", line 13, in <module>
    C = Nome(None)
  File "nome.py", line 4, in __init__
    raise ValueError("Nome não pode ser nulo nem em branco")
ValueError: Nome não pode ser nulo nem em branco
"""
print(repr(A))  # <Classe Nome em 0x12c6474d0c8 Nome: Nilo Chave: nilo>
print(A == Nome("Nilo"))  # __eq__ Chamado True
print(A != Nome("Nilo"))  # __eq__ Chamado False
print(A < Nome("Nilo"))  # __lt__ Chamado False
print(A > Nome("Nilo"))  # __lt__ Chamado False


"""
print(A >= Nome("Nilo"))
Traceback (most recent call last):
  File "teste_nome.py", line 29, in <module>
    print(A >= Nome("Nilo"))
TypeError: '>=' not supported between instances of 'Nome' and 'Nome'
"""
"""
print(A <= Nome("Nilo"))
Traceback (most recent call last):
  File "teste_nome.py", line 37, in <module>
    print(A <= Nome("Nilo"))
TypeError: '<=' not supported between instances of 'Nome' and 'Nome'
"""
