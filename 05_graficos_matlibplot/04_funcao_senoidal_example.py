import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.1)
print(x)
print(type(x))

f = np.sin(x)
print(f)
print(type(f))

plt.plot(x, f,
         color="c",
         marker="+",
         linestyle="-.")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Senoidal")
plt.grid()
plt.savefig("plot_funcao_senoidal_example.png")
plt.show()
