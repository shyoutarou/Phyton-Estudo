import random

# LI Limite Inferior
LI = int(input("Digite o Limite Inferior (LI) ="))

# LS Limite Superior
LS = int(input("Digite o Limite Superior (LS) ="))

# Gerar aleatório decimal manualmente
# aleatório_manual = Aleatório digitado manualmente
aleatorio_manual = int(input("Digite um número entre "
                             "0 (zero) e 1 (um) = "))

aleatorio = aleatorio_manual * (LS - LI) + LI

print(aleatorio)

# Gerar aleatório inteiro manualmente
aleatorio_inteiro = int(aleatorio_manual * (LS - LI) + LI)

print(aleatorio_inteiro)

# Correção do aleatório inteiro
aleatorio_inteiro = int(random.random() * (LS - LI + 1) + LI)

print(aleatorio_inteiro)
