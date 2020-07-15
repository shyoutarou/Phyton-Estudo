import sqlite3
from contextlib import closing

nome = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:

        # cursor.execute("DROP TABLE agenda")
        # print("Table dropped... ")

        #cursor.execute(f'select * from agenda where nome = "{nome}"')
        cursor.execute("select * from agenda where nome = ?", (nome,))

        # cursor.execute('select * from agenda where nome  = "Nilo"')
        # cursor.execute("""select * from agenda where nome  = "Nilo" """)

        """ Imprimir um
        resultado = cursor.fetchone()
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
        Nome: Nilo
        Telefone: 7788-1432
        """

        """ imprimir todos, até 100 registros
        resultados = cursor.fetchall()
        for registro in resultados:
            print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")
        """
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0 :
                    print("Nada encontrado")
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            x += 1

