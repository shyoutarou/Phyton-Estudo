import math
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  a = []
  for item in x:
    a.append(1 / (1 + math.exp(-item)))
  return a

x = np.arange(-10., 10., 0.2)
print(x)
print(type(x))

sig = sigmoid(x)
sig = np.array(sig)
print(sig)
print(type(sig))

plt.plot(x,sig,
         color="g",
         marker="o",
         linestyle=":")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Sigmóide Iterável")
plt.grid()
plt.savefig("plot_funcao_sigmoide_iteravel_example.png")

plt.show()