import numpy   as   np
import matplotlib.pyplot   as   plt

LI = 0
LS = 2 * np.pi
passo = 0.1
R = 5

#Alterar com os alunos o passo
# c = Origem O do circulo que desliza
c = np.arange(LI, LS, passo)

x = R * (c - np.sin(c))
y = R * (1 - np.cos(c))
plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Cicloide")
plt.grid()
plt.axis("equal")
plt.savefig("plot_polar_cicloide_example.png")

plt.show()
