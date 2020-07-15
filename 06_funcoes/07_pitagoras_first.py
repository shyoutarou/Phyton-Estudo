import numpy as np

def pitagoras(catetol, cateto2):
    # Calcular Pitagoras
    pitagoras = np.sqrt(catetol ** 2 + cateto2 ** 2)
    return pitagoras

print(pitagoras(3, 4))
