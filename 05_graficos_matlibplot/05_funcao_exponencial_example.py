import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01, 5, 0.1)
f = np.exp(x)
plt.plot(x, f,
         color="magenta",
         marker="^",
         linestyle="-.")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("plot_funcao_exponencial_example.png")
plt.show()
