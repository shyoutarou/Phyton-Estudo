import numpy   as   np
import matplotlib.pyplot   as   plt

plt.close("all")

meses = ["Jan", "Fev", "Marc", "Abr",
         "Mai", "Jun", "Jul", "Ago",
         "Set", "Out", "Nov", "Dez"]

qtde_colaboradores = [566, 512, 571, 578,
                      515, 533, 596, 535,
                      548, 592, 574, 576]

valores_x = np.arange(1, 13, 1)

plt.bar(valores_x, qtde_colaboradores)

plt.xlabel("Meses")
plt.ylabel("Qtde")
plt.title("Quantidade Colaboradores")

# Fica ruim com barras
# plt.grid()

plt.savefig("plot_bar_first_example.png")
plt.show()
