import sqlite3
from contextlib import closing

BANCO = """
create table tipos(id integer primary key autoincrement,
                    descricao text); 
create table nomes(id integer primary key autoincrement,
                    nome text); 
create table telefones(id integer primary key autoincrement,
                    id_nome integer,
                    numero text,
                    id_tipo integer);

insert into tipos(descricao)   values ("Celular");
insert into tipos(descricao)   values ("Fixo");
insert into tipos(descricao)   values ("Fax");
insert into tipos(descricao)   values ("Casa");
insert into tipos(descricao)   values ("Trabalho");
"""

with sqlite3.connect("db_agenda.db") as conexao:
    #conexao.executescript(BANCO)
    #conexao.commit()


    for reg in conexao.execute("select * from tipos"):
        print(reg)
    for reg in conexao.execute("select * from nomes"):
        print(reg)
    for reg in conexao.execute("select * from telefones"):
        print(reg)

    #with closing(conexao.cursor()) as cursor:
        #cursor.execute("DROP TABLE feriados")
