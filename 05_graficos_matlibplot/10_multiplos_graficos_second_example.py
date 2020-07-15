import numpy   as   np
import matplotlib.pyplot   as   plt

plt.close("all")

x = np.arange(-5, 5, 1)
a = 1
b = -2
c = -15
d = 0

f = a * x ** 3 + b * x ** 2 + c * x + d
g = 3 + a * x + 2 * b * x + c
h = 6 * a * x + 2 * b

plt.plot(x, f,
         color="green",
         marker="d",
         linestyle="-")

plt.plot(x, g,
         color="red",
         marker="h",
         linestyle="-.")

plt.plot(x, h,
         color="blue",
         marker="h",
         linestyle="--")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função do Terceiro Grau e suas Derivadas")
plt.grid()
plt.legend(["f(x) = a * x ** 3 + b * x ** 2 + c * x + d",
            "g(x) = f' (x) = 3 + a * x + 2 * b * x + c",
            "h(x) = g' (x) = 6 * a * x + 2 * b"])

plt.savefig("plot_multiplos_graficos_second_example.png")
plt.show()
