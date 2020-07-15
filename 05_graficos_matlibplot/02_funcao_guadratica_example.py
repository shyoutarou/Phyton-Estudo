import numpy as np
import matplotlib.pyplot as plt

a = -1
b = -2
c = -15

x = np.arange(-10, 10, 0.01)
print(x)
print(type(x))

f = a * x ** 2 + b * x + c
print(f)
print(type(f))

plt.plot(x, f,
         color="g",
         marker="*",
         linestyle="--")
plt.xlabel("x")
plt.ylabel("f")
plt.title("Função Quadrática")
plt.grid()
plt.savefig("plot_funcao_quadratica_example.png")
plt.show()
