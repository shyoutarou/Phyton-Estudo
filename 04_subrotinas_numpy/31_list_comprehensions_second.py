# Na forma trasicional
multiplos_de_onze = []
for i in range(0, 230, 1):
    if i % 11 == 0:
        multiplos_de_onze.append(i)
print(multiplos_de_onze)

# Na forma de List Comprehensions
multiplos_de_onze_lc = [i for i in range(0, 230, 1) if i % 11 == 0]
print(multiplos_de_onze_lc)

modelos = ["Atrium", "Attentus", "Bhaskara", "BigproddatA",
           "Corpus", "Fibonacci", "Fluxo de Caixa", "Formica",
           "Horobox", "Horoférias", "Horótimo", "Hurst",
           "Installation", "Moneta", "Mulcta", "Palete Caixa",
           "Productio", "Tecellarius", "Thermo", "Transdia"]

# Na forma trasicional
h_modelos = []
for i in modelos:
    if i.startswith("H"):
        h_modelos.append(i)
print(h_modelos)

# Na forma de List Comprehensions
h_modelos_lc = [i for i in modelos if i.startswith("H")]
print(h_modelos_lc)

# Limites Relativos ao Eixo H - Horizontal do Palete de Caixa
calculo_h = ["pertence", "pertence", "pertence", "não pertence",
             "pertence", "pertence", "não pertence"]

# Na forma trasicional
pontos_eixo_h = []
ponto = 0
for i in calculo_h:
    if i == "pertence":
        pontos_eixo_h.append(ponto)
    ponto = ponto + 1
print(pontos_eixo_h)


# Na forma de List Comprehensions
pontos_eixo_h_lc = [i for i in calculo_h if i == "pertence"]
print(pontos_eixo_h_lc)

