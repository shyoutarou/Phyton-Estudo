from nome_decorador import Nome

A = Nome("Nilo")
print(A)  # Nilo
print(A == Nome("Nilo"))  # __eq__Chamado True
print(A != Nome("Nilo"))  # __eq__Chamado False
print(A > Nome("Nllo"))  # __It__Chamado False
print(A < Nome("Nilo"))  # __It__Chamado False
print(A <= Nome("Nilo"))
"""
__It__Chamado
__eq__Chamado
True
"""
print(A >= Nome("Nilo"))  # __It__Chamado True

print(A.CriaChave("X"))  # x
print(Nome.CriaChave("X"))  # x

# NÃO deveria permitir a alteração do nome ou chave que fossem diferentes
# pois na classe eles são setados no mesmo tempo em __init__
# a chave é setada no metodo estatico CriaChave
print(repr(A)) # <Classe Nome em 0x1bda6204688 Nome: Nilo Chave: nilo>
A.nome = "Teste"
print(repr(A)) # <Classe Nome em 0x180d1cc3208 Nome: Teste Chave: nilo>
A.chave = "TST"
print(repr(A)) # <Classe Nome em 0x180d1cc3208 Nome: Teste Chave: TST>