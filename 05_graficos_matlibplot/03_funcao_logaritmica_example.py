import numpy   as   np
import matplotlib.pyplot   as   plt

x = np.arange(0.01, 5, 0.1)
f = np.log(x)
plt.plot(x, f,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Logaritmica")

plt.grid()
plt.savefig("plot_funcao_logaritmica_example.png")
plt.show()
