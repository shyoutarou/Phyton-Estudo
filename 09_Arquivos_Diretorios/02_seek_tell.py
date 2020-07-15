arquivo = open('nome_errado.txt', 'r', encoding="utf8")

print('Posição no arquivo: {}'.format(arquivo.tell()))  # 0
print(arquivo.read())  # conteudo de arquivo
print('Posição no arquivo: {}'.format(arquivo.tell()))  # 19
print(arquivo.read())  # ""
arquivo.seek(8)
print('Posição no arquivo: {}'.format(arquivo.tell()))  # 8
print(arquivo.read())  # de arquivo
arquivo.close()
