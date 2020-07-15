import sqlite3

with sqlite3.connect("agenda.db") as conexao:
    for registro in conexao.execute('select * from agenda'):
        print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")

# Acessando os campos como em um dicionário
print(f'Acessando os campos como em um dicionário')
with sqlite3.connect("agenda.db") as conexao:
    conexao.row_factory = sqlite3.Row
    for registro in conexao.execute('select * from agenda'):
        print(f"Nome: {registro['NOME']}\nTelefone: {registro['telefone']}")