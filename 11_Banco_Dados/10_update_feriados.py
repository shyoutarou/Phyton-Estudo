import sqlite3
from contextlib import closing
import datetime

with sqlite3.connect("feriados.db", detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("update feriados set data = date(strftime('%Y', date('now')) || strftime('-%m-%d', data))")

        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
        else:
            conexao.rollback()
            print("Alteracoes abortadas")






