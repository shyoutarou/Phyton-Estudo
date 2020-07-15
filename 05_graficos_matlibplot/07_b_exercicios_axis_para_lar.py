# Plotar função : f(x) = tag(x), Dom[f(x}] = [0,2Pi]

import numpy   as   np
import matplotlib.pyplot   as   plt

x = np.arange(0, 2 * np.pi)
f = np.tan(x)

plt.plot(x, f,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")

# plt.axis('square')

plt.title("Axis exercicio b")
plt.grid()
plt.savefig("plot_axis_exercico_b.png")
plt.show()
