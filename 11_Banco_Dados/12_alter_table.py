import sqlite3

with sqlite3.connect("brasil.db") as conexao:
    #conexao.execute("""alter table estados add sigla text""")
    #conexao.execute("""alter table estados add regiao text""")

    dados = [["SP", "SE", "São Paulo"], ["MG", "SE", "Minas Gerais"],
             ["PJ", "SE", "Rio de Janeiro"], ["BA", "NE", "Bahia"],
             ["RS", "S", "Rio Grande do Sul"], ["PR", "S", "Parana"],
             ["PE", "NE", "Pernanbuco"], ["CE", "NE", "Ceara"],
             ["PA", "N", "Pará"], ["MA", "NE", "Maranhão"],
             ["SC", "S", "Santa Catarina"], ["GO", "CO", "Goias"],
             ["PB", "NE", "Paraiba"], ["ES", "SE", "Espirito Santo"],
             ["AM", "N", "Amazonas"], ["RN", "NE", "Rio Grande do Norte"],
             ["AL", "NE", "Alagoas"], ["PI", "NE", "Piauí"],
             ["MT", "CO", "Mato Grosso"], ["DF", "CO", "Distrito Federal"],
             ["MS", "CO", "Mato Grosso do Sul"], ["SE", "NE", "Sergipe"],
             ["RO", "N", "Rondônia"], ["TO", "N", "Tocantins"],
             ["AC", "N", "Acre"], ["AP", "N", "Amapá"], ["RR", "N", "Roraina"]]

    conexao. executemany("""update estados
    set sigla = ?,
    regiao = ?
    where nome = ?""", dados)

    conexao.commit()

