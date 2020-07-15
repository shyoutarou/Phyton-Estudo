import sqlite3
from contextlib import closing


conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

try:
    cursor.execute('''
    create table agenda(
    nome text,
    telefone text)
    ''')
except sqlite3.OperationalError:
    None

""" Inserir um registro
cursor.execute('''
insert into agenda (nome, telefone) values(?, ?)
''', ("Nilo", "7788-1432"))
"""

dados = [("Joao", "98901-0109"),
         ("Andre", "98902-8900"),
         ("Maria", "97891-3321")]

cursor.executemany('''
insert into agenda (nome, telefone) values(?, ?)
''', dados)

conexao.commit()
cursor.close()
conexao.close()
