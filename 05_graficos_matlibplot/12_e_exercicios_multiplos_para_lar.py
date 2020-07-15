# Plotar função :
# f(x) = sqrt(x), g(x) = sqrt(x) ** 3, h(x) = sqrt(x) ** 4
# Dom[f(x}] = [-5, 5]

import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(-5, 5)

# RuntimeWarning: invalid value encountered in power
# Problema de número negatico, complexos
# f = np.sqrt(x)
# g = x ** (1/3)
# h = x ** (1/4)

f = (np.abs(x)) ** (1 / 2)
g = (np.abs(x)) ** (1 / 3)
h = (np.abs(x)) ** (1 / 4)

plt.plot(x, f)
plt.plot(x, g)
plt.plot(x, h)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Multiplas \n Exercicio e")
plt.grid()
plt.legend(["f(x) = x ** (1/2)",
            "g(x) = x ** (1/3)",
            "h(x) = x ** (1/4)"])

plt.savefig("plot_multiplos_graficos_exercicio_e.png")
plt.show()