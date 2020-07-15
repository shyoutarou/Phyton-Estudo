import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('delete from agenda where nome = "Maria"')

        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
        else:
            conexao.rollback()
            print("Alteracoes abortadas")

        for registro in conexao.execute('select * from agenda'):
            print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")