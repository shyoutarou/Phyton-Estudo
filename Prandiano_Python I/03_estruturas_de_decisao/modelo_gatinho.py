contas_em_dia = int(input("O usuário paga as faturas em dia? "
                          "(0 - NAO, 1 - SIM).Resposta: "))

if contas_em_dia == 0:
    medidor_alterado = int(input("O medidor foi alterado? "
                                 "(0 - NAO, 1 - SIM). Resposta: "))
    if medidor_alterado == 0:
        qtde_de_multas = int(input("Digitar o valor da ""Quantidade de Multas"" do usuário: "))
        if qtde_de_multas < 2:
            folha = "Honesto"
        elif qtde_de_multas >=2:
            folha = "Desonesto"
    elif medidor_alterado == 1:
        folha = "Desonesto"
elif contas_em_dia == 1:
    folha = "Honesto"

print(folha)

