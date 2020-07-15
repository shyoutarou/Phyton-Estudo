import numpy   as   np
import matplotlib.pyplot   as   plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from  matplotlib.ticker import LinearLocator, FormatStrFormatter

x = np.arange(0, 6, 0.5)
y = np.arange(0, 8, 0.5)

# np.meshgrid = Malha
[X, Y] = np.meshgrid(x, y)
Z = - X ** 2 - Y ** 2 + 6 * X + 6 * Y

plt.close("all")
# plt.figure(i) = Figura (Gráfico) com índice i
figura = plt.figure(1)
# add_subplot = Tranformar o gráfico
# padrão 2-D em uma projeção 3-D
axes = figura.gca(projection="3d")

# cmap = Superficie
# cm.jet
# cm.coolwarm
# cm.gist_rainbow ou cm.rainbow
# antialiased = Ajuste (spline)
surf = axes.plot_surface(X, Y, Z,
                    cmap = cm.gist_rainbow,
                    linewidth = 0,
                    antialiased=True)

axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")

z_min = 0
z_max = 15
# zlim = limites do eixo z
axes.set_zlim(z_min, z_max)

# LinearLocator(c) = Número de divisões do eixo z
axes.zaxis.set_major_locator(LinearLocator(10))
# Formatar os números do eixo z
axes.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))

# shrik = Tamanho da barra de cores
# aspect = Espessura da barra decores
figura.colorbar(surf, shrink = 0.5, aspect = 10)

plt.savefig("plot_ponto_maximo_surface.png")

plt.show()
