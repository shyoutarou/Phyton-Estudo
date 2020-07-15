# Leitura de Arquivo Separado por Colunas


arquivo = open('nome_errado.txt', 'r', encoding="utf8")
"""
# Tamanho Fixo.
for linha in arquivo:
    n1 = linha[:4]
    # c1 = linha[4:]
    c1 = linha[4:9]
    print(n1, c1)
    
1001 aaaaa

1002 bbbbb

1003 ccccc

1004 ddddd

1005 eeeee
"""

# Tamanho Variável.

"""
for linha in arquivo:
    n1 = linha[:4]
    # c1 = linha[4:]
    c1 = linha[4:len(linha)-1]
    print(n1, c1)
"""


# método read(), do objeto file handle,
# NÃO recomendado para arquivos muito grandes.

conteudo = arquivo.read()
print(conteudo)
