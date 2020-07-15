import sqlite3

feriados = [["2018-01-01", "Confraternizagao Universal"],
            ["2018-04-21", "Tiradentes"],
            ["2018-05-01", "Dia do trabalhador"],
            ["2018-09-07", "Independencia"],
            ["2018-10-12", "Padroeira do Brasil"],
            ["2018-11-02", "Finados"],
            ["2018-11-15", "Proclanacao da Repiiblica"],
            ["2018-12-25", "Natal"]]
with sqlite3.connect("feriados.db") as conexao:
    conexao.execute("create table feriados("
                    "id integer primary key autoincrement, "
                    "data date, "
                    "descricao text)")

    conexao.executemany("insert into feriados(data,descricao) values (?,?)", feriados)
    conexao.commit()
