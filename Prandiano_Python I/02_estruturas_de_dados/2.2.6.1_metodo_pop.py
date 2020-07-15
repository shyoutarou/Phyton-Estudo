num_atendentes_necessarios = [60, 56, 57, 52, 45, 38, 44, 45, 40, 43]
print(num_atendentes_necessarios)

num_atendentes_necessarios.pop()
print(num_atendentes_necessarios)

num_atendentes_necessarios.pop()
print(num_atendentes_necessarios)

num_atendentes_necessarios.pop(5)
print(num_atendentes_necessarios)

num_atendentes_necessarios.pop(2)
print(num_atendentes_necessarios)

num_atendentes_necessarios.pop(-3)
print(num_atendentes_necessarios)

# Proposital. Erro porque ele tenta tirar uma lista enão um elemento
# num_de_atendentes_necessarios.pop([0, 3])
# print(num_de_atendentes_necessarios)
