arquivo = open('nome_errado.txt', 'r', encoding="utf8")

line = arquivo.readline()
while line != '':
    print(line)
    line = arquivo.readline()

arquivo.close()
