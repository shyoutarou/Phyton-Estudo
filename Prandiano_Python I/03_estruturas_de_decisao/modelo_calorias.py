x = ["", "", ""]
x[0] = float(input("Digite a 'Massa' (kg): "))
x[1] = float(input("Digite a 'Altura' (cm): "))
x[2] = float(input("Digite a 'Idade' (anos): "))

nivel_de_atividade = int(input("Qual seu nível de atividade? "
                           "(0 - Sedentário, 1 - Pouco Ativo, 2 - Ativo, 3 - Muito Ativo)."
                           " Resposta: "))

sexo = int(input("Informe o seu sexo: "
             "(0 - Mulher, 1 - Homem)."
             " Resposta: "))

if sexo == 0:
    calorias_para_mulher = 670 + 10 * x[0] + 1.5 * x[1] - 5 * x[2]
    calorias = calorias_para_mulher
elif sexo == 1:
    calorias_para_homem = 67 + 14 * x[0] + 5 * x[2] - 6.5 * x[2]
    calorias = calorias_para_homem

if nivel_de_atividade == 0:
    calorias_nivel_de_atividade = 1.3 * calorias
elif nivel_de_atividade == 1:
    calorias_nivel_de_atividade = 1.4 * calorias
elif nivel_de_atividade == 2:
    calorias_nivel_de_atividade = 1.7 * calorias
elif nivel_de_atividade == 3:
    calorias_nivel_de_atividade = 1.9 * calorias

print("")
print("RESULTADO(S): ")

print("A quantidade mínima de calorias BASAL que o indivíduo deve consumir para manter o mesmo peso é de:",
      str(round(calorias,2)) + "cal")

print("")

print("A quantidade mínima de calorias que o indivíduo deve consumir para manter o mesmo peso é de:",
      str(round(calorias_nivel_de_atividade,2)) + "cal")