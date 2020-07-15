import numpy as np
import matplotlib.pyplot as plt

# a = input("Digite valor de 'a'": )
# a = float(a)
a = 3

# b = input("Digite valor de 'b'": )
# b = float(b)
b = -1

x = np.arange(0, 10, 0.01)
print(x)        # [0.   0.01 0.02 0.03 .....
print(type(x))  # <class 'numpy.ndarray'>

f = a * x + b
print(f)        # [-1.000e+00 -9.700e-01 -9.400e-01 -9.100e-01 -8.800e-01 -8.500e-01
print(type(f))  # <class 'numpy.ndarray'>

plt.plot(x, f,
         color="y",
         marker="v",
         linestyle="-.")
plt.xlabel("x")
plt.ylabel("f")
plt.title("Função Linear")
plt.grid()
plt.savefig("plot_funcao_linear_example.png")
plt.show()