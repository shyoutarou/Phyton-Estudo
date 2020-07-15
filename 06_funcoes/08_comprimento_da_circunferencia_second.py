import numpy as np


def comprimento_da_circunferencia(raio):
    # Calcular o comprimento da circunferencia
    comprimento_da_circunferencia = 2 * np.pi * raio
    return comprimento_da_circunferencia


print(comprimento_da_circunferencia(5))
