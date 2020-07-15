# Plotar função : f(x) = sqrt(x), Dom[f(x}] = [0,12]

import numpy   as   np
import matplotlib.pyplot   as   plt

x = np.arange(0, 12)
f = np.sqrt(x)

plt.plot(x, f,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")

plt.axis('normal')
plt.axis([0.2, 10, 0, np.pi])

plt.title("Axis exercicio a")
plt.grid()
plt.savefig("plot_axis_exercico_a.png")
plt.show()
