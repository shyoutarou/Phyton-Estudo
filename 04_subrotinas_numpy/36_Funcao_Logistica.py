import math
import numpy as np

"""
A função sigmóide pode ser calculada com o truque exp-normalize para 
evitar overflow numérico. No caso do sigmóide (x), temos uma distribuição 
com probabilidades de log não normalizadas [x, 0], onde estamos 
interessados apenas na probabilidade do primeiro evento. A partir da 
identidade exp-normalize, sabemos que as distribuições [x, 0] e [0, −x] 
são equivalentes (para ver por que, insira b = max (0, x)). É por isso que 
o sigmoide geralmente é expresso de uma das duas maneiras equivalentes:
sigmoid(x)=1/(1+exp(−x))=exp(x)/(exp(x)+1)
Curiosamente, cada versão cobre um caso extremo: x = ∞ e x = −∞, respectivamente. 
Abaixo está um código python que implementa o truque:
"""
def sigmoid(x):
  "Numerically-stable sigmoid function."
  if x >= 0:
    z = math.exp(-x)
    return 1 / (1 + z)
  else:
    z = math.exp(x)
    return z / (1 + z)

def sigmoid_np(x):
  return math.exp(-np.logaddexp(0, -x))

# Em geral, o sigmóide logístico multinomial é:
def nat_to_exp(q):
    max_q = max(0.0, np.max(q))
    rebased_q = q - max_q
    return np.exp(rebased_q - np.logaddexp(-max_q, np.logaddexp.reduce(rebased_q)))

print(sigmoid(1.10)) # 0.7502601055951177
print(sigmoid(1.00)) # 0.7310585786300049
print(sigmoid(0.90)) # 0.7109495026250039
print(sigmoid(0.70)) # 0.6681877721681662
print(sigmoid(0.50)) # 0.6224593312018546
print(sigmoid(2.31)) # 0.9097018552970803
print(sigmoid(-1.89)) # 0.13124446943852333
print("==========sigmoid_np=============")
print(sigmoid_np(1.10)) # 0.7502601055951176
print(sigmoid_np(1.00)) # 0.7310585786300049
print(sigmoid_np(0.90)) # 0.7109495026250039
print(sigmoid_np(0.70)) # 0.6681877721681662
print(sigmoid_np(0.50)) # 0.6224593312018546
print(sigmoid_np(2.31)) # 0.9097018552970801
print(sigmoid_np(-1.89)) # 0.13124446943852333
print("==========nat_to_exp=============")
print(nat_to_exp(1.10)) # 0.7502601055951176
print(nat_to_exp(1.00)) # 0.7310585786300049
print(nat_to_exp(0.90)) # 0.7109495026250039
print(nat_to_exp(0.70)) # 0.6681877721681662
print(nat_to_exp(0.50)) # 0.6224593312018546
print(nat_to_exp(2.31)) # 0.9097018552970801
print(nat_to_exp(-1.89)) # 0.13124446943852333