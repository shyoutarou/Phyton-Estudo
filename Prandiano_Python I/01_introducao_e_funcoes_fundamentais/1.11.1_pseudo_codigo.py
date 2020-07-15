prova_um = float(input("Digite o valor da 'Prova 1 (P1)' = "))
prova_dois = float(input("Digite o valor da 'Prova 2 (P2)' = "))
calculo = (6 * prova_um + 4 * prova_dois) / 10
if calculo >= 5:
    print("Aluno aprovado")
else:
    print("Aluno precisa prestar prova de recuperação")
