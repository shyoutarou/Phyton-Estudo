# Plotar função : f(x) = exp(-x**2) (Gaussiana), Dom[f(x}] = [-5,5]

import numpy   as   np
import matplotlib.pyplot   as   plt

x = np.arange(-5, 5)
f = np.exp(-x ** 2)

plt.plot(x, f,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")

#plt.axis('square')

plt.title("Axis exercicio c")
plt.grid()
plt.savefig("plot_axis_exercico_c.png")
plt.show()
