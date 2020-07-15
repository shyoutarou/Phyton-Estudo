import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x, a, c):
    return 1 / (1 + np.exp(-a * (x - c)))


def sigmf(x, b, c):
    """
    The basic sigmoid membership function generator.
    Parameters
    ----------
    x : 1d array
        Data vector for independent variable.
    b : float
        Offset or bias.  This is the center value of the sigmoid, where it
        equals 1/2.
    c : float
        Controls 'width' of the sigmoidal region about `b` (magnitude); also
        which side of the function is open (sign). A positive value of `a`
        means the left side approaches 0.0 while the right side approaches 1.;
        a negative value of `c` means the opposite.
    Returns
    -------
    y : 1d array
        Generated sigmoid values, defined as y = 1 / (1. + exp[- c * (x - b)])
    Notes
    -----
    These are the same values, provided separately and in the opposite order
    compared to the publicly available MathWorks' Fuzzy Logic Toolbox
    documentation. Pay close attention to above docstring!
    """
    return 1. / (1. + np.exp(- c * (x - b)))



# definimos x como um vetor de valores que vai de -5 a 5
# em um intervalo de 0.5, ou seja, x = {-5 , -4.5, -4, -3.5, …
x = np.arange(-6, 6.5, 0.5)
print(x)
print(type(x))

sig = sigmf(x,1.1,0.5)
sig = np.array(sig)
print(sig)
print(type(sig))

plt.plot(x, sig,
         color="g",
         marker="o",
         linestyle=":")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Sigmóide Ponto médio")
plt.grid()
plt.savefig("plot_funcao_sigmoide_ptomedio_example.png")
plt.show()

"""
x = 0:0.5:20 //definimos x como um vetor de valores que vai de 0 a 20 em um intervalo de 0.5, ou seja, x = {0 , 0.5, 1, 1.5, … , 19.5, 20}
s1 = sigmf(x,[1 5]) // s1 será uma sigmoid cujo centro é no 5
s2 = sigmf(x,[0.5 5]) // s2 será uma sigmoid cujo centro é no 5, porém com uma inclinação mais suave que anterior
s3 = sigmf(x,[0.5 10]) // s3 será uma sigmoid cujo centro é no 10, com a mesma inclinação que anterior 
plot(x,s1) 
plot(x,s2)
plot(x,s3)

"""
