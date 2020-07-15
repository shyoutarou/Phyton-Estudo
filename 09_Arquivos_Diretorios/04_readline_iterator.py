arquivo = open('nome_errado.txt', 'r', encoding="utf8")

"""
while True:
    try:
        line = next(arquivo)
        print(line)
    except StopIteration:
        break
"""

for line in arquivo:
    print(line)

arquivo.close()
