from nome_decorador_property import Nome

A = Nome("Nilo")

print(repr(A)) # <Classe Nome em 0x1bda6204688 Nome: Nilo Chave: nilo>
A.nome = "Teste"
print(repr(A)) # <Classe Nome em 0x2183c4d3208 Nome: Teste Chave: teste>

# A.chave = "TST" # AttributeError: can't set attribute

"""
Porém, ainda é possível ter acesso ao nome e chave, 
com o truque de usar o nome completo após a escondida 
do Python (name mangling): _nonedaclasse__atributo, 
gerando: _Nome__chave. Entenda esse tipo de acesso como 
uma curiosidade e que, quando um programador marcar um 
atributo com __. esta dizendo: não utilize esse atributo 
fora da classe, salvo se tiver certeza do que esta fazendo.
"""
# Mas ainda é possível driblar esta estrutura na seguinte maneira
A._Nome__nome = "Nilo menezes"
A._Nome__chave = "TST"
print(repr(A)) # <Classe Nome em 0x180d1cc3208 Nome: Teste Chave: TST>