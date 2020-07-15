pontos_p = [1, 2, 4, 7]
pontos_q = [2, 5, -3, 9]

# Na forma trasicional
combinacoes = []
ponto = 0
for i in pontos_p:
    for j in pontos_q:
        if i == "pertence":
            combinacoes.append((i, j))
print(combinacoes)

# Na forma de List Comprehensions
combinacoes_lc = [(i, j) for i in pontos_p for i in pontos_q]
print(combinacoes_lc)

# outro exemplo
maquinas = [12, 17, 31, 3, 82, 26]
operadores = [3514, 2569, 1213, 1015, 7732, 4801, 2862, 1643]

# Na forma de List Comprehensions
acoplamento = [(m, o) for m in maquinas for o in operadores]
print(acoplamento)
print(len(acoplamento))

# outro exemplo
cidades = []
for i in range(0, 17, 1):
    cidades.append(i)
print(cidades)

# Na forma de List Comprehensions
cidades_combinadas = []
cidades_combinadas = [(m, o) for m in cidades for o in cidades]
print(cidades_combinadas)
print(len(cidades_combinadas))