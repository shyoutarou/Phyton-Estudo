# Plotar função : f(x) = exp(sin(x**2))

import numpy   as   np
import matplotlib.pyplot   as   plt

x = np.arange(-5, 5)
f = np.sin(x ** 2)

plt.plot(x, f,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")

#plt.axis('square')

plt.title("Axis exercicio e")
plt.grid()
plt.savefig("plot_axis_exercico_e.png")
plt.show()