# Plotar função :
# f(x) = sqrt(x), g(x) = x ** (1/3), h(x) = x ** (1/4)
# Dom[f(x}] = [0, 5]

import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(0, 5)

f = x ** (1/2)
g = x ** (1/3)
h = x ** (1/4)

plt.plot(x, f)
plt.plot(x, g)
plt.plot(x, h)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Multiplas \n Exercicio d")
plt.grid()
plt.legend(["f(x) = x ** (1/2)",
            "g(x) = x ** (1/3)",
            "h(x) = x ** (1/4)"])

plt.savefig("plot_multiplos_graficos_exercicio_d.png")
plt.show()