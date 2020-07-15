import numpy   as   np
import matplotlib.pyplot as plt

plt.close("all")

# Foi colocado 0.01 para nçao dar divisão por zero na equação E
x = np.arange(0.01, 0.5 * np.pi, 0.1)
L = 1 / np.cos(x) + 1 / np.sin(x)

plt.plot(x, L,
         color="k",
         marker=">",
         linestyle="-")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Rampa Hélice Cilíndrica")
plt.grid()
plt.savefig("plot_helice_cilindrica_example.png")
plt.show()
