import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

x = np.arange(-5, 5, 0.1)
a = 1
b = -2
c = -15

f = a * x ** 2 + b * x + c
g = 2 * a * x + b

plt.plot(x, f)
plt.plot(x, g)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Quadrática e sua Derivada")
plt.grid()
plt.legend(["f(x) = a * x ** 2 + b * x + c",
            "g(x) = f' (x) = 2 * a * x + b"])

plt.savefig("plot_multiplos_graficos_first_example.png")
plt.show()
