# Plotar função :
# f(x) = sin(x), g(x) = sin(2x), h(x) = sin(50x)
# Dom[f(x}] = [0, 2 * pi]

import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(0, 2 * np.pi)

f = np.sin(x)
g = np.sin(2 * x)
h = np.sin(50 * x)

plt.plot(x, f)
plt.plot(x, g)
plt.plot(x, h)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Multiplas \n Exercicio c")
plt.grid()
plt.legend(["f(x) = sin(x)",
            "g(x) = sin(2 * x)",
            "h(x) = sin(50 * x)"])

plt.savefig("plot_multiplos_graficos_exercicio_c.png")
plt.show()