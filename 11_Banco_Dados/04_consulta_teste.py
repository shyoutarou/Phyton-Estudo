import sqlite3
from contextlib import closing

with sqlite3.connect("brasil.db") as conexao:
    for reg in conexao.execute("select * from feriados"):
        print(reg)
    for reg in conexao.execute("select * from estados"):
        print(reg)

    with closing(conexao.cursor()) as cursor:
        cursor.execute("DROP TABLE feriados")


