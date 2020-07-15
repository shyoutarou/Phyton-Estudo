# Não usei <pi>, trata-se de uma palavra reservada pelo Python
const_pi = 3.1415
const_e = 2.7182
const_Y = 0.5772
const_phi = 1.6180

consts_mais_usadas = [const_pi, const_e, const_Y, const_phi]
print(type(consts_mais_usadas))
print(consts_mais_usadas)

const_delta = 4.6692 # Feigenbaum
const_alpha = 2.5029 # Feingenbaum
const_K = 0.9160 # Catalan
const_mu = 1.4514 # Ramanujan-Soldner
const_L = 0.1100 # Louville

demais_consts = [const_delta, const_alpha, const_K, const_mu, const_L]
print(type(demais_consts))
print(demais_consts)

# se usar append, ele vai adicionar mais um elemento,
# que vai ser a lista demais_consts. Ou seja, ele não
# adiciona cada elemento da lista
consts_mais_usadas.extend(demais_consts)
print(type(consts_mais_usadas))
print(consts_mais_usadas)

vector_a = [1, 5, 7, 9]
vector_b = [6, -1, 4]

# operador "+" para lista faz um extend
vector_c = vector_a + vector_b
print(type(vector_c))
print(vector_c) # [1, 5, 7, 9, 6, -1, 4]

