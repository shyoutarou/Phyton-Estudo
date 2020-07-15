# 1. Digitar o número de pecados que você acha ter cometido nesse ano
num_de_pecados = int(input("Digite o número de pecados que você acha ter cometido nesse ano: "))

# 2. Multiplicar esse número por 2
calculo_um = num_de_pecados * 2

# 3. Somar 5 ao resultado anterior
calculo_dois = calculo_um + 5

# 4. Multiplicar o resultado anterior por 50
calculo_tres = calculo_dois * 50

# 5. Se você já fez aniversário esse ano, somar 1768 ao resultado anterior, senão somar 1769
fez_aniversario_este_ano = int(input("Você já fez aniversário este ano? (0 - NÃO, 1 - SIM): "))
if fez_aniversario_este_ano == 1:
    calculo_quatro  = calculo_tres + 1770
elif fez_aniversario_este_ano == 0:
    calculo_quatro = calculo_tres + 1769

# 6. Subtrair o ano em que você nasceu do resultado anterior
ano_de_nascimento = int(input("Digitar o ano em que você nasceu: "))
calculo_cinco = calculo_quatro - ano_de_nascimento

# Antes de extrair os caracteres representantes da idade, deve-se converter o número em texto.
# Os dois últimos caracteres são a idade

pecados_e_idade = str(calculo_cinco)
print("Você possui", pecados_e_idade[-2] + pecados_e_idade[-1],"anos")