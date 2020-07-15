import numpy   as   np
import matplotlib.pyplot   as   plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.arange(0, 6, 0.1)
y = np.arange(0, 6, 0.1)

# np.meshgrid = Malha
[X, Y] = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2 - 6 * X - 6 * Y + 20

plt.close("all")
# plt.figure(i) = Figura (Gráfico) com índice i
figura = plt.figure(1)
# add_subplot = Tranformar o gráfico
# padrão 2-D em uma projeção 3-D
axes = figura.add_subplot(1, 1, 1, projection="3d")

# rstride = Distância na coordenada x
# cstride = Distância na coordenada y
# alpha = Espessura da linha
# wireframe = Estrutura em arame

axes.plot_wireframe(X, Y, Z,
                    color="b",
                    rstride=5,
                    cstride=5,
                    alpha=0.5)

axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")

plt.savefig("plot_ponto_minimo.png")

plt.show()
