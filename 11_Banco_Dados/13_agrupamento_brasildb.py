import sqlite3
print("Região Estados População Mínima     Máxima      Média      Total(soma)")
print("====== =======          ========= ==========  =========   ===========")
with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute("""
    select regiao, 
    count(*), 
    min(populacao),
    max(populacao), 
    avg(populacao), 
    sum(populacao) as tpop 
    from estados group by regiao 
    having count(*) > 5 order by tpop desc
    """):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:12,}".format(*regiao))
"""
Região Estados População Mínima     Máxima      Média      Total(soma)
====== =======          ========= ==========  =========   ===========
NE           9          2,195,662 15,044,127  6,199,407   55,794,663
N            7            488,072  7,969,655  2,426,212   16,983,485
"""
