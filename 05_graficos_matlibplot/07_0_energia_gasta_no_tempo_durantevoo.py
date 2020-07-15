import numpy   as   np
import matplotlib.pyplot   as   plt

# Foi colocado 0.1 para nçao dar divisão por zero na equação E
V = np.arange(0.1, 4, 0.1)
E = 1 / V + V ** 3

plt.plot(V, E,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Energia gasta No tempo durante Voo")
plt.grid()
plt.savefig("plot_energia_gasta_no_tempo_durantevoo.png")
plt.show()
