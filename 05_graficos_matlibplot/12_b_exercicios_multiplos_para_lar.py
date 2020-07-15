# Plotar função :
# # f(x) = sin(x), g(x) = 2sin(x), h(x) = sin(2x)
# # Dom[f(x}] = [0, 2 * pi]

import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(0, 2 * np.pi)

f = np.sin(x)
g = 2 * np.sin(x)
h = np.sin(2 * x)

plt.plot(x, f)
plt.plot(x, g)
plt.plot(x, h)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Multiplas \n Exercicio b")
plt.grid()
plt.legend(["f(x) = sin(x)",
            "g(x) = 2 * sin(x)",
            "h(x) = sin(2 * x)"])

plt.savefig("plot_multiplos_graficos_exercicio_b.png")
plt.show()