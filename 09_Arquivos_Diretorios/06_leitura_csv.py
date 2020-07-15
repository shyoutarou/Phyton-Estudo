f = open('ceps.csv', 'r', encoding="utf8")
aux = 0  # auxiliar para permitir que cabeçalho seja ignorado
for linha in f:
    if (aux > 0):  # ignora a linha de cabeçalho
        linha = linha[:len(linha) - 1]  # remove o tremendamente chato do "\n"
        lstPalavras = linha.split(",")
        cep_ini = lstPalavras[0]
        cep_fim = lstPalavras[1]
        uf = lstPalavras[2]
        print(uf + " -> CEPS de " + cep_ini + " a " + cep_fim)
    aux = aux + 1

"""
UTC:
Rio de Janeiro -> CEPS de 20000000 a 28999999
Espírito Santo -> CEPS de 29000000 a 29999999
Minas Gerais -> CEPS de 30000000 a 39999999
São Paulo -> CEPS de 01000000 a 19999999
NÃO UTC
Rio de Janeiro -> CEPS de 20000000 a 28999999
EspÃ­rito Santo -> CEPS de 29000000 a 29999999
Minas Gerais -> CEPS de 30000000 a 39999999
SÃ£o Paulo -> CEPS de 01000000 a 19999999
"""

import csv

with open('paises.csv', 'rt') as f:
    meu_csv = csv.reader(f, delimiter=';')
    for linha in meu_csv:
        print(linha)
"""
['sigla', 'nome', 'continente', 'extensao', 'populacao']
['BRA', 'Brasil', 'A', '8515767', '204450649']
['CUB', 'Cuba', 'A', '109890', '11389562']
['FRA', 'FranÃ§a', 'E', '549190', '64395345']
['HUN', 'Hungria', 'E', '93030', '9855023']
['ITA', 'ItÃ¡lia', 'E', '301340', '59797685']
['MEX', 'MÃ©xico', 'A', '1964380', '127017224']
['NOR', 'Noruega', 'E', '323780', '5210967']
['PER', 'Peru', 'A', '1285220', '31376670']
['PRT', 'Portugal', 'E', '92090', '10349803']
['URY', 'Uruguai', 'A', '176220', '3431555']
[]
"""

with open('paises.csv', 'rt', encoding="utf8") as f:
    meu_csv = csv.reader(f, delimiter=';')
    i = 0;
    for linha in meu_csv:
        if i > 0 and len(linha) > 3:  # para ignorar o cabeçalho
            print(linha[0] + ' -> população = ' + linha[4])
        i = i + 1
"""
BRA -> população = 204450649
CUB -> população = 11389562
FRA -> população = 64395345
HUN -> população = 9855023
ITA -> população = 59797685
MEX -> população = 127017224
NOR -> população = 5210967
PER -> população = 31376670
PRT -> população = 10349803
URY -> população = 3431555
"""
print("============DictReader=================")
with open('paises.csv', 'rt', encoding="utf8") as f:
    meu_csv = csv.DictReader(f, delimiter=';')
    for linha in meu_csv:
        print(linha["sigla"] + ' -> populacao = ' + linha["populacao"])
