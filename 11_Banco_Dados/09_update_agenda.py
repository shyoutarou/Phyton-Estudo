import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('update agenda set telefone = "12345-6789" where nome = "Nilo"')

        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
            cursor.execute('select * from agenda where nome  = "Nilo"')
            resultado = cursor.fetchone()
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
        else:
            conexao.rollback()
            print("Alteracoes abortadas")






