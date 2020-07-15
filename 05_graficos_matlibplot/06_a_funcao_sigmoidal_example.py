import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

#definimos x como um vetor de valores que vai de -5 a 5
# em um intervalo de 0.5, ou seja, x = {-5 , -4.5, -4, -3.5, …
x = np.arange(-5, 5, 0.5)

print(x)
print(type(x))

sig = sigmoid(x)
sig = np.array(sig)
print(sig)
print(type(sig))

plt.plot(x, sig,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Sigmóide")
plt.grid()
plt.savefig("plot_funcao_sigmoide_example.png")
plt.show()

