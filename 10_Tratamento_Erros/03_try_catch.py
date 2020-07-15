meu_dicionario = {'chave.a': 1, 'chave.b': 2}

try:
    print(meu_dicionario['chave_c'])
except KeyError:
    print("Chave não encontrada!")
