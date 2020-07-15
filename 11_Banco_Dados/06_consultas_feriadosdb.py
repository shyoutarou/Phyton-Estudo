import sqlite3
import datetime
from dateutil.relativedelta import relativedelta

with sqlite3.connect("feriados.db", detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    for feriado in conexao.execute("select * from feriados"):
        print(feriado)

    hoje = datetime.date.today()
    hoje = hoje - relativedelta(years=2)
    hoje60dias = hoje + datetime.timedelta(days=60)
    conexao.row_factory = sqlite3.Row
    for feriado in conexao.execute("select * from feriados "
                                   "where data >= ? and data <= ?", (hoje, hoje60dias)):
        print(f"{feriado['data']:%d/%m} {feriado['descricao']}")
"""
21/04 Tiradentes
01/05 Dia do trabalhador
"""
