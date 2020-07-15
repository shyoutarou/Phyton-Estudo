# Plotar função : f(x) = sin(x), Dom[f(x}] = [-50,50] e Im[f(x}] = [-50,50]

import numpy   as   np
import matplotlib.pyplot   as   plt

x = np.arange(-50, 50)
f = np.sin(x)

plt.plot(x, f,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")

#plt.axis('square')

plt.title("Axis exercicio d")
plt.grid()
plt.savefig("plot_axis_exercico_d.png")
plt.show()