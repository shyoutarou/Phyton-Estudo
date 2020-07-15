import sqlite3
from contextlib import closing

with sqlite3.connect("brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    print(f"{'Id':3s} {'Estado':20s} {'População':12s}")
    print("=" * 37)
    for estado in conexao.execute("select * from estados order by nome"):
        print(f"{estado['id']:3d} {estado['nome']:20s} {estado['populacao']:12d}")
"""
Id  Estado               População   
=====================================
 25 Acre                       776463
 17 Alagoas                   3300938
 26 Amapá                      734995
"""