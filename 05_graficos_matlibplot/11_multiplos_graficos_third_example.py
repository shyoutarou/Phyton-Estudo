import numpy   as   np
import matplotlib.pyplot   as   plt

plt.close("all")

x = np.arange(0, 2 * np.pi, 0.1)
f = np.sin(x)
g = np.cos(x)

f1 = np.sin(x) + 1
g1 = np.cos(x) - 1

plt.plot(x, f, x, g)
"""
plt.plot(x, f, x, g, 
         color="green",
         marker="d",
         linestyle="-")

"""

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Trigonométricas")
plt.grid()
plt.legend(["f(x) = sin(x)",
            "g(x) = cos(x)"])

plt.savefig("plot_multiplos_graficos_third_example.png")
plt.show()
