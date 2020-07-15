# Plotar função :
# f(x) = sin(x), g(x) = cos(x),
# Dom[f(x}] = [0, 2 * pi]

import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(0, 2 * np.pi)

f = np.sin(x)
g = np.cos(x)

plt.plot(x, f)
plt.plot(x, g)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Multiplas \n Exercicio a")
plt.grid()
plt.legend(["f(x) = sin(x)",
            "g(x) = cos(x)"])

plt.savefig("plot_multiplos_graficos_exercicio_a.png")
plt.show()
