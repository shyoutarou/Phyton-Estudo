import numpy   as   np
import matplotlib.pyplot   as   plt

R = 5
theta = np.arange(0, 2 * np.pi, 0.01)

x = R * np.cos(theta)
y = R * np.sin(theta)
plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Circulo")
plt.grid()
plt.axis("equal")
plt.savefig("plot_polar_circulo_example.png")

plt.show()
