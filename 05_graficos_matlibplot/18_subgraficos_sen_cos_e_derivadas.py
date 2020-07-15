import numpy   as   np
import matplotlib.pyplot   as   plt

plt.close("all")

x = np.arange(0, 2 * np.pi, 0.01)

y = np.sin(x)
y_linha = np.cos(x)
y_duas_linhas = - np.sin(x)

x_dois = np.arange(-5, 5, 0.1)

g = x_dois ** 3 - 4 * x_dois ** 2 - 4 * x_dois + 16
g_linha = 3 * x_dois ** 2 - 8 * x_dois - 4
g_linha_dois = 6 * x_dois - 8

# figura = Figura que armazena o arranjo com os subgráficos
# sharex = True (compartilhar o eixo x )
# sharey = True (compartilhar o eixo y )
[figura, subgraficos] = plt.subplots(nrows=3, ncols=2, sharex=False, sharey=False)

subgraficos[0, 0].plot(x, y)
subgraficos[0, 0].set_ylabel("sin(x)")
subgraficos[0, 0].grid()

subgraficos[1, 0].plot(x, y_linha)
subgraficos[1, 0].set_ylabel("cos(x)")
subgraficos[1, 0].grid()

subgraficos[2, 0].plot(x, y_duas_linhas)
subgraficos[2, 0].set_xlabel("x")
subgraficos[2, 0].set_ylabel("- sin(x)")
subgraficos[2, 0].grid()

subgraficos[0, 1].plot(x_dois, g,
                       color='g',
                       linestyle="--")
subgraficos[0, 1].set_ylabel("g(x)")
subgraficos[0, 1].grid()

subgraficos[1, 1].plot(x_dois, g_linha,
                       color='m',
                       linestyle="-.")
subgraficos[1, 1].set_ylabel("g'(x)")
subgraficos[1, 1].grid()

subgraficos[2, 1].plot(x_dois, g_linha_dois,
                       color='r',
                       linestyle=":")
subgraficos[2, 1].set_xlabel("x")
subgraficos[2, 1].set_ylabel("g''(x)")
subgraficos[2, 1].grid()

figura.subplots_adjust(hspace=0)
plt.savefig("plot_subgraficos_sen_cos.png")
plt.show()
